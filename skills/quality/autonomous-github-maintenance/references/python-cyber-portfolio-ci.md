# Python cyber portfolio CI pattern

Use this for small public cybersecurity/portfolio repos that have a single Python CLI/module, no dependencies, and no CI/tests yet.

## Good slice

Add characterization tests before changing detection logic. This is low-risk, reviewable, and creates a safety net for later correctness fixes.

## Files to add

- `tests/test_<module>.py` with pytest characterization coverage for documented behavior and scoring boundaries.
- `.github/workflows/ci.yml` that runs pytest on the Python versions the README claims to support.
- README update that documents the test command and updates the project tree/roadmap.

## Test coverage checklist

For detector-style tools, cover:

- verdict/severity threshold boundaries;
- benign baseline case;
- one test for each heuristic/signal;
- documented README example output;
- edge cases like missing host, scheme-less input, score cap, and input-file comment/blank-line handling;
- smoke invocation that proves CLI output still matches the documented example.

For log/timeline/parser tools, cover:

- JSON and CSV loading paths;
- common field-name aliases (`timestamp`, `time`, `datetime`, `event_time`, `date`);
- chronological sorting from intentionally unsorted fixtures;
- rendering/output-file behavior via a subprocess CLI smoke test;
- invalid input shape and missing required field errors;
- mixed timezone-aware and timezone-naive timestamps. If fallback formats create naive `datetime` values while ISO/Zulu inputs are aware, normalize or explicitly localize them before sorting so Python does not raise on mixed comparisons.

## CI template

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

jobs:
  test:
    name: pytest (${{ matrix.python-version }})
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.10", "3.12"]

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: python -m pip install --upgrade pip pytest
      - run: python -m pytest -q
```

## Local verification

Prefer an external temp venv or a repo-local venv that is removed before staging:

```bash
VENV=/tmp/<repo>-verify-$(date +%s)
python3 -m venv "$VENV"
"$VENV/bin/python" -m pip install --upgrade pip pytest
"$VENV/bin/python" -m pytest -q
"$VENV/bin/python" <cli>.py --url "<documented sample>"
git diff --check
git diff --stat
git status --short --branch
```

Do not stage `.venv/`, `.omc/`, or other agent/runtime metadata. If a coding agent or local verification creates them, remove them before `git add` and re-check `git status --short`.