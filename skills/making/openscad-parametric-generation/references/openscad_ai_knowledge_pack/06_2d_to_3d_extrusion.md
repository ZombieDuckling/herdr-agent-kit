# 06 — 2D to 3D Extrusion

Extrusion is one of the strongest modelling strategies in OpenSCAD. It lets the agent define clean 2D profiles, then convert them into printable solids.

## `linear_extrude()`

Creates a 3D object from a 2D shape by extruding along Z.

```scad
linear_extrude(height = 10)
    circle(d = 20);
```

Common parameters:

```scad
linear_extrude(
    height = 10,
    center = false,
    convexity = 10,
    twist = 0,
    slices = 20,
    scale = 1
)
    shape_2d();
```

Use `center = false` for print-oriented solids that start at Z = 0. Use `center = true` for symmetric cutters.

## 2D-first strategy

For plates, signs, brackets, keychains, outlines, slots, rounded rectangles, and profiles, generate a 2D shape first.

```scad
module rounded_plate_2d(w, d, r) {
    offset(r = r)
        offset(delta = -r)
            square([w, d], center = true);
}

linear_extrude(height = 5)
    rounded_plate_2d(80, 40, 5);
```

## Cut holes in 2D before extruding

```scad
module plate_profile_2d(w, d, r, hole_d, hole_inset) {
    difference() {
        offset(r = r) offset(delta = -r) square([w, d], center = true);
        for (x = [-w/2 + hole_inset, w/2 - hole_inset])
        for (y = [-d/2 + hole_inset, d/2 - hole_inset])
            translate([x, y]) circle(d = hole_d);
    }
}

linear_extrude(height = 4)
    plate_profile_2d(80, 40, 4, 5, 8);
```

This often renders faster and cleaner than creating a 3D plate and subtracting many 3D cylinders.

## Raised text

```scad
module raised_label(text_value, size, height) {
    linear_extrude(height = height)
        text(text_value, size = size, halign = "center", valign = "center");
}

translate([0, 0, 5]) raised_label("A1", 12, 1);
```

## Engraved text

Subtract extruded text from the target. Make the text cutter slightly deeper than the target engraving depth.

```scad
eps = 0.01;
engrave_depth = 0.8;
plate_t = 5;

difference() {
    linear_extrude(height = plate_t) square([60, 30], center = true);
    translate([0, 0, plate_t - engrave_depth])
        linear_extrude(height = engrave_depth + eps)
            text("NAME", size = 8, halign = "center", valign = "center");
}
```

## `rotate_extrude()`

Creates a rotationally symmetric solid by rotating a 2D profile around the Z-axis.

```scad
rotate_extrude($fn = 96)
    translate([10, 0, 0]) circle(d = 3);
```

Use for knobs, rings, wheels, vases, pulleys, domed caps, washers, and lathe-like forms.

Important: the profile should generally sit on the positive X side of the origin. If the profile crosses the rotation axis, geometry may self-intersect.

## Projection

`projection()` flattens 3D geometry into 2D. It can be useful for generating outlines from a 3D model.

```scad
projection(cut = false)
    rotate([90, 0, 0]) object_3d();
```

Use sparingly in generated production models. It can be useful for debugging, laser-cut outlines, or converting a side view into 2D.

## Imported SVG pattern

```scad
linear_extrude(height = 3)
    import("logo.svg");
```

Agent caution: imported SVGs may contain multiple paths, self-intersections, scale issues, or unsupported features. Always expose scale and height parameters when generating around imports.

```scad
logo_scale = 0.5;
logo_height = 2;

linear_extrude(height = logo_height)
    scale([logo_scale, logo_scale])
        import("logo.svg");
```

## When to choose extrusion

Choose extrusion when the user describes:

- a flat part with holes;
- a sign/plaque/keychain/nameplate;
- a bracket profile;
- a gasket/spacer/washers;
- a sketch-like outline;
- a part whose top and bottom outline are mostly identical;
- a rotational part when using `rotate_extrude()`.
