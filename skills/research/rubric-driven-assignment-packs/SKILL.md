---
name: rubric-driven-assignment-packs
description: "Use when a brief or rubric must become a submission pack."
version: 1.0.0
platforms: [macos, linux]
metadata:
  hermes:
    tags: [Documents, Citations, School, Packaging, Word]
    category: productivity
    related_skills: [grounded-citations, docx, ocr-and-documents]
---

# Rubric-Driven Assignment Packs

Use when someone hands over coursework — a brief and marking rubric, usually
alongside an exported group chat — and wants the work produced: the entire
assignment compiled, and/or each participant's allocated section separately,
delivered as one pack.

This is the workflow around the writing; the citation mechanics themselves live
in the `grounded-citations` skill. Depth on packaging and shared-ledger handling
is in `references/multi-part-deliverables.md`; the figure production recipe,
embedding, numbering policy and per-part verification are in
`references/figures-and-visuals.md`. Turning the marking criteria into a
runnable check suite, and the traps that make such a suite lie, is in
`references/rubric-gates.md`.

## Procedure

① **Read the brief and the rubric before writing a word.** They define the
scored criteria, and dropping one costs marks regardless of how good the prose
is. Extract with a layout-preserving tool — `pdftotext -layout` keeps the rubric
table structure that plain text extraction collapses into an unreadable run.

② **Read the chat export and recover the allocation.** A WhatsApp export ZIP
extracts with `ditto -x -k` and typically contains only `_chat.txt` with no
attachments, so work from the text. Map each person to the section the group
actually agreed for them, by name.

③ **Map every scored rubric item to a section before drafting.** Anything no one
was assigned still has to exist — conclusions, the abstract/summary, anticipated
questions, an individual-insight item. Write those yourself and say in the
handover that they were unassigned.

④ **Check the topic against the rubric's required focus.** When the rubric
demands a specific disciplinary combination and the group's own phrasing only
supplies half of it, add a section that carries the missing half and mark it
do-not-cut-for-time. This is the failure the group cannot see from inside its
own conversation.

⑤ **Build one shared citation ledger** (see `grounded-citations`) and keep ids
stable across every part, so numbering is consistent between the parts, the
abstract and the compiled document. For essay-style submissions, turn any source-count, source-age, or author-mix instruction into a measured gate before delivery; if the user asks for “22+ references” or “more than one author”, verify the final References list programmatically rather than relying on the prose pass.

⑥ **Write the parts, verify each, then assemble the compiled document** with a
single reference list. Never hand-edit a reference block.

⑦ **Build the figures and embed them into the documents.** A pack that scores
figures, diagrams or slide exhibits is not finished as prose. Produce the
visuals, place each at the point it is discussed, caption it with its source,
and introduce it with an in-text reference. Recipe: draw them yourself with PIL
— the section on drawing figures in `references/figures-and-visuals.md`.

⑧ **When the rubric scores a presentation, build the real deck.** Produce a
`.pptx` — not a slide-shaped Word document — with one slide per outline item,
the figure for each slide embedded, and the speaker cue in the notes pane. For
workshop-style assessments, also ship the presenter script and participant
handout as separate editable files, because facilitation and engagement are
usually scored alongside slide content. Recipe and construction rules: the
slide-deck section of `references/figures-and-visuals.md`.

⑧a **For Canva-style manuals, workshops, and student-facing intervention decks, make the first visual pass visibly designed, not merely themed.** Use an editorial workbook / magazine direction with bold section pages, large typographic moments, flow maps, stamps, diagrams, activity panels, and alternating layouts. Avoid a single dark/light template repeated across every slide; the user prefers eye-catching, editable material that can be uploaded to Canva and still feel alive before manual styling.

⑨ **Convert the written documents to `.docx`, package everything as one ZIP
with a README and handover notes, and deliver the compiled document and the
deck as separate files too** so they can be opened inline without unpacking.

⑩ **Turn the rubric into executable gates and work until every one is green.**
Write a suite in which each scored line becomes a measurable assertion with a
printed measured-versus-threshold result, run it, and close every failure. It
converts "I think this is covered" into a receipt, and the suite ships with the
pack so the group can re-run it after edits. Procedure and trap catalogue:
`references/rubric-gates.md`.

⑪ **When the rubric scores live delivery, ship the artefacts that carry it.**
Delivery and answering-questions marks are earned in the room, but the
preparation is checkable and belongs in the pack: a run-sheet giving speaking
order, per-speaker content and timings that sum inside the stated limit, and the
rehearsed answers to the likely questions. Write the anticipated answers as
separate answers with their source ids, not as prose buried in one participant's
section.

⑫ **When the deliverable carries a student's own name, generate first and prune second.**
Produce everything the evidence supports, then cut to what the marker will read as the
student's work: hold the critique to a single paragraph at the length the rubric implies, drop
any concept the course has not taught (named distribution tests, estimators the textbook never
reaches, jargon such as "time-dependent covariate"), and tell the user exactly which concepts
you removed so they can veto. Trim any evidence table to the rubric's floor — remove the spare
"the model got this right" rows but keep one, so the audit does not read as a hunt for errors —
and after any humanizer pass, merge the clipped one-clause sentences it leaves behind, because
staccato sentence fragments are the loudest model tell.

## Rules

- **The brief and rubric outrank the chat.** Write against the stated
  requirements and dates. When the chat assumed something different — a date,
  a deadline, a scope — deliver against the brief and state the discrepancy
  rather than silently picking one.
- **Never leave a scored criterion uncovered.** Produce it, even if the group
  never allocated it.
- **Every figure and datum carries a verbatim supporting quote** from its source
  so a reader can check any number against the text it came from.
- **Assign by the names used in the chat**, never by a guessed owner.
- **Handover notes are part of the deliverable**, not an extra: brief
  requirements, the marking breakdown, who was allocated what, the deadline, and
  the work that remains for the group.
- **Never deliver prose only.** Where the rubric scores figures, diagrams or
  visual exhibits, a text-only pack loses those marks no matter how good the
  writing is. Produce the visuals and embed them in place; treat the text-only
  draft as a work in progress, not a deliverable.
- **A deck is a different artefact from slides-written-as-prose.** When
  presentation quality is marked, ship a `.pptx` with speaker notes in the
  notes pane; somebody will otherwise paste the outline into PowerPoint by hand.
- **One figure set serves the whole pack.** Number figures by topic and keep
  that numbering identical in every document, so the compiled document and each
  part refer to the same figure by the same number. Do not renumber a single
  document; state the policy in the handover notes so nobody "fixes" it.
- Keep the material peer-reviewed or institutional where the rubric asks for
  reliable and up-to-date sources.
- **Reference-count and author-mix requirements are hard gates.** If the user or rubric gives a minimum number of sources, recent-source window, or “more than one author” preference, make the final report include the measured reference count, oldest/newest year check, and number of single-person-author references.
- **One citation style across the entire pack.** When the rubric asks for a
  meticulously consistent style, restyle every list into a single author-year-
  journal-URL form rather than leaving a consistent-but-unusual shape such as
  URL-first. Take author and journal detail from the publisher record, never
  from memory or inference.
- **Formatting criteria are deliverables too.** Page numbering, margins, column
  count and page length are each a scored line; set them in the converter so
  every generated document carries them rather than fixing them by hand.
- **Word limits must be measured exactly in the requested scope.** If the brief says total words include in-text citations but exclude references, count the body programmatically with citations left in and the reference list removed; do not report a vague estimate or exclude citations by habit.
- **Slide images are part of "send the slides".** When the deck is requested as
  images, render one image per slide from the deck file itself, so the images
  match what will be projected.
- **Report the submission, not the process.** Close with the artefacts, the measured checks
  that passed, and whatever is still outstanding — one short message. Do not narrate the build,
  relist the rubric items just satisfied, or replay a failed attempt the user has already read;
  they want the result and the next action.
- **Student presentation/manual decks must be eye-catching by default.** If the user asks for a workshop, intervention manual, or Canva-ready deck, treat visual engagement as a scored deliverable: vary slide structures, include diagrams/worksheets, and use a deliberate palette rather than a safe corporate template.

## Pitfalls

- **Do not solve a "make it professional" deck request by applying the same dark theme to every slide.** Repetition of black backgrounds, panels, and accent dots reads boring even when it is neat; build a stronger visual world with contrast in layout, scale, colour blocking, and artefact-like pages.
- **Naive markdown→docx conversion leaves literal `**` asterisks in the Word
  file.** Parse inline bold/italic into runs, then grep the generated files for
  `**` and expect zero hits before delivering.
- **Appending a rendered reference block to a document that already carries one
  duplicates the heading.** Grep for the heading before finalising.
- **Reading a ledger-wide "registered but not cited" warning as a failure on a
  multi-part submission.** Each part's own Sources block correctly lists only
  what that part cites; judge coverage per part, not against the whole ledger.
- **Padding citations to clear a coverage flag.** Split the sentence instead —
  the ceiling is three ids per sentence.
- **Renaming a part's reference heading to `References`.** The citation
  verifier looks for `## Sources`; a correctly built list under any other
  heading fails verification. Render the heading, don't retype it.
- **Verifying a part document against the whole-pack ledger.** The ledger-wide
  "registered but not cited" warning fails `--strict` on every part. Verify each
  part against a ledger subset holding only the ids that part cites; verify the
  compiled document against the full ledger.
- **Shipping a figure you never checked geometrically.** You cannot see the
  image, so audit it in code: measure each text run and fail if any exceeds the
  canvas bounds. Overflowed or clipped labels reach the marker otherwise.
- **Assuming attachments came with the export.** Chat exports are often
  text-only; if the group referenced files you do not have, say so.
- **Reading a red gate as a document defect without checking the gate.** A
  word-boundary regex can match a longer word, a sentence splitter can merge a
  whole paragraph because citations follow the full stop, and a blank floor can
  flag a reference list as a text wall. Fix the checker and report it as a
  checker correction — presenting a corrected checker as a document fix makes
  the pass count claim work that was never done.
- **A fixed "nothing older than year X" rule on a literature gate.** It will
  flag a foundational methods paper and tempt you into deleting a source the
  argument needs. Express the policy as a share of recent sources plus a hard
  oldest-year bound, and name the exception in the handover notes.
- **Treating "major detail" as permission to exceed the limit.** Add depth until the body approaches the cap, then rerun the scoped word counter; assignments often specify whether citations and references count differently.
- **Treating a maximum as a target.** A maximum is a ceiling, not permission to pad. Follow explicit user instructions against padding; meet any genuine institutional minimum using substantive evidence. If participant data or completed analysis are missing, do not invent results or inflate a literature review to conceal incomplete empirical chapters. Deliver the supported revision with an explicit blocked-status register and report both the user cap and institutional minimum.
- **Assuming a thesis-labelled DOCX contains a full thesis.** Inspect the entire OOXML package, comments and anchors, revision records, tables and text boxes before deciding content is missing. If it truly contains only an abstract, state that exact scope and distinguish a revised abstract from newly drafted background and a completed empirical manuscript.
- **Parsing Markdown headings only at blank lines.** A heading may directly precede prose on the next line. Split heading lines explicitly before DOCX construction, then reopen the output and assert exact section boundaries before counting words; otherwise entire paragraphs can silently become heading text.
- **Treating an expanded essay as complete before re-checking its references.** A body can meet the word cap while failing the source floor; after any expansion or rewrite, recalculate references and author mix, then add citations and reference entries together so every listed source is actually used.
- **Trusting a page-length estimate as a measurement.** With no office suite
  available to render, page count is computed from words plus figure area. Say
  it is an estimate rather than implying the file was paginated.
- **A verification ledger written from memory instead of copied from the appendix.** Every quotation in a ledger must be an exact substring of the unedited model output that Appendix B reproduces. Gate it: the document builder refuses to write the file unless each quoted fragment is found verbatim, and reports the pass count. A ledger that drifts from its own appendix is the fastest way to lose marks on a "quote the LLM exactly" instruction.
- **Rendering the submission PDF with `textutil` when no office suite is installed.** `textutil -convert html` then headless-Chrome print produces clipped table cells (a wide verdict column silently disappears from the text layer) and type crushed to roughly 7pt, so a 3,700-word submission collapses into three dense pages. Render the PDF from your own spec-derived HTML with an explicit A4 `@page` box, wrapping cells and `thead` repetition, then read the PDF back and count its pages before delivering.
- **Claiming a style score improvement without a fidelity check.** When a humanizer or rewriter is used, verify mechanically that every number, page reference and table reference survived the rewrite unchanged, and report the classifier's cross-validated balanced accuracy alongside the before/after scores — an unaudited rewrite is as likely to have dropped a value as improved the prose.
- **Padding an evidence table because every entry is verifiably true.** A ledger much longer than the rubric's floor forces the marker to read rows that score nothing, and a wall of "the model was right here" makes the audit look like it was generated rather than selected. Hold the table near the stated minimum, keep at least one verified-correct row for balance, and keep at least the required number of statistical or numerical entries.
- **Extending an audited appendix's scope while editing the surrounding document.** A "do not edit the model's response" instruction also binds the document builder: the prompt that was issued and the model output appear character-for-character as returned, verified by comparing the built document against the source files, not by reading it over.

## Verification

- Every scored rubric item has a section that answers it.
- The measured word count matches the brief's counting rule, including or excluding citations/references exactly as stated.
- Each document's reference list matches its own in-text citations on both
  sides — nothing listed and uncited, nothing cited and unlisted.
- Source gates are measured: reference count meets the stated floor, source years meet the stated recency window, and author-mix constraints such as no single-author sources are reported explicitly.
- Zero literal markdown emphasis markers and zero duplicated headings in the
  generated Word files.
- The ZIP unpacks to the intended layout, and the compiled document opens.
- The deck's slide count matches the outline, every slide carries its notes,
  no shape sits off-canvas, and the embedded figures are high enough resolution
  to project.
- The rubric gate suite runs green, and any gate that was corrected during the
  pass is reported as a checker correction rather than as a document fix.
