# Static portfolio smoke validation

Use this pattern during autonomous portfolio maintenance for small GitHub Pages / standalone HTML portfolio repos that have no urgent failing PRs.

## When to choose this slice

- Repo is a static HTML/CSS/JS portfolio or demo gallery.
- It already deploys to GitHub Pages or similar static hosting.
- There are no active test/lint commands, package dependencies, or open failures to fix.
- A small PR-time safety net is more valuable than adding another visual artifact.

## What to add

1. A no-dependency validator script:
   - Prefer `scripts/validate_static.py` using only the Python standard library for plain static HTML galleries.
   - Prefer `scripts/validate_course.js` / `scripts/validate_static.js` using only Node built-ins when the repo is already a JavaScript-shaped single-file template with embedded JS data objects (for example `COURSE_DATA`), because Node can syntax-check the script and validate/evaluate the extracted object literal without adding npm dependencies.
2. `.github/workflows/validate.yml` (or a repo-specific name) triggered on `pull_request` to the default branch and `workflow_dispatch`.
3. A short README section documenting the local validation command.

## Validator checks

Keep the validator deliberately lightweight and deterministic:

- Discover root `*.html` files plus `demos/*.html` when present.
- Parse with `html.parser.HTMLParser`; do not require BeautifulSoup or npm packages.
- For each HTML file, assert:
  - `<html lang=...>` is present.
  - `<meta name="viewport" ...>` is present.
  - `<title>` has non-empty text.
  - Local `href` and `src` targets exist.
  - Local links resolve inside the repository root; reject `../` escapes.
- Skip external/special links: `http(s)`, protocol-relative URLs, anchors, `mailto:`, `tel:`, and `data:`.
- For demo galleries, assert `index.html` contains required demo links so launch buttons do not silently disappear.
- For single-file templates with embedded JS data, extract the data object only (not the whole page script) and validate real consistency rules: required string fields, lesson/page arrays, sidebar page indexes, quiz `correct` indexes within `opts`, flashcard/Q&A `q`/`a` fields, and checklist item strings. If the validator exposes a mismatch in the checked-in template (for example placeholder sidebar links pointing past the included lesson count), fix the template/comment so the guardrail is meaningful instead of loosening the check.

## Workflow shape

```yaml
name: Validate static portfolio

on:
  pull_request:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  static-smoke:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Validate HTML files and local demo links
        run: python3 scripts/validate_static.py
```

## Verification before PR

Run and report real output:

```bash
python3 -m py_compile scripts/validate_static.py
python3 scripts/validate_static.py
git diff --check
git diff --stat
```

A good success line is explicit, e.g. `Validated 3 HTML files and required demo links.`

## Pitfalls

- If an agent creates incidental helper folders such as `.omc/`, remove them before staging.
- `set -e` shells can stop on harmless non-zero commands during diagnostics; if a combined command fails unexpectedly, rerun subcommands individually and capture each exit code before changing the code.
- Do not add package managers or browser-heavy tests to a tiny static portfolio unless the repo already uses them. The value is a fast no-dependency guardrail.
