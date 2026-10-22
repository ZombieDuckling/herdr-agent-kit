# Landing Page Asset Fan-Out Pattern

Use this reference when a development task asks for a polished landing page that combines generated imagery, logos/assets, external coding-agent input, local verification, and deployment.

## Class-level pattern

1. **Scaffold first.** Create a small working app and stable asset directories before generation, e.g. `public/assets/`, `public/icons/`, and `docs/`.
2. **Generate real assets early.** Use `image_generate` or `scripts/generate_codex_image.py` to write hero/macro/OG imagery directly to `public/assets/<descriptive-name>.png`. Prefer text-free images and overlay exact text in React/CSS/SVG.
3. **Create vector brand primitives by hand.** For logos, favicons, and wordmarks, author SVG first; use image generation only for concept inspiration.
4. **Fan out design/review agents safely.** Give Claude/Cursor/OpenCode non-overlapping ownership such as `docs/<agent>-brief.md` so they can contribute design, motion, and QA guidance without racing on source files.
5. **Hermes integrates and verifies.** Hermes owns final source edits, asset wiring, build, local preview, browser open, deployment, and proof. Do not trust agent self-reports.
6. **Deploy and prove it.** Run the canonical build, deploy (for example Vercel), `curl -I` the production URL, and open it in the requested desktop browser when asked.

## Good worker split

- Claude: creative direction / copy / section rhythm brief.
- Cursor: UI motion / responsive / interaction brief.
- OpenCode: QA / performance / deployment checklist.
- Hermes: final implementation, conflict control, verification, deploy.

## Aesthetic iteration pass

If the user reacts with an intensity instruction after the first deployment — e.g. “make it more cinematic,” “make it feel more premium,” “make it darker,” or “make it more fluid” — treat it as a second-pass asset+CSS iteration, not a full rebuild.

Useful cinematic upgrades:

- Generate one new supporting image that targets the missing mood, e.g. `cinematic-tunnel.png` for a wash-tunnel film still.
- Add atmospheric CSS layers: film-gate/letterbox bars, projector haze, volumetric light beams, grain, vignettes, lens flares, rain/water streaks.
- Add small production-design details: scene slates, frame counters, shot-list copy, ghosted oversized background typography.
- Keep exact text in HTML/SVG/CSS, not inside generated images.
- Respect `prefers-reduced-motion` by disabling decorative loops and high-motion overlays.
- Rebuild, redeploy, verify the aliased production URL and the new asset URL.

## Prompt recipe for supporting cinematic image

```bash
python <this skill>/scripts/generate_codex_image.py \
  --prompt "Text-free cinematic wide photograph for <brand/category>: <subject>, moody <setting>, volumetric light beams, water/mist/reflections, anamorphic lens flare, premium film still, no text, no logo, no watermark" \
  --aspect landscape \
  --out ./public/assets/cinematic-<subject>.png
```

## Asset checklist

- Hero image has dimensions and `fetchPriority="high"` when above the fold.
- Below-fold images have `loading="lazy"` and width/height attributes.
- OG image exists and `index.html` points to it.
- SVG logo has title/description and meaningful alt text where used.
- Generated images are copied into project paths, not left only in Hermes cache.

## Verification checklist

- [ ] `npm run build` or the project’s canonical build command passes.
- [ ] Generated assets exist in stable project paths and have non-zero size.
- [ ] Production deployment returns HTTP 200.
- [ ] Newly added assets return HTTP 200 from production.
- [ ] Safari opens the final production URL on macOS when requested.
- [ ] Final response includes the live link, changed asset names, and real verification results.

## Avoid

- Letting multiple agents edit `src/App.jsx` or `src/styles.css` at the same time.
- Asking image models to render exact brand text.
- Reporting a deployed link before a real HTTP 200 check.
- Treating an aesthetic revision as “just copy changes”; it often needs one additional generated asset plus code-level atmosphere.
