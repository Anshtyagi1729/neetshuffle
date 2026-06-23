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
neetshuffle stats          # overall progress + per-topic (solved problems only)
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
