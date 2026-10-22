---
name: static-demo-portfolio-publishing
description: Build, verify, version-control, and publish static HTML demo portfolios for the user — polished one-off UI demos, sellable portfolio pages, Safari preview, GitHub, Vercel, and GitHub Pages deployment.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [frontend, portfolio, static-site, github-pages, demo, safari]
---

# Static Demo Portfolio Publishing

Use this when the user asks for a quick visual/UI demo and wants it added to a demo portfolio, GitHub, or GitHub Pages. This skill complements frontend design skills; it focuses on packaging, verification, preview, and publishing workflow.

## Trigger phrases

- "build me a demo"
- "make it sell"
- "add this to my demo portfolio"
- "push this to GitHub"
- "constantly push to git"
- "push to production on Vercel"
- "make a demo portfolio on GitHub"
- "open in Safari when you're done"

## Default artifact shape

Prefer a static site unless the user asks for a real app/framework:

```text
index.html
README.md
demos/<demo-name>.html
assets/<demo-logo-or-hero>.(svg|png|webp)
.github/workflows/pages.yml
```

The portfolio `index.html` should sell the work, not just list files:

- a clear value proposition
- cards/swatches linking each demo
- short commercial/use-case copy
- repo link
- lightweight proof points such as static deploy, no framework bloat, live demos

Do not leave obvious placeholder visuals in portfolio demos. For polished demos, create or generate real assets:

- SVG/code logos and marks for crisp identity;
- text-free generated hero/background art for rich visual worlds;
- stable repo paths under `assets/`, never cache paths;
- asset references wired into both the portfolio swatch and the standalone demo page.

Each demo should be standalone and self-contained enough to open directly from disk.

## Aesthetic differentiation rule

When the user asks for a second demo "different to how you've done this," change the actual design language, not just the palette:

- material language
- palette temperature
- motion vocabulary
- spatial composition
- commercial framing/copy
- interaction model

Example split:

- **Claymorphic spatial UI:** warm inflated panels, inner highlights, candy gradients, pointer tilt, tactile CTAs.
- **Neumorphic spatial UI:** cool matte surfaces, inset controls, monochrome restraint, rotating orbital elements, signal glows, instrument-panel copy.

## Spatial portfolio interaction rule

The user specifically likes demo portfolio work where the selected surface feels like a real spatial plane sitting in a void: angled depth, layered surfaces, panels projecting off the page, and page motion around the plane. Do **not** interpret “spatial UI” as merely tilting the whole page toward the mouse.

For multi-demo portfolios, avoid overlapping swatches that pile up. Prefer a scrollable/swipeable rotating track or carousel:

- each demo is an object/swatch on the track;
- the centered item pulls forward in 3D;
- arrows, wheel/swipe, dots, and click-to-center all work;
- the detail panel and launch link update from the selected item.

When switching between design languages, the **whole portfolio shell** should change to that language — typography, background/hero image, logo/mark, border radius/geometry, texture, shadows, copy voice, and component treatment — not just the active card color. See `references/spatial-demo-portfolio-pattern.md` for the session-derived checklist.

## Public collateral boundary

When a project includes collateral such as a recruitment poster, handoff PDF, QR sheet, flyer, or evidence screenshot, do not automatically publish it as a public route. Keep collateral as an offline/generated artifact unless the user explicitly asks for it to be hosted. If you briefly publish or link collateral and the user corrects it, remove the route/link, rebuild, push, and verify the public site no longer exposes it.

## Client storefront iteration rules

For small static storefronts where the user gives rapid brand/menu/product corrections, treat each correction as a site-wide content-system update, not a one-page edit:

1. Normalize the product taxonomy in the source data first (`products.json` or equivalent), then regenerate any inlined product constants in JS so search, filters, cart, and category pages do not drift.
2. Update repeated navigation fragments across every HTML page in one scripted pass: top nav, hover dropdowns, mobile/side directory, footer, and page-category attributes.
3. When the user specifies menu structure, preserve labels exactly and verify them programmatically in both the sidebar and top nav on every page; stale labels in hidden menus count as unfinished work.
4. For product data, expose requested variants such as gluten-free or sugar-free as structured metadata and render visible badges, not just copy in descriptions, so search and cards both surface them.
5. For predictive search on static sites, build suggestions from existing product names, categories, tags, and structured variant fields; link suggestions to a queryable products page rather than hard-coding unrelated prompts.
6. For typography, keep a two-font brand system when the user references the logo: headings, buttons, strong labels, nav, and other bold/capitalised text use the logo-name/display style; normal paragraph/body text, inputs, descriptions, and small explanatory copy use the logo-slogan style. Do not introduce a third “warmer” body font after the user asks for font consistency.
7. For menu labels, distinguish the collapsed control from the opened panel: the closed button should say “Menu” when requested, while the opened sidebar/panel may retain its branded directory title.
8. For logo edits, verify the SVG text/shape semantics directly: requested words, original/display font treatment, positioning markers, rotation/orientation, colour count, and decorative dot/sparkle count before deploy.

## Verification before publishing

Before GitHub push, Vercel, or Pages deployment, run real checks:

1. Validate each HTML file has exactly one `<!doctype html>` and a closing `</html>`.
2. Validate data files such as `products.json` with `python -m json.tool`.
3. Check referenced assets exist and smoke key static assets with `curl -fsS` when a preview server is running.
4. Start a local preview server with Hermes `terminal(background=true)` — do not use shell `&`.
5. `curl -fsS` the index and every demo URL.
6. Stop the preview server and report the actual smoke output.
7. If a command is blocked by approval policy, do not retry the same outcome through a different command; preserve the useful partial verification and report the blocker plainly.

## Safari preview

If the user says to open the demo in Safari, do it after writing the artifact.

If `computer_use` capture fails or expires, verify Safari's active document with AppleScript rather than claiming visual confirmation:

```bash
osascript -e 'tell application "Safari" to get URL of front document'
```

## Git and publishing workflow

The user prefers continuous version control for client/static sites. Commit and push every meaningful checkpoint: initial scaffold, design pass, major feature group, production-deploy metadata, and post-deploy fixes. Do not leave a finished deploy sitting only in Vercel/local files.

Keep side-effecting steps approval-friendly and separable:

1. Local artifact creation.
2. Local HTML/server smoke checks.
3. `git init -b main` if there is no repo; configure the expected author if needed.
4. `git add <explicit files>` and `git commit -m "feat: ..."` for each meaningful checkpoint.
5. `gh repo create <repo-name> --private --source . --remote origin --push` for new client demos unless they requests public visibility; otherwise `git push` to the existing remote.
6. Deploy only after the current work is committed or immediately commit/push deployment metadata such as `.gitignore` after deploy tools create it.
7. Verify repo URL, branch tracking, `git status --short --branch`, and the live deployment URL/status.

If a GitHub publish command is blocked by Hermes approval/consent guard, stop and report that the local artifact is ready. Do not retry the same outcome through a different command route without approval.

## Vercel static deployment

For simple static sites, deploy from the artifact directory with:

```bash
vercel --prod --yes
```

Read the CLI output for both the immutable deployment URL and the aliased production URL. Prefer sending the stable aliased URL, then verify it by reading the live page and key assets. Check for expected brand text, product/CTA sections, and asset HTTP 200s before claiming production is live. If the user says “Vosell” or another speech-to-text variant while working on an existing Vercel project, verify the intended Vercel alias from the repo/deploy output instead of creating a new target name from the transcript. If Vercel creates `.vercel` and adds `.gitignore`, commit and push the `.gitignore` change; keep `.vercel/` out of git because it is local project metadata.

## GitHub Pages source gotcha

For simple branch-source Pages publishing, GitHub only supports serving from repository root (`/`) or `/docs`; it will not serve an arbitrary `/site` folder in branch mode. If the artifact lives in `site/`, either move/copy it to `docs/` before configuring Pages, or use a Pages workflow with `upload-pages-artifact` once Pages is enabled.

If Actions fails while trying to enable Pages with `Resource not accessible by integration`, configure Pages once with an authenticated operator `gh api` call, then rerun the workflow. Always `curl -L --fail` the public Pages URL and check expected text/links before claiming the site is live.

## Pitfalls

- Do not package a demo portfolio as one long, generic landing page. Use individual demo pages and a portfolio index.
- Do not claim a GitHub push happened unless `git push`/`gh repo view` returned real output.
- Do not claim Vercel production is live from deploy output alone; read back the aliased live URL and at least the key CSS/JS assets because aliases and static files can fail independently.
- Do not conflate local Safari preview with published GitHub Pages or Vercel availability.
- Do not leave preview servers running after smoke checks.
- Do not verify only the visible desktop header on multi-page static sites; hidden side menus, dropdowns, repeated footers, search prompts, and category attributes often retain old labels unless checked across every HTML file.
- Do not rename product categories only in page copy; filters, cart rendering, predictive search, and category pages usually read from shared product data, so update the data source and regenerated JS together.
