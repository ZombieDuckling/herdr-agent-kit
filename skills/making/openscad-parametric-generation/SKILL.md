---
name: openscad-parametric-generation
description: Generate, edit, validate, and repair OpenSCAD parametric CAD models. Use when working with OpenSCAD, .scad files, 3D-printable parametric parts, Customizer-friendly CAD scripts, STL/PNG export, model repair after OpenSCAD errors, kit cards/model sprues, or iterative edits such as changing dimensions, holes, labels, walls, enclosures, trays, brackets, knobs, signs, jigs, fixtures, and other functional printed objects.
---

# OpenSCAD Parametric Generation

Use this skill to turn natural-language part requests into clean OpenSCAD source that is readable, printable, and easy for later agents to modify.

## Core Workflow

1. Interpret the requested object, purpose, critical dimensions, fit constraints, manufacturing method, and output needs. Ask only when a missing detail makes the model impossible or unsafe; otherwise choose conservative defaults and document them.
2. Choose a modeling strategy before writing code:
   - Plates, signs, gaskets, keychains: 2D profile plus `linear_extrude()`.
   - Kit cards and model sprues: 2D card layout plus `linear_extrude()`, with a runner frame, breakaway connectors, part silhouettes, tabs, slots, labels, and relief/cutout detail.
   - Trays and enclosures: outer body minus inner cavity, with wall and bottom thickness parameters.
   - Repeated holes, bosses, vents, or tabs: loops and coordinate helpers.
   - Cylindrical or lathe-like parts: cylinders, tapered cylinders, or `rotate_extrude()`.
   - Complex mechanical standards such as threads or gears: consider a documented library only when native OpenSCAD would be fragile.
3. Generate `model.scad` and `README.md` unless the user requests a different shape.
4. Validate with `scripts/validate_scad.sh path/to/model.scad` when OpenSCAD is available. If validation cannot run, clearly state that the model is unvalidated and why.
5. If OpenSCAD reports errors, make the smallest repair, rerun validation, and stop after a bounded number of attempts.

## Source Requirements

Every generated `.scad` file must:

- Start with a short description comment including units and export notes.
- Expose user-adjustable values at the top in Customizer-style sections such as `/* [Dimensions] */`, `/* [Holes] */`, and `/* [Hidden] */`.
- Use millimetres unless the user explicitly asks otherwise.
- Define `eps = 0.01` or a similar boolean overlap value.
- Keep important dimensions parameterized or derived from top-level parameters.
- Use `assert()` for impossible or non-printable parameter combinations.
- Use modules for meaningful subparts and functions only for pure calculations.
- Put the bottom of printable parts on `Z = 0` unless there is a stated reason not to.
- Avoid mixing 2D and 3D objects in the same boolean operation.
- Make cutters extend fully through targets by `eps` or more.
- Avoid coincident faces and zero-thickness geometry.
- End with exactly one final `model();` call or an equivalent single final assembly call.
- Document any external `use <...>` or `include <...>` dependency in both the source and README.

Prefer standalone native OpenSCAD. Use external libraries such as BOSL2 only when they materially improve a difficult feature, and document setup, install path, purpose, and fallback limitations.

## Replicating A Photographed Part

When the model is a replica of a physical part measured off photos:

- Never let an estimate masquerade as a measurement. Tag every dimension comment `(measured)` or `(GUESS)`, and say which measurements came from which photo. The user must be able to tell at a glance what to trust.
- Take scale from the tape's own printed numbers, not from guessed tick pitch. Tapes print centimetres, so two identified numbers fix mm/px. Autocorrelation tick pitch cannot tell a 1 mm tick from a 10 mm tick - use it only as a cross-check, never as the scale.
- Tesseract frequently reads nothing off a red tape (low contrast, sideways digits). The reliable local route is to draw guide lines at the part's extremes, then ask a vision model which printed tape numbers those lines sit on.
- Cross-check the result against the part's own aspect ratio from a clean outline, and verify final size by parsing the exported STL's vertices rather than trusting a render.
- Features only a few pixels wide (small holes, pin diameters) cannot be measured at photo resolution. Keep them as parameters, mark them `(GUESS)`, and ask the user.
- If OpenSCAD is unavailable, do not fall back to an unverified STL: recover the toolchain first. On macOS, Homebrew's `openscad` cask can be disabled outright ("does not pass the macOS Gatekeeper check") leaving a dangling symlink; install the official DMG from files.openscad.org into `/Applications` instead.

## Kit Card Rules

For kit cards like flat model kits, design the whole card as a coherent 2D manufacturing layout before extrusion:

- Use a rounded rectangular outer runner frame, internal sprue rails, and small breakaway tabs connecting each part to the frame or nearby rails.
- Keep parts as separate silhouettes with functional assembly features: slots, tabs, pegs, sockets, keyed notches, and labels that explain orientation when useful.
- Prefer printable relief and cutouts over tiny sculpted details. Fine linework should be parameterized with `detail_line_w`, `detail_gap`, and `min_feature`.
- Keep breakaway tabs thinner than structural runners, but not so thin they fail during printing. Good FDM defaults are `runner_w = 2.0`, `sprue_w = 1.2`, `breakaway_w = 0.7`, and `min_feature = 0.6`.
- Use 2D `difference()` for decorative panel openings, vents, grille lines, and slots, then extrude the final 2D union to card thickness.
- Place all parts inside the card boundary with explicit margins. Add `assert()` checks for card size, runner width, material thickness, and minimum feature sizes.
- For reference images, approximate the recognizable structure with named primitives and editable parameters; do not bury fragile traced polygons unless the user explicitly supplies vector artwork.
- If the requested subject is a protected character, vehicle, or branded object, make the source easy to re-theme and avoid embedding logos or trademarked text unless the user has permission or the work is personal/noncommercial fan use.

## README Requirements

For each generated model, include:

- What the part is for.
- Key parameters and safe ranges when useful.
- Assumptions made for missing dimensions.
- Print orientation and manufacturing assumptions.
- Export commands for STL and optional PNG.
- Validation status: passed, failed with notes, or not run because OpenSCAD was unavailable.
- Any library or imported asset dependencies.

## Validation And Export

Use the bundled scripts from the skill root:

```bash
scripts/find_openscad.sh
scripts/validate_scad.sh path/to/model.scad
scripts/render_stl.sh path/to/model.scad exports/model.stl
scripts/render_png.sh path/to/model.scad exports/model.png
```

`OPENSCAD_BIN=/path/to/OpenSCAD` overrides binary discovery. On macOS, the binary may live inside `OpenSCAD.app/Contents/MacOS/OpenSCAD`.

## References

Load only the references needed for the current request:

- `references/openscad_ai_knowledge_pack/00_agent_orientation.md`: agent rules and model quality.
- `references/openscad_ai_knowledge_pack/09_customizer_parametric_inputs.md`: Customizer parameter surfaces.
- `references/openscad_ai_knowledge_pack/10_import_export_cli.md`: CLI import/export behavior.
- `references/openscad_ai_knowledge_pack/11_libraries_use_include.md`: library policy.
- `references/openscad_ai_knowledge_pack/12_3d_print_design_rules.md`: FDM/SLA design defaults.
- `references/openscad_ai_knowledge_pack/13_debugging_validation.md`: repair and validation workflow.
- `references/openscad_ai_knowledge_pack/14_ai_generation_protocol.md`: natural-language to OpenSCAD generation protocol.
- `references/openscad_ai_knowledge_pack/15_common_model_patterns.md`: reusable modeling patterns.
- `references/openscad_ai_knowledge_pack/17_reference_cheatsheet.md`: syntax and quick reference.
- `references/kit_card_design.md`: kit card and model sprue layout guidance.

Use templates in `assets/templates/` as starting points when they match the requested object, then adapt them rather than forcing every request into a template.
