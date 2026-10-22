# Batch layout for manual filament-swap cards

Use this note when a CAD-to-print job moves from a successful single two-color card/token to a bed batch of multiple copies.

## Durable lesson

For business-card style parts, theoretical bed packing can be misleading. The right workflow is:

1. Keep the single-card CAD/STL as the source of truth.
2. Ask the slicer to arrange multiple copies using the real printer profile.
3. Inspect every generated `plate_*.gcode`; the slicer may split an attempted batch across plates.
4. Select the densest valid single plate, then insert the manual color-swap pause into that selected G-code only.

## K1C example from a real run

Single card size: `85.6 × 54.0 × 1.82 mm`.

A theoretical 8-up layout (`2 × 4`, about `172.2 × 219.0 mm`) was too optimistic for a safe single-bed print. Creality Print CLI split eight copies into two plates:

- `plate_1.gcode`: 6 cards, about `166.0 × 173.2 mm`, valid single-bed batch.
- `plate_2.gcode`: 2 cards, about `110.0 × 85.6 mm`.

Use the 6-up plate as the max-safe single-bed batch rather than forcing a custom combined STL.

## Creality CLI pitfalls

- Combined duplicated ASCII STL may fail model loading even when the original single-card STL is valid.
- `--repetitions` with `--slice 0` can fail with `Invalid params: can not set repetitions when slice all.`
- Passing the same STL path repeatedly and letting Creality arrange/split plates was more reliable.

## Pause behavior

For a `1.20 mm` base and `0.20 mm` layers:

- Insert exactly one pause before the first detail layer above the base, normally `Z=1.40`.
- Patch the pause prompt to match the actual colors loaded for that run.
- When the user likes both colorways, black-base/white-detail and white-base/black-detail can both be valid outputs; do not force a reload if the user accepts an inverted run.
