# Noirwash dashboard asset fan-out

Session-derived asset workflow for the BlockDAG/Noirwash dashboard redesign.

## What worked

- Generated the main photographic assets with the local Hermes OpenAI-Codex image provider via `python <this skill>/scripts/generate_codex_image.py`.
- Used text-free prompts for the photographic assets and added exact UI text in code instead of asking the model to render typography.
- Created logos, favicon, and nav icons as SVGs directly in the repo for crisp small-size rendering.
- Wired the new assets into the dashboard through a dedicated `/assets/` static route and a favicon route.

## Asset set that was useful

- `hero-noirwash.png` — cinematic hero backdrop for the Overview tab.
- `water-beads.png` — macro detail image used as a supporting visual tile.
- `ambient-dark-bg.png` — subtle atmospheric texture for the whole page.
- `chrome-wheel-detail.png` — optional supporting detail image.
- `favicon.svg`, `logo-mark-solo.svg`, `brand-lockup.svg` — brand identity.
- `icon-nav-*.svg` — small nav glyphs for each tab.

## Practical rules

1. Prefer SVG for logo, favicon, and nav icons.
2. Prefer AI image generation for hero/background/detail photos.
3. Keep image prompts text-free when exact wording matters in the UI.
4. Save all assets in a stable project path under `public/assets/` (or equivalent).
5. Verify the live page by fetching HTML and checking for the actual asset URLs in the served output.

## Pitfalls

- A successful file write does not guarantee the running server is serving the new template; verify the live HTML after restart.
- When the hosted image backend is unavailable, the local Codex provider script is a reliable fallback for production-grade image generation.
- If a visual refactor is mostly aesthetic, keep backend/behavior changes minimal so existing tests remain green.
