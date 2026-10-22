# WhatsApp capability-map image replacement workflow

Use when the user asks for a friendly capability map or explanatory visual to send to a trusted contact over WhatsApp.

## Lesson

For human-facing relationship/context images, a hand-coded SVG can feel too rigid or underwhelming. Prefer the ChatGPT/Codex image backend for the visual/art direction, then verify the text with vision before sending. If exact labels are mission-critical and the generated text is garbled, regenerate once with fewer words or overlay final text programmatically.

## Good prompt shape

```text
Create a beautiful premium illustrated capability map infographic for WhatsApp, square format, titled '<TITLE>'. Friendly but polished, warm dark background, luminous hand-drawn network map, a central helpful AI assistant orb connected to six capability islands. Make the text clean and readable. Include these exact capability labels if possible: '<label 1>', '<label 2>', ... Include a clear safety footer: '<footer>'. Elegant, human, not corporate, not generic SaaS, no clutter.
```

## Procedure

1. If replacing an already-sent WhatsApp image, delete/revoke the old media first using the messaging gateway delete workflow.
2. Generate via `scripts/generate_codex_image.py` with `--aspect square` and a stable path under `~/Downloads/` or the project asset directory.
3. Verify technical file details: PNG/JPEG exists, dimensions are appropriate, non-zero bytes.
4. Use `vision_analyze` or native vision to inspect legibility and check for misspelled labels/safety footer.
5. Only send after visual verification. If text is wrong, regenerate with fewer/shorter labels or produce a text-free visual and overlay exact text in code.
6. Send through `/send-media` with a short caption; report the new WhatsApp message ID.

## Notes

- The ChatGPT/Codex backend can produce surprisingly readable infographic text, but it is not guaranteed.
- For private capability maps, avoid implying the contact can do destructive/purchase/password/2FA actions. Keep the user-approval safety boundary visible.
