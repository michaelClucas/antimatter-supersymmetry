"""L01b cycle 4, task 1: gauge dependence of the species split of the Higgs Lambda^2 coefficient.

Method. The Lambda^2 (quadratically divergent) part of the one-loop Higgs 2-point function at p = 0 is
    Sigma_hh(0)|_{Lambda^2} = (Lambda^2 / 32 pi^2) d^2/dphi^2 STr M^2(phi)   (Euclidean cutoff),
where STr M^2(phi) is the coefficient of 1/k^2 in the large-k expansion of  sum_sectors (+-) ln det K_sector(k; phi)
(K = quadratic fluctuation operator in momentum space, bosons +, ghosts and fermions -).
We use C = (1/2) d^2/dphi^2 STr M^2 at phi = v, the line's normalization (C_top = -6 y_t^2).

Gauge-fixing families (one abelian sector: vector A with M(phi) = c*phi, Goldstone G with m_G^2(phi)):
  F  Fermi:              L_gf = (1/2 xi)(dA)^2,                ghosts massless
  R  ordinary R_xi:      L_gf = (1/2 xi)(dA - xi M_v G)^2,      M_v = M(v) fixed;  ghost mass^2 xi M_v M(phi)
  B  background R_xi:    L_gf = (1/2 xi)(dA - xi M(phi) G)^2,   ghost mass^2 xi M(phi)^2
Longitudinal-A / Goldstone block (k = |k| Euclidean), from the kinetic mixing (M - M_gf) A.dG:
    K_L = [[k^2/xi + M^2,  i k (M - M_gf)], [-i k (M - M_gf),  k^2 + m_G^2 + xi M_gf^2]]
transverse: 3 x (k^2 + M^2). Fermi: M_gf = 0;  R: M_gf = M_v;  B: M_gf = M(phi).
Charged sector W+-, G+-: 2 real copies with c^2 = g^2/4; neutral Z, G0: 1 copy with c^2 = (g^2+g'^2)/4.
Photon: massless, no h coupling: 0.  Higgs h: m_h^2(phi) = 3 lam phi^2 - lam v^2.  Top: -12 x y^2 phi^2 / 2.
V = lam (|H|^2 - v^2/2)^2 (rg_sm.py convention), m_G^2(phi) = lam (phi^2 - v^2).
"""
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools')))
import sm_inputs as smi  # noqa: E402
from rg_sm import run  # noqa: E402

out = []


def P(s=""):
    print(s)
    out.append(str(s))


k, phi, v, xi, c, lam, g, gp, yt = sp.symbols('k phi v xi c lambda g gp y_t', positive=True)
x = sp.symbols('x', positive=True)  # x = 1/k^2

# ---------------------------------------------------------------- Part 0: diagram-level propagator identities
P("Part 0. Propagator identities (Euclidean, R_xi vector propagator D = [delta - (1-xi) kk/(k^2+xi M^2)]/(k^2+M^2))")
M = sp.symbols('M', positive=True)
trD = (4 - (1 - xi) * k**2 / (k**2 + xi * M**2)) / (k**2 + M**2)   # seagull: g^{mu nu} D_{mu nu}
kDk = (k**2 - (1 - xi) * k**4 / (k**2 + xi * M**2)) / (k**2 + M**2)  # V-G bubble numerator k.D.k
P(f"  tr D - [3/(k^2+M^2) + xi/(k^2+xi M^2)] = {sp.simplify(trD - (3/(k**2+M**2) + xi/(k**2+xi*M**2)))}")
P(f"  k.D.k - xi k^2/(k^2+xi M^2)            = {sp.simplify(kDk - xi*k**2/(k**2+xi*M**2))}")
P("  => vector seagull Lambda^2 weight (3 + xi); V-G bubble Lambda^2 weight proportional to xi;"
  " Landau (xi=0): bubble has no Lambda^2.")


# ---------------------------------------------------------------- Part 1: STr M^2(phi) per piece, per family
def inv_k2_coeff(expr):
    """coefficient of 1/k^2 in the large-k expansion of ln(expr/leading)."""
    e = sp.expand(expr.subs(k, 1 / sp.sqrt(x)))
    lead = sp.limit(e * x**2, x, 0)  # det ~ k^4 * lead
    ser = sp.series(sp.log(sp.simplify(e * x**2 / lead)), x, 0, 2).removeO()
    return sp.simplify(ser.coeff(x, 1))


def sector_pieces(fam, Mphi, Mv, mG2):
    """Return dict of STr M^2 contributions (one real vector + one real Goldstone + its ghost pair)."""
    Mgf = {'F': 0, 'R': Mv, 'B': Mphi}[fam]
    KL = sp.Matrix([[k**2 / xi + Mphi**2, sp.I * k * (Mphi - Mgf)],
                    [-sp.I * k * (Mphi - Mgf), k**2 + mG2 + xi * Mgf**2]])
    mixed = inv_k2_coeff(KL.det())
    ghost_m2 = {'F': 0, 'R': xi * Mv * Mphi, 'B': xi * Mphi**2}[fam]
    # split of the mixed block by diagram class (each is a piece of the 1/k^2 coefficient)
    pieces = {
        'V transverse seagull (3 pol.)': 3 * Mphi**2,
        'V longitudinal seagull (xi)': xi * Mphi**2,
        'G seagull + GF mass': mG2 + xi * Mgf**2,
        'V-G mixing bubble': sp.simplify(mixed - xi * Mphi**2 - mG2 - xi * Mgf**2),
        'ghosts (-2 dof)': -2 * ghost_m2,
    }
    return pieces


mG2 = lam * (phi**2 - v**2)
sectors = {
    'charged (W+-, G+-, c+-)': (2, g * phi / 2, g * v / 2),
    'neutral (Z, G0, cZ)': (1, sp.sqrt(g**2 + gp**2) * phi / 2, sp.sqrt(g**2 + gp**2) * v / 2),
}

P("\nPart 1. STr M^2(phi) pieces and C_i = (1/2) d^2/dphi^2 at phi = v, three gauge families")
results = {}
for fam, fname in (('F', 'Fermi'), ('R', 'ordinary R_xi'), ('B', 'background-field R_xi')):
    P(f"\n  --- {fname} gauge ---")
    for sname, (mult, Mphi, Mv) in sectors.items():
        pcs = sector_pieces(fam, Mphi, Mv, mG2)
        tot_str = 0
        tot_C = 0
        for pname, val in pcs.items():
            val = sp.simplify(mult * val)
            Ci = sp.simplify(sp.Rational(1, 2) * sp.diff(val, phi, 2).subs(phi, v))
            tot_str += val
            tot_C += Ci
            P(f"    {sname:24s} {pname:32s} STr: {str(val):38s} C: {Ci}")
        tot_str = sp.simplify(tot_str)
        tot_C = sp.simplify(tot_C)
        results[(fam, sname)] = tot_C
        P(f"    {sname:24s} {'SECTOR TOTAL':32s} STr: {str(sp.factor(tot_str)):38s} C: {tot_C}"
          f"   d/dxi STr = {sp.simplify(sp.diff(tot_str, xi))}")

Ch = sp.Rational(1, 2) * sp.diff(3 * lam * phi**2 - lam * v**2, phi, 2)
Ctop = sp.Rational(1, 2) * sp.diff(-12 * yt**2 * phi**2 / 2, phi, 2)
P(f"\n  h (gauge independent at one loop: no gauge vertex in its own seagull): C_h = {Ch};  top: C_t = {Ctop}")
for fam in 'FRB':
    assert sp.simplify(results[(fam, 'charged (W+-, G+-, c+-)')] - (sp.Rational(3, 2) * g**2 + 2 * lam)) == 0
    assert sp.simplify(results[(fam, 'neutral (Z, G0, cZ)')] - (sp.Rational(3, 4) * (g**2 + gp**2) + lam)) == 0
P("  CHECK: in all three families and for all xi (xi_W, xi_Z independent):")
P("     charged sector  C_ch = 3/2 g^2 + 2 lam          (xi-independent)")
P("     neutral sector  C_n  = 3/4 (g^2+g'^2) + lam,  + h: 3 lam  => self-conjugate C_sc = 3/4(g^2+g'^2) + 4 lam")
P("     total C = 9/4 g^2 + 3/4 g'^2 + 6 lam - 6 y_t^2   (Veltman, gauge independent)")
P("  Individual diagram classes ARE xi-dependent (see per-piece C above): e.g. ordinary R_xi, charged sector,")
P("  vector seagull = (3+xi) g^2/2 and V-G bubble = -xi g^2/2;  background R_xi: vector = (3+xi) g^2/2,")
P("  Goldstone = 2 lam + xi g^2/2, ghosts = -xi g^2.  Landau gauge (xi = 0) is the unique member of each family")
P("  in which every diagram class equals its 'physical' gauge-invariant grouping.")

# ---------------------------------------------------------------- Part 2: gauge-invariant grouping
P("\nPart 2. Gauge-invariant groupings (any U(1)_em-preserving linear gauge, any xi_W, xi_Z, xi_gamma)")
P("  (a) by physical particle, Goldstones absorbed (W = 3 pol. incl. eaten G+-; Z incl. eaten G0):")
P("        C_W = 3/2 g^2 + 2 lam,   C_Z = 3/4(g^2+g'^2) + lam,   C_h = 3 lam,   C_gamma = 0,   C_t = -6 y_t^2")
P("      => 'charged pairs' (W+W-) = C_W, 'self-conjugate' (Z, h, gamma) = C_Z + C_h: identical to the line's")
P("         Landau-gauge split, because each sector sum is xi-independent separately.")
P("  (b) by coupling structure: transverse-vector part (g^2 terms) vs scalar-curvature part (lam terms):")
P("        both xi-independent sector by sector (the mixed block + ghosts sum to m_G^2 in every family).")
P("  (c) NOT gauge invariant: 'W seagull alone', 'Goldstone alone', 'V-G bubble', 'ghosts'.")
P("  Limit of validity: a gauge fixing that breaks U(1)_em (e.g. axial n.A with charged-neutral mixing) makes")
P("  'charged sector' ill-defined field-by-field; the grouping by physical charge eigenstates is still fixed by")
P("  the SU(2)xU(1) group theory (W1,W2 vs W3/B; G1,G2 vs G3) and the total is invariant.")

# ---------------------------------------------------------------- Part 3: numbers at M_t, M_Pl
f = run(nloops=3, mu_max=1e20)


def fr(cc):
    g2_, gy_, l_, t_, b_, ta_ = cc['g2'], cc['gY'], cc['lam'], cc['yt'], cc['yb'], cc['ytau']
    ch = 1.5 * g2_**2 + 2 * l_
    sc = 0.75 * (g2_**2 + gy_**2) + 4 * l_
    top = 6 * t_**2
    ferm = top + 6 * b_**2 + 2 * ta_**2
    return ch, sc, top, ferm


P("\nPart 3. Gauge-invariant fractions (3-loop MS-bar couplings; MS-bar beta functions of g, g', y, lam are")
P("        gauge independent, Caswell-Wilczek PLB 49, 291 (1974), so R(mu) is gauge independent)")
P(f"  {'scale':10s} {'C_W(ch)':>8s} {'C_Z+h':>8s} {'C_top':>8s} {'C_ferm':>8s} {'R_top':>7s} {'R_ferm':>7s}")
for name, mu in (("M_t", smi.MT), ("1e10", 1e10), ("1e16", 1e16), ("M_Pl", smi.M_PLANCK)):
    ch, sc, top, ferm = fr(f(mu))
    P(f"  {name:10s} {ch:8.4f} {sc:8.4f} {-top:8.4f} {-ferm:8.4f} {(ch+sc)/top:7.4f} {(ch+sc)/ferm:7.4f}")

P("\n  Diagram-level split is gauge dependent, e.g. at M_t, charged sector, ordinary R_xi:")
cc = f(smi.MT)
for xv in (0, 1, 3):
    vs = (3 + xv) * cc['g2']**2 / 2
    bub = -xv * cc['g2']**2 / 2
    gs = 2 * cc['lam']
    P(f"    xi = {xv}:  W seagull {vs:+.4f}  W-G bubble {bub:+.4f}  G seagull {gs:+.4f}  ghosts +0.0000"
      f"  sum {vs+bub+gs:+.4f}")
P("  So a statement like 'W pairs alone cancel X%' is gauge dependent; 'W sector (W+G+ghost)' is not.")

with open(os.path.join(HERE, 'c4_rxi_split_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
