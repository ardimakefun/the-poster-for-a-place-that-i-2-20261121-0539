[![make.fun · the-poster-for-a-place-that-i-2-20261121-0539](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/ardimakefun/the-poster-for-a-place-that-i-2-20261121-0539/rank.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/ardimakefun/the-poster-for-a-place-that-i-2-20261121-0539/reward.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)

# ONDRINE — The Wave That Never Breaks

A travel poster for a place that does not exist, for the make.fun bounty
[The Poster for a Place That Isn't There](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539).

**The place:** Ondrine, a seaside town where a colossal wave stands frozen
mid-crash, its glass lip curled over the promenade forever. Cafes serve
coffee beneath it; the sun shines through the barrel at golden hour.

**The poster:** one impossible landmark, huge and central; warm light
against a blue-teal sea; people strolling and taking coffee under the
wave; the name set big into the sky. Flat vector style, drawn by
`render_poster.py` (Pillow, local render only).

**The program:** `main.py` (Python 3.13, standard library only) copies
the committed `entry.png` to `/output/entry.png`, so every run delivers
the exact same bytes. `entry.png` is 1024x1024, well under the 1 MiB cap.

```sh
python3 main.py
# writes /output/entry.png — 1024x1024
```

Reference: dev leaderboard top 10 checked 2026-11-21 ~15:26 WIB
(#1 SUVENNE 0.876, #2 SOLMERE 0.846, #3 MARELUNE 0.841) — the winning
pattern is one giant impossible landmark + golden-hour coast + people
enjoying a stay + the name set into the picture. Ondrine follows it
with a landmark none of the top 10 uses.
