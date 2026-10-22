# 10 — Import, Export, and CLI

OpenSCAD can import external geometry and export rendered models. A future AI design tool should support both GUI workflows and command-line generation.

## Imports

Common import patterns:

```scad
import("part.stl");
import("profile.dxf");
import("logo.svg");
surface(file = "heightmap.png");
```

Typical rules:

- STL, OFF, DXF, and similar formats can be brought in with `import()`.
- PNG heightmaps can be brought in with `surface()`.
- File suffix determines type in many workflows.
- Paths are resolved relative to the importing script unless absolute.

## Importing SVG and extruding

```scad
linear_extrude(height = 3)
    import("logo.svg");
```

Expose scale and height:

```scad
svg_scale = 0.4;
svg_height = 2;

linear_extrude(height = svg_height)
    scale([svg_scale, svg_scale])
        import("logo.svg");
```

## Importing STL for modification

OpenSCAD can operate on imported meshes, but it is not a mesh repair tool. Imported STL must be valid enough for booleans and export.

```scad
difference() {
    import("base.stl");
    translate([0,0,-1]) cylinder(h = 20, d = 5);
}
```

Agent caution: modifying arbitrary STL can fail because imported meshes may be non-manifold, self-intersecting, over-detailed, or poorly scaled.

## Exports from GUI

The normal GUI flow:

1. Render with F6.
2. Export through File → Export.
3. Use STL/3MF/OFF/AMF for 3D printing workflows; SVG/DXF/PDF for 2D workflows; PNG for images.

## Command-line exports

OpenSCAD can be called from the command line. Basic pattern:

```bash
openscad -o output.stl input.scad
```

For PNG/image output:

```bash
openscad -o preview.png input.scad
```

On macOS, the binary may be inside the app bundle:

```bash
/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD -o output.stl input.scad
```

## Passing parameter values from CLI

OpenSCAD supports defining constants from command-line arguments in common workflows. Pattern:

```bash
openscad -D 'width=100' -D 'height=20' -o output.stl model.scad
```

For an AI design system, this enables batch variant generation.

## Batch generation pattern

A script can generate multiple variants by calling OpenSCAD repeatedly:

```bash
openscad -D 'label="A"' -o part_A.stl model.scad
openscad -D 'label="B"' -o part_B.stl model.scad
openscad -D 'label="C"' -o part_C.stl model.scad
```

## Makefile pattern

For repositories, a simple Makefile can export STL from SCAD:

```makefile
%.stl: %.scad
	openscad -o $@ $<
```

## Agent export recommendations

When the agent creates a repository, include:

- `model.scad`: source;
- `README.md`: parameters and export instructions;
- `Makefile`: optional CLI export;
- `examples/`: example parameter variants;
- `renders/`: optional PNG previews;
- `exports/`: generated STL/3MF outputs, usually gitignored unless release artifacts.

## CLI validation target

An AI pipeline should eventually run:

```bash
openscad -o /tmp/test.stl generated_model.scad
```

If this command fails, the model should not be presented as final.
