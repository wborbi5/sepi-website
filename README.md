# Vanguard Venture Society

UI screens for the Vanguard Venture Society ("ELITE"), imported from the Stitch
project `5130805192559942858`.

> Self-contained and **independent of the CleanWear app** around it. Nothing here
> imports from or affects `../src`. Screens are static HTML using the Tailwind
> Play CDN, so they open directly in a browser.

## Layout

```
vanguard/
├── index.html          # Screen gallery / launcher
├── DESIGN.md           # Design-system spec (extracted reference)
├── README.md           # This file
├── shared/             # Extracted design tokens — REFERENCE ONLY (see note)
│   ├── theme.js        # Tailwind tokens (colors, fonts, spacing)
│   └── theme.css       # CSS variables + shared UI primitives
└── screens/            # 12 page designs, verbatim from Stitch
```

## Screens

The 12 files in `screens/` are **exact Stitch exports** — each is fully
self-contained (its own inline Tailwind config + styles) and renders precisely as
designed in Stitch. They do not depend on anything else in this folder.

`home` · `home-v3` · `ventures` · `roster` · `membership` · `recruitment` ·
`entrepreneurship` · `forge` · `forge-v2` · `summits` · `events` · `leaderboard`

## Viewing

Open `index.html` in a browser, or serve the folder:

```bash
npx serve vanguard      # then open the printed URL
```

Each screen pulls Tailwind + fonts from CDNs, so it needs a network connection but
no build step.

## About `shared/` and `DESIGN.md`

These capture the design system in one place (tokens + reusable primitives) as a
**reference**. They are intentionally **not** wired into the screens, because the
Stitch export isn't internally uniform — it spans two accent variants (a Cyan
"Digital Noir" set and a Blue "Industrial Blueprint" set). Applying a single
shared theme would recolor some screens and they'd no longer match Stitch.

If you later want one unified look across all screens, `shared/theme.js` +
`shared/theme.css` are the starting point — see "Reskinning" in
[DESIGN.md](DESIGN.md). Until then, the screens stay faithful to Stitch.
