/*
Model: CTRL-01 electronics enclosure with open-top box and snap-on vented lid
Units: millimetres
Export: Render (F6), then export STL/3MF
*/

/* [Outer Dimensions] */
outer_w = 90; // [50:1:180]
outer_d = 55; // [35:1:140]
outer_h = 28; // [12:1:80]
corner_r = 5; // [0:0.5:18]

/* [Shell] */
wall = 2.4; // [1.2:0.1:6]
bottom_t = 2.4; // [1.2:0.1:6]
lid_t = 2.0; // [1.2:0.1:5]
lid_lip_h = 3.0; // [1:0.5:8]
lid_lip_wall = 1.4; // [0.8:0.1:4]
lid_overhang = 1.0; // [0:0.25:4]

/* [Mounting] */
standoff_h = 6.0; // [3:0.5:16]
standoff_outer_d = 7.2; // [5:0.2:14]
screw_d = 3.2; // [2:0.1:6]
standoff_inset = 8.5; // [5:0.5:20]

/* [Cable Cutouts] */
cable_w = 18; // [6:1:40]
cable_h = 7; // [3:0.5:18]
cable_z = 10; // [5:0.5:24]

/* [Lid Features] */
vent_count = 5; // [1:1:9]
vent_l = 32; // [10:1:70]
vent_w = 3.2; // [1:0.2:8]
vent_pitch = 6.0; // [3:0.5:12]
label_text = "CTRL-01";
label_size = 8; // [4:1:18]
engrave_depth = 0.55; // [0.2:0.05:1.2]

/* [Snap Fit] */
snap_w = 7; // [3:0.5:14]
snap_h = 1.0; // [0.4:0.1:2]
snap_bump_depth = 0.45; // [0.2:0.05:1]
snap_x_offset = 24; // [10:1:40]
snap_drop = 4.5; // [2:0.5:10]

/* [Manufacturing] */
clearance = 0.25; // [0:0.05:1]
min_wall = 1.2; // [0.8:0.1:2.4]

/* [Hidden] */
eps = 0.01;
$fn = 64;

inner_w = outer_w - 2 * wall;
inner_d = outer_d - 2 * wall;
inner_h = outer_h - bottom_t;
lid_w = outer_w + 2 * lid_overhang;
lid_d = outer_d + 2 * lid_overhang;
lip_outer_w = inner_w - 2 * clearance;
lip_outer_d = inner_d - 2 * clearance;
lip_inner_w = lip_outer_w - 2 * lid_lip_wall;
lip_inner_d = lip_outer_d - 2 * lid_lip_wall;
box_x = -(outer_w + 18) / 2;
lid_x = (outer_w + 18) / 2;
outer_r = min(corner_r, min(outer_w, outer_d) / 2 - eps);
inner_r = max(0, outer_r - wall);
lid_r = min(outer_r + lid_overhang, min(lid_w, lid_d) / 2 - eps);
lip_outer_r = max(0, inner_r - clearance);
lip_inner_r = max(0, lip_outer_r - lid_lip_wall);

assert(outer_w > 2 * wall + 20, "outer_w too small for shell");
assert(outer_d > 2 * wall + 20, "outer_d too small for shell");
assert(outer_h > bottom_t + standoff_h, "outer_h too short for standoffs");
assert(wall >= min_wall, "wall below min_wall");
assert(bottom_t >= min_wall, "bottom_t below min_wall");
assert(lid_t >= min_wall, "lid_t below min_wall");
assert(lid_lip_wall >= min_wall, "lid_lip_wall below min_wall");
assert(lip_inner_w > 0, "lid lip inner width is invalid");
assert(lip_inner_d > 0, "lid lip inner depth is invalid");
assert(standoff_outer_d > screw_d + 2 * min_wall, "standoff too thin around screw hole");
assert(standoff_inset + standoff_outer_d / 2 < min(inner_w, inner_d) / 2, "standoffs too close to enclosure center/edge");
assert(cable_z > cable_h / 2, "cable cutout below bottom");
assert(cable_z + cable_h / 2 < outer_h - wall, "cable cutout too high");
assert(vent_count >= 1, "vent_count must be at least 1");
assert(vent_w >= min_wall, "vent_w below min_wall");
assert(vent_l < lip_inner_w, "vents too long for lid opening");

module rounded_rect_2d(w, d, r) {
    if (r <= eps)
        square([w, d], center = true);
    else
        offset(r = r)
            offset(delta = -r)
                square([w, d], center = true);
}

module slot_2d(length, width) {
    hull() {
        translate([-length / 2 + width / 2, 0])
            circle(d = width);
        translate([length / 2 - width / 2, 0])
            circle(d = width);
    }
}

module rounded_ring_2d(outer_width, outer_depth, inner_width, inner_depth, outer_radius, inner_radius) {
    difference() {
        rounded_rect_2d(outer_width, outer_depth, outer_radius);
        rounded_rect_2d(inner_width, inner_depth, inner_radius);
    }
}

module standoff_positions() {
    for (x = [-inner_w / 2 + standoff_inset, inner_w / 2 - standoff_inset])
    for (y = [-inner_d / 2 + standoff_inset, inner_d / 2 - standoff_inset])
        translate([x, y, 0])
            children();
}

module outer_shell() {
    linear_extrude(height = outer_h)
        rounded_rect_2d(outer_w, outer_d, outer_r);
}

module cavity_cutter() {
    translate([0, 0, bottom_t])
        linear_extrude(height = inner_h + eps)
            rounded_rect_2d(inner_w, inner_d, inner_r);
}

module standoffs() {
    standoff_positions()
        translate([0, 0, bottom_t - eps])
            cylinder(h = standoff_h + eps, d = standoff_outer_d);
}

module standoff_hole_cutters() {
    standoff_positions()
        translate([0, 0, -eps])
            cylinder(h = bottom_t + standoff_h + 2 * eps, d = screw_d);
}

module cable_cutters() {
    for (side = [-1, 1])
        translate([0, side * (outer_d / 2), cable_z])
            rotate([90, 0, 0])
                linear_extrude(height = wall + 2 * eps, center = true)
                    slot_2d(cable_w, cable_h);
}

module snap_pocket_cutters() {
    for (side = [-1, 1])
    for (x = [-snap_x_offset, snap_x_offset])
        translate([x, side * (outer_d / 2 - wall / 2), outer_h - snap_drop])
            cube([snap_w, wall + 2 * eps, snap_h], center = true);
}

module box_part() {
    translate([box_x, 0, 0])
        difference() {
            union() {
                difference() {
                    outer_shell();
                    cavity_cutter();
                }
                standoffs();
            }
            standoff_hole_cutters();
            cable_cutters();
            snap_pocket_cutters();
        }
}

module lid_plate() {
    translate([0, 0, lid_lip_h])
        linear_extrude(height = lid_t)
            rounded_rect_2d(lid_w, lid_d, lid_r);
}

module lid_lip() {
    linear_extrude(height = lid_lip_h + eps)
        rounded_ring_2d(lip_outer_w, lip_outer_d, lip_inner_w, lip_inner_d, lip_outer_r, lip_inner_r);
}

module lid_snap_bumps() {
    for (side = [-1, 1])
    for (x = [-snap_x_offset, snap_x_offset])
        translate([x, side * (lip_outer_d / 2 + snap_bump_depth / 2 - eps), lid_lip_h - snap_drop / 2])
            cube([snap_w, snap_bump_depth, snap_h], center = true);
}

module vent_cutters() {
    start = -(vent_count - 1) * vent_pitch / 2;
    for (i = [0 : vent_count - 1])
        translate([0, start + i * vent_pitch, lid_lip_h - eps])
            linear_extrude(height = lid_t + 2 * eps)
                slot_2d(vent_l, vent_w);
}

module label_cutter() {
    translate([0, -lid_d * 0.36, lid_lip_h + lid_t - engrave_depth])
        linear_extrude(height = engrave_depth + 2 * eps)
            text(label_text, size = label_size, halign = "center", valign = "center");
}

module lid_part() {
    translate([lid_x, 0, 0])
        difference() {
            union() {
                lid_plate();
                lid_lip();
                lid_snap_bumps();
            }
            vent_cutters();
            label_cutter();
        }
}

module model() {
    union() {
        box_part();
        lid_part();
    }
}

model();
