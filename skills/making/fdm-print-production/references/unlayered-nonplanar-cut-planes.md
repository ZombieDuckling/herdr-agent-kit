# Non-planar slicing in Unlayered Slicer (Orca-derived) — the real gate

## Why a sliced print can come out planar anyway

The engine branches on a per-object state, not on the printer config:

```cpp
m_config.enable_nonplanar.value &&
  (model_object->cut_planes.active() || object_has_directed_parts(*model_object))
```

- `enable_nonplanar` is a **machine** preset key (setting it in a *process* preset is silently
  stripped: "contains incorrect keys: enable_nonplanar, which were removed").
- `axis_selection = virtual` is their "Printer type → Virtual": toolpaths are generated as
  five-axis but no rotary words are written, the nozzle stays upright, and tilted chunks are
  bounded by max tilt angle / max height.
- With both set and no cut planes, the produced G-code is identical to the planar slice apart from
  header comments — verified byte-for-byte.

**Proof of the feature is Z on extruding moves *inside* a layer.** Planar output: 0 layers have
more than one Z on extruding moves. Non-planar output: layers whose Z climbs while extruding.

## Authoring planes headlessly

Cut planes live in the project archive as `Metadata/cut_planes.xml`:

```xml
<objects>
<object id="1" enabled="1">
<plane px="0" py="0" pz="20" nx="0.5736" ny="0" nz="0.8192"/>
</object>
</objects>
```

`id` is the 1-based object index; a plane's `normal` is the build direction for everything beyond
it (`bnx/bny/bnz` optionally overrides the build normal). Inject it into the exported project with
`zipfile`, then slice that 3MF — the CLI cannot author planes itself.

Also required: `print_sequence = by group` (a multiplanar job prints each chunk complete, not
layer-by-layer across the plate). Both bundled presets must be edited in place: `--load-settings`
refuses external files that are not registered presets in the vendor bundle
("Preset was not found in the loaded bundle").

## Limits, learned the hard way

- Steep chunks are refused, with a precise message naming the angle the machine allows (e.g.
  "tilted 77.9 degrees from vertical, but this virtual 5-axis printer allows at most 43.9 degrees
  here") — the limit comes from the hotend envelope/`nonplanar_gantry_height`, not from a setting
  The user can ignore.
- Auto-generated skeleton planes are frequently unusable for a given model: a benchy produced 57
  cuts that all partitioned to `SegmentTooThin`, i.e. zero chunks and therefore flat layers.
- A single deliberate, gentle plane is what demonstrates the feature. On a benchy, a 35° plane at
  z=20 produced 21 layers built tilted with up to 24 mm of Z travel inside one layer; the planar
  slice of the same model had none.
- `--export-3mf` takes a **bare filename** (the output directory is prepended), and
  `--export-skeleton <dir>` dumps the skeleton plus a partition diagnostic that is the quickest
  read on whether planes will carve usable chunks.
