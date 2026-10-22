# 14 — AI Generation Protocol for OpenSCAD

This is the practical protocol for converting natural-language requests into OpenSCAD models.

## Step 1: Extract requirements

From the prompt, identify:

- object type;
- purpose;
- critical dimensions;
- fit constraints;
- adjustable parameters;
- manufacturing method;
- aesthetic requirements;
- text/logo content;
- required file/export format;
- external dependencies/imports.

If dimensions are missing, make conservative defaults and expose them as parameters. Do not bury assumptions.

## Step 2: Select modelling strategy

Use this decision tree:

- Flat sign, plate, bracket, gasket, keychain: 2D profile + `linear_extrude()`.
- Box/enclosure/tray: outer solid minus inner cavity, lid features, rounded profile if needed.
- Repeated holes/posts: loops and coordinate functions.
- Cylindrical/lathe shape: `rotate_extrude()` or cylinders/cones.
- Rounded plate: 2D `offset()` + extrusion.
- Organic-ish relief: spheres/domes/hulls, not high-detail sculpting.
- Mechanical standard components: consider library, but document dependency.
- Existing logo/SVG: import + scale + extrude.
- Existing STL edit: import + boolean operations, with caution.

## Step 3: Define parameter surface

Create grouped top-level variables:

```scad
/* [Dimensions] */
...

/* [Feature Options] */
...

/* [Manufacturing] */
clearance = 0.25;
wall = 2.4;

/* [Hidden] */
eps = 0.01;
$fn = 64;
```

Every meaningful dimension should be parameterized or derived from a parameter.

## Step 4: Define derived dimensions

```scad
inner_w = outer_w - 2*wall;
inner_d = outer_d - 2*wall;
inner_h = outer_h - bottom_t;
```

Then assert validity:

```scad
assert(inner_w > 0, "outer_w too small for wall");
```

## Step 5: Create modules

Recommended module set:

```scad
module profile_2d() { ... }
module base_body() { ... }
module hole_cutters() { ... }
module decorative_features() { ... }
module model() { ... }
```

## Step 6: Compose final model

Use `difference()` for cuts and `union()` for additive geometry.

```scad
module model() {
    union() {
        difference() {
            base_body();
            hole_cutters();
        }
        decorative_features();
    }
}

model();
```

## Step 7: Add comments and modification notes

Generated source should include:

- what the model is;
- parameter descriptions;
- export instructions;
- known limitations;
- print notes.

## Step 8: Validate against common failure cases

- no mixed 2D/3D booleans;
- no flush cutters;
- no hidden unparameterized magic dimensions;
- no impossible parameter combinations;
- no text too small for intended print;
- no unsupported library dependency.

## Natural language mapping examples

### “Make a mounting plate with four holes”

Strategy: rounded rectangle 2D profile + 3D hole cutters or 2D holes before extrusion.

Parameters:

```scad
plate_w, plate_d, plate_t, corner_r, hole_d, hole_inset
```

### “Make a box for electronics”

Strategy: outer rounded box, subtract inner cavity, add standoffs, add lid lip if requested.

Parameters:

```scad
outer_w, outer_d, outer_h, wall, bottom_t, standoff_d, screw_hole_d
```

### “Make a coin/token with text”

Strategy: cylinder or circle extrusion, raised/engraved text, optional border ring.

Parameters:

```scad
token_d, token_t, text_value, text_size, text_height, border_w
```

### “Make a knob”

Strategy: cylinder body, grip ridges via loop, central hole, optional pointer mark.

Parameters:

```scad
knob_d, knob_h, shaft_d, ridge_count, ridge_depth
```

## Final output standard

The generated OpenSCAD should be:

- readable;
- parameterized;
- modular;
- printable;
- exportable;
- dependency-declared;
- easy for another AI agent to modify.
