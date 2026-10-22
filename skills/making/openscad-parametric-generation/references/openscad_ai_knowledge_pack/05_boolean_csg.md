# 05 — Boolean CSG

Boolean operations are the backbone of OpenSCAD modelling.

## `union()`

Combines children into one positive object.

```scad
union() {
    cube([40, 20, 6], center = true);
    translate([0, 0, 6]) cylinder(h = 12, d = 10, center = true);
}
```

OpenSCAD has implicit union when objects are listed together, but explicit `union()` is better for generated code.

## `difference()`

Subtracts the second and later child nodes from the first child.

```scad
difference() {
    cube([40, 20, 6], center = true);     // base object
    cylinder(h = 10, d = 5, center = true); // cutter
}
```

Only the first child is kept. Everything after it is negative geometry.

### Correct grouping in `difference()`

If the positive object is made of multiple objects, wrap them in `union()`.

```scad
difference() {
    union() {
        cube([40, 20, 6], center = true);
        translate([0, 0, 6]) cylinder(h = 12, d = 10, center = true);
    }
    cylinder(h = 30, d = 4, center = true);
}
```

Without `union()`, only the first child is the target and the later positive-looking objects may become cutters.

## `intersection()`

Keeps only the overlapping volume of all children.

```scad
intersection() {
    cube([20, 20, 20], center = true);
    sphere(d = 25);
}
```

Use for domes, clipping, keeping only a region, or making flat-backed relief models.

## Boolean overlap margin

Never make cutter geometry end exactly flush with the target face. Extend it through by `eps`.

```scad
eps = 0.01;
plate_t = 6;

translate([0, 0, -eps])
    cylinder(h = plate_t + 2*eps, d = 5);
```

For centered cutters:

```scad
cylinder(h = plate_t + 2*eps, d = hole_d, center = true);
```

## Avoid coincident faces

Coincident faces can create preview flicker, ambiguous booleans, and non-manifold renders. If two solids should merge, overlap them slightly.

Bad:

```scad
cube([20, 20, 5]);
translate([20, 0, 0]) cube([20, 20, 5]); // touches exactly at x=20
```

Better:

```scad
eps = 0.01;
cube([20 + eps, 20, 5]);
translate([20 - eps, 0, 0]) cube([20 + eps, 20, 5]);
```

## Do not mix 2D and 3D in booleans

This is a common failure mode. Keep booleans all-2D or all-3D.

Correct 2D then extrude:

```scad
linear_extrude(height = 5)
difference() {
    square([50, 30], center = true);
    circle(d = 10);
}
```

Correct 3D:

```scad
difference() {
    cube([50, 30, 5], center = true);
    cylinder(h = 10, d = 10, center = true);
}
```

Wrong:

```scad
difference() {
    cube([50, 30, 5], center = true);
    circle(d = 10); // 2D cutter in 3D boolean
}
```

## Boolean templates

### Through-hole plate

```scad
module plate_with_holes(w, d, t, hole_d, inset) {
    eps = 0.01;
    difference() {
        translate([0, 0, t/2]) cube([w, d, t], center = true);
        for (x = [-w/2 + inset, w/2 - inset])
        for (y = [-d/2 + inset, d/2 - inset])
            translate([x, y, t/2])
                cylinder(h = t + 2*eps, d = hole_d, center = true);
    }
}
```

### Counterbored hole

```scad
module counterbore_cutter(t, hole_d, head_d, head_depth) {
    eps = 0.01;
    union() {
        translate([0, 0, t/2])
            cylinder(h = t + 2*eps, d = hole_d, center = true);
        translate([0, 0, t - head_depth/2 + eps])
            cylinder(h = head_depth + 2*eps, d = head_d, center = true);
    }
}
```

### Slot cutter

```scad
module slot_cutter_3d(length, d, t) {
    eps = 0.01;
    linear_extrude(height = t + 2*eps, center = true)
        hull() {
            translate([-length/2, 0]) circle(d = d);
            translate([ length/2, 0]) circle(d = d);
        }
}
```

## Manifold mindset

A final exported model must be watertight. Avoid zero-thickness surfaces, internal coincident faces, self-intersecting polyhedra, and ambiguous cutters.
