# Practical industrial dashboard assets

Session-derived notes for operational dashboards (mining, infra, internal tools) where visuals must feel practical rather than lifestyle or cinematic.

## Useful rules
- Match the asset to the domain: racks, boards, LEDs, gauges, topology, logs, terminals, status cards.
- Prefer simple SVG or diagrammatic art for logos, favicons, and iconography.
- For hero/supporting imagery, use industrial scenes and component close-ups, not consumer-product or aspirational imagery.
- When a user corrects the domain, regenerate the asset set instead of relabeling the wrong one.
- Keep text exact by overlaying it in code; do not rely on image-model typography.
- Check the final image at the size it will actually appear in the UI. If it looks like decoration instead of instrumentation, simplify.

## Anti-patterns to avoid
- Car-wash / automotive glamour language in a crypto-mining or ops dashboard.
- Full-bleed cinematic hero art when the product is an operator console.
- Rounded-card + gradient + glossy-photo combinations that read as generic AI marketing.
- Reusing assets from an unrelated project because they are already available.

## Raster fallback note
If hosted image generation is unavailable or rate-limited, generate real PNG assets locally (for example with Pillow or another deterministic drawing pipeline), wire them into the app, and verify them with `file` plus a live render. A real local PNG is better than stalling on the task.

## Good prompts
- "Industrial ASIC rack illustration, dark slate palette, status LEDs, clean negative space, no text"
- "Minimal SVG logo mark for a mining ops dashboard, geometric, small-size legible, no lifestyle cues"
- "Hardware detail tile for a fleet monitoring UI, technical, utility-focused, flat lighting, no glamour"
