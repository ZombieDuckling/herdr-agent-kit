# Mining dashboard raster asset fallback

## Trigger
Use this workflow when a user asks for *new images* for an industrial/mining dashboard and the hosted image backend is unavailable or rate-limited.

## Lesson from session
- Do not stop at SVG/code assets if the user asked for images.
- Generate actual raster PNGs locally when needed.
- Use domain-specific imagery: rack hardware, ASIC boards, industrial textures, status-light accents.
- Wire the generated PNGs into the page immediately and verify the served HTML references them.

## Practical fallback flow
1. Create 1–3 PNGs sized for the target slots:
   - hero background / feature tile (landscape)
   - supporting hardware detail (square)
   - subtle texture / backdrop (landscape or square)
2. Prefer local code generation if external image APIs are unavailable.
3. Save assets under `public/assets/` with descriptive names.
4. Update templates/CSS to use the new raster files.
5. Verify:
   - `file` reports PNG image data
   - the live page references the new paths
   - the images read as industrial/practical rather than decorative or cinematic

## Prompt reminders for generated imagery
- industrial, utilitarian, mining-first
- dark navy / steel palette
- clean status indicators and hardware cues
- no luxury, lifestyle, car-wash, or cinematic photography language
- no text in the image itself
