"""psList — the roadmap problem set, solvable by topic, by difficulty, or jumbled.

Unlike the topic-blind NeetCode flow, psList is meant to be *browsed and filtered*:
draw a set scoped to a topic, to a difficulty band, or to nothing at all (a pure
jumble across the whole set). Progress (done / stats / revision) is tracked in its
own state file so it never touches your NeetCode progress.

Two roadmap modes are available:
  faang    - FAANG Essentials (377 problems, 29 topics)
  cracked  - Cracked (850 problems, 40 topics; a superset of faang)
Each mode keeps its own progress file, so reps in one mode don't leak into the
other.

The problem's URL is its identity. A few problems appear under more than one topic
in the roadmap; solving such a problem marks it done under every topic it lists in.
"""

import datetime
import json
import os
import random
import re
import secrets
import sys
import tempfile

from .pslist_data_faang import PSLIST as _PSLIST_FAANG
from .pslist_data_cracked import PSLIST as _PSLIST_CRACKED

DEFAULT_COUNT = 4
MIN_COUNT = 1
MAX_COUNT = 25
STATE_VERSION = 1
APP_NAME = "neetshuffle"

# Available roadmap modes: name -> (dataset, human label).
MODES = {
    "faang": (_PSLIST_FAANG, "FAANG Essentials"),
    "cracked": (_PSLIST_CRACKED, "Cracked"),
}
DEFAULT_MODE = "cracked"

# Difficulty bands from easiest to hardest -- used for ordering and validation.
DIFF_ORDER = ["Easy", "Easy+", "Normal", "Normal+", "Hard", "Harder", "Insane",
              "Expert", "Master", "Grandmaster", "Glitched", "Mythic", "Mythic+"]
_DIFF_RANK = {d: i for i, d in enumerate(DIFF_ORDER)}


def _normalize(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


# Active-mode catalog. These are populated by activate() before any command runs
# (the CLI handles one invocation per process, so module-level state is fine).
MODE = DEFAULT_MODE
MODE_LABEL = MODES[DEFAULT_MODE][1]
PROBLEMS = []
_BY_URL = {}
ALL_URLS = []
TOPICS = []
TOPIC_TOTALS = {}
DIFF_TOTALS = {}
_NAME_TO_URL = {}


def activate(mode):
    """Select a roadmap mode and (re)build the derived lookup tables."""
    global MODE, MODE_LABEL, PROBLEMS, _BY_URL, ALL_URLS, TOPICS
    global TOPIC_TOTALS, DIFF_TOTALS, _NAME_TO_URL
    if mode not in MODES:
        fail("unknown mode '%s'. Valid modes: %s"
             % (mode, ", ".join(sorted(MODES))))
    MODE = mode
    PROBLEMS, MODE_LABEL = MODES[mode]

    _BY_URL = {}
    for p in PROBLEMS:
        _BY_URL.setdefault(p["url"], p)  # first listing wins as the primary record
    ALL_URLS = list(_BY_URL.keys())

    TOPICS = []
    for p in PROBLEMS:
        if p["topic"] not in TOPICS:
            TOPICS.append(p["topic"])

    TOPIC_TOTALS = {}
    DIFF_TOTALS = {}
    for url, p in _BY_URL.items():
        TOPIC_TOTALS[p["topic"]] = TOPIC_TOTALS.get(p["topic"], 0) + 1
        DIFF_TOTALS[p["difficulty"]] = DIFF_TOTALS.get(p["difficulty"], 0) + 1

    _NAME_TO_URL = {}
    for p in PROBLEMS:
        _NAME_TO_URL.setdefault(_normalize(p["name"]), p["url"])


# --------------------------------------------------------------------------
# Output helpers
# --------------------------------------------------------------------------

def warn(msg):
    print("⚠️  " + msg, file=sys.stderr)


def fail(msg, code=1):
    print("Error: " + msg, file=sys.stderr)
    sys.exit(code)


# --------------------------------------------------------------------------
# State storage (independent of the NeetCode progress file)
# --------------------------------------------------------------------------

def default_state_path(mode):
    """Per-mode progress file. $NEETSHUFFLE_PSLIST_DIR overrides the directory;
    each mode still gets its own file inside it."""
    base_dir = os.environ.get("NEETSHUFFLE_PSLIST_DIR")
    if base_dir:
        base_dir = os.path.abspath(os.path.expanduser(base_dir))
    else:
        base = os.environ.get("XDG_DATA_HOME") or os.path.expanduser("~/.local/share")
        base_dir = os.path.join(base, APP_NAME)
    return os.path.join(base_dir, "pslist_progress_%s.json" % mode)


def new_state():
    return {
        "version": STATE_VERSION,
        "salt": secrets.token_hex(16),
        "done": [],          # urls solved
        "solved_at": {},     # url -> ISO date (may be None)
        "current": None,     # last drawn set: {"urls", "done", "label"}
        "revise": [],        # urls flagged for revision
        "revise_set": None,  # {"urls", "done"}
    }


def _atomic_write_json(path, obj):
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
            os.chmod(tmp, 0o600)
        except OSError:
            pass
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def load_state(path):
    if not os.path.exists(path):
        return new_state()
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError, ValueError) as exc:
        backup = path + ".corrupt"
        try:
            os.replace(path, backup)
            warn("psList progress file was unreadable (%s); backed it up to %s "
                 "and started fresh." % (exc, backup))
        except OSError:
            warn("psList progress file was unreadable (%s); starting fresh." % exc)
        return new_state()
    return _sanitize(data)


def _clean_url_list(value, valid):
    if not isinstance(value, list):
        return []
    seen, out = set(), []
    for u in value:
        if isinstance(u, str) and u in valid and u not in seen:
            seen.add(u)
            out.append(u)
    return out


def _clean_set(value, valid):
    if not isinstance(value, dict):
        return None
    urls = value.get("urls")
    if not isinstance(urls, list) or not all(
            isinstance(u, str) and u in valid for u in urls):
        return None
    done = value.get("done", [])
    done = [u for u in done if isinstance(u, str) and u in urls] \
        if isinstance(done, list) else []
    out = {"urls": urls, "done": done}
    if isinstance(value.get("label"), str):
        out["label"] = value["label"]
    return out


def _sanitize(data):
    if not isinstance(data, dict):
        warn("psList progress file had an unexpected shape; starting fresh.")
        return new_state()
    state = new_state()
    valid = set(ALL_URLS)
    if isinstance(data.get("salt"), str) and data["salt"]:
        state["salt"] = data["salt"]
    state["done"] = _clean_url_list(data.get("done"), valid)
    solved_at = data.get("solved_at", {})
    if isinstance(solved_at, dict):
        done_set = set(state["done"])
        state["solved_at"] = {
            u: v for u, v in solved_at.items()
            if u in done_set and (v is None or isinstance(v, str))
        }
    state["revise"] = _clean_url_list(data.get("revise"), valid)
    state["current"] = _clean_set(data.get("current"), valid)
    state["revise_set"] = _clean_set(data.get("revise_set"), valid)
    return state


def save_state(path, state):
    _atomic_write_json(path, state)


def today_str():
    return datetime.date.today().isoformat()


# --------------------------------------------------------------------------
# Filtering / drawing
# --------------------------------------------------------------------------

def resolve_topic(token):
    """Match a topic name case-insensitively (exact, then substring)."""
    norm = token.strip().lower()
    for t in TOPICS:
        if t.lower() == norm:
            return t
    matches = [t for t in TOPICS if norm in t.lower()]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        fail("ambiguous topic '%s'; matches: %s" % (token, ", ".join(matches)))
    fail("unknown topic '%s'. See `neetshuffle pslist topics`." % token)


def resolve_difficulty(token):
    norm = token.strip().lower()
    for d in DIFF_ORDER:
        if d.lower() == norm:
            return d
    fail("unknown difficulty '%s'. Valid bands: %s"
         % (token, ", ".join(DIFF_ORDER)))


def filter_pool(topic=None, difficulty=None, source=None, min_importance=0,
                exclude=None):
    """Return problem records matching the filters, skipping `exclude` urls.

    Deduplicates by URL so a multi-topic problem is offered once (unless the
    filter is scoped to a specific topic, where its topic-specific listing wins)."""
    exclude = exclude or set()
    out, seen = [], set()
    for p in PROBLEMS:
        url = p["url"]
        if url in exclude or url in seen:
            continue
        if topic and p["topic"] != topic:
            continue
        if difficulty and p["difficulty"] != difficulty:
            continue
        if source and p["source"].lower() != source.lower():
            continue
        if p["importance"] < min_importance:
            continue
        seen.add(url)
        out.append(p)
    return out


def _describe_filters(topic, difficulty, source, min_importance):
    bits = []
    if topic:
        bits.append("topic=%s" % topic)
    if difficulty:
        bits.append("difficulty=%s" % difficulty)
    if source:
        bits.append("source=%s" % source)
    if min_importance:
        bits.append("importance>=%d" % min_importance)
    return ", ".join(bits) if bits else "jumble (all topics & difficulties)"


def _print_set(records, done_urls, header):
    print(header + "\n")
    for i, p in enumerate(records, start=1):
        mark = "✓" if p["url"] in done_urls else " "
        meta = "%s · %s" % (p["topic"], p["difficulty"])
        print("  [{}] {}. {}  ({})".format(mark, i, p["name"], meta))
        print("        {}".format(p["url"]))
    print()


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------

def cmd_draw(state, path, args):
    topic = resolve_topic(args.topic) if args.topic else None
    difficulty = resolve_difficulty(args.difficulty) if args.difficulty else None
    source = args.source
    min_imp = args.min_importance or 0

    pool = filter_pool(topic, difficulty, source, min_imp,
                       exclude=set(state["done"]))
    if not pool:
        fail("no unsolved problems match (%s). Try loosening the filters or "
             "`neetshuffle pslist stats`."
             % _describe_filters(topic, difficulty, source, min_imp))

    count = args.count if args.count is not None else DEFAULT_COUNT
    count = max(MIN_COUNT, min(count, len(pool)))

    rng = random.SystemRandom()
    rng.shuffle(pool)
    chosen = pool[:count]
    urls = [p["url"] for p in chosen]

    label = _describe_filters(topic, difficulty, source, min_imp)
    state["current"] = {"urls": urls, "done": [], "label": label}
    save_state(path, state)

    header = "🎯 psList [{}] draw — {} ({} problem{}, {} left in this filter)".format(
        MODE_LABEL, label, len(chosen),
        "" if len(chosen) == 1 else "s", len(pool))
    _print_set(chosen, set(state["done"]), header)
    print("Mark solved with:  neetshuffle pslist done <number>")


def _records_for(urls):
    return [_BY_URL[u] for u in urls]


def cmd_done(state, path, args):
    cur = state.get("current")
    if not cur or not cur.get("urls"):
        fail("no psList set drawn yet. Run `neetshuffle pslist draw` first.")
    n = args.number
    urls = cur["urls"]
    if n < 1 or n > len(urls):
        fail("pick a number between 1 and %d." % len(urls))

    url = urls[n - 1]
    name = _BY_URL[url]["name"]
    if url in cur.get("done", []):
        print("Already marked done: %s" % name)
        return

    if url not in state["done"]:
        state["done"].append(url)
    if state["solved_at"].get(url) is None:
        state["solved_at"][url] = today_str()
    cur.setdefault("done", []).append(url)
    save_state(path, state)

    p = _BY_URL[url]
    print("✓ Marked done: %s" % name)
    print("   Topic: %s · %s   (%s)" % (p["topic"], p["difficulty"], p["source"]))
    left = len(urls) - len(cur["done"])
    if left == 0:
        print("That's the whole set. 🎯")
    else:
        print("%d left in this set." % left)


def cmd_list(state, path, args):
    topic = resolve_topic(args.topic) if args.topic else None
    difficulty = resolve_difficulty(args.difficulty) if args.difficulty else None
    source = args.source
    min_imp = args.min_importance or 0

    records = filter_pool(topic, difficulty, source, min_imp)
    done = set(state["done"])
    if args.undone:
        records = [p for p in records if p["url"] not in done]
    if not records:
        print("Nothing matches (%s)."
              % _describe_filters(topic, difficulty, source, min_imp))
        return

    # Stable, readable ordering: by topic (roadmap order), then difficulty.
    records.sort(key=lambda p: (TOPICS.index(p["topic"]),
                                _DIFF_RANK.get(p["difficulty"], 99),
                                p["name"].lower()))
    limit = args.limit
    shown = records[:limit] if limit else records

    print("psList — %s  (%d problem%s%s)\n" % (
        _describe_filters(topic, difficulty, source, min_imp),
        len(records), "" if len(records) == 1 else "s",
        "" if not limit or limit >= len(records) else ", showing %d" % limit))
    cur_topic = None
    for p in shown:
        if p["topic"] != cur_topic:
            cur_topic = p["topic"]
            print("  %s" % cur_topic)
        mark = "✓" if p["url"] in done else " "
        print("    [{}] {:<11} {}".format(mark, p["difficulty"], p["name"]))
        print("              {}".format(p["url"]))


def cmd_topics(state, path, args):
    done = set(state["done"])
    print("psList topics [%s mode] (solved / total):\n" % MODE_LABEL)
    width = max(len(t) for t in TOPICS)
    for t in TOPICS:
        tot = TOPIC_TOTALS[t]
        d = sum(1 for u, p in _BY_URL.items() if p["topic"] == t and u in done)
        seg = 12
        f = int(seg * d / tot) if tot else 0
        bar = "█" * f + "░" * (seg - f)
        print("  {:<{w}}  {}  {:>3}/{:<3}".format(t, bar, d, tot, w=width))
    print("\nDraw a topic with:  neetshuffle pslist draw --topic \"<name>\"")


def cmd_difficulties(state, path, args):
    done = set(state["done"])
    print("psList difficulty bands (solved / total):\n")
    width = max(len(d) for d in DIFF_ORDER)
    for d in DIFF_ORDER:
        tot = DIFF_TOTALS.get(d, 0)
        if not tot:
            continue
        s = sum(1 for u, p in _BY_URL.items()
                if p["difficulty"] == d and u in done)
        seg = 12
        f = int(seg * s / tot) if tot else 0
        bar = "█" * f + "░" * (seg - f)
        print("  {:<{w}}  {}  {:>3}/{:<3}".format(d, bar, s, tot, w=width))
    print("\nDraw a difficulty with:  neetshuffle pslist draw --difficulty <band>")


def cmd_stats(state, path, args):
    total = len(ALL_URLS)
    done = len(state["done"])
    pct = (done / total * 100) if total else 0
    bar_len = 30
    filled = int(bar_len * done / total) if total else 0
    bar = "█" * filled + "░" * (bar_len - filled)
    print("psList progress  [%s mode]" % MODE_LABEL)
    print("  [{}] {}/{}  ({:.1f}%)".format(bar, done, total, pct))
    print("  Remaining: {}".format(total - done))
    print("\nUse `neetshuffle pslist topics` or `... difficulties` for breakdowns.")


# --------------------------------------------------------------------------
# Revision
# --------------------------------------------------------------------------

def _resolve_ref(state, token):
    """Resolve a reference to a url: a bare integer = #n of the current draw;
    otherwise a URL, or a problem name."""
    token = token.strip()
    if token.isdigit():
        cur = state.get("current")
        if cur and cur.get("urls"):
            i = int(token)
            if 1 <= i <= len(cur["urls"]):
                return cur["urls"][i - 1]
        return None
    if token in _BY_URL:
        return token
    m = re.search(r"https?://\S+", token)
    if m and m.group(0) in _BY_URL:
        return m.group(0)
    return _NAME_TO_URL.get(_normalize(token))


def cmd_revise_add(state, path, args):
    added, dup, unknown = [], [], []
    for ref in args.refs:
        url = _resolve_ref(state, ref)
        if url is None:
            unknown.append(ref)
        elif url in state["revise"]:
            dup.append(url)
        else:
            state["revise"].append(url)
            added.append(url)
    save_state(path, state)
    print("Added %d to revision (%d already listed, %d unrecognised)."
          % (len(added), len(dup), len(unknown)))
    for u in added:
        print("  + %s" % _BY_URL[u]["name"])
    for u in unknown:
        print("  ? %s" % u)


def cmd_revise_remove(state, path, args):
    removed, missing = [], []
    for ref in args.refs:
        url = _resolve_ref(state, ref)
        if url and url in state["revise"]:
            state["revise"].remove(url)
            removed.append(url)
        else:
            missing.append(ref)
    save_state(path, state)
    print("Removed %d from revision." % len(removed))
    for u in removed:
        print("  - %s" % _BY_URL[u]["name"])
    for m in missing:
        print("  ? not on the list: %s" % m)


def cmd_revise_list(state, path, args):
    rev = state["revise"]
    if not rev:
        print("psList revision list is empty.")
        print("Add with:  neetshuffle pslist revise add <draw-number | name | url>")
        return
    print("📝 psList revision list (%d problem%s):"
          % (len(rev), "" if len(rev) == 1 else "s"))
    for i, url in enumerate(rev, start=1):
        p = _BY_URL[url]
        print("  %d. %s  (%s · %s)" % (i, p["name"], p["topic"], p["difficulty"]))
        print("       %s" % url)
    print("\nPractice them with:  neetshuffle pslist revise draw")


def cmd_revise_clear(state, path, args):
    n = len(state["revise"])
    state["revise"] = []
    state["revise_set"] = None
    save_state(path, state)
    print("Cleared %d problem(s) from psList revision." % n)


def cmd_revise_draw(state, path, args):
    rev = state["revise"]
    if not rev:
        fail("revision list is empty. Add problems first: "
             "neetshuffle pslist revise add ...")
    count = args.count if args.count is not None else min(DEFAULT_COUNT, len(rev))
    count = max(MIN_COUNT, min(count, len(rev)))
    pool = rev[:]
    random.SystemRandom().shuffle(pool)
    urls = pool[:count]
    state["revise_set"] = {"urls": urls, "done": []}
    save_state(path, state)
    _print_set(_records_for(urls), set(),
               "🔁 psList revision set (%d problem%s)"
               % (len(urls), "" if len(urls) == 1 else "s"))
    print("When solved:  neetshuffle pslist revise done <number>")


def cmd_revise_done(state, path, args):
    rset = state.get("revise_set")
    if not rset or not rset.get("urls"):
        fail("no revision set drawn yet. Run `neetshuffle pslist revise draw` first.")
    n = args.number
    urls = rset["urls"]
    if n < 1 or n > len(urls):
        fail("pick a number between 1 and %d." % len(urls))
    url = urls[n - 1]
    name = _BY_URL[url]["name"]
    if url in rset.get("done", []):
        print("Already revised: %s" % name)
        return
    rset.setdefault("done", []).append(url)
    if url in state["revise"]:
        state["revise"].remove(url)
    # Revising also counts as solved if it wasn't already.
    if url not in state["done"]:
        state["done"].append(url)
        state["solved_at"].setdefault(url, today_str())
    save_state(path, state)
    print("✓ Revised: %s" % name)
    left = len(urls) - len(rset["done"])
    print("Revision set complete. 🔁" if left == 0
          else "%d left in this revision set." % left)


def cmd_revise(state, path, args):
    action = getattr(args, "pslist_revise_action", None)
    handlers = {
        "add": cmd_revise_add,
        "remove": cmd_revise_remove,
        "list": cmd_revise_list,
        "clear": cmd_revise_clear,
        "draw": cmd_revise_draw,
        "done": cmd_revise_done,
    }
    handlers.get(action, cmd_revise_list)(state, path, args)


def cmd_reset(state, path, args):
    if not args.yes:
        try:
            ans = input("This wipes ALL psList [%s] progress. Type 'yes' to "
                        "confirm: " % MODE_LABEL)
        except (EOFError, KeyboardInterrupt):
            print()
            fail("aborted.")
        if ans.strip().lower() != "yes":
            fail("aborted.")
    save_state(path, new_state())
    print("psList progress reset. 🌱")


# --------------------------------------------------------------------------
# Dispatch + CLI wiring
# --------------------------------------------------------------------------

def run(args):
    """Entry point called from the top-level CLI for any `pslist ...` command.

    psList keeps its own per-mode progress file, independent of the NeetCode
    `--file` progress."""
    activate(getattr(args, "pslist_mode", None) or DEFAULT_MODE)
    path = default_state_path(MODE)
    state = load_state(path)
    action = getattr(args, "pslist_action", None)
    handlers = {
        "draw": cmd_draw,
        "done": cmd_done,
        "list": cmd_list,
        "topics": cmd_topics,
        "difficulties": cmd_difficulties,
        "stats": cmd_stats,
        "revise": cmd_revise,
        "reset": cmd_reset,
    }
    handlers.get(action, cmd_draw)(state, path, args)


def _add_filter_args(parser):
    parser.add_argument("--topic", default=None,
                        help="restrict to a roadmap topic (see `pslist topics`)")
    parser.add_argument("--difficulty", default=None,
                        help="restrict to a difficulty band (see `pslist difficulties`)")
    parser.add_argument("--source", default=None,
                        help="restrict to a judge (leetcode, cses, atcoder, ...)")
    parser.add_argument("--min-importance", type=int, default=0,
                        dest="min_importance",
                        help="only problems with importance >= N (0-3)")


def register(subparsers):
    """Attach the `pslist` command group to the top-level subparsers."""
    ps = subparsers.add_parser(
        "pslist", help="roadmap problem set: solve by topic, difficulty, or jumbled")
    ps.add_argument("--mode", dest="pslist_mode",
                    choices=sorted(MODES), default=DEFAULT_MODE,
                    help="which roadmap to use (default %s); give it before the "
                         "subcommand, e.g. `pslist --mode faang draw`"
                         % DEFAULT_MODE)
    ps.set_defaults(func=lambda state, path, args: run(args))
    psub = ps.add_subparsers(dest="pslist_action")

    p_draw = psub.add_parser(
        "draw", help="draw a set (jumbled, or filtered by topic/difficulty)")
    p_draw.add_argument("count", nargs="?", type=int, default=None,
                        help="how many problems (default %d)" % DEFAULT_COUNT)
    _add_filter_args(p_draw)

    p_done = psub.add_parser("done", help="mark problem #n of the current set solved")
    p_done.add_argument("number", type=int, help="problem number from `pslist draw`")

    p_list = psub.add_parser("list", help="browse the catalog (sorted, not random)")
    _add_filter_args(p_list)
    p_list.add_argument("--undone", action="store_true",
                        help="hide problems you've already solved")
    p_list.add_argument("--limit", type=int, default=None,
                        help="cap how many rows are printed")

    psub.add_parser("topics", help="list topics with solved/total counts")
    psub.add_parser("difficulties", help="list difficulty bands with counts")
    psub.add_parser("stats", help="show overall psList progress")

    p_reset = psub.add_parser("reset", help="wipe all psList progress")
    p_reset.add_argument("-y", "--yes", action="store_true",
                         help="skip the confirmation prompt")

    p_rev = psub.add_parser("revise", help="manage a psList revision list")
    rsub = p_rev.add_subparsers(dest="pslist_revise_action")
    r_add = rsub.add_parser("add", help="add by draw-number, name, or URL")
    r_add.add_argument("refs", nargs="+")
    r_rm = rsub.add_parser("remove", help="remove problem(s) from the list")
    r_rm.add_argument("refs", nargs="+")
    rsub.add_parser("list", help="show the revision list")
    rsub.add_parser("clear", help="empty the revision list")
    r_draw = rsub.add_parser("draw", help="draw a jumbled practice set to revise")
    r_draw.add_argument("count", nargs="?", type=int, default=None)
    r_done = rsub.add_parser("done", help="mark #n of the revision set as revised")
    r_done.add_argument("number", type=int)

    return ps
