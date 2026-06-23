# neetshuffle

A daily, **topic-blind** NeetCode 150 problem shuffler.

Every day it draws a handful of problems jumbled across *every* category and
shows you only the **name and link** — never the topic. The point is to stop
you from pattern-matching ("this is in the sliding-window section, so I'll use
a sliding window") and force you to actually recognise the problem and build
genuine problem-solving. Solved problems are tracked so they never repeat.

Topics only ever appear in `stats`, and only for problems you've **already
solved** — a retrospective view of where your reps have gone, which can't help
you cheat on a problem you haven't done yet.

## Install

With [pipx](https://pipx.pypa.io) (recommended — isolated, on your PATH):

```bash
pipx install .
```

Or a plain pip install / editable install:

```bash
pip install .
# or, for development:
pip install -e .
```

No third-party dependencies — pure Python standard library (3.8+).

You can also run it without installing:

```bash
python -m neetshuffle today 4
```

## Usage

```bash
neetshuffle today [num]    # today's jumble (default 4 problems); stable all day
neetshuffle done <n>       # mark problem #n of today's set as solved
neetshuffle reroll [num]   # throw away today's set and draw a fresh one
neetshuffle import <file>  # bulk-mark problems you've already solved
neetshuffle stats          # overall progress + per-topic (solved problems only)
neetshuffle notion ...     # mirror solved problems to a Notion database
neetshuffle reset          # wipe all progress (asks to confirm; -y to skip)
```

Bare `neetshuffle` is the same as `neetshuffle today`.

### Example

```
$ neetshuffle today 4
📅 2026-06-23  —  today's jumble (4 problems)
   Topics are hidden on purpose. Figure out the approach yourself.

  [ ] 1. Sliding Window Maximum
        https://leetcode.com/problems/sliding-window-maximum/
  [ ] 2. Non-overlapping Intervals
        https://leetcode.com/problems/non-overlapping-intervals/
  [ ] 3. Search a 2D Matrix
        https://leetcode.com/problems/search-a-2d-matrix/
  [ ] 4. Redundant Connection
        https://leetcode.com/problems/redundant-connection/

Solve them, then run:  neetshuffle done <number>   (4 left today)

$ neetshuffle done 1
✓ Marked done: Sliding Window Maximum
3 left in today's jumble.
```

## Importing problems you've already solved

If you're not starting from zero, bulk-mark what you've done so neetshuffle
won't draw them again:

```bash
neetshuffle import solved.txt        # from a file
pbpaste | neetshuffle import -       # or from stdin
neetshuffle import solved.txt --date 2025-12-01   # set the solved-on date
```

The file is one problem per line, in **any mix** of these formats — blank lines
and `#` comments are ignored:

```
https://leetcode.com/problems/two-sum/
valid-anagram
Group Anagrams
```

Matching is forgiving (case- and punctuation-insensitive). Anything that isn't
part of the NeetCode 150 is reported back so you can fix typos.

## Mirroring to Notion

neetshuffle can push your solved problems into a Notion database as tidy rows
(Problem, Link, Topic, Solved-on date, Status), each with a ✅ icon. Topics
appear here only for problems you've **already solved**, consistent with the
topic-blind rule.

**One-time setup**

1. Create an internal integration at
   <https://www.notion.so/my-integrations> and copy its **token**
   (`ntn_...` / `secret_...`).
2. In Notion, open the page you want the database created under, and **share
   that page with your integration** (`•••` → *Connections* → add it).
3. Grab the page id — it's the 32-hex chunk in the page URL.

```bash
export NEETSHUFFLE_NOTION_TOKEN="ntn_xxx"          # keeps the token out of disk
neetshuffle notion setup --parent-page-id <PAGE_ID>
neetshuffle notion sync
```

Prefer an existing database? Share it with the integration and use
`--database-id <DB_ID>` instead of `--parent-page-id`.

**Day-to-day**

```bash
neetshuffle notion sync      # push everything solved-but-not-yet-mirrored
neetshuffle notion status    # connection + how many problems are mirrored
```

Add `--auto` to `setup` to mirror automatically each time you mark a problem
done (best-effort: a network blip never blocks `done`).

**Token handling.** The token is read from `$NEETSHUFFLE_NOTION_TOKEN` by
default and is **not** written to disk. If you'd rather store it, pass
`--token <T> --save-token` and it's saved to the config file with `0600`
permissions. The config lives at `$XDG_CONFIG_HOME/neetshuffle/config.json`
(default `~/.config/neetshuffle/config.json`), separate from your progress, and
records which problems have already been pushed so re-running `sync` never
creates duplicates.

## How the shuffle works

The daily draw is seeded by `sha256(salt + date + reroll-nonce)`:

- A cryptographically random **salt** (from Python's `secrets`) is generated
  once per install, so two people running the tool get different draws.
- Mixing in the **date** keeps today's set stable no matter how many times you
  run `today`.
- A **reroll nonce** changes the seed each time you `reroll`, so a redraw is a
  genuinely different set.

Already-solved problems are removed from the pool, so you never see a problem
you've finished again.

## Where progress is stored

A single local JSON file, by default:

```
$XDG_DATA_HOME/neetshuffle/progress.json
# (falls back to ~/.local/share/neetshuffle/progress.json)
```

Override the location with `--file <path>` or the `NEETSHUFFLE_FILE`
environment variable.

The file is written atomically (temp file + rename, so it's never left
half-written) and with owner-only `0600` permissions. If it ever gets corrupted
or hand-edited into something invalid, neetshuffle backs it up to
`progress.json.corrupt` and starts fresh rather than crashing or losing data
silently.
