# Cinematic wellness image systems

Session-derived pattern from the Everleaf Dietetics redesign.

Use when the user says a wellness/dietician/clinic site should feel dark, cinematic, flowing, relaxing, inviting, or that images should not just sit inside cards.

## Design direction

- Treat generated imagery as atmosphere and structure, not content thumbnails.
- Generate more assets than a minimal page needs: route backgrounds, section backgrounds, texture overlays, appointment/background art, resource/goals imagery, and hero fields.
- Use text-free images only; overlay exact copy in HTML/CSS.
- Blend images into the page with CSS backgrounds, pseudo-elements, gradients, masks/clip paths, opacity, and overlays.
- Prefer dark olive/espresso/black with warm amber/brown highlights when the user asks for “black cinematic”.
- Keep typography calm; avoid giant shouty hero text even if cinematic.

## Implementation pattern

1. Generate an asset burst:
   - `dark-hero-cinematic.png`
   - `dark-services-cinematic.png`
   - `dark-meal-cinematic.png`
   - `dark-appointment-cinematic.png`
   - `dark-resources-cinematic.png`
   - `dark-goals-cinematic.png`
   - optional texture/ambient backgrounds
2. Copy assets into stable `assets/` paths immediately.
3. Give each page a body class such as `page-home`, `page-services`, `page-goals`, etc.
4. Set page-level background variables in CSS, e.g. `--page-bg:url('assets/dark-services-cinematic.png')`.
5. Use `:before` / `:after` pseudo-elements for cinematic background fields, not only `<img>` tags.
6. Add section bands that flow into each other with background images, gradients, elliptical clip paths, opacity, and dark overlays.
7. Keep forms readable with a lighter foreground surface, but keep the surrounding appointment section cinematic.
8. Add scroll reveal/fly-in motion, with `prefers-reduced-motion` fallback.

## Anti-patterns to avoid

- Treating every generated image as a card image.
- Stopping after local file creation without deploying and verifying the live alias.
- Overcorrecting “AI slop” into rigid ledger/editorial UI when the user asked for soft/liquid/wellness flow.
- Visible `01 / 02 / 03` step blocks unless requested.
- Placeholder language on a client demo (“placeholder testimonial”, “placeholder copy”). Use realistic demo-safe wording instead.
- Huge bold text as a substitute for cinematic composition.

## Verification

- Static checks: every page has logo, full nav, page class, no placeholder wording, no numeric step spans.
- Asset checks: every generated background returns HTTP 200 locally and live.
- CSS checks: cinematic assets referenced, reveal animation styles present, and page body classes map to page backgrounds.
- Browser screenshots: desktop/mobile home plus representative new pages and appointment page.
- Deploy and verify the live alias directly; do not trust deploy CLI exit status alone if it prints successful alias output.
