# 09 — Customizer and Parametric Inputs

OpenSCAD Customizer provides a GUI for editing top-level model parameters. This is directly relevant for an AI parametric design tool because it imposes a clean parameter surface.

## Basic principle

Customizer displays suitable variables assigned near the top of the main file. It lets non-coders modify parameters without editing source code.

A Customizer-friendly script starts like this:

```scad
/* [Dimensions] */
width = 80;
depth = 40;
height = 12;
wall_thickness = 2.4;

/* [Holes] */
hole_diameter = 4.2;
hole_inset = 8;

/* [Options] */
add_label = true;
label_text = "A1";

/* [Hidden] */
eps = 0.01;
$fn = 64;
```

## Supported variables

For broad compatibility, expose simple literals:

- numbers;
- strings;
- booleans;
- vectors/lists of up to a few numeric literals.

Avoid exposing complex expressions as user-facing parameters. Use simple top-level values, then derive complex values below.

Good:

```scad
outer_width = 100;
wall = 3;
inner_width = outer_width - 2*wall;
```

Bad:

```scad
inner_width = 100 - 2*3; // hard to adjust cleanly
```

## Section headers

Customizer can group variables using comments:

```scad
/* [Main Dimensions] */
box_width = 100;
box_depth = 60;
box_height = 30;

/* [Mounting] */
hole_d = 4;
hole_spacing = 80;
```

Use sections to keep the parameter UI understandable.

## Hidden parameters

Use a hidden section for constants, derived tuning values, or internal toggles.

```scad
/* [Hidden] */
eps = 0.01;
minimum_wall = 1.2;
```

## Sliders and value hints

Customizer-style comments can provide ranges or choices in many OpenSCAD/Thingiverse-compatible workflows. Use these where practical:

```scad
width = 80;          // [20:1:200]
height = 10;         // [1:0.5:50]
quality = "medium"; // [low, medium, high]
```

Even where a parser does not use these hints, they are useful documentation for the AI agent and human editor.

## Agent parameter-surface design

Every generated model should expose:

- main dimensions;
- wall thickness or material thickness;
- clearance values;
- hole diameters and positions;
- resolution/quality where relevant;
- optional features as booleans;
- text content and font where relevant;
- hidden `eps` and derived variables.

## Example: Customizer-ready enclosure

```scad
/* [Outer Dimensions] */
outer_w = 90; // [30:1:200]
outer_d = 50; // [20:1:150]
outer_h = 25; // [5:1:100]
wall = 2.4; // [1.2:0.1:6]

/* [Lid] */
lid_lip_h = 3; // [1:0.5:10]
clearance = 0.25; // [0:0.05:1]

/* [Mounting] */
add_mounting_holes = true;
hole_d = 3.2;
hole_inset = 7;

/* [Hidden] */
eps = 0.01;
$fn = 64;

assert(outer_w > 2*wall, "outer_w too small for wall");
assert(outer_d > 2*wall, "outer_d too small for wall");
assert(outer_h > wall, "outer_h too small");
```

## Why this matters for AI

A natural-language-to-CAD agent should emit code with a stable, machine-readable parameter surface. That lets a later agent modify dimensions without digging through body geometry.
