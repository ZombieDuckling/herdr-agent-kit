# 02 — Syntax, Values, Variables, and Scope

## Statement forms

OpenSCAD source is a list of statements. Common forms:

```scad
name = value;
object();
transform() object();
transform() {
    object();
    object();
}
module name(args) { ... }
function name(args) = expression;
```

Objects and assignments end with semicolons. Transformations and boolean operators act on following child geometry and do not take a trailing semicolon before the child.

Correct:

```scad
translate([10, 0, 0])
    cube(5);
```

Wrong pattern:

```scad
translate([10, 0, 0]);
cube(5); // translation no longer applies
```

## Comments

```scad
// single-line comment

/* multi-line
   comment */
```

Use comments to explain intent, not every obvious primitive.

## Values

Important OpenSCAD value types:

- numbers;
- booleans: `true`, `false`;
- strings;
- vectors/lists: `[1, 2, 3]`;
- ranges: `[0 : 2 : 10]`;
- `undef`;
- objects/dictionaries in newer development snapshots.

## Numbers

OpenSCAD uses floating-point numbers. Do not rely on exact equality for derived decimal geometry. Avoid coincident faces by using an epsilon margin.

```scad
eps = 0.01;

// cutter extends below and above target
translate([0, 0, -eps])
    cylinder(h = plate_h + 2*eps, d = hole_d);
```

## Vectors

Vectors are used for dimensions, coordinates, rotations, colors, and lists.

```scad
size = [80, 40, 12];
pos = [10, -5, 0];
rot = [0, 0, 45];

translate(pos)
    rotate(rot)
        cube(size, center = true);
```

Indexing is zero-based:

```scad
v = [10, 20, 30];
echo(v[0]); // 10
```

Nested vectors are used for points, paths, matrices, and polyhedra:

```scad
points = [[0,0], [20,0], [20,10], [0,10]];
polygon(points);
```

## Ranges

Ranges are common in loops:

```scad
for (x = [0 : 10 : 100])
    translate([x, 0, 0]) cube(2);
```

Range syntax uses colons, not commas.

## Variables behave like override-able constants

OpenSCAD variables are not mutable runtime variables in the normal imperative sense. Values are evaluated at compile time, scoped, and effectively constant within a scope. The last assignment in a scope applies within that scope.

For generated code, avoid trying to update variables inside loops like JavaScript/Python. Instead, use list comprehensions, functions, or derive values directly.

Bad pattern:

```scad
total = 0;
for (i = [0:5]) total = total + i; // not how OpenSCAD should be used
```

Better:

```scad
values = [for (i = [0:5]) i];
```

## Scope

Braces create inner scopes. Variables from outer scopes are visible in inner scopes. Inner-scope variables do not leak outward.

```scad
a = 10;

translate([0,0,0]) {
    b = 20;
    cube([a, b, 5]);
}

// b is not available here
```

## `undef`

An undefined variable evaluates to `undef` with a warning. Use `is_undef()` when checking optional values.

```scad
module pin(d = undef) {
    actual_d = is_undef(d) ? 5 : d;
    cylinder(h = 10, d = actual_d);
}
```

## Naming conventions for agent-generated code

Recommended:

- `snake_case` for variables/modules/functions;
- suffix dimensions with `_w`, `_d`, `_h`, `_r`, `_d`, `_t` where useful;
- use `eps` for boolean overlap margin;
- use `clearance` for fit allowance;
- prefix debug toggles with `show_` or `debug_`.

Examples:

```scad
plate_w = 90;
plate_d = 45;
plate_t = 6;
corner_r = 5;
hole_d = 4.2;
show_axes = false;
```
