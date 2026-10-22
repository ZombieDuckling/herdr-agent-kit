# Static Demo Multi-Page Anti-Slop Pass

Use this reference when a static demo site is criticized as "too much of a one page", "needs more pages", "needs images", "generate a logo", "use the logo instead of text", or "remove AI slop".

## Trigger

The user wants a quick demo site to feel like a real client-facing website rather than a single scrolling brochure. This is an asset + information-architecture + deployment pass, not just a cosmetic CSS tweak.

## Hard scope rule

If multiple demo projects exist, confirm the active domain from the latest user instruction and keep unrelated projects untouched. If the user corrects scope (for example, "we are working entirely and solely on the dietician website"), treat it as a hard reset and do not continue the previous project unless explicitly re-requested.

## Upgrade pattern

1. Inspect the current site structure and assets.
2. Define a small real page map, usually 4–6 pages:
   - `index.html` — home / positioning
   - domain-specific offer page(s), e.g. `services.html`, `rooms.html`, `meal-plans.html`
   - trust/about/safety page, e.g. `about.html`, `responsible-play.html`
   - conversion page, e.g. `appointments.html`, `demo.html`
3. Generate page-specific images, not one generic hero reused everywhere:
   - home hero
   - primary offer page hero
   - education/process page hero
   - appointment/conversion/trust page hero
4. Create a real logo system:
   - Prefer hand-coded SVG for the final logo/mark.
   - AI can generate a text-free brand concept image, but exact wordmark/logotype should be SVG/code to avoid garbled text.
   - Save at least `assets/<brand>-logo.svg` and `assets/<brand>-mark.svg`.
   - Use the logo image in nav/footer and mark as favicon; do not leave a plain text brand or initial-only pill when the user asked for a logo.
5. Rebuild navigation and footer across all pages:
   - all pages link to all primary pages
   - active nav state uses `aria-current="page"`
   - conversion CTA is visible
6. Rewrite copy to be concrete and domain-specific:
   - avoid vague "journey", "unlock", "transform", "premium experience" filler unless the domain genuinely calls for it
   - explain what the service/app does, what happens next, and demo boundaries
7. Preserve honest demo constraints:
   - no backend / no data submission / front-end only
   - no fake regulated functionality
   - no medical/legal/financial claims unless reviewed by qualified people
8. Update README/agent notes with the page map and asset list.

## Verification checklist

Before reporting done:

- JS syntax passes.
- Every page includes the SVG logo, CSS, script, and full nav.
- Every page has domain-appropriate demo-boundary copy.
- All new PNG/SVG assets exist, are non-empty, and `file` identifies them correctly.
- Serve locally over HTTP and fetch every page + key assets with HTTP 200.
- Capture at least desktop and mobile screenshots of the home page, plus screenshots of key new pages.
- If there is a form, verify client-side validation and success state when possible.
- Deploy/redeploy only after local verification; verify the live alias directly with HTTP/content checks rather than trusting CLI success text alone.

## Pitfalls from session history

- Do not infer the active project from stale context or a quoted/replied message. Latest user instruction wins.
- If a voice transcript says a near-domain word incorrectly (e.g. "statistician" while the active project is dietician), resolve it against the user's explicit current project before acting.
- Do not convert the wrong demo site just because it is the most recent site touched.
- Do not stop at "generated a logo" if the nav/footer still show text-only branding.
