# Creality/3MF project conversion for preview and Blender handoff

Use with `cad-to-print-delivery` when the user provides a slicer/project `.3mf` file and asks to open it, blend it, inspect it, or extract geometry.

## Key lesson

A Creality/Bambu-style `.3mf` is a ZIP package. Do not assume it is a single STL. It may contain:

- preview thumbnails under `Metadata/`;
- a root `3D/3dmodel.model` file with build items and transforms;
- many `3D/Objects/object_*.model` files, only some of which contain actual mesh vertices/triangles;
- components that reference other object models with transforms.

For a real conversion, parse the build graph and apply transforms. Do not just extract a thumbnail or the first mesh object.

## Durable extraction workflow

1. Treat the 3MF as a ZIP and list entries.
2. Parse every `*.model` XML file with the 3MF core namespace:
   - vertices: `.//vertex`
   - triangles: `.//triangle`
   - components: `.//component`
   - build items: `.//build/item`
3. Identify actual mesh-bearing object files. Empty object files are common.
4. In `3D/3dmodel.model`, resolve each build item:
   - build item transform;
   - referenced object id;
   - nested component path/object id;
   - nested component transform.
5. Apply all transforms and merge printable build items into an arranged plate mesh.
6. Export both:
   - STL for slicers/printing tools;
   - OBJ for Blender import.
7. Generate a simple preview render from the merged geometry or use the embedded `Metadata/plate_1.png` as a sanity cross-check.

## Blender handoff

If Blender is not installed, do not claim a `.blend` was created. Instead deliver:

- converted OBJ/STL;
- preview PNG;
- a small Blender Python script that imports the OBJ, assigns a material, adds a light/camera, and saves a `.blend`.

Example command after Blender installation:

```bash
blender --background --python blender_import_project.py
```

## Verification

- Report build item count, triangle count, and merged footprint dimensions.
- Visually inspect the preview for a coherent arranged plate.
- If transforms produce absurd dimensions or broken projection, fix transform interpretation before delivering.
- Label the output as a conversion/handoff unless Blender actually saved the `.blend`.
