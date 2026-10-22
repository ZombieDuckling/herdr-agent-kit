# Rubric gates: turning marking criteria into a check suite

Why this file exists: a rubric read once is a checklist you drift away from. A
rubric written as executable checks is a gate you can prove you passed, and the
suite can ship with the pack so a later edit is re-verified instead of trusted.

Write and run the suite after the pack exists, then close every failure. Report
the pass count as `passed/total` with exit status, and keep the suite in the
deliverable.

## Shape of a gate

Each scored rubric line becomes one assertion that prints
`PASS|FAIL [rubric section] check — measured value vs threshold`. Failing gates
must print enough to fix them without re-reading the whole document: the
measured number, the threshold, and the offending snippet.

Gate families that map to typical rubric sections:

- **Discussion** — presence of each required conceptual heading; count of
distinct domain concepts the topic demands; in-text citation volume; that the
integration section actually links sources rather than only carrying a heading
(count ids inside its body); that the conclusions and individual-insight items
exist.
- **Presentation quality** — slide count against the outline; per-slide word
budget; minimum font size per slide class; figure count; speaker-note length;
absence of transition/animation elements in the slide XML; figure-label size
from a generator audit; no figure reused twice in the compiled document.
- **Delivery** — a run-sheet exists, its stated minutes sum to no more than the
time limit, every presenter is named with an allocated slot, and cue-only
delivery is stated.
- **Answering questions** — count of prepared questions, count of source ids
inside their answers, and that the deck's notes point the presenter at them.
- **Abstract** — title length and informativeness, count of informative
headings, page-length estimate, page-number field present, column count, margin
widths.
- **Referencing** — a style regex applied to every listed entry, per-document
citation-to-list correspondence, and the currency policy.
- **Writing** — mechanical scans: doubled words, double spaces, space before
punctuation, mixed spelling against the chosen variant with a proper-noun
allowlist.

## A red gate is not automatically a document defect

Check the checker first. These are the traps that produce false failures:

- **Word-boundary regexes.** `\bcolor\b` is safe; `\bcolor\w*` also matches
  "colorectal". Anchor both ends, and keep a proper-noun allowlist (organisation
  and guideline names) instead of loosening the rule.
- **Sentence splitting.** A splitter that breaks on punctuation followed by
  whitespace merges an entire paragraph into one "sentence" when citations
  follow the full stop. Strip headings, bullets, table rows and citation markers
  before measuring, or you will chase long sentences that do not exist.
- **Minimal-text budgets.** Exempt the reference slide — a reference list is
  dense by necessity, and a few hundred words there is not a slide-quality
  failure.
- **Font-size floors.** Attribution lines and reference lists legitimately sit
  below body size. Set a floor per slide class rather than one global minimum.
- **Currency gates.** A fixed "nothing older than year X" rule flags the
  foundational methods reference the argument depends on. Express it as a share
  of recent sources plus a hard oldest-year bound, and name the exception.
- **Heading presence by prefix.** A heading repeated across parts matches the
  first occurrence; check the intended section, not whichever comes first.
- **Style regexes and author strings.** Author fields legitimately contain
  periods ("et al."), so a style pattern must not forbid them.

## Correct the gate, then say so

When a check is wrong, fix the checker and report it as a checker correction:
the work was already sound, and folding it into the list of document fixes
claims credit for something that was never broken. Keep the two categories
separate in the final report — documents changed, and checkers changed.

## Formatting gates are code, not manual steps

Abstract formatting criteria (page numbering, margins, column count) are
checkable and belong in the converter so every generated document carries them:

```python
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def add_page_numbers(doc):
    for section in doc.sections:
        para = section.footer.paragraphs[0]
        fld = OxmlElement("w:fldSimple")
        fld.set(qn("w:instr"), " PAGE ")
        run = OxmlElement("w:r")
        text = OxmlElement("w:t")
        text.text = "1"
        run.append(text)
        fld.append(run)
        para._p.append(fld)
```

Set one-inch margins on every section at build time. Verify by reading the
`.docx` zip: the footer XML must contain `PAGE`, and the document XML must carry
`w:cols` and the margin values.

Page length is estimated from words per page plus the area the figures occupy,
because there is often no office suite on the machine to paginate the file. Say
so when reporting: an estimate is not a measurement.

## Honest reporting of the outcome

State the baseline and the final count, separate document fixes from checker
fixes, and list the judgement calls that remain (a labelled schematic, a
foundational older reference, a deliberately exempted reference slide). A green
suite is not a claim that nothing is imperfect — it is a claim that every rule
the rubric states was checked.
