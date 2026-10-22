# 08 — Control Flow, Math, and Vectors

OpenSCAD has loops, conditionals, mathematical functions, vector operations, and list comprehensions. These are central to parametric design.

## `for` loops

Use `for` to instantiate repeated geometry.

```scad
for (x = [-20, 0, 20])
    translate([x, 0, 0]) cylinder(h = 5, d = 4);
```

Range loop:

```scad
for (i = [0 : 5]) echo(i);
for (a = [0 : 15 : 360]) rotate([0,0,a]) cube([20,2,2]);
```

Nested loops:

```scad
for (x = [-20, 20])
for (y = [-10, 10])
    translate([x, y, 0]) cylinder(h = 5, d = 4);
```

Multi-variable shorthand:

```scad
for (x = [-20, 20], y = [-10, 10])
    translate([x, y, 0]) cylinder(h = 5, d = 4);
```

## `if` / `else`

Use to conditionally include geometry.

```scad
if (add_label)
    label();
else
    blank_plate();
```

Useful for feature toggles:

```scad
if (with_mounting_holes)
    mounting_hole_cutters();
```

## Ternary operator

Use `condition ? true_value : false_value` for value selection.

```scad
actual_height = heavy_duty ? 8 : 5;
```

## List comprehensions

Generate lists of values or points.

```scad
points = [for (i = [0:5]) [i*10, sin(i*20)*5]];
```

Useful for polygon paths, hole positions, gear-like decorative patterns, and repetitive geometry.

## Math functions

Common functions:

```scad
sin(angle); cos(angle); tan(angle); // degrees
asin(x); acos(x); atan(x);
sqrt(x); pow(x, y);
abs(x); min(a, b); max(a, b);
floor(x); ceil(x); round(x);
len(vector_or_string);
norm(vector);
concat(a, b, c);
str(a, b, c);
```

Trigonometric functions use degrees.

## Position on a circle

```scad
function point_on_circle(r, a) = [r*cos(a), r*sin(a)];

for (a = [0 : 60 : 300]) {
    p = point_on_circle(20, a);
    translate([p[0], p[1], 0]) cylinder(h = 5, d = 3);
}
```

## Polar pattern

```scad
module polar_pattern(count, radius) {
    for (i = [0 : count - 1]) {
        angle = 360 * i / count;
        rotate([0, 0, angle])
            translate([radius, 0, 0])
                children();
    }
}

polar_pattern(8, 20)
    cylinder(h = 4, d = 3);
```

## Vector helpers

```scad
function v2(x, y) = [x, y];
function v3(x, y, z) = [x, y, z];
function mid(a, b) = (a + b) / 2;
```

OpenSCAD supports vector arithmetic in many contexts:

```scad
p1 = [0, 0, 0];
p2 = [10, 5, 0];
pmid = (p1 + p2) / 2;
```

## `let()`

Use `let()` to make complex expressions readable.

```scad
function ring_area(outer_d, inner_d) =
    let(outer_r = outer_d/2, inner_r = inner_d/2)
    PI * (outer_r*outer_r - inner_r*inner_r);
```

## `lookup()`

Useful for interpolation from a table of values.

```scad
function height_at(x) = lookup(x, [[0, 5], [10, 12], [20, 8]]);
```

## Recursion

OpenSCAD supports recursive functions. Use sparingly for agent-generated code; loops and list comprehensions are usually clearer.

## Control-flow design rules for agents

- Use loops for repeated geometry, not copied blocks.
- Use functions to generate repeated coordinate lists.
- Use `if` for optional features.
- Use `assert()` to prevent impossible geometry.
- Use `let()` for complex derived expressions.
- Keep math in named variables when the result influences geometry.
