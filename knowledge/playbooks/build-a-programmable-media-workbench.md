# build a programmable media workbench

Use this playbook when a creative artifact is repeatable enough to deserve source,
preview, render, and provenance files instead of a single opaque export.

## output

A folder that follows `architecture/programmable-media-pipeline.md` and completes
`templates/media-artifact-registry.md` for every reviewed output.

## procedure

1. **Write the brief.** Name audience, message, target format, length, style
   constraints, forbidden claims, allowed-use boundary, and acceptance reviewer.
2. **Inventory source assets.** List original files, references, prompts, generated
   takes, licenses or permissions, attribution needs, and any unknown provenance.
3. **Choose the source form.** Decide whether the durable source is a script,
   storyboard, scene spec, component tree, caption file, prompt chain, or mixed
   package. Do not let the hosted session be the only copy.
4. **Create one reviewable unit.** Build one scene, slide, shot, or component and
   render a preview before scaling the whole artifact.
5. **Separate generation from finishing.** Use generative tools for ideation,
   takes, backgrounds, drafts, or components; use deterministic steps for text,
   captions, crops, sequencing, checksums, and final export whenever practical.
6. **Record provenance while it is fresh.** Capture model/tool names where
   available, prompts/specs, source assets, edits, rejected takes, and render
   commands before the UI history disappears.
7. **Review by lanes.** Evaluate visible quality, source provenance,
   transformation/originality, consent/licensing, and deployment context
   separately. A blind quality test does not approve the other lanes.
8. **Bind the final artifact.** Record final path, revision or checksum, render
   command, reviewer, status, and unresolved limitations.
9. **Export the workbench.** Preserve source files and review notes beside the
   rendered artifact so another file-capable runtime or human editor can continue.

## acceptance gate

Ship the artifact only when:

- the final render opens and matches the target format;
- the source/spec needed to rebuild or revise it is present;
- every non-original asset has an allowed-use status or is removed;
- generated and human-edited portions are distinguishable enough for review;
- visible-quality approval and provenance/usage approval are both recorded; and
- limitations from missing visual/audio/source context are explicit.