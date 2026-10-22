# 13 — Debugging and Validation

OpenSCAD errors often come from syntax, invalid geometry, wrong scope assumptions, or boolean ambiguity. AI-generated code needs a validation workflow.

## Basic debug flow

1. Run preview.
2. Check console warnings.
3. Isolate suspicious modules with `!`.
4. Highlight cutters with `#`.
5. Make hidden cutters visible with `%`.
6. Render with F6 or CLI export.
7. Inspect exported STL/3MF in slicer or mesh viewer.

## Modifier characters

```scad
# object(); // highlight object
% object(); // transparent/background object
! object(); // show only this object/subtree
* object(); // disable object/subtree
```

Example:

```scad
difference() {
    base();
    #hole_cutters();
}
```

## `echo()`

Use `echo()` to inspect values.

```scad
echo("inner width", inner_w);
echo("hole positions", hole_positions);
```

## `assert()`

Use `assert()` to stop impossible parameter combinations.

```scad
assert(wall > 0, "wall must be positive");
assert(width > 2*wall, "width too small for wall thickness");
```

Use asserts liberally in AI-generated parametric models.

## Common syntax errors

### Semicolon after transform

Wrong:

```scad
translate([10,0,0]); cube(5);
```

Correct:

```scad
translate([10,0,0]) cube(5);
```

### Missing braces for multiple children

Wrong:

```scad
translate([0,0,10])
    cube(5);
    sphere(5); // not translated
```

Correct:

```scad
translate([0,0,10]) {
    cube(5);
    sphere(5);
}
```

### Wrong `difference()` grouping

Wrong:

```scad
difference() {
    cube(10);
    sphere(5);
    cylinder(h=20, d=2);
}
```

This subtracts both `sphere` and `cylinder` from `cube`.

If the positive object is cube + sphere, use:

```scad
difference() {
    union() {
        cube(10);
        sphere(5);
    }
    cylinder(h=20, d=2);
}
```

## Common geometry errors

### Non-manifold export

Causes:

- coincident faces;
- cutters exactly flush with targets;
- self-intersections;
- invalid polyhedron faces;
- imported mesh defects;
- zero-thickness geometry.

Fixes:

- add `eps` overlap;
- make cutters longer;
- use explicit `union()`;
- simplify geometry;
- render again;
- avoid questionable imported STL modifications.

### Preview differs from render

Preview uses an approximation. Trust render for final export. Some preview artifacts disappear after render; some render failures expose true geometry problems.

### Slow render

Causes:

- excessive `$fn`;
- `minkowski()` on detailed 3D shapes;
- many nested booleans;
- high-resolution imported meshes;
- large repeated features.

Fixes:

- lower `$fn` while iterating;
- use 2D hull/offset then extrude;
- simplify boolean tree;
- add `render()` selectively to cache complex subassemblies;
- reduce imported mesh detail.

## Agent validation checklist

A generation agent should inspect its own code for:

- top-level parameters are clear;
- units and origin policy are documented;
- no obvious syntax errors;
- no transform semicolon mistakes;
- all cutters have overlap margins;
- all optional features are controlled by booleans;
- all important constraints have `assert()`;
- no dependency is undocumented;
- final model call exists exactly once.
