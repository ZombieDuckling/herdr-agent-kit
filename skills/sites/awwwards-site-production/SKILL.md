---
name: awwwards-site-production
description: Use when running the awwwards/jury design skills.
version: 1.0.0
platforms: [macos, linux]
metadata:
  hermes:
    tags: [design, qa, playwright, gsap, performance]
    category: web-design
---

# Running the awwwards / jury skills for real

Lessons from a full build-and-QA run of `~/.hermes/skills/web-design/awwwards` and `jury`. The
skill's own docs cover the design method; this covers what actually breaks when you execute it.

## Tooling

- The skill's scripts (`shoot.mjs`, `audit.mjs`, `serve.mjs`, `og.mjs`, `font.mjs`, `photos.mjs`)
  resolve Playwright and axe-core from the **project directory**, not from the skill directory.
  Run them with `NODE_PATH=<project>/node_modules` and install `playwright axe-core` in the project.
- `browser.mjs` launches the system Chrome, so `chromium.launch({})` from your own scripts fails
  when the cached Playwright browser build is stale. Use `chromium.launch({ channel: 'chrome' })`.
- Read `report.json` fields directly (`desktop.loaderMs`, `mobile.vitals`, `hover`, `a11y`,
  `keyboard`, `reduced`, `smallTargets`) instead of trusting the summary line.

## The loader cap is a wall-clock problem, not an animation problem

`loaderMs` measures until `#loader` is hidden. On a 4x-throttled phone that number blows past the
2.6 s bar for reasons unrelated to the loader's own timing: the JS bundle and fonts arrive late,
so `boot()` starts late and the sequence runs late. Fixes that actually work:

1. Bound the asset wait: `Promise.race([document.fonts.ready, wait(0.8)])`; never let a font fetch
   gate the first screen.
2. Add a plain-JS failsafe in the layout head that hides the loader at ~1.6 s if the engine has
   not finished it.
3. Only hide content behind `html.motion` once the engine is actually running
   (`.is-booted.motion [data-split]`), otherwise a slow bundle leaves a blank page when the
   failsafe fires. With that gate the hero text paints underneath and LCP stays under 1 s.

Measured after those three changes: loader hidden at 1.9 s desktop and 1.87 s throttled phone.

## Idle motion

`shoot.mjs`'s `idleMotion` detector is a threshold on pixel change, so thin 1 px sweeps and small
colour drifts read as false even when the concept is moving. Verify yourself with two screenshots
of the same clip 4 s apart, hashed and compared, and drive something with real amplitude on the
site's single clock (a 2 px scanning bar, travelling packets, pulsing status LEDs). Record the
measurement in `DESIGN.md` either way.

## Accessibility traps these builds hit

- A gradient-background underline technique makes axe report `contrastNeedsReview` for every such
  link. `text-decoration` with `text-decoration-color` toggling has no background, so contrast
  stays computable.
- `aria-label` on a link whose visible text is an email address triggers a serious
  `label-content-name-mismatch`. Do not label an address: write the link as "Email" and keep the
  raw address as plain text beside it.
- Primary targets must change something that is not a colour (`translate`, thickness, clip).
  `hover.colorOnly` is read as a failure.

## Blind critic

Delegate the critic with the rubric text, the `.shots` path, the audit output and up to 8 images
as `images` - the child cannot read PNGs by path without them. Give it no DESIGN.md and no code.
Its one-line reading of the concept is the useful signal: if it disagrees with the concept card,
fix the site, not the critic.
