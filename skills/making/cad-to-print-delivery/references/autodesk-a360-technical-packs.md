# Autodesk A360 / Fusion public-share technical packs

Use this when the user provides an Autodesk A360 short link and asks for a technical spec, technical drawing pack, load/stress notes, or manufacturing review.

## Procedure

1. Resolve the short link and save traceability.
   - `https://a360.co/...` redirects to a Galileo share URL like `https://<hub>.autodesk360.com/g/shares/<share_id>`.
   - Fetch the non-`/g` metadata endpoint: `https://<hub>.autodesk360.com/shares/metadata/<share_id>?version=0`.
   - Save `metadata.json`, the share ID, `versionUrn`, file type, version number, download flag, derivative status, and original short URL.

2. Download the source file if the share allows it.
   - Use `https://<hub>.autodesk360.com/shares/download/<share_id>/` with the trailing slash; the no-slash variant can return a 403.
   - Save the returned `.f3d` beside metadata and include it in the source folder of the pack.
   - Treat the source `.f3d` as traceability/source material, not as proof of exact exported manufacturing dimensions until Fusion or a neutral export verifies them.

3. Extract embedded Fusion assets.
   - Fusion `.f3d` files are ZIP containers and may use ZIP compression method 93 (Zstandard). Use Python 3.14 or another Zstd-capable extractor when system Python cannot read compressed entries.
   - Extract `Previews/big.png`, `Previews/small.png`, `Breps.BlobParts/`, `OGS.BlobFolder/`, `Manifest.dat`, and `Properties.dat` when available.
   - Use embedded previews as visual source views only; label them non-controlled if no orthographic drawings or exported geometry are available.

4. Fetch the derivative manifest.
   - Metadata usually points at `https://<hub>.autodesk360.com/shares/derivatives/<share_id>/manifest`.
   - Save `derivative_manifest.json` and mine it for camera views, file size, derivative status, resource URNs, view names, and viewable IDs.
   - Do not assume public derivative resource URNs can be downloaded directly; if only manifest and preview data are accessible, label all dimensions as approximate.

5. Estimate dimensions only with explicit caveats unless a real CAD export is available.
   - Prefer Fusion 360 Inspect, STEP/STL export, or properties DB/mesh decode that you can verify.
   - If using public-viewer mesh buffers, report them as approximate viewer-mesh envelopes and include the method/limitation in the PDF and README.
   - Never present viewer-derived envelope numbers as manufacturing tolerances.

6. Build the pack.
   - Include a PDF drawing/spec pack, `TECHNICAL_SPEC.md`, source previews, `metadata.json`, `derivative_manifest.json`, source `.f3d`, and `SOURCE_VERIFICATION.json`.
   - The PDF should have: cover/source metadata, embedded preview/general arrangement, approximate envelope sheet, load/stress point sheet, verification checklist, and assumptions/limitations.

7. Always include load/stress points for brackets, mounts, and structural parts.
   - Identify likely load paths: mass, torque reaction, vibration/fatigue, fastener preload, shock loads, and frame reactions.
   - Call out stress concentration zones: bolt-hole bearing/tear-out, boss/web transitions, inside corners, thin webs, rear edges, and layer-line risks if printed.
   - State what is required for numeric FEA or load rating: material, process, motor/load mass, peak torque, shock factor, fastener size/grade, boundary constraints, and print orientation.

8. Verify before delivery.
   - Check the ZIP contains the PDF, source `.f3d`, metadata, derivative manifest, spec markdown, drawings, and verification JSON.
   - Render at least one PDF page or inspect drawing PNGs visually. Fix label overlap or clipped notes before sending.

## Pitfalls

- Preserve the trailing slash on `/shares/download/<share_id>/` because Autodesk may reject the no-slash endpoint.
- Do not harden a temporary extraction failure into a tool limitation. Try a newer Python or Zstd-capable extractor for method-93 ZIP entries.
- Do not treat public-viewer mesh dimensions as controlled drawings because scene/view buffers can include helper geometry, multiple bodies, or camera/scene primitives.
- Do not claim load rating from qualitative stress notes; without real loads, constraints, material, and fasteners it is only a preliminary review.
