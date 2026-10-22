#!/usr/bin/env bash
set -euo pipefail

if [[ -n "${OPENSCAD_BIN:-}" ]]; then
  if [[ -x "$OPENSCAD_BIN" ]]; then
    printf '%s\n' "$OPENSCAD_BIN"
    exit 0
  fi
  printf 'OPENSCAD_BIN is set but is not executable: %s\n' "$OPENSCAD_BIN" >&2
  exit 2
fi

if command -v openscad >/dev/null 2>&1; then
  command -v openscad
  exit 0
fi

candidates=(
  "/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD"
  "/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD"
  "$HOME/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD"
  "$HOME/Applications/OpenSCAD-2021.01.app/Contents/MacOS/OpenSCAD"
  "/opt/homebrew/bin/openscad"
  "/usr/local/bin/openscad"
)

for volume in /Volumes/OpenSCAD*; do
  if [[ -d "$volume" ]]; then
    candidates+=(
      "$volume/OpenSCAD.app/Contents/MacOS/OpenSCAD"
      "$volume"/OpenSCAD*.app/Contents/MacOS/OpenSCAD
    )
  fi
done

for candidate in "${candidates[@]}"; do
  if [[ -x "$candidate" ]]; then
    printf '%s\n' "$candidate"
    exit 0
  fi
done

printf 'OpenSCAD CLI was not found. Set OPENSCAD_BIN=/path/to/OpenSCAD or add openscad to PATH.\n' >&2
exit 1
