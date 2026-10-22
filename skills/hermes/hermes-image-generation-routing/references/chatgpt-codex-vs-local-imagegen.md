# ChatGPT/Codex vs Local Image Generation Notes

## Session Learning

A user asked to generate an image via ChatGPT UI automation after Hermes `image_generate` failed because the active FAL provider lacked `FAL_KEY`. The better solution was not GUI automation: the Hermes install already had a bundled `plugins/image_gen/openai-codex` provider that uses ChatGPT/Codex OAuth to call the Codex Responses API `image_generation` tool and save the result locally.

Outcome verified in-session:

- `OpenAICodexImageGenProvider().is_available()` returned `True`.
- `generate(...)` returned `success: true`.
- Image saved under `~/.hermes/cache/images/openai_codex_gpt-image-2-medium_...png`.
- The image was delivered over WhatsApp with `MEDIA:/absolute/path.png`.

## Key Commands

Direct provider probe:

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
res = provider.generate('Create a polished square image, no text', aspect_ratio='square')
print(json.dumps(res, indent=2))
PY
```

Preferred config after verification:

```bash
hermes config set image_gen.provider openai-codex
hermes config set image_gen.model gpt-image-2-medium
```

Restart the gateway/session after changing config.

## Quality Comparison: GPT/OpenAI vs Free Local

Claude Haiku research in this session found the practical rule of thumb:

- **GPT/OpenAI image generation** is strongest for prompt adherence, text rendering, complex multi-object scenes, faces/people, editing/inpainting, and reliable client-facing work.
- **ComfyUI/local generation** is good enough for stylized art, backgrounds, avatars, concept art, and WhatsApp images that do not require exact text.
- **Local text rendering remains weak.** For local images needing labels/captions, generate without text and overlay text afterward with Pillow/Imagemagick.

## Recommended Routing for the user

1. Use `openai-codex` / GPT image generation when quality, text, or reliability matters.
2. Use ComfyUI/FLUX/SDXL locally when cost/privacy/offline/unlimited experimentation matters.
3. Use browser/UI automation only if the native provider path is impossible and the user specifically wants the ChatGPT web UI.

## Computer-Use Permission Fix

In this session `computer_use` was enabled but `cua-driver` was not installed. Installing it worked:

```bash
hermes computer-use install
```

After install, `hermes computer-use doctor` reported degraded state until macOS permissions were granted to **CuaDriver.app**:

```bash
hermes computer-use permissions status
hermes computer-use permissions grant
hermes computer-use doctor
```

Do not encode this as “computer-use is broken.” The durable lesson is the setup/permission sequence above.
