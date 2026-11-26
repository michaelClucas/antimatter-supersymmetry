"""L01b task 2: can any SM-only (discrete or antimatter-related) symmetry acting on the self-conjugate h
forbid the h^2 / |H|^2 term or enforce the Veltman relation C = 0?

Checks:
 (1) Bilinear-invariant test. For each candidate transformation, act on the field monomials of the SM
     Higgs/top sector (symmetric phase, H doublet) and report which operators are allowed/forbidden, and how
     the couplings (lambda, y_t, g, g', and the mass parameter mu^2) must transform for invariance (spurion map).
     Fermion bilinears are tracked by their chiral charges, which is all that matters for invariance.
 (2) Spin-0 vs spin-1/2 mass bilinears (cycle 5 rewrite after Referee 1 finding 2). A scalar mass term is
     phi* phi (complex) or phi^2 (real); both are invariant under any unitary/orthogonal linear symmetry, so
     self-conjugacy is irrelevant. A Weyl mass psi psi has no conjugate and carries charge 2a. This is
     observation (c) alone.
 (3) RG test. A relation imposed by a symmetry of the full theory, in a mass-independent scheme, is RG
     invariant. Compute beta_C on the surface C = 0 (1 loop, analytic; 3 loop, numerical with tools/rg_sm.py).
"""
import math
import os
import sys
import itertools

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools')))
from rg_sm import run  # noqa: E402

out = []


def P(s=""):
    print(s)
    out.append(str(s))


# ---------------------------------------------------------------- (1) operator / spurion scan
# Represent each candidate symmetry by its action on: H (as a phase / sign / conjugation), and chiral fermions
# Q_L, t_R (phases). Bilinears: Hdag H, (Hdag H)^2, Yukawa  Qbar_L Htilde t_R (+ h.c.), Dirac mass Qbar_L t_R (not
# gauge invariant in the SM; included for the 'm psibar psi' comparison with the electron/Weisskopf case).
# A transformation is a dict of multiplicative phases. 'conj' flags transformations mapping H -> H* type (C, CP):
# for those, a term T maps to T^dagger, so a real coupling is invariant and an imaginary part flips sign.
a = sp.symbols('alpha', real=True)
CANDIDATES = {
    # name: (phase_H, phase_QL, phase_tR, conj, description)
    "C (charge conjugation)": (1, 1, 1, True, "H -> H*, psi -> C psibar^T. Not a symmetry of the chiral gauge sector; acts on the Higgs/Yukawa sector as hermitian conjugation"),
    "CP": (1, 1, 1, True, "H(t,x) -> H*(t,-x); fermion bilinears -> their hermitian conjugates. Exact up to the CKM phase"),
    "P (parity, L<->R exchange)": (1, 1, 1, True, "maps Qbar_L t_R <-> tbar_R Q_L, i.e. each Yukawa term to its h.c. (observation (b)); not a symmetry of the SM gauge sector (L doublet, R singlet)"),
    "Z2: h -> -h  (H -> -H) alone": (-1, 1, 1, False, "sign flip of the self-conjugate field only"),
    "Z2: H -> -H, t_R -> -t_R  ('h -> -h with L<->R sign')": (-1, 1, -1, False, "discrete chiral transformation; extended to all fields it equals the SU(2) centre element (-1 on doublets) times a (3B+L)-rotation by pi, i.e. an exact SM symmetry"),
    "U(1) phase on H: H -> e^{i a} H": (sp.exp(sp.I * a), 1, 1, False, "hypercharge-like phase on H only"),
    "Chiral U(1)_A on top: Q_L -> e^{i a}Q_L, t_R -> e^{-i a}t_R": (1, sp.exp(sp.I * a), sp.exp(-sp.I * a), False, "protects a Dirac top mass"),
    "Chiral U(1)_A + H -> e^{-2 i a} H (PQ-like, combined)": (sp.exp(-2 * sp.I * a), sp.exp(sp.I * a), sp.exp(-sp.I * a), False, "the Yukawa's own chiral symmetry"),
}
# monomials: (name, coupling, exponents of (H, Hdag, Qbar_L=QL*, Q_L, tR*, tR))
OPS = [
    ("mu^2 Hdag H", "mu^2", dict(H=1, Hd=1)),
    ("lambda (Hdag H)^2", "lambda", dict(H=2, Hd=2)),
    ("y_t Qbar_L Htilde t_R (Htilde ~ H*)", "y_t", dict(Hd=1, QLb=1, tR=1)),
    ("gauge kinetic |D H|^2 (g, g')", "g, g'", dict(H=1, Hd=1)),
    ("Dirac mass m Qbar_L t_R (comparison; not gauge inv.)", "m", dict(QLb=1, tR=1)),
    ("odd power of H (comparison; not gauge inv.)", "-", dict(H=1)),
]


def phase_of(op, cand):
    pH, pQ, pt, conj, _ = cand
    ex = op[2]
    ph = (pH ** ex.get('H', 0)) * (sp.conjugate(pH) ** ex.get('Hd', 0)) * (sp.conjugate(pQ) ** ex.get('QLb', 0)) \
        * (pQ ** ex.get('QL', 0)) * (pt ** ex.get('tR', 0)) * (sp.conjugate(pt) ** ex.get('tRb', 0))
    return sp.simplify(ph)


P("=" * 100)
P("(1) Candidate symmetries acting on the Higgs/top sector: allowed operators and coupling (spurion) map")
P("=" * 100)
for cname, cand in CANDIDATES.items():
    P(f"\n  {cname}:  {cand[4]}")
    for op in OPS:
        ph = phase_of(op, cand)
        if cand[3]:
            if 'not gauge inv' in op[0]:
                continue  # conjugating maps on non-gauge-invariant comparison operators are meaningless
            status = "term -> its h.c. (by definition of the map, not computed): needs real coupling"
        elif ph == 1:
            status = "ALLOWED, coupling invariant"
        elif ph == -1:
            status = "forbidden unless coupling -> -coupling (spurion sign flip)"
        else:
            status = f"forbidden for generic alpha (picks up {ph}); coupling -> coupling x {sp.simplify(1/ph)}"
        P(f"     {op[0]:52s} [{op[1]:7s}]: {status}")
P("\n  Result: mu^2 |H|^2 is ALLOWED with mu^2 invariant under every candidate. No candidate flips the sign of")
P("  mu^2 or rotates it by a phase. Under the ones that act on couplings at all, lambda, g, g' are invariant and")
P("  y_t -> -y_t or y_t -> y_t e^{i a} (spurion). C = 6 lambda + 9/4 g^2 + 3/4 g'^2 - 6|y_t|^2 is invariant under")
P("  all of these maps, so none of them can force C = 0 (a symmetry can only force to zero a quantity that is ODD")
P("  under it or that carries a nonzero charge).")

# check C's invariance under all spurion maps explicitly
lam, g, gp, yt = sp.symbols('lambda g gprime y_t')
Cexpr = 6 * lam + sp.Rational(9, 4) * g**2 + sp.Rational(3, 4) * gp**2 - 6 * yt * sp.conjugate(yt)
maps = {"y_t -> -y_t": {yt: -yt}, "y_t -> e^{ia} y_t": {yt: sp.exp(sp.I * a) * yt}, "y_t -> y_t*": {yt: sp.conjugate(yt)},
        "g -> -g, g' -> -g'": {g: -g, gp: -gp}, "custodial limit g' -> 0": {gp: 0}}
P("\n  C under spurion maps:")
for k, m in maps.items():
    P(f"     {k:28s}: C -> {sp.simplify(Cexpr.subs(m, simultaneous=True))}  (changed: {sp.simplify(Cexpr.subs(m, simultaneous=True) - Cexpr) != 0})")
P("     (custodial SU(2)_L x SU(2)_R: g' and y_t - y_b are spurions that break it; |H|^2 is the O(4)-invariant")
P("      bidoublet norm, so custodial symmetry allows the mass term. Setting g' -> 0 only removes the 3/4 g'^2 piece.)")

# ---------------------------------------------------------------- (2) real-field theorem, numerical demonstration
P("\n" + "=" * 100)
P("(2) Scalar (real OR complex) vs chiral fermion mass bilinears")
P("=" * 100)
rng = np.random.default_rng(1)


def random_orthogonal_group_avg(n, gens, nsamp=4000):
    """Average R^T R over products of given real generators (finite group closure by random words)."""
    acc = np.zeros((n, n))
    for _ in range(nsamp):
        R = np.eye(n)
        for _ in range(rng.integers(1, 8)):
            R = gens[rng.integers(len(gens))] @ R
        acc += R.T @ R
    return acc / nsamp


# Example: real 4-component Higgs doublet with the SU(2)_L x U(1)_Y generators exponentiated at random angles,
# plus the h -> -h reflection, plus CP (H -> H*: flips the imaginary components).
def su2u1_real(theta):
    t1, t2, t3, ty = theta
    s = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
    from scipy.linalg import expm
    U = expm(1j * (t1 * s[0] + t2 * s[1] + t3 * s[2]) / 2) * np.exp(1j * ty / 2)
    # realify: H = x + i y (x,y in R^2) -> R^4
    return np.block([[U.real, -U.imag], [U.imag, U.real]])


gens = [su2u1_real(rng.normal(size=4)) for _ in range(6)]
gens.append(np.diag([1, -1, 1, 1]) @ np.eye(4))       # flip one real component (e.g. h -> -h in unitary gauge)
gens.append(np.diag([1, 1, -1, -1]))                    # CP: imaginary parts flip
Q = random_orthogonal_group_avg(4, gens)
P(f"  group-averaged quadratic form for the real 4-component Higgs (SU(2)xU(1), h->-h, CP):\n{np.array2string(Q, precision=4)}")
P("  -> proportional to the identity (standard: compact groups act orthogonally on real reps).")
ph = sp.symbols('phi')
P(f"  complex scalar (e.g. a stop), phi -> e^(i a) phi:  phi* phi -> {sp.simplify(sp.conjugate(sp.exp(sp.I*a))*sp.exp(sp.I*a))} x phi* phi (invariant)")
P(f"  real scalar h, h -> -h:                            h^2      -> {(-1)**2} x h^2 (invariant)")
P(f"  Weyl fermion psi -> e^(i a) psi:                   psi psi  -> {sp.exp(2*sp.I*a)} x psi psi (forbidden)")
P(f"  Dirac = two Weyl (chi, eta), axial chi,eta -> e^(i a): chi eta -> {sp.exp(2*sp.I*a)} x chi eta (forbidden)")
P("  -> The scalar mass bilinear always contains the conjugate field (or is a square of a real field), so it is")
P("     neutral under every linear internal symmetry, for real and complex scalars alike. Stops are complex and")
P("     unprotected too. Self-conjugacy (observation (a)) plays no role. The fermion mass is holomorphic in the")
P("     Weyl fields (psi psi, no psi*), so a phase rotation can forbid it, Majorana or Dirac. The obstruction is")
P("     the Lorentz structure of spin-0 vs spin-1/2 mass terms: observation (c) alone.")

# ---------------------------------------------------------------- (3) RG invariance of C = 0
P("\n" + "=" * 100)
P("(3) Is C = 0 an RG-invariant surface? (it must be, if a symmetry enforced it)")
P("=" * 100)
L, Y, G, Gp, G3 = sp.symbols('lambda y g gp g3', positive=True)
k = 16 * sp.pi**2
# 1-loop SM betas, d/dln mu, V = lambda |H|^4 normalization (m_h^2 = 2 lambda v^2)
bL = (24 * L**2 + 12 * L * Y**2 - 6 * Y**4 - 3 * L * (3 * G**2 + Gp**2)
      + sp.Rational(3, 8) * (2 * G**4 + (G**2 + Gp**2)**2)) / k
bY = Y * (sp.Rational(9, 2) * Y**2 - 8 * G3**2 - sp.Rational(9, 4) * G**2 - sp.Rational(17, 12) * Gp**2) / k
bG = -sp.Rational(19, 6) * G**3 / k
bGp = sp.Rational(41, 6) * Gp**3 / k
C = 6 * L + sp.Rational(9, 4) * G**2 + sp.Rational(3, 4) * Gp**2 - 6 * Y**2
bC = sp.expand(6 * bL + sp.Rational(9, 2) * G * bG + sp.Rational(3, 2) * Gp * bGp - 12 * Y * bY)
Lsurf = sp.solve(sp.Eq(C, 0), L)[0]
bC_surf = sp.simplify(sp.expand(bC.subs(L, Lsurf) * k))
P(f"  16pi^2 dC/dln mu on C = 0 (lambda eliminated):\n    {sp.expand(bC_surf)}")
P(f"  Not identically zero -> C = 0 is not RG invariant at one loop; no symmetry of the SM can enforce it.")
# numerical, 3 loops
from scipy.optimize import brentq
f3 = run(nloops=3, mu_max=1e30)


def Cnum(lmu):
    c = f3(10**lmu)
    return 6 * c['lam'] + 9 / 4 * c['g2']**2 + 3 / 4 * c['gY']**2 - 6 * c['yt']**2 - 6 * c['yb']**2 - 2 * c['ytau']**2


l0 = brentq(Cnum, 18, 29)
h = 1e-3
dCdl = (Cnum(l0 + h) - Cnum(l0 - h)) / (2 * h) / math.log(10)
c0 = f3(10**l0)
num1 = float(bC_surf.subs({Y: c0['yt'], G: c0['g2'], Gp: c0['gY'], G3: c0['g3']}) / k)
P(f"  3-loop running (tools/rg_sm.py, incl. y_b, y_tau in C): C = 0 at log10(mu0/GeV) = {l0:.3f}")
P(f"    dC/dln mu at mu0 (3-loop, numerical)        = {dCdl:+.5f}")
P(f"    1-loop formula above at the mu0 couplings   = {num1:+.5f}")
P(f"    couplings at mu0: lambda={c0['lam']:+.5f} y_t={c0['yt']:.5f} g={c0['g2']:.5f} g'={c0['gY']:.5f} g3={c0['g3']:.5f}")
P("  Compare SUSY: the stop quartic lambda_{h stop stop} = y_t^2 is an F-term identity, preserved by RG running")
P("  (non-renormalization theorem); the SUSY cancellation is RG-stable, the SM's C = 0 is a crossing point.")

with open(os.path.join(HERE, 'symmetry_scan_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
