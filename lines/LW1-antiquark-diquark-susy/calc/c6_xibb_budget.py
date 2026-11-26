"""LW1 cycle 6, c6d: Xi_bb* - Xi_bb error budget including the spread over lattice charm inputs
(referee 1 cycle 5, finding 7), and the strong-decay thresholds for Xi_cc*++.

Same one-parameter model as c4 (D): R_Q = Delta(QQq)/Delta(Qbar q) = 3/4 (1 + kappa/s_Q), s_Q = m_Q or m_Q v_Q.
c4 fixed kappa from the dynamical Xi_cc mean only. Here kappa is fixed from EACH dynamical charm input
(Xi_cc from three groups; Omega_cc from two, with the D_s hyperfine as the meson reference), and the spread
of the transported Xi_bb value is added to the budget. [conjecture: the correction model]
"""
import math

mc, mb = 3096.900 / 2000, 9460.40 / 2000          # GeV, BVR convention (c4)
v = {"c": 0.3 ** 0.5, "b": 0.1 ** 0.5}
DM = {"D0": 142.014, "Ds": 143.85, "B+": 45.34}
INPUTS = [  # (label, Delta_lat, err, meson reference)
    ("Xi_cc  Brown+ 1409.0497", 82.8, math.hypot(7.2, 5.8), "D0"),
    ("Xi_cc  Alexandrou-Kallidonis 1704.02647", 76.0, math.sqrt(10**2 + 26**2 + 11**2 + 8**2), "D0"),
    ("Xi_cc  PACS-CS 1301.4743", 103.0, math.hypot(28, 22), "D0"),
    ("Omega_cc Brown+ 1409.0497", 83.8, math.hypot(1.4, 5.3), "Ds"),
    ("Omega_cc Mathur-Padmanath 1807.00174", 76.0, math.hypot(6, 6), "Ds"),
]
print("Xi_bb* - Xi_bb transported from each charm lattice input (MeV):")
print(f"  {'input':42s} {'R_cc':>6s}   1/m_Q    1/(m_Q v)")
cent = []
for lab, d, e, ref in INPUTS:
    R = d / DM[ref]
    out = []
    for sc, sb in [(mc, mb), (mc * v["c"], mb * v["b"])]:
        kappa = (R / 0.75 - 1) * sc
        out.append(0.75 * (1 + kappa / sb) * DM["B+"])
    cent += out
    print(f"  {lab:42s} {R:6.3f}   {out[0]:5.1f}    {out[1]:5.1f}")
lo, hi = min(cent), max(cent)
mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
c4_c, c4_e = 30.4, 3.7
tot = math.sqrt(c4_e**2 + (half) ** 2 / 3)   # spread treated as a flat distribution of half-width `half`
print(f"  range over inputs and scalings: [{lo:.1f}, {hi:.1f}] -> centre {mid:.1f}, half-width {half:.1f}")
print(f"  c4 value 30.4 +- 3.7; adding the input spread (flat, sigma = half-width/sqrt3 = {half/math.sqrt(3):.1f}):"
      f"  Xi_bb* - Xi_bb = {c4_c:.0f} +- {tot:.0f} MeV")
print(f"  Compare: LO 34.0, BVR eq.(37) 34 +- 4, Brown+ lattice 34.6 +- 7.8. Within 1 sigma of all three:"
      " the number does not discriminate. It is a refinement of BVR, not an independent test.")
print("  Kappa calibrated on Brown+ charm and compared to Brown+ bottom is a correlated comparison (same ensembles).")

print("\nXi_cc*++ strong-decay thresholds (MeV):")
Xpp, Xp, mpi0, mpip = 3621.55, 3619.97, 134.977, 139.570
print(f"  Xi_cc++ pi0 : Delta > {mpi0:.1f};   Xi_cc+ pi+ : Delta > {Xp + mpip - Xpp:.1f}")
for lab, d in [("LO", 106.5), ("lattice mean", 83.5), ("EFT 1 sigma upper", 106.5 + 32), ("EFT 2 sigma upper", 106.5 + 64)]:
    print(f"  {lab:18s} Delta = {d:5.1f}: {'pi decays open' if d > mpi0 else 'M1 only (Xi_cc gamma)'}")
print("  The band 107 +- 32 is a power-counting estimate, not a Gaussian error; the [43, 170] '2 sigma' band is naive.")
