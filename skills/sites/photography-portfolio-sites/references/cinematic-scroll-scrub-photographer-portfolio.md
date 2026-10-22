# Cinematic scroll-scrub photographer portfolio pattern

Session-derived pattern for photographer portfolios where the user wants ScrollCraft-like motion without AI-slop hero/nav/mobile failures.

## What the user was correcting

- Background video that merely plays behind copy does not feel like scrolling through footage.
- Reveal gates/clip-path openings also miss the brief when they ask for pure video scrub.
- A generic collage/card hero and generic nav read as AI slop even if the rest of the site is technically working.
- Mobile must be treated as its own viewport, not the desktop pinned experience squeezed down.
- Delicate serif typography can feel wrong for this class; the user described the desired feel as blocky/techy/artsy photographer type.
- “No gradients” is literal: remove CSS gradients and verify computed style.

## Implementation guidance

- Use a pinned hero video scene that flows into the rest of the site. The hero should be a cinematic entry point, not a conventional landing-page card/collage.
- For each scrubbed video:
  - `muted playsinline preload="metadata"`
  - no `loop`
  - no autoplay dependency
  - keep it paused
  - map scroll progress to `video.currentTime`
- If scroll feels too abrupt, use a RAF loop with damped progress and a max time-step per frame. Verify that a quick scroll produces a small early `currentTime` delta and a larger settled delta.
- Avoid video reveal/opening effects when the requested motion is pure scrub: no `clip-path` gate, scale-in, fade-in, or crop-progress on the video plate.
- For mobile, shorten pinned spans, prevent fixed nav from covering hero text, hide route strips or heavy chrome, and turn long sticky rails into normal-flow horizontal scrollers or compact sections.
- Use blocky local-safe display fonts for the photographer-art/tech feel: `Impact`, `Avenir Next Condensed`, `DIN Condensed`, `Bahnschrift Condensed`, `Arial Black`, plus condensed sans body/chrome. Prefer local stacks over remote font imports when publishing quick demos.
- Remove process/internal residue before deploy: `OpenClaw`, `agent`, `prompt`, `Claude`, `Hermes`, `ScrollCraft`, outcome contracts, and implementation commentary should not appear in public source/docs unless deliberately part of the repo docs.

## Verification probes

- Build passes.
- Desktop and 390px mobile browser checks pass with no horizontal overflow.
- Mobile screenshot at `scrollTo(0,0)` shows nav not covering hero copy.
- Source and computed styles contain no gradients when gradients were rejected.
- Source contains no rejected font names or remote `@import` font dependencies if local fonts were chosen.
- Video scrub probe:
  - `video.paused === true`
  - no `video[loop]`
  - `currentTime` changes as scroll changes
  - early delta after a fast jump is bounded
  - settled delta continues moving after the initial jump
