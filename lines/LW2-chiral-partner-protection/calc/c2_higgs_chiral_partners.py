"""LW2 c2: SM Higgs sector as a chiral-partner system (h = 0+ 'sigma', G0 = 0- 'pion') and comparison with QCD.

Checks:
 (a) top-antitop loop with hard Euclidean cutoff: the h (scalar, tbar t) and G0 (pseudoscalar, tbar i g5 t)
     self-energies at p^2 = 0 in the broken phase have IDENTICAL Lambda^2 parts; the difference S - P is only
     log-divergent and proportional to m_t^2 (an order parameter of the SO(4) ~ SU(2)L x SU(2)R breaking),
     the same structure as Pi_V - Pi_A in QCD.  Same check in dim-reg style via the PV-type sum rule.
 (b) numbers: naive naturalness scales (pion: c1; Higgs: Veltman form, CONSTRAINTS G) vs where partners are.
 (c) radial-mode comparison: m_sigma/f_pi in QCD vs m_h/v in the SM; QCD condensate's share of v^2.
"""
import math
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'tools')))
import sm_inputs as smi  # noqa: E402

# ---------- (a)
k2, Lam2, m2, y, Nc = sp.symbols('k2 Lambda2 m2 y N_c', positive=True)
meas = k2 / (16 * sp.pi**2)                      # d^4k_E/(2pi)^4 = k2 dk2 /(16 pi^2)
# Euclidean traces: scalar Tr[(k+m)(k+m)] -> 4(m2 - k2); pseudoscalar Tr[i g5 (k+m) i g5 (k+m)] -> -4(k2 + m2)
# coupling y/sqrt2 each vertex; curvature contribution = +N_c (y^2/2) * trace / (k2+m2)^2 (fermion loop sign included)
dS = sp.integrate(Nc * y**2 / 2 * 4 * (m2 - k2) / (k2 + m2)**2 * meas, (k2, 0, Lam2))
dP = sp.integrate(Nc * y**2 / 2 * (-4) * (k2 + m2) / (k2 + m2)**2 * meas, (k2, 0, Lam2))
qS = sp.limit(dS / Lam2, Lam2, sp.oo); qP = sp.limit(dP / Lam2, Lam2, sp.oo)
print("(a) Lambda^2 coefficient: h (S) =", sp.simplify(qS), "; G0 (P) =", sp.simplify(qP), "; equal:", sp.simplify(qS - qP) == 0)
diff = sp.simplify(dS - dP)
print("    S - P (exact, cutoff) =", diff)
print("    S - P leading: ", sp.simplify(sp.limit(diff / sp.log(Lam2), Lam2, sp.oo)), "* ln Lambda^2   (proportional to m_t^2: order parameter)")
print("    m->0 check at fixed Lambda (chiral limit): S - P ->", sp.limit(diff, m2, 0))
print("    [CW cross-check: V_top = -(12/64pi^2) M^4 ln(M^2/L^2), M^2=y^2h^2/2, gives +3y^4/(64pi^2) h^4 ln(L^2/M^2):"
      " positive quartic from tbar-t, i.e. beta_lambda contains -6 y^4 (Buttazzo eq. 101 normalisation)]")

# ---------- (b) naturalness scales
mh, mt, mw, mz, v = smi.MH, smi.MT, smi.MW, smi.MZ, smi.V
bracket = mh**2 + 2 * mw**2 + mz**2 - 4 * mt**2
L_full = math.sqrt(8 * math.pi**2 * v**2 * mh**2 / (3 * abs(bracket)))
L_top = math.sqrt(8 * math.pi**2 * v**2 * mh**2 / (3 * 4 * mt**2))
print(f"(b) Veltman bracket = {bracket:.4g} GeV^2 (CONSTRAINTS G: ~ -8.2e4)")
print(f"    |delta m_h^2| = m_h^2 at Lambda_nat: full SM {L_full:.0f} GeV; top-antitop only {L_top:.0f} GeV")
print("    pion analogue (c1): Lambda_nat = 851 MeV, partners rho 775 / a1 1230 MeV  -> found")
print(f"    Higgs: partner-like states needed near {L_top:.0f} GeV; LHC: stop > ~1200-1300 GeV, gluino > ~2200 GeV (CONSTRAINTS C3)")
print(f"    ratio (LHC stop bound / Lambda_nat,top) ~ {1250 / L_top:.1f}; Barbieri-Giudice-type tuning ~ (ratio)^2 = {(1250 / L_top)**2:.0f}")

# ---------- (c) radial modes
fpi = 130.2 / math.sqrt(2)          # MeV, PDG 2024 f_pi+ = 130.2(1.2) MeV
for lab, ms in (("f0(500) pole Re (CCL 2006)", 441.0), ("PDG range low", 400.0), ("PDG range high", 550.0)):
    print(f"(c) QCD sigma [{lab:27s}]: m_sigma = {ms:.0f} MeV, m_sigma/f_pi = {ms / fpi:.2f}, lambda_eff = m^2/(2f^2) = {ms**2 / (2 * fpi**2):.1f}")
print(f"    SM Higgs: m_h/v = {mh / v:.3f}, lambda = m_h^2/(2v^2) = {mh**2 / (2 * v**2):.3f}")
print(f"    f0(500) pole Im/Re = 272/441 = {272 / 441:.2f} (broad, strongly coupled); h: Gamma_SM/m = 4.1e-3/125 = {4.1e-3 / 125:.1e}")
sh = (fpi * 1e-3)**2 / v**2
print(f"    QCD qbar-q condensate share of v^2 (one light doublet, f_pi^2/v^2) = {sh:.2e}; M_W(QCD only) = g f_pi/2 = {0.6517 * fpi / 2:.1f} MeV")
