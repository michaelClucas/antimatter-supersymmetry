"""L01b cycle 4, task 2: regulator-independent formulation of the boson-pair vs top-sea matching.

Two quantities, both defined from the tree-level field-dependent spectrum M_i^2(phi), no regulator in the definition:

 R2 (quadratic level): C = (1/2) d^2/dphi^2 STr M^2(phi).  Every one-loop regulator that is applied uniformly to all
    species turns the per-species weight into n_i * d^2 M_i^2/dphi^2 times ONE universal constant: Lambda^2 (cutoff),
    sum_j c_j Lambda_j^2 ln Lambda_j^2 (Pauli-Villars), or the residue of the pole at d = 2 (dimensional
    regularization; Veltman, Acta Phys. Polon. B 12, 437 (1981)). So R2 = C_bos/|C_ferm| is the same number in all
    three. In DR at d = 4 there is no such term at all: R2 has no d = 4 DR observable attached [established].
 R4 (logarithmic level): the phi^4 coefficient of STr M^4(phi), i.e. the coefficient of ln(mu) in the one-loop
    effective potential. This is regulator independent (universal one-loop log) and equals the non-wave-function
    part of 16 pi^2 beta_lambda^(1). Its lam*g^2 cross terms are gauge dependent (Nielsen identity, they multiply
    m_G^2 ~ V'/phi), so we keep only the gauge-invariant pieces: lam^0 (g^4, y^4) and lam^2.
      R4 = [24 lam^2 + (3/8)(2 g^4 + (g^2+g'^2)^2)] / [6 y_t^4 + 6 y_b^4 + 2 y_tau^4]
    In exact SUSY (m_stop = m_top) the top's y_t^4 term is cancelled by the stops: STr M^4 = 0.
"""
import math
import os
import sys

import sympy as sp
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools')))
import sm_inputs as smi  # noqa: E402
from rg_sm import run  # noqa: E402

out = []


def P(s=""):
    print(s)
    out.append(str(s))


# ------------------------------------------------------------------ Part A: three regulators, species weights
P("Part A. Per-species weight of the quadratically sensitive term in three regulators")
k, L, M2, d, L1, L2 = sp.symbols('k Lambda M2 d Lambda1 Lambda2', positive=True)
Icut = sp.integrate(2 * sp.pi**2 * k**3 / (k**2 + M2), (k, 0, L)) / (2 * sp.pi)**4
Icut_L2 = sp.limit(sp.expand(Icut) / L**2, L, sp.oo)
P(f"  cutoff:  I(M^2) = int^Lambda d^4k/(2pi)^4 1/(k^2+M^2);  coefficient of Lambda^2 = {Icut_L2}  (M-independent)")
# Pauli-Villars: two regulators with sum c_j = 0, sum c_j m_j^2 = 0 (c_0 = 1, m_0^2 = M2)
c1, c2 = sp.symbols('c1 c2')
m1, m2 = M2 + L1**2, M2 + L2**2
sol = sp.solve([1 + c1 + c2, M2 + c1 * m1 + c2 * m2], [c1, c2])
Ipv = -(M2 * sp.log(M2) + sol[c1] * m1 * sp.log(m1) + sol[c2] * m2 * sp.log(m2)) / (16 * sp.pi**2)
# leading large-Lambda piece: set Lambda2 = 2 Lambda1 = 2 Lambda, expand in 1/Lambda
lam_ = sp.symbols('lam_', positive=True)
Ipv_s = sp.simplify(Ipv.subs({L1: lam_, L2: 2 * lam_}))
lead = sp.limit(Ipv_s / lam_**2, lam_, sp.oo)
P(f"  Pauli-Villars (2 regulators, Lambda, 2 Lambda): leading term = Lambda^2 x {sp.nsimplify(sp.simplify(lead))}"
  f"  (M-independent: d/dM2 = {sp.simplify(sp.diff(lead, M2))})")
A0 = sp.gamma(1 - d / 2) * M2**(d / 2 - 1) / (4 * sp.pi)**(d / 2)
res = sp.residue(A0, d, 2)
P(f"  dim. reg.: A0 = Gamma(1-d/2)(M^2)^(d/2-1)/(4pi)^(d/2); residue at d = 2: {sp.simplify(res)}  (M-independent)")
P("  => weight of species i in d^2V/dphi^2 is n_i * d^2 M_i^2/dphi^2 x (universal constant) in all three.")
P("     Ratios of the C_i (hence R2, the 34% / 79%) are identical in cutoff, PV and DR(d=2 pole). [established]")
P("     Caveat: only at one loop; the 2-loop Lambda^2 coefficient is scheme dependent (Einhorn-Jones, PRD 46,")
P("     5206 (1992)), and at d = 4 in DR the term is absent.")

# ------------------------------------------------------------------ Part B: STr M^4 gauge dependence (Fermi gauge)
P("\nPart B. STr M^4 gauge dependence: Fermi-gauge mixed block, coefficient of 1/k^4 in ln det")
kk, xi, Mm, mG2, x = sp.symbols('k xi M mG2 x', positive=True)
detF = sp.expand((kk**4 + kk**2 * mG2 + xi * Mm**2 * mG2).subs(kk, 1 / sp.sqrt(x)) * x**2)
ser = sp.series(sp.log(detF), x, 0, 3).removeO()
str4 = sp.simplify(-2 * ser.coeff(x, 2))  # ln det = sum m^2 x - (1/2) sum m^4 x^2 + ...
P(f"  mixed (A_L,G) block: sum m^4 = {sp.expand(str4)}  -> xi term proportional to m_G^2 = lam(phi^2 - v^2)")
P("  so d^2/dphi^2 STr M^4 at phi = v is xi-dependent (contains 2 m_G^2' M^2' ~ xi lam g^2 v^2), while the lam^0 and")
P("  lam^2 parts of the phi^4 coefficient are not. R4 below keeps only those. [established; Nielsen NPB 101, 173 (1975)]")

# ------------------------------------------------------------------ Part C: numbers and running
def split(cc):
    g, gy, l = cc['g2'], cc['gY'], cc['lam']
    W2 = 1.5 * g**2 + 2 * l
    S2 = 0.75 * (g**2 + gy**2) + 4 * l
    W4 = 0.75 * g**4 + 4 * l**2              # W (3 pol., 2 charges) + G+-: 2*[6 (g^2/4)^2 + 2 lam^2]
    S4 = 0.375 * (g**2 + gy**2)**2 + 20 * l**2  # Z + G0 (2 lam^2) + h (18 lam^2)
    T2 = 6 * cc['yt']**2
    F2 = T2 + 6 * cc['yb']**2 + 2 * cc['ytau']**2
    T4 = 6 * cc['yt']**4
    F4 = T4 + 6 * cc['yb']**4 + 2 * cc['ytau']**4
    return W2, S2, T2, F2, W4, S4, T4, F4


P("\nPart C. Fractions of the top (and all-fermion) sea cancelled by boson pairs, 3-loop MS-bar running")
P("  R2 = (C_W + C_Z+h)/C_top   [quadratic; = Lambda^2 / PV / DR(d=2) coefficient]")
P("  R4 = (W + Z + h + G pieces of beta_lambda, lam^0 and lam^2 terms)/(6 y_t^4)   [log; gauge + regulator invariant]")
f = run(nloops=3, mu_max=1e32)
P(f"  {'log10 mu':>8s} {'R2_top':>7s} {'R2_ferm':>7s} {'R4_top':>7s} {'R4_ferm':>7s} {'R4 ch':>7s} {'R4 sc':>7s} {'lam':>8s}")
for lmu in (math.log10(smi.MT), 4, 6, 8, 10, 12, 14, 16, 18, math.log10(smi.M_PLANCK), 20, 22):
    W2, S2, T2, F2, W4, S4, T4, F4 = split(f(10**lmu))
    P(f"  {lmu:8.2f} {(W2+S2)/T2:7.4f} {(W2+S2)/F2:7.4f} {(W4+S4)/T4:7.4f} {(W4+S4)/F4:7.4f}"
      f" {W4/T4:7.4f} {S4/T4:7.4f} {f(10**lmu)['lam']:+8.5f}")


def cross(which, nl=3, **kw):
    ff = run(nloops=nl, mu_max=1e32, **kw)

    def h(l):
        W2, S2, T2, F2, W4, S4, T4, F4 = split(ff(10**l))
        return (W2 + S2 - F2) if which == 2 else (W4 + S4 - F4)
    return brentq(h, 4, 31.5)


P("\n  Crossing scales (boson pairs = fermion seas), all fermions in the denominator:")
for nl in (1, 2, 3):
    P(f"    {nl}-loop RGEs: R2 = 1 at log10 mu = {cross(2, nl):.3f};  R4 = 1 at log10 mu = {cross(4, nl):.3f}")
P("  Input dependence of the R4 crossing (3-loop):")
for kw in (dict(Mt=smi.MT - 0.29), dict(Mt=smi.MT + 0.29), dict(als=smi.ALPHA_S_MZ - 0.0009),
           dict(als=smi.ALPHA_S_MZ + 0.0009), dict(Mh=smi.MH - 0.11), dict(Mh=smi.MH + 0.11)):
    P(f"    {kw}: log10 mu(R4=1) = {cross(4, 3, **kw):.3f}")
P(f"  (reference: log10 M_Pl = {math.log10(smi.M_PLANCK):.3f}, reduced M_Pl = {math.log10(2.435e18):.3f})")

W2, S2, T2, F2, W4, S4, T4, F4 = split(f(smi.MT))
P("\n  Charged-pair / self-conjugate split at M_t (gauge invariant in both formulations):")
P(f"    R2: charged W(+G+-) {W2/T2:.4f}, self-conjugate Z(+G0)+h {S2/T2:.4f}")
P(f"    R4: charged W(+G+-) {W4/T4:.4f}, self-conjugate Z(+G0)+h {S4/T4:.4f}")

with open(os.path.join(HERE, 'c4_regulator_running_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
