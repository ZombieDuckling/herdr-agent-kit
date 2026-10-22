---
name: photography-portfolio-sites
description: Use when building photography portfolio sites for the user.
version: 1.0.0
author: Hermes Agent
license: MIT
---

# Photography Portfolio Sites

Use this when building, redesigning, or repairing a photographer portfolio, gallery site, or image-first creative-services website for the user.

## Core stance

Do not ship a generic one-page SaaS-style landing page with a hero, a tiny decorative carousel, stacked cards, and a booking form at the bottom. A photography site must behave like a portfolio first and a services site second.

## Required architecture

Default multipage shape:

- `/` — front door / positioning / selected images / route directory
- `/gallery` — the real archive
- `/services` — bookable shoot types
- `/about` — approach, editing style, delivery expectations
- `/pricing` — starting packages or pricing guide
- `/booking` or `/contact` — enquiry path

If the user says the site still feels like “a one-page app” or says “there’s no actual gallery section,” treat that as an architecture failure, not a styling nit. Split the site into real routes immediately.

## Homepage rule

The homepage is a front door only:

- strong photographic hero
- concise positioning
- route directory into gallery/services/about/pricing/booking
- a few selected frames only

Do not dump the full portfolio onto the homepage after the user asks for multipage structure.

## Gallery rule

The gallery must be first-class, not token:

- dedicated route (`/gallery`)
- multiple categories such as Portrait, Wedding, Commercial, Lifestyle, Events, Creative
- enough images to read as an archive, not a 4–5 image demo
- image-led layout: masonry/editorial grid, contact sheet, or equivalent
- image inspection/lightbox or expanded view
- mobile-safe browsing and filtering
- optional spatial/3D featured runway if it supports the portfolio instead of replacing it

A small hero carousel is not “the gallery.”

## Anti-slop rules for portfolio sites

- Flatten sections against the page background when possible.
- If the user says borders/cards are overused, remove containerized pricing, booking, and gallery-caption panels first.
- Use typography, spacing, image rhythm, and page atmosphere instead of stacked cards.
- Claymorphic treatment, if used at all, should be limited to tactile accents such as logo marks or a primary CTA — not every content block.
- No opacity fade-in reveal system.
- Use real images as the visual authority.
- Do not leave meta copy on the page about the site being a “concept,” “front door,” or “not a single-page site.” Translate that into customer-facing copy.

## Pixel-art interface tier

When the user asks for a "pixel art design scheme", that describes the site's interface, not its photography: portfolio images stay real photographs, the chrome around them (nav, headings, buttons, panels, hero scene) is authored pixel art.

- The hero pixel scene must contain authored characters doing something legible — drawn pixel by pixel from sprite maps — never a field of procedurally placed animated rectangles. Animated rectangles with no silhouette read as "they didn't do any pixel art" and get rejected.
- Use an instrument strip (readout bar: record marker, place, counts) instead of an eyebrow label above the heading. It carries information and starts flush-left with the heading, lede and CTAs.
- Headline, strip, lede and button row must share one left edge at every breakpoint; a heading that starts at a different offset from its own eyebrow reads as broken alignment.
- Buttons are square, hard-edged pixel slabs with stepped hover states, not rounded gradient button kits.
- Run pixel scenes on a stepped frame clock (~8 fps), never smooth 60 fps motion; honour `prefers-reduced-motion`.
- Scene scaling, sprite composition and canvas verification: `references/pixel-art-site-interfaces.md`.

## Build workflow

1. Write a short outcome contract before rebuilding:
   - brand/palette
   - required routes
   - gallery requirements
   - anti-slop constraints
   - business content requirements
   - acceptance evidence
2. Build shared navigation, shared styling, and clean routes.
3. Keep the homepage shorter than the archive.
4. Build the gallery route as an actual destination.
5. When the user asks for multiple design options, build each option as a full site treatment with its own route or preview surface: header/nav, hero, work/gallery preview, services/approach, contact CTA, and footer/contact. Do not satisfy this with three mood cards unless they explicitly asks for a comparison board.
6. For style-route comparisons, open the actual variant routes in the desktop browser, not only a screenshot or selector page.
7. Verify locally before deploy.
8. Deploy and verify the live routes.

## Verification checklist

- One `<!doctype html>`, `<html>`, `<head>`, `<body>`, and `<h1>` per page.
- Every route exists and loads from the live host.
- Desktop and mobile have no horizontal overflow.
- Scroll the gallery during QA so deferred-loading image failures are not hiding below the fold.
- Gallery images resolve and lightbox/dialog behavior works.
- If a lightbox is used, return focus to the clicked thumbnail after close.
- Remove prompt-like/internal critique copy before deploy.
- Confirm the live result still reads as the intended brand on every route.
- Read the hero canvas back pixel-by-pixel: no unpainted pixels, sprite silhouettes present at their authored coordinates, and a visibly different frame a second later (animation actually advances).
- Drive the booking/enquiry wizard end to end after any route or generator change: reach the receipt step, confirm the reference code renders, and confirm the booking persisted on the device.
- Confirm heading, strip, lede and CTA share one left edge at desktop and mobile widths (`getBoundingClientRect().left`).

## Reporting

Final report should be concrete:

- live URL
- route list
- what changed architecturally
- what was verified with real outputs
