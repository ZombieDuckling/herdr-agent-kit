# workflow context layer architecture

A workflow context layer is a small workspace built around one valuable operation.
It is not a universal second brain. Its job is to make the next operator or agent
able to continue the workflow without rereading the entire source archive.

## minimum shape

```text
workflow/
  README.md          # front desk: purpose, status, entry points, rules
  manifest.md        # source, derived, output, and decision inventory
  sources/           # raw or source-linked inputs; not the default read path
  derived/           # briefs, summaries, conclusions, packages, indexes
  instructions/      # repeatable procedures and skill-like runbooks
  outputs/           # produced artifacts and review surfaces
  decisions.md       # durable choices and rationale
  questions.md       # unresolved request slips and open issues
  tools.md           # tool contracts or links to a tool registry
```

Keep secrets, credentials, protected records, and provider access outside the
editable/exportable tree. The workspace may point to an integration, but it must
not contain the secret that powers it.

## build order

1. Name the workflow and the outcome it improves.
2. Inventory source material without rewriting it.
3. Extract derived signal that future runs should read first.
4. Write instructions for repeated operation.
5. Record decisions, open questions, outputs, and verification paths.
6. Add access and export boundaries before sharing the layer.
7. Test with a fresh session.

## local-first rule

Start local and narrow unless sharing is required. A personal workflow layer is
often faster and safer than a prematurely centralized workspace. Move to a shared
workbench only after the layer has proved value and has explicit permissions,
handoff rules, and export boundaries.

## anti-patterns

- dumping every note into one archive and expecting retrieval to create order;
- asking the model to rediscover signal from raw source every run;
- creating graph views where no operational dependency uses the graph;
- mixing raw source, derived conclusions, mutable outputs, and secrets;
- scaling to a team before the single-operator workflow is understandable.