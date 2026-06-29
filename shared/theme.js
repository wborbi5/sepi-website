/* ============================================================
   Vanguard Venture Society — Tailwind theme (single source of truth)
   Loaded by every screen AFTER the Tailwind Play CDN so the CDN
   picks up these tokens. Unifies the Stitch screens onto one
   palette: "Obsidian" surfaces + a single Electric Blue accent.

   To switch the whole system to the original Cyan accent, change
   the three accent values below (and --vv-accent in theme.css):
     primary-container / electric-blue / surface-tint  ->  #00E5FF
   ============================================================ */
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        /* Surfaces — Obsidian */
        "background": "#0A0A0B",
        "surface": "#131314",
        "surface-dim": "#131314",
        "surface-bright": "#3a393a",
        "surface-variant": "#353436",
        "surface-container-lowest": "#0e0e0f",
        "surface-container-low": "#1c1b1c",
        "surface-container": "#201f20",
        "surface-container-high": "#2a2a2b",
        "surface-container-highest": "#353436",
        "surface-tint": "#2563EB",

        /* Text / on-colors */
        "on-background": "#e5e2e3",
        "on-surface": "#e5e2e3",
        "on-surface-variant": "#bac9cc",
        "outline": "#849396",
        "outline-variant": "#3b494c",
        "inverse-surface": "#e5e2e3",
        "inverse-on-surface": "#313031",

        /* Accent — Electric Blue (canonical) */
        "primary": "#b4c5ff",
        "primary-container": "#2563EB",
        "on-primary": "#00204e",
        "on-primary-container": "#dbe1ff",
        "primary-fixed": "#dbe1ff",
        "primary-fixed-dim": "#3B82F6",
        "inverse-primary": "#2563EB",
        "electric-blue": "#2563EB",
        "electric-blue-bright": "#3B82F6",

        /* Secondary / tertiary (Obsidian set) */
        "secondary": "#c4c6cc",
        "secondary-container": "#46494e",
        "on-secondary": "#2d3135",
        "on-secondary-container": "#b6b8be",
        "tertiary": "#efecef",
        "tertiary-container": "#d3d0d2",
        "on-tertiary": "#303032",
        "on-tertiary-container": "#5a595b",

        /* Status */
        "error": "#ffb4ab",
        "error-container": "#93000a",
        "on-error": "#690005",
        "on-error-container": "#ffdad6"
      },
      borderRadius: {
        "DEFAULT": "0.125rem",
        "lg": "0.25rem",
        "xl": "0.5rem",
        "full": "0.75rem"
      },
      spacing: {
        "unit": "8px",
        "gutter": "24px",
        "margin-mobile": "20px",
        "margin-desktop": "64px",
        "container-max": "1280px",
        "max-width": "1200px"
      },
      fontFamily: {
        "headline-display": ["Inter"],
        "headline-lg": ["Inter"],
        "headline-lg-mobile": ["Inter"],
        "headline-md": ["Inter"],
        "body-lg": ["Inter"],
        "body-md": ["Inter"],
        "label-sm": ["JetBrains Mono"],
        "data-label": ["JetBrains Mono", "monospace"],
        "display-lg": ["Playfair Display", "serif"]
      },
      fontSize: {
        "headline-display": ["72px", { "lineHeight": "1.1", "letterSpacing": "-0.04em", "fontWeight": "800" }],
        "headline-lg": ["48px", { "lineHeight": "1.2", "letterSpacing": "-0.02em", "fontWeight": "700" }],
        "headline-lg-mobile": ["32px", { "lineHeight": "1.2", "letterSpacing": "-0.02em", "fontWeight": "700" }],
        "headline-md": ["24px", { "lineHeight": "1.4", "letterSpacing": "-0.01em", "fontWeight": "600" }],
        "body-lg": ["18px", { "lineHeight": "1.6", "fontWeight": "400" }],
        "body-md": ["16px", { "lineHeight": "1.6", "fontWeight": "400" }],
        "label-sm": ["12px", { "lineHeight": "1.0", "letterSpacing": "0.1em", "fontWeight": "500" }]
      }
    }
  }
}
