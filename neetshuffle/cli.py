#!/usr/bin/env python3
"""neetshuffle - a daily, topic-blind NeetCode 150 problem shuffler.

Philosophy: problems are ALWAYS shown topic-blind. You get them jumbled across
every category so you can't lean on "oh this is the sliding-window section" and
pattern-match your way through -- you have to actually recognise the problem.

Topics only ever surface in `stats` and in the Notion mirror, and only for
problems you've already solved -- a retrospective view of where your reps have
gone, which can't help you pattern-match a problem you haven't done yet.
"""

import argparse
import datetime
import hashlib
import json
import os
import random
import re
import secrets
import sys
import tempfile
import time

from . import notion
from .problems import NEETCODE_150, gist_for, url_for

DEFAULT_COUNT = 4
MIN_COUNT = 1
MAX_COUNT = 25  # sanity cap so a typo can't request the whole list
STATE_VERSION = 1
APP_NAME = "neetshuffle"

# Map slug -> (name, topic) once, so lookups are O(1) and the canonical
# ordering of NEETCODE_150 is the source of truth for valid slugs.
_BY_SLUG = {slug: (name, topic) for (name, slug, topic) in NEETCODE_150}
ALL_SLUGS = [slug for (_, slug, _) in NEETCODE_150]
TOPICS = []  # distinct topics, in canonical order
for _name, _slug, _topic in NEETCODE_150:
    if _topic not in TOPICS:
        TOPICS.append(_topic)

# Topic -> total problem count.
TOPIC_TOTALS = {}
for _name, _slug, _topic in NEETCODE_150:
    TOPIC_TOTALS[_topic] = TOPIC_TOTALS.get(_topic, 0) + 1


def _normalize_name(text):
    """Lowercase, strip everything but alphanumerics -- so "Two Sum II",
    "two-sum-ii" and "twosumii" all collapse to the same key."""
    return re.sub(r"[^a-z0-9]", "", text.lower())


# Lookups for matching imported problems.
_NAME_TO_SLUG = {_normalize_name(name): slug for (name, slug, _) in NEETCODE_150}
_NORMSLUG_TO_SLUG = {_normalize_name(slug): slug for slug in ALL_SLUGS}


# --------------------------------------------------------------------------
# State storage
# --------------------------------------------------------------------------

def default_state_path():
    """Where progress lives. Override with $NEETSHUFFLE_FILE.

    Default follows XDG so an installed/packaged copy never tries to write
    into a read-only site-packages dir."""
    env = os.environ.get("NEETSHUFFLE_FILE")
    if env:
        return os.path.abspath(os.path.expanduser(env))
    base = os.environ.get("XDG_DATA_HOME") or os.path.expanduser("~/.local/share")
    return os.path.join(base, APP_NAME, "progress.json")


def new_state():
    # secrets gives a cryptographically strong, per-install salt. Combined with
    # the date (and reroll nonce) it makes the daily draw reproducible within a
    # day but unpredictable across installs/days -> the jumble can't be foreseen.
    return {
        "version": STATE_VERSION,
        "salt": secrets.token_hex(16),
        "done": [],          # slugs solved (never drawn again)
        "solved_at": {},     # slug -> ISO date (may be None if unknown)
        "today": None,       # {"date", "slugs", "done", "nonce"}
        "revise": [],        # slugs flagged for revision (may include solved)
        "revise_set": None,  # current practice draw: {"slugs", "done"}
    }


def load_state(path):
    if not os.path.exists(path):
        return new_state()
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError, ValueError) as exc:
        # Never silently lose data: keep a backup of the unreadable file.
        backup = path + ".corrupt"
        try:
            os.replace(path, backup)
            warn("progress file was unreadable (%s); backed it up to %s and "
                 "started fresh." % (exc, backup))
        except OSError:
            warn("progress file was unreadable (%s); starting fresh." % exc)
        return new_state()
    return _sanitize_state(data)


def _sanitize_state(data):
    """Validate/coerce loaded data so a hand-edited or garbled file can't crash
    us or smuggle in bogus slugs."""
    if not isinstance(data, dict):
        warn("progress file had an unexpected shape; starting fresh.")
        return new_state()

    state = new_state()
    if isinstance(data.get("salt"), str) and data["salt"]:
        state["salt"] = data["salt"]

    valid = set(ALL_SLUGS)
    done = data.get("done", [])
    if isinstance(done, list):
        seen = set()
        clean = []
        for s in done:
            if isinstance(s, str) and s in valid and s not in seen:
                seen.add(s)
                clean.append(s)
        state["done"] = clean

    solved_at = data.get("solved_at", {})
    if isinstance(solved_at, dict):
        state["solved_at"] = {
            s: v for s, v in solved_at.items()
            if s in set(state["done"]) and (v is None or isinstance(v, str))
        }

    today = data.get("today")
    if isinstance(today, dict):
        date = today.get("date")
        slugs = today.get("slugs")
        tdone = today.get("done", [])
        nonce = today.get("nonce", 0)
        if (isinstance(date, str)
                and isinstance(slugs, list)
                and all(isinstance(s, str) and s in valid for s in slugs)):
            tdone = [s for s in tdone if isinstance(s, str) and s in slugs] \
                if isinstance(tdone, list) else []
            state["today"] = {
                "date": date,
                "slugs": slugs,
                "done": tdone,
                "nonce": nonce if isinstance(nonce, int) else 0,
            }

    revise = data.get("revise", [])
    if isinstance(revise, list):
        seen = set()
        clean = []
        for s in revise:
            if isinstance(s, str) and s in valid and s not in seen:
                seen.add(s)
                clean.append(s)
        state["revise"] = clean

    rset = data.get("revise_set")
    if isinstance(rset, dict):
        slugs = rset.get("slugs")
        rdone = rset.get("done", [])
        if isinstance(slugs, list) and all(
                isinstance(s, str) and s in valid for s in slugs):
            rdone = [s for s in rdone if isinstance(s, str) and s in slugs] \
                if isinstance(rdone, list) else []
            state["revise_set"] = {"slugs": slugs, "done": rdone}
    return state


def _atomic_write_json(path, obj):
    """Atomic, owner-only JSON write (temp file + rename)."""
    directory = os.path.dirname(path) or "."
    os.makedirs(directory, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=directory, prefix=".tmp-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(obj, fh, indent=2, sort_keys=True)
            fh.write("\n")
            fh.flush()
            os.fsync(fh.fileno())
        try:
            os.chmod(tmp, 0o600)  # this data is yours alone
        except OSError:
            pass
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def save_state(path, state):
    _atomic_write_json(path, state)


# --------------------------------------------------------------------------
# Config storage (Notion settings live here, separate from progress)
# --------------------------------------------------------------------------

def config_path():
    env = os.environ.get("NEETSHUFFLE_CONFIG")
    if env:
        return os.path.abspath(os.path.expanduser(env))
    base = os.environ.get("XDG_CONFIG_HOME") or os.path.expanduser("~/.config")
    return os.path.join(base, APP_NAME, "config.json")


def load_config():
    path = config_path()
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError, ValueError):
        warn("config file was unreadable; ignoring it.")
        return {}


def save_config(config):
    _atomic_write_json(config_path(), config)


def notion_token(config):
    """Resolve the Notion token. Environment wins so it never has to be written
    to disk; fall back to a token saved in config if the user chose to."""
    return (os.environ.get("NEETSHUFFLE_NOTION_TOKEN")
            or config.get("notion", {}).get("token"))


# --------------------------------------------------------------------------
# Core logic
# --------------------------------------------------------------------------

def today_str():
    return datetime.date.today().isoformat()


def remaining_slugs(state):
    done = set(state["done"])
    return [s for s in ALL_SLUGS if s not in done]


def mark_solved(state, slug, date):
    """Record a solved problem (idempotent). Also flags it done in today's set
    if it happens to be in there, so the listing shows the ✓."""
    if slug not in state["done"]:
        state["done"].append(slug)
    # Only set/overwrite the date if we don't already have a real one.
    if date is not None or slug not in state["solved_at"]:
        state["solved_at"][slug] = date
    day = state.get("today")
    if day and slug in day.get("slugs", []) and slug not in day.get("done", []):
        day.setdefault("done", []).append(slug)


def draw_set(state, count, date, nonce):
    """Deterministically draw `count` unsolved problems.

    Seed = sha256(salt + date + nonce). Same install + same day + same nonce ->
    same draw, so the set is stable through the day; bumping the nonce (reroll)
    yields a genuinely different jumble. The salt keeps it all unguessable."""
    pool = remaining_slugs(state)
    if not pool:
        return []
    count = max(MIN_COUNT, min(count, len(pool)))

    seed_material = "{}|{}|{}".format(state["salt"], date, nonce).encode("utf-8")
    seed = int.from_bytes(hashlib.sha256(seed_material).digest(), "big")
    rng = random.Random(seed)

    shuffled = pool[:]
    rng.shuffle(shuffled)
    return shuffled[:count]


def ensure_today(state, count, force=False):
    """Return today's set, creating it if needed. force=True redraws with a
    bumped nonce so reroll actually changes the set."""
    date = today_str()
    cur = state["today"]
    if not force and cur and cur.get("date") == date and cur.get("slugs"):
        return cur

    nonce = 0
    if force and cur and cur.get("date") == date:
        nonce = int(cur.get("nonce", 0)) + 1

    slugs = draw_set(state, count, date, nonce)
    state["today"] = {"date": date, "slugs": slugs, "done": [], "nonce": nonce}
    return state["today"]


# --------------------------------------------------------------------------
# Presentation
# --------------------------------------------------------------------------

def warn(msg):
    print("⚠️  " + msg, file=sys.stderr)


def fail(msg, code=1):
    print("Error: " + msg, file=sys.stderr)
    sys.exit(code)


def _reveal(slug):
    """Print the topic and optimal-approach gist for a just-solved problem."""
    _name, topic = _BY_SLUG[slug]
    print("   Topic:   {}".format(topic))
    gist = gist_for(slug)
    if gist:
        print("   Optimal: {}".format(gist))


def print_today(state):
    day = state["today"]
    slugs = day["slugs"]
    done = set(day.get("done", []))

    if not slugs:
        print("🎉 You've solved every NeetCode 150 problem. Nothing left to draw!")
        print("   Run `neetshuffle reset` if you want to start over.")
        return

    print("📅 {}  —  today's jumble ({} problem{})".format(
        day["date"], len(slugs), "" if len(slugs) == 1 else "s"))
    print("   Topics are hidden on purpose. Figure out the approach yourself.\n")

    for i, slug in enumerate(slugs, start=1):
        name, _topic = _BY_SLUG[slug]
        mark = "✓" if slug in done else " "
        print("  [{}] {}. {}".format(mark, i, name))
        print("        {}".format(url_for(slug)))
    print()

    left = len(slugs) - len(done)
    if left == 0:
        print("All done for today. Come back tomorrow for a fresh jumble. 💪")
    else:
        print("Solve them, then run:  neetshuffle done <number>   "
              "({} left today)".format(left))


def cmd_today(state, path, args):
    count = args.count if args.count is not None else DEFAULT_COUNT
    ensure_today(state, count)
    save_state(path, state)
    print_today(state)


def cmd_reroll(state, path, args):
    count = args.count if args.count is not None else DEFAULT_COUNT
    ensure_today(state, count, force=True)
    save_state(path, state)
    print("🔀 Drew a fresh set for today.\n")
    print_today(state)


def cmd_done(state, path, args):
    date = today_str()
    day = state["today"]
    if not day or day.get("date") != date or not day.get("slugs"):
        fail("no problems drawn for today yet. Run `neetshuffle today` first.")

    n = args.number
    slugs = day["slugs"]
    if n < 1 or n > len(slugs):
        fail("pick a number between 1 and {}.".format(len(slugs)))

    slug = slugs[n - 1]
    name, _topic = _BY_SLUG[slug]

    if slug in day.get("done", []):
        print("Already marked done: {}".format(name))
        return

    mark_solved(state, slug, date)
    save_state(path, state)

    # Now that you've solved it, reveal the topic + optimal approach as a
    # post-solve learning beat (it's hidden only *before* you solve).
    print("✓ Marked done: {}".format(name))
    _reveal(slug)
    left = len(slugs) - len(day["done"])
    if left == 0:
        print("That's the whole set. Nice work today. 🎯")
    else:
        print("{} left in today's jumble.".format(left))

    _maybe_auto_sync(state, [slug])


def cmd_import(state, path, args):
    """Bulk-mark already-solved problems from a file (or stdin).

    Each line may be a LeetCode URL, a problem slug, or a problem name. Blank
    lines and lines starting with '#' are ignored."""
    source = args.source
    try:
        if source == "-":
            text = sys.stdin.read()
        else:
            with open(os.path.expanduser(source), "r", encoding="utf-8") as fh:
                text = fh.read()
    except OSError as exc:
        fail("could not read {}: {}".format(source, exc))

    date = args.date or today_str()
    matched, already, unknown = [], [], []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        slug = _resolve_to_slug(line)
        if slug is None:
            unknown.append(line)
        elif slug in state["done"]:
            already.append(slug)
        else:
            mark_solved(state, slug, date)
            matched.append(slug)

    save_state(path, state)

    print("Imported {} newly-solved, {} already known, {} unrecognised.".format(
        len(matched), len(already), len(unknown)))
    for slug in matched:
        print("  ✓ {}".format(_BY_SLUG[slug][0]))
    if unknown:
        print("\nCouldn't match these (not in NeetCode 150, or typo):")
        for line in unknown:
            print("  ? {}".format(line))
    if matched:
        _maybe_auto_sync(state, matched)


def _resolve_to_slug(token):
    """Turn a URL / slug / name into a known slug, or None."""
    token = token.strip()
    m = re.search(r"leetcode\.com/problems/([a-z0-9\-]+)", token, re.I)
    if m:
        cand = m.group(1).lower()
        if cand in _BY_SLUG:
            return cand
        return _NORMSLUG_TO_SLUG.get(_normalize_name(cand))
    if token in _BY_SLUG:                       # exact slug
        return token
    norm = _normalize_name(token)
    return _NORMSLUG_TO_SLUG.get(norm) or _NAME_TO_SLUG.get(norm)


def cmd_stats(state, path, args):
    total = len(ALL_SLUGS)
    done_slugs = state["done"]
    done = len(done_slugs)
    pct = (done / total * 100) if total else 0
    bar_len = 30
    filled = int(bar_len * done / total) if total else 0
    bar = "█" * filled + "░" * (bar_len - filled)

    print("NeetCode 150 progress")
    print("  [{}] {}/{}  ({:.1f}%)".format(bar, done, total, pct))
    print("  Remaining: {}".format(total - done))
    if state["today"] and state["today"].get("date") == today_str():
        d = state["today"]
        print("  Today: {}/{} solved".format(
            len(d.get("done", [])), len(d.get("slugs", []))))

    # Topic-wise breakdown of SOLVED problems only -- retrospective, never
    # shown before you finish a problem, so it can't help you pattern-match.
    print("\nBy topic (solved / total):")
    done_set = set(done_slugs)
    per_topic_done = {t: 0 for t in TOPIC_TOTALS}
    for _name, slug, topic in NEETCODE_150:
        if slug in done_set:
            per_topic_done[topic] += 1

    width = max(len(t) for t in TOPIC_TOTALS)
    for topic, tot in TOPIC_TOTALS.items():
        d = per_topic_done[topic]
        seg = 12
        f = int(seg * d / tot) if tot else 0
        mini = "█" * f + "░" * (seg - f)
        print("  {:<{w}}  {}  {:>2}/{:<2}".format(topic, mini, d, tot, w=width))


def cmd_reset(state, path, args):
    if not args.yes:
        try:
            ans = input("This wipes ALL progress. Type 'yes' to confirm: ")
        except (EOFError, KeyboardInterrupt):
            print()
            fail("aborted.")
        if ans.strip().lower() != "yes":
            fail("aborted.")
    save_state(path, new_state())
    print("Progress reset. Fresh start. 🌱")


# --------------------------------------------------------------------------
# Revision list
# --------------------------------------------------------------------------

def _resolve_ref(state, token):
    """Resolve a problem reference to a slug. A bare integer means "problem #n
    in today's set"; otherwise it's treated as a slug / name / LeetCode URL."""
    token = token.strip()
    if token.isdigit():
        day = state.get("today")
        if day and day.get("slugs"):
            i = int(token)
            if 1 <= i <= len(day["slugs"]):
                return day["slugs"][i - 1]
        return None
    return _resolve_to_slug(token)


def cmd_revise_add(state, path, args):
    added, dup, unknown = [], [], []
    for ref in args.refs:
        slug = _resolve_ref(state, ref)
        if slug is None:
            unknown.append(ref)
        elif slug in state["revise"]:
            dup.append(slug)
        else:
            state["revise"].append(slug)
            added.append(slug)
    save_state(path, state)
    print("Added {} to revision ({} already listed, {} unrecognised).".format(
        len(added), len(dup), len(unknown)))
    for s in added:
        print("  + {}".format(_BY_SLUG[s][0]))
    for u in unknown:
        print("  ? {}".format(u))


def cmd_revise_remove(state, path, args):
    removed, missing = [], []
    for ref in args.refs:
        slug = _resolve_ref(state, ref)
        if slug and slug in state["revise"]:
            state["revise"].remove(slug)
            removed.append(slug)
        else:
            missing.append(ref)
    save_state(path, state)
    print("Removed {} from revision.".format(len(removed)))
    for s in removed:
        print("  - {}".format(_BY_SLUG[s][0]))
    for m in missing:
        print("  ? not on the list: {}".format(m))


def cmd_revise_list(state, path, args):
    rev = state["revise"]
    if not rev:
        print("Revision list is empty.")
        print("Add with:  neetshuffle revise add <today-number | name | url>")
        return
    print("📝 Revision list ({} problem{}):".format(
        len(rev), "" if len(rev) == 1 else "s"))
    for i, slug in enumerate(rev, start=1):
        print("  {}. {}".format(i, _BY_SLUG[slug][0]))
        print("       {}".format(url_for(slug)))
    print("\nPractice them with:  neetshuffle revise draw")


def cmd_revise_clear(state, path, args):
    n = len(state["revise"])
    state["revise"] = []
    state["revise_set"] = None
    save_state(path, state)
    print("Cleared {} problem(s) from revision.".format(n))


def cmd_revise_draw(state, path, args):
    rev = state["revise"]
    if not rev:
        fail("revision list is empty. Add problems first: "
             "neetshuffle revise add ...")
    count = args.count if args.count is not None else min(DEFAULT_COUNT, len(rev))
    count = max(MIN_COUNT, min(count, len(rev)))

    # A fresh shuffle each time (revision practice isn't tied to the calendar).
    pool = rev[:]
    random.SystemRandom().shuffle(pool)
    slugs = pool[:count]
    state["revise_set"] = {"slugs": slugs, "done": []}
    save_state(path, state)

    print("🔁 Revision set ({} problem{}) — topics still hidden:\n".format(
        len(slugs), "" if len(slugs) == 1 else "s"))
    for i, slug in enumerate(slugs, start=1):
        print("  [ ] {}. {}".format(i, _BY_SLUG[slug][0]))
        print("        {}".format(url_for(slug)))
    print("\nWhen solved:  neetshuffle revise done <number>")


def cmd_revise_done(state, path, args):
    rset = state.get("revise_set")
    if not rset or not rset.get("slugs"):
        fail("no revision set drawn yet. Run `neetshuffle revise draw` first.")

    n = args.number
    slugs = rset["slugs"]
    if n < 1 or n > len(slugs):
        fail("pick a number between 1 and {}.".format(len(slugs)))

    slug = slugs[n - 1]
    name = _BY_SLUG[slug][0]
    if slug in rset.get("done", []):
        print("Already revised: {}".format(name))
        return

    rset.setdefault("done", []).append(slug)
    # Revising it clears it from the revision list; re-add any time you want
    # another pass.
    if slug in state["revise"]:
        state["revise"].remove(slug)
    save_state(path, state)

    print("✓ Revised: {}".format(name))
    _reveal(slug)
    left = len(slugs) - len(rset["done"])
    if left == 0:
        print("Revision set complete. 🔁")
    else:
        print("{} left in this revision set.".format(left))


def cmd_revise(state, path, args):
    action = getattr(args, "revise_action", None)
    handlers = {
        "add": cmd_revise_add,
        "remove": cmd_revise_remove,
        "list": cmd_revise_list,
        "clear": cmd_revise_clear,
        "draw": cmd_revise_draw,
        "done": cmd_revise_done,
    }
    handlers.get(action, cmd_revise_list)(state, path, args)


# --------------------------------------------------------------------------
# Notion integration
# --------------------------------------------------------------------------

def _require_token(config):
    token = notion_token(config)
    if not token:
        fail("no Notion token found. Set $NEETSHUFFLE_NOTION_TOKEN, or pass "
             "--token to `notion setup`. Create one at "
             "https://www.notion.so/my-integrations")
    return token


def cmd_notion_setup(state, path, args):
    config = load_config()
    nconf = config.setdefault("notion", {})

    if args.token and args.save_token:
        nconf["token"] = args.token
    token = args.token or _require_token(config)

    try:
        who = notion.verify_token(token)
    except notion.NotionError as exc:
        fail("token check failed: {}".format(exc))
    print("🔗 Connected as Notion integration: {}".format(who))

    if args.database_id:
        try:
            notion.get_database(token, args.database_id)
        except notion.NotionError as exc:
            fail("couldn't open that database (is it shared with the "
                 "integration?): {}".format(exc))
        nconf["database_id"] = args.database_id
        print("Using existing database {}.".format(args.database_id))
    else:
        if not args.parent_page_id:
            fail("provide either --database-id (an existing DB) or "
                 "--parent-page-id (a page to create the DB under). Share that "
                 "page/DB with your integration first.")
        try:
            db_id = notion.create_database(token, args.parent_page_id, TOPICS,
                                           title=args.title)
        except notion.NotionError as exc:
            fail("couldn't create the database: {}".format(exc))
        nconf["database_id"] = db_id
        nconf["parent_page_id"] = args.parent_page_id
        print("📒 Created database '{}' ({}).".format(args.title, db_id))

    nconf["auto_sync"] = bool(args.auto)
    nconf.setdefault("pushed", {})
    save_config(config)
    print("Saved config to {} (chmod 600).".format(config_path()))
    if not (args.token and args.save_token) and not os.environ.get(
            "NEETSHUFFLE_NOTION_TOKEN"):
        print("Tip: export NEETSHUFFLE_NOTION_TOKEN=... so sync can find your "
              "token next time.")
    print("Now run:  neetshuffle notion sync")


def cmd_notion_sync(state, path, args):
    config = load_config()
    nconf = config.get("notion", {})
    db_id = nconf.get("database_id")
    if not db_id:
        fail("Notion isn't set up yet. Run `neetshuffle notion setup` first.")
    token = _require_token(config)

    pushed = nconf.setdefault("pushed", {})
    todo = [s for s in state["done"] if s not in pushed]
    if not todo:
        print("Notion is already up to date ({} problems mirrored).".format(
            len(pushed)))
        return

    print("Pushing {} problem(s) to Notion...".format(len(todo)))
    ok = 0
    for slug in todo:
        name, topic = _BY_SLUG[slug]
        solved_on = state["solved_at"].get(slug)
        try:
            page_id = notion.add_problem(token, db_id, name, url_for(slug),
                                         topic, solved_on)
        except notion.NotionError as exc:
            if exc.status in (401, 403):
                save_config(config)
                fail("auth error from Notion ({}). Re-check your token / that "
                     "the database is shared with the integration.".format(exc))
            warn("skipped {}: {}".format(name, exc))
            continue
        pushed[slug] = page_id
        ok += 1
        save_config(config)            # persist after each row -> resumable
        print("  ✓ {}".format(name))
        time.sleep(0.34)               # stay under Notion's ~3 req/s limit

    print("Done. {} added, {} total mirrored.".format(ok, len(pushed)))


def cmd_notion_status(state, path, args):
    config = load_config()
    nconf = config.get("notion", {})
    have_token = bool(notion_token(config))
    print("Notion integration")
    print("  Config file:  {}".format(config_path()))
    print("  Token:        {}".format("found" if have_token else "missing"))
    print("  Database id:  {}".format(nconf.get("database_id") or "(not set)"))
    print("  Auto-sync:    {}".format("on" if nconf.get("auto_sync") else "off"))
    print("  Mirrored:     {}/{} solved problems".format(
        len(nconf.get("pushed", {})), len(state["done"])))


def cmd_notion(state, path, args):
    # Dispatch the notion sub-subcommand; default to status.
    action = getattr(args, "notion_action", None)
    handlers = {
        "setup": cmd_notion_setup,
        "sync": cmd_notion_sync,
        "status": cmd_notion_status,
    }
    handlers.get(action, cmd_notion_status)(state, path, args)


def _maybe_auto_sync(state, slugs):
    """Best-effort push of just-solved problems when auto-sync is on. Never
    fatal -- a network hiccup must not break marking a problem done."""
    config = load_config()
    nconf = config.get("notion", {})
    if not nconf.get("auto_sync") or not nconf.get("database_id"):
        return
    token = notion_token(config)
    if not token:
        return
    pushed = nconf.setdefault("pushed", {})
    db_id = nconf["database_id"]
    pushed_any = False
    for slug in slugs:
        if slug in pushed:
            continue
        name, topic = _BY_SLUG[slug]
        try:
            page_id = notion.add_problem(token, db_id, name, url_for(slug),
                                         topic, state["solved_at"].get(slug))
        except notion.NotionError as exc:
            warn("Notion auto-sync skipped {}: {}".format(name, exc))
            continue
        pushed[slug] = page_id
        pushed_any = True
    if pushed_any:
        save_config(config)
        print("   ↳ mirrored to Notion.")


# --------------------------------------------------------------------------
# CLI wiring
# --------------------------------------------------------------------------

def build_parser():
    p = argparse.ArgumentParser(
        prog="neetshuffle",
        description="Daily topic-blind NeetCode 150 problem shuffler.")
    p.add_argument("--file", dest="file", default=None,
                   help="progress file path (default: $XDG_DATA_HOME/neetshuffle/"
                        "progress.json, or $NEETSHUFFLE_FILE).")
    sub = p.add_subparsers(dest="command")

    s_today = sub.add_parser("today", help="show today's jumbled set")
    s_today.add_argument("count", nargs="?", type=int, default=None,
                         help="how many problems (default %d)" % DEFAULT_COUNT)
    s_today.set_defaults(func=cmd_today)

    s_reroll = sub.add_parser("reroll", help="redraw today's set")
    s_reroll.add_argument("count", nargs="?", type=int, default=None,
                          help="how many problems (default %d)" % DEFAULT_COUNT)
    s_reroll.set_defaults(func=cmd_reroll)

    s_done = sub.add_parser("done", help="mark problem #n of today as solved")
    s_done.add_argument("number", type=int, help="problem number from `today`")
    s_done.set_defaults(func=cmd_done)

    s_import = sub.add_parser(
        "import", help="bulk-mark already-solved problems from a file/stdin")
    s_import.add_argument("source",
                          help="path to a file of LeetCode URLs/slugs/names, "
                               "or '-' for stdin")
    s_import.add_argument("--date", default=None,
                          help="solved-on date for imported problems "
                               "(YYYY-MM-DD; default today)")
    s_import.set_defaults(func=cmd_import)

    s_revise = sub.add_parser("revise", help="manage a personal revision list")
    s_revise.set_defaults(func=cmd_revise)
    rsub = s_revise.add_subparsers(dest="revise_action")
    r_add = rsub.add_parser(
        "add", help="add problem(s) by today-number, name, slug, or URL")
    r_add.add_argument("refs", nargs="+",
                       help="today's problem number(s) and/or names/slugs/URLs")
    r_rm = rsub.add_parser("remove", help="remove problem(s) from the list")
    r_rm.add_argument("refs", nargs="+",
                      help="revision items by name/slug/URL (or today-number)")
    rsub.add_parser("list", help="show the revision list")
    rsub.add_parser("clear", help="empty the revision list")
    r_draw = rsub.add_parser(
        "draw", help="draw a jumbled practice set from the revision list")
    r_draw.add_argument("count", nargs="?", type=int, default=None,
                        help="how many problems (default %d)" % DEFAULT_COUNT)
    r_done = rsub.add_parser("done", help="mark #n of the revision set as revised")
    r_done.add_argument("number", type=int, help="problem number from `revise draw`")

    s_stats = sub.add_parser("stats", help="show overall + per-topic progress")
    s_stats.set_defaults(func=cmd_stats)

    s_reset = sub.add_parser("reset", help="wipe all progress")
    s_reset.add_argument("-y", "--yes", action="store_true",
                         help="skip the confirmation prompt")
    s_reset.set_defaults(func=cmd_reset)

    s_notion = sub.add_parser("notion", help="mirror solved problems to Notion")
    s_notion.set_defaults(func=cmd_notion)
    nsub = s_notion.add_subparsers(dest="notion_action")

    n_setup = nsub.add_parser("setup", help="connect a Notion database")
    n_setup.add_argument("--token", default=None,
                         help="Notion integration token (else "
                              "$NEETSHUFFLE_NOTION_TOKEN)")
    n_setup.add_argument("--save-token", action="store_true",
                         help="store the token in the config file (chmod 600)")
    n_setup.add_argument("--parent-page-id", default=None,
                         help="page id to create a new database under")
    n_setup.add_argument("--database-id", default=None,
                         help="use an existing database instead of creating one")
    n_setup.add_argument("--title", default="NeetCode 150 Progress",
                         help="title for a newly-created database")
    n_setup.add_argument("--auto", action="store_true",
                         help="auto-mirror to Notion whenever you mark done")

    nsub.add_parser("sync", help="push all solved problems not yet in Notion")
    nsub.add_parser("status", help="show Notion connection + mirror status")

    return p


def validate_count(args):
    count = getattr(args, "count", None)
    if count is not None and (count < MIN_COUNT or count > MAX_COUNT):
        fail("count must be between {} and {}.".format(MIN_COUNT, MAX_COUNT))


def validate_date(args):
    date = getattr(args, "date", None)
    if date is None:
        return
    try:
        datetime.date.fromisoformat(date)
    except ValueError:
        fail("--date must be in YYYY-MM-DD format.")


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        # Bare `neetshuffle` behaves like `today` with the default count.
        args.func = cmd_today
        args.count = None

    validate_count(args)
    validate_date(args)

    path = (os.path.abspath(os.path.expanduser(args.file))
            if args.file else default_state_path())
    state = load_state(path)
    args.func(state, path, args)


if __name__ == "__main__":
    main()
