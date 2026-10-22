---
name: dev-asset-generation
description: Use when a software project needs images, logos, icons, favicons, Open Graph images, app-store screenshots, hero art, placeholders, or brand assets generated on the fly during development. Guides when to use SVG/code vs AI image generation, where to save assets, how to verify them, and how to fall back to the user's ChatGPT/Codex image backend.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [image-generation, logos, design-assets, development, branding, ai-images, svg]
    related_skills: [popular-web-designs, frontend-design, claude-design]
---

# Development Asset Generation

## Overview

Use this skill to create project assets while building: logos, app icons, favicons, OG/social cards, hero illustrations, empty-state art, background textures, avatars, product mockup images, and development placeholders.

The goal is *shipping momentum*: create useful assets immediately, save them into the project in the right format and location, wire them into the app when appropriate, and verify they render. Do not stop at a prompt suggestion. Produce files.

Default quality strategy:

1. **SVG/code first for logos, icons, and UI primitives** — precise, editable, scalable, fast, no model weirdness.
2. **AI image generation for hero art, mascots, rich illustrations, textures, and realistic/social imagery** — use `image_generate` when available.
3. **ChatGPT/Codex image fallback** — when configured image generation fails (for example FAL key missing), use the user's local Hermes `openai-codex` image-gen provider via the helper script in this skill.
4. **Text overlay in code** — avoid asking image models to render exact text unless necessary. Generate text-free art, then add exact text in HTML/CSS/SVG/Pillow/Canvas.

## When to Use

Use this skill when the user says or implies:

- "make a logo", "create branding", "need an icon", "favicon", "app icon"
- "generate an image for this app", "hero image", "illustration", "mascot"
- "we need assets while building", "placeholder art", "Open Graph image"
- "make it look real", "add polish", "make screenshots/assets"
- during frontend development when an asset is blocking visual completion

Do *not* use this skill for:

- final legal trademark work without user review
- production brand systems requiring stakeholder approval
- user-provided copyrighted likenesses unless the user has the rights
- exact text-heavy posters unless you plan to overlay text programmatically

## Asset Decision Matrix

| Need | Best artifact | Primary method | Verification |
|---|---|---|---|
| Logo mark | SVG + PNG export | Hand-code SVG or vector design | Render at 32px, 128px, 512px |
| Wordmark | SVG text converted or CSS text | Code/HTML/SVG, not AI text | Check exact spelling |
| Favicon | SVG + PNG/ICO | Derive from logo mark | Browser tab shows correctly |
| App icon | 1024 PNG + downscaled sizes | SVG base or AI mascot | Check rounded-mask crop |
| Hero image | PNG/WebP | AI image generation | Visual inspect at target aspect |
| OG/social card | 1200x630 PNG | HTML/SVG template + screenshot or AI bg + text overlay | Metadata preview size |
| Empty state | SVG/PNG | Simple SVG illustration or AI | Renders in component |
| Texture/background | WebP/PNG | AI or CSS gradient | File size acceptable |

## Workflow

For full landing pages that combine generated imagery with external coding-agent input, see `references/landing-page-asset-fanout.md` for the scaffold → generate assets → fan-out briefs → Hermes integration → deploy verification pattern. When the user asks for an aesthetic intensity change after seeing the deployed page (for example “make it more cinematic”), treat it as an asset+CSS iteration pass: add or regenerate one targeted supporting image, layer atmosphere/motion in code, rebuild, redeploy, and reopen/verify the live URL.

For quick static website/app demos that need generated imagery and Vercel deployment, see `references/static-demo-site-vercel.md`: confirm whether the user wants a separate project, generate text-free domain assets, copy them into stable `assets/` paths, build dependency-free front-end files, verify locally over HTTP, deploy to Vercel, and verify the live alias directly.

When the user says a demo site is too one-page / too generic / needs more pages, more images, a generated logo, or logo branding instead of text, use `references/static-demo-multipage-anti-slop.md`: treat it as a multi-page information-architecture + asset pass, keep the active project/domain isolated from stale context, generate page-specific imagery, create an SVG logo/mark, wire the logo into nav/footer/favicon, verify every page locally, then redeploy and verify the live alias.

When a demo is promoted from one-page prototype to client-facing multi-page site, generate or author a complete brand asset set instead of leaving text placeholders: SVG logo lockup, mark/favicon, page-specific hero images, and stable filenames for each page. Prefer SVG/code for the logo and text-free AI images for page art. Wire the logo into nav/footer and use page-specific images so each route feels intentional rather than like a stretched landing page.

If the user says the images feel like they are merely displayed in cards, or asks for many images / seamless / flowing / liquid design, switch to the pattern in `references/flowing-demo-site-image-systems.md`: generate an asset burst of page backgrounds, abstract textures, and section washes, then integrate them as CSS backgrounds, overlays, pseudo-elements, and organic image fields rather than only `<img>` cards. If they later rejects a visual pivot, keep the generated assets but swap route/CSS references back to the preferred palette and verify no stale asset family remains live.

If the user pivots a wellness/dietician/clinic site toward “black cinematic”, relaxing, inviting, scroll-flowing, or says not to use big bold text, use `references/cinematic-wellness-image-systems.md`: generate dark cinematic route/section backgrounds, wire them as CSS backgrounds/pseudo-elements, add calm scroll reveal/fly-in motion with reduced-motion fallback, remove placeholder wording and numeric-step tropes, then deploy and verify the live alias directly. If they then says the light scheme was better, revert the color system and asset references immediately rather than defending the dark concept.

### 1. Extract the asset brief

Before generating, infer or inspect:

- Project name and product category.
- Audience and tone: developer, enterprise, playful, luxury, cyber, fintech, etc.
- Existing palette, typography, and UI style from the codebase when available.
- Required dimensions and final destination.
- Whether the asset needs exact text.

Completion criterion: you can state the asset type, style, dimensions, output paths, and integration target.

### 2. Choose SVG/code vs AI

Use **SVG/code** when the asset must be crisp, exact, reusable, small, and brand-like:

- logos
- icons
- favicons
- line art
- diagrams
- badges
- simple mascots
- exact text or letters

Use **AI image generation** when the asset benefits from texture, depth, realism, illustration richness, or a warmer human-facing feel:

- hero images
- mascot portraits
- social preview backgrounds
- cinematic product imagery
- rich illustrations
- decorative textures
- relationship/contact-facing capability maps or explanatory infographics, when a hand-coded SVG would feel too rigid

Completion criterion: the chosen method is justified by the asset's constraints, not by convenience. For WhatsApp capability-map images, see `references/whatsapp-capability-map-images.md`: generate with ChatGPT/Codex, verify text legibility with vision, then send.

### 3. Generate the asset

#### Preferred: built-in `image_generate`

Use `image_generate` for rich assets when the active backend is available:

```text
Prompt structure:
<asset type> for <project/product>, <visual subject>, <style>, <palette>, <composition>, <lighting/material>, <constraints: no text / transparent background / centered>, <quality notes>
```

Examples:

```text
A premium SaaS hero illustration for a cybersecurity agent platform: a luminous command graph flowing through dark glass nodes, emerald and electric-blue accents, high-contrast black background, clean negative space on the left for headline text, no text, no logo, 16:9.
```

```text
A friendly robot duck mascot for a developer tool, geometric vector-like 3D style, yellow beak, subtle cyberpunk visor, dark slate background, centered, no text, square app icon composition.
```

After generation, save/copy the returned file into the project asset directory.

#### Fallback: ChatGPT/Codex image provider script

If `image_generate` fails because the configured backend is unavailable, use the helper script:

```bash
python <this skill>/scripts/generate_codex_image.py \
  --prompt "A polished text-free hero image for ..." \
  --aspect landscape \
  --out ./public/assets/hero.png
```

The script uses the user's Hermes `openai-codex` image generation provider (`gpt-image-2`) through existing ChatGPT/Codex OAuth. It saves a local PNG and prints its path.

Completion criterion: a real file exists at the intended path and has non-zero size.

### 4. Save in conventional project locations

Pick a path that fits the stack:

- Vite/Next/static web: `public/assets/`, `public/images/`, `public/logos/`, `public/icons/`
- React component-local assets: `src/assets/`
- Electron assets: `assets/`, `build/icons/`, `public/`
- App icons: `public/icon.png`, `public/favicon.svg`, `public/favicon.ico`, `build/icon.icns`
- OG images: `public/og.png` or `public/og/<slug>.png`
- Generated scratch assets: `generated/assets/` only if not production-bound

Use descriptive names:

```text
logo-mark.svg
logo-horizontal.svg
favicon.svg
app-icon-1024.png
hero-cyber-command.png
og-home.png
empty-state-no-projects.svg
```

Completion criterion: every generated asset has a stable, meaningful filename and is not stranded in `/tmp` or a cache folder unless intentionally temporary.

### 5. Create derivative sizes when needed

For SVG logos, also export PNG sizes if the app needs them. Use built-in macOS tools, `sips`, ImageMagick, or Python if available.

Examples:

```bash
# Resize a PNG app icon into common web sizes
mkdir -p public/icons
sips -z 512 512 app-icon-1024.png --out public/icons/icon-512.png
sips -z 192 192 app-icon-1024.png --out public/icons/icon-192.png
sips -z 32 32 app-icon-1024.png --out public/favicon-32.png
```

If SVG to PNG conversion is needed and no renderer is available, prefer browser screenshot or `qlmanage`/`rsvg-convert` when installed.

Completion criterion: required sizes exist and are generated from the master asset, not independently hallucinated.

### 6. Wire the asset into the app

If the asset was requested for a development task, integrate it immediately:

- Update `img src`, CSS `background-image`, manifest icon path, metadata/OG image tags, or component imports.
- For logos, ensure `alt` text is present.
- For decorative images, use empty `alt=""` or CSS background appropriately.
- Avoid bloating the app with multi-megabyte PNGs; use WebP/JPEG for photographic art when supported.

Completion criterion: the app references the new asset path and no broken import/path remains.

### 7. Verify visually and technically

Minimum verification:

```bash
file path/to/asset.png
```

For web apps, run or use the existing dev server and verify the rendered page. If browser/computer-use tools are available, inspect screenshots. For SVG, read the file and check it is valid XML-ish SVG with correct viewBox.

Visual checks:

- Looks correct at target size and crop.
- Logo remains legible at small sizes.
- No accidental text gibberish from AI model.
- Transparent/opaque background matches use case.
- Colors fit the existing UI.
- File size is reasonable.

Completion criterion: real command/tool output proves the files exist, and visual inspection or render verification confirms they are usable.

## Logo-Specific Rules

1. **Prefer vector first.** A logo should normally start as SVG, not PNG.
2. **Use simple geometry.** Logos need silhouette recognition at 16–32px.
3. **Avoid exact letters generated by AI.** If using initials, draw them as SVG text/paths or overlay text programmatically.
4. **Make variants.** At minimum: mark-only, horizontal lockup, monochrome, favicon.
5. **Check tiny sizes.** If it fails at 32px, simplify.
6. **Keep source editable.** Do not only save a flattened raster unless the user explicitly wants a quick placeholder.

## Prompt Recipes

### Logo mark prompt for AI concepting

Use AI for inspiration, then recreate/refine in SVG:

```text
Minimal vector logo mark concept for <project>, <symbol/metaphor>, geometric, strong silhouette, single-color friendly, no text, centered on plain background, works as app icon, modern SaaS brand, high contrast.
```

### Hero image prompt

```text
Text-free hero image for <project>, <audience>, showing <scene/metaphor>. Style: <design-system style>. Palette: <colors>. Composition: <left/right negative space for UI copy>. Lighting/material: <details>. Constraints: no text, no watermark, no UI labels, production-grade, 16:9.
```

### App icon prompt

```text
Square app icon for <app>, centered <mascot/symbol>, simple strong silhouette, soft depth, <palette>, rounded-square safe composition, no text, no letters, recognizable at small sizes, 1024x1024.
```

### OG card prompt

Generate the background only, then overlay exact text in code:

```text
Abstract background for an Open Graph social preview card for <product>, <style>, high contrast, clean space for large title text, no text, no logo, 1200x630 composition.
```

## Scroll-Scrubbed Motion Sequence Pattern

When the user wants the page to feel like motion through a story, use a scroll-scrubbed image sequence instead of decorative CSS animation:

1. Generate or source a **start frame** and **end frame** with matching camera angle, subject scale, lighting, and composition.
2. Generate the in-between frames with video/interpolation tooling (Runway/Pika/Kling/ComfyUI video nodes/RIFE/FramePack/etc.) or render a short video and extract frames.
3. Export 40–120 frames as numbered WebP/JPEG files, e.g. `public/sequence/wash-0001.webp`.
4. Preload the first few frames, then lazy-preload the rest.
5. Use scroll progress to choose a frame: `index = Math.round(progress * (frameCount - 1))`.
6. Render to a `<canvas>` or a single `<img>` whose `src` changes. Canvas gives smoother control; `<img>` is simpler.
7. Pin the sequence section for 200–500vh so scrolling feels like moving through the shot.
8. Add content beats at progress thresholds, not separate cards, so copy emerges from the motion.
9. Respect `prefers-reduced-motion`: show a static key frame or allow normal scrolling.

Completion criterion: scrolling the section visibly scrubs through a coherent shot, not just parallaxing a still image.

Reusable files:

- `scripts/make_scroll_sequence.py` — reliable ffmpeg baseline that turns two keyframes into numbered WebP/JPEG/PNG frames. Treat simple start/end blending as a fallback only, not proof of convincing motion.
- `templates/ScrollSequenceCanvas.jsx` — React canvas scrubber component.
- `templates/scroll-sequence.css` — base CSS for a pinned sequence section.
- `references/scroll-scrub-sequence.md` — full recipe and verification checklist.
- `references/scroll-scrub-sequence-reality-check.md` — correction note: plumbing, 200-status frame URLs, or a soft dissolve are not enough; test actual rendered visual motion.

Hard rule for scroll-scrub work: do not report success until you have generated actual visible frames, integrated them, opened/tested the rendered page, and inspected a contact sheet or preview. If the sequence is not visibly changing during scroll, say it is not done.

## Common Pitfalls

1. **Letting AI render exact text.** It will often misspell. Generate a text-free image and overlay exact text with HTML/SVG/Pillow.
2. **Saving only to cache.** Move generated assets into the project and use stable filenames.
3. **Skipping small-size logo checks.** A pretty 1024px mark can fail as a favicon.
4. **Using PNG when SVG is better.** Logos and icons should usually be vector.
5. **Ignoring file size.** Hero PNGs can be huge. Convert to WebP/JPEG when production-bound.
6. **Not matching the app style.** Inspect existing colors/components before generating.
7. **Forgetting licensing.** Check exact model/license before commercial release if using local or third-party model outputs.
8. **Over-polishing placeholders.** During development, ship a useful asset quickly; revisit final brand work later.
9. **Defaulting to AI-slop layout tropes.** Big generated images should not be trapped inside rounded cards with obvious gradients. For story-driven landing pages, prefer full-bleed or edge-to-edge imagery, hard editorial cuts, intentional sequencing, and a clear visual narrative so the user feels they are moving through a story rather than looking at a vibe-coded template.
10. **Ignoring the product domain.** If the user corrects the context (for example, from a lifestyle/consumer aesthetic to an industrial or operational one), discard the earlier visual language and regenerate assets for the new domain instead of re-labeling the old imagery. For mining/infra dashboards, use rack diagrams, boards, telemetry, LEDs, gauges, and technical close-ups—not cinematic, automotive, or aspirational photography.

Reference: see `references/practical-industrial-dashboard-assets.md` for a condensed checklist, anti-patterns, and the local PNG fallback pattern from the BlockDAG mining dashboard correction session.

## Verification Checklist

- [ ] Asset type, dimensions, destination, and style were identified.
- [ ] Correct method chosen: SVG/code for precise assets; AI for rich imagery.
- [ ] Generated or authored files exist at stable project paths.
- [ ] Required derivative sizes/formats were created.
- [ ] Asset is wired into the app or documented as ready-to-use.
- [ ] Logo/icon was checked at small sizes.
- [ ] No AI-garbled text appears in the final asset.
- [ ] File size is acceptable for the app context.
- [ ] Final response includes paths and verification results.
