# Vanguard Venture Society — Design System

> "Digital Noir" — high-end business exclusivity meets deep-tech. Light-on-dark,
> cinematic depth, glassmorphism, and a single luminous accent.

This is an **extracted reference** of the design tokens, captured in
[`shared/theme.js`](shared/theme.js) (Tailwind tokens) and
[`shared/theme.css`](shared/theme.css) (CSS variables + UI primitives).

> **Note:** the screens in `screens/` are verbatim Stitch exports and each keeps
> its own original inline styling, so they render exactly as designed in Stitch.
> They do **not** import these shared files. This spec documents the common
> language across them; applying it uniformly would recolor some screens (see the
> two-variant note under "Accent").

## Accent

The system uses **one** accent, exposed as `--vv-accent` (CSS) and
`primary-container` / `electric-blue` (Tailwind).

| Role        | Value     | Notes                                   |
| ----------- | --------- | --------------------------------------- |
| **Accent**  | `#2563EB` | Electric Blue — matches the brand logo/nebula art |
| Accent dim  | `#3B82F6` | Hover / bright variant                  |
| _(alt)_     | `#00E5FF` | Original Cyan — see "Reskinning" below  |

> The Stitch screens shipped as two drifting variants (a Cyan "Digital Noir" set
> and a Blue "Industrial Blueprint" set). They are now unified on Electric Blue,
> since the brand mark and the majority of screens already used it.

## Color tokens

| Token                       | Hex       | Use                          |
| --------------------------- | --------- | ---------------------------- |
| `background`                | `#0A0A0B` | Deep Obsidian — base canvas  |
| `surface` / `surface-dim`   | `#131314` | Base surface                 |
| `surface-container-lowest`  | `#0E0E0F` | Footers, recessed sections   |
| `surface-container`         | `#201F20` | Cards                        |
| _raised (CSS `--vv-surface-raised`)_ | `#161618` | Glass / panel fill   |
| `on-surface`                | `#E5E2E3` | Primary text                 |
| `on-surface-variant`        | `#BAC9CC` | Secondary text               |
| `outline`                   | `#849396` | Hairlines, tertiary text     |
| `primary`                   | `#B4C5FF` | Accent text/icons on dark    |
| `primary-container`         | `#2563EB` | Accent fills / CTAs          |

Hairlines are 1px translucent white (`rgba(255,255,255,0.05–0.10)`).

## Typography

| Family              | Role                                   |
| ------------------- | -------------------------------------- |
| **Inter**           | Headlines + body (`400/600/700/800`)   |
| **JetBrains Mono**  | Labels / metadata — UPPERCASE, `0.1em` tracking |
| **Playfair Display**| Editorial accents (rankings, display-lg) |

Scale (`fontSize` tokens): `headline-display` 72px · `headline-lg` 48px ·
`headline-md` 24px · `body-lg` 18px · `body-md` 16px · `label-sm` 12px.

## Shape & spacing

- **Radius:** sharp-leaning. `DEFAULT` 2px · `lg` 4px · `xl` 8px · `full` 12px.
- **Spacing:** 8px rhythm. `gutter` 24px · `margin-mobile` 20px ·
  `margin-desktop` 64px · `container-max` 1280px.

## Elevation

Depth comes from **translucency + blur + inner glow**, not drop shadows.

- **Base:** `#0A0A0B`.
- **Glass (`.glass-card` / `.glass-panel` / `.forged-panel`):** `rgba(22,22,24,0.6)`,
  `backdrop-filter: blur(40px)`, 1px translucent border, diagonal top-left sheen.
- **Accent glow:** `box-shadow: 0 0 20px rgba(37,99,235,0.2)`.

## Shared UI primitives (in `theme.css`)

| Class                                   | Purpose                                  |
| --------------------------------------- | ---------------------------------------- |
| `.glass-card` / `.glass-panel` / `.forged-panel` | Glassmorphic surfaces           |
| `.industrial-border` / `-accent`        | Technical corner-ticked / left-rule borders |
| `.blueprint-grid` / `.blueprint-bg` / `.blueprint-lines` | Grid backdrops          |
| `.primary-glow` / `.glow-cyan` / `.industrial-glow` / `.noir-glow` | Accent box-glow |
| `.text-glow` / `.cyan-glow-text`        | Accent text-shadow                       |
| `.cyan-border-hover` / `.glow-border` / `.electric-glow` | Hover accent border     |
| `.draft-card` / `.gate-line` / `.step-line` / `.timeline-line` | Accent connectors  |
| `.gritty-photo`                         | Grayscale→color photo treatment          |
| `.animate-pulse-cyan`                   | Status pulse                             |

> Class names keep their original Stitch spellings (e.g. `glass-card` vs
> `glass-panel`, `cyan-*`) so the imported markup renders unchanged — they all
> now resolve to the **same** unified, accent-driven styles.

Page-specific motion (tickers, marquees, odometers) remains in each screen's own
`<style>` block.

## Reskinning the whole system

1. In [`shared/theme.css`](shared/theme.css): change `--vv-accent`,
   `--vv-accent-rgb`, `--vv-accent-bright`.
2. In [`shared/theme.js`](shared/theme.js): change `primary-container`,
   `electric-blue`, `surface-tint`, `primary-fixed-dim`.

To revert to the original Cyan: accent `#00E5FF`, rgb `0,229,255`, bright `#00DAF3`.
