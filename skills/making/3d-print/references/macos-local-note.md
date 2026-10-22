# macOS local note for the user's Hermes

The upstream `vladthecto/hermes-3d-print` skill is designed for a Linux x86_64 Hermes VPS with Docker, CadQuery, Blender, and Bambu Studio CLI inside an isolated image.

On the user's Mac, use the skill's design discipline first: parametric CadQuery/OpenSCAD source, previews, iterative feedback, and explicit print-file confirmation. Do not hand-build raw triangle meshes for functional CAD.

If Docker is available and can run amd64 Linux images, the upstream toolchain may work via emulation, but Bambu Studio CLI/AppImage inside Docker is not guaranteed on macOS.

Practical fallback order on this Mac:
1. Install/use CadQuery locally for STL/STEP: `python3 -m pip install cadquery` or conda if pip fails.
2. Install/use OpenSCAD for scriptable robust solids: `brew install openscad`.
3. Use Blender only for previews/organic models, not precision dash inserts.

For car interior parts, require real measurements before final-fit output: width, height, depth, radii/curvature, mounting tabs, clearances, target phone/accessory, material, and print orientation.
