# Flowing demo-site image systems

Use this when the user says a site feels like images were just dropped into cards, or asks for images to flow seamlessly through the design.

## Lesson

For modern clinic/wellness/service demo sites, do not treat generated images only as `<img>` content blocks. Generate a larger asset set and use images as visual material:

- full-page background washes
- section-specific background fields
- soft texture overlays
- footer/CTA atmospheric layers
- organic masked hero art
- low-opacity pseudo-elements behind copy
- page-class-specific background variables

## Asset burst pattern

Generate more than the obvious 2–3 page images. Include:

- hero flow background
- services flow background
- meal-planning / education flow background
- appointment / consult background
- subtle paper/leaf texture
- abstract brand wash / liquid nutrition texture
- logo mark / SVG lockup separately, with exact text handled in SVG/code

Save with stable names, e.g.:

```text
assets/bg-hero-flow.png
assets/bg-services-flow.png
assets/bg-meal-flow.png
assets/bg-appointment-flow.png
assets/bg-paper-leaf-texture.png
assets/bg-liquid-nutrition.png
assets/brand-logo.svg
assets/brand-mark.svg
```

## Integration pattern

Use CSS variables and page body classes:

```css
body::before { background: url('assets/bg-paper-leaf-texture.png') center/cover; opacity: .2; }
.hero::before { background: var(--flow-img) center/cover; opacity: .7; }
.page-services { --flow-img: url('assets/bg-services-flow.png'); }
.page-meals { --flow-img: url('assets/bg-meal-flow.png'); }
```

Blend images into the composition rather than boxing them:

- `::before`/`::after` image layers behind sections
- asymmetric `border-radius` for soft brown corners
- `mix-blend-mode: multiply` or low-opacity overlays when appropriate
- large organic background fields with cream gradients over them
- avoid every image appearing in a bordered card

## Anti-patterns

- generating assets but leaving the live site on the old one-page design
- using page-specific images only as card thumbnails
- limiting generation to exactly one hero + two support images when the user asks for richness
- visible `01 / 02 / 03` step blocks unless the design genuinely calls for them
- overcorrecting from generic SaaS slop into hard, encoded, ledger-like UI when the desired direction is soft/flowing

## Verification

Before reporting done:

- check live pages reference the logo and multi-page routes
- fetch all new background assets via HTTP
- inspect CSS for background references, not just `<img>` references
- capture desktop + mobile screenshots
- verify the live alias after Vercel, because deploy CLI may print success/alias while still returning nonzero
