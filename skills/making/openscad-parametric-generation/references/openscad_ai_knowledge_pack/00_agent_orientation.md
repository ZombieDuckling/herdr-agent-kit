# 00 — Agent Orientation

## What OpenSCAD is good for

OpenSCAD is a script-based solid CAD tool. A model is defined by source code rather than by manually dragging geometry in a viewport. This makes it especially useful for AI-driven parametric modelling because the model state is text, inspectable, reproducible, and version-controllable.

Use OpenSCAD when the target part can be described through dimensions, repetition, symmetry, simple solids, 2D profiles, boolean cuts, and adjustable parameters. This includes brackets, enclosures, jigs, fixtures, signs, trays, adapters, gears with libraries, mechanical plates, knobs, spacers, handles, tool holders, and most functional FDM parts.

Avoid treating OpenSCAD like Blender. It is not built for organic sculpting, mesh painting, subdivision surfaces, animation-quality characters, or constraint-based sketching like Fusion/Onshape/SolidWorks.

## The AI agent's job

The agent should not jump straight from user prompt to code. It should internally perform four stages:

1. Interpret intent: what object is being made, what it must fit, what dimensions matter, what should be adjustable.
2. Choose modelling strategy: 2D profile plus extrusion, primitive CSG, hull/minkowski/offset rounding, imported asset, library-assisted construction, or hybrid.
3. Produce parametric source: top-level parameters, derived dimensions, modules, final assembly, debug helpers.
4. Validate model quality: manifold logic, boolean overlap margins, print orientation, wall thickness, clearance, parameter limits.

## Hard rules for generated OpenSCAD

- Always put user-adjustable dimensions at the top of the file.
- Use millimetres unless the user explicitly states otherwise.
- Prefer named parameters over positional arguments when ambiguity exists.
- Keep the final model call at the bottom of the file.
- Do not mix 2D and 3D objects inside the same boolean operation.
- In `difference()`, make cutters extend fully through the target by a small margin.
- Avoid exactly coincident faces; add small epsilon overlap.
- Use modules for meaningful subparts.
- Use functions for pure calculations only.
- Keep `$fn` configurable and do not set it absurdly high by default.
- Use `assert()` for important parameter constraints.
- If the model is for 3D printing, prioritize watertight solids over visual tricks.

## AI-specific success criteria

A generated design is acceptable when another agent can read the source and modify the model without reverse-engineering arbitrary transforms. Every important geometry decision should be traceable to a parameter, derived variable, or named module.

Bad AI OpenSCAD:

```scad
translate([13.2, -4.8, 7]) rotate([0, 0, 17]) cube([37, 11, 4]);
```

Better AI OpenSCAD:

```scad
mount_angle = 17;
arm_length = 37;
arm_width = 11;
arm_thickness = 4;
mount_offset = [13.2, -4.8, 7];

module angled_mount_arm() {
    translate(mount_offset)
        rotate([0, 0, mount_angle])
            cube([arm_length, arm_width, arm_thickness], center = true);
}
```
