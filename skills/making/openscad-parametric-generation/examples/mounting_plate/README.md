# Mounting Plate Example

This example is a rounded rectangular mounting plate with four through holes and an optional raised label.

## Parameters

- `plate_w`, `plate_d`, `plate_t`: overall width, depth, and thickness in millimetres.
- `corner_r`: 2D corner radius before extrusion.
- `hole_d`: through-hole diameter.
- `hole_inset`: distance from each edge to the hole center.
- `add_label`, `label_text`, `label_size`, `label_height`: raised label controls.

## Print Assumptions

- Units are millimetres.
- The bottom face sits on `Z = 0`.
- The plate is intended to print flat on the bed.
- Hole cutters extend through the full part with `eps` overlap to avoid coincident faces.

## Export

From the skill root:

```bash
scripts/validate_scad.sh examples/mounting_plate/model.scad
scripts/render_stl.sh examples/mounting_plate/model.scad exports/mounting_plate.stl
scripts/render_png.sh examples/mounting_plate/model.scad exports/mounting_plate.png
```

If OpenSCAD is not on `PATH`, set:

```bash
export OPENSCAD_BIN=/path/to/OpenSCAD
```

## Validation Status

Not run until OpenSCAD is discoverable in the local shell.
