# Pixel-art site interfaces: authoring and verification

Depth for the pixel-art tier of a photos-are-real / chrome-is-pixel site.

## Authoring sprites

- One array of strings per sprite, one character per pixel, with a character-to-hex-colour table; `.` and space are transparent.
- Keep characters 12–20 px tall so their silhouette reads at hero scale.
- Anchor every character on the ground line: the sprite's last row sits on the deck/parapet row. A sprite stamped below the ground line looks like it floats off the surface.
- Compose a fixed, authored scene (skyline blocks with fixed window grids, deck, props) rather than randomised placement, then layer motion: cloud drift, bird crossing, blinking windows, a walking passer-by, a flash firing on a stepped schedule.

## Canvas scaling — the failure that looks like "empty"

Size the canvas `LW * scale` x `LH * scale`, then `ctx.setTransform(scale, 0, 0, scale, 0, 0)` and draw in logical coordinates. Drawing without that transform paints only the top-left `LW` x `LH` device pixels: the scene appears as a stamp-sized drawing in the corner while the rest of the hero stays blank, and a pixel-level read-back shows the majority of pixels unpainted.

- `Math.floor` animated coordinates so pixels stay crisp under a scaled transform.
- Draw light bloom (flash, glow) before the subject, never after: a bright rectangle drawn last erases the character for those frames.
- Stepped clock: repaint on `setInterval` at ~125 ms; a 1-px vertical bob every 6 frames reads as breathing without smooth motion.
- It is safe to skip `clearRect` when the first fill covers the full logical grid.

## Verifying without seeing the image

Screenshots are the wrong tool when the model cannot view them. Read the canvas back instead:

- `getImageData` over the full canvas, then map each pixel to a letter using a table keyed on the exact palette hexes, and print crops around each sprite's authored coordinates.
- Use that colour table, not a brightness ramp: dark palettes (near-black sky and building tones) collapse into blanks under a luminance ramp, so a fully drawn scene reads as empty.
- Any non-zero count of alpha-0 pixels means the scale transform is missing or the paint is incomplete.
- Take two readbacks a second apart and diff them to prove the animation clock is running.

## Driving interactive wizards in QA

- Option cards, day grids and time slots are created at runtime under classes (`.opt`, `.cal button`, `.slots button`) — query the rendered step body, not hand-guessed `data-*` attributes.
- Set text inputs by assigning `.value` then dispatching `new Event('input', {bubbles: true})`; assigning `.value` alone leaves the tool's state empty and totals stay at zero.
- Validation blocks advancing until the current step is answered, so a step body that never changes means the click was rejected — not that the selector is wrong.

## Editing generated sites

Generated routes come from a build script; source files often already exist on disk. Edit with targeted replacements (`read_file` then `patch`) rather than whole-file overwrites, and rebuild the generator before verifying the routes.
