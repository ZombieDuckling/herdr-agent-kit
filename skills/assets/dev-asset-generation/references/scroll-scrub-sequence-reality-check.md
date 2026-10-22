# Scroll-Scrub Sequence Reality Check

This reference captures the correction from a landing-page iteration where a "scroll sequence" was technically wired but not visually convincing.

## Durable lesson

A scroll-scrub section is not done when:

- a canvas component exists,
- frame URLs return 200,
- a manifest has a `frame_count`, or
- the frames are just a soft dissolve between unrelated stills.

It is done only when the page has **visible frame-by-frame motion while scrolling** and the agent has tested the rendered page itself.

## Minimum viable visual sequence

For development proof-of-motion, generate a sequence with at least 3 phases, not a start/end crossfade:

1. Camera push-in / perspective movement.
2. Contact event: water, foam, mist, light sweep, object movement, or scene transition.
3. Finish/settle frame with a visibly different composition.

The frames may be deterministic/generated rather than model-video-perfect, but they must show obvious change when scrubbed.

## Verification checklist

- [ ] 60+ frames for a serious section, or 24+ for a quick prototype.
- [ ] Sample frames from early/middle/late differ by hash **and** by visible content.
- [ ] A contact sheet or preview video is generated for quick inspection.
- [ ] The rendered page is opened/tested, not just built.
- [ ] The canvas/image sequence is visible above overlays and not hidden by z-index, blend modes, opacity, or missing draw calls.
- [ ] The component uses the actual frame count and extension deployed.
- [ ] Production verifies at least first, middle, and last frame URLs.

## Anti-patterns

- Calling a cross-dissolve between two still images "motion".
- Shipping only plumbing/templates/scripts without integrating a convincing example.
- Relying on `curl -I` success as proof that scroll motion works.
- Letting dark overlays hide the very visual sequence the user asked to see.

## Preferred proof artifacts

Create one or both:

```bash
# Contact sheet sampled every 12 frames
ffmpeg -y -pattern_type glob -i 'public/sequence/wash/frame-*.jpg' \
  -vf "select='not(mod(n,12))',scale=320:180,tile=4x2" \
  -frames:v 1 -update 1 public/sequence/wash/contact-sheet.jpg

# Preview video
ffmpeg -y -framerate 24 -i public/sequence/wash/frame-%04d.jpg \
  -c:v libx264 -pix_fmt yuv420p public/sequence/wash/preview.mp4
```
