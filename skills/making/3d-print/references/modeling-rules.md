# Modeling rules (CadQuery / model.py)

## Contract

`model.py` is executed via CQGI — the same way by the CadQuery MCP server and
by `print3d`. It must:

- use **millimeters** everywhere;
- define tweakable dimensions as named variables at the top, with a short
  comment each (this is what makes the model "parametric");
- put the final shape into a variable named `result` (or call
  `show_object(shape)`);
- build one or more **valid solids** — no naked wires/faces, no exceptions;
- fit the printer: 180 × 180 × 180 mm (A1 Mini). Leave a few mm of margin.

Template:

```python
import cadquery as cq

# --- parameters (mm) ---
width = 60.0     # outer width
depth = 40.0     # outer depth
height = 25.0    # outer height
wall = 2.0       # wall thickness

# --- model ---
result = (
    cq.Workplane("XY")
    .box(width, depth, height)
    .faces(">Z")
    .shell(-wall)          # open-top box
    .edges("|Z")
    .fillet(3.0)
)
```

## Design for FDM printing (PLA, 0.4 mm nozzle, 0.20 mm layers)

- **Orientation**: design with a flat face on Z=0 — the model prints as
  oriented, big flat side down. Avoid needing supports where possible.
- **Overhangs**: keep unsupported overhangs ≤ 45° from vertical; small
  bridges (< 20 mm) are fine.
- **Walls**: minimum 1.6 mm (4 extrusion lines); 2.0–2.4 mm for anything
  load-bearing. Never design 0.5 mm "veils".
- **Small features**: minimum reliable feature/pin ≈ 2 mm; embossed text
  depth ≥ 0.6 mm, stroke ≥ 1.2 mm, font size ≥ 8 mm.
- **Holes** print undersized: add ~0.2 mm to functional hole diameters
  (an "8 mm" screw hole → model 8.2–8.3 mm).
- **Clearances** between mating printed parts: 0.2 mm snug, 0.3 mm sliding,
  0.4 mm loose.
- **Bottom edges**: a small 0.3–0.5 mm chamfer on the base perimeter fights
  elephant-foot and eases removal.
- **Fillets**: nice on vertical edges and stress corners, but CadQuery
  `fillet()` fails easily on complex/short edges — if the build breaks right
  after adding a fillet, halve the radius or fillet fewer edges.

## Working style

- Change the existing `model.py` incrementally; do not regenerate from
  scratch on each user request — the user's earlier tweaks must survive.
- After any edit run `print3d inspect` before showing anything.
- Prefer simple constructive geometry (boxes, cylinders, shells, cuts,
  lofts, revolves). No mesh/organic sculpting in this pipeline.
- Don't claim strength, water-tightness or food safety — printed PLA has
  layer seams and is not certified for food contact.
