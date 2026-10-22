# Reliable Scroll-Scrubbed Image Sequence Workflow

This is the repeatable baseline for turning generated keyframes into a scroll-driven cinematic section.

## Contract

Output a directory of numbered frames:

```text
public/sequence/wash/frame-0001.webp
public/sequence/wash/frame-0002.webp
...
public/sequence/wash/frame-0072.webp
public/sequence/wash/manifest.json
```

Any generator can be swapped in as long as it obeys that contract.

## Baseline: deterministic ffmpeg keyframe blend

Use when reliability matters more than perfect optical-flow motion. It creates a coherent scroll-scrub asset from two still frames with no external AI/video service.

```bash
python <this skill>/scripts/make_scroll_sequence.py \
  --start ./public/assets/cinematic-tunnel.png \
  --end ./public/assets/hero-noirwash.png \
  --out-dir ./public/sequence/wash \
  --frames 72 \
  --width 1440 \
  --height 810 \
  --format webp \
  --clean
```

Verify:

```bash
python - <<'PY'
from pathlib import Path
frames = sorted(Path('public/sequence/wash').glob('frame-*.webp'))
print(len(frames), frames[0], frames[-1])
assert len(frames) == 72
PY
```

## Better middle frames

When a real image-to-video or interpolation backend is available:

1. Generate start/end keyframes with the same camera, car position, lighting, and aspect.
2. Generate a 3–5s video between them using a video model or ComfyUI workflow.
3. Extract frames to the same contract:

```bash
mkdir -p public/sequence/wash
ffmpeg -y -i generated-shot.mp4 -vf "fps=24,scale=1440:810:force_original_aspect_ratio=increase,crop=1440:810" \
  -c:v libwebp -q:v 82 public/sequence/wash/frame-%04d.webp
```

4. Create/update `manifest.json` with frame count and dimensions.

## React integration

Copy the template into the project:

```bash
cp <this skill>/templates/ScrollSequenceCanvas.jsx ./src/ScrollSequenceCanvas.jsx
cat <this skill>/templates/scroll-sequence.css >> ./src/styles.css
```

Use it:

```jsx
import ScrollSequenceCanvas from './ScrollSequenceCanvas.jsx';

<ScrollSequenceCanvas
  frameBase="/sequence/wash/frame-"
  frameCount={72}
  extension="webp"
  heightVh={380}
>
  <div className="sequence-copy sequence-copy--one">Enter.</div>
  <div className="sequence-copy sequence-copy--two">Pressure hits.</div>
  <div className="sequence-copy sequence-copy--three">Finish appears.</div>
</ScrollSequenceCanvas>
```

## Anti-slop rules

- Do not add rounded cards over the sequence.
- Do not hide weak motion behind gradients.
- Do not make text float randomly. Tie text beats to progress points.
- Use hard cuts, full bleed imagery, and typography that feels editorial/filmic.
- If the generated frames are incoherent, reduce ambition: use fewer keyframes, a simpler camera move, or a deterministic blend until a proper video backend is available.

## Verification checklist

- `manifest.json` exists and frame count matches actual files.
- First and last frames visibly match the intended keyframes.
- `npm run build` passes after integration.
- Scrolling through the pinned section visibly changes frames.
- `prefers-reduced-motion` does not trap users in a long pinned animation.
