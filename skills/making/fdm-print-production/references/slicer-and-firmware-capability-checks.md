# Slicer and firmware capability checks

Use when asked whether a slicer or a slicing feature is compatible with the user's printer, before
installing anything or promising a print. Two halves: what the software supports, and what the
machine's firmware will actually execute.

## 1. Slicer half

- Check the vendor's own printer page first, then whether the upstream slicer already ships the
  model's profile. Unlayered Slicer (a non-planar/5-axis fork) states that it ships OrcaSlicer's
  profiles and its printer page names "Creality Ender 3, K1 and K2"; OrcaSlicer ships K1C profiles,
  and K1C is a K1 variant. That answers the software side without installing anything.
- Vendor limit worth quoting back: on 3-axis machines the practical limit is nozzle and duct
  clearance, not the slicer — "Voron's small, low ducts leave more nozzle clearance, so non-planar
  layers can curve more steeply."

## 2. Acquisition is usually the real blocker

Gated downloads masquerade as open links. Before promising an install, check the gate:

```bash
curl -sIL <vendor-download-url> | grep -iE '^(HTTP/|location:)'   # 307 -> /login means an account is required
gh api repos/<org>/<repo>/releases --jq '.[] | "\(.tag_name) \(.assets | length)"'   # zero assets = no binaries shipped
brew info --cask <name>                                            # is there a cask at all?
```

Worked example: Unlayered Slicer is invite-only. `/download` 307-redirects to `/login`, the login page
answers *"We couldn't find an account for that email"* for an address that never signed up, every
GitHub release carries 0 assets, and there is no Homebrew cask. Their README states it: *"Installers are
provided to Unlayered 3D customers. There are no public binary releases, so everyone else builds from
source."* The fallback build, per their README, is:

```bash
git clone --depth 1 --branch <tag> https://github.com/<org>/<repo>.git src
brew install cmake ninja                                        # cmake/ninja may be missing even on a dev Mac
cd src && ./build_release_macos.sh -a arm64                     # native arm64; '-a universal' doubles compile time
```

Start that build in the background with a completion notification instead of blocking; expect an hour or
more for the dependencies. Report the gate and the build cost as part of the answer — the user believed
it was a free download.

## 3. Machine half — probe the printer, do not trust the page

```bash
P=<printer-ip>:7125
# what the firmware can do
curl -s "http://$P/printer/objects/query?configfile=settings" | python3 -c '
import sys, json
s = json.load(sys.stdin)["result"]["status"]["configfile"]["settings"]["printer"]
for k in ("kinematics", "max_velocity", "max_accel", "max_z_velocity", "max_z_accel"): print(k, "=", s.get(k))'
# installed motion features that matter for a curved first layer
curl -s "http://$P/printer/objects/list" | python3 -c '
import sys, json
print([o for o in json.load(sys.stdin)["result"]["objects"] if any(k in o for k in ("bed_mesh", "probe", "z_tilt", "quad_gantry", "safe_z", "input_shaper"))])'

# live proof that one move can carry X, Y and Z together (what non-planar toolpaths need)
curl -s -X POST "http://$P/printer/gcode/script" -H 'Content-Type: application/json' -d '{"script":"G28"}'
curl -s -X POST "http://$P/printer/gcode/script" -H 'Content-Type: application/json' -d '{"script":"G90"}'
curl -s -X POST "http://$P/printer/gcode/script" -H 'Content-Type: application/json' -d '{"script":"G1 Z15 F600"}'
curl -s -X POST "http://$P/printer/gcode/script" -H 'Content-Type: application/json' -d '{"script":"G1 X140 Y140 Z11 F3000"}'
curl -s "http://$P/printer/objects/query?toolhead=position"
```

Proof shape: `toolhead.position` reads X 140.00, Y 140.00, Z 10.78 after the diagonal — three axes
moved inside one command, so the firmware will execute a non-planar toolpath. Resources to record:
`kinematics = corexy`; on a stock K1C `max_z_velocity = 10.0`, `max_z_accel = 300.0` against
`max_velocity = 600.0` / `max_accel = 20000.0`.

Pitfalls:

- Build the call as a JSON body. `POST /printer/gcode/script?script=G1 X100 Y100` (spaces in the query,
  no body) returns success without moving and `toolhead.position` does not change, so a position check
  is the only honest proof. A missing or non-JSON content-type has the same silent failure.
- A `200` from the script endpoint is not proof the move happened; re-read `toolhead.position`.
- Only probe when the printer is idle (`printer/info` state `ready`, no active `print_stats`), and leave
  it parked; homing a printer that is mid-job ruins the job.
- Gear with the newer 2025 K1C mainboard revision has no local web UI and no root SSH, and uses host type
  "CrealityPrint" in Orca instead of "Klipper (Octo/Klipper)" — check what Moonraker port actually
  answers before scripting against it.

## 4. Prove the feature in the produced toolpath, not in the machine

Motion capability (§3) only says the firmware *could* execute a curved toolpath. Whether the slicer
emitted one is a separate, checkable fact, and the app's settings screen does not answer it.

Unlayered's non-planar engine is gated in their source on
`enable_nonplanar && (object->cut_planes.active() || object_has_directed_parts(object))`. A plain STL
through the CLI therefore slices planar whatever the flags say: with `enable_nonplanar = 1` and
`axis_selection = virtual` set, the produced G-code was byte-identical to the planar slice apart from
three comment lines (`enable_nonplanar = 1`, `axis_selection = virtual`, `virtual_5axis = 1`). Their
engine also partitions the object into segments before it can tilt anything, and reports the outcome
honestly, e.g. `[partition] 3DBenchy: SegmentTooThin, 0 segment(s) from 57 plane(s)` — zero segments
means flat layers, so a solid benchy is a poor non-planar demo even in the GUI.

Check the toolpath the same way you check the printer: parse it.

```python
import re
layer = 0; per = {}; cur = None
for ln in open(gcode):
    if ln.startswith(';LAYER_CHANGE'): layer += 1; continue
    if not ln.startswith(('G1', 'G0')): continue
    m = re.search(r'Z([-\d.]+)', ln)
    if m: cur = float(m.group(1))
    if 'E' in ln and re.search(r'[XY][-\d]', ln) and cur is not None:
        per.setdefault(layer, set()).add(round(cur, 3))
# non-planar: layers carrying 3+ distinct Z heights on extruding moves; planar: every layer is one height
```

Report "layers built with more than one Z height" plus the biggest in-layer Z swing. That number is the
difference between the ordinary print and the requested feature.

Preset/CLI pitfalls that cost the most time:

- The loader resolves presets **by name inside the app bundle**. An external JSON handed to
  `--load-settings` fails with `Preset was not found in the loaded bundle` even when its `name`
  matches, and keys invalid for that preset *type* are stripped (`contains incorrect keys:
  enable_nonplanar, which were removed`). Patch the bundled preset file in place and keep a backup
  rather than fighting the loader; non-planar keys (`enable_nonplanar`, `axis_selection`) belong to a
  *machine* preset, while print keys (`print_sequence = "by group"`, required of a multiplanar job)
  belong to a *process* preset.
- `--export-3mf` takes a **bare filename** that is joined onto `--outputdir`, so an absolute path
  becomes `/outdir//tmp/file.3mf` and the export fails. Use `--outputdir <dir> --export-3mf name.3mf`.
- Cut planes are project data, at `Metadata/cut_planes.xml`, schema
  `<objects><object id="1" enabled="1"><plane px py pz nx ny nz/>…`. `--export-skeleton` computes and
  dumps the skeleton (nodes, `cut_edges`, `cut_normals`) but does not author the stack on the model, so
  headless non-planar needs either that file injected into the project or the GUI's Cut Planes /
  Skeleton Cut tool — the vendor-intended route, whose output the injected planes reproduce.

## 5. Reading the numbers back to the user

Translate limits into consequence, not jargon: with Z capped at 10 mm/s, a 20° slope forces roughly
29 mm/s of path speed, so steep non-planar curves print slowly; raising `max_z_velocity` in
`printer.cfg` is the single biggest win if the revision allows editing it. Keep curvature modest on
enclosed printers with low-slung part-cooling ducts. Say plainly what was not checked — e.g. the app
was never launched and its printer dropdown never read with your own eyes.
