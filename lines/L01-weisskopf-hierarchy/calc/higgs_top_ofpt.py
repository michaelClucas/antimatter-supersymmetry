"""Higgs self-energy from the top loop, decomposed by time ordering (old-fashioned PT / hole theory).

H_int = (y/sqrt2) h psibar psi, N_c = 3. Higgs at rest (energy m_h), sharp cutoff K on the top 3-momentum p.
Spinors normalized u^dag u = 1. Pair t(p) tbar(-p) <-> negative-energy top state of momentum +p being
promoted to t(p): sum over spins = Tr[Lam_+(p) beta Lam_-(p) beta].

Time orderings (per d^3p/(2pi)^3, contribution to delta m_h^2 = 2 m_h delta E):
  F  forward:  h -> t tbar -> h                     denominator (m_h - 2E)
  B  backward: vacuum -> h' t tbar, then t tbar h -> 0   denominator -(m_h + 2E)  (the Z-graph)
In hole language both are excitations of the filled top Dirac sea (sea top -> positive-energy top).
There is no top-free ("particle only") intermediate state and no Pauli blocking (no top is present).

Cross-check: for each p, integrate the covariant Feynman integrand over k0 numerically and compare to F+B.
"""
import sympy as sp
import numpy as np
from scipy.integrate import quad

p, m, mh, y = sp.symbols('p m m_h y', positive=True)
Nc = 3
E = sp.sqrt(p**2 + m**2)
I2, Z2 = sp.eye(2), sp.zeros(2)
sz = sp.Matrix([[1, 0], [0, -1]])
blk = lambda a, b, c, d: sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
beta = blk(I2, Z2, Z2, -I2)
alz = blk(Z2, sz, sz, Z2)
H = alz * p + beta * m
Lp = (sp.eye(4) + H / E) / 2
Lm = (sp.eye(4) - H / E) / 2
S = sp.simplify((Lp * beta * Lm * beta).trace())

out = []
P = lambda s: (print(s), out.append(str(s)))
P(f"spin sum |u^dag beta v|^2 = {S}   (vanishes as p->0: scalar couples to P-wave pair)")

M2 = Nc * (y**2 / 2) * S / (2 * mh)            # |<t tbar|H|h>|^2 * Volume
meas = p**2 / (2 * sp.pi**2)
F = sp.simplify(2 * mh * meas * M2 / (mh - 2 * E))
B = sp.simplify(2 * mh * meas * M2 / (-(mh + 2 * E)))
x = sp.symbols('x', positive=True)
for name, f in (('F (forward, h->t tbar)', F), ('B (backward / Z-graph / vacuum pair)', B), ('F+B', F + B)):
    ser = sp.series(sp.simplify(f.subs(p, 1 / x)), x, 0, 2).removeO().subs(x, 1 / p)
    P(f"  {name}: d(delta m_h^2)/dp = {f}")
    P(f"      large p: {sp.expand(sp.simplify(ser))}")
P(f"  coefficient of p (quadratic div, coefficient of K^2/2) in F: {sp.limit(F/p, p, sp.oo)}, in B: {sp.limit(B/p, p, sp.oo)}")
P(f"  -> both orderings have the SAME sign; total delta m_h^2 ~ {sp.limit((F+B)/p, p, sp.oo)/2} K^2 (3-momentum cutoff)")
P(f"  covariant 4D Euclidean cutoff gives -N_c y^2 Lambda^2/(8 pi^2) = {-Nc*y**2/(8*sp.pi**2)} Lambda^2;")
P("  the K^2 coefficient differs by a factor 2: quadratic-divergence coefficients are regulator dependent.")
P(f"  F+B at m_top = 0: {sp.simplify((F+B).subs(m, 0))}  (does NOT vanish: no symmetry forces delta m_h^2 ~ m_h^2)")

# numerical cross-check against covariant integrand at fixed |p|, numerically integrating k0
vals = {m: 1.0, mh: 0.72, y: 1.0}
Fn = sp.lambdify(p, (F + B).subs(vals))


def covariant(pp):
    """Feynman-diagram integrand at fixed spatial loop momentum pp, k0 integrated after Wick rotation.
    -i Sigma = (-1)(-i y/sqrt2)^2 N_c int d^4k/(2pi)^4 Tr[i(kslash+m) i(kslash+qslash+m)]/(D1 D2), q = (m_h, 0)
             = -(y^2/2) N_c int d^4k/(2pi)^4 num/(D1 D2),  num = 4(k.(k+q) + m^2).
    k0 = i w, dk0 = i dw  ->  Sigma = (y^2/2) N_c (1/2pi) int dw num/(D1 D2)  per d^3k/(2pi)^3; delta m_h^2 = Sigma.
    Valid (no pinched poles) since m_h < 2 m_t."""
    mt, MH = 1.0, 0.72
    Ep2 = pp**2 + mt**2

    def integrand(w):
        k0 = 1j * w
        num = 4 * (k0 * (k0 + MH) - pp**2 + mt**2)
        return num / ((k0**2 - Ep2) * ((k0 + MH)**2 - Ep2))
    re = quad(lambda w: integrand(w).real, -np.inf, np.inf, limit=400)[0]
    return 3 * 0.5 * re / (2 * np.pi) * pp**2 / (2 * np.pi**2)


P("\nCovariant (k0 integrated numerically, Wick-rotated) vs time-ordered F+B, m_t=1, m_h=0.72, y=1:")
for pp in (0.1, 0.5, 1.0, 3.0, 10.0):
    P(f"  p={pp:5.1f}: covariant {covariant(pp):+.8f}   F+B {float(Fn(pp)):+.8f}")

with open(__file__.replace('.py', '_out.txt'), 'w') as fh:
    fh.write("\n".join(out) + "\n")
