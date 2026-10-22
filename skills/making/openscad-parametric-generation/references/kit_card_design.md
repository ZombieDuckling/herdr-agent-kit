# Kit Card Design Notes

Kit cards are 2.5D model kits: a flat card contains multiple printable parts held by sprues. The goal is not only to look good on the card, but to break out cleanly and assemble into a small object.

## Layout

- Start with the finished object decomposed into flat printable parts.
- Arrange large mirrored parts first, then central body parts, then small detail parts.
- Keep a visible outer runner frame around the whole card.
- Connect each part to runners with 2-4 breakaway tabs. Avoid connecting only to fragile details.
- Keep labels and decorative plaques inside the runner frame so they print as part of the card.

## Parameter Defaults

- `card_t`: 1.6-2.4 mm for FDM kit cards.
- `runner_w`: about 2.0 mm for the outside frame.
- `sprue_w`: about 1.2 mm for internal rails.
- `breakaway_w`: about 0.6-0.9 mm.
- `clearance`: 0.2-0.35 mm for slots and tabs.
- `min_feature`: at least 0.6 mm for reliable FDM details.
- `detail_depth`: 0.4-0.8 mm for raised or engraved surface relief.

## Geometry Strategy

Use 2D profiles for the whole card:

1. Draw the outer frame as a rounded-rectangle ring.
2. Draw internal runners as capsules or rounded bars.
3. Draw part silhouettes as separate 2D polygons/circles/offset profiles.
4. Subtract slots, sockets, vents, grille openings, and decorative linework in 2D.
5. Union frame, runners, tabs, and parts.
6. `linear_extrude(height = card_t)` the complete 2D layout.
7. Add optional raised text/relief as a second shallow extrusion on top.

Avoid mixing already-extruded 3D parts with 2D booleans. Keep the card bottom on `Z = 0`.

## Assembly Features

- Slots should be slightly wider than mating tab thickness plus clearance.
- Tabs should have lead-in chamfers or rounded ends when possible.
- Use keyed slots/notches when two similar parts could be assembled backward.
- Add small orientation marks or labels if the card has many similar pieces.

## Detail Limits

Dense linework can look excellent, but every line must be printable. Parameterize line count and spacing, and assert that `detail_line_w >= min_feature` and `detail_gap >= min_feature`. For grille-like panels, subtract repeated rounded slots from a solid panel while leaving a perimeter rim and diagonal/vertical ribs.

## Validation Checklist

- All parts are inside the card frame.
- Every free part has breakaway tabs.
- Slots and tabs have clearance.
- Detail lines meet minimum feature size.
- The final source has a single `model();` call.
- The exported STL renders without non-manifold warnings.
