---
name: web-qa
description: Use before calling any website or web app done, and for any request to audit, QA, test, review or check a site. Checks the running site, not only the source - console errors, failed requests and 404s, broken links, dead buttons, axe accessibility, phone-width overflow, screenshots - plus real static scanners for the code. Reports numbers.
---

# Web QA: check the running thing

A site is done when the **running** site passes, measured, not when the code looks right. A static
scanner and a live page each miss what the other catches, so do both.

## 1. Run the site

Start it the way the project does (`npm run dev`, `npm run preview`, `python3 -m http.server`). Note the URL.

## 2. Check the running site

```sh
cd <project>
npm i -D playwright @axe-core/playwright && npx playwright install chromium   # once per project
node <this skill>/scripts/check-site.mjs http://localhost:<port>/ --out .qa
```

It crawls every same-origin page at desktop (1440 wide) and phone (390 wide) and prints one JSON line:
`pages, consoleErrors, failedRequests, brokenLinks, axeSeriousOrCritical, axeOther, phoneOverflowPages,
buttonsToConfirm, ok`. Exit 0 means no console errors, failed requests, broken links or serious/critical
axe violations. Details are in `.qa/report.json`; screenshots in `.qa/desktop/` and `.qa/phone/`.

- **Fix to zero:** console errors, failed requests, broken links, serious and critical axe violations,
  phone overflow.
- **Confirm by hand:** each "button to confirm" (the script cannot see listeners added in JavaScript;
  click it and check something happens).
- **Look at the screenshots** if you can see images. If you cannot, say "visual check: not done" and
  ask a vision-capable worker for one pass.

## 3. Check the code with real scanners

- SonarQube (`sonarqube` skill), or `npx eslint . --plugin sonarjs` against a committed baseline so
  only new findings fail.
- `semgrep --config p/javascript --config p/security-audit` (no account needed).
- The project build and tests.

Baseline findings that are house style; fix the ones that are defects.

## 4. Performance on a phone

LCP under 2.5 s and CLS under 0.1 on a throttled phone (Lighthouse:
`npx lighthouse <url> --preset=perf --form-factor=mobile --quiet --output=json`). Preload the LCP image;
size images (`srcset`, WebP); keep layout stable while things load.

## 5. Facts and rules

- Business facts (phone numbers, address, hours, prices, emails) are identical to the source unless the
  user asked to change them: `git diff | grep -E '^[-+].*(tel:|mailto:|wa\.me)'`.
- The house rules (`~/.herdr-agent/house-rules.md`) are met, for example `grep -rn 'gradient(' src` when
  gradients are banned.

## Report

```
QA: <url>, <pages> pages
console errors 0 · failed requests 0 · broken links 0 · axe serious/critical 0 (other: N) · phone overflow 0
LCP <s> · CLS <n> (phone, throttled) · sonar: N new · semgrep: N
Not checked: <what>
```
