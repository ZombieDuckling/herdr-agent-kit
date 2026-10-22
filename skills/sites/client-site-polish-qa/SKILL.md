---
name: client-site-polish-qa
description: Use when polishing and QAing client static sites.
---

# Client Site Polish QA

Use this skill when a client site already exists and the task is to make it look finished rather than rebuild the product: visual polish, Impeccable-style refinement, static-site QA, mobile checks, deploy verification, or anti-slop cleanup.

This is a class-level companion to broader client-site design skills. It focuses on the last-mile pass: remove telltale scaffolding, verify the built artifact, and ship only after screenshots and public URL checks.

## Core workflow

1. Identify whether this is a new visual world or a scoped refinement.
   - If the user asks for a new design language, use the relevant redesign skill first.
   - If the user says “do another run”, “polish”, “with Impeccable”, or “make it less slop” after a design is already live, treat it as a bounded craft/refinement pass.
2. Inspect incumbent visual truth before editing:
   - main CSS/tokens
   - representative page/component
   - real logo/assets
   - package/build stack
3. Remove common client-site craft tells:
   - eyebrow/kicker labels above headings that only restate the heading; replace them with an informational status/readout strip that sits flush-left with the heading instead
   - meaningless `01/02/03` scaffolding
   - generic default fonts if a detector flags them, especially Inter
   - rounded cards/glass/gradient borders/fake metrics unless explicitly approved
   - public TODO/placeholder/agent-meta copy
4. Theme browser surfaces that models usually skip:
   - `::selection`
   - `:focus-visible`
   - scrollbars
   - caret color
   - placeholder color
   - link underline offset
5. Verify mobile as a real viewport, not a cropped desktop screenshot.
   - Check `innerWidth`, `documentElement.scrollWidth`, and `body.scrollWidth` at ~390 CSS px.
   - Open the mobile menu and screenshot it; it must not bleed page content through.
6. Check internal alignment with measurements, not vibes: heading, any strip/eyebrow, lede and CTA must share one `getBoundingClientRect().left` at desktop and mobile widths. A heading that starts at a different left offset from the label above it is the alignment complaint users actually raise.
7. Build, route-test, screenshot, detector/audit once, fix mechanical findings, then stop polishing.
8. Commit, push, and verify the public alias/custom domain itself with HTTP checks and expected assets. Do not rely only on a deployment dashboard saying “Ready”.
9. Re-verify interactive flows on the live host after deploy (wizard end-to-end to its confirmation state), not just route status codes.

## Impeccable-specific notes

- Run Impeccable context when loaded. If it says `PRODUCT.md` or `DESIGN.md` is missing but also says scoped existing refinement is allowed, proceed with the polish pass instead of blocking on a product interview.
- If the detector flags `Inter` as overused, swap to a more deliberate font that fits the design world rather than arguing with the detector. For flat black editorial photography, `Archivo` worked well.
- Add or refresh `DESIGN.md` after the built result is known so the visual system survives future sessions.
- If adding an Impeccable contract comment, verify the production build preserves it by grepping `dist/`.

## Verification commands / patterns

For Vite/static sites, use Playwright to capture desktop, representative inner page, mobile, and mobile-menu screenshots. Also run a route sweep for console errors.

Minimum checks:

- `npm run build`
- route sweep: `/`, key inner pages, booking/contact pages
- screenshot desktop + mobile
- mobile overflow metrics at 390px
- stale-copy grep for rejected language and public placeholders
- detector/audit pass if available
- public alias `curl -L` status and expected asset names

## Reference

- `references/flat-black-impeccable-pass.md` — session-derived checklist for a flat black spatial photography portfolio refinement.
