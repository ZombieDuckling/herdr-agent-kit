/*
Model: Generic flat kit card with frame, sprues, parts, slots, and relief
Units: millimetres
Export: Render (F6), then export STL/3MF
*/

/* [Card] */
card_w = 120; // [60:1:250]
card_h = 100; // [60:1:250]
card_t = 2.0; // [1:0.1:4]
corner_r = 8; // [0:0.5:20]
frame_w = 2.2; // [1.2:0.1:5]

/* [Sprues] */
sprue_w = 1.2; // [0.8:0.1:3]
breakaway_w = 0.75; // [0.4:0.05:1.5]

/* [Parts] */
panel_w = 42; // [20:1:80]
panel_h = 58; // [20:1:90]
hub_d = 18; // [8:1:35]
slot_w = 3.0; // [1:0.1:8]
slot_l = 12; // [4:0.5:30]

/* [Detail] */
detail_line_w = 0.8; // [0.4:0.05:2]
detail_gap = 1.4; // [0.6:0.1:4]
label_text = "KIT CARD";
label_size = 7; // [3:1:16]
label_height = 0.55; // [0.2:0.05:1.2]

/* [Manufacturing] */
clearance = 0.25; // [0:0.05:1]
min_feature = 0.6; // [0.3:0.05:1.2]

/* [Hidden] */
eps = 0.01;
$fn = 48;

inner_w = card_w - 2 * frame_w;
inner_h = card_h - 2 * frame_w;
safe_corner_r = min(corner_r, min(card_w, card_h) / 2 - eps);
detail_pitch = detail_line_w + detail_gap;

assert(card_w > 2 * frame_w + 20, "card_w too small for frame");
assert(card_h > 2 * frame_w + 20, "card_h too small for frame");
assert(card_t > 0, "card_t must be positive");
assert(frame_w >= min_feature, "frame_w below min_feature");
assert(sprue_w >= min_feature, "sprue_w below min_feature");
assert(breakaway_w >= min_feature, "breakaway_w below min_feature");
assert(detail_line_w >= min_feature, "detail_line_w below min_feature");
assert(detail_gap >= min_feature, "detail_gap below min_feature");
assert(panel_w < card_w / 2 - frame_w, "panel_w too large for two-panel layout");
assert(panel_h < card_h - 2 * frame_w, "panel_h too large for card");
assert(slot_w > clearance, "slot_w must be greater than clearance");

module rounded_rect_2d(w, h, r) {
    if (r <= eps)
        square([w, h], center = true);
    else
        offset(r = r)
            offset(delta = -r)
                square([w, h], center = true);
}

module capsule_2d(length, width) {
    hull() {
        translate([-length / 2 + width / 2, 0])
            circle(d = width);
        translate([length / 2 - width / 2, 0])
            circle(d = width);
    }
}

module runner_segment_2d(a, b, width) {
    hull() {
        translate(a)
            circle(d = width);
        translate(b)
            circle(d = width);
    }
}

module frame_2d() {
    difference() {
        rounded_rect_2d(card_w, card_h, safe_corner_r);
        rounded_rect_2d(inner_w, inner_h, max(0, safe_corner_r - frame_w));
    }
}

module panel_outline_2d(w, h) {
    polygon(points = [
        [-w / 2, -h / 2],
        [ w / 2, -h * 0.34],
        [ w / 2,  h * 0.34],
        [-w / 2,  h / 2]
    ]);
}

module decorative_panel_2d(w, h) {
    difference() {
        panel_outline_2d(w, h);

        for (x = [-w / 2 + 5 : detail_pitch : w / 2 - 5])
            translate([x, 0])
                square([detail_gap, h - 12], center = true);

        translate([0, 0])
            capsule_2d(slot_l, slot_w + clearance);
    }

    runner_segment_2d([-w / 2 + 4, -h / 2 + 4], [w / 2 - 4, 0], detail_line_w);
    runner_segment_2d([-w / 2 + 4, h / 2 - 4], [w / 2 - 4, 0], detail_line_w);
}

module circular_part_2d(d) {
    difference() {
        circle(d = d);
        translate([0, -d * 0.12])
            capsule_2d(slot_l, slot_w + clearance);
    }
}

module wheel_part_2d(d) {
    difference() {
        circle(d = d);
        circle(d = d * 0.28);
        for (i = [0 : 7])
            rotate(360 * i / 8)
                translate([d * 0.26, 0])
                    capsule_2d(d * 0.34, detail_gap);
    }
}

module plaque_2d() {
    rounded_rect_2d(28, 16, 1.5);
}

module parts_2d() {
    translate([-28, 18])
        decorative_panel_2d(panel_w, panel_h);

    mirror([1, 0])
        translate([-28, 18])
            decorative_panel_2d(panel_w, panel_h);

    translate([0, -10])
        circular_part_2d(hub_d + 8);

    translate([-38, -26])
        wheel_part_2d(18);

    translate([36, -30])
        plaque_2d();
}

module sprues_2d() {
    runner_segment_2d([-inner_w / 2, 0], [inner_w / 2, 0], sprue_w);
    runner_segment_2d([0, -inner_h / 2], [0, inner_h / 2], sprue_w);
    runner_segment_2d([-inner_w / 2, -36], [inner_w / 2, -36], sprue_w);

    runner_segment_2d([-52, 18], [-49, 18], breakaway_w);
    runner_segment_2d([-7, 18], [-4, 18], breakaway_w);
    runner_segment_2d([52, 18], [49, 18], breakaway_w);
    runner_segment_2d([7, 18], [4, 18], breakaway_w);
    runner_segment_2d([0, -26], [0, -18], breakaway_w);
    runner_segment_2d([-38, -36], [-38, -35], breakaway_w);
    runner_segment_2d([22, -30], [15, -30], breakaway_w);
    runner_segment_2d([50, -30], [inner_w / 2, -30], breakaway_w);
}

module card_2d() {
    union() {
        frame_2d();
        sprues_2d();
        parts_2d();
    }
}

module raised_label() {
    translate([36, -30, card_t - eps])
        linear_extrude(height = label_height + eps)
            text(label_text, size = label_size, halign = "center", valign = "center");
}

module model() {
    union() {
        linear_extrude(height = card_t)
            card_2d();
        raised_label();
    }
}

model();
