# Rack-mount STL fallback notes

Use when designing functional rack trays/panels and the normal CAD renderer hangs or cannot export.

## Durable dimensions used successfully

- 1U height: `44.45 mm`.
- Common 10-inch rack front width: `254 mm`.
- Common 10-inch rack horizontal mounting centre spacing: about `222.25 mm`.
- Raspberry Pi 5 board envelope: `85 x 56 mm`.
- Raspberry Pi / Model B mounting holes: M2.5-ish clearance, use `2.75 mm` nominal holes or `~3.1 mm` clearance for printed parts.
- Common Pi mounting pattern used for fit-first modelling: `58 mm x 49 mm` with `3.5 mm` edge offset.

## Working fallback pattern

If OpenSCAD hangs even on a known-simple model or `openscad --version`, do not keep simplifying blindly. Keep the parametric `.scad` source for future editing, then generate the STL from an equivalent Python mesh source:

1. Use `trimesh` + `manifold3d` booleans for boxes, cylinders, rack slots, tray vents, screw holes, and clips.
2. Export STL from the generated mesh.
3. Verify with mesh bounds, watertightness, triangle count, and file size.
4. Render a preview from the actual STL mesh. If `trimesh.Scene.save_image()` fails because `pyglet` is missing, use `matplotlib` `Poly3DCollection` as a deterministic preview fallback.

## Design pattern

For a clip-in Pi tray behind a 1U panel:

- Make the front panel full `254 x 44.45 mm`.
- Put a flat rear tray behind the panel, centred around the Pi board.
- Add four short clip lips at the board ends, low side guide rails, and M2.5 mounting-hole fallback.
- Add cable relief windows in tray walls and ventilation in the floor/front panel.
- Report caveats for active coolers/heatsinks and rack-hole standard variance.
