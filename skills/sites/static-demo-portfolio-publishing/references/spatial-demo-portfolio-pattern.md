# Spatial demo portfolio pattern

Session-derived pattern for the user's interface demo portfolio work.

## What the user responded well to

- A page/surface that feels like a real spatial plane sitting in a void.
- Angled depth: cards/panels/planes lifted at different Z depths and rotations, not just a flat page with a mouse-follow tilt.
- The design language lives *inside* the spatial plane: claymorphic/neumorphic/etc. controls, typography, shadows, and surfaces are rendered within the selected world.
- Selection should visibly pull an object forward and retheme the surrounding shell.

## Corrections captured

- Do not make “spatial UI” mean only that the whole page tilts toward the mouse.
- Avoid overlapping swatches that pile up visually. Use a swipeable/scrollable rotating track or carousel so the user can move through portfolio pieces.
- Switching design languages should hard-snap the full page shell into that design language: typography, background, logo/mark, border radius, texture, shadows, copy voice, and component geometry.
- Placeholder blocks are not enough for portfolio demos. Generate or author real logos/marks and visual assets, then wire them into the page.

## Recommended implementation shape

1. Build each demo as a standalone page with its own strong visual system.
2. Create stable assets under `assets/`: SVG logos/marks for crisp identity, generated text-free PNG/WebP hero art where rich imagery helps.
3. On the portfolio home, represent demos as individual spatial objects in a swipeable horizontal/rotating track.
4. Centered item becomes active: scroll-snap to center, pull forward in 3D, update details panel, update launch link.
5. Apply a root theme (`body[data-theme=...]`) that changes the entire shell, not only the active card.
6. Verify locally over HTTP and smoke every asset/page path before deployment.

## Anti-slop checklist

- [ ] The selected design language changes the whole shell, not just card color.
- [ ] Assets are real files in the repo, not cache paths or CSS-only placeholders.
- [ ] Logos are SVG/code where possible; generated images are text-free.
- [ ] Swatches are scrollable/swipeable and do not overlap awkwardly.
- [ ] Each demo page has a different composition and interaction pattern, not the same layout reskinned.
