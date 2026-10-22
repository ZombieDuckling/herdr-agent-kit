---
name: 3d-print
description: Design 3D models and prepare print files for Bambu A1 mini
version: 1.0.0
platforms: [linux, macos]
metadata:
  hermes:
    tags: [3d-printing, cad, cadquery, bambu]
    category: fabrication
---

# 3D Print: parametric modeling and print preparation

Design a parametric 3D model from a chat conversation, show PNG previews,
iterate on user feedback, and — only after explicit confirmation — produce a
sliced 3MF file for a **Bambu Lab A1 Mini** (0.4 mm nozzle, Bambu PLA Basic,
0.20 mm Standard). The user copies the 3MF to a microSD card and prints.

The single source of truth for geometry is `model.py` — a CadQuery script in
the project workspace. Blender only renders previews; STL is an intermediate
export; the sliced 3MF is the final artifact.

## When to Use

- The user asks to design, model, or 3D-print an object ("сделай подставку…",
  "напечатай кубик…", "design a bracket…").
- The user asks to change or view an existing model from this conversation.
- Invoked explicitly as `/3d-print`.

Do NOT use for organic sculpting (figurines, faces): politely explain that
this pipeline targets functional parametric parts.

## Tools

1. `scripts/print3d` (this skill's dir) — pipeline CLI. Runs in a sandboxed
   Docker container; prints one JSON object to stdout; non-zero exit = error
   (2 usage/state, 3 model build failed, 4 slicer failed, 5 too big for
   printer, 6 render failed).
2. MCP tools `mcp_cadquery_*` (render / inspect / get_parameters / export) —
   fast, fileless geometry checks while drafting. They take the *code string*
   (read `model.py` and pass its content). Prefer `print3d` for anything the
   user receives; MCP `render` (SVG) is a fallback if PNG rendering fails.

Workspaces live on the host at `$HERMES_3D_WORKSPACES`
(default `/srv/hermes-3d/workspaces`); the same dir is `/work` inside the
containers. `print3d` always prints host paths — pass them to Telegram as-is.

## Procedure

### 1. New model
1. Only ask the user questions that are truly required (key dimensions,
   orientation). Assume sensible defaults and say what you assumed.
2. `scripts/print3d init` → note `project_id` and `model_path`. One physical
   object = one project; keep using the same project for all its edits.
3. Write `model.py` at `model_path` following `references/modeling-rules.md`
   (millimeters, named parameters on top, final shape in `result`).
4. `scripts/print3d inspect --project <id>` — must return `"ok": true`.
   If the build fails (exit 3): read the error, fix `model.py`, retry — at
   most 3 attempts, then tell the user plainly what didn't work. Never show
   a broken model.
5. Check `fits_printer` — the build volume is 180×180×180 mm. If false, warn
   immediately and propose scaling down or splitting.

### 2. Preview
1. `scripts/print3d preview --project <id>` (default view `iso`).
2. Send the PNG to the user with a short description: what it is, overall
   dimensions in mm, key parameters you chose.

### 3. Edit loop
1. Always modify the **existing** `model.py` — never start the model from
   scratch and never switch projects mid-object. Revisions are snapshotted
   automatically; old revisions must survive.
2. After every change: `inspect` → `preview` → send the PNG.
3. Extra viewpoints on request:
   `scripts/print3d views --project <id> --views back,top`
   (available: iso, front, back, left, right, top, bottom). Asking for a
   view alone never changes the model.

### 4. Confirmation gate
Slicing is allowed only after the user explicitly confirms the model is
final: «печатаем», «готовь к печати», «делай файл», "print it", "go ahead".
A compliment ("класс!", "выглядит отлично") is NOT confirmation. When unsure,
ask: «Печатаем, готовить файл?». Never slice proactively.

### 5. Prepare the print file
1. `scripts/print3d approve --project <id>` (refuses oversized models,
   exit 5 — then propose scaling down or splitting into parts; MVP has no
   auto-splitting).
2. `scripts/print3d slice --project <id>`. On success it already validated
   the 3MF (exit 0, `"ok": true`, existing non-empty ZIP with a 3MF payload).
3. Send the `three_mf` file itself to the user in Telegram, with a message in
   The user's language, e.g.:
   «Готово. Файл нарезан под A1 Mini · сопло 0,4 мм · Bambu PLA Basic ·
   слой 0,20 мм. Скопируй его на microSD и запускай печать.»
4. If any edit happens after approval, the approval is dropped automatically —
   re-approve after the user confirms again.

## Pitfalls

- **Never** run `slice` before explicit confirmation, and never send an STL
  as if it were a print file. If the slicer fails (exit 4): tell the user,
  mention that the model itself is safe, and check `slicer.log` in the
  project's `output/` dir.
- If `preview` fails twice (exit 6), fall back to MCP `render` (SVG) and tell
  The user the pretty render didn't come out; the model is intact.
- Don't promise mechanical strength, water-tightness or food safety.
- Avoid gratuitous complexity: heavy overhangs (>45°), thin walls (<1.6 mm),
  organic sculpting. See `references/modeling-rules.md`.
- Fillets are the most common CadQuery failure: if `fillet()` crashes the
  build, reduce the radius or drop the fillet, don't loop blindly.
- Printer/filament/process are fixed for MVP (see
  `references/printing-rules.md`); don't offer other materials or profiles.

## Verification

- Every `print3d` call: check exit code and the `"ok"` field of its JSON.
- After `preview`: the PNG path exists and is non-empty before sending.
- After `slice`: use the returned `three_mf` path; the CLI already verified
  the container structure and set project status to `ready`.
- `scripts/print3d status --project <id>` shows state, revision and files
  when in doubt (e.g. resuming an old conversation).
