"""L01b cycle 7: the same-spin obstruction, checked step by step. Run from this directory: python c7_same_spin.py

Chain (WORK.md Section 4):
 S1  Every SM antimatter operation maps a field/state to one of the SAME Lorentz representation (same spin j)
     and the same statistics. Checked explicitly for the Dirac field: charge conjugation psi -> psi^c = i g^2 psi*
     commutes with the spinor Lorentz transformation, so psi^c is again a (1/2,0)+(0,1/2) field; P, T and CPT act
     with J -> +J, -J, -J, so J^2 is preserved. Dirac-sea / Feynman-Stueckelberg readings relabel the same Fock
     space (H3): the hole in a spin-1/2 negative-energy level is a spin-1/2 positron.
 S2  A linear field map that preserves spin and statistics maps every Lagrangian monomial into the span of
     monomials with the same multiset of field types {scalar, Weyl fermion, vector}. Invariance of L then gives
     conditions only within each type class. The Veltman combination C = 6 lam + 9/4 g^2 + 3/4 g'^2 - 6 y_t^2
     needs a relation between y_t (class S.F.F) and lam (S^4) or g (V.S.S / V.F.F, fixed by gauge universality).
     No such map can relate them. Printed: the class of every SM coupling.
 S3  The way out: an operator that changes spin by 1/2 and commutes with H. By Coleman-Mandula + HLS this is
     SUSY. Checked: [J_z, Q_alpha] = -sigma_z/2 Q_alpha type action (Q lowers/raises J_z by 1/2); F-term of
     W = y H Q U gives the stop quartic y^2 and the top mass y H, so STr M^2 cancels in the top sector.
 S4  SUSY needs SM states to fill supermultiplets (equal gauge charges, spin differing by 1/2). Scan the SM: no
     colour-triplet scalar exists for the top, no octet fermion for the gluon, etc. dof 28 bosonic vs 90 fermionic.
 S5  Without a symmetry, C = 0 could hold only by accident. It does not hold along the flow: beta_C != 0 on C = 0
     (one loop, symbolic) and dC/dlnmu != 0 at the 3-loop crossing.
 S6  Classical scale invariance (Bardeen 1995): the surface m^2 = 0 IS RG invariant in a mass-independent scheme
     (beta_{m^2} ~ m^2), but (i) dilatation preserves spin, so it is not a boson-fermion relation and does not
     touch C; (ii) it is anomalous; (iii) the SM with tree mu^2 = 0 does not break EW symmetry radiatively
     (Coleman-Weinberg B < 0 with the measured top), so the measured spectrum needs mu^2 != 0.
"""
import math
import os
import sys

import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools')))
import sm_inputs as smi  # noqa: E402
from rg_sm import run  # noqa: E402

out = []


def P(s=""):
    print(s)
    out.append(str(s))


# ------------------------------------------------------------------ S1: discrete operations preserve spin
P("S1. Antimatter operations preserve the Lorentz representation (spin) of the field")
I2 = np.eye(2)
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
Z2 = np.zeros((2, 2))
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)  # Dirac representation
gs = [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
gam = [g0] + gs
S = {}
for m in range(4):
    for n in range(m + 1, 4):
        S[(m, n)] = 0.25j * (gam[m] @ gam[n] - gam[n] @ gam[m])
Cop = 1j * gam[2]                    # psi^c = i gamma^2 psi*
T_op = 1j * gam[1] @ gam[3]          # psi_T(t,x) = i gamma^1 gamma^3 psi*(-t,x)  (Bjorken-Drell)
P0 = g0                              # psi_P(t,x) = gamma^0 psi(t,-x)
rng = np.random.default_rng(1)
maxdev = 0.0
for trial in range(5):
    w = rng.normal(size=6)
    gen = sum(wi * S[k] for wi, k in zip(w, S))
    L = expm(-0.5j * gen)             # spinor Lorentz transformation, real omega
    # C: psi -> Cop psi*; transformed field Cop (L psi)* = (Cop L* Cop^-1) Cop psi*; same rep iff Cop L* Cop^-1 = L
    maxdev = max(maxdev, np.abs(Cop @ L.conj() @ np.linalg.inv(Cop) - L).max())
P(f"  C: max |C L* C^-1 - L| over 5 random Lorentz transformations = {maxdev:.1e}  -> psi^c is a spin-1/2 Dirac field")
# rotation generators J_i = S_jk ; check P J P^-1 = +J ; T J* T^-1 = -J (antiunitary: K J K = J*)
J = [S[(2, 3)], S[(1, 3)] * -1, S[(1, 2)]]
devP = max(np.abs(P0 @ Ji @ np.linalg.inv(P0) - Ji).max() for Ji in J)
devT = max(np.abs(T_op @ Ji.conj() @ np.linalg.inv(T_op) + Ji).max() for Ji in J)
CPT = Cop @ P0 @ T_op
J2 = sum(Ji @ Ji for Ji in J)
P(f"  P: max |P J P^-1 - J| = {devP:.1e};  T: max |T J* T^-1 + J| = {devT:.1e}  (J -> -J, antiunitary)")
P(f"  J^2 on the Dirac spinor = {np.round(np.diag(J2).real, 6)} = j(j+1) with j = 1/2; every map above commutes with J^2")
devC2 = np.abs(Cop @ J2.conj() @ np.linalg.inv(Cop) - J2).max()
P(f"  C J^2* C^-1 - J^2 = {devC2:.1e}. Bosons: phi -> phi* (scalar to scalar), W+_mu <-> -W-_mu (vector to vector).")
P("  Statistics: none of these maps changes (-1)^F, which is (-1)^{2j} by spin-statistics.")
P("  => every SM antimatter operation (C, CP, CPT; sea / Feynman-Stueckelberg relabelings) maps spin j to spin j.")

# ------------------------------------------------------------------ S2: type classes of SM couplings
P("\nS2. Field-type class of each coupling entering C (S = scalar, F = Weyl fermion, V = vector)")
classes = [
    ("y_t   (Q t^c H)", "S F F"),
    ("y_b, y_tau, other Yukawas", "S F F"),
    ("lam   (|H|^4)", "S S S S"),
    ("g, g' in |D H|^2", "V S S, V V S S"),
    ("g, g' in psi-bar D psi", "V F F"),
    ("g, g' in F_mu nu^2", "V V V, V V V V"),
]
for c, t in classes:
    P(f"  {c:28s} class {t}")
P("  A spin- and statistics-preserving linear map sends S->S, F->F, V->V, so it maps each class into itself.")
P("  Gauge universality ties g in V S S to g in V F F (same gauge field, same group).")
P("  Nothing ties y_t (class S F F, with S a scalar not a gauge field) to lam (S^4) or to g: the only symmetry that")
P("  could is one mapping S <-> F or S <-> V. S <-> V is gauge-Higgs unification (H = A_5, extra dimensions: BSM).")
P("  S <-> F is supersymmetry (S3). Shift symmetry h -> h + c is non-linear and mixes classes of different degree,")
P("  but requires h to be a Goldstone of a larger broken group: new fields (LW2 Sec. 3).")
P("  [argument, narrowed c9 (Referee C): holds for GLOBAL, HOMOGENEOUS, LINEAR maps only. Gauge invariance,")
P("   nonlinear/pNGB realizations, scale invariance + Gildener-Weinberg and a twin Z2 on an enlarged field space")
P("   evade it; each is shown unavailable with SM content in c9_symmetry_group.py and c9_twin_antimatter.py.]")

# ------------------------------------------------------------------ S3: SUSY changes spin and ties couplings
P("\nS3. SUSY: the generator changes J_z by 1/2, and the F-term ties the stop quartic to y_t^2")
# Q_alpha transforms as a left-handed Weyl spinor: [J_i, Q_alpha] = -(sigma_i/2)_{alpha beta} Q_beta
Jz = sz / 2
for a in (0, 1):
    P(f"  [J_z, Q_{a+1}] = {-Jz[a, a].real:+.1f} Q_{a+1}: Q_{a+1} acting on a state of J_z = m gives J_z = m {-Jz[a, a].real:+.1f}")
y, h, Qs, Us = sp.symbols('y h Q U')
Wsp = y * h * Qs * Us
FQ, FU = sp.diff(Wsp, Qs), sp.diff(Wsp, Us)
VF = sp.expand(FQ * sp.conjugate(FQ) + FU * sp.conjugate(FU))
P(f"  W = y H Q U ; V_F = |dW/dQ|^2 + |dW/dU|^2 = {VF}")
P("  -> stop quartic |H|^2(|Q|^2+|U|^2) with coefficient |y|^2: lambda_{H stop stop} = y_t^2, and m_top = y <H>.")
phi = sp.symbols('phi', positive=True)
Nc = 3
stops = 2 * Nc * 2 * (y**2 * phi**2 / 2)        # 2 complex stops x colour x 2 real dof, mass^2 y^2 phi^2/2
top = -4 * Nc * (y**2 * phi**2 / 2)             # Dirac top: 4 dof x colour
P(f"  top sector (1/2) d^2/dphi^2 STr M^2 = {sp.simplify(sp.diff(stops + top, phi, 2) / 2)}  (stops +{sp.diff(stops, phi, 2)/2}, top {sp.diff(top, phi, 2)/2})")
P("  The relation lambda_{H stop stop} = y_t^2 holds because Q maps the top (j=1/2) into the stop (j=0). No map in S1 can.")

# ------------------------------------------------------------------ S4: SM cannot fill supermultiplets
P("\nS4. Can SM states be grouped into supermultiplets? (same SU3 x SU2 x U1_Y, spin differs by 1/2)")
# (SU3 dim, SU2 dim, Y); fermions as left-handed Weyl, with conjugates allowed
R_ = sp.Rational
ferm = {'Q': (3, 2, R_(1, 6)), 'u^c': (-3, 1, R_(-2, 3)), 'd^c': (-3, 1, R_(1, 3)), 'L': (1, 2, R_(-1, 2)), 'e^c': (1, 1, 1)}
bos = {'H': (1, 2, R_(1, 2)), 'G (gluon)': (8, 1, 0), 'W': (1, 3, 0), 'B': (1, 1, 0)}


def conj(r):
    return (-r[0] if abs(r[0]) == 3 else r[0], r[1], -r[2])


for fn, fr in ferm.items():
    hits = [bn for bn, br in bos.items() if br == fr or br == conj(fr)]
    P(f"  fermion {fn:4s} {str(fr):18s} scalar/vector partner in SM: {hits if hits else 'none'}")
for bn, br in bos.items():
    hits = [fn for fn, fr in ferm.items() if br == fr or br == conj(fr)]
    P(f"  boson   {bn:9s} {str(br):13s} fermion partner in SM: {hits if hits else 'none'}")
P("  Only H ~ L* matches in quantum numbers (the old 'Higgs as sneutrino' idea); it does not help the top loop,")
P("  which needs a colour-triplet scalar. No SM state has the quantum numbers of t~_L or t~_R.")
P("  dof: 28 bosonic vs 90 fermionic (CONSTRAINTS G): STr 1 != 0, so no SUSY representation exists on SM content.")
P("  Supersymmetrizing the SM therefore requires new fields, excluded by A1 and by C3.")

# ------------------------------------------------------------------ S5: no accidental relation along the flow
P("\nS5. Could C = 0 hold accidentally at all scales? (one-loop beta of C on C = 0; 3-loop numerics)")
g, gp, lam, yt, g3 = sp.symbols('g gp lam y g3', positive=True)
bg = -sp.Rational(19, 6) * g**3
bgp = sp.Rational(41, 6) * gp**3
by = yt * (sp.Rational(9, 2) * yt**2 - 8 * g3**2 - sp.Rational(9, 4) * g**2 - sp.Rational(17, 12) * gp**2)
blam = 24 * lam**2 - 6 * yt**4 + sp.Rational(3, 8) * (2 * g**4 + (g**2 + gp**2)**2) + lam * (12 * yt**2 - 9 * g**2 - 3 * gp**2)
C = 6 * lam + sp.Rational(9, 4) * g**2 + sp.Rational(3, 4) * gp**2 - 6 * yt**2
bC = 6 * blam + sp.diff(C, g) * bg + sp.diff(C, gp) * bgp + sp.diff(C, yt) * by
bC0 = sp.expand(bC.subs(lam, sp.solve(C, lam)[0]))
P(f"  16 pi^2 beta_C |_(C=0) = {bC0}  (not identically zero)")


def Cnum(f):
    return 6 * f['lam'] + 2.25 * f['g2']**2 + 0.75 * f['gY']**2 - 6 * f['yt']**2 - 6 * f['yb']**2 - 2 * f['ytau']**2


s = run(nloops=3, mu_max=1e24)
l0 = brentq(lambda l: Cnum(s(10**l)), 15, 23.9)
dC = (Cnum(s(10**(l0 + 0.01))) - Cnum(s(10**(l0 - 0.01)))) / (0.02 * math.log(10))
P(f"  3-loop: C = 0 at mu0 = 10^{l0:.2f} GeV, dC/dln mu there = {dC:+.4f} (a transverse crossing, not an invariant surface)")
f = s(10**l0)
num = bC0.subs({g: f['g2'], gp: f['gY'], yt: f['yt'], g3: f['g3']})
P(f"  one-loop beta_C/(16pi^2) evaluated with mu0 couplings = {float(num)/(16*math.pi**2):+.4f}")

# ------------------------------------------------------------------ S6: classical scale invariance
P("\nS6. Classical scale invariance (Bardeen, FERMILAB-CONF-95-391-T)")
P("  In MS-bar, beta_{mu^2} = mu^2 x (function of dimensionless couplings): mu^2 = 0 is RG invariant. [established]")
P("  This is the SM's only internal handle on mu^2. It is not a boson-fermion relation: dilatations commute with")
P("  J^2, so it constrains the dimensionful mu^2, not C. It is broken by the trace anomaly (dimensional transmutation).")
v = smi.V
B = (6 * smi.MW**4 + 3 * smi.MZ**4 - 12 * smi.MT**4) / (64 * math.pi**2 * v**4)
P(f"  Test of the scale-invariant SM (tree mu^2 = 0, CW potential, no Higgs-loop term): B = (6M_W^4+3M_Z^4-12m_t^4)/(64pi^2 v^4) = {B:.2e}")
P("  B < 0: the stationary point at phi != 0 is a maximum, so no radiative EWSB (reproduces L01 cw_radiative_ewsb, B = -4.3e-3 with m_h included).")
P("  The measured spectrum (m_h = 125.2, m_t = 172.57) requires a tree mu^2 = m_h^2/2 = "
  f"({smi.MH/math.sqrt(2):.1f} GeV)^2 != 0, so classical scale invariance is explicitly broken in the SM itself.")

with open(os.path.join(HERE, 'c7_same_spin_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
