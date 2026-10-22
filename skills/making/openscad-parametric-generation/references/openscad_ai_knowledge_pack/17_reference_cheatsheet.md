# 17 — OpenSCAD Reference Cheatsheet for Agents

## Syntax

```scad
var = value;
module name(args) { ... }
function name(args) = expression;
name();
include <file.scad>
use <file.scad>
```

## 3D primitives

```scad
cube([x,y,z], center=true);
sphere(r=10);
sphere(d=20);
cylinder(h=10, r=5);
cylinder(h=10, d=10);
cylinder(h=10, r1=8, r2=4);
polyhedron(points=[...], faces=[...]);
```

## 2D primitives

```scad
square([x,y], center=true);
circle(r=10);
circle(d=20);
polygon(points=[[x,y], ...], paths=[...]);
text("Label", size=10, font="Liberation Sans", halign="center", valign="center");
```

## Transformations

```scad
translate([x,y,z]) child();
rotate([x,y,z]) child();
scale([x,y,z]) child();
resize([x,y,z]) child();
mirror([1,0,0]) child();
color("red") child();
offset(r=2) child_2d();
hull() { child1(); child2(); }
minkowski() { child1(); child2(); }
```

## Booleans

```scad
union() { ... }
difference() { positive(); negative(); }
intersection() { ... }
```

## Extrusion

```scad
linear_extrude(height=10, center=false, twist=0, scale=1, slices=20)
    shape_2d();

rotate_extrude($fn=96)
    translate([10,0]) shape_2d();
```

## Control flow

```scad
for (i = [0:10]) child();
for (i = [0:2:10]) child();
for (p = points) translate([p[0], p[1], 0]) child();

if (condition) child(); else other_child();

value = condition ? a : b;
```

## Common functions

```scad
sin(a); cos(a); tan(a);       // degrees
sqrt(x); pow(x,y); abs(x);
min(a,b); max(a,b);
floor(x); ceil(x); round(x);
len(v); norm(v);
concat(a,b); str(a,b);
let(a=1, b=2) expression;
lookup(x, [[x0,y0], [x1,y1]]);
is_undef(x);
```

## Debugging

```scad
echo(value);
assert(condition, "message");
# child(); // highlight
% child(); // transparent
! child(); // show only
* child(); // disable
```

## Special variables

```scad
$fn = 64; // fixed fragments
$fa = 12; // minimum angle per fragment
$fs = 2;  // minimum fragment size
$preview // true in preview mode
$t       // animation time
```

## Clean hole cutter

```scad
eps = 0.01;
translate([0,0,-eps]) cylinder(h = part_h + 2*eps, d = hole_d);
```

## Rounded rectangle

```scad
module rounded_rect_2d(w, d, r) {
    offset(r=r) offset(delta=-r) square([w,d], center=true);
}
```

## Slot

```scad
module slot_2d(length, d) {
    hull() {
        translate([-length/2, 0]) circle(d=d);
        translate([ length/2, 0]) circle(d=d);
    }
}
```

## Parametric file skeleton

```scad
/* [Dimensions] */
w = 80;
d = 40;
h = 6;

/* [Hidden] */
eps = 0.01;
$fn = 64;

assert(w > 0);
assert(d > 0);
assert(h > 0);

module body() {
    translate([0,0,h/2]) cube([w,d,h], center=true);
}

module model() {
    body();
}

model();
```
