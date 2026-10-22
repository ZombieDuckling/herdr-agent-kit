# 11 — Libraries, `use`, and `include`

Libraries are important for an AI parametric design tool because they can provide reusable mechanical primitives: threads, gears, bearings, screw helpers, fillets, rounded boxes, hardware models, and enclosure patterns.

## `use` vs `include`

OpenSCAD has two mechanisms for loading other `.scad` files.

```scad
use <library.scad>
include <settings.scad>
```

General practical distinction:

- `use` imports modules/functions from another file without executing its top-level geometry.
- `include` includes the file more directly, including top-level assignments and possible top-level geometry.

Agent rule: prefer `use` for libraries. Use `include` for shared constants/settings only when intended.

## Library path lookup

OpenSCAD searches for library files in multiple locations, including the directory of the calling file, user-defined library paths, built-in/user library locations, and installation libraries.

A repository should avoid relying on a user's global library path unless documented. Safer pattern:

```scad
use <libs/rounded.scad>
```

Then include `libs/rounded.scad` in the repo.

## Repository library structure

```text
project/
  model.scad
  libs/
    util.scad
    hardware.scad
  examples/
    variant_small.scad
    variant_large.scad
  README.md
```

`model.scad`:

```scad
use <libs/util.scad>
use <libs/hardware.scad>
```

## Common public libraries

The official OpenSCAD library index lists many libraries. Useful categories:

- BOSL/BOSL2: broad helper libraries, shapes, transforms, attachments, mechanical helpers.
- MCAD: older mechanical CAD helpers.
- NopSCADlib: 3D printer/electronics/enclosure parts.
- dotSCAD: mathematical modelling helpers.
- threads libraries: screw threads.
- enclosure helpers and board-game/component-box libraries.

Agent caution: library dependency is a product decision. A self-contained generated model is easier to share. A library-assisted model can be more powerful but requires dependency setup.

## When to use libraries

Use libraries when:

- the geometry is complex and well-covered by existing code;
- thread generation is needed;
- gears, bearings, hardware models, or standard components are needed;
- high-quality rounding/filleting helpers are needed;
- The user accepts external dependencies.

Avoid libraries when:

- the part can be built simply with native OpenSCAD;
- the output must be standalone;
- dependency installation would create friction;
- license compatibility is unclear.

## AI repository practice

If the generated model uses a library, the agent should:

1. state the exact dependency;
2. state where to place it;
3. include a fallback or simple-native alternative where possible;
4. document the library license separately;
5. avoid silently assuming the user's machine has it installed.
