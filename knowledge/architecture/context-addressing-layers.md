# context addressing layers

A workbench can remember by where a fact lives, what it links to, or what its
content resembles. Choose the cheapest address mode that lets the next operator
find the right context with evidence.

## address modes

| mode | primary handle | use when | failure mode |
|---|---|---|---|
| Position-addressed | folder, filename, stage, local router, template | the workflow has known stages, artifacts, and human editing paths | flat dumps, ambiguous paths, or giant catch-all instruction files |
| Link-addressed | explicit index, wiki page, graph edge, source citation | maintained entities, decisions, and relationships are the main navigation problem | stale links, orphan notes, or uncited prose summaries |
| Content-addressed | search index, embedding, keyword, metadata surrogate | discovery across large or messy corpora matters more than a stable path | plausible but irrelevant matches, lost provenance, or expensive full-source scans |

Most shipping systems are hybrid, but they should not start hybrid by default.
Build the position layer first when the job is a repeated workflow with visible
outputs. Add links when curated relationships become valuable. Add semantic
search when the corpus is too large or irregular for routing files to cover.

## position-addressed workbench shape

A position-addressed memory layer needs:

1. **Front desk.** The root orientation file names the purpose, canonical entry
   points, mutable areas, protected areas, and current status.
2. **Canonical manifest.** Work items, source handles, derived notes, artifacts,
   and processing state live in a table or machine-readable manifest.
3. **Cascading context.** Root instructions explain global rules; subfolders hold
   stage-, role-, or deliverable-specific routing tables that name read-first
   files, protected paths, outputs, and checks.
4. **Templates.** Repeated artifacts start from named forms rather than from a
   chat memory.
5. **Source/derived separation.** Raw inputs, derived notes, decisions, outputs,
   scripts, and integration secrets occupy different layers.
6. **Review surface.** Diffs, registries, checklists, and acceptance records make
   the work inspectable without replaying the session.

## escalation rule

Before adding a vector store, autonomous memory agent, or wiki system, answer:

- What repeated workflow cannot be continued from the current folder structure?
- Which context is invisible from path, manifest, and local routing alone?
- What freshness/provenance guarantee will the new memory layer provide?
- How will a reviewer trace a retrieved answer back to its source?
- What cost, latency, and maintenance burden does the layer add?

If those answers are weak, improve the front desk, manifest, filenames,
templates, and local routing first.

## related laws

- [WB-1](../notes/08-workbench-architecture.md#wb-1-a-front-desk-is-part-of-the-product)
- [WB-6](../notes/08-workbench-architecture.md#wb-6-chat-is-not-durable-state)
- [WB-9](../notes/08-workbench-architecture.md#wb-9-build-context-layers-around-workflows-not-around-everything)
- [WB-13](../notes/08-workbench-architecture.md#wb-13-route-context-in-three-layers-before-building-agents)
- [CORP-1](../notes/09-corpus-and-review.md#corp-1-the-surrogate-is-a-map-not-the-territory)
- [MECH-2](../notes/10-mechanism-selection.md#mech-2-deterministic-work-does-not-need-an-agent)
