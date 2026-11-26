"""LW1 cycle 6, c6b: is the "96% SU(3)-breaking cancellation" (c5c) evidence for superflavor at all?

Referee 1 (cycle 5), finding 3. c5c found
    r_SF = [Omega_cc - <Xi_cc>] - [D_s - <D>] = +4.0 MeV  (4% of the ~101 MeV SU(3) breaking).
Controls:
 (1) Additive quark model (AQM): M = sum_i m_i + C(hadron type). Every s-for-u/d substitution shifts the mass by
     m_s - m_u, whatever the rest of the hadron is. So the AQM predicts r = 0 for EVERY pair of
     strange/non-strange differences, superflavor partners or not. It has SU(3) breaking and no superflavor.
 (2) Data: the same residual for pairs that are NOT superflavor partners (reference D_s - <D>):
     heavy-quark spin partners (D*), heavy-flavour partners (B), and hadrons with light diquarks.
 (3) A model with SU(3) breaking and no superflavor relation imposed: De Rujula-Georgi-Glashow (DGG) hyperfine
     model, M = sum m_i + C_M/B + A_M/B sum_{i<j} S_i.S_j/(m_i m_j), with independent meson and baryon
     coefficients (superflavor would tie them, A_B = A_M/2 in this normalisation). Fitted to ground-state
     mesons and baryons NOT containing two heavy quarks; then predicts r_SF.
Also: corrected Xi_cc+ error (finding 4) and the isospin decomposition with the numerology removed (finding 5).
Masses: PDG 2024 central values (transcribed; last digits [uncertain], irrelevant at the 1 MeV level used here),
LHCb Xi_cc++ (1911.08594), Xi_cc+ (PRL 137, 021902 (2026)), Omega_cc+ (2609.21921, preprint).
"""
import numpy as np
from scipy.optimize import least_squares

avg = lambda *x: float(np.mean(x))
M = {  # MeV
    "rho": 775.26, "omega": 782.66, "Kst": avg(891.67, 895.55), "phi": 1019.461,
    "D": avg(1864.84, 1869.66), "Dst": avg(2006.85, 2010.26), "Ds": 1968.35, "Dsst": 2112.2,
    "B": avg(5279.41, 5279.72), "Bst": 5324.71, "Bs": 5366.93, "Bsst": 5415.4,
    "N": avg(938.272, 939.565), "Delta": 1232.0, "Lambda": 1115.683, "Sigma": avg(1189.37, 1192.642, 1197.449),
    "Sigmast": avg(1382.83, 1383.7, 1387.2), "Xi": avg(1314.86, 1321.71), "Xist": avg(1531.80, 1535.0),
    "Omega": 1672.45,
    "Lc": 2286.46, "Sc": avg(2453.97, 2452.65, 2453.75), "Scst": avg(2518.41, 2517.4, 2518.48),
    "Xic": avg(2467.71, 2470.44), "Xicp": avg(2578.2, 2578.7), "Xicst": avg(2645.10, 2646.16),
    "Omc": 2695.2, "Omcst": 2765.9,
    "Lb": 5619.60, "Sb": avg(5810.56, 5815.64), "Sbst": avg(5830.32, 5834.74), "Xib": avg(5791.9, 5797.0),
    "Xibp": 5935.02, "Xibst": avg(5952.3, 5955.33), "Omb": 6045.8,
    "Xicc": avg(3621.55, 3619.97), "Omcc": 3725.9,
}

# ----------------------------------------------------------------------------- (0) errors (finding 4)
e_xpp = np.hypot(0.23, 0.30)
e_xp_up, e_xp_dn = np.sqrt(0.83**2 + 0.26**2 + 1.90**2), np.sqrt(0.83**2 + 0.26**2 + 1.30**2)
e_xp = 0.5 * (e_xp_up + e_xp_dn)
e_om_unc = np.sqrt(1.0**2 + 0.2**2)          # stat, syst
e_om_ext, e_om_tau = 0.6, 0.4                # ext (Xi_cc++ mass, correlated), lifetime (correlated in sign with Xi_cc+)
e_mes = np.sqrt(0.07**2 + 0.25 * (0.05**2 + 0.05**2))
# r = Om - (Xpp + Xp)/2 - mesons. Correlated pieces added linearly in the worst-sign combination:
#  ext: Om moves with Xpp -> coefficient (1 - 1/2) on 0.6 (Omega's ext error tracks the Xi_cc++ mass)
#  lifetime: Om tau-term (0.4) and Xp tau-term (~1.6) same sign -> coefficient |0.4 - 0.5 x 1.6| (partial cancel);
#  conservative choice below: treat them as uncorrelated (larger) and quote both.
e_unc = np.sqrt(e_om_unc**2 + e_om_tau**2 + e_om_ext**2 + (0.5 * e_xpp) ** 2 + (0.5 * e_xp) ** 2 + e_mes**2)
e_cor = np.sqrt(e_om_unc**2 + (0.5 * e_xpp) ** 2 + (0.5 * np.sqrt(0.83**2 + 0.26**2)) ** 2 + e_mes**2
                + (0.5 * e_om_ext) ** 2 + (e_om_tau - 0.5 * 1.6) ** 2)
mes = M["Ds"] - M["D"]
bar = M["Omcc"] - M["Xicc"]
r_sf = bar - mes
print("(0) Superflavor residual with corrected errors")
print(f"   Xi_cc+ total error: +{e_xp_up:.2f} / -{e_xp_dn:.2f} MeV (symmetrised {e_xp:.2f}); c5c used 1.6 (lifetime term only)")
print(f"   D_s - <D> = {mes:.1f}, Omega_cc - <Xi_cc> = {bar:.1f}, r_SF = {r_sf:+.1f} MeV")
print(f"   error: all pieces uncorrelated {e_unc:.1f} MeV; with ext/lifetime correlations {e_cor:.1f} MeV."
      f" Quoted: r_SF = {r_sf:+.1f} +- {max(e_unc, e_cor):.1f} MeV ({100*r_sf/mes:.0f}% of the breaking)")

# ----------------------------------------------------------------------------- (1)+(2) data controls
print("\n(1) AQM prediction: r = 0 for every pair below (no superflavor in the AQM).")
print("(2) Observed strange-minus-nonstrange differences and residual r = Delta_s(X) - Delta_s(D) [MeV]")
pairs = [
    ("D_s - D           (reference)", "Ds", "D", "ref"),
    ("Omega_cc - Xi_cc  superflavor partner of D", "Omcc", "Xicc", "SF"),
    ("D_s* - D*         HQ spin partner", "Dsst", "Dst", "HQSS"),
    ("B_s - B           HQ flavour partner", "Bs", "B", "HQFS"),
    ("B_s* - B*         HQ spin+flavour", "Bsst", "Bst", "HQFS"),
    ("K* - rho          light meson", "Kst", "rho", "none"),
    ("phi - K*          light meson", "phi", "Kst", "none"),
    ("Sigma* - Delta    light baryon", "Sigmast", "Delta", "none"),
    ("Xi* - Sigma*      light baryon", "Xist", "Sigmast", "none"),
    ("Omega - Xi*       light baryon", "Omega", "Xist", "none"),
    ("Xi_c' - Sigma_c   light spin-1 diquark", "Xicp", "Sc", "none"),
    ("Xi_c* - Sigma_c*  light spin-1 diquark", "Xicst", "Scst", "none"),
    ("Omega_c - Xi_c'   light spin-1 diquark", "Omc", "Xicp", "none"),
    ("Omega_c* - Xi_c*  light spin-1 diquark", "Omcst", "Xicst", "none"),
    ("Xi_b' - Sigma_b   light spin-1 diquark", "Xibp", "Sb", "none"),
    ("Xi_b* - Sigma_b*  light spin-1 diquark", "Xibst", "Sbst", "none"),
    ("Omega_b - Xi_b'   light spin-1 diquark", "Omb", "Xibp", "none"),
    ("Xi_c - Lambda_c   light spin-0 diquark", "Xic", "Lc", "none"),
    ("Xi_b - Lambda_b   light spin-0 diquark", "Xib", "Lb", "none"),
]
res = {}
for lab, a, b, kind in pairs:
    d = M[a] - M[b]
    res[lab] = (d - mes, kind)
    print(f"   {lab:44s} {d:7.1f}   r = {d - mes:+6.1f}")
none = np.array([abs(v) for v, k in res.values() if k == "none"])
hq = np.array([abs(v) for v, k in res.values() if k in ("HQSS", "HQFS")])
print(f"   non-superflavor, non-heavy-symmetry pairs: n = {len(none)}, median |r| = {np.median(none):.1f},"
      f" min {none.min():.1f}, max {none.max():.1f} MeV")
print(f"   heavy-quark spin/flavour partners of D: |r| = {', '.join(f'{x:.1f}' for x in hq)} MeV")
print(f"   superflavor pair: |r| = {abs(r_sf):.1f} MeV")
print("   Note: the 'none' pairs with the largest |r| (Xi_c - Lambda_c, Xi_b - Lambda_b, Sigma* - Delta) are those")
print("   where the s quark enters a light diquark whose spin-spin energy depends on 1/(m_u m_s) vs 1/m_u^2.")

# ----------------------------------------------------------------------------- (3) DGG fit
print("\n(3) DGG hyperfine model with free meson/baryon coefficients (no superflavor relation imposed)")
# spin factors sum_{i<j} S_i.S_j/(m_i m_j) as functions of masses (u,s,c,b); see WORK.md sec. 20
def mes_hf(m1, m2, J):
    return (-0.75 if J == 0 else 0.25) / (m1 * m2)


def bar_hf(kind, mq, mX, mY=None):
    """kind: 'N','Delta' (all equal), 'L' (light pair (q,q) spin 0, third X), 'S' / 'Sst' (pair spin 1, J=1/2 / 3/2),
    'A' (pair (q,Y) of unequal mass spin 0, third X), 'Sp'/'Spst' (pair (q,Y) spin 1, third X)."""
    if kind == "N":
        return -0.75 / mq**2
    if kind == "Delta":
        return 0.75 / mq**2
    if kind == "L":
        return -0.75 / mq**2
    if kind == "S":
        return 0.25 / mq**2 - 1.0 / (mq * mX)
    if kind == "Sst":
        return 0.25 / mq**2 + 0.5 / (mq * mX)
    if kind == "A":
        return -0.75 / (mq * mY)
    if kind == "Sp":
        return 0.25 / (mq * mY) - 0.5 * (1 / (mq * mX) + 1 / (mY * mX))
    if kind == "Spst":
        return 0.25 / (mq * mY) + 0.25 * (1 / (mq * mX) + 1 / (mY * mX))
    raise ValueError(kind)


def model(p, mesmass=None):
    mu, ms, mc, mb, AM, AB, CM, CB = p
    m = {"u": mu, "s": ms, "c": mc, "b": mb}
    xu, xs = (mu, ms) if mesmass is None else mesmass   # Griffiths-style: separate light masses in mesons
    th = {
        "rho": (2 * xu, AM * mes_hf(xu, xu, 1), CM), "Kst": (xu + xs, AM * mes_hf(xu, xs, 1), CM),
        "phi": (2 * xs, AM * mes_hf(xs, xs, 1), CM),
        "D": (xu + mc, AM * mes_hf(xu, mc, 0), CM), "Dst": (xu + mc, AM * mes_hf(xu, mc, 1), CM),
        "Ds": (xs + mc, AM * mes_hf(xs, mc, 0), CM), "Dsst": (xs + mc, AM * mes_hf(xs, mc, 1), CM),
        "B": (xu + mb, AM * mes_hf(xu, mb, 0), CM), "Bst": (xu + mb, AM * mes_hf(xu, mb, 1), CM),
        "Bs": (xs + mb, AM * mes_hf(xs, mb, 0), CM), "Bsst": (xs + mb, AM * mes_hf(xs, mb, 1), CM),
        "N": (3 * mu, AB * bar_hf("N", mu, mu), CB), "Delta": (3 * mu, AB * bar_hf("Delta", mu, mu), CB),
        "Lambda": (2 * mu + ms, AB * bar_hf("L", mu, ms), CB), "Sigma": (2 * mu + ms, AB * bar_hf("S", mu, ms), CB),
        "Sigmast": (2 * mu + ms, AB * bar_hf("Sst", mu, ms), CB),
        "Xi": (mu + 2 * ms, AB * bar_hf("S", ms, mu), CB), "Xist": (mu + 2 * ms, AB * bar_hf("Sst", ms, mu), CB),
        "Omega": (3 * ms, AB * bar_hf("Delta", ms, ms), CB),
    }
    for Q, tag in [("c", "c"), ("b", "b")]:
        mQ = m[Q]
        L = {"c": ("Lc", "Sc", "Scst", "Xic", "Xicp", "Xicst", "Omc", "Omcst"),
             "b": ("Lb", "Sb", "Sbst", "Xib", "Xibp", "Xibst", "Omb", None)}[Q]
        th[L[0]] = (2 * mu + mQ, AB * bar_hf("L", mu, mQ), CB)
        th[L[1]] = (2 * mu + mQ, AB * bar_hf("S", mu, mQ), CB)
        th[L[2]] = (2 * mu + mQ, AB * bar_hf("Sst", mu, mQ), CB)
        th[L[3]] = (mu + ms + mQ, AB * bar_hf("A", mu, mQ, ms), CB)
        th[L[4]] = (mu + ms + mQ, AB * bar_hf("Sp", mu, mQ, ms), CB)
        th[L[5]] = (mu + ms + mQ, AB * bar_hf("Spst", mu, mQ, ms), CB)
        th[L[6]] = (2 * ms + mQ, AB * bar_hf("S", ms, mQ), CB)
        if L[7]:
            th[L[7]] = (2 * ms + mQ, AB * bar_hf("Sst", ms, mQ), CB)
    # doubly charmed (predictions only): (cc) spin 1 + light q, J = 1/2
    th["Xicc"] = (2 * mc + mu, AB * (0.25 / mc**2 - 1.0 / (mu * mc)), CB)
    th["Omcc"] = (2 * mc + ms, AB * (0.25 / mc**2 - 1.0 / (ms * mc)), CB)
    return {k: (a + b + c) for k, (a, b, c) in th.items()}


fit_keys = [k for k in M if k not in ("Xicc", "Omcc", "omega")]
ctrl = [(lab, a, b) for lab, a, b, kind in pairs[2:]]
variants = {
    "3a common light masses + C_M, C_B": (lambda q: model(q), [330, 500, 1600, 4950, 1.6e7, 0.8e7, 0.0, 0.0],
                                          [100, 100, 300, 300, 1e7, 1e7, 100, 100]),
    "3b Griffiths: separate meson/baryon light masses, C = 0":
        (lambda q: model([q[0], q[1], q[2], q[3], q[4], q[5], 0, 0], mesmass=(q[6], q[7])),
         [360, 540, 1600, 4950, 1.6e7, 0.8e7, 310, 480], [100, 100, 300, 300, 1e7, 1e7, 100, 100]),
}
rsf_models = []
for name, (fn, p0, xs_) in variants.items():
    sol = least_squares(lambda q: np.array([fn(q)[k] - M[k] for k in fit_keys]), p0, x_scale=xs_)
    pred = fn(sol.x)
    rms = np.sqrt(np.mean(sol.fun**2))
    r_m = (pred["Omcc"] - pred["Xicc"]) - (pred["Ds"] - pred["D"])
    rsf_models.append(r_m)
    dev = np.array([((pred[a] - pred[b]) - (pred["Ds"] - pred["D"])) - res[lab][0] for lab, a, b in ctrl])
    print(f"   [{name}] fit to {len(fit_keys)} hadrons (Xi_cc, Omega_cc excluded): rms {rms:.1f} MeV;"
          f" A_B/A_M = {sol.x[5]/sol.x[4]:.3f} (a superflavor tie would be 0.5)")
    print(f"      predicted Xi_cc = {pred['Xicc']:.0f}, Omega_cc = {pred['Omcc']:.0f} MeV (obs {M['Xicc']:.0f}, {M['Omcc']:.0f});"
          f" D_s - D = {pred['Ds']-pred['D']:.1f} (obs {mes:.1f})")
    print(f"      r_SF(model) = {r_m:+.1f} MeV vs observed {r_sf:+.1f};  model error on the 17 control residuals:"
          f" rms {np.sqrt(np.mean(dev**2)):.1f} MeV")
# also: AQM-only version
solA = least_squares(lambda q: np.array([model([q[0], q[1], q[2], q[3], 0, 0, q[4], q[5]])[k] - M[k] for k in fit_keys]),
                     [330, 500, 1600, 4950, 0, 0], x_scale=[100, 100, 300, 300, 100, 100])
print(f"   [AQM, A = 0] fit rms = {np.sqrt(np.mean(solA.fun**2)):.0f} MeV; r(any pair) = 0 identically;"
      f" error on the control residuals: rms {np.sqrt(np.mean(np.array([res[l][0] for l, _, _ in ctrl])**2)):.1f} MeV")

print("\n   Verdict [established for these models]: the AQM (no superflavor) predicts r_SF = 0; the two DGG fits")
print(f"   (no superflavor tie) predict r_SF = {rsf_models[0]:+.1f} and {rsf_models[1]:+.1f} MeV. The observed {r_sf:+.1f} +- 1.6")
print("   MeV is reproduced by the AQM with no superflavor, so it is NOT evidence for superflavor. The data do show")
print("   a pattern: pairs where the s quark sits next to a heavy source (D_s*, B_s, Omega_cc) have |r| <~ 14 MeV,")
print("   pairs where it shares a light diquark have |r| = 10-80 MeV. That pattern is heavy-quark symmetry")
print("   (suppressed light-heavy spin coupling), of which superflavor is one instance; it does not single it out.")

# ----------------------------------------------------------------------------- isospin (finding 5)
print("\n(4) Isospin decomposition, numerology removed")
a = 1869.66 - 1864.84; ea = np.hypot(0.05, 0.05)
b = 3619.97 - 3621.55; eb = np.hypot(e_xp, e_xpp)
Ec = (a - b) / 2.0; dl = (2 * a + b) / 3.0
print(f"   D+ - D0 = {a:+.2f} +- {ea:.2f};  Xi_cc+ - Xi_cc++ = {b:+.2f} +- {eb:.2f} MeV  ({abs(b)/eb:.1f} sigma from zero)")
print(f"   two-parameter, zero-d.o.f. solve: E_c = {Ec:.1f} +- {np.hypot(ea, eb)/2:.1f}, delta = {dl:.1f} +- "
      f"{np.hypot(2*ea/3, eb/3):.1f} MeV")
print(f"   The opposite sign of the two isospin splittings is a {abs(b)/eb:.1f} sigma statement. delta is an effective hadronic")
print("   parameter (current-mass difference + light-quark EM self-energy + isospin dependence of the hyperfine term);")
print("   it is not compared with the MS-bar m_d - m_u. [speculation: any physical reading of E_c, delta]")
