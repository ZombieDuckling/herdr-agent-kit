# 01 — OpenSCAD Mental Model

## Text-first CAD

OpenSCAD scripts describe a model. They do not store a direct-manipulated CAD history. The viewport is a preview/render of the script.

OpenSCAD is mostly declarative and functional in flavour. You define values, modules, and functions; then instantiate geometry. The code is evaluated to build a tree of geometry operations.

## Preview vs render

OpenSCAD has two important modes:

- Preview: fast, approximate, useful while editing. It can show artifacts that do not exist in final geometry.
- Render: slower, exact mesh generation. Required before final STL-style export.

For AI-generated models, assume preview is for iteration and render is for validation. Bugs that only appear after render are often related to manifoldness, coincident faces, invalid booleans, self-intersections, or mixed 2D/3D operations.

## CSG: constructive solid geometry

The core modelling pattern is constructive solid geometry:

- create positive geometry;
- subtract negative geometry;
- intersect shapes when needed;
- hull or minkowski shapes for smooth blended forms;
- extrude 2D profiles into solids.

The three main boolean operators are:

```scad
union() { a(); b(); }        // combine children

difference() { a(); b(); }   // subtract child 2+ from child 1

intersection() { a(); b(); } // keep only overlapping volume
```

OpenSCAD often permits implicit union when multiple objects are placed side by side, but explicit `union()` is clearer for generated code.

## Coordinate system

Use the conventional OpenSCAD coordinate assumptions:

- X: left/right or width axis;
- Y: front/back or depth axis;
- Z: vertical axis;
- most 2D primitives live on the XY plane;
- extrusions usually grow along Z;
- rotations are in degrees, not radians.

For generated parts, define a consistent origin policy. Good defaults:

- functional part centered in X/Y;
- bottom at Z = 0 for easy printing;
- vertical height grows in +Z;
- symmetry around origin when possible.

## Dimensions and units

OpenSCAD itself does not enforce units. For 3D printing and mechanical parts, treat all numeric dimensions as millimetres unless explicitly stated otherwise.

## Script structure recommended for AI

```scad
// Parameters
part_w = 80;
part_d = 40;
part_h = 12;
clearance = 0.25;
eps = 0.01;
$fn = 64;

// Derived values
wall = 2.4;
inner_w = part_w - 2*wall;

// Validation
assert(part_w > 0, "part_w must be positive");
assert(wall > 0, "wall must be positive");
assert(inner_w > 0, "wall too thick for width");

// Utility modules
module ...

// Part modules
module ...

// Final assembly
module model() {
    ...
}

model();
```

## What counts as parametric

A model is genuinely parametric when changing the top-level parameters updates the part without breaking geometry. It is not enough to expose a few numbers if the model contains hard-coded magic offsets everywhere.

Use derived values to prevent breakage:

```scad
outer_w = 100;
wall = 3;
inner_w = outer_w - 2*wall;
```

Instead of:

```scad
outer_w = 100;
inner_w = 94; // fragile: should derive from wall
```
