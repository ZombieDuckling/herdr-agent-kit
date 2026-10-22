# One-color painted QR business cards

Use this reference when designing 3D-printable business cards, leave-behind tokens, badges, signs, or plates where the user will print in one filament color and add paint marker/highlight afterward.

## Core lesson

Do not model a QR code as same-color raised modules and assume it will scan. A real QR needs optical contrast after finishing, not just geometric detail.

For a black PLA + gold paint marker workflow, prefer:

- black base card;
- raised paintable text, traces, border, and QR field;
- recessed QR dark cells cut into the raised field so they remain black;
- gold marker swept lightly over raised top surfaces only.

This creates black-on-gold contrast while keeping the print single-color.

For bronze/copper/gold PLA-only workflows:

- treat QR geometry as decorative unless a contrast step is added;
- single-color metallic PLA usually lacks enough contrast for reliable scanning;
- offer a non-QR variant or tell the user that scan reliability depends on post-processing.

## Verification pattern

1. Generate the QR matrix from the exact URL/payload.
2. Avoid OpenSCAD 2021 string-index tricks such as `substr()` for matrix lookup; generate explicit square/cutter geometry or a 2D import.
3. Export STL and check mesh bounding box.
4. Generate a flat image simulation of the intended final contrast, e.g. black modules on gold background.
5. Decode that simulation with a real QR decoder (`cv2.QRCodeDetector`, `zbarimg`, etc.).
6. Be explicit: source QR decode passing proves the matrix/payload, but physical scan reliability still depends on contrast, paint cleanliness, surface finish, camera, and module size.

## FDM design defaults

- Standard card footprint: 85.6 × 54 mm unless the user gives another size.
- Base thickness: about 0.8–1.0 mm.
- Raised detail/paint field: about 0.3–0.5 mm.
- Minimum QR module on 0.4 mm nozzle: aim for roughly 0.9–1.2 mm modules; smaller modules become paint/fuzz sensitive.
- Keep QR quiet zone intact as a raised paintable field around the code.
- Prefer raised text for paint-marker finishing; recessed text can flood with paint.

## User-facing guidance

When handing off the STL, tell the user how to finish it:

- print flat, face-up, no supports;
- use a chisel-tip paint marker lightly across top surfaces;
- avoid flooding paint into recessed QR cells;
- test-scan one finished card before batch printing.
