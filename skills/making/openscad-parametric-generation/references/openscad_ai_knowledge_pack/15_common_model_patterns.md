# 15 — Common Model Patterns

This file gives reusable modelling patterns for AI-generated OpenSCAD.

## Rounded rectangle plate

```scad
module rounded_rect_2d(w, d, r) {
    offset(r = r)
        offset(delta = -r)
            square([w, d], center = true);
}

module rounded_plate(w, d, t, r) {
    linear_extrude(height = t)
        rounded_rect_2d(w, d, r);
}
```

## Four-corner hole placement

```scad
module four_corners(w, d, inset) {
    for (x = [-w/2 + inset, w/2 - inset])
    for (y = [-d/2 + inset, d/2 - inset])
        translate([x, y, 0]) children();
}

four_corners(80, 40, 8)
    cylinder(h = 5, d = 4);
```

## Through-hole plate

```scad
module through_hole_plate(w, d, t, r, hole_d, inset) {
    eps = 0.01;
    difference() {
        rounded_plate(w, d, t, r);
        four_corners(w, d, inset)
            translate([0, 0, -eps])
                cylinder(h = t + 2*eps, d = hole_d);
    }
}
```

## Hollow box/tray

```scad
module tray(outer_w, outer_d, outer_h, wall, bottom_t) {
    eps = 0.01;
    inner_w = outer_w - 2*wall;
    inner_d = outer_d - 2*wall;
    inner_h = outer_h - bottom_t;

    assert(inner_w > 0, "inner width <= 0");
    assert(inner_d > 0, "inner depth <= 0");
    assert(inner_h > 0, "inner height <= 0");

    difference() {
        translate([0,0,outer_h/2]) cube([outer_w, outer_d, outer_h], center = true);
        translate([0,0,bottom_t + inner_h/2])
            cube([inner_w, inner_d, inner_h + eps], center = true);
    }
}
```

## Rounded tray using 2D profiles

```scad
module rounded_rect_2d(w, d, r) {
    offset(r = r) offset(delta = -r) square([w, d], center = true);
}

module rounded_tray(outer_w, outer_d, outer_h, wall, bottom_t, r) {
    eps = 0.01;
    difference() {
        linear_extrude(height = outer_h)
            rounded_rect_2d(outer_w, outer_d, r);
        translate([0,0,bottom_t])
            linear_extrude(height = outer_h - bottom_t + eps)
                rounded_rect_2d(outer_w - 2*wall, outer_d - 2*wall, max(0, r - wall));
    }
}
```

## Slot

```scad
module slot_2d(length, d) {
    hull() {
        translate([-length/2, 0]) circle(d = d);
        translate([ length/2, 0]) circle(d = d);
    }
}

module slot_cutter(length, d, h) {
    linear_extrude(height = h, center = true)
        slot_2d(length, d);
}
```

## Standoff boss

```scad
module standoff(h, outer_d, hole_d) {
    eps = 0.01;
    difference() {
        cylinder(h = h, d = outer_d);
        translate([0,0,-eps]) cylinder(h = h + 2*eps, d = hole_d);
    }
}
```

## Ring/washer

```scad
module washer(outer_d, inner_d, t) {
    eps = 0.01;
    difference() {
        cylinder(h = t, d = outer_d);
        translate([0,0,-eps]) cylinder(h = t + 2*eps, d = inner_d);
    }
}
```

## Embossed label on plate

```scad
module embossed_text(label, size, height) {
    linear_extrude(height = height)
        text(label, size = size, halign = "center", valign = "center");
}

translate([0, 0, plate_t]) embossed_text("A1", 10, 1);
```

## Engraved label cutter

```scad
module engraved_text_cutter(label, size, depth) {
    linear_extrude(height = depth)
        text(label, size = size, halign = "center", valign = "center");
}
```

Use inside `difference()` and place at the top surface.

## Polar ridges on a knob

```scad
module knob_ridge(radius, h, ridge_w, ridge_d) {
    translate([radius, 0, h/2])
        cube([ridge_d, ridge_w, h], center = true);
}

module ridged_knob(d, h, ridge_count, ridge_d) {
    union() {
        cylinder(h = h, d = d);
        for (i = [0 : ridge_count - 1])
            rotate([0,0,360*i/ridge_count])
                knob_ridge(d/2, h, 3, ridge_d);
    }
}
```

## Flat-backed relief clip

```scad
module flat_back(z_min = 0, z_max = 20) {
    intersection() {
        children();
        translate([-1000, -1000, z_min]) cube([2000, 2000, z_max - z_min]);
    }
}
```

## Pattern selection logic

- Plate: rounded rectangle + holes.
- Tray/enclosure: outer minus inner cavity.
- Mount: base plate + bosses + holes.
- Sign/keychain: 2D profile + text + loop hole.
- Knob: cylinder + ridges + shaft hole.
- Adapter: difference between outer body and inner channel/hole.
