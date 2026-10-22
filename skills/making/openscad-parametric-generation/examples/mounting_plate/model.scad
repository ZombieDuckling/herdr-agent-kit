/*
Model: Example rounded mounting plate with four through holes and raised label
Units: millimetres
Export: Render (F6), then export STL/3MF
*/

/* [Dimensions] */
plate_w = 80; // [20:1:200]
plate_d = 40; // [20:1:200]
plate_t = 5; // [1:0.5:30]
corner_r = 4; // [0:0.5:20]

/* [Holes] */
hole_d = 4.2; // [1:0.1:20]
hole_inset = 8; // [3:0.5:40]

/* [Label] */
add_label = true;
label_text = "A1";
label_size = 9; // [4:1:30]
label_height = 0.8; // [0.2:0.1:3]

/* [Hidden] */
eps = 0.01;
$fn = 64;

safe_corner_r = min(corner_r, min(plate_w, plate_d) / 2 - eps);

assert(plate_w > 0, "plate_w must be positive");
assert(plate_d > 0, "plate_d must be positive");
assert(plate_t > 0, "plate_t must be positive");
assert(hole_d > 0, "hole_d must be positive");
assert(hole_inset > hole_d / 2, "hole_inset must keep holes inside plate");
assert(plate_w > 2 * hole_inset, "plate_w too small for hole_inset");
assert(plate_d > 2 * hole_inset, "plate_d too small for hole_inset");
assert(safe_corner_r >= 0, "corner_r too large for plate dimensions");
assert(label_height > 0, "label_height must be positive");

module rounded_rect_2d(w, d, r) {
    if (r <= eps)
        square([w, d], center = true);
    else
        offset(r = r)
            offset(delta = -r)
                square([w, d], center = true);
}

module plate_body() {
    linear_extrude(height = plate_t)
        rounded_rect_2d(plate_w, plate_d, safe_corner_r);
}

module four_corner_positions() {
    for (x = [-plate_w / 2 + hole_inset, plate_w / 2 - hole_inset])
    for (y = [-plate_d / 2 + hole_inset, plate_d / 2 - hole_inset])
        translate([x, y, 0])
            children();
}

module hole_cutters() {
    four_corner_positions()
        translate([0, 0, -eps])
            cylinder(h = plate_t + 2 * eps, d = hole_d);
}

module raised_label() {
    translate([0, 0, plate_t - eps])
        linear_extrude(height = label_height + eps)
            text(label_text, size = label_size, halign = "center", valign = "center");
}

module model() {
    union() {
        difference() {
            plate_body();
            hole_cutters();
        }
        if (add_label)
            raised_label();
    }
}

model();
