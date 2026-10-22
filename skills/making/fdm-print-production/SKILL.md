---
name: fdm-print-production
description: "Use when slicing/uploading/monitoring FDM print jobs."
version: 1.0.0
platforms: [macos, linux]
metadata:
  hermes:
    tags: [3d-printing, fdm, creality, klipper, moonraker, slicing, finishing]
    category: fabrication
---

# FDM Print Production

Use this skill when a task moves beyond CAD modeling into actual FDM production: selecting a printable artifact, slicing it with a real printer profile, uploading/starting a job, monitoring telemetry, or designing for a one-color finishing workflow.

This is the production companion to parametric CAD skills. The durable source remains the CAD file; the final printer action must be grounded in generated G-code, printer status, and visible or API telemetry.

## Core workflow

1. **Confirm the artifact and printer target.**
   - Identify the exact STL/3MF/CAD export to print.
   - Identify printer model, nozzle, filament/material, and bed envelope.
   - Confirm the material actually loaded or stated by the user before slicing; do not infer TPU just because a part would be better in TPU. For hard PLA/PETG contact parts, loosen fit and warn about scratch/binding risk before starting.
   - For thin cards/tokens, verify mesh dimensions from vertices or slicer metadata, not just the CAD constants.

2. **Slice before upload.**
   - Do not upload raw STL to Moonraker/Klipper as a print job.
   - Use the installed slicer CLI or GUI profile to produce G-code.
   - On the user's Mac, Creality Print CLI is `/Applications/Creality Print.app/Contents/MacOS/CrealityPrint`. For K1C 0.4 mm slicing, useful profile files are under `/Applications/Creality Print.app/Contents/Resources/profiles/Creality/`: `machine/Creality K1C 0.4 nozzle.json`, `process/0.20mm Standard @Creality K1C 0.4 nozzle.json`, and for Ender PLA `filament/Ender-PLA @Creality K1C 0.4 nozzle.json`.
   - If a MakerWorld/Bambu 3MF fails with `File Version ... not supported by current cli version`, treat it as a project container: unzip it, extract `3D/Objects/*.model`, convert the 3MF mesh triangles to STL, then slice the STL with the local printer/filament profiles. Do not upload the 3MF or raw STL as the print job.
   - Keep revised slices in versioned output folders when a previous/active print exists; never overwrite the G-code currently being printed or monitored.
   - Before starting any job, explicitly inspect and report print orientation, support state, overhang/bridge handling, brim/adhesion, material profile, and object height from the G-code or slicer metadata — the user expects proof that the print was prepared, not merely sent.
   - For hollow caps, sleeves, cups, and end covers, orient the closed face on the bed and the open side upward whenever practical. This avoids internal supports inside the cavity; create a print-oriented wrapper/export if the source CAD's modelling axes do not already put that face on Z=0, then verify the oriented STL `z_min == 0` before slicing.
   - **Verify orientation numerically before slicing, not by eyeballing a preview.** Parse the STL and check three numbers: downward-facing planar area sitting on Z=0 (that is the bed contact), downward-facing area on the top plane (a non-zero value means an internal ceiling — the cavity opens downward and needs support), and downward-facing area that is neither at Z=0 nor the top (the true overhang budget). `scripts/stl_inspect.py <file.stl>` reports extents, volume, contact area, top-plane test, overhang split, component count and non-manifold/boundary edges in one pass; run it before every slice.
   - **Placement requests are verified from the G-code, never from the preview.** When the user asks for a part centred on the plate, translate the mesh so its XY bounding-box centre lands on the bed centre (110,110 on a 220x220 machine), export a centred STL, and slice with `--arrange 0` — auto-arrange re-places geometry and silently discards the shift. Then prove it by parsing the min/max X and Y of the `G0/G1` moves in the produced G-code and requiring both centres to equal 110.0; report those two numbers instead of saying it looks centred.
   - For snap-fit or contact parts touching valuable objects, call out material risk before starting: TPU is preferred for soft contact; hard PLA/PETG may scratch or fit too stiffly unless the design has deliberate clearance.
   - When the user asks to minimize visible layer lines, reslice with the finest valid printer/nozzle process profile before upload/start, then report the time and layer-count tradeoff against the standard slice. For the K1C 0.4 mm profile, prefer `process/0.08mm Standard @Creality K1C 0.4 nozzle.json` when surface finish matters and geometry permits it.
   - Record slicer, printer profile, material profile, nozzle/bed temperature, layer count, estimated time, and filament mass.

3. **Probe printer state read-only before control.**
   - Confirm the printer is reachable and idle/ready.
   - Confirm no active `virtual_sdcard` file and no active print.
   - Confirm temperatures are sane before starting.
   - If bed occupancy is uncertain and no camera/frame is available, state that limitation before starting.

4. **Upload and start with the printer API only after a valid G-code exists.**
   - For Moonraker: use `/server/files/upload` and `/printer/print/start`.
   - Confirm the uploaded path with `/server/files/metadata` before start.
   - Some implementations store files under a nested path if both `path` and filename are supplied; start the exact path returned by upload/metadata.
   - Send the start as a POST that carries a JSON content-type and an empty body: `curl -s -H "Content-Type: application/json" -d '{}' -X POST "http://<printer>:7125/printer/print/start?filename=<exact-path>"`. A bare `curl -X POST` carrying no body is refused with `411 Length Required` and the printer stays in `standby`, so always send the empty body (`-d ''`); the response body is not the proof of success — re-query `print_stats` and require `state=printing` with the expected `filename` before reporting a start.

5. **Monitor after start.**
   - Poll `print_stats`, `virtual_sdcard`, `extruder`, `heater_bed`, and `toolhead`.
   - Treat `state=printing` during heating as not yet proof of extrusion; wait until `print_duration`, `filament_used`, or file progress advances.
   - For planned manual swaps, hand off a background monitor with a watch/notification on the pause condition, then verify `pause_resume.is_paused=true` before telling the user to change filament; the printer may report “printing” through heat-up and calibration long before the swap point.
   - Continue monitoring until completion/error or hand off a background monitor.
   - Start a hand-off monitor with `persist_on_release=true`, otherwise it is killed when the session closes and you lose the completion signal. If the monitor was killed anyway, recover the outcome from `/server/history/list` (status `completed`/`error`, duration, filament used) instead of re-printing or guessing from a reset `print_stats`.

6. **Use camera evidence when available, but do not fake it.**
   - Camera URLs may be WebRTC, MJPEG, RTSP, or vendor-specific.
   - If camera capture returns a black frame or handshake-only result, report telemetry separately from visual confirmation.

## Slicer and firmware capability checks

When the question is "does slicer X work with my printer" or "can the printer do feature Y" (non-planar
layers, wave overhangs, 5-axis toolpaths), check both halves and prove the machine half on the hardware
itself — vendor pages only speak for the slicer:

- Slicer half: their printer page plus whether OrcaSlicer ships that model's profile. A slicer that
  ships OrcaSlicer's profiles inherits its whole printer list, so an existing Orca profile answers the
  question. (K1C is a K1 variant and OrcaSlicer has K1C profiles.)
- Machine half, read from the printer API: `configfile.settings.printer.kinematics` must be `corexy`
  (a bed-slinger moves the part, so curved layers become impractical), and `max_z_velocity` /
  `max_z_accel` set the real ceiling — Z at 10 mm/s against XY at 600 mm/s means a sloped toolpath can
  only run at `max_z_velocity / sin(slope)` speed, so steep curves crawl unless the config is raised.
- Then prove it live: home, lift off the bed, run a simultaneous X/Y/Z move through
  `/printer/gcode/script`, and read `toolhead.position` back. An HTTP 200 is not proof; the moved
  position is.
- Acquisition is often the real blocker — account-gated download pages, GitHub releases with zero
  assets, no Homebrew cask. Check the gate before promising an install.
- Non-planar on an Orca-derived slicer (Unlayered) is gated on the *object* carrying cut
  planes, not on the printer setting: the engine branches on
  `enable_nonplanar && (cut_planes.active() || object_has_directed_parts)`. So a CLI slice of a
  plain STL is byte-identical to a planar one apart from header comments (`enable_nonplanar = 1`,
  `axis_selection = virtual`) however the machine preset is authored — the user sees an ordinary
  print and says so. Options: author planes in the GUI Cut Planes/Skeleton tool, or inject them
  headlessly into the project at `Metadata/cut_planes.xml` (schema: `<objects><object id="1"
  enabled="1"><plane px py pz nx ny nz/></object></objects>`; a plane's normal is the build
  direction of the chunk beyond it), set `print_sequence = by group`, and keep every chunk's tilt
  inside the machine's limit — the slicer refuses steeper build directions outright and names the
  angle it allowed. Auto-generated skeleton planes are often too steep to be usable; one gentle
  plane is what demonstrates the feature. Recipe and evidence:
  `references/unlayered-nonplanar-cut-planes.md`.
- Prove the *feature*, not the machine. Simultaneous XYZ motion says the firmware could execute a
  curved toolpath; only the produced G-code says the slicer emitted one. Parse the toolpath for the
  feature itself (for non-planar: Z coordinates on extruding moves *inside* a layer) before claiming
  it — a slicer can be flag-set for non-planar and still emit a byte-identical planar slice, header
  comments included. Feature gates and the parse snippet: `references/slicer-and-firmware-capability-checks.md`.

Exact commands, the request shape that silently fails, and the clearance limits:
`references/slicer-and-firmware-capability-checks.md`.

## Design-for-finish rules

For one-color prints that will be paint-marker highlighted:

- Model raised paintable surfaces and recessed protected detail intentionally.
- For QR codes on black PLA with a gold marker, prefer a raised gold-paintable field with recessed black QR modules, not same-color raised modules.
- Verify the QR payload from the generated source matrix and, where possible, a black-on-gold scan simulation.
- Bronze/silk/metallic single-color PLA can look premium, but QR reliability still requires contrast.

## Verification checklist

Before saying a print started:

- G-code file exists and is non-empty.
- Slicer metadata matches the intended printer/material.
- Print orientation is named and appropriate for the geometry and gravity, not just for how the part is used: broad/flat faces should usually sit on the bed, inward lips should not become unsupported bridges, and watch/cover/protector parts may print better face-down even when used face-up.
- Support setting is named; if supports are off, state why the geometry can print without them and identify any intentional short bridges.
- When the print exists to demonstrate a slicer feature (non-planar layers, wave overhangs), that feature is verified in the G-code before upload — otherwise you print the ordinary version and the user reports it back to you.
- Overhang/bridge/brim settings are checked from the G-code or slicer metadata before starting, and user-visible uncertainty is reported before printing.
- Printer API says ready/idle before start.
- Upload returns a path and metadata confirms the same path.
- Start endpoint returns success.
- Follow-up telemetry shows actual progress or extrusion, not merely preheating.

## References

- `references/creality-k1c-moonraker-direct-control.md` — tested direct-control workflow for a Creality K1C exposing Moonraker/Nexusp.
- `references/manual-filament-swap-contrast-cards.md` — two-color contrast card workflow with explicit pause insertion, monitoring, and resume checks.
- `references/one-color-paint-marker-qr-cards.md` — one-color business card/QR design pattern for black PLA plus gold marker or bronze PLA.
- `scripts/stl_inspect.py` — STL print-readiness inspector: extents, volume, bed-contact area, cavity-opening direction (top-plane test), overhang budget, per-part split, component count, manifold/boundary-edge check. Use it to prove orientation before slicing.
