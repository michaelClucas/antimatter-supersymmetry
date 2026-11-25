"""Veltman coefficient: normalization, self-conjugacy check, EW-scale value, RG running (tools/rg_sm.py).

Convention (CONSTRAINTS G): V = -mu^2|H|^2 + lambda|H|^4, H = (0, (v+h)/sqrt2), phi = |H| sqrt2,
m_h^2 = 2 mu^2 = 2 lambda v^2 at tree level (Buttazzo et al. write m^2 = 2 mu^2).
4D Euclidean cutoff Lambda on the loop momentum, Landau gauge. The Lambda^2 term of the one-loop
effective potential is (Lambda^2/32pi^2) STr M^2(phi) = (C Lambda^2/32pi^2) phi^2 + const, so
    |H|^2 coefficient:  -mu^2 -> -mu^2 + C Lambda^2/(16 pi^2)     i.e. |delta mu^2| = |C| Lambda^2/(16 pi^2)
    physical mass (fixed bare mu^2, lambda, tadpole included):  |delta m_h^2| = |C| Lambda^2/(8 pi^2)
    C = 6 lambda + (9/4) g2^2 + (3/4) gY^2 - 6 yt^2 [- 6 yb^2 - 2 ytau^2 ...]
      = (3/v^2) (m_h^2 + 2 M_W^2 + M_Z^2 - 4 m_t^2)  [+ light fermions].
So delta m_h^2 = (3 Lambda^2/(8 pi^2 v^2)) x bracket in magnitude, the standard form. The overall sign of
"delta" depends on whether one quotes the correction or the counterterm; the zero of C does not.
"""
import math
import os
import sys

import numpy as np
import sympy as sp
from scipy.optimize import brentq

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools')))
from rg_sm import run, smi, couplings_at_mt  # noqa: E402

out = []
P = lambda s: (print(s), out.append(str(s)))

# --- 1. derive C from the supertrace
phi, lam, g, gp, yt, mu2, Lam = sp.symbols('phi lambda g gprime y_t mu2 Lambda', positive=True)
masses = [  # (dof, sign, M^2(phi)) ; Landau gauge, V = -mu2/2 phi^2 + lambda/4 phi^4
    (6, +1, g**2 * phi**2 / 4),                  # W+-: 2 x 3 polarizations
    (3, +1, (g**2 + gp**2) * phi**2 / 4),        # Z
    (1, +1, -mu2 + 3 * lam * phi**2),            # h
    (3, +1, -mu2 + lam * phi**2),                # Goldstones
    (12, -1, yt**2 * phi**2 / 2),                # top: 4 Dirac components x 3 colours
]
STr = sum(n * s * M2 for n, s, M2 in masses)
V2 = Lam**2 / (32 * sp.pi**2) * STr
C = sp.simplify(sp.diff(V2, phi, 2) * 16 * sp.pi**2 / Lam**2)
P(f"C from d^2/dphi^2 of (Lambda^2/32pi^2) STr M^2, times 16pi^2/Lambda^2:  C = {sp.expand(C)}")
v, mh, MW, MZ, mt = sp.symbols('v m_h M_W M_Z m_t', positive=True)
Cm = sp.expand(C.subs({lam: mh**2 / (2 * v**2), g: 2 * MW / v, gp: 2 * sp.sqrt(MZ**2 - MW**2) / v,
                       yt: sp.sqrt(2) * mt / v}))
P(f"  in masses: C = {sp.factor(Cm)}")
P("  -> shift of the |H|^2 coefficient: delta mu^2 = C Lambda^2/(16 pi^2)  (= 1PI h self-energy at fixed v)")

# physical m_h^2 with the tadpole / v-shift: fixed bare mu^2 and lambda
m2b, l2 = sp.symbols('mu2_bare lambda_', positive=True)
Ceff = sp.symbols('C_eff', real=True)
Veff = -m2b / 2 * phi**2 + l2 / 4 * phi**4 + Ceff * Lam**2 / (32 * sp.pi**2) * phi**2
vsol = sp.solve(sp.diff(Veff, phi), phi)
vsol = [x for x in vsol if x != 0][0]
mh2_phys = sp.simplify(sp.diff(Veff, phi, 2).subs(phi, vsol))
P(f"  physical m_h^2 at the shifted minimum (bare mu^2, lambda fixed) = {mh2_phys}")
P(f"  -> delta m_h^2 = {sp.simplify(mh2_phys - 2*m2b)}  = 2 x delta mu^2 in magnitude; i.e.")
P("     |delta m_h^2| = (3 Lambda^2/(8 pi^2 v^2)) |m_h^2 + 2 M_W^2 + M_Z^2 - 4 m_t^2|, the standard form.")

# --- 1b. self-conjugate vs charged particle-antiparticle pairs (Referee 1, finding 3)
P("\nPer-species contributions to C (C_i = n_i (-1)^F a_i with M_i^2 = a_i phi^2 + const):")
species = [  # name, self-conjugate?, dof n, sign, a
    ("W+  (antiparticle: W-)", False, 3, +1, g**2 / 4), ("W-  (antiparticle: W+)", False, 3, +1, g**2 / 4),
    ("G+  (antiparticle: G-)", False, 1, +1, lam), ("G-  (antiparticle: G+)", False, 1, +1, lam),
    ("Z   (self-conjugate)", True, 3, +1, (g**2 + gp**2) / 4), ("h   (self-conjugate)", True, 1, +1, 3 * lam),
    ("G0  (self-conjugate)", True, 1, +1, lam), ("photon (self-conj., massless)", True, 2, +1, 0),
    ("t   (antiparticle: tbar)", False, 6, -1, yt**2 / 2), ("tbar (antiparticle: t)", False, 6, -1, yt**2 / 2),
]
Csum = 0
_c = couplings_at_mt()
num = {lam: _c['lam'], g: _c['g2'], gp: _c['g1'] * math.sqrt(3 / 5), yt: _c['yt']}  # MS-bar at mu = M_t
for name, sc, n, sg, a in species:
    Ci = n * sg * a
    Csum += Ci
    P(f"  {name:32s} C_i = {str(Ci):14s} = {float(Ci.subs(num)) if Ci != 0 else 0.0:+.4f} at M_t")
assert sp.simplify(Csum - C) == 0
P("  sum reproduces C. Signs: every boson +, every fermion -, whether or not the field is self-conjugate.")
P("  Self-conjugate bosons (Z, h, G0) alone: "
  f"{float(sum(n*sg*a for _, sc, n, sg, a in species if sc).subs(num)):+.4f};"
  f" charged boson pairs (W+W-, G+G-) alone: {float(sum(n*sg*a for _, sc, n, sg, a in species if not sc and sg > 0).subs(num)):+.4f}")

# basis independence: a degenerate charged pair = two real (self-conjugate) fields; STr is a trace
M2s, i_ = sp.symbols('M2', positive=True), sp.I
U = sp.Matrix([[1, i_], [1, -i_]]) / sp.sqrt(2)      # (W1, W2) -> (W+, W-) for each polarization
Mreal = sp.diag(M2s, M2s)                             # M_W^2 (W1^2 + W2^2)/2 in the real basis
Mcharge = sp.simplify(U * Mreal * U.H)
P(f"  W mass matrix, real basis (W1,W2): trace {Mreal.trace()}; charge basis (W+,W-): {Mcharge.tolist()}, trace {sp.simplify(Mcharge.trace())}")
P("  -> the Lambda^2 coefficient is Tr over the mass-squared matrix, invariant under the unitary map")
P("     between 'particle/antiparticle' (charge) eigenstates and real self-conjugate components.")
P("     A Dirac top (4 real-component dof per colour) = two degenerate Majorana components, same trace.")
P("     So 'which states are antiparticles' is a basis label that C cannot depend on; the sign is (-1)^F.")

# --- 2. EW-scale numbers with pole masses
V = smi.V
br = smi.MH**2 + 2 * smi.MW**2 + smi.MZ**2 - 4 * smi.MT**2
P(f"\nPole masses (PDG 2024): m_h={smi.MH}, M_W={smi.MW}, M_Z={smi.MZ}, m_t={smi.MT}, v={V:.2f}")
P(f"  bracket m_h^2+2M_W^2+M_Z^2-4m_t^2 = {br:.0f} GeV^2;  C = {3*br/V**2:.3f}")
P(f"  m_t needed for C=0 at these masses: {math.sqrt((smi.MH**2+2*smi.MW**2+smi.MZ**2)/4):.1f} GeV")
P(f"  m_h needed for C=0 at m_t={smi.MT}: {math.sqrt(4*smi.MT**2-2*smi.MW**2-smi.MZ**2):.1f} GeV")


def Cof(c):
    gY2 = c['gY']**2
    return 6 * c['lam'] + 9 / 4 * c['g2']**2 + 3 / 4 * gY2 - 6 * c['yt']**2 - 6 * c['yb']**2 - 2 * c['ytau']**2


def scan(nloops, **kw):
    f = run(nloops=nloops, mu_max=1e31, **kw)
    lmu = np.linspace(math.log10(kw.get('Mt', smi.MT)), 31, 1500)
    Cs = np.array([Cof(f(10**x)) for x in lmu])
    idx = np.where(np.sign(Cs[:-1]) != np.sign(Cs[1:]))[0]
    zero = None
    if len(idx):
        i = idx[0]
        zero = brentq(lambda x: Cof(f(10**x)), lmu[i], lmu[i + 1])
    return f, lmu, Cs, zero


P("\nRunning MS-bar couplings (rg_sm.py; Buttazzo et al. 1307.3536 matching + RGEs):")
f3, lmu, Cs, z3 = scan(3)
c0 = f3(smi.MT)
P(f"  at mu=M_t: lam={c0['lam']:.5f} yt={c0['yt']:.5f} g2={c0['g2']:.5f} gY={c0['gY']:.5f} g3={c0['g3']:.4f}")
P(f"  C(M_t) MS-bar = {Cof(c0):.3f}")
P("  C(mu) at selected scales (3-loop):")
for x in (math.log10(smi.MT), 4, 6, 8, 10, 12, 14, 16, 18, 19.087, 20, 22, 25, 30):
    c = f3(10**x)
    P(f"    log10 mu={x:6.2f}: C={Cof(c):+.4f}   [6lam={6*c['lam']:+.4f}, gauge={9/4*c['g2']**2+3/4*c['gY']**2:.4f},"
      f" -6yt^2={-6*c['yt']**2:+.4f}]")
P("\nZero crossing of C(mu):")
for n in (1, 2, 3):
    _, _, _, z = scan(n)
    P(f"  {n}-loop RGEs, central inputs: log10(mu0/GeV) = {z:.3f}" if z else f"  {n}-loop: no zero below 1e31")
P("  (M_Pl = 1.22e19 -> log10 = 19.09; reduced Planck 2.4e18 -> 18.39)")
P("\nParametric dependence (3-loop):")
for dMt in (-3 * 0.29, -0.29, 0.29, 3 * 0.29, -1.0, -2.0):
    _, _, _, z = scan(3, Mt=smi.MT + dMt)
    P(f"  M_t = {smi.MT+dMt:7.2f}: log10 mu0 = {z:.3f}" if z else f"  M_t={smi.MT+dMt:.2f}: none")
for das in (-0.0009, 0.0009):
    _, _, _, z = scan(3, als=smi.ALPHA_S_MZ + das)
    P(f"  alpha_s = {smi.ALPHA_S_MZ+das:.4f}: log10 mu0 = {z:.3f}")
for dmh in (-0.11 * 3, 0.11 * 3):
    _, _, _, z = scan(3, Mh=smi.MH + dmh)
    P(f"  M_h = {smi.MH+dmh:.2f}: log10 mu0 = {z:.3f}")
P("  Buttazzo et al. inputs (Mt=173.34, Mh=125.15, as=0.1184):")
_, _, _, z = scan(3, Mh=125.15, Mt=173.34, als=0.1184, MW=80.384)
P(f"    log10 mu0 = {z:.3f}")

# Sensitivity to the top Yukawa matching: what y_t(M_t) puts the zero at Jegerlehner's 7e16 GeV,
# and what y_t(M_Pl) does that correspond to (he quotes y_t(M_Pl) ~ 0.355, vs 0.3825 in Buttazzo et al.)
def zero_with_yt(dyt):
    c = couplings_at_mt()
    c['yt'] += dyt
    f = run(nloops=3, mu_max=1e31, inputs=c)
    lm = np.linspace(math.log10(smi.MT), 31, 800)
    Cv = np.array([Cof(f(10**x)) for x in lm])
    i = np.where(np.sign(Cv[:-1]) != np.sign(Cv[1:]))[0][0]
    return brentq(lambda x: Cof(f(10**x)), lm[i], lm[i + 1]), f(1.2209e19)['yt']


dyt = brentq(lambda d: zero_with_yt(d)[0] - math.log10(7e16), -0.1, 0.0)
z, ytpl = zero_with_yt(dyt)
P("")
P(f"To move the zero to 7e16 GeV (Jegerlehner 1305.6652) need y_t(M_t) shifted by {dyt:+.4f}"
  f" (to {couplings_at_mt()['yt']+dyt:.4f}); then y_t(M_Pl) = {ytpl:.4f}")
P(f"  equivalent pole-mass shift via eq.(57) slope 0.00556/GeV: {dyt/0.00556:+.1f} GeV")
dyt = brentq(lambda d: zero_with_yt(d)[0] - 19.087, -0.1, 0.0)
P(f"To put the zero at M_Pl need delta y_t(M_t) = {dyt:+.4f}  (~ {dyt/0.00556:+.1f} GeV in M_t)")
P("  (a shift in GeV; no significance quoted: the MC-vs-pole top-mass ambiguity (~0.5 GeV) and the")
P("   y_t matching theory error are not included, and mu0 itself is scheme dependent)")

# minimum of |C| region and lambda zero for context
f = f3
lz = brentq(lambda x: f(10**x)['lam'], 8, 12)
P(f"\nContext: lambda(mu)=0 at log10 mu = {lz:.2f} (3-loop)")

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(6, 3.6))
    for n, ls in ((1, ':'), (2, '--'), (3, '-')):
        _, lm, Cn, _ = scan(n)
        ax.plot(lm, Cn, ls, label=f'{n}-loop RGE')
    ax.axhline(0, color='k', lw=0.5)
    ax.axvline(19.09, color='grey', lw=0.5)
    ax.set_xlim(2, 30)
    ax.set_ylim(-5, 1)
    ax.set_xlabel('log10(mu / GeV)')
    ax.set_ylabel('Veltman coefficient C(mu)')
    ax.legend()
    fig.tight_layout()
    fig.savefig(__file__.replace('.py', '.png'), dpi=120)
except ImportError:
    pass

with open(__file__.replace('.py', '_out.txt'), 'w') as fh:
    fh.write("\n".join(out) + "\n")
