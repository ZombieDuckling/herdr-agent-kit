# asset-to-workbench package

A hosted AI tool can be useful for interpreting assets, but the durable product is
an exportable workbench: source assets, a map, routed instructions, examples,
components, review rules, and generated outputs that another capable file-reading
runtime can reuse.

## shape

```text
workbench/
  README.md              # front desk and entry points
  AGENTS.md              # model/operator routing rules
  manifest.md            # source map and artifact catalog
  assets/                # original or referenced source assets
  brief.md               # audience, job, constraints, non-goals, acceptance proof
  spec.md                # executable translation of the brief into requirements
  stages/                # scene, slide, page, report, or component work units
  components/            # reusable code, design pieces, snippets, or blocks
  examples/
    good/                # approved outputs and why they work
    bad/                 # anti-patterns and why they fail
  instructions/          # task-specific procedures and style rules
  scripts/               # deterministic render, conversion, or validation helpers
  outputs/               # generated artifacts for review/export
```

## rules

1. Preserve source assets separately from derived summaries and generated files.
2. Spend model credits once to create the source map, not on every future task.
3. Encode taste and constraints as examples, anti-examples, and non-negotiables.
4. Split creative or business outputs into brief, spec, stages, source assets,
   and review rules before generating the finished artifact.
5. Keep vendor-specific affordances replaceable by plain-file instructions and
   deterministic helpers when practical.
6. Route expensive models to extraction, synthesis, and review; route cheaper
   workers to routine generation only after the package is clear.
7. Export the package before considering the hosted tool's UI to be the system of
   record.

## done test

A fresh runtime that can read files should be able to:

- orient from the front desk;
- locate the right assets from the manifest;
- follow one task instruction without scanning the whole folder;
- regenerate a single stage without re-explaining the whole artifact;
- reuse examples and components;
- produce an output in the review surface;
- cite or link the source material it depended on.
