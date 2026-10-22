# Reverse engineering parts from photographs

Depth behind the SKILL.md rules for photo-derived CAD. Use it to set expectations,
choose the measurement route, and decide what to model.

## Accuracy hierarchy

| Route | Realistic error on a hand-held part | Use it for |
|---|---|---|
| Calibrated planar capture, coplanar features | Sub-millimetre if the fiducial spans the object and camera distortion is modelled | Outline, feature placement, wall thickness of flat faces |
| Photogrammetry / phone Object Capture | 1-2 mm on a ~10 cm object against caliper ground truth | Shape, texture, organic relief |
| Phone LiDAR | ~10 cm scale and above; resolves nothing millimetre-scale | Rooms and large surfaces, not small parts |
| Desktop structured light / laser | 0.05-0.1 mm claimed, but occluded bores and deep recesses stay unmeasured | Surface detail, when the feature has line of sight |
| Calipers / micrometer / pin gauges | 0.01 mm, technique-limited | Every mating dimension |
| FDM output | 0.2-0.3 mm per side assembly clearance, holes print undersize | The real accuracy floor of the delivered part |

Rule: photographs supply shape, instruments supply fit. A dimension that must
assemble is never taken from an image.

## Calibration rules

- The reference must span the object. Scaling a reconstruction from a small
  mark multiplies its scale error; a 2.8 mm reference produced 1.48 mm average
  width error where the object's own full length produced 0.23 mm on the same
  model.
- Verify the printed capture sheet against a ruler before photographing it. A
  sheet silently scaled to fit the page scales every downstream dimension by
  the same factor.
- Estimate camera intrinsics and correct lens distortion instead of assuming a
  pinhole; use multi-view CharUco/ArUco calibration. Barrel distortion is
  largest at the frame edges, where the fiducials sit.
- Shoot from far away and zoomed in to approximate orthographic projection.
  Perspective error on raised features is the dominant term once calibration is
  sound.
- Backlight flat parts for silhouette captures: a near-binary edge removes
  moulding texture, glare and surface artifacts from the outline measurement.
- A hand or shadow over a marker invalidates that image for measurement; keep it
  for orientation only.

## Artifact or feature

Decide by function and cross-section, not appearance:

- Does anything engage it? If nothing mates with the feature it is decorative or
  incidental.
- Is it a drafted, radiused blind recess with a sensible diameter, or a broad
  shallow dish? A clay or paper impression settles it in one step.
- Does it cluster on one face (the B-side)? Ejector marks and gate vestiges do.
- Would the part function identically without it? Then omit it.

Moulded flatness deviation from sink marks measures 0.04-0.06 mm on a corrected
part and 0.28-0.38 mm on a warped one, against specified form tolerances in the
tenths of a millimetre. On a 6 mm tall part that is 5% of the height - exactly
where blob detection starts inventing recesses.

## Fit compensation

- Measure the mate: barrel outer diameter at the engagement length, engagement
  depth, socket bore, peg pitch. Convert the fitting problem into a direct
  reading.
- Put clearance in the parametric source as its own named, deliberately signed
  parameter; apply it in the direction that makes the print fit, not the
  direction that copies the original.
- Material shrinkage is material-specific (PLA ~0.2-0.3%, PETG 0.5-0.7%, ABS
  0.6-0.8%); let the printed part cool to ambient for at least an hour before
  measuring, zero calipers on a reference block, and measure across the
  centreline of a feature rather than at an edge, over bridging, or over
  elephant's foot.
- Print a one-peg/one-bore test coupon with the target fit before re-slicing the
  whole part. It is the cheapest closure of the measure-model-print-test loop.
- Once measurement error is below roughly a third of the printer's clearance
  allowance, stop refining measurements and go to the fit test.

## From measurements to CAD

Read dimensions off the capture and rebuild from parametric primitives with
named variables; do not convert the scan mesh into a solid and expect to edit
it, because that yields tens of thousands of facets with no editable features.
Close the loop with a deviation check between the rebuilt body and the reference
mesh, and check results against the caliper numbers rather than against the
photograph.
