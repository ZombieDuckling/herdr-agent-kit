#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  printf 'Usage: %s path/to/model.scad path/to/output.png\n' "$0" >&2
  exit 64
fi

input="$1"
output="$2"
if [[ ! -f "$input" ]]; then
  printf 'SCAD file not found: %s\n' "$input" >&2
  exit 66
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
openscad_bin="$("$script_dir/find_openscad.sh")"
mkdir -p "$(dirname "$output")"

printf 'Rendering PNG %s from %s\n' "$output" "$input"
"$openscad_bin" -o "$output" "$input"
printf 'Rendered PNG: %s\n' "$output"
