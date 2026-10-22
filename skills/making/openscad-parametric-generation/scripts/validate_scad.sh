#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  printf 'Usage: %s path/to/model.scad\n' "$0" >&2
  exit 64
fi

input="$1"
if [[ ! -f "$input" ]]; then
  printf 'SCAD file not found: %s\n' "$input" >&2
  exit 66
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
openscad_bin="$("$script_dir/find_openscad.sh")"
tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

output="$tmp_dir/validation.stl"
printf 'Validating %s with %s\n' "$input" "$openscad_bin"
"$openscad_bin" -o "$output" "$input"
printf 'Validation passed: %s\n' "$input"
