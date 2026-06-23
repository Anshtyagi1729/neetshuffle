#!/usr/bin/env python3
"""neetshuffle - a daily, topic-blind NeetCode 150 problem shuffler.

Philosophy: problems are ALWAYS shown topic-blind. You get them jumbled across
every category so you can't lean on "oh this is the sliding-window section" and
pattern-match your way through -- you have to actually recognise the problem.

Topics only ever surface in `stats`, and only for problems you've already
solved, as a retrospective view of where your reps have gone.
"""

import argparse
import datetime
import hashlib
import json
import os
import random
import secrets
import sys
import tempfile

from .problems import NEETCODE_150, url_for

DEFAULT_COUNT = 4
MIN_COUNT = 1
MAX_COUNT = 25  # sanity cap so a typo can't request the whole list
STATE_VERSION = 1
APP_NAME = "neetshuffle"

# Map slug -> (name, topic) once, so lookups are O(1) and the canonical
# ordering of NEETCODE_150 is the source of truth for valid slugs.
_BY_SLUG = {slug: (name, topic) for (name, slug, topic) in NEETCODE_150}
ALL_SLUGS = [slug for (_, slug, _) in NEETCODE_150]

# Topic -> total problem count, in first-seen order (for stable stats output).
TOPIC_TOTALS = {}
for _name, _slug, _topic in NEETCODE_150:
    TOPIC_TOTALS[_topic] = TOPIC_TOTALS.get(_topic, 0) + 1


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
        "today": None,       # {"date", "slugs", "done", "nonce"}
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
    return state


def save_state(path, state):
    """Atomic, owner-only write. Temp file in the same dir + os.replace means we
    never leave a half-written progress file behind."""
    directory = os.path.dirname(path) or "."
    os.makedirs(directory, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=directory, prefix=".progress-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(state, fh, indent=2, sort_keys=True)
            fh.write("\n")
            fh.flush()
            os.fsync(fh.fileno())
        try:
            os.chmod(tmp, 0o600)  # progress is yours alone
        except OSError:
            pass
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


# --------------------------------------------------------------------------
# Core logic
# --------------------------------------------------------------------------

def today_str():
    return datetime.date.today().isoformat()


def remaining_slugs(state):
    done = set(state["done"])
    return [s for s in ALL_SLUGS if s not in done]


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

    day.setdefault("done", []).append(slug)
    if slug not in state["done"]:
        state["done"].append(slug)
    save_state(path, state)

    # Deliberately NO topic reveal here -- keep your brain guessing.
    print("✓ Marked done: {}".format(name))
    left = len(slugs) - len(day["done"])
    if left == 0:
        print("That's the whole set. Nice work today. 🎯")
    else:
        print("{} left in today's jumble.".format(left))


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

    s_stats = sub.add_parser("stats", help="show overall + per-topic progress")
    s_stats.set_defaults(func=cmd_stats)

    s_reset = sub.add_parser("reset", help="wipe all progress")
    s_reset.add_argument("-y", "--yes", action="store_true",
                         help="skip the confirmation prompt")
    s_reset.set_defaults(func=cmd_reset)

    return p


def validate_count(args):
    count = getattr(args, "count", None)
    if count is not None and (count < MIN_COUNT or count > MAX_COUNT):
        fail("count must be between {} and {}.".format(MIN_COUNT, MAX_COUNT))


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        # Bare `neetshuffle` behaves like `today` with the default count.
        args.func = cmd_today
        args.count = None

    validate_count(args)

    path = (os.path.abspath(os.path.expanduser(args.file))
            if args.file else default_state_path())
    state = load_state(path)
    args.func(state, path, args)


if __name__ == "__main__":
    main()
