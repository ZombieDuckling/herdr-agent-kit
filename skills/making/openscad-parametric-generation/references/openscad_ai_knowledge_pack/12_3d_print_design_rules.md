# 12 — 3D-Print-Oriented Design Rules

This file converts OpenSCAD knowledge into practical FDM/SLA model-generation rules. These are not OpenSCAD syntax rules; they are production rules for useful printable geometry.

## Default orientation

Unless specified otherwise, generate parts with the bottom face on Z = 0.

```scad
translate([0, 0, h/2])
    cube([w, d, h], center = true);
```

This makes slicer placement predictable.

## Wall thickness

For FDM, avoid very thin walls. As a safe generic default:

- small decorative walls: at least 1.2 mm;
- functional walls: 2.0–3.0 mm;
- load-bearing walls: context-specific, often thicker.

Expose `wall` as a parameter.

```scad
wall = 2.4;
assert(wall >= 1.2, "wall too thin for typical FDM");
```

## Clearances

For fit between printed parts, expose `clearance`.

Generic starting points:

- snug static fit: 0.15–0.25 mm per side;
- easy sliding fit: 0.3–0.5 mm per side;
- rough printers/materials: more.

```scad
clearance = 0.25;
hole_d = peg_d + 2*clearance;
```

## Holes

Printed holes often come out undersized. Expose hole diameter and optionally add a compensation parameter.

```scad
hole_compensation = 0.2;
actual_hole_d = nominal_hole_d + hole_compensation;
```

## Boolean cutters

Always make cutters taller/longer than the part they cut.

```scad
eps = 0.01;
translate([0,0,-eps]) cylinder(h = part_h + 2*eps, d = hole_d);
```

## Fillets and roundovers

OpenSCAD does not have native feature-history fillets like mainstream CAD. Common approximations:

- `offset()` on 2D profiles, then extrude;
- `minkowski()` with sphere/circle, but this can be slow;
- `hull()` between circles/spheres/cylinders;
- chamfers using tapered cylinders, bevelled polygons, or hulls.

Prefer 2D rounding for plates.

## Overhangs

Avoid unsupported overhangs where possible. For FDM, 45-degree chamfers are easier than horizontal ledges.

Chamfer-like profile:

```scad
module chamfered_cylinder(h, d, chamfer) {
    cylinder(h = h, d = d);
    // More advanced: build as rotate_extrude profile.
}
```

For AI generation, ask internally: can this print flat? does it need supports? is there a better orientation?

## Avoid zero-thickness geometry

Do not create infinitely thin walls, faces, or decorative surfaces that are not part of a volume. Exported models must be solid.

## Text on prints

Raised text usually prints more reliably than engraved text for small features. Keep text thick enough.

Good defaults:

```scad
text_height = 1.0;
text_size = 8;
```

For engraving, subtract shallow text and make the cutter slightly deeper than the intended cut.

## Screws and hardware

If the user requests screw holes, expose:

```scad
screw_d = 3.2;
head_d = 6.2;
head_depth = 2.0;
```

Do not hard-code a single screw standard unless specified.

## Manifold export checklist

Before final output:

- no mixed 2D/3D boolean operations;
- cutters extend through targets;
- joined solids overlap slightly or are explicitly unioned;
- polyhedra have consistent faces;
- imported meshes are assumed risky;
- no surfaces masquerading as solids;
- render succeeds before export.

## Design-for-agent rule

The model should degrade gracefully when parameters change. If the agent exposes `width`, `height`, `wall`, and `hole_spacing`, changing those values should not move holes outside the body or create negative inner dimensions. Use `assert()` to catch invalid combinations.
