# Watch accessories and protectors

Use this reference when designing bezel protectors, watch stands, bracelet cradles, display docks, or any printed part that touches a watch.

## Procedure

1. **Identify the contact surface first.** Separate the visible styling surface from the retention/contact surface. For bezels, model the full contact annulus and crystal clearance separately; for stands, model the case/bracelet support path before decoration.
2. **Ask or infer material before slicing.** TPU can use light interference and flex; PLA/PETG need clearance because they are rigid and can scratch polished metal or bind on bezels.
3. **Design print orientation before printing.** Put broad visible/protective faces on the bed when possible. Do not leave inward lips, cap roofs, or over-bezel shoulders as unsupported bridges unless the bridge is short and intentionally checked in the slicer.
4. **Prototype retention in stages.** First prove orientation and surface quality, then tune fit. If a protector is loose or does not cover the full bezel, prefer a full 360-degree cap with a tuned socket over a large C-ring gap.
5. **Make wearable accessories look intentional.** Add broad, printable detail such as scalloped/coin-edge perimeters, wave ribs, chamfered plinths, or flat raised inlays. Avoid tiny text and only add logos when the user explicitly requests/provides authorized artwork.
6. **Prefer flat inlay geometry for logos and ornaments.** Make logo/ornament features broad, shallow, and manifold; avoid overlapping rods/tubes because intersecting decorative shells can slice but create non-manifold mesh edges.
7. **Verify before printing.** Report material, clearance, support state, overhang/bridge markers, object height, and estimated time. If the bed/camera cannot be visually inspected, say so.

## Starting dimensions for Omega Seamaster Professional Chronograph / calibre 1164 class

Use only as first-fit assumptions until measured:

- Case diameter: about 41.5 mm.
- Thickness: about 16–16.5 mm.
- Lug/bracelet width: about 20 mm.
- Bezel protector first-fit socket for PLA: start around 0.4–0.7 mm diameter clearance, then tune from physical feedback.
- Bezel protector first-fit socket for TPU: start around 0.1–0.3 mm diameter clearance, depending on printer accuracy and desired snap.

## Pitfalls

- Do not print watch-contact parts in hard PLA with a TPU-tight fit — rigid plastic can scratch or seize because it cannot flex around polished metal.
- Do not use a wide C-gap for a bezel protector that must stay on while worn — the opening removes retention and leaves part of the bezel exposed.
- Do not trust a slicer success alone for protectors — inspect bridge/overhang comments or preview because unsupported lips can slice but print as stringing.
- Do not call a decorative watch accessory final after the first fit test — expect at least one physical feedback loop for looseness, coverage, and appearance.
