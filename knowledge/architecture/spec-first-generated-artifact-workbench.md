# spec-first generated artifact workbench

Use this shape when AI is generating media, presentations, pages, UI components,
reports, or code-backed visual artifacts that humans will need to edit later.

The goal is to prevent a prompt from becoming an opaque blob. Keep the intended meaning, the generated source, the rendered output, and the review notes in separate positions.

## folder shape

```text
artifact-workbench/
  README.md                 # front desk: purpose, stages, entry points
  source/                   # script, brief, transcript, requirements, assets
  spec/
    artifact-spec.md         # human-readable contract
    beat-map.md              # sequence, timing, meaning, transitions
    acceptance.md            # editability and review criteria
  build/                    # generated source files or component tree
  scripts/                  # deterministic build/render/export helpers
  renders/                  # outputs for human review
  review/
    findings.md             # requested edits, defects, accepted tradeoffs
    change-log.md           # what changed and why
```

## artifact specification contract

The spec should say:

1. source material and intended audience;
2. thesis or user goal;
3. sequence of beats, scenes, sections, or components;
4. timing or ordering constraints when timing matters;
5. visual, interaction, or tone philosophy;
6. meaning each section must convey;
7. named assets or evidence that must be used;
8. acceptance tests and review surface;
9. what the model may improvise;
10. what the model must not change without approval.

Do not start by locking pixels, frame numbers, component props, file names, or implementation details unless they are part of the contract. Overconstraining the first pass often reduces quality and makes the model optimize local mechanics instead of intended meaning.

## stage gates

| stage | durable input | output | done proof |
|---|---|---|---|
| Source | source files and brief | extracted requirements | reviewer can trace requirements to source |
| Spec | requirements and examples | human-readable artifact contract | fresh worker can explain intended result before building |
| Build | spec | generated source/components | targeted edit maps to a named spec section |
| Render/export | source plus helper command | visible artifact | artifact opens/renders outside the chat |
| Review | rendered artifact and spec | findings and accepted fixes | edits are recorded against spec sections |

## done test

A fresh file-capable worker should be able to change one named beat, section, scene, or component by reading the front desk and spec, without regenerating the whole artifact or replaying the original chat.
