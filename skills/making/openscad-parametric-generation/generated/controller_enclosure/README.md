# CTRL-01 Controller Enclosure

This generated OpenSCAD model contains a two-part electronics enclosure: an open-top controller box and a separate snap-on vented lid laid out beside it for printing.

## Key Parameters

- `outer_w`, `outer_d`, `outer_h`: enclosure size, defaulting to 90 mm x 55 mm x 28 mm.
- `wall`, `bottom_t`: shell wall and bottom thickness, both defaulting to 2.4 mm.
- `lid_t`, `lid_lip_h`, `lid_lip_wall`, `clearance`: snap-on lid plate and inset lip fit controls.
- `standoff_h`, `standoff_outer_d`, `screw_d`, `standoff_inset`: four internal M3-style mounting standoffs.
- `cable_w`, `cable_h`, `cable_z`: rounded cable openings on the two short sides.
- `vent_count`, `vent_l`, `vent_w`, `vent_pitch`: lid ventilation slots.
- `label_text`, `label_size`, `engrave_depth`: engraved lid label.
- `snap_w`, `snap_h`, `snap_bump_depth`, `snap_x_offset`, `snap_drop`: simple snap bump and relief pocket geometry.

## Assumptions

- Units are millimetres.
- The box and lid are arranged as separate printable parts in one build layout.
- The lid is modeled lip-side down so both parts sit on `Z = 0`.
- The screw holes are generic M3 clearance holes with no countersinks.
- The snap bumps are intentionally conservative and may need tuning for a specific printer/material.
- The label is engraved into the lid rather than raised.

## Print Notes

- Print the layout flat on the bed.
- Start with `clearance = 0.25`; increase it for rougher printers or materials.
- If snap fit is too tight, reduce `snap_bump_depth` or increase `clearance`.
- If the standoffs feel weak, increase `standoff_outer_d` or reduce `screw_d`.

## Export

From the skill root:

```bash
scripts/validate_scad.sh generated/controller_enclosure/model.scad
scripts/render_stl.sh generated/controller_enclosure/model.scad generated/controller_enclosure/exports/controller_enclosure.stl
scripts/render_png.sh generated/controller_enclosure/model.scad generated/controller_enclosure/exports/controller_enclosure.png
```

## Validation Status

Passed with OpenSCAD CLI at `/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD`.

- Status: `NoError`
- Top-level object: manifold 3D object
- Vertices: 3496
- Facets: 7036
- Exported STL: `generated/controller_enclosure/exports/controller_enclosure.stl`
- Exported PNG: `generated/controller_enclosure/exports/controller_enclosure.png`
