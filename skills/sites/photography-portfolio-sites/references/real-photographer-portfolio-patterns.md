# Real photographer portfolio pattern reset

Use when the user asks to research photographer/portfolio pages and copy the common design language, or when a photography site still feels like a generic marketing/template page.

## Observed real-site patterns

From a portfolio-site session inspecting several well-known photographers' public sites (blocked sites were excluded from claims), the durable patterns were:

- Navigation is minimal and portfolio-native: `Work`, `Stories`, `About`, `Contact`; sometimes `Journal`, `Motion`, `Shop`, or category labels.
- The work/archive is the product. The homepage is a front door into a real archive, not a SaaS feature pitch.
- Galleries are category/project/story led: Overview, Beauty, Fashion, Celebrity, Select Projects, Stories, Portraits, etc.
- Copy is sparse. Photographs, named projects, and story titles carry credibility.
- Services/pricing/contact support the portfolio; they should not dominate the brand language.
- Many strong photographer sites use large/full-bleed images, contact sheets, project grids, and direct contact CTAs.

## Adaptation steps

1. Inspect 4–6 real photographer sites if web/browser access is available. Ignore blocked/security-check pages and do not cite them as evidence.
2. Extract common navigation labels and archive structure before styling.
3. Rename generic site routes/labels toward photographer language when appropriate:
   - Gallery → Work
   - Services → Shoots / Commissions
   - Booking → Contact
   - selected image blocks → Stories / Selected Work
4. Make the homepage a work index:
   - strong image-first hero
   - one concise positioning line
   - selected named stories/projects with image-backed links
   - direct route into the full archive
5. Keep services/pricing as secondary utility pages, not the main persuasion device.
6. Remove public meta-copy about “common patterns”, “front door”, or implementation rationale; translate it into client-facing copy.
7. Verify with desktop/mobile screenshots, route checks, and stale-copy scans before deploy.

## Pitfalls

- Do not overfit to one example site; copy the common class pattern, not a specific site’s identity.
- Do not use blocked pages as research evidence.
- Do not turn “copy common designs” into generic cards, fake metrics, or SaaS conversion sections.
- If the client has no real images yet, use strong placeholders only as implementation scaffolding and mark replacement needs in handoff/docs, not as public page copy.
