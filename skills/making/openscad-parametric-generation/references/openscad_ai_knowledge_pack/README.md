# OpenSCAD AI Knowledge Pack

This pack is designed for building an AI-powered parametric 3D design agent using OpenSCAD as the first modelling backend.

It is not a copy of the OpenSCAD manual. It is a compressed, task-oriented reference built from the official OpenSCAD documentation surface: the official documentation page, the OpenSCAD cheat sheet, the Wikibooks User Manual, the Wikibooks Language Reference, Customizer documentation, CLI documentation, import/export documentation, library documentation, and the official library index.

## Intended use

Use these Markdown files as supporting knowledge for a coding agent, Codex task, repository documentation, or prompt-injection-resistant internal reference. The pack is optimized for:

- converting natural-language product/part requests into OpenSCAD scripts;
- making models parametric rather than one-off geometry;
- avoiding common manifold, preview/render, and boolean errors;
- creating 3D-print-friendly solids;
- structuring files so future AI agents can modify them safely;
- exporting STL/3MF/SVG/DXF through the GUI or CLI.

## Recommended reading order

1. `00_agent_orientation.md`
2. `01_openscad_mental_model.md`
3. `02_syntax_values_scope.md`
4. `03_geometry_primitives.md`
5. `04_transformations.md`
6. `05_boolean_csg.md`
7. `06_2d_to_3d_extrusion.md`
8. `07_functions_modules_children.md`
9. `08_control_flow_math_vectors.md`
10. `09_customizer_parametric_inputs.md`
11. `10_import_export_cli.md`
12. `11_libraries_use_include.md`
13. `12_3d_print_design_rules.md`
14. `13_debugging_validation.md`
15. `14_ai_generation_protocol.md`
16. `15_common_model_patterns.md`
17. `16_agent_prompt_contract.md`
18. `17_reference_cheatsheet.md`
19. `18_sources_and_attribution.md`

## Core principle for the future AI design tool

OpenSCAD is strong when the agent can describe a model as parameters, modules, transforms, and CSG operations. It is weak when the request requires freeform sculpting, exact surfacing, constraint solving, or direct manipulation. The agent should therefore convert user intent into a structured parametric plan before writing code.

A good OpenSCAD model usually looks like this:

```scad
// 1. Parameters
width = 80;
depth = 40;
height = 12;
corner_r = 4;
hole_d = 5;

$fn = 64;

// 2. Derived values
hole_r = hole_d / 2;

// 3. Reusable modules
module rounded_box_2d(w, d, r) {
    offset(r = r)
        offset(delta = -r)
            square([w, d], center = true);
}

module base_plate() {
    linear_extrude(height = height)
        rounded_box_2d(width, depth, corner_r);
}

module mounting_holes() {
    for (x = [-width/2 + 10, width/2 - 10])
        translate([x, 0, -1])
            cylinder(h = height + 2, r = hole_r);
}

// 4. Final model
difference() {
    base_plate();
    mounting_holes();
}
```

That structure is the baseline target for generated models.
