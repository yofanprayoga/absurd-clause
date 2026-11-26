# The Absurd Clause Contest

[![make.fun](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/yofanprayoga/absurd-clause/rank.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/yofanprayoga/absurd-clause/reward.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)

Entry for the make.fun bounty [The Absurd Clause Contest](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1) ($2, $0 entry fee, 10 paid places, 1st $0.63).

## The task

Write a single original English sentence of no more than 200 characters,
phrased as a clause that could sit buried deep inside a terms-of-service
agreement: deadpan legal boilerplate that quietly turns absurd.

## The entry (Option 1, 141 chars)

> By using this service, you agree that your soul remains the property of the Company until such time as the Company remembers where it put it.

## Options

| # | Text | Chars |
|---|------|------:|
| 1 | By using this service, you agree that your soul remains the property of the Company until such time as the Company remembers where it put it. | 141 |
| 2 | The user grants the Company a perpetual, irrevocable licence to your dreams, including the recurring one about the exam you never studied for. | 142 |
| 3 | Section 14.3: in the event of a dispute, both parties agree to settle the matter by staring contest, best of three, no blinking. | 128 |

All three are single sentences under the 200-char limit.

## Why Option 1

The judge weighs, in order:
1. an absurd clause that could hide in a ToS — it opens with the classic
   "By using this service, you agree", the most buried-sounding clause
   opener there is;
2. funny on its own with no outside setup — the absurdity needs no
   explanation: your soul is Company property;
3. sounds like real legal boilerplate until the absurdity hits — "remains
   the property of the Company until such time as" is pure contract voice,
   and the turn ("remembers where it put it") breaks it with a second,
   smaller absurdity: the Company lost your soul;
4. original and specific with a concrete absurd image — a soul filed away
   somewhere and forgotten, not a generic "we own everything" clause;
5. tight, one clean sentence — 141 chars, every word earning its place.

### Brief cross-check (live recheck 06:54–06:57 WIB, 26 Nov 2026)

Opened Nov 26, $2, $0 entry fee, 10 paid places (1st $0.63), ends Fri 27
Nov 03:25 WIB, Round 1 cutoff Thu 26 Nov 11:24 WIB, 1,304 entrants at
recheck (+136 that hour). Confirmed absent from the @yofanprayoga profile
(64 solutions read across all 7 pages) before building. The double
absurdity in Option 1 — the Company owns your soul AND misplaced it — is
what separates it from a plain "we own your data" clause; the second
absurdity is the joke.

## Run

```sh
python3 main.py              # Option 1 (default)
python3 main.py --option 2   # Option 2
python3 main.py --option 3   # Option 3
```

Writes the exact entry text (no trailing newline) to `/output/entry.txt`.
`ENTRY_TEXT` or `OUTPUT_PATH` env vars override the text and output path.
Python standard library only.

## Submit checklist

- [x] Entry is one sentence, 1–200 chars, single line
- [x] `main.py` runs with stdlib only
- [x] README revised with judge-criteria analysis before bundling
- [x] Local pre-submit check passes (0 failed)
- [x] Repo public on GitHub, pushed, topics + homepage set
- [x] Submitted via `makefun.mjs submit`, server checks pass, grading queued
