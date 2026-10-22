# spec-component-preview pipeline

Use this shape when AI is generating media, presentations, pages, UI components,
reports, or code-backed visual artifacts that humans will need to edit later.
The goal is to keep the intended meaning, reusable components, generated source,
rendered output, and review notes in separate positions.

## folder shape

```text
artifact-workbench/
  README.md                 # front desk: purpose, stages, entry points
  source/                   # script, brief, transcript, requirements, assets
  spec/
    artifact-spec.md        # human-readable contract
    beat-map.md             # sequence, timing, meaning, transitions
    style-guide.md          # voice, visual language, examples, anti-examples
    acceptance.md           # editability and review criteria
  components/
    registry.md             # reusable blocks, inputs, constraints, failures
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
4. timing, pacing, or ordering constraints when timing matters;
5. visual, interaction, or tone philosophy;
6. examples and anti-examples;
7. meaning each section must convey;
8. named assets or evidence that must be used;
9. acceptance tests and review surface;
10. what the model may improvise;
11. what the model must not change without approval.

Do not start by locking pixels, frame numbers, component props, file names, or
implementation details unless they are part of the contract. Overconstraining the
first pass often reduces quality and makes the model optimize local mechanics
instead of intended meaning.

## component registry fields

Each reusable component should record:

- name;
- purpose;
- accepted inputs;
- output or render shape;
- constraints;
- examples;
- known failure modes;
- last review result.

Treat reusable components as context capital. If the model repeatedly makes the
same mistake, update the style guide, registry, or acceptance example rather than
burying the correction in chat.

## stage gates

| stage | durable input | output | done proof |
|---|---|---|---|
| Source | source files and brief | extracted requirements | reviewer can trace requirements to source |
| Spec | requirements, examples, constraints | human-readable artifact contract | fresh worker can explain intended result before building |
| Component selection | spec and registry | chosen components or new-component request | worker prefers known parts over fresh invention |
| Build | spec and selected components | generated source/components | targeted edit maps to a named spec section or component |
| Render/export | source plus helper command | visible artifact | artifact opens/renders outside the chat |
| Review | rendered artifact and spec | findings and accepted fixes | edits are recorded against spec sections or components |
| Finish | accepted review findings | final artifact | human taste, timing, risk, and distribution choices are explicit |

## done test

A fresh file-capable worker should be able to change one named beat, section,
scene, or component by reading the front desk, spec, style guide, and registry,
without regenerating the whole artifact or replaying the original chat.
