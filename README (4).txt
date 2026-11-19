# makefun-news-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119) [![rank](https://make.fun/badge/news-image-20261119/Fauziwildan0856/makefun-news-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119) [![reward](https://make.fun/badge/news-image-20261119/Fauziwildan0856/makefun-news-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

One image that sums up the world news of Thursday 19 November 2026,
built for the make.fun bounty "Sum up 19 November's world news in one
image": https://make.fun/bounty/news-image-20261119

## The picture

`entry.png` is a 1024x1024 front page, "THE WORLD TODAY", dated
Thursday 19 November 2026. It carries 32 stories from 6 continents:
the first Trump-Xi-Putin trilateral summit in Shenzhen as the lead,
the ICJ ruling 9-6 that Myanmar committed genocide against the
Rohingya, the Iran-Gulf escalation, plus a world-map panel showing
where the day's news happened and a ticker along the bottom.

## How to run

```
python3 main.py
```

That writes the picture to `/output/entry.png`. The program uses only
the Python standard library, touches no network, and produces exactly
the same bytes on every run; it even checks the copy's SHA-256 against
the original before reporting success.

## Files in this repo

- `entry.png` — the front-page image itself (1024x1024, under the
  1 MiB limit).
- `main.py` — the entry program described above.
- `build_image.py` — the generator that composed `entry.png` from the
  day's verified headlines.
- `.makefun/owner.json` — the entrant's public Solana wallet address,
  proving this repository belongs to the make.fun account entering it.
- `LICENSE` — MIT.

## The bounty

$250 in total, 50 places paid: 1st $50, 2nd $30, 3rd $15, 4th-10th $5
each, 11th-50th $3 each. Entries closed Saturday 21 November 2026 at
07:00 WIB. It is a competition, so only the top 50 entries are paid;
entering is free and nothing is guaranteed.
