"""LW1 cycle 6, c6c: corrected supermultiplet census (referee 1 cycle 5, findings 2 and 8).

Takes the c5d table unchanged (imported) and applies the corrections:
 - row chi_c2(3556) / "Xi_cc(3621) as 3/2+": the J=3/2 Xi_cc* is unobserved -> baryon status PRED (ruling R1).
 - EXO / QQB tetraquark tallies counted only in rows whose baryon is observed.
 - J^P assignment conflicts flagged (slot counted as filled in c5d): D(2600) "assumed 2-" but PDG lists
   D1*(2600) as 1-; D0(2550) "assumed 1+" but LHCb assigns 0-.
 - max |dM| per sector reported with the pair that produces it.
"""
import contextlib
import io
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import c5_hadronic_supermultiplets as c5d  # noqa: E402

R = [list(r) for r in c5d.R]
CONFLICT = {"D(2600)?n": "PDG: D1*(2600) is 1-, slot needs 2-", "D0(2550)": "LHCb: 0-, slot needs 1+"}
for r in R:
    if r[4] == "Xi_cc(3621) as 3/2+":
        r[4], r[6] = "Xi_cc*(3/2+) unobs.", "PRED"
both = [r for r in R if r[3] == "OBS" and r[6] == "OBS"]
print(f"Rows: {len(R)}.  Both members observed: {len(both)}  (c5d: 31; Xi_cc* row moved to PRED)")
print(f"  baryon predicted/unobserved: {sum(r[6] == 'PRED' for r in R)};  meson predicted: {sum(r[3] == 'PRED' for r in R)};"
      f"  meson unconfirmed: {sum(r[3] == 'UNC' for r in R)}")
conf = [r for r in both if r[1] in CONFLICT]
print(f"  of the {len(both)}, meson-baryon rows whose meson has a J^P conflict: {len(conf)} "
      f"({'; '.join(r[1] + '/' + r[4] + ' [' + CONFLICT[r[1]] + ']' for r in conf)})")
print(f"  both observed and no meson J^P conflict: {len(both) - len(conf)} / {len(R)}")
tconf = [r for r in R if r[7] in CONFLICT]
print(f"  tetraquark-slot J^P conflicts (slot counted as filled in c5d): "
      f"{'; '.join(r[7] + ' in row ' + r[1] + '/' + r[4] + ' [' + CONFLICT[r[7]] + ']' for r in tconf)}")
print("\nPer-sector statistics (rows with both observed):")
for sec in ["light", "charm", "bottom", "2heavy"]:
    rows = [r for r in both if r[0] == sec]
    if not rows:
        continue
    dm = np.array([r[2] - r[5] for r in rows])
    frac = np.array([(r[2] - r[5]) / (0.5 * (r[2] + r[5])) for r in rows])
    j = int(np.argmax(np.abs(dm)))
    print(f"  {sec:7s} n={len(rows):2d}  mean |dM/M| = {np.mean(np.abs(frac)):.3f}  mean |dM| = {np.mean(np.abs(dm)):4.0f} MeV"
          f"  max |dM| = {abs(dm[j]):4.0f} MeV ({rows[j][1]} / {rows[j][4]})")
h1 = [r for r in both if r[1] == "h1(1170)"][0]
print(f"  (h1/N: |dM| = {abs(h1[2]-h1[5]):.0f} MeV; c5 WORK.md mislabelled the 254 MeV maximum as h1/N)")
print("\nTetraquark slots:")
for code in ["EXO", "DEB", "QQB", "PRED", "NONE"]:
    all_ = [r for r in R if r[9] == code]
    obsb = [r for r in all_ if r[6] == "OBS"]
    print(f"  {code:4s}: all rows {len(all_):2d};  rows with observed baryon {len(obsb):2d}"
          + (f"  ({', '.join(r[7] for r in obsb)})" if code == "EXO" else ""))
print("\nSelection bias: the Nielsen-Brodsky tables were assembled from already known hadrons, so a high observed")
print("fraction is expected by construction. The count has no evidential weight for SUSY result #6.")
