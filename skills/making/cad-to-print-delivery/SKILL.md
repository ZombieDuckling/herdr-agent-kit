---
name: cad-to-print-delivery
description: Use when delivering CAD/STL/G-code to a printer.
version: 1.0.0
platforms: [macos, linux]
metadata:
  hermes:
    tags: [cad, 3d-printing, openscad, slicer, moonraker, klipper, finishing]
    category: fabrication
---

# CAD to Print Delivery

Use this skill when the user asks for a physical 3D-printable object and expects a working artifact, not a pretty mesh preview. It covers source-first CAD, slicer verification, finishing-aware details, and safe direct printer control when available.

## Core principles

1. **Start from the mating/interface requirement.** If the object must fit existing hardware, measure or parameterize the interface before modelling decoration.
2. **Keep source CAD as truth.** Use OpenSCAD/CadQuery source files with top-level parameters; STL is an export, not the editable artifact.
3. **Verify geometry at every boundary.** Export STL, inspect mesh dimensions, then check slicer-reported dimensions/profile metadata.
4. **Design for the finishing workflow.** One-color prints, paint markers, filament swaps, embossing, engraving, and QR scanability change the geometry.
5. **Do not print from STL directly.** Printers execute G-code/3MF workflows; direct printer APIs usually upload/start sliced G-code, not raw CAD meshes.

## Standard workflow

1. Load any domain-specific CAD/printing skill already available.
2. Create a project directory with:
   - `model.scad` or `model.py`;
   - `README.md` with assumptions, dimensions, print orientation, and export commands;
   - `exports/` for STL/PNG/3MF/G-code outputs.
3. Model in millimetres. Put critical user-adjustable values at the top. For fit-critical accessories around valuable objects such as watches, phones, camera gear, or tools, separate **known measured dimensions** from **assumed first-fit dimensions** in the source and README; use public specs only to seed a prototype, then ask for caliper measurements before calling it final.
4. For reverse-engineered photographed parts, establish measurement truth before modelling details:
   - Prefer calipers; otherwise make a calibrated A4/ArUco capture sheet and require all four markers visible, then rectify by homography into millimetres.
   - Match contrast to the part: white plastic belongs on a black placement panel; white-on-white grid photos make the printed sheet segment as the part and hide edges.
   - Capture separate top, underside/peg, and side/thickness views. If a hand blocks markers or features, use that image only for qualitative orientation, never measurement.
   - Treat shallow circular marks on molded plastic as injection artifacts unless the user confirms they are functional holes/recesses; model the main body and pegs first. Sink marks, ejector-pin witness marks, gate vestiges and weld lines run 0.04-0.38 mm deep - the same order as the features being sought - so an artifact detector will read them as geometry. Acceptance standards treat them as cosmetic, not as drawing dimensions: omitting them is fidelity to the spec, not lost detail.
   - Separate functional from decorative dimensions explicitly in the source and README. Features that mate with another part (pegs, bores, engagement length, wall thickness at the interface) must be measured with instruments; outline, finish and cosmetic recesses may come from the calibrated photo. Never let a photo-derived peg diameter stand in for a caliper reading.
   - A calibrated planar capture only measures features coplanar with the sheet. Any raised feature is recorded as a projection, so its apparent size shifts with height and viewing angle; measure raised features physically instead of trying to segment them out of the image.
   - Measure the mating component, not the replica, for every fit dimension - bore/barrel diameter, engagement depth, peg pitch. A photo can never supply the mate's dimension, and copying the original feature exactly is the standard cause of an assembly that will not fit once print shrinkage and clearance are applied.
   - Keep measured and guessed values explicit in CAD comments. Expose uncertain peg diameter, pitch, offsets, thickness, clearance, and locator-wall dimensions as parameters.
   - For mating components, create a separate fit variant rather than overwriting the clean replica; use known component dimensions as a low locator/cradle/clearance envelope and keep the original plate recoverable.
   - When the user rejects the current object as the wrong target, stop iterating that artifact and reset the CAD scope to the named subcomponent. For example, switch from a whole mating component or bracket to a standalone end cap/sleeve if that is what the user asks for; preserve the rejected variant as a separate file rather than deleting or silently morphing it.
   - For standalone end caps or sleeves, model the fitted internal opening first from the mating component dimensions plus explicit clearance, then add wall/front thickness, depth, notches/relief slots, and printable orientation. Do not model the full mating component when the deliverable is only the cap.
5. For wearable/contact accessories, design the print orientation and fit loop together: first ensure the part works with gravity during printing, then ensure it covers/clips around the whole physical interface. A part that fits the CAD silhouette can still fail if an inward lip becomes a bridge, a large C-gap prevents retention, or hard material cannot flex. The user expects this reasoning before printing, not after failed parts.
6. Export preview images and STLs. If the primary CAD exporter stalls or cannot complete, switch to a source-first fallback such as a small `model.py` mesh generator rather than delivering only a picture; keep the editable source and regenerate the STL from it. For styling requests, use printable integrated geometry such as broad raised inlays, ribs, scallops, or engraved fields; avoid fragile overlapping decorative meshes and re-check manifoldness after adding decoration.
6. Parse the exported STL or use slicer metadata to confirm dimensions. For generated meshes, also verify manifoldness by counting STL/mesh edges: every undirected edge should appear exactly twice; report and fix boundary or non-manifold edges before delivery.
6. If the user asks to test print, slice with the correct printer/material profile and inspect G-code metadata: printer, layer height, nozzle/bed temps, time, filament, object height.
7. If direct printer control is requested or useful:
   - discover the printer from slicer config, mDNS/ARP, or known LAN ranges;
   - probe read-only status endpoints first;
   - verify printer is `ready`/idle, temperatures are safe, and no print is active;
   - upload G-code with `print=false` first;
   - verify metadata for the uploaded remote path;
   - start only the verified remote filename;
   - poll until heating/progress/extrusion confirms the job actually started.

## Safety gates

- Never click through physical-printer warnings blindly.
- Do not start a print if the printer reports an active print, paused/error state, or unknown state.
- If you cannot inspect the bed/camera, say so. Starting is acceptable only when the user explicitly asked and printer API status is clean; the human still owns bed-clearing/filament reality.
- Stop or pause a printer only when the user asks or an API-reported error makes continued operation unsafe.
- Treat nozzle/bed heating and motion as real-world side effects.

## Finishing-aware design

For one-color black PLA with a metallic paint marker:

- make paintable features raised and broad enough for a chisel-tip marker;
- avoid tiny raised same-color QR modules;
- for QR codes, make a raised paintable light/metallic field and recessed dark cells that stay unpainted;
- generate and decode a flat contrast simulation of the intended final appearance.

For bronze/gold/copper PLA-only:

- design for visual texture and relief;
- do not promise reliable QR scanning unless there is added contrast.

See `references/one-color-painted-qr-cards.md` for the detailed QR/card pattern.

For watch protectors, stands, and display accessories, see `references/watch-accessories.md` before slicing or starting a print.

For Autodesk A360/Fusion public-share links that need technical specs or drawing packs, see `references/autodesk-a360-technical-packs.md`. Always separate source-derived facts from approximate viewer-mesh estimates, and include qualitative load/stress points for mounts, brackets, and structural parts.

## Crude scan / zero-thickness STL rescue

When the user supplies a scanned or repaired STL and says it is already scaled, do not pivot into dimension discovery or drawing-pack work unless asked. Preserve the STL coordinate scale and make the requested printable artifact directly.

For a 0 mm shell or surface scan that needs thickness:

1. Copy the source STL into a working/output folder; never overwrite the upload.
2. Inspect mesh basics with `trimesh.load_mesh(..., force='mesh')`: vertices, faces, extents, watertightness, winding consistency, and boundary-edge count.
3. Add the requested thickness at the existing scale. For practical rescue work, create two variants when the correct offset direction is uncertain:
   - Z/extruded thickness, best when the scan represents a flat plate/silhouette;
   - normal-offset thickness, best when the scan has real curved surface shape.
4. Build sidewalls around boundary edges after duplicating the surface, then export STL variants plus a short JSON report. Count boundary edges again; prefer the variant with fewer open edges and clearer print intent.
5. If hole filling requires an unavailable dependency or extra install approval, still deliver the thickened STL variants if they materially improve printability; report remaining open edges plainly and offer a watertight repair pass after approval. Do not present non-watertight output as fully verified.
6. For the user's rough rescue parts, prioritize a usable thickened mesh over perfect CAD reconstruction when they say sanding/rough cleanup is acceptable.

## Reverse engineering from photographs

For the accuracy hierarchy, calibration rules, artifact-vs-feature test, and the fit-compensation numbers to encode as parameters, see `references/photo-to-cad-reverse-engineering.md`. Report the achievable error of each route before promising a fit, and state the printer's own tolerance budget as the floor for anything finer.

## Verification checklist

Before final response, report what actually happened:

- source file path;
- exported STL/preview paths;
- measured STL dimensions and, for source-generated meshes, whether edge/manifold checks passed;
- for scan-rescue thickening, requested thickness, generated variants, boundary-edge/watertight status, and which file to try first;
- any assumed fit dimensions that need real-world caliper confirmation before final print;
- material-specific fit decisions, especially when PLA/PETG is used where TPU would be safer for contact;
- slicer profile/material/settings if sliced;
- upload/start result if direct control was used;
- printer state/progress after starting if a test print was launched.
