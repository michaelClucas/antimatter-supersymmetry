"""LW1 calc 4: subleading corrections to the heavy quark-diquark (superflavor) hyperfine relation.

Run from anywhere:  python c4_subleading.py   (imports alpha_s(MZ) from tools/sm_inputs.py)

What the literature actually provides (verified cycle 3, see ../LITCHECK.md):
  [1] Savage & Wise, PLB 248, 177 (1990): LO relation  D_B(QQq) = 3/4 D_M(Qbar q).
  [2] Brambilla, Vairo, Rosch, PRD 72, 034021 (2005), hep-ph/0506065, eq. (35):
        M(Xi*_QQ) - M(Xi_QQ) = 3/4 * [m_Q' c_F(Q)] / [m_Q c_F(Q')] * (M(P*_Q') - M(P_Q'))
                               * (1 + O(alpha_s^2, Lambda/m_Q, Lambda/m_Q'))
      They give eq. (36) 120 +- 40 MeV (cc) and eq. (37) 34 +- 4 MeV (bb), with c_F at NLL,
      m_c = M(J/psi)/2, m_b = M(Upsilon 1S)/2, and error Lambda/m_c ~ 0.3, Lambda/m_b ~ 0.1.
  [3] Fleming & Mehen, PRD 73, 034502 (2006), hep-ph/0509313: rederive the LO relation in NRQCD;
      leading corrections from 4-heavy-quark + usoft B operators, suppressed by alpha_s^2
      (and operators suppressed by alpha_s(m_Q)^2 v^2). No numerical value for the correction
      is given ("future publication"). Expect ~30% for charm.
  [4] Mehen & Tiburzi, PRD 74, 054505 (2006), hep-lat/0607023: chiral corrections to the
      relation are small ("rather insensitive to chiral corrections").
  So no closed-form numerical NLO correction exists in the literature. This script therefore
  (A) reproduces the LO numbers, (B) reproduces BVR eq. (35)-(37) at LL c_F, (C) calibrates the
  size of the 1/m_Q-type correction in the meson sector itself, and (D) fits the correction
  coefficient to dynamical lattice QCD in the charm sector and transports it to bottom under
  two scaling hypotheses. Labels: [established] = quoted from verified papers; [conjecture] =
  this script's own error model.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools"))
import sm_inputs as smi  # noqa: E402

# ---------------------------------------------------------------- inputs (MeV), PDG 2024
# Verified against PDG 2024 listings in cycle 3: D*0-D0 = 142.014(30); B*+-B+ = 45.34(20);
# Bs*-Bs = 48.5(1.4). D*+-D+ and Ds*-Ds taken from c2 (PDG 2024 fit values, not re-fetched).
DM = {"D0": (142.014, 0.030), "D+": (140.603, 0.015), "Ds": (143.85, 0.40),
      "B+": (45.34, 0.20), "Bs": (48.5, 1.4)}
M_JPSI, M_UPS = 3096.900, 9460.40          # PDG 2024
mc, mb = M_JPSI / 2 / 1000, M_UPS / 2 / 1000  # GeV, BVR convention
M_XICC_PP = (3621.55, math.hypot(0.23, 0.30))  # LHCb 1911.08594
M_OMCC = (3725.9, math.sqrt(1.0**2 + 0.2**2 + 0.4**2 + 0.6**2))  # LHCb 2609.21921 (2026, preprint)

# Lattice J=3/2 - J=1/2 splittings (MeV), dynamical unless noted. Uncorrelated-difference errors
# are used where the paper gives only masses (overestimates the error).
LAT_CC = {
    "Xi_cc  Brown+ 1409.0497 (2+1f, a->0)": (82.8, math.hypot(7.2, 5.8)),
    "Xi_cc  Alexandrou-Kallidonis 1704.02647 (Nf=2, phys. m_pi; masses only)":
        (3682 - 3606, math.sqrt(10**2 + 26**2 + 11**2 + 8**2)),
    "Xi_cc  PACS-CS Namekawa+ 1301.4743 (2+1f, phys. pt; masses only)":
        (3706 - 3603, math.hypot(28, 22)),
}
LAT_CC_QUENCHED = {"Xi_cc  Flynn-Mescia-Tariq hep-lat/0307025 (quenched)": (87.0, math.sqrt(13**2 + 13**2 + 2**2))}
LAT_OMCC = {"Omega_cc Brown+": (83.8, math.hypot(1.4, 5.3)),
            "Omega_cc Mathur-Padmanath 1807.00174": (76.0, math.hypot(6, 6))}
LAT_BB = {"Xi_bb    Brown+": (34.6, math.hypot(2.5, 7.4)),
          "Omega_bb Brown+": (35.7, math.hypot(1.3, 5.5))}


# ---------------------------------------------------------------- 2-loop alpha_s with thresholds
def beta01(nf):
    return 11 - 2 * nf / 3, 102 - 38 * nf / 3


def run_as(a0, mu0, mu1, nf, steps=4000):
    b0, b1 = beta01(nf)
    t0, t1 = math.log(mu0**2), math.log(mu1**2)
    h = (t1 - t0) / steps
    a = a0
    f = lambda a: -(b0 * a**2 / (4 * math.pi) + b1 * a**3 / (16 * math.pi**2))
    for _ in range(steps):  # RK4 in t = ln mu^2
        k1 = f(a); k2 = f(a + h * k1 / 2); k3 = f(a + h * k2 / 2); k4 = f(a + h * k3)
        a += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return a


def alpha_s(mu):
    a = smi.ALPHA_S_MZ
    if mu >= smi.MB:
        return run_as(a, smi.MZ, mu, 5)
    a_b = run_as(a, smi.MZ, smi.MB, 5)
    if mu >= smi.MC:
        return run_as(a_b, smi.MB, mu, 4)
    return run_as(run_as(a_b, smi.MB, smi.MC, 4), smi.MC, mu, 3)


def wmean(vals):
    w = [1 / e**2 for _, e in vals]
    m = sum(v * wi for (v, _), wi in zip(vals, w)) / sum(w)
    return m, (1 / sum(w)) ** 0.5


asc, asb = alpha_s(mc), alpha_s(mb)
# LL chromomagnetic coefficient ratio at a common scale mu < m_c: running between m_c and m_b has nf=4
cF_c_over_b = (asc / asb) ** (3 / beta01(4)[0])  # = (as(mc)/as(mb))^(9/25)

print("=" * 78)
print("Inputs: m_c = M(J/psi)/2 = %.4f GeV, m_b = M(Y1S)/2 = %.4f GeV" % (mc, mb))
print("        alpha_s(m_c) = %.4f, alpha_s(m_b) = %.4f (2-loop, alpha_s(MZ)=%.4f)" % (asc, asb, smi.ALPHA_S_MZ))
print("        LL c_F(c)/c_F(b) = (as(mc)/as(mb))^(9/25) = %.4f" % cF_c_over_b)

# ---------------------------------------------------------------- (A) LO
print("\n(A) LO superflavor, same flavour  [established: Savage-Wise 1990]")
LO = {}
for lab, key in [("Xi_cc++", "D0"), ("Xi_cc+", "D+"), ("Omega_cc", "Ds"), ("Xi_bb", "B+"), ("Omega_bb", "Bs")]:
    LO[lab] = 0.75 * DM[key][0]
    print("  %-9s = 3/4 x %7.3f = %6.1f MeV" % (lab, DM[key][0], LO[lab]))

# ---------------------------------------------------------------- (B) BVR eq. 35 cross-flavour
print("\n(B) BVR eq.(35) cross-flavour relation with LL c_F  [established formula; LL is this script's choice]")
xicc_from_B = 0.75 * (mb / mc) * cF_c_over_b * DM["B+"][0]
xibb_from_D = 0.75 * (mc / mb) / cF_c_over_b * DM["D0"][0]
print("  Xi_cc from D: %.1f MeV   Xi_cc from B: %.1f MeV   (BVR, NLL c_F: ~107 and ~133)" % (LO["Xi_cc++"], xicc_from_B))
print("  Xi_bb from B: %.1f MeV   Xi_bb from D: %.1f MeV   (BVR: ~34 and ~27)" % (LO["Xi_bb"], xibb_from_D))
bvr_cc = 0.5 * (LO["Xi_cc++"] + xicc_from_B)
print("  BVR prescription: Xi_cc = average +- 30%% = %.0f +- %.0f MeV  (BVR eq.36: 120 +- 40)" % (bvr_cc, 0.3 * bvr_cc))
print("                    Xi_bb = B-based  +- 10%% = %.1f +- %.1f MeV (BVR eq.37: 34 +- 4)" % (LO["Xi_bb"], 0.1 * LO["Xi_bb"]))

# ---------------------------------------------------------------- (C) meson-sector calibration
print("\n(C) Size of the heavy-quark correction measured in the meson sector  [conjecture: used as a proxy]")
pred_ratio = (mc / mb) / cF_c_over_b  # LO HQET: Delta_B/Delta_D = (m_c/m_b) c_F(b)/c_F(c)
meas_ratio = DM["B+"][0] / DM["D0"][0]
print("  Delta_B/Delta_D: LO-HQET (LL) %.4f, measured %.4f -> relative 1/m correction %.1f%%"
      % (pred_ratio, meas_ratio, 100 * (meas_ratio / pred_ratio - 1)))
print("  So the charm hyperfine already deviates from HQET scaling by O(15-25%) on the meson side alone.")

# ---------------------------------------------------------------- (D) lattice-calibrated power correction
print("\n(D) R_Q = Delta(QQq)/Delta(Qbar q) = 3/4 (1 + kappa / s_Q)   [conjecture: one-parameter correction model]")
print("  Lattice J=3/2-J=1/2 splittings (MeV):")
for k, (v, e) in {**LAT_CC, **LAT_CC_QUENCHED, **LAT_OMCC, **LAT_BB}.items():
    print("    %-72s %6.1f +- %4.1f" % (k, v, e))
xcc, excc = wmean(list(LAT_CC.values()))
print("  Dynamical Xi_cc weighted mean = %.1f +- %.1f MeV (quenched excluded)" % (xcc, excc))
Rcc, eRcc = xcc / DM["D0"][0], excc / DM["D0"][0]
print("  R_cc = %.3f +- %.3f   (Brown+ Table XX: 0.58(6));  LO 0.750" % (Rcc, eRcc))

# Two scaling hypotheses for the correction: s_Q = m_Q (HQET Lambda/m_Q), s_Q = m_Q v_Q
# (diquark-size, Lambda r_QQ ~ Lambda/(m_Q v)). v^2 ~ 0.3 (cc), 0.1 (bb): standard NRQCD estimates.
v = {"c": 0.3**0.5, "b": 0.1**0.5}
res_bb = []
for name, sc, sb in [("1/m_Q", mc, mb), ("1/(m_Q v)", mc * v["c"], mb * v["b"])]:
    kappa = (Rcc / 0.75 - 1) * sc
    ekappa = eRcc / 0.75 * sc
    Rbb = 0.75 * (1 + kappa / sb)
    eRbb = 0.75 * ekappa / sb
    # residual higher-order term: (kappa/s)^2 at the bottom scale, taken as an extra 1-sigma error
    resid = 0.75 * (kappa / sb) ** 2
    for lab, key in [("Xi_bb", "B+"), ("Omega_bb", "Bs")]:
        d = Rbb * DM[key][0]
        ed = math.sqrt((eRbb * DM[key][0]) ** 2 + (resid * DM[key][0]) ** 2 + (Rbb * DM[key][1]) ** 2)
        if lab == "Xi_bb":
            res_bb.append((d, ed))
        print("  scaling %-10s kappa = %+.3f +- %.3f GeV -> R_bb = %.3f -> %-8s = %5.1f +- %3.1f MeV"
              % (name, kappa, ekappa, Rbb, lab, d, ed))
lo_ = min(d - e for d, e in res_bb); hi_ = max(d + e for d, e in res_bb)
xbb_c = 0.5 * (lo_ + hi_); xbb_e = 0.5 * (hi_ - lo_)
print("  Envelope over both scalings: Xi_bb* - Xi_bb = %.1f +- %.1f MeV  (LO 34.0; lattice Brown+ 34.6 +- 7.8)" % (xbb_c, xbb_e))
# Corrections that do not follow either power law (alpha_s^2(m_b v) terms, BVR/FM) are not captured
# by the one-parameter model; add BVR's 10% bottom estimate as an independent error.
xbb_unmod = 0.10 * xbb_c
xbb_e = math.hypot(xbb_e, xbb_unmod)
print("  + unmodelled alpha_s^2(m_b v) term (10%%, BVR): Xi_bb* - Xi_bb = %.1f +- %.1f MeV" % (xbb_c, xbb_e))
print("  Pull vs LO 34.0: %.1f sigma; vs Brown+ lattice: %.1f sigma"
      % ((LO["Xi_bb"] - xbb_c) / xbb_e, (34.6 - xbb_c) / math.hypot(xbb_e, 7.8)))

# ---------------------------------------------------------------- (E) charm: what can honestly be said
print("\n(E) Charm summary")
eft_cc = (LO["Xi_cc++"], 0.3 * LO["Xi_cc++"])
print("  EFT-only (LO +- 30%% power counting, BVR/FM estimate): Xi_cc* - Xi_cc = %.0f +- %.0f MeV" % eft_cc)
print("  BVR eq.(36) (avg of D- and B-based):                   120 +- 40 MeV")
print("  Lattice-QCD (dynamical mean):                          %.0f +- %.0f MeV" % (xcc, excc))
print("  Shift lattice vs LO: %.0f%% (inside the 30%% band, pull %.1f sigma_EFT)"
      % (100 * (xcc / LO["Xi_cc++"] - 1), (xcc - LO["Xi_cc++"]) / eft_cc[1]))
m_lo = M_XICC_PP[0] + LO["Xi_cc++"]
m_lat = M_XICC_PP[0] + xcc
print("  Xi_cc*++ mass: LO %.0f +- %.0f MeV;  lattice-calibrated %.0f +- %.0f MeV" % (m_lo, eft_cc[1], m_lat, excc))
print("  Omega_cc*+ mass (using LHCb 2026 Omega_cc+ = %.1f): LO %.0f, lattice-calibrated %.0f MeV"
      % (M_OMCC[0], M_OMCC[0] + LO["Omega_cc"], M_OMCC[0] + Rcc * DM["Ds"][0]))

# ---------------------------------------------------------------- (F) decay channel kinematics
MPI0, MPIP = 134.977, 139.570
print("\n(F) Decay channel: Xi_cc*++ -> Xi_cc++ pi0 needs Delta > %.1f MeV." % MPI0)
for lab, d in [("LO", LO["Xi_cc++"]), ("lattice", xcc), ("EFT upper 1 sigma", eft_cc[0] + eft_cc[1])]:
    print("  %-18s Delta = %5.1f -> %s" % (lab, d, "strong decay open" if d > MPI0 else "only M1 radiative Xi_cc gamma"))
print("  Falsifier (updated): EFT band [%.0f, %.0f] MeV at 1 sigma, [%.0f, %.0f] at 2 sigma."
      % (eft_cc[0] - eft_cc[1], eft_cc[0] + eft_cc[1], eft_cc[0] - 2 * eft_cc[1], eft_cc[0] + 2 * eft_cc[1]))
print("  Sharper test (lattice-calibrated): Xi_bb* - Xi_bb = %.0f +- %.0f MeV." % (xbb_c, xbb_e))
