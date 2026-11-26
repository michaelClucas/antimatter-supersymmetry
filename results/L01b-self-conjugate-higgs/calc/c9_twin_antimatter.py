"""L01b cycle 9: can SM antimatter play the twin in a twin-Higgs-type (same-spin) protection?
(Referee E c8 findings 1-3, Referee C c7 finding 2.)

Twin Higgs (Chacko, Goh, Harnik, hep-ph/0506256): a Z2 maps the SM to an independent mirror copy (H_A -> H_B,
t_A -> t_B). With y_A = y_B the top-loop Lambda^2 term is k(|H_A|^2 + |H_B|^2), invariant under U(4) acting on
the 8 real fields; the light Higgs is a pseudo-Goldstone of U(4) -> U(3) and the Lambda^2 term does not enter its mass.
Here: (A) H^c = i sigma2 H* is not an independent field; (B) the counterfactual twin computation, independent H_B vs
H_B := H^c; (C) the H <-> H^c swap is the SU(2)_R element i sigma2; (D) the antitop is already in the top loop;
(E) custodial limit with y_b, and the h self-loop share.
Run from this directory: python c9_twin_antimatter.py
"""
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools')))
from rg_sm import couplings_at_mt  # noqa: E402

out = []


def P(s=""):
    print(s)
    out.append(str(s))


I = sp.I
p = sp.symbols('p1:5', real=True)
q = sp.symbols('q1:5', real=True)
eps = sp.Matrix([[0, 1], [-1, 0]])  # i sigma_2
H = sp.Matrix([(p[0] + I * p[1]), (p[2] + I * p[3])]) / sp.sqrt(2)
Hc = eps * H.conjugate()
n2 = lambda X: sp.expand(sp.simplify((X.H * X)[0]))  # noqa: E731

P("=" * 96)
P("(A) H^c = i sigma2 H* is a function of H, not an independent field")
P("=" * 96)
P(f"  |H|^2   = {n2(H)}")
P(f"  |H^c|^2 - |H|^2 = {sp.simplify(n2(Hc) - n2(H))}")
P(f"  |H|^2 + |H^c|^2 = {sp.factor(n2(H) + n2(Hc))}   (= 2|H|^2)")
P(f"  H^c^dag H = {sp.simplify((Hc.H * H)[0])}   (the would-be H-H^c mixing bilinear vanishes identically)")
comps = [sp.re(x) for x in list(H) + list(Hc)] + [sp.im(x) for x in list(H) + list(Hc)]
J = sp.Matrix(comps).jacobian(p)
P(f"  real components of (H, H^c): {len(comps)}; rank of d(H,H^c)/d(p1..p4) = {J.rank()}  (4 = no new d.o.f.)")
a, b, c, d = sp.symbols('a b c d', real=True)
U = sp.Matrix([[a + I * b, c + I * d], [-c + I * d, a - I * b]])  # generic SU(2) element when a^2+b^2+c^2+d^2 = 1
diff = sp.simplify((eps * (U * H).conjugate() - U * eps * H.conjugate()).subs(d, sp.sqrt(1 - a**2 - b**2 - c**2)))
P(f"  (U H)^c - U H^c for generic U in SU(2): {list(diff)}  (H^c is a doublet built from H)")
P("  Count of independent gauge-invariant quadratic operators:")
P("    field space {H}        : |H|^2 only (H^c^dag H = 0, |H^c|^2 = |H|^2)                  -> 1")
HA = H
HB = sp.Matrix([(q[0] + I * q[1]), (q[2] + I * q[3])]) / sp.sqrt(2)
ops = [n2(HA), n2(HB), sp.expand((HA.H * HB)[0]), sp.expand((HB.H * HA)[0])]
allm = sorted({m for o in ops for m in sp.Poly(o, *p, *q).monoms()})
M = sp.Matrix([[sp.Poly(o, *p, *q).coeff_monomial(m) for m in allm] for o in ops])
P(f"    field space {{H_A, H_B}} (independent twin): |H_A|^2, |H_B|^2, H_A^dag H_B, h.c. -> rank {M.rank()}")
P("  A Z2 can relate the coefficients of two DIFFERENT invariants (|H_A|^2 <-> |H_B|^2). C, CP and CPT map")
P("  |H|^2 to itself, so on the 1-dimensional space of SM Higgs bilinears they impose no relation at all.")

P("\n" + "=" * 96)
P("(B) Counterfactual: twin Z2 with an independent H_B vs 'antimatter twin' H_B := H^c")
P("=" * 96)
k, lam, f = sp.symbols('kappa lambda f', real=True)
x = list(p) + list(q)
r2 = n2(HA) + n2(HB)
V8 = k * r2 + lam * r2**2  # k = tree + top-loop Lambda^2 piece, same for A and B by the Z2 (y_A = y_B)
grad = [sp.diff(V8, xi) for xi in x]
vac = {xi: 0 for xi in x}
vac[q[0]] = f  # vacuum along H_B; |H_B|^2 = f^2/2
kmin = sp.solve(grad[4].subs(vac), k)
kmin = [s for s in kmin if s != 0][0] if kmin else None
Hess = sp.hessian(V8, x).subs(vac).subs(k, kmin)
ev = Hess.eigenvals()
P(f"  independent twin (8 real fields): stationarity gives kappa = {kmin}")
P(f"    mass matrix eigenvalues {{value: multiplicity}} = {ev}")
P("    7 exact zeros: the U(4) -> U(3) Goldstones. The SM-like Higgs lives in these directions (after gauging,")
P("    3 are eaten by the twin W, Z and 3 by ours; one pNGB is the light h). The Lambda^2 coefficient kappa")
P("    sets only the radial mode. Explicit U(4) breaking delta(|H_A|^4 + |H_B|^4), Z2-symmetric, lifts h:")
dl = sp.symbols('delta', positive=True)
th = sp.symbols('theta', real=True)
circ = {xi: 0 for xi in x}
circ[q[0]] = f * sp.cos(th)
circ[p[0]] = f * sp.sin(th)
Vth = sp.simplify((k * r2 + lam * r2**2 + dl * (n2(HA)**2 + n2(HB)**2)).subs(circ))
P(f"    V on the vacuum circle (H_A = f sin th, H_B = f cos th): {sp.simplify(Vth)}")
d2 = sp.simplify(sp.diff(Vth, th, 2))
P(f"    d^2V/dth^2 = {d2}  (at th = pi/4: {sp.simplify(d2.subs(th, sp.pi/4))});  d/dkappa of it = {sp.simplify(sp.diff(d2, k))}")
P("    The pNGB curvature is set by delta (log-sized in twin models), and is kappa-independent at fixed f;")
P("    so the top-loop Lambda^2 term never reaches the pNGB mass. That is the twin protection [established, CGH 2005].")
P("")
h = sp.symbols('h', real=True)
V4 = (k * (n2(H) + n2(Hc)) + lam * (n2(H) + n2(Hc))**2)
V4h = sp.simplify(V4.subs({p[0]: h, p[1]: 0, p[2]: 0, p[3]: 0}))
P(f"  'antimatter twin' H_B := H^c: V = kappa(|H|^2+|H^c|^2) + lambda(...)^2 = {sp.expand(V4h)} on H = (h,0)/sqrt2")
hmin = [s for s in sp.solve(sp.diff(V4h, h), h) if s != 0][0]
mh2 = sp.simplify(sp.diff(V4h, h, 2).subs(h, hmin))
P(f"    m_h^2 = V''(h_min) = {mh2}   (proportional to kappa, i.e. to the Lambda^2 term: no protection)")
Vgen = sp.simplify(V4.subs({p[1]: 0, p[2]: 0, p[3]: 0}))
Hess4 = sp.hessian(sp.expand(V4), list(p)).subs({p[0]: hmin, p[1]: 0, p[2]: 0, p[3]: 0})
P(f"    4x4 mass matrix eigenvalues = {sp.simplify(Hess4).eigenvals()}")
P("    3 zeros are the SM Goldstones G+-, G0 (eaten). The 4th, h, is the RADIAL mode: there is no extra")
P("    angular direction to host a pNGB, because H^c adds no degrees of freedom (A). And kappa(|H|^2+|H^c|^2)")
P("    = 2 kappa|H|^2 double-counts: the top loop is computed once (see D).")

P("\n" + "=" * 96)
P("(C) The particle <-> antiparticle swap of the doublet is the custodial SU(2)_R element i sigma2")
P("=" * 96)
Phi = sp.Matrix.hstack(Hc, H)
R = eps
PhiR = Phi * R.H
P(f"  Phi = (H^c, H);  Tr Phi^dag Phi = {sp.factor(sp.simplify((Phi.H * Phi).trace()))}")
P(f"  Phi R^dag with R = i sigma2: columns -> (H, -H^c)? {sp.simplify(PhiR - sp.Matrix.hstack(H, -Hc)) == sp.zeros(2, 2)}")
P(f"  det R = {R.det()}, R R^dag = {R * R.H}  -> R in SU(2)_R: continuous, internal, spin-preserving")
P(f"  (-H^c)^c = H? {sp.simplify(eps * (-Hc).conjugate() - H) == sp.zeros(2, 1)}  (the swapped matrix is again a bidoublet)")
P(f"  Tr (Phi R^dag)^dag (Phi R^dag) - Tr Phi^dag Phi = {sp.simplify((PhiR.H * PhiR).trace() - (Phi.H * Phi).trace())}")
P("  The swap leaves kappa Tr Phi^dag Phi invariant for every kappa: it constrains nothing in C. SU(2)_R rotates")
P("  (t_R, b_R); it is not chirality L <-> R. Parity is broken maximally by the SU(2)_L gauge coupling (9/4 g^2 in C).")

P("\n" + "=" * 96)
P("(D) The antitop is already inside the top's Lambda^2 term")
P("=" * 96)
yt, Nc = sp.symbols('y_t N_c', positive=True)
m2 = yt**2 * h**2 / 2
dirac_states = 4  # t(up), t(down), tbar(up), tbar(down): trace of the identity on (1/2,0)+(0,1/2)
Cferm = sp.Rational(1, 2) * sp.diff(-dirac_states * Nc * m2, h, 2)
P(f"  one Dirac top, 4 states per colour (2 spin x particle/antiparticle): C_top = (1/2) d^2/dh^2 [-4 N_c m_t^2(h)]"
  f" = {Cferm.subs(Nc, 3)}")
P("  The antitop states are 2 of those 4. A 'twin' made of antitops would count them twice. C, CP, CPT map the")
P("  top loop into itself (same field, same |y_t|^2), so they relate y_t to y_t: an identity, nothing to cancel.")
P("  A twin needs t_B with its own y_B coupling to H_B: new fields, excluded by CONSTRAINTS A1.")

P("\n" + "=" * 96)
P("(E) Custodial limit (with y_b) and the h self-loop")
P("=" * 96)
g, gp, yb, y, l = sp.symbols("g g' y_b y lambda", positive=True)
Cs = 6 * l + sp.Rational(9, 4) * g**2 + sp.Rational(3, 4) * gp**2 - 6 * yt**2 - 6 * yb**2
P(f"  C (top, bottom)                      = {Cs}")
P(f"  custodial limit g' -> 0, y_t = y_b = y: {Cs.subs({gp: 0, yt: y, yb: y})}")
cc = couplings_at_mt()
gY = math.sqrt(0.6) * cc['g1']
num = {g: cc['g2'], gp: gY, l: cc['lam'], yt: cc['yt'], yb: cc['yb']}
P(f"  at M_t (MS-bar, PDG 2024): C = {float(Cs.subs(num)):.3f};  custodial limit with y = y_t: "
  f"{float(Cs.subs({gp: 0, yb: cc['yt']}).subs(num)):.3f}  (further from zero; no relation imposed)")
top = 6 * cc['yt']**2
P(f"  h self-loop 3 lambda = {3*cc['lam']:.4f}; top 6 y_t^2 = {top:.4f}; share = {3*cc['lam']/top:.4f}")
P(f"  all scalars (h 3lam + G0 lam + G+- 2lam) 6 lambda = {6*cc['lam']:.4f}; share = {6*cc['lam']/top:.4f}")
P(f"  per real dof: h -> 3 lambda, each Goldstone -> lambda; complex G+- = 2 real dof x lambda.")
P("  The self-conjugate h has the stop sign and the largest single scalar weight (3 lambda vs lambda), because")
P("  d^2(lambda h^4/4)/dh^2 = 3 lambda h^2 (the quartic's combinatorics), not because h is its own antiparticle.")
P(f"  Pure-scalar term: delta m_h^2 propto lambda Lambda^2 = (m_h^2 / 2v^2) Lambda^2: proportional to m_h^2 but")
P("  multiplied by Lambda^2/v^2, not by a log. No Weisskopf softening: that needed delta m propto m with an")
P("  enhanced (chiral) symmetry at m = 0; m_h^2 -> 0 enlarges only scale symmetry (S6).")

with open(os.path.join(HERE, 'c9_twin_antimatter_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
