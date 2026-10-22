# prompt workflow compiler map

Treat a reusable AI prompt as a small compiler pipeline, not as a clever chat
message. The prompt turns changing source material plus stable instructions into
a structured artifact that can be checked, retried, stored, and reused.

Use this shape when a language-model workflow repeats, but still needs judgment,
synthesis, translation, or source-sensitive adaptation.

## minimum components

1. **Fixed instruction.** The stable task, constraints, and non-goals.
2. **Variable source inputs.** Files, records, transcripts, forms, tables, or
   current readings that change per run.
3. **Role and context slot.** The operating point of view, audience, tone, and
   local assumptions that are allowed to vary.
4. **Output contract.** Schema, sections, filenames, fields, or downstream API
   shape.
5. **Execution envelope.** Model/provider class, context budget, temperature,
   tool access, and retry budget.
6. **Validation.** Parse checks, source-citation checks, diffs, tests, review
   gates, scorecards, or human acceptance thresholds.
7. **Error policy.** When to retry, narrow scope, ask for review, fall back to a
   simpler mechanism, or stop.
8. **Durable result.** Where the accepted output, source links, run notes, and
   verification receipt are stored.

## source boundaries

Keep changing source data outside the fixed instruction. The model may read the
source, cite it, and transform it, but source text should not be allowed to alter
system rules, tool authority, or publication criteria. Pair this architecture
with the context execution hierarchy and untrusted-content rules whenever source
material is copied from users, pages, repositories, tickets, messages, logs, or
other agents.

## when to escalate

Stay in ordinary chat for one-off thinking. Create a compiler map when the work
must be repeated, compared, delegated, audited, or parsed downstream. Move from a
map to scripts or a custom harness only when manual copying, schema validation,
large-batch execution, cost tracking, or retry handling becomes the bottleneck.

## review questions

- What stays fixed across runs?
- What varies, and where is it stored?
- What exact artifact must be produced?
- Which checks prove the artifact is usable?
- Which failures should stop instead of retrying?
- Where does accepted state live after the session ends?
- What simpler mechanism was rejected, and why?
