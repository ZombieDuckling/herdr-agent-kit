---
name: client-site-design
description: "Use when building client demo websites."
license: MIT
---

# Client Site Design

Use this skill when building, revising, or reviewing client/demo websites, landing pages, local HTML artifacts, or Vercel/GitHub Pages-style static sites for the user.

The user is sensitive to generic AI/vibe-coded output. Prefer production-looking, context-specific, grounded client surfaces over glossy template polish.

## Core Rules

1. **No rounded corners unless explicitly requested.**
   - Default `border-radius: 0`.
   - Avoid pill navs, pill buttons, rounded cards, rounded image crops, and soft SaaS tiles unless the user specifically asks for that shape language.
   - Verify with a CSS search before shipping: no nonzero `border-radius` values.

2. **Do not overuse borders.**
   - Avoid stacked bordered cards everywhere.
   - Separate content with whitespace, typography, image fields, subtle dividers, section rhythm, and tonal shifts.
   - Hairlines are fine as deliberate editorial separators; boxed grids everywhere read as vibe-code.

3. **Use images as atmosphere, not just card thumbnails.**
   - Prefer full-width image slabs, editorial image bands, background image fields, and text sitting directly against the scene.
   - If generated images are available, integrate them throughout the scroll rather than using one hero and a few tiny cards.

4. **Motion should feel cinematic and restrained.**
   - Use scroll reveal, image drift/zoom, mild parallax, and section entrance timing.
   - Avoid noisy micro-animation everywhere.
   - Respect `prefers-reduced-motion`.

5. **Remove obvious vibe-coding tells.**
   - Fake metrics: “18 months growth,” “360° support,” arbitrary numbers.
   - Generic headings: “No destination too remote,” “Complete solution,” “Seamless experience” unless backed by specific operations.
   - Numbered SaaS cards (`01 / Feature`) when the business is not a SaaS dashboard.
   - Excessive glassmorphism, frosted panels, blur, soft rounded boxes.

6. **Write grounded operator copy.**
   - Replace brochure clichés with specific operational realities.
   - Say what actually happens: staff briefing, kit delivery, supervision, routing, Shabbos timing, separate equipment, made-after-order timing, production lead times, secure checkout handoff, collection/delivery, etc.

7. **For small handmade/commerce sites, design the actual buying path.**
   - Include categories, search prompts, product CTAs, side-menu navigation, cart/order request, contact, and clear made-to-order language when the business only creates goods after purchase.
   - Put each major topic/category on its own page when the site has distinct product classes or flows; do not bury baked goods, 3D prints, stickers, bundles, custom work, checkout, process, and contact inside one long page.
   - Treat “Products” as the umbrella route for sellable categories; keep category pages as subroutes/side-menu entries rather than making every category a top-level primary-nav peer.
   - Keep products in a data file or CMS-shaped structure where practical, so future edits do not require hunting through repeated markup.
   - For static demos, never imply card details are collected on-page; position checkout as a secure hosted payment-gateway handoff.

8. **Treat logo revisions as brand-continuity work, not automatic replacement.**
   - When the user asks to improve a logo, preserve the parts they later identify as working before inventing a new mark; if they ask to return to a former logo, restore the original structure and update only the requested colour/type details.
   - Keep explicit logo taglines such as “made to order” when they carry a core business rule; do not remove them during minimalism passes.
   - If the user asks to replace “homemade” with “made to order,” change the logo/footer language consistently while preserving the made-after-order business rule.

9. **Tune minimalist palettes and type without flattening the brand.**
   - For black/white/purple commerce sites, use purple as a crisp high-contrast accent; if it feels too muted, move to a more eye-catching saturated purple while keeping the rest restrained.
   - When the user asks for a font between a clean sans and Times New Roman, use a readable transitional serif stack such as Iowan Old Style / Palatino / Georgia rather than defaulting all the way to Times or staying in a pure sans.

## Recommended Workflow

1. Load relevant design/frontend skill(s) if available.
2. Establish the brand/context-specific visual direction.
3. Build with real assets/logos/images where possible.
4. Audit for the user anti-slop tells:
   - nonzero border radius
   - generic metrics
   - generic AI phrases
   - too many bordered boxes
   - underused imagery
   - placeholder contact details or placeholder logos
5. Verify locally/static before deploy:
   - exactly one HTML document structure
   - all referenced assets exist
   - data files such as `products.json` validate
   - no nonzero `border-radius` unless asked
   - core phrases/assets present in deployed HTML
6. Commit and push meaningful checkpoints for version control before or immediately after deploy; the user expects client sites to be kept in git, not only deployed.
7. Deploy and verify live URL + key assets.

## References

- `references/travel-landing-anti-vibecode.md` — concrete corrections from a specialist travel landing-page build.
