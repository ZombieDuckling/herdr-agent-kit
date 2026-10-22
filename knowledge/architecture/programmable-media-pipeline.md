# programmable media pipeline

Use this shape when an image, animation, explainer, slide sequence, or short video
can be represented as source files plus a render step instead of only a hand-edited
binary artifact.

## shape

```text
media-workbench/
  README.md                 # front desk: purpose, audience, output formats
  brief.md                  # message, constraints, allowed-use boundaries
  manifest.md               # source assets, licenses, generated takes, final outputs
  assets/                   # original media and references
  scenes/                   # scene specs, captions, timing, scripts, storyboards
  components/               # reusable visual/audio/code components
  renders/                  # preview and final rendered outputs
  review/                   # blind-review notes, provenance checks, acceptance
  scripts/                  # deterministic build, render, caption, or export commands
```

## lanes

Keep these claims separate throughout the workbench:

1. **Perceptual quality:** what the viewer can see or hear.
2. **Source provenance:** which assets, prompts, models, references, or generated
   takes contributed to the output.
3. **Transformation:** what changed from source to final artifact.
4. **Allowed use:** licensing, consent, attribution, privacy, and commercial-use
   boundaries.
5. **Execution proof:** the build/render command, final revision, checksum, or
   exported file that produced the reviewed artifact.

A blind comparison can test perceptual claims, but it cannot settle provenance,
consent, originality, or allowed-use claims. Those require the other lanes.

## operating rules

- Treat the final render as an output, not the system of record.
- Preserve prompt/spec, source assets, generated takes, model/tool metadata where
  available, deterministic edit steps, and final review notes.
- Use code or structured scene specs for repeatable motion, captions, charts,
  overlays, product demos, and explainers.
- Keep one-unit preview loops short enough for human taste review before expanding
  the sequence.
- Record thin-source or visual-only items as low confidence unless screenshots,
  frames, or source files were reviewed.

## done test

A fresh operator can rebuild or review the artifact because the workbench contains
all of these:

- source asset list with allowed-use status;
- scene/spec/component source or prompt chain;
- render/export instructions;
- final artifact location and immutable identity;
- review notes that separate visible quality from provenance and usage claims;
- unresolved limitations or source gaps.