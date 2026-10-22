---
name: document-to-test-automation
description: "Use when converting test plans into executable tests."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [testing, tdd, acceptance-tests, playwright, documents]
    related_skills: [test-driven-development, playwright-cli, docx]
---

# Document to Test Automation

## When to Use

Use this when a user supplies a DOCX/PDF/spreadsheet/manual test plan and wants it turned into code for TDD or acceptance testing.

## Always-on rules

- Treat the document as the requirements source, not as a form to mark up. If the user says to make test cases green in a TDD context, write runnable tests and a project report.
- Preserve source test IDs exactly in fixtures, test names, and reports so failures map back to the document.
- Verify extraction count against the document's summary before writing tests. Do not trust narrow regexes; IDs may use two-, three-, or longer-letter prefixes.
- Keep the suite honest: the RED baseline must fail for missing product behaviour, and the final GREEN suite must contain normal executable tests with no expected-failure or skip scaffolding.
- Do not weaken a requirement to make the suite pass. If the product is missing the behaviour, keep the test failing while you build the product; remove temporary RED guards before reporting green.

## Procedure

1. Load any relevant document/test/browser skills, then extract the document into a structured fixture such as `tests/<project>-test-cases.json`.
   - Preserve: `id`, `title`, `priority`, `steps`, `expected`, `scope`, and original result/status if present.
   - Verify totals by programmatic count and compare to any document summary table.

2. Inspect the target project before generating tests.
   - Identify the framework, existing test runner, routes/pages/API seams, and package scripts.
   - Prefer the project-native runner. For browser customer journeys, use Playwright.

3. Add test infrastructure in the project.
   - Add config (`playwright.config.ts`, pytest config, Vitest config, etc.) only if missing.
   - Add package scripts such as `test:e2e` and `test:e2e:report`.
   - Keep reports in a stable project location: HTML/JSON runner output plus a human report under `docs/testing/`.

4. Generate one coded test per source case ID.
   - Test names must begin with the case ID.
   - Add annotations/comments carrying the source steps and expected result.
   - Use helper functions for repeated journeys instead of duplicating brittle selector sequences.

5. Drive RED to GREEN through the product, not the tests.
   - Baseline RED may use a temporary guard only to prove every source case is represented and failing before implementation starts.
   - Replace each guard with real browser/API steps and assertions against the application before calling the case green.
   - Build the actual app behaviour and rerun the suite; do not satisfy a case with a fake test screen, edited result file, `test.fail`, `skip`, broad catch, or weakened assertion.
   - If a selector assertion and the source document disagree, align to the source document's stated expected result; narrow selectors only for stability.

6. Verify before reporting done.
   - Run the build/typecheck command.
   - Run the full generated suite against the built app or real dev server.
   - Grep the test tree for `test.fail`, `skip(`, `redFailure`, `Expected-red`, and `RED:` before claiming green.
   - Report real output: total tests, final pass/fail count, command results, file paths, and the anti-cheat check.

## Pitfalls

- Do not edit a DOCX/PDF to tick Pass when the user's intent is software TDD; the deliverable is executable code and a project report.
- Do not leave expected-red scaffolding, RED guards, or skips in the final suite; they turn missing implementation into a false green.
- Do not skip extraction verification because the document summary says a number; malformed tables or ID prefix assumptions can silently drop sections.
- Do not hide product gaps by changing assertions to what the current app happens to do; preserve the source expected result and keep fixing the product until the real assertion passes.
- Do not leave generated tests unrun. A test pack is not complete until the runner exits successfully and the project still builds.
