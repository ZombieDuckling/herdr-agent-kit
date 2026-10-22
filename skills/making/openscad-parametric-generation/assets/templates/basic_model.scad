/*
Model: Basic parametric solid
Units: millimetres
Export: Render (F6), then export STL/3MF
*/

/* [Dimensions] */
width = 60; // [10:1:200]
depth = 30; // [10:1:200]
height = 8; // [1:0.5:80]

/* [Hidden] */
eps = 0.01;
$fn = 64;

assert(width > 0, "width must be positive");
assert(depth > 0, "depth must be positive");
assert(height > 0, "height must be positive");

module body() {
    translate([0, 0, height / 2])
        cube([width, depth, height], center = true);
}

module model() {
    body();
}

model();
