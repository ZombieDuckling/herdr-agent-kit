---
name: long-form-research-reports
description: Use when writing a cited multi-section research report.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos, linux]
metadata:
  hermes:
    tags: [research, reports, citations, pdf, rendering]
    category: research
    related_skills: [grounded-citations, deep-research, pdf]
---

# Long-Form Research Reports

Producing a deliverable research document (a deep-dive report, comparison study,
literature synthesis) that carries numbered citations, a full bibliography and a
rendered PDF. This skill owns the *artifact production* pipeline: source
ordering, section drafting, marker verification, rendering and delivery checks.
For the citation mechanics themselves (`sources.py`, evidence quotes) follow the
bundled `grounded-citations` skill; for retrieval fan-out, any research skill
may be loaded first.

## When to Use

- The user asks for "a deep research session", a report, a study, or a written
  synthesis rather than a chat answer.
- The deliverable is a document (markdown/HTML/PDF) grounded in outside sources.
- A topic needs 20+ sources and structured findings, not a bullet list.

Skip it for chat answers and one-paragraph summaries — cite those inline and stop.

## Procedure

1. **Scope first, retrieval second.** Write the research question and the
explicit exclusions before searching, and keep a running gap list: every search
round should target a *named* gap (a technology class, an accuracy figure, a
failure mode), not a rephrasing of the last one. Two or three rounds is normal;
stop when new sources stop changing a finding.
2. **Register sources in bibliography order.** Decide the citation order you
intend to use (grouping by theme reads best), then add the URLs to the ledger in
that exact order so ledger ids equal bibliography ids. Registering as URLs
arrive and renumbering later costs a whole extra pass.
3. **Draft to part files, not one document.** Write `partA.md`, `partB.md`, …
(section per finding or per group), then concatenate once into `report.md`.
Smaller writes survive tool timeouts and let you append more sources without
re-emitting the whole document. Word budget for a deep report: executive
summary and introduction short, findings substantial, synthesis/limitations/
recommendations proportional to the findings, bibliography and a methodology
appendix at the end. See `templates/report-skeleton.md`.
4. **Cite as you draft, with the URL inside the marker.** `[[7]](url)` keeps the
claim self-identifying even if numbering later drifts.
5. **Verify the markers mechanically before rendering.** Re-read the assembled
report and check, in code: every cited URL is in the ledger, no marker's number
disagrees with the ledger id for its URL, and the bibliography lists every
ledger id. If numbers drifted (sources registered out of order), rewrite them by
matching the URL inside the citation link to the ledger id for that URL —
anchoring on URL identity is safe on prose already written; anchoring on the
number is not, because numbers get reused across sections.
6. **Render, then inspect the artifact.** Markdown → HTML via `pandoc -f
markdown -t html5 --wrap=none` with a custom stylesheet, HTML → PDF via
`weasyprint`. Then read the PDF back: page count, extractable text length, and a
search for a few section names and a distinctive number from the body. A PDF
that renders but extracts no text, or that is missing its bibliography, is not
delivered.
7. **Deliver the artifact, not a description of it.** Attach the PDF with a
`MEDIA:` path plus a short, skimmable summary of what the findings actually are;
name the markdown source path so the user can edit it.

## Rendering specifics

- `pandoc`, `weasyprint` and Chrome's headless `--print-to-pdf` are the working
  routes on this machine; pandoc+weasyprint is the first choice because the
  stylesheet controls page margins, page numbers and block quotes.
- Strip YAML front matter into your own HTML header block; do not rely on
  pandoc's default template for the title.
- Stylesheet: solid surfaces, 1px hairline rules above section headings, system
  sans-serif body, no gradients, no rounded cards, no emoji — match the user's
  anti-slop house style. One CSS file reused across reports.

## Pitfalls

- **Registering sources as they arrive and drafting later.** The ledger order is
  the bibliography order; retrieving first and drafting second forces the
  URL-anchored renumbering pass in step 5.
- **Presenting borrowed numbers as measured facts.** Accuracy figures lifted
  from other people's rigs apply to *those* rigs. State which claims are the
  report's own worked estimates, and put that disclosure in the Limitations
  section, not in a footnote. A report that implies its error budget was
  measured when it was calculated will be trusted too far.
- **Fabricating a literature-wide consensus.** Practitioner documentation and
  vendor pages are not peer-reviewed evidence. Label the source mix and prefer
  the primary study when one exists; where sources disagree, say so instead of
  averaging.
- **Writing findings as narration of what you did.** A finding is a
  generalizable claim with its evidence attached, not a chronology. Keep dates,
  ticket ids and incident stories out of them.
- **Attaching a huge markdown in chat.** Send the PDF as the artifact; paste
  only the handful of findings that change the user's next action.
- **Claiming completion from a successful render command.** Verify by reading
  the produced file back (step 6).

## Verification

Before delivering, confirm all of: report.md assembled and citation-verified;
PDF exists, opens, has the expected page count, and yields extractable text
containing the bibliography, limitations and methodology sections; summary
message names the source path and states what is still unverified (e.g. a
measurement pass the report recommends but has not run).
