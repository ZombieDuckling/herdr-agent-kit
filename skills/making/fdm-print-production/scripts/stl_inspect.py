#!/usr/bin/env python3
"""Inspect an STL for print readiness: geometry, orientation, contact area, manifoldness.

Reports the evidence needed before slicing/printing: dimensions, whether a broad flat
face sits on Z=0 (correct print orientation), contact area on the bed, overhang profile,
and mesh integrity.
"""
import struct
import sys
from pathlib import Path

path = Path(sys.argv[1] if len(sys.argv) > 1 else "ET4_ALL_33.stl")
raw = path.read_bytes()
print(f"file: {path}  size: {len(raw)/1e6:.2f} MB")

try:
    import numpy as np
    HAVE_NP = True
except ImportError:
    HAVE_NP = False
print("numpy:", HAVE_NP, "| trimesh:", end=" ")
try:
    import trimesh
    print("yes")
except ImportError:
    trimesh = None
    print("no")

# --- parse STL (binary or ascii) ---
if raw[:5] == b"solid" and b"facet" in raw[:2000]:
    txt = raw.decode(errors="ignore")
    verts = []
    for line in txt.splitlines():
        p = line.split()
        if len(p) == 4 and p[0] == "vertex":
            verts.append(tuple(float(x) for x in p[1:]))
    tris = np.array(verts).reshape(-1, 3, 3) if HAVE_NP else verts
    print("format: ascii")
else:
    n = struct.unpack("<I", raw[80:84])[0]
    print(f"format: binary, triangles={n:,}")
    if HAVE_NP:
        arr = np.frombuffer(raw[84:84 + n * 50], dtype=np.uint8).reshape(n, 50)
        f = arr[:, 12:48].copy().view("<f4").astype("float64").reshape(n, 3, 3)
        tris = f
    else:
        tris = [struct.unpack("<12f", raw[84 + i * 50:84 + i * 50 + 48])[1:] for i in range(n)]
        tris = [(t[0:3], t[3:6], t[6:9]) for t in tris]

if HAVE_NP:
    v = tris.reshape(-1, 3)
    mn, mx = v.min(axis=0), v.max(axis=0)
    ext = mx - mn
    print(f"bbox min: ({mn[0]:.2f}, {mn[1]:.2f}, {mn[2]:.2f}) mm")
    print(f"bbox max: ({mx[0]:.2f}, {mx[1]:.2f}, {mx[2]:.2f}) mm")
    print(f"extents: {ext[0]:.2f} x {ext[1]:.2f} x {ext[2]:.2f} mm  (X x Y x Z)")
    # signed volume
    a, b, c = tris[:, 0], tris[:, 1], tris[:, 2]
    vol = np.einsum("ij,ij->i", a, np.cross(b, c)).sum() / 6.0
    print(f"volume: {abs(vol)/1000:.2f} cm^3")
    # normals + areas
    nrm = np.cross(b - a, c - a)
    area = 0.5 * np.linalg.norm(nrm, axis=1)
    tot_area = area.sum() / 100.0
    print(f"surface area: {tot_area:.1f} cm^2")
    # flat faces grouped by axis-aligned normal
    flat = area > 0.5
    nz = np.zeros(len(tris))
    ok = np.linalg.norm(nrm, axis=1) > 1e-9
    nn = np.zeros_like(nrm)
    nn[ok] = nrm[ok] / np.linalg.norm(nrm[ok], axis=1)[:, None]
    down = (nn[:, 2] < -0.98)          # facing the bed
    up = (nn[:, 2] > 0.98)             # facing the sky
    side = np.abs(nn[:, 2]) < 0.02     # vertical walls
    print(f"\nface-area split: down(-Z) {area[down].sum()/100:.1f} cm^2 | up(+Z) {area[up].sum()/100:.1f} cm^2 | walls {area[side].sum()/100:.1f} cm^2 | other {tot_area - (area[down].sum()+area[up].sum()+area[side].sum())/100:.1f} cm^2")
    # contact area: downward faces whose vertices sit on the lowest plane
    if down.any():
        dz = tris[down][:, :, 2]
        on_bed = (np.abs(dz - mn[2]) < 0.05).all(axis=1)
        contact = area[down][on_bed].sum() / 100.0
        zc = (dz.max(axis=1) - dz.min(axis=1))
        print(f"downward faces at z_min (contact): {contact:.2f} cm^2 across {int(on_bed.sum())} faces (z-flatness max {zc[on_bed].max() if on_bed.any() else 0:.4f} mm)")
        if not on_bed.any():
            # nearest downward plane above z_min
            import collections
            zs = np.round(np.min(tris[down][:, :, 2], axis=1), 2)
            print("  lowest downward planes:", collections.Counter(zs.tolist()).most_common(4))
    else:
        print("NO downward-facing flat face: the part has no planar base on the bed")
    print(f"z_min: {mn[2]:.3f} mm  (0.000 = sitting exactly on the bed; negative = sunk into it)")
    # open/boundary edges (manifold check) via rounded vertex keys
    key = np.round(v, 3)
    uk, inv = np.unique(key, axis=0, return_inverse=True)
    f_i = inv.reshape(-1, 3)
    e = np.concatenate([f_i[:, [0, 1]], f_i[:, [1, 2]], f_i[:, [2, 0]]])
    e = np.sort(e, axis=1)
    uniq_e, counts = np.unique(e, axis=0, return_counts=True)
    bad = (counts != 2).sum()
    print(f"\nmesh check: {len(uk):,} unique verts, {len(uniq_e):,} edges, non-manifold/boundary edges: {bad:,} ({(counts==1).sum():,} open)")
    print("  watertight: YES" if bad == 0 else f"  watertight: NO ({bad:,} bad edges)")
    if trimesh is not None:
        try:
            m = trimesh.load_mesh(str(path), force="mesh")
            parts = m.split(only_watertight=False)
            print(f"  disconnected components: {len(parts)}", end="")
            if len(parts) > 1:
                sizes = sorted((round(p.extents[0],1), round(p.extents[1],1), round(p.extents[2],1)) for p in parts)
                print(f" — sizes (mm): {sizes[:8]}{' …' if len(sizes) > 8 else ''}")
            else:
                print()
            print(f"  winding consistent: {m.is_winding_consistent}")
        except Exception as exc:
            print(f"  trimesh: {exc}")
else:
    print("(no numpy: limited report)")
