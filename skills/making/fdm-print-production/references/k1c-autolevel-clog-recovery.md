# K1C auto-level, manual-swap resume, and clog-recovery gate

Use with `fdm-print-production` when running the user's Creality K1C via Moonraker/Klipper for multi-card manual filament-swap batches.

## Auto-level before a card batch

When the user asks for auto-level before print, insert explicit bed mesh commands before the slicer's normal `START_PRINT` block:

```gcode
; HERMES_AUTO_LEVEL_START - requested by the user
G28
BED_MESH_CALIBRATE
; HERMES_AUTO_LEVEL_END
START_PRINT EXTRUDER_TEMP=220 BED_TEMP=50
```

Monitoring caveat: after this insertion the printer may report `state=printing` while heaters are still `0` for several minutes during probing. Do not claim extrusion has started until `print_duration`, `filament_used`, or progress advances. Confirm the bed mesh profile becomes active, e.g. `bed_mesh.profile_name == "default"`.

## Manual colour-swap pause and resume

For a 1.20 mm base and 0.20 mm layer height, insert the colour-change pause immediately before the first `;LAYER_CHANGE` above the base, typically `;:1.4`.

At the pause, ask the user to swap to the exact detail colour and purge clean. Before resuming, heat back to print temperature and verify `extruder.can_extrude`.

Reliable resume path on this K1C was not `/printer/print/resume`; use direct gcode through Moonraker:

```json
POST /printer/gcode/script {"script":"M104 S220\nM117 Heating <DETAIL> filament"}
POST /printer/gcode/script {"script":"RESUME"}
```

After resume, verify `state=printing`, `pause_resume.is_paused=false`, progress/filament used increases, and Z is on the raised-detail layer.

## Six-up card batch packing

For the tested `85.6 × 54.0 × 1.82 mm` business-card geometry, Creality Print split eight copies across two plates. The safe maximum single-bed batch was six cards at about `166.0 × 173.2 mm`. Treat six as the practical K1C batch size for this geometry unless a new slice proves otherwise.

## Clog recovery gate

If a nozzle clog occurs during or after manual colour changes, do not immediately start another six-card batch. After the user clears the clog, monitor a simple validation print such as `3DBenchy_PLA_19m.gcode` to successful completion first. Only then retry the card batch.
