# 04 — Transformations

Transformations modify their child geometry. They are written before the object or block they affect.

```scad
translate([10, 0, 0]) cube(5);
```

To transform multiple children, use braces:

```scad
translate([0, 0, 10]) {
    cube(5);
    sphere(3);
}
```

## Order matters

Transformations are nested. The operation closest to the object is applied first.

```scad
rotate([0, 0, 45])
    translate([20, 0, 0])
        cube(5);
```

This is not the same as:

```scad
translate([20, 0, 0])
    rotate([0, 0, 45])
        cube(5);
```

Agent rule: when in doubt, create a named module for the untransformed local feature, then place instances with clear transforms.

```scad
module hole_cutter() {
    cylinder(h = 20, d = 4, center = true);
}

for (x = [-20, 20])
    translate([x, 0, 5]) hole_cutter();
```

## `translate()`

Moves geometry by `[x, y, z]`.

```scad
translate([10, -5, 3]) cube(4);
```

Use translation for positioning, not for changing dimensions.

## `rotate()`

Rotates geometry in degrees. Common signatures:

```scad
rotate([x_angle, y_angle, z_angle]) object();
rotate(a = 45, v = [0, 0, 1]) object();
```

Examples:

```scad
rotate([0, 0, 90]) cube([20, 5, 5], center = true);
rotate([90, 0, 0]) cylinder(h = 40, d = 6, center = true);
```

## `scale()`

Scales geometry by a scalar or vector.

```scad
scale([2, 1, 0.5]) sphere(r = 10);
```

Use with care in mechanical parts because it also scales holes, clearances, and wall thicknesses. Prefer parameterized dimensions where possible.

## `resize()`

Resizes geometry to target dimensions.

```scad
resize([40, 20, 10]) sphere(r = 10);
```

Use for decorative or organic-like approximations, not precision engineering where direct dimensions are clearer.

## `mirror()`

Mirrors across a plane normal to a vector.

```scad
mirror([1, 0, 0]) object(); // mirror across YZ plane
```

Useful for symmetric brackets, left/right parts, paired features.

## `color()`

Sets viewport color only. It does not generally carry through to STL as material data. Do not rely on it for manufacturing instructions.

```scad
color("red") cube(10);
color([0.2, 0.8, 0.4, 0.5]) sphere(6);
```

Use color for debugging subparts.

## `offset()`

A 2D operation. Expands or contracts 2D shapes. Useful for rounded rectangles and clearances.

Rounded rectangle pattern:

```scad
module rounded_rect_2d(w, d, r) {
    offset(r = r)
        offset(delta = -r)
            square([w, d], center = true);
}
```

Outer/inner profile pattern:

```scad
outer = 40;
wall = 3;
linear_extrude(5)
difference() {
    offset(r = 4) square([outer, outer], center = true);
    offset(r = 2) square([outer - 2*wall, outer - 2*wall], center = true);
}
```

## `hull()`

Creates the convex hull around child shapes. Excellent for smooth bridges between circles/cylinders/spheres.

2D slot pattern:

```scad
module slot_2d(length, d) {
    hull() {
        translate([-length/2, 0]) circle(d = d);
        translate([ length/2, 0]) circle(d = d);
    }
}
```

Then extrude:

```scad
linear_extrude(height = 5)
    slot_2d(30, 8);
```

Prefer 2D hull + extrusion over 3D hull where possible. It is usually faster and cleaner.

## `minkowski()`

Combines two shapes by sweeping one around the other. Useful for rounded boxes, but computationally expensive.

```scad
module rounded_box(w, d, h, r) {
    minkowski() {
        cube([w - 2*r, d - 2*r, h - 2*r], center = true);
        sphere(r = r);
    }
}
```

Agent caution: `minkowski()` can render slowly. Prefer `offset()` + `linear_extrude()` for 2D-rounded plates.

## `multmatrix()`

Applies a matrix transformation. Most AI-generated models should avoid it unless implementing advanced transforms.

## Debug transforms

OpenSCAD supports modifier characters that are useful while debugging:

```scad
# object(); // highlight
% object(); // transparent/background
! object(); // show only this subtree
* object(); // disable subtree
```

Use these in temporary debug output only. Keep final deliverables clean unless the user requests debug toggles.
