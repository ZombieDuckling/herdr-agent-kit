---
name: image-generation-freely
description: Use whenever a task could use any visual asset - website or app work, UI, landing pages, hero art, backgrounds, logos, icons, textures, illustrations, placeholders, social images, slides, docs. Agents generate such assets freely and on their own, after checking the asset does not already exist.
---

# Generate images freely - after checking they do not exist

The user's rule: never ask permission for an image, and never ship a bare page for want of one. Generate
what you need, as you go, and generate plenty. The one gate: first confirm it does not already exist.

## 1. Does it already exist? (do all four, fast, before every generation)

    ls assets public images media static src/assets 2>/dev/null          # project folders
    git log --all --name-only --format= -- '*.png' '*.jpg' '*.jpeg' '*.webp' '*.svg' | sort -u | head -80
    find . -path ./node_modules -prune -o -iname '*<keyword>*' \( -name '*.png' -o -name '*.jpg' -o -name '*.webp' -o -name '*.svg' \) -print
    pdfimages -list <supplier.pdf>                                       # PDFs/packs the project holds (pdfimages -png to extract)
    codex-image --find "<keyword> <keyword>"                             # shared registry of everything any agent generated

Also check the project's CMS / asset library if it has one (e.g. its media tools or upload folder).
Found something? Reuse it. Found something low-res or damaged? Restore/upscale it with `--ref` instead
of generating from scratch. Found nothing? Generate.

## 2. Generate

    codex-image --prompt "<labelled build spec>" --out <path>.png --aspect square|landscape|portrait \
                [--ref a.png --ref b.png] [--model gpt-image-2-low|medium|high]

- Backend: gpt-image-2 through the ChatGPT/Codex sign-in. No API key. Prints one JSON line; exit 0 only if written.
- `--ref` (repeatable) = edits, recolours, restyles, restoration, upscales, "same style as this".
- Models: `low` for drafts, placeholders and bulk; `medium` (default) for normal assets; `high` for restoration and hero images.
- ~40 s per image. Run 5-6 in parallel (separate `--out` files, background jobs); do not exceed that.
- Prompt as a labelled spec: Subject / Style / Composition / Palette / Background / What to avoid. No text in the image.
- The skill `image-generation-workflow` (in this kit: `~/.herdr-agent/kit/skills/assets/image-generation-workflow`) has fuller prompt guidance; `scripts/generate_image.py` also routes here via `IMAGE_BACKEND_CMD`.
- Every success is logged to ~/.cache/agent-images/index.jsonl with a copy by hash, so later agents find it with `--find`.

## 3. Verify and place

    python3 ~/.herdr-agent/kit/skills/assets/image-generation-workflow/scripts/verify_image.py <file>

Look at the picture if you have vision (reject warped hands/logos, stray text, wrong aspect). Save into
the project's own asset folder (public/images, assets/, ...) with a descriptive name; if there is none,
use `<workdir>/generated/`. Convert to WebP afterwards when a site needs it (`cwebp` or `sips`).

## 4. Rules

- Never render critical text (prices, names, legal) inside an image; set it in HTML/text.
- Never imitate a real brand, logo or person.
- A generated image never stands in for a real product photo unless your report says so.
- A project's own rules (CLAUDE.md, brief) override this skill when they forbid something.
- Do not drive chatgpt.com in a browser, and never work around a bot check.
- If codex-image fails ("Codex sign-in not available"), say so in your report; do not loop.
