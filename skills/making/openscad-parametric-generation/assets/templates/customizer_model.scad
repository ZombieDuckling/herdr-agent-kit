/*
Model: Customizer-ready starter
Units: millimetres
Export: Render (F6), then export STL/3MF
*/

/* [Dimensions] */
part_w = 80; // [20:1:200]
part_d = 40; // [20:1:200]
part_t = 5; // [1:0.5:30]
corner_r = 4; // [0:0.5:20]

/* [Options] */
add_label = true;
label_text = "A1";
label_size = 10; // [4:1:30]
label_height = 0.8; // [0.2:0.1:3]

/* [Hidden] */
eps = 0.01;
$fn = 64;

safe_corner_r = min(corner_r, min(part_w, part_d) / 2 - eps);

assert(part_w > 0, "part_w must be positive");
assert(part_d > 0, "part_d must be positive");
assert(part_t > 0, "part_t must be positive");
assert(corner_r >= 0, "corner_r must be non-negative");
assert(safe_corner_r >= 0, "corner_r too large for part dimensions");

module rounded_rect_2d(w, d, r) {
    if (r <= eps)
        square([w, d], center = true);
    else
        offset(r = r)
            offset(delta = -r)
                square([w, d], center = true);
}

module base_body() {
    linear_extrude(height = part_t)
        rounded_rect_2d(part_w, part_d, safe_corner_r);
}

module label() {
    translate([0, 0, part_t - eps])
        linear_extrude(height = label_height + eps)
            text(label_text, size = label_size, halign = "center", valign = "center");
}

module model() {
    union() {
        base_body();
        if (add_label)
            label();
    }
}

model();
