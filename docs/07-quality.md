# Quality: measured, not hoped

"Done" is a claim that needs proof. The kit gives agents the tools to prove it and the habit
(`fable-verify`) of using them.

## Websites: check the running site

```sh
npm i -D playwright @axe-core/playwright && npx playwright install chromium     # once per project
node ~/.herdr-agent/kit/skills/quality/web-qa/scripts/check-site.mjs http://localhost:4173/ --out .qa
```

One JSON line comes back:

```json
{"pages":6,"consoleErrors":0,"failedRequests":0,"brokenLinks":0,"axeSeriousOrCritical":0,
 "axeOther":2,"phoneOverflowPages":0,"buttonsToConfirm":1,"ok":true}
```

It crawls every page at desktop and phone width, records console errors, failed requests and 404s,
broken links, axe accessibility violations, horizontal overflow on phones and buttons with no visible
action, and saves full-page screenshots of each page in both sizes.

## Code: real scanners

| Tool | Command | Finds |
|---|---|---|
| SonarQube | `sonar analyze` (or eslint + eslint-plugin-sonarjs with a baseline) | Bugs, code smells, complexity |
| semgrep | `semgrep --config p/javascript --config p/security-audit` | Security patterns |
| gitleaks | `gitleaks dir .` | Committed secrets |
| The project | `npm run build`, `npm test` | Whether it works at all |

Baseline what is house style so only **new** findings fail; fix what is a defect.

## Performance

On a throttled phone: LCP under 2.5 s, CLS under 0.1. `npx lighthouse <url> --preset=perf
--form-factor=mobile`. Preload the hero image; serve WebP with `srcset`; reserve space for things that
load late.

## The report

```
QA: http://localhost:4173/, 6 pages
console errors 0 · failed requests 0 · broken links 0 · axe serious/critical 0 (other 2) · phone overflow 0
LCP 1.8 s · CLS 0.02 (phone, throttled) · sonar 0 new · semgrep 0
Not checked: real-device test
```

Numbers, not adjectives. And "not checked" is always said out loud.

Next: [limits and handover](08-limits-and-handover.md).
