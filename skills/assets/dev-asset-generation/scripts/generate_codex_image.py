#!/usr/bin/env python3
"""Generate an image with Hermes' OpenAI-Codex image provider.

Usage:
  python <this skill>/scripts/generate_codex_image.py \
    --prompt "Text-free hero image for a cybersecurity SaaS" \
    --aspect landscape \
    --out ./public/assets/hero.png
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def _default_repo() -> Path:
    home = Path(os.environ.get("HERMES_HOME", "~/.hermes")).expanduser()
    return Path(os.environ.get("HERMES_REPO", str(home / "hermes-agent"))).expanduser()


def _load_provider(repo: Path):
    plugin = repo / "plugins" / "image_gen" / "openai-codex" / "__init__.py"
    if not plugin.exists():
        raise SystemExit(f"openai-codex image plugin not found at {plugin}")
    sys.path.insert(0, str(repo))
    spec = spec_from_file_location("hermes_openai_codex_image_gen", plugin)
    if spec is None or spec.loader is None:
        raise SystemExit(f"Could not load plugin spec from {plugin}")
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.OpenAICodexImageGenProvider()


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a dev asset image through Hermes OpenAI-Codex auth")
    parser.add_argument("--prompt", required=True, help="Image prompt. Prefer no exact text; overlay text separately.")
    parser.add_argument("--aspect", default="square", choices=["square", "landscape", "portrait"], help="Output aspect ratio")
    parser.add_argument("--out", required=True, help="Destination image path, usually under public/assets or src/assets")
    parser.add_argument("--repo", default=str(_default_repo()), help="Hermes repo path containing plugins/image_gen/openai-codex")
    args = parser.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    out = Path(args.out).expanduser().resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    provider = _load_provider(repo)
    if not provider.is_available():
        raise SystemExit("OpenAI-Codex image provider is not available. Run `hermes auth add openai-codex` / `hermes setup` first.")

    res = provider.generate(args.prompt, aspect_ratio=args.aspect)
    if not res.get("success"):
        print(json.dumps(res, indent=2), file=sys.stderr)
        raise SystemExit("Image generation failed")

    src = Path(res["image"]).expanduser().resolve()
    if not src.exists() or src.stat().st_size <= 0:
        raise SystemExit(f"Provider reported missing/empty image: {src}")

    shutil.copy2(src, out)
    print(json.dumps({
        "success": True,
        "image": str(out),
        "source": str(src),
        "bytes": out.stat().st_size,
        "provider": res.get("provider"),
        "model": res.get("model"),
        "aspect_ratio": res.get("aspect_ratio"),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
