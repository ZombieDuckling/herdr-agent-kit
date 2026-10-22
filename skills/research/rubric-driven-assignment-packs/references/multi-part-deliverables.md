# Multi-part deliverables from one ledger

For submissions that arrive as "do the whole thing, and separately do each
person's part": one ledger, several drafts, one compiled document, packaged as
a single deliverable.

## Keep one ledger and stable ids

Do not reset between parts. One ledger across every part means the numbering is
consistent in the individual sections, the abstract, and the compiled document —
which is exactly what a rubric scoring referencing consistency checks for.
Register sources once at retrieval; `add` is idempotent, so a URL fetched while
researching part 3 returns the same id later.

## Render per part, not per ledger

Each per-part draft gets its own Sources block via
`sources.py render --cited-in <part>` so it lists only what that part cites. The
compiled document is assembled from the parts and gets a single Sources block
rendered from the union of their citations. Never hand-edit either block.

`verify` on a single part flags the sources cited by other parts as "registered
but not cited" and exits non-zero. That is expected, not a defect — read the
`info: stats:` line for that part's own coverage instead. Do not pad citations
to clear the flag; split the offending sentence.

## Package layout

Keep the internal structure obvious to someone who did not watch you build it:

```
<Assignment name>/
  README.md                     what the pack contains
  HANDOVER-NOTES.md             rubric breakdown, allocation, deadlines
  00-COMPILED-FULL-ASSIGNMENT.md
  Separate sections (markdown)/
  Submission ready (Word)/      the .docx files
  source evidence quotes/       extracted text behind each quotation
  ledger.json
```

Zip with `ditto -c -k --keepParent <dir> <name>.zip` on macOS.

## Convert with inline emphasis handled

A docx converter must parse `**bold**` and `*italic*` into runs. Verify by
extracting the generated file's paragraphs and counting any that still contain
`**` — expect zero. Do this for every generated document, not just the compiled
one.

## Flag discrepancies, do not silently resolve them

When the brief's dates disagree with what the group chat assumed, deliver
against the brief and say plainly that the discrepancy exists and should be
confirmed — do not pick one and stay quiet.
