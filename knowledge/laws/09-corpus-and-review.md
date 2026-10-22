# 09 · corpus engineering and review

These laws cover large source collections, generated output, and the review debt
created when agents produce more than humans can inspect.

---

## CORP-1: the surrogate is a map, not the territory

**Law.** Captions, summaries, embeddings, and labels are navigation aids; the
source span remains the evidence.

A large corpus became searchable only after it was reduced to compact text. The
critical design choice was preserving source pointers so any finding could be
checked against the original.

- Detect: search results cannot jump back to source file, page, row, or time.
- Fix: every derived record carries a stable source pointer.
- Do not act on the surrogate without source review for high-value claims.

---

## CORP-2: compression ratio is an architecture decision

**Law.** Decide what the index keeps and what it discards before large-scale
extraction begins.

If every source is summarized differently, the index becomes a pile of prose. If
the schema is too thin, it cannot answer useful questions. Compression defines
what future agents can cheaply know.

- Detect: repeated searches require rereading raw sources.
- Fix: define fields for summary, themes, entities, problems, timestamps, and
  confidence before processing the corpus.
- Review the schema after a small batch, not after the whole archive.

---

## CORP-3: generated output must carry review handles

**Law.** A generated document, table, or code change must expose how to review it:
diff, tests, citations, screenshots, source rows, or validation output.

The bottleneck moved from writing to checking. Without review handles, generated
volume becomes debt.

- Detect: the artifact is large and polished, but the reviewer cannot tell what
  changed or what supports it.
- Fix: require a review handle as part of the output contract.
- If no review handle exists, reduce the scope.

---

## CORP-4: source tables beat prose summaries during discovery

**Law.** When the goal is research or inventory, build a table of source objects
before writing narrative conclusions.

A narrative summary hid duplicates, uncertainty, versions, and missing fields. A
source table made gaps visible and kept later writing grounded.

- Detect: the agent starts drafting before it can list the sources.
- Fix: source table first, prose second.
- Required columns: source pointer, type, status, key fields, and verification.

---

## CORP-5: preserve bad versions when the task is inventory

**Law.** In an inventory, superseded, messy, duplicated, and unclear artifacts are
still artifacts.

Filtering too early destroys exactly the evidence needed to reconstruct how work
happened. Relevance judgment belongs after inventory, not before.

- Detect: the scanner drops files because they look old or useless.
- Fix: list the artifact and mark status or uncertainty.
- Later curation can group versions without pretending they never existed.

---

## CORP-6: semantic catalogs are for repeated navigation, not decoration

**Law.** Add a semantic catalog when a corpus is large or repeatedly queried;
for small corpora, a manifest and derived index are enough.

A catalog around data, documents, or media helps agents choose the right source
without loading everything: descriptions, access rules, common questions, example
queries, refresh cadence, caveats, and links to related entries. The same pattern
becomes waste when it is installed before there are repeated questions or a large
source set.

- Detect: queries repeatedly scan raw files, or a new catalog has no real lookup
  path beyond pretty descriptions.
- Fix: catalog only the stable source objects that need repeated navigation, and
  include access rules, refresh cadence, common questions, examples, caveats, and
  source pointers.
- Verification: the next query can choose a source and know whether it is current
  without reading the raw corpus first.

---

## CORP-7: confidence is a field, not a vibe

**Law.** Every derived corpus item must carry its source coverage class; a
metadata-only record may orient a reader, but it cannot support source claims.

A batch mixed deep source-backed notes with tiny items whose underlying evidence
was unavailable. Counting all records as equally processed made progress look
better while increasing hallucination pressure. A separate coverage index made
the limitation visible: source-backed, metadata-only, retry-pending, or rejected.

- Detect: a manifest says `processed` but does not say whether the source was
  actually read, partially read, unavailable, or too thin to use.
- Fix: add a coverage/status field and a coverage index; label metadata-only
  notes in the note header and restrict them to claims present in metadata.
- Generalizes to: transcript ingestion, web research, PDF extraction, OCR,
  scraping, support logs, meeting notes, media catalogs, and benchmark datasets.
## CORP-8: dated claims need outcome reviews

**Law.** Predictions, strategy claims, and tool advice become knowledge only when
they are revisited with what held, what failed, what changed, and what rule now
replaces them.

Fast-moving AI archives can turn into mythology: old correct calls are repeated
without nuance, old wrong calls vanish, and tool-specific advice keeps its
authority after the toolchain changes. A lightweight claim ledger keeps the
archive honest by preserving the original claim and adding a later outcome
review instead of rewriting history.

- Detect: a strategy cites old material as proof but cannot name the original
  date, outcome, changed conditions, or surviving principle.
- Fix: record dated claims with source pointer, expected outcome, review date,
  held/failed/nuanced verdict, replacement rule, and future watchpoint.
- Verification: new guidance links to the reviewed claim or explicitly marks it
  as unreviewed, stale, or superseded.
## CORP-9: analysis is not grounded until the data semantics are grounded

**Law.** AI-assisted tables, charts, rankings, and summaries require a data
dictionary, provenance, transformation log, and interpretation caveats before
their conclusions are reusable.

Generated analysis can look rigorous while the model has only guessed what a
field means, silently mixed raw and derived values, or skipped the sampling limits
that make a conclusion unsafe. The review target is not whether the chart renders;
it is whether a competent reviewer can explain what the inputs mean, how they
changed, and which claims the data can actually support.

- Detect: an analysis artifact has polished visuals or prose but no field
  definitions, source inventory, transformation steps, or caveats.
- Fix: build a source-understood workbench: raw inputs, data dictionary,
  transformation log, analysis contract, interpretation notes, and review packet.
- Generalizes to: research datasets, analytics notebooks, survey exports,
  benchmark tables, generated reports, and decision-support dashboards.
## CORP-10: source readiness is part of generation

**Law.** A model cannot reliably build from a folder until the authoritative
sources, stale material, terms, constraints, and review handles are made explicit.

Messy source folders caused the model to spend effort rediscovering which files
mattered, which facts were current, and what human judgment should constrain the
output. Cleaning the source map before generation made the same model more useful
without changing the model at all.

- Detect: the request says "use this folder" but does not say which files are
  authoritative, stale, background-only, or forbidden.
- Fix: add a source-readiness pass: source map, current/stale labels, short
  definitions, alignment notes, and required citations/diffs/tests/previews.
- Generalizes to: decks, reports, code generation, brand work, data analysis,
  research synthesis, and any workbench where source material is the product's
  context.
## CORP-11: separate durable principles from volatile tactics

**Law.** Before promoting old guidance into shared memory, classify it as a
durable primitive, a current tactic, a market observation, or an unsupported
source-limited claim.

Fast-moving AI notes rot when every useful sentence is treated as equally
timeless. A folder, routing, review, state, governance, or human-judgment pattern
may survive model churn, while the named tool, price, interface, or market claim
around it may already be stale. Reviewing the layer first keeps good primitives
without preserving old confidence.

- Detect: a note cites old advice, a model/tool behavior, a pricing claim, or a
  thin source as if it were a general law.
- Fix: extract the transferable primitive; keep dated tactics and market claims
  in a ledger with source date, changed assumptions, current action, and next
  review trigger.
- Do not promote source-limited or identity-dependent material; record the
  omission instead of laundering it into generic prose.
