# 07 — Functions, Modules, and Children

OpenSCAD separates functions and modules.

- Functions return values.
- Modules create geometry or perform actions.

## Functions

Functions are pure value calculators.

```scad
function clamp(x, lo, hi) = min(max(x, lo), hi);
function radius_from_diameter(d) = d / 2;
function hole_positions(w, d, inset) = [
    [-w/2 + inset, -d/2 + inset],
    [ w/2 - inset, -d/2 + inset],
    [ w/2 - inset,  d/2 - inset],
    [-w/2 + inset,  d/2 - inset]
];
```

Functions do not create geometry directly. They are used inside expressions, assignments, loops, and module arguments.

```scad
for (p = hole_positions(80, 40, 8))
    translate([p[0], p[1], 0]) cylinder(h = 5, d = 4);
```

## Modules

Modules create geometry, wrap transforms, or provide reusable modelling components.

```scad
module standoff(h = 10, outer_d = 8, hole_d = 3) {
    difference() {
        cylinder(h = h, d = outer_d);
        translate([0, 0, -0.01]) cylinder(h = h + 0.02, d = hole_d);
    }
}
```

## Module defaults

Use defaults for parameters that should be customizable but safe.

```scad
module rounded_plate(w = 80, d = 40, t = 4, r = 4) {
    linear_extrude(height = t)
        offset(r = r) offset(delta = -r)
            square([w, d], center = true);
}
```

## Named arguments

Prefer named arguments for readability.

```scad
rounded_plate(w = 100, d = 50, t = 6, r = 6);
```

## `children()`

`children()` lets a module operate on child geometry passed into it.

```scad
module place_four_corners(w, d, inset) {
    for (x = [-w/2 + inset, w/2 - inset])
    for (y = [-d/2 + inset, d/2 - inset])
        translate([x, y, 0]) children();
}

place_four_corners(80, 40, 8)
    cylinder(h = 5, d = 4);
```

This is useful for reusable patterns like mirroring, placing repeated holes, applying debug colors, or transforming subparts.

## Child indexing

`children(0)`, `children(1)`, etc. can select specific children.

```scad
module show_pair() {
    color("red") children(0);
    color("blue") translate([20, 0, 0]) children(1);
}

show_pair() {
    cube(5);
    sphere(4);
}
```

## Module composition pattern for AI

Use modules with one responsibility each:

```scad
module outer_shell() { ... }
module inner_cavity_cutter() { ... }
module screw_hole_cutters() { ... }
module label_emboss() { ... }

module model() {
    union() {
        difference() {
            outer_shell();
            inner_cavity_cutter();
            screw_hole_cutters();
        }
        label_emboss();
    }
}

model();
```

## Validation with `assert()`

Use `assert()` for parameter constraints.

```scad
module box(w, d, h, wall) {
    assert(w > 2*wall, "width must exceed twice wall thickness");
    assert(d > 2*wall, "depth must exceed twice wall thickness");
    cube([w, d, h], center = true);
}
```

## Agent design rules

- Functions calculate dimensions, positions, lists, or booleans.
- Modules create or transform geometry.
- Avoid giant monolithic modules.
- Give modules nouns or verb-noun names: `base_plate`, `hole_cutter`, `rounded_rect_2d`, `mounting_boss`.
- Use `children()` for reusable placement/transformation wrappers.
- Keep final composition obvious.
