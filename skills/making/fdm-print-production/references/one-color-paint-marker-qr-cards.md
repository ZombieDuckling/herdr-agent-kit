# One-color FDM business cards with paint-marker QR contrast

Use this reference when designing 3D-printable business cards, leave-behind cards, plaques, or tokens that will be printed in one filament color and highlighted manually with a paint marker.

## Pattern

For black PLA plus a gold paint marker, do **not** model a QR code as same-color raised modules on a same-color base. It will look decorative but usually will not scan.

Use this geometry instead:

1. Generate a real QR matrix from the final URL/payload.
2. Model a raised square field that can be swept with the gold paint marker.
3. Cut/recess the dark QR modules into that field so they remain black after marking.
4. Keep the quiet zone as part of the raised paintable field.
5. Make modules large enough for FDM and marker bleed:
   - 0.4 mm nozzle: prefer module size about `0.9–1.2 mm`.
   - module cutout width: about `80–88%` of pitch.
   - field height: about `0.35–0.50 mm` above base.
6. Verify the *generated QR payload* with a flat source PNG decoder before trusting the CAD.
7. If possible, generate a black-on-gold scan simulation and decode that too.

## Practical finish notes

- Best functional finish: black PLA card, gold marker on raised text/traces/QR field.
- Use a chisel-tip marker lightly across top faces; avoid flooding paint into recessed QR cells.
- Bronze PLA or metallic silk PLA can look premium, but treat QR as decorative unless contrast is added.
- Shaded CAD preview renders are not valid QR scan tests; decode a flat source image or a real photographed print.

## CAD implementation notes

- Source-first: store the QR payload and matrix-generation recipe in the project notes/source.
- Do not hand-draw QR-like decorations if scanability matters.
- In OpenSCAD 2021, avoid generated QR snippets that rely on unsupported string-indexing patterns such as `substr(row, i, i)`. Prefer explicit square geometry emitted from the QR matrix, or numeric module coordinate lists.
- Keep cards thin but not flimsy: a `0.8–1.0 mm` base with `0.3–0.5 mm` raised details worked as a practical starting point.
