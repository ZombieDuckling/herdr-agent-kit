# 19 — Suggested Repository Structure for Step 2

This is the recommended repo layout for building the AI-powered parametric OpenSCAD design skill/tool.

```text
openscad-ai-agent/
  README.md
  AGENTREADME.md
  docs/
    openscad_ai_knowledge_pack/
      *.md
  prompts/
    system_prompt.md
    model_generation_contract.md
    repair_prompt.md
    image_reference_prompt.md
  templates/
    basic_model.scad
    customizer_model.scad
    plate_with_holes.scad
    enclosure.scad
    relief_sign.scad
  examples/
    mounting_plate/
      model.scad
      README.md
    small_enclosure/
      model.scad
      README.md
  scripts/
    render_stl.sh
    render_png.sh
    validate_scad.sh
  tests/
    smoke_test_models/
  exports/
    .gitkeep
```

## `AGENTREADME.md` purpose

`AGENTREADME.md` should tell Codex/Claude/GPT agents exactly how to behave inside the repo. It should be stricter than the human README.

It should include:

- how to read the knowledge pack;
- code style for generated `.scad` files;
- validation commands;
- where to put generated outputs;
- how to handle missing dimensions;
- how to avoid unsafe/impossible geometry;
- when to use libraries;
- how to document assumptions.

## Minimum viable product

The fastest working version of the tool can be:

1. User prompt enters a web form or CLI.
2. Agent turns prompt into a structured spec JSON.
3. Agent generates `model.scad` from spec and templates.
4. OpenSCAD CLI renders STL and PNG.
5. Agent reads errors/warnings and performs repair loop.
6. User receives `.scad`, `.stl`, `.png`, and parameter summary.

## Spec JSON shape

```json
{
  "object_type": "mounting_plate",
  "units": "mm",
  "parameters": {
    "plate_w": 80,
    "plate_d": 40,
    "plate_t": 5,
    "corner_r": 4,
    "hole_d": 4.2,
    "hole_inset": 8
  },
  "features": [
    {"type": "rounded_plate"},
    {"type": "four_mounting_holes"},
    {"type": "raised_text", "text": "A1"}
  ],
  "print_assumptions": {
    "orientation": "bottom_on_z0",
    "clearance": 0.25,
    "wall_min": 2.0
  }
}
```

## Repair loop

When OpenSCAD CLI fails:

1. Capture stderr/stdout.
2. Identify syntax vs geometry issue.
3. Apply minimal patch.
4. Re-render.
5. Stop after a bounded number of attempts.
6. Return code and explanation if still failing.

## MVP validation command

```bash
openscad -o exports/model.stl model.scad
```

Optional PNG preview:

```bash
openscad -o exports/model.png model.scad
```

## Important product direction

The differentiator is not simply generating OpenSCAD once. The differentiator is repeatable parametric editing: the user can say “make it 20mm wider, add two countersunk holes, round the corners more, and make the label engraved,” and the agent modifies the existing clean parameterized source rather than regenerating a messy new file.
