# Manual filament-swap FDM card batches

Use this reference when producing small flat FDM business cards, tags, labels, badges, or QR plaques that need readable two-color detail without AMS/CFS.

## Lessons from business-card run

- One-color relief/recessed text is usually not readable enough for cards; use real color contrast.
- Prefer a flat base color plus raised detail layer in the second color.
- For QR codes, use true contrast and verify the QR payload source separately. A practical design is a raised field with opposite-color QR modules/cutouts.
- Small URL text around 2.2 mm printed poorly on a 0.4 mm nozzle. Enlarge critical URL text to roughly 3 mm+ and remove decorative motifs if they compete for space.
- Preview renders can miss FDM readability issues; inspect actual print photos and iterate text size/spacing.
- Batch packing should be slicer-verified, not just geometrically assumed. On a K1C, 85.6 x 54 mm cards sliced safely as 6-up; an 8-up geometric layout was too aggressive / split by the slicer.
- Insert a single color-change pause at the first layer above the base height. Example: base through Z=1.20 mm, pause before Z=1.40 mm for 0.20 mm layers.
- On Klipper/Moonraker printers, `PAUSE` can drop nozzle target; before resuming, reheat (e.g. `M104 S220`), confirm `can_extrude`, then send direct `RESUME` via gcode if the HTTP resume endpoint does not unpause.
- For repeat batches, encode/confirm the current base color. If the printer still has white loaded, run an inverted white-base/black-detail job rather than requiring a filament swap before start.
- If the user asks for auto-leveling, insert/verify explicit `G28` + `BED_MESH_CALIBRATE` before the normal print start/heatup block, then verify `bed_mesh.profile_name` becomes active before extrusion.

## Production workflow

1. Keep CAD source parametric and verified: dimensions, preview renders, STL bbox, QR source decode.
2. Slice a single card first and run a real test print.
3. After the physical print, fix legibility before batching.
4. For batches, use the slicer to arrange/verify copies; trust slicer plate output over theoretical bed packing.
5. Patch G-code with exactly one manual color-change block before the raised detail layer.
6. Upload/start only after checking printer state is idle.
7. Monitor until pause; tell the user exactly which filament to swap to.
8. After swap, reheat if needed, direct `RESUME`, verify movement/extrusion, then monitor to completion.

## Safety / quality gates

- Do not remove the part from the bed during swap.
- Tell the user to purge until the new color is clean.
- Avoid overpromising QR scanability from a render alone; verify real prints when possible.
- For small raised text, prioritize fewer/larger words over decorative detail.
