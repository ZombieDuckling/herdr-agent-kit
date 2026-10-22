# Manual filament-swap contrast cards

Session learning for CAD-to-print delivery of business-card/token style objects with readable text and QR codes on a single-extruder FDM printer.

## When to use

Use this pattern when one-color black/bronze/same-color relief cannot make small details readable or scannable. A manual color swap is a better physical manufacturing strategy than endlessly deepening relief.

## CAD pattern

- Single-piece model: no glued halves unless the user explicitly asks.
- Base prints first in color A.
- Raised details print second in color B after a pause.
- Put all detail geometry above a clean base split, e.g. `base_t = 1.20 mm`, `detail_h = 0.40–0.60 mm`.
- For QR: make a raised contrast field and cut out the QR modules so the base color shows through.
- Keep text bold; avoid thin scripts and tiny decorative motifs.
- Real-world result: a `2.20 mm` high URL was not readable on a 0.4 mm nozzle; enlarge URL/footer text to around `3.0 mm+` and remove decorative filler.

## Print/G-code pattern

For 0.20 mm layers and a 1.20 mm base:

- Base ends at `Z=1.20`.
- Insert a single `PAUSE` before `Z=1.40`, immediately before the raised detail layer starts.
- Verify the G-code has exactly one pause block and the following layer marker is the intended detail layer.

Example:

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

## Operational pitfall

On the tested Creality K1C/Moonraker workflow, the printer may cool the nozzle while paused and `/printer/print/resume` may return an empty response without unpausing. Reliable sequence:

1. Query `print_stats`, `pause_resume`, and `extruder`.
2. If nozzle target dropped, send `M104 S220` or the material's printing temp through `/printer/gcode/script`.
3. Wait for `can_extrude=true` and temperature near target.
4. Send `RESUME` through `/printer/gcode/script`.
5. Verify `state=printing`, `pause_resume.is_paused=false`, progress/filament increase, and Z is on the detail layer.

## Human handoff

If the user says the wrong color is already loaded, do not block unnecessarily. You can invert the run: print the base in the current color, patch the pause prompt to request the opposite color, and proceed if the user accepts the inverted colorway.
