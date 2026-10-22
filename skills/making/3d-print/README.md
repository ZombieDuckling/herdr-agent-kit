# 3d-print — Hermes skill

Chat-driven parametric 3D modeling (CadQuery) with PNG previews (Blender)
and print-ready 3MF slicing (Bambu Studio CLI) for a Bambu Lab A1 Mini.

This directory is the installable skill: copy it to
`~/.hermes/skills/3d-print/`. The heavy lifting happens in the
`hermes-3d-toolchain` Docker image; `scripts/print3d` and
`scripts/cadquery-mcp` are thin host-side wrappers around it.

Install, build and deployment instructions live in the repo root README:
https://github.com/vladthecto/hermes-3d-print
