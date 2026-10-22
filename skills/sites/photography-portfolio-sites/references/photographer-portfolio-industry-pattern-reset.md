# Photographer portfolio industry-pattern reset

Use when the user asks to research other photographer/portfolio pages and copy common designs, or when a photography portfolio still reads like a generic marketing/agency/SaaS site.

## Source-backed pattern

A recent portfolio-site pass inspected several well-known photographers' public portfolio sites. Some candidate sites were blocked by Cloudflare/access controls and were not used as evidence.

Common traits that transferred well:

1. Minimal navigation language:
   - `Work`, `Stories`, `About`, `Contact` are more common than feature-style labels.
   - Services/pricing can exist, but should feel secondary to the work/archive.
2. Homepage as portfolio front door:
   - large image-first hero
   - sparse positioning copy
   - selected work/project/story index
   - direct contact path
3. Archive first:
   - category/project/story-led browsing
   - enough images to feel like a real body of work
   - named series/stories, not generic “features”
4. Copy restraint:
   - photographers’ sites often have less explanation and more visual authority.
   - avoid meta copy explaining the redesign or “common pattern” rationale publicly.
5. Visual grammar:
   - large/full-bleed or hard-edged images
   - simple typographic nav
   - black/white or restrained editorial palette works when the brief asks for flat black.

## Implementation steps

1. Inspect 4–6 real photographer sites when tools permit. Capture nav labels, home structure, gallery/archive structure, and CTA/contact placement.
2. Distill common architecture, not just colors:
   - nav labels
   - hero role
   - work/story index
   - gallery/archive depth
   - services/pricing hierarchy
3. Adapt the current project:
   - rename nav toward `Work / Shoots / About / Pricing / Contact` when appropriate
   - make the homepage a selected-work front door
   - add image-backed story/project entries instead of generic route cards
   - make gallery/archive the primary product
   - keep services/pricing available but secondary
4. Verify with screenshots and route checks.
5. Scrub stale direction in docs as well as source so old palette/copy guidance does not reappear later.

## Pitfalls

- Do not claim blocked sites were inspected; note that they were blocked and omit them from evidence.
- Do not copy a single competitor’s distinctive identity. Copy common structure and interaction patterns.
- Do not turn the site into a one-page marketing funnel; photography portfolios should behave like archives first.
- Do not leave internal phrases like “common industry pattern”, “front door”, or redesign rationale as public-facing copy.
