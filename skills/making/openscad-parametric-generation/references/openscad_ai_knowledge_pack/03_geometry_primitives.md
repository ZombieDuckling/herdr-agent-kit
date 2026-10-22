# 03 — Geometry Primitives

OpenSCAD geometry starts from primitive 2D and 3D objects. Complex parts are built by transforming and combining these primitives.

## 3D primitives

### `cube()`

Use `cube()` for rectangular prisms.

```scad
cube(size = [x, y, z], center = false);
cube(size = 10, center = true);
```

When `center = false`, the cube extends from the origin in the positive X/Y/Z directions. When `center = true`, it is centered on the origin.

Recommended AI usage:

```scad
module box_at_origin(w, d, h) {
    cube([w, d, h], center = true);
}

module printable_box(w, d, h) {
    translate([0, 0, h/2])
        cube([w, d, h], center = true);
}
```

Use the printable version when the bottom should sit on Z = 0.

### `sphere()`

Use for balls, domes, rounded blobs, and smooth features.

```scad
sphere(r = 10);
sphere(d = 20);
```

Resolution is controlled by `$fn`, `$fa`, and `$fs`.

```scad
$fn = 64;
sphere(d = 20);
```

For a dome, intersect a sphere with a cube or place only half above the base plane:

```scad
module dome(d, h) {
    intersection() {
        scale([1, 1, h/(d/2)]) sphere(d = d);
        translate([-d, -d, 0]) cube([2*d, 2*d, h]);
    }
}
```

### `cylinder()`

Use for cylinders, holes, cones, tapered pegs, rounded posts.

```scad
cylinder(h = 20, r = 5, center = false);
cylinder(h = 20, d = 10, center = true);
cylinder(h = 20, r1 = 8, r2 = 4);
```

For circular holes, subtract a cylinder from the target. Extend the cutter by `eps` so it cuts cleanly through.

```scad
eps = 0.01;

difference() {
    cube([40, 30, 6], center = true);
    translate([0, 0, -6/2 - eps])
        cylinder(h = 6 + 2*eps, d = 5);
}
```

For horizontal holes, rotate the cylinder:

```scad
rotate([90, 0, 0])
    cylinder(h = 40, d = 6, center = true);
```

### `polyhedron()`

Use only when primitive/CSG/extrude strategies are not enough. A polyhedron needs points and faces. It is powerful but easy to break.

```scad
polyhedron(
    points = [
        [0,0,0], [10,0,0], [10,10,0], [0,10,0],
        [0,0,10], [10,0,10], [10,10,10], [0,10,10]
    ],
    faces = [
        [0,1,2,3], [4,7,6,5], [0,4,5,1],
        [1,5,6,2], [2,6,7,3], [3,7,4,0]
    ]
);
```

AI caution: prefer `linear_extrude(polygon(...))` for prismatic custom profiles. Use `polyhedron()` for genuinely non-prismatic solids.

## 2D primitives

2D primitives live on the XY plane. They are commonly extruded into 3D.

### `square()`

```scad
square(size = [x, y], center = true);
square(size = 10, center = false);
```

### `circle()`

```scad
circle(r = 10);
circle(d = 20);
circle(r = 10, $fn = 6); // hexagon-like 2D shape
```

Use `scale()` or `resize()` to make ellipses:

```scad
scale([2, 1]) circle(r = 10);
```

### `polygon()`

Use for custom 2D outlines.

```scad
polygon(points = [[0,0], [30,0], [25,15], [0,10]]);
```

For holes in polygons, use the `paths` parameter or use `difference()` with 2D shapes before extrusion.

```scad
linear_extrude(height = 5)
difference() {
    polygon([[0,0], [40,0], [40,20], [0,20]]);
    translate([20,10]) circle(d = 8);
}
```

### `text()`

Creates 2D text. Usually needs `linear_extrude()` for raised or engraved text.

```scad
linear_extrude(height = 1.2)
    text("OPENSCAD", size = 10, halign = "center", valign = "center");
```

Fonts depend on the user system. For robust AI output, expose the font as a parameter and keep a fallback note.

```scad
label_font = "Liberation Sans:style=Bold";
```

## Primitive selection guide

- Rectangular functional part: `cube()`.
- Round post/hole: `cylinder()`.
- Ball/dome/blobby relief: `sphere()` plus scale/intersection/hull.
- Flat profile to extrude: `square()`, `circle()`, `polygon()`, `text()`.
- Custom mechanical cross-section: `polygon()` + `linear_extrude()`.
- Lathe-like part: 2D profile + `rotate_extrude()`.
- Fully custom non-prismatic mesh: `polyhedron()` only when needed.
