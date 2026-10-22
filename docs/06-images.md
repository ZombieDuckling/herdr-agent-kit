# Images

Agents should make the images they need (hero art, icons, textures, illustrations, placeholders)
themselves, as they work, instead of leaving grey boxes. The `image-generation-freely` skill says when;
`image-generation-workflow` says how, and above all how to **verify** the file.

## Before generating: reuse

1. Search the project (`assets/`, `public/`, `images/`), its CMS, and any supplier packs or PDFs.
2. Search the shared registry of images other agents already made: `codex-image --find "<words>"`.
3. Upscale or restore an existing image (`--ref`) before generating a new one.

## Backends (the kit uses the first that works)

| Backend | Setup | Notes |
|---|---|---|
| **Hermes + Codex sign-in** (`codex-image`) | Install Hermes Agent, run `hermes auth codex` | No API key; uses your ChatGPT/Codex sign-in |
| **OpenAI-compatible images API** | `export IMAGE_API_KEY=...` (or `OPENAI_API_KEY`) | `scripts/generate_image.py` in the workflow skill |
| **Any command** | `IMAGE_BACKEND_CMD='my-gen --prompt {prompt} --out {out}'` | ComfyUI, a local model, anything |
| **None** | | Agents use SVG, CSS shapes and real photos instead; no fake images |

```sh
codex-image --prompt "<labelled spec>" --out public/img/hero.png --aspect landscape
python3 ~/.herdr-agent/kit/skills/assets/image-generation-workflow/scripts/verify_image.py public/img/hero.png
```

## Hard rules

- **Verify every file** with `verify_image.py` (it rejects HTML saved as .png, empty files, wrong sizes)
  and look at it if the agent can see images.
- **No text inside images.** Put words in HTML, where they are readable and translatable.
- **No real brands or people.**
- **Never present a generated image as a real photo** of a real business, product or person. Say in the
  report which images are generated.
- **Real photos first** for real businesses. Convert to WebP and add `srcset` sizes for the web.
- The project's own rules win (for example a ban on stock imagery).

Next: [quality](07-quality.md).
