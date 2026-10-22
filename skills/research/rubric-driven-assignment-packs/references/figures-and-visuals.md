# Figures and visuals for assignment packs

Why this file exists: rubrics that score presentation quality mark figures,
diagrams and visual exhibits. A pack of good prose with no visuals loses those
marks, and the loss is invisible from inside the text.

## Decide the set from the rubric's own scored items

One figure per argument the section actually makes — burden and projection
charts, mechanism diagrams (the molecular basis), engineering chain diagrams
(recognition element to digital output), pipeline diagrams, pooled-accuracy
panels, cost panels, access and adoption panels. A pack of ~10-14 is normal.
Each figure carries the datum its section argues from, and its caption carries
the source id.

The compiled document carries the whole set; each part document carries only the
figures belonging to that part, plus the slides document carrying the figure for
each slide it outlines, so the deck can be built by dropping them in.

## Drawing figures when no charting library is available

Do not depend on matplotlib being installed, and do not rasterise hand-written
SVG through ImageMagick — without a font configuration ImageMagick fails on
text ("unable to read font") and the labels vanish. Draw directly with PIL,
which is present in the standard environment and loads system fonts by path:

```python
from PIL import Image, ImageDraw, ImageFont
REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
SS = 2  # draw at 2x, then downscale with LANCZOS for clean edges
```

Build a small canvas class with `rect`, `text`, `line` and `arrow` helpers that
multiply every coordinate by `SS`, cache `ImageFont.truetype` per (weight, size),
and keep the 2x supersample in the saved file — `img.resize((w * 2, h * 2),
Image.LANCZOS)`, not a downscale to `(w, h)`. These files are projected and
printed: a downscaled export lands near 110 dpi across a full slide and looks
soft on a projector. Keep a single generator script in the pack so the figures
can be regenerated after a late edit.

House style: flat solid fills, no gradients, no rounded cards, heavy blocky
type, black and white plus one accent colour, no emoji, no decorative pills.
Size text for projection distance — the same files serve as slides.

## The geometric audit is mandatory

You cannot see the rendered image, so verify it in code. Inside the `text`
helper, measure the run and record any whose left or right edge leaves the
canvas or whose baseline passes the bottom:

```python
wpx = draw.textlength(s, font=f) / SS
if x0 < 0 or x0 + wpx > self.w or y > self.h - 2:
    OVERFLOW.append((self.name, s[:60], x0, x0 + wpx, y))
```

Print the collected list at the end and require it empty before shipping.
Overflowed or clipped labels are the defect you cannot catch by reading code.

## Embedding into the Word documents

- Mark each figure position in the markdown with an image marker such as
  `![Figure 3. caption](figures/fig03-....png)` and support that marker in the
  converter: a centred picture plus a bold caption paragraph beneath it.
- Resolve image paths relative to the document's own directory, with a fallback
  to the parent directory — the part documents sit in a subdirectory while the
  figures sit at the pack root, and a converter without that fallback aborts on
  the first part.
- Put a one-sentence in-text introduction naming the figure immediately above
  it (`Figure 3 quantifies the problem this argument rests on.`) so the figure
  is cited in the text. Both the rubric and the citation verifier expect it.
- After building, count images per document to confirm every planned placement
  landed (`word/media/` entries in the `.docx` zip), and grep the extracted
  paragraph text for `**[` leakage and for `## Sources` rendering as
  `References`.

Keep any single markdown line at three ids or fewer. The citation checker
splits only on punctuation followed by whitespace, so ids placed after a period
are not split points and a paragraph written as one long line accumulates ids
and trips the ceiling. Give the sentence its own line, or drop the least
necessary attribution — do not reorder to hide it.

## Building the slide deck

The deck is a separate deliverable from the slides-outline document, and the
rubric that scores slide quality is the reason to produce it. Build it with
`python-pptx` without touching the global environment:

```bash
uv run --with python-pptx --with pillow python build_slides.py
```

`uv run --with` provisions an ephemeral environment, so a package the system
Python does not have is never a reason to skip the deck or to install globally.

Construction rules, all of them driven by the rubric text:

- 16:9 at 13.333 x 7.5 in, blank layout, one slide per outline item in outline
  order, and the same title wording as the outline.
- Use a professional high-contrast theme rather than a default academic deck:
  black or near-black ground, white main text, and one or two restrained accent
  colours such as turquoise and lavender. Keep accent stripes, dots, panels and
  rules consistent; do not add gradients, animations, emoji, or decorative
  clutter.
- Fit each figure inside the body area by aspect ratio, never by fixed size —
  `add_picture` with one dimension only rescales the source, but computing both
  from the image's own aspect and centring it avoids distortion and overflow.
- Every slide gets notes: the speaking cue, written as a cue rather than a
  script, because rubrics commonly penalise reading from notes. When the brief
  asks for a timed workshop, also generate a separate full presenter script
  with a timing guide and a participant handout for the interactive activity.
- Text-only slides are the right answer for guideline, limitation and
  conclusion items — a handful of short lines, never a paragraph.
- The references slide is generated from the same ledger, split into two
  columns, one entry per source with its URL.

Verify before delivering, since none of this is visible by inspection: slide
count against the outline, notes present on every slide, no shape starting
before the origin or extending past the slide bounds, required terms present in
the slide XML, ZIP integrity passes, and the pixel size of each embedded image
(`ppt/media/` entries) is large enough to project.

## Numbering policy

Number figures by topic and hold that numbering fixed across every document in
the pack, so the compiled document and each part refer to the same figure by the
same number. A compiled document whose sections run in author order will not
have ascending figure numbers; say so in the handover notes so nobody renumbers
a single document. Per-document renumbering gives two conflicting systems for
the same figure — pick one policy and state it.

## Verifying each part standalone

`verify --strict` fails a part whose ledger also holds sources other parts cite
(the ledger-wide "registered but not cited" warning). Prove each part is
internally consistent by verifying it against a ledger subset of just the ids it
cites, then verify the compiled document against the full ledger:

```python
import json, re
body = open(doc).read().split("## Sources")[0]
ids = sorted({int(m) for m in re.findall(r"\[(\d+)\]", body)})
subset = dict(ledger); subset["sources"] = [by_id[i] for i in ids if i in by_id]
```

Re-render each part's list with `render --cited-in <part>` after any edit so the
list matches the body exactly; the verifier requires the heading `## Sources`,
so do not rename it to `References` in the markdown (the converter can still
display it as "References").
