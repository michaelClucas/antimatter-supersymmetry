"""Classification of sector reweightings of the one-loop gauge beta coefficients, and the empirical kill of each.

Setup. b_i = sum_s w_s b_i^s over sectors s (gluon loops, W loops, Higgs loops, Weyl multiplets Q, u^c, d^c, L, e^c).
"Antiparticle-only" weights: a vacuum-polarisation bubble always contains one particle and one antiparticle line
(both time orderings, fs_residues.py), so a weight x on the antiparticle states of species X can only mean
"the X loop counts (1+x)/2 times". Every antiparticle reweighting is a species reweighting with w = (1+x)/2,
and conversely x = 2w - 1.

One-loop unification (B-test) condition: L(w) = (b2-b3) - R (b1-b2) = 0, R = (A2-A3)/(A1-A2) measured at MZ.
L is LINEAR in the weights: L(w) = sum_s w_s l_s. The unifying weights form a hyperplane in weight space.
For one sector alone: w_s = 1 - L(1)/l_s.

Empirical handles. Unitarity ties a loop weight to a rate: the optical theorem gives Im Pi_VV(s) = sum over pair
final states, and the one-loop beta coefficient is the asymptotic coefficient of that absorptive part (dispersion
relation). A weight that changes the loop but not the rate violates unitarity, so it is not an SM-equivalent theory.
A weight that changes both changes a measured rate.
  * Z partial widths (ALEPH, DELPHI, L3, OPAL, SLD et al., Phys. Rept. 427, 257 (2006), hep-ex/0509008):
      Gamma_had = 1744.4 +- 2.0 MeV, Gamma_ll = 83.984 +- 0.086 MeV, Gamma_inv = 499.0 +- 1.5 MeV, SM agrees.
    LO: Gamma(Z -> f fbar) ~ N_c (w_L gL^2 + w_R gR^2), gL = T3 - Q s2, gR = -Q s2. Only ratios to the SM are used.
  * R-ratio below the Z: R ~ N_c sum_q Q_q^2 (w_L + w_R)/2.
  * alpha_s running between m_tau and MZ: at one loop, holding alpha_s(m_tau) fixed,
    Delta alpha_s^-1(MZ) = -Delta b3/(2 pi) ln(MZ/m_tau), 5 active flavours.
  * Higgs couplings to W/Z: kappa_V = 1 within 5-10% (ATLAS, Nature 607, 52 (2022); CMS, Nature 607, 60 (2022)).
"""
import math
from fractions import Fraction as Fr
import sm_path  # noqa: F401
import sm_inputs as smi

a1, a2, a3 = smi.gauge_couplings_mz()
A = [1 / a1, 1 / a2, 1 / a3]
R = (A[1] - A[2]) / (A[0] - A[1])
F = float


def bweyl(d3, d2, Y):
    """b_i contribution of one Weyl field: 2/3 T(R), U(1) GUT-normalised T = 3/5 Y^2."""
    return [Fr(2, 3) * Fr(3, 5) * Y ** 2 * d3 * d2, Fr(2, 3) * (Fr(1, 2) if d2 == 2 else 0) * d3,
            Fr(2, 3) * (Fr(1, 2) if d3 == 3 else 0) * d2]


mult = {"Q": (3, 2, Fr(1, 6)), "u^c": (3, 1, Fr(-2, 3)), "d^c": (3, 1, Fr(1, 3)), "L": (1, 2, Fr(-1, 2)),
        "e^c": (1, 1, Fr(1))}
bF = {k: bweyl(*v) for k, v in mult.items()}
groups = {"Q": ["Q"], "u^c": ["u^c"], "d^c": ["d^c"], "L": ["L"], "e^c": ["e^c"], "5bar = d^c+L": ["d^c", "L"],
          "10 = Q+u^c+e^c": ["Q", "u^c", "e^c"], "all quarks": ["Q", "u^c", "d^c"], "all leptons": ["L", "e^c"],
          "all fermions (uniform)": list(mult)}
sectors = {
    "gluon loops (SU3 gauge+ghost)": ([Fr(0), Fr(0), Fr(-11)], {}),
    "W loops (SU2 gauge+ghost)": ([Fr(0), Fr(-22, 3), Fr(0)], {}),
    "all gauge loops (w_V)": ([Fr(0), Fr(-22, 3), Fr(-11)], {}),
    "Higgs doublet loops (w_S)": ([Fr(1, 10), Fr(1, 6), Fr(0)], {}),
}
for g, ms in groups.items():
    sectors[f"fermions: {g}, 3 gens"] = ([3 * sum(bF[m][i] for m in ms) for i in range(3)], {"ms": ms, "ngen": 3})
for g in ("Q", "all quarks"):
    sectors[f"fermions: {g}, 3rd gen only"] = ([sum(bF[m][i] for m in groups[g]) for i in range(3)],
                                               {"ms": groups[g], "ngen": 1})

bSM = [Fr(41, 10), Fr(-19, 6), Fr(-7)]


def ell(b):
    return F(b[1] - b[2]) - R * F(b[0] - b[1])


L0 = ell(bSM)
print(f"R measured at MZ = {R:.4f} (alpha_em^-1 = {smi.ALPHA_EM_INV_MZ}); SM L(1) = {L0:.4f}  (unification needs L = 0)")
print("l-values of complete SU(5) multiplets (per generation): "
      f"5bar {ell([bF['d^c'][i] + bF['L'][i] for i in range(3)]):.1e}, "
      f"10 {ell([bF['Q'][i] + bF['u^c'][i] + bF['e^c'][i] for i in range(3)]):.1e}  -> both drop out (GQW 1974)")

s2 = 0.2315  # sin^2 theta_eff, LO estimate; only ratios to the SM are used
# (flavour, Nc, T3, Q, generation index, left multiplet, right multiplet)
zf = [("u", 3, .5, 2 / 3, 1, "Q", "u^c"), ("c", 3, .5, 2 / 3, 2, "Q", "u^c"), ("d", 3, -.5, -1 / 3, 1, "Q", "d^c"),
      ("s", 3, -.5, -1 / 3, 2, "Q", "d^c"), ("b", 3, -.5, -1 / 3, 3, "Q", "d^c"),
      ("e", 1, -.5, -1, 1, "L", "e^c"), ("mu", 1, -.5, -1, 2, "L", "e^c"), ("tau", 1, -.5, -1, 3, "L", "e^c")]


def widths(w, gens):
    def wt(m, gen):
        return w.get(m, 1) if (m is not None and gen in gens) else 1
    had = sum(n * (wt(l, g) * (t - q * s2) ** 2 + wt(r, g) * (q * s2) ** 2) for f, n, t, q, g, l, r in zf[:5])
    ll = sum(n * (wt(l, g) * (t - q * s2) ** 2 + wt(r, g) * (q * s2) ** 2) for f, n, t, q, g, l, r in zf[5:]) / 3
    inv = sum(wt("L", g) * 0.25 for g in (1, 2, 3))
    Rr = sum(n * q * q * (wt(l, g) + wt(r, g)) / 2 for f, n, t, q, g, l, r in zf[:5])
    return had, ll, inv, Rr


W0 = widths({}, ())
err = {"had": 2.0 / 1744.4, "ll": 0.086 / 83.984, "inv": 1.5 / 499.0}
lnmt = math.log(smi.MZ / smi.MTAU)
L1T = math.log(1000 / smi.MZ)

print("\nEach sector reweighted alone (others = 1). w = loop weight giving one-loop unification; x = 2w-1 is the same")
print("thing written as a weight on the antiparticle states only. M_U, alpha_U^-1 from the one-loop alpha1=alpha2 crossing.\n")
for name, (b, meta) in sectors.items():
    l = ell(b)
    if abs(l) < 1e-12:
        print(f"{name:40s}: l = 0 -> drops out of the B-test; NO weight of this sector can unify")
        continue
    dw = -L0 / l
    w = 1 + dw
    bb = [F(bSM[i]) + dw * F(b[i]) for i in range(3)]
    t = 2 * math.pi * (A[0] - A[1]) / (bb[0] - bb[1])
    aU = A[0] - bb[0] / (2 * math.pi) * t
    head = f"{name:40s}: w = {w:+.3f} (x = {2 * w - 1:+.2f}); b = ({bb[0]:+.2f}, {bb[1]:+.2f}, {bb[2]:+.2f})"
    print(head + (f"; M_U = 10^{math.log10(smi.MZ * math.exp(t)):.2f} GeV, alpha_U^-1 = {aU:.1f}" if t > 0
                  else "; alpha1=alpha2 crossing below MZ"))
    kills = []
    if t <= 0 or aU <= 0 or t > math.log(smi.M_PLANCK / smi.MZ):
        kills.append("B-test satisfied only formally: the 'meeting point' is beyond M_Pl or at negative alpha^-1, "
                     "i.e. no physical unification at all")
    elif t > 0:
        MU = smi.MZ * math.exp(t)
        tau = MU ** 4 * aU ** 2 / 0.938272 ** 5 * 6.582119569e-25 / 3.15576e7
        kills.append(f"(conditional, SM has no X boson) d=6 proton lifetime at M_U ~ {tau:.0e} yr "
                     f"({'excluded' if tau < 2.4e34 else 'allowed'} by F1, 2.4e34 yr)")
    if w < 0:
        kills.append("negative loop weight = negative pair-production rate (optical theorem) / wrong-sign kinetic term")
    if meta:
        gens = (1, 2, 3) if meta["ngen"] == 3 else (3,)
        had, ll, inv, Rr = widths({m: w for m in meta["ms"]}, gens)
        r = [had / W0[0], ll / W0[1], inv / W0[2], Rr / W0[3]]
        sig = max(abs(r[0] - 1) / err["had"], abs(r[1] - 1) / err["ll"], abs(r[2] - 1) / err["inv"])
        kills.append(f"Gamma_had x{r[0]:.3f}, Gamma_ll x{r[1]:.3f}, Gamma_inv x{r[2]:.3f} (N_nu = {3 * r[2]:.2f}; "
                     f"meas. 2.984+-0.008), R x{r[3]:.3f}: up to {sig:.0f} sigma from LEP Z-pole data")
        # quark part of Delta b3 with 5 active flavours below m_t
        q_ms = [m for m in meta["ms"] if m in ("Q", "u^c", "d^c")]
        if q_ms:
            per_gen = sum(F(bF[m][2]) for m in q_ms)
            n_active = 2.5 if meta["ngen"] == 3 else 0.5  # 5 flavours = 2.5 'generations'; 3rd gen: b only
            d3 = dw * per_gen * n_active
            da = -d3 / (2 * math.pi) * lnmt
            kills.append(f"alpha_s(MZ) evolved from fixed alpha_s(m_tau) -> {1 / (A[2] + da):.4f} (meas. 0.1180+-0.0009)")
    if name.startswith("gluon") or name.startswith("all gauge"):
        db3 = -11 * dw
        b3_5 = -11 * w + 10 / 3
        da = -db3 / (2 * math.pi) * lnmt
        kills.append(f"b3(5 flavours) = {b3_5:+.2f}; alpha_s(MZ) evolved from fixed alpha_s(m_tau) -> {1 / (A[2] + da):.4f} "
                     "(meas. 0.1180+-0.0009)")
        if b3_5 > 0:
            a_tau = 1 / (A[2] + b3_5 / (2 * math.pi) * lnmt)
            kills.append(f"asymptotic freedom lost: alpha_s(m_tau) = {a_tau:.3f} < alpha_s(MZ); measured alpha_s(m_tau) ~ 0.3")
    if name.startswith("Higgs"):
        kills.append(f"as a doublet-coupling rescaling: kappa_V ~ sqrt(w) = {math.sqrt(w):.2f} (meas. 1 within 5-10%)")
        kills.append(f"as a multiplicity: {w:.1f} doublets = BSM (A1); the known version (Willenbrock hep-ph/0302168)")
        kills.append(f"as a bare loop weight: violates unitarity; V* -> (W_L W_L, Z_L h, W_L h) rate would be {w:.1f}x SM "
                     "(equivalence theorem); measured VH rates and kappa_V consistent with SM")
        d1, d2 = (w - 1) * 0.1 / (2 * math.pi) * L1T, (w - 1) / 6 / (2 * math.pi) * L1T
        kills.append(f"direct effect on running MZ -> 1 TeV: Delta alpha_1^-1 = {d1:.2f}, Delta alpha_2^-1 = {d2:.2f} "
                     f"({d2 / A[1] * 100:.1f}%): not tested by any measurement used here -> no clean kill from running alone")
    if name.startswith("W loops"):
        d2 = -(w - 1) * (-22 / 3) / (2 * math.pi) * L1T
        kills.append(f"Delta b2 = {(w - 1) * (-22 / 3):+.2f}; MZ -> 1 TeV Delta alpha_2^-1 = {d2:+.2f} ({abs(d2) / A[1] * 100:.1f}%): "
                     "no clean empirical kill from running; killed by equivalence (gauge+ghost weight fixed by BRST/"
                     "Slavnov-Taylor; the vertices are the LEP2-tested triple gauge couplings)")
    for k in kills:
        print(f"{'':42s}-> {k}")
