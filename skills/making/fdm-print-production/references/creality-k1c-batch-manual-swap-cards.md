# Creality K1C batch manual-swap cards

Session-specific production notes for batching thin two-color business-card style FDM prints on a Creality K1C via Creality Print CLI + Moonraker/Klipper.

## When to use

Use this when the user wants multiple copies of a thin card/token on the bed and the design has a base layer printed in one filament color followed by raised details after a manual color swap.

## Practical packing lesson

For an `85.6 × 54.0 × 1.82 mm` business-card geometry on a K1C:

- A theoretical tight `2 × 4` layout with ~`1 mm` gaps is `172.2 × 219.0 mm`; it is close to the bed edge and not a safe assumption.
- Duplicating the STL into one large combined ASCII STL can be rejected by Creality Print as a failed model load; do not treat that as proof the single card is bad.
- Creality Print CLI with eight separate STL inputs may split the job across multiple plates. In the tested case it produced:
  - Plate 1: 6 cards, footprint about `166.0 × 173.2 mm`, estimated around `93 min`.
  - Plate 2: 2 cards, footprint about `110.0 × 85.6 mm`.
- The safest maximum single-bed batch from that run was therefore 6 cards, not the theoretical 8.

## CLI pitfalls

- `--repetitions 8 --slice 0` failed with: `Invalid params: can not set repetitions when slice all.`
- Trying `--slice 1` did not help on that setup because the CLI reset it to `0` for the current project shape.
- A reliable fallback was to pass the same STL path multiple times and let Creality arrange/split plates, then choose the densest valid `plate_N.gcode` for the real print.

Example shape:

```bash
CrealityPrint \
  --load-settings "$MACHINE;$PROCESS" \
  --load-filaments "$FILAMENT" \
  --allow-rotations \
  --arrange 1 \
  --ensure-on-bed \
  --slice 0 \
  --outputdir "$OUT" \
  "$STL" "$STL" "$STL" "$STL" "$STL" "$STL" "$STL" "$STL"
```

Then inspect all `plate_*.gcode` files, not just the newest one.

## Pause insertion for batch cards

After choosing the target plate G-code:

1. Parse `;LAYER_CHANGE` blocks and the following `;:<z>` marker.
2. For a `base_t = 1.20 mm` and `0.20 mm` layers, insert exactly one pause before the first layer above base height, typically `Z=1.40`.
3. Patch the pause message to match the actual colorway:
   - black base → swap to white for raised details;
   - white base/inverted run → swap to black.
4. Verify `pause_count == 1` and the next layer marker after the pause is the intended detail layer.

## Human coordination

- If the user says the current filament is the opposite of the intended base, offer an inverted run rather than forcing an unnecessary unload/reload, provided they accept the colorway.
- For long batches, the useful user-facing message is the pause/reminder, not the full telemetry stream. Monitor in the background and notify only when intervention is needed or on completion/error.
