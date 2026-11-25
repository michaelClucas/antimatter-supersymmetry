"""LW1 calc 3: test of the light-hadron meson/baryon degeneracy of Brodsky, de Teramond, Dosch, Lorce,
PLB 759, 171 (2016), arXiv:1604.06746 (chiral limit):
    mesons  M^2 = 4 lam (n + L_M) + 2 lam s
    baryons M^2 = 4 lam (n + L_B + 1) + 2 lam s,   partners have L_M = L_B + 1.
Paper's fit: sqrt(lam) = 0.523 GeV overall; mesons 0.524(23); baryons 0.509(15).

Here: independent least-squares fits of lam to I=1 mesons and to N/Delta baryons
(PDG 2024 masses, GeV, transcribed; state assignments follow the paper and are [conjecture] for
L>=1 baryons), then the mass mismatch of each predicted superpartner pair.
Pion excluded: it is the zero mode with no baryon partner (L_B = -1).
"""
import numpy as np

# (name, M [GeV], n, L, s)
mesons = [
    ("rho(770)",   0.7753, 0, 0, 1),
    ("b1(1235)",   1.2295, 0, 1, 0),
    ("a2(1320)",   1.3182, 0, 1, 1),
    ("pi2(1670)",  1.6706, 0, 2, 0),
    ("rho3(1690)", 1.6888, 0, 2, 1),
    ("a4(1970)",   1.967,  0, 3, 1),
    ("pi(1300)",   1.300,  1, 0, 0),
    ("rho(1450)",  1.465,  1, 0, 1),
]
baryons = [
    ("N(939)",     0.9389, 0, 0, 0),
    ("N(1440)",    1.440,  1, 0, 0),
    ("N(1520)",    1.515,  0, 1, 0),
    ("N(1680)",    1.685,  0, 2, 0),
    ("Delta(1232)", 1.232, 0, 0, 1),
    ("Delta(1700)", 1.710, 0, 1, 1),
    ("Delta(1950)", 1.930, 0, 2, 1),
]

def coef_m(n, L, s): return 4 * (n + L) + 2 * s
def coef_b(n, L, s): return 4 * (n + L + 1) + 2 * s

def fit(states, coef):
    x = np.array([coef(n, L, s) for _, _, n, L, s in states], float)
    y = np.array([m**2 for _, m, *_ in states])
    lam = (x @ y) / (x @ x)
    res = y - lam * x
    return lam, res, x, y

lm, rm, xm, ym = fit(mesons, coef_m)
lb, rb, xb, yb = fit(baryons, coef_b)
print(f"meson fit:  sqrt(lam) = {np.sqrt(lm):.3f} GeV, rms dM^2 = {np.sqrt(np.mean(rm**2)):.3f} GeV^2")
print(f"baryon fit: sqrt(lam) = {np.sqrt(lb):.3f} GeV, rms dM^2 = {np.sqrt(np.mean(rb**2)):.3f} GeV^2")
print(f"lam_meson / lam_baryon = {lm/lb:.3f}  (exact SUSY: 1)")
for (nm, m, n, L, s), r in zip(mesons, rm):
    print(f"  {nm:12s} M^2={m*m:5.3f}  fit={lm*coef_m(n,L,s):5.3f}  resid={r:+.3f}")
for (nm, m, n, L, s), r in zip(baryons, rb):
    print(f"  {nm:12s} M^2={m*m:5.3f}  fit={lb*coef_b(n,L,s):5.3f}  resid={r:+.3f}")

pairs = [("b1(1235)", "N(939)"), ("a2(1320)", "Delta(1232)"), ("pi2(1670)", "N(1520)"),
         ("rho3(1690)", "Delta(1700)"), ("a4(1970)", "Delta(1950)")]
M = {nm: m for nm, m, *_ in mesons + baryons}
print("\nsuperpartner pairs (meson L_M = baryon L_B + 1, same s, same n):")
fr = []
for a, b in pairs:
    d = (M[a] - M[b]) / ((M[a] + M[b]) / 2)
    fr.append(d)
    print(f"  {a:11s} vs {b:12s}: {M[a]:.3f} vs {M[b]:.3f} GeV  dM/M = {d:+.3f}  dM^2 = {M[a]**2-M[b]**2:+.3f} GeV^2")
fr = np.array(fr)
print(f"mean |dM/M| = {np.mean(np.abs(fr)):.3f}, mean dM/M = {np.mean(fr):+.3f}")
print("Comparison: an exact SUSY gives dM = 0; the hadronic 'breaking' is O(10%) of the mass, i.e. the")
print("breaking scale is of the same order as sqrt(lam) itself.")
