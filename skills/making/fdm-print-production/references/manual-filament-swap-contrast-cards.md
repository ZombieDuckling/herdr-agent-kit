# Manual filament-swap contrast cards

Use this when a flat card/token needs readable text or a scannable QR but the printer has no AMS/CFS.

## Proven pattern

For small business-card-style pieces, one-color relief is often not enough. If the user reports black-on-black recessed/raised detail is illegible, switch to a **two-stage contrast print**:

1. Print the base in the currently loaded color.
2. Insert a manual `PAUSE` immediately before the first raised-detail layer.
3. User swaps filament to the contrast color and purges until the old color is gone.
4. Resume and print only the raised detail layer(s).

This can be inverted without re-slicing geometry: if white is already loaded, print a white base first and swap to black for raised detail.

## Geometry rules for FDM legibility

- Treat tiny URL/footer text as high risk. On a 0.4 mm nozzle, `2.2 mm` high raised URL text was not readable in a real print; enlarge to about `3.0 mm+` and remove decorative motifs that compete for space.
- Split long email addresses or URLs across two lines instead of forcing one tiny line; two larger block lines are more readable than one narrow continuous string.
- Keep important text chunky, bold, and raised by at least 2–3 layers (`0.4–0.6 mm` at 0.2 mm layer height, or equivalent physical height on finer layers).
- Prefer blocky typography and iconography for raised card detail; thin or decorative letterforms round over and disappear at wallet-card scale.
- Do not waste printable detail space on small decorative line art until all required text is legible.
- Verify a top-view preview for clipping before slicing; rendered text can look contained in CAD constants but clip visually.

## QR pattern that worked better

For contrast QR on a two-color card:

- Print the base in the dark color and a raised light QR field on top.
- Model dark QR modules as cutouts through the raised light field so the base color shows through; if the pause happens before the QR geometry, all non-cutout QR geometry will become the swap color and may scan poorly as gold-on-gold relief.
- Verify the final intended visual pattern, not only the source QR: generate a black/base-on-gold/swap-color contrast simulation from the same mask that drives the STL and decode that before slicing.
- Prefer a short redirect URL for FDM business-card QR codes: fewer modules and larger module pitch scan better than dense direct URLs.
- For wallet business cards, default to true credit-card footprint `85.60 × 53.98 mm` unless the user explicitly wants oversized; keep thickness near `1.2 mm` base plus `0.4–0.6 mm` raised contrast detail.
- If the run is inverted, the same geometry gives a light base with dark raised field/cutouts inverted visually; acceptable for a test run if the user approves.
- Treat the printed QR as needing human/photo verification after the physical print.

## High-detail slicing for raised text and QR

When a 0.4 mm-nozzle card has small raised text or QR modules near the practical limit, create a separate high-detail process profile rather than reusing a fast standard profile:

- Use a fine layer height around `0.08–0.12 mm` for the raised detail job.
- Reduce line widths where the slicer supports it, e.g. about `0.36–0.38 mm` for outer/top detail while keeping the first layer wider for adhesion.
- Slow visual/detail paths: outer walls around `35 mm/s`, top surfaces around `30 mm/s`, and small perimeters around `20 mm/s` are a safer starting point than high-speed K1 defaults.
- Keep supports and brim off for flat wallet cards unless warping demands otherwise; brim cleanup can damage edges and make the card less wallet-friendly.
- Expect print time to increase sharply; report the time tradeoff as the cost of readable text and QR fidelity.

## Pause insertion procedure

For a base thickness of `1.20 mm` and `0.20 mm` layers:

- Base layers end at `Z=1.20`.
- Insert pause before the first layer above the base, typically `Z=1.40`.
- Confirm the G-code has exactly one intended color-change `PAUSE` block and a unique marker/comment around it; do not rely on a stale marker name from an older insertion script, because the validation can falsely report “missing pause” while the current G-code uses a different marker such as `GOLD_SWAP_BEGIN`.
- Inspect the lines before and after the pause and confirm the next motion/extrusion belongs to the raised-detail section; slicers may not preserve a neat `;LAYER_CHANGE` immediately after an inserted pause.

Example pause block:

```gcode
; HERMES_MANUAL_COLOR_CHANGE_START
; Base is complete. Swap filament to CONTRAST COLOR now, then RESUME.
M400
M117 Swap filament then RESUME
RESPOND TYPE=command MSG="Swap filament for raised text, URL, and QR, then RESUME"
PAUSE
; HERMES_MANUAL_COLOR_CHANGE_END
;LAYER_CHANGE
;:1.4
```

## Monitoring the swap

After starting the job, monitor until extrusion/progress is confirmed; heat-up/calibration can leave `print_duration=0` and `filament_used=0` for several minutes. For a hands-off swap alert, run a background monitor that polls `pause_resume`, `print_stats`, `virtual_sdcard`, `extruder`, `heater_bed`, and `toolhead`, and notifies on the pause condition. Before telling the user to swap, re-check that `print_stats.state` is `paused` or `pause_resume.is_paused=true`, and report nozzle/bed temperature plus whether `can_extrude` is true. If the pause lowered the nozzle target but the nozzle is still hot and `can_extrude=true`, tell the user to swap and purge immediately; if it cooled too far, heat back to the filament print temperature before purging/resume.

## Moonraker/Klipper resume pitfall

On the K1C/Moonraker path used here, `/printer/print/resume` returned an empty body and did not always unpause. The reliable recovery was:

1. Check current pause state and nozzle target.
2. If the pause cooled the nozzle, run `M104 S220` (or the material’s print temp) and wait until `can_extrude=true` and temperature is near target.
3. Resume via direct G-code script:

```json
{"script":"RESUME"}
```

posted to `/printer/gcode/script`.

After resume, verify actual motion/progress: `state=printing`, `pause_resume.is_paused=false`, increasing `print_duration`/`filament_used`, and `Z` on the detail layer.
