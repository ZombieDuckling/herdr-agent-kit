---
name: hermes-image-generation-routing
description: "Choose and operate the best image-generation route for Hermes: built-in GPT/OpenAI providers, ChatGPT/Codex OAuth, local ComfyUI/free backends, or UI automation fallback."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [image-generation, hermes, openai-codex, chatgpt, comfyui, local-generation, whatsapp]
    category: creative
    related_skills: [hermes-agent, comfyui, macos-computer-use]
---

# Hermes Image Generation Routing

Use this skill when the user asks to generate images, compare image-generation options, make image generation work in Hermes, route around missing FAL/OpenAI API keys, or use ChatGPT/OpenAI/Codex/local ComfyUI to produce and deliver an image.

## Routing Decision

1. **Try the native Hermes `image_generate` tool first** when it is configured and available. It handles delivery-facing results cleanly and returns a URL or local path.
2. **If FAL is selected but `FAL_KEY` is missing, do not stop at “image generation unavailable.”** Check for alternate installed providers before falling back to external UI automation. Hermes may already have bundled image-gen providers under `plugins/image_gen/`.
3. **If the user has ChatGPT/Codex OAuth, prefer the bundled `openai-codex` image provider over driving chatgpt.com in the browser.** It routes GPT image generation through the Codex Responses API, requires no OpenAI API key, saves PNGs under `$HERMES_HOME/cache/images/`, and is much more reliable than GUI automation.
4. **Use local ComfyUI for free/unlimited generation** when cost/privacy/offline use matters and exact text rendering is not critical.
5. **Use UI automation only as a last resort** for ChatGPT image generation, because browser UI state, permissions, login prompts, and downloads are brittle.

## Quick OpenAI/Codex Provider Probe

When the normal tool is unavailable but Codex auth may exist, probe the provider directly from the Hermes repo venv:

```bash
~/.hermes/hermes-agent/venv/bin/python - <<'PY'
import sys, json
from importlib.util import spec_from_file_location, module_from_spec
sys.path.insert(0, '~/.hermes/hermes-agent')
p = '~/.hermes/hermes-agent/plugins/image_gen/openai-codex/__init__.py'
spec = spec_from_file_location('openai_codex_image_gen', p)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
provider = mod.OpenAICodexImageGenProvider()
print('available', provider.is_available())
res = provider.generate('A polished futuristic mascot image, no text', aspect_ratio='square')
print(json.dumps(res, indent=2))
PY
```

If `success: true`, deliver the returned local path with `MEDIA:/absolute/path.png`.

## Configuring Hermes to Prefer Codex Image Generation

If the direct provider works, configure Hermes image generation to use it in future sessions:

```bash
hermes config set image_gen.provider openai-codex
hermes config set image_gen.model gpt-image-2-medium
```

Restart the gateway/session after config changes. Use `gpt-image-2-low` for faster/cheaper iteration, `gpt-image-2-medium` for default WhatsApp quality, and `gpt-image-2-high` for highest fidelity when time/cost is acceptable.

## Local/Free vs GPT Quality Rule of Thumb

- **GPT/OpenAI image generation wins** for prompt adherence, readable text, complex scenes, faces/people, editing/inpainting, and client-facing reliability.
- **ComfyUI/local models win** for free unlimited experiments, privacy, offline use, stylized images, backgrounds, avatars, and images where text can be added separately.
- For local images that need readable captions, generate the image **without text** and overlay clean text with Pillow/Imagemagick before sending.

## Professional and social images of the user

For the user’s LinkedIn/professional posts, default to **clear infographics or diagrams only** unless they explicitly asks for another style:

- Use architecture diagrams, flow diagrams, threat models, control maps, trust-boundary diagrams, decision trees, and minimal explanatory layouts.
- Avoid generic AI-slop: cyberpunk decoration, fake glossy dashboards, stock-photo corporate imagery, fake humans, cinematic scenes, random abstract art, or luxury/founder-bro visuals.
- The image must map to the post’s exact technical concept. If it is only vaguely “security themed,” regenerate once with a stricter diagram/infographic prompt.
- Prefer no text when the image model may garble labels; if labels are needed, keep them short, large, and technically accurate.

## WhatsApp Delivery

After generating or downloading an image, verify the file exists and is a real raster image, then send:

```text
MEDIA:/absolute/path/to/generated.png
```

For images produced by the bundled OpenAI/Codex provider, paths usually look like:

```text
~/.hermes/cache/images/openai_codex_gpt-image-2-medium_YYYYMMDD_HHMMSS_xxxxxxxx.png
```

## UI Automation Pitfalls

If the user explicitly asks for UI automation through ChatGPT:

- First check whether a native provider can do the same job; mention if you used the more reliable provider instead.
- macOS computer-use requires `cua-driver`; install with `hermes computer-use install` if absent.
- Accessibility and Screen Recording permissions must be granted to **CuaDriver.app**. Use:
  ```bash
  hermes computer-use permissions status
  hermes computer-use permissions grant
  hermes computer-use doctor
  ```
- Do not click password, payment, 2FA, or permission dialogs. Stop and ask the user.

## References

- `references/chatgpt-codex-vs-local-imagegen.md` — session-derived notes on GPT/OpenAI vs local/free generation, and the Codex provider workaround.
