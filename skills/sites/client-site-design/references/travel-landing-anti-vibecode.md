# Anti-vibecode corrections: a specialist travel landing page

Session context: the user reviewed a cinematic the client landing page and called out "Lots of vibecoding tells," then clarified the design direction.

## Corrections that mattered

- Remove fake metric tiles and arbitrary credibility numbers:
  - `18 months of rapid growth`
  - `17 years Hatzolah service`
  - `360° specialist travel support`
- Remove generic travel/SaaS headings unless they are grounded in operational detail:
  - `No destination too remote`
  - `A complete specialist layer over a five-star safari`
- Replace with practical operator copy:
  - `Field-ready specialist hospitality`
  - `The practical work behind a specialist safari`
  - specific lines about kashering, staff briefing, kit delivery, kitchen separation, tiffins, Shabbos timing, and supervision.
- The user requested:
  - elements flat against the background
  - animation and motion
  - fewer borders
  - more pictures
  - no rounded corners unless explicitly asked

## Design repair pattern

1. Flatten panels into the scene: remove boxed/glass hero cards and let text sit over image/background fields.
2. Replace heavy bordered cards with editorial text blocks, whitespace, small dividers, or section rhythm.
3. Use images as the page structure:
   - full-width image slabs
   - image-led editorial bands
   - atmospheric background fields
   - not just thumbnails inside cards
4. Add restrained motion:
   - scroll reveal via `IntersectionObserver`
   - image hover drift/zoom
   - mild hero parallax
   - `prefers-reduced-motion` fallback
5. Before deploy, run a `border-radius` audit and keep only `0`/`0px` unless the user requested rounded corners.
6. Verify live HTML for the corrected phrases/classes after deploying.

## CSS audit examples

- Search for `border-radius:` and reject nonzero values.
- Search for generic copy like `360°`, `rapid growth`, `seamless`, `complete solution`, and arbitrary `01 /` feature labels.
- Check for repeated `border:` usage if the page feels like a grid of cards rather than a designed surface.
