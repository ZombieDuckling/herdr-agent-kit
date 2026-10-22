/*
Model: Open-top electronics tray/enclosure
Units: millimetres
Export: Render (F6), then export STL/3MF
*/

/* [Outer Dimensions] */
outer_w = 90; // [30:1:200]
outer_d = 55; // [30:1:200]
outer_h = 28; // [8:1:100]
corner_r = 5; // [0:0.5:25]

/* [Shell] */
wall = 2.4; // [1.2:0.1:8]
bottom_t = 2.4; // [1.2:0.1:8]

/* [Hidden] */
eps = 0.01;
$fn = 64;

inner_w = outer_w - 2 * wall;
inner_d = outer_d - 2 * wall;
inner_h = outer_h - bottom_t;
outer_r = min(corner_r, min(outer_w, outer_d) / 2 - eps);
inner_r = max(0, outer_r - wall);

assert(outer_w > 2 * wall, "outer_w too small for wall");
assert(outer_d > 2 * wall, "outer_d too small for wall");
assert(outer_h > bottom_t, "outer_h must be greater than bottom_t");
assert(wall >= 1.2, "wall is thin for typical FDM printing");
assert(bottom_t >= 1.2, "bottom_t is thin for typical FDM printing");
assert(outer_r >= 0, "corner_r too large for enclosure dimensions");

module rounded_rect_2d(w, d, r) {
    if (r <= eps)
        square([w, d], center = true);
    else
        offset(r = r)
            offset(delta = -r)
                square([w, d], center = true);
}

module outer_body() {
    linear_extrude(height = outer_h)
        rounded_rect_2d(outer_w, outer_d, outer_r);
}

module inner_cavity_cutter() {
    translate([0, 0, bottom_t])
        linear_extrude(height = inner_h + eps)
            rounded_rect_2d(inner_w, inner_d, inner_r);
}

module model() {
    difference() {
        outer_body();
        inner_cavity_cutter();
    }
}

model();
