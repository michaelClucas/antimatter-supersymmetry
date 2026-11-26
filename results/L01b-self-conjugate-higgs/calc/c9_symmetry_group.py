"""L01b cycle 9: the symmetry group of the SM Lagrangian and its action on the couplings in C
(Referee C c7 finding 1 / c8 MAJOR: replace the over-general step-2 lemma by an enumeration).
Also: Gildener-Weinberg B, the QCD-condensate scale factors (Referee D 1), and the F-b significance as a
function of the y_t matching spread (Referee D 5).

Method. For each symmetry (or approximate symmetry / spurion) of the SM Lagrangian:
  (1) check numerically, with random group elements, that each renormalizable Higgs-sector operator
      O_mu = |H|^2, O_lam = |H|^4, O_t = (Q^dag H^c) t_R, O_b = (Q^dag H) b_R is mapped to itself
      (up to a phase / hermitian conjugation absorbed by the coupling), never to a DIFFERENT operator;
  (2) record the induced action on coupling space (lam, g, g', y_t, y_b);
  (3) check that C is invariant. An invariant, uncharged function can take any value: no element forces C = 0.
A symmetry can force a relation between two couplings only if it maps one operator into another (SUSY:
O_t <-> |H|^2 |t~|^2; twin Z2: |H_A|^2 <-> |H_B|^2). Step (1) shows no SM symmetry does.
Run from this directory: python c9_symmetry_group.py
"""
import math
import os
import sys

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools')))
import sm_inputs as smi  # noqa: E402
from rg_sm import couplings_at_mt  # noqa: E402

out = []


def P(s=""):
    print(s)
    out.append(str(s))


rng = np.random.default_rng(9)
eps = np.array([[0, 1], [-1, 0]], dtype=complex)


def rand_su2():
    a = rng.normal(size=4)
    a /= np.linalg.norm(a)
    return np.array([[a[0] + 1j * a[1], a[2] + 1j * a[3]], [-a[2] + 1j * a[3], a[0] - 1j * a[1]]])


def cvec(n):
    return rng.normal(size=n) + 1j * rng.normal(size=n)


H, Q, t, b = cvec(2), cvec(2), cvec(1)[0], cvec(1)[0]  # one colour component; colour is a spectator here
Hc = lambda X: eps @ X.conj()  # noqa: E731


def ops(H, Q, t, b, yt=1.0, yb=1.0):
    return dict(mu=np.vdot(H, H).real, lam=np.vdot(H, H).real ** 2,
                t=np.vdot(Q, Hc(H)) * t, b=np.vdot(Q, H) * b)


O0 = ops(H, Q, t, b)
Y = dict(H=0.5, Q=1 / 6, t=2 / 3, b=-1 / 3)


def check(name, newfields, expect):
    O1 = ops(*newfields)
    res = []
    for k in O0:
        r = O1[k] / O0[k]
        res.append(f"{k}:{'same' if abs(r - 1) < 1e-10 else ('phase' if abs(abs(r) - 1) < 1e-10 else 'CHANGED')}")
    P(f"  {name:44s} " + "  ".join(res) + f"   coupling action: {expect}")


P("=" * 110)
P("(1)-(2) Elements of the SM symmetry group acting on the Higgs-sector operators")
P("=" * 110)
U = rand_su2()
check("SU(2)_L (random element)", (U @ H, U @ Q, t, b), "trivial")
a = rng.uniform(0, 2 * np.pi)
check("U(1)_Y (random angle)", (np.exp(1j * a * Y['H']) * H, np.exp(1j * a * Y['Q']) * Q,
                                np.exp(1j * a * Y['t']) * t, np.exp(1j * a * Y['b']) * b), "trivial")
P("  SU(3)_c: Q, t_R, b_R triplets, H singlet; colour contraction Q^dag_i t_i invariant -> trivial")
check("U(1)_B (quarks B = 1/3)", (H, np.exp(1j * a / 3) * Q, np.exp(1j * a / 3) * t, np.exp(1j * a / 3) * b), "trivial")
P("  U(1)_Le, U(1)_Lmu, U(1)_Ltau: act on lepton doublets / e_R only; Higgs-sector operators untouched -> trivial")
P("    (B + L anomalous; B - L and L_i - L_j anomaly-free; all are phase rotations, coupling action trivial)")
R = rand_su2()
Phi = np.column_stack([Hc(H), H])
PhiR = Phi @ R.conj().T
H_R = PhiR[:, 1]
tb = R @ np.array([t, b])  # (t_R, b_R) as SU(2)_R doublet
O1 = ops(H_R, Q, tb[0], tb[1])
P(f"  custodial SU(2)_R (Phi -> Phi R^dag): |H|^2 same: {abs(O1['mu']/O0['mu']-1) < 1e-10}, |H|^4 same: "
  f"{abs(O1['lam']/O0['lam']-1) < 1e-10}; Yukawa sum y(O_t + O_b) same: "
  f"{abs((O1['t']+O1['b'])/(O0['t']+O0['b'])-1) < 1e-10} only for y_t = y_b")
P("    coupling action: trivial on lam, g; g' and y_t - y_b are spurions (approximate symmetry)")
P("  C   : H -> H* (conj. rep.), psi -> psi^c: each operator -> its hermitian conjugate; y -> y*  (C broken by g, g')")
P("  P   : psi_L <-> psi_R: maps O_t to an operator with no SM coupling; broken maximally by SU(2)_L")
P("  CP  : each operator -> its h.c.; y_ij -> y_ij* (broken by the CKM phase, B8)")
P("  T   : antiunitary; same coupling action as CP (CPT exact)")
P("  CPT : exact; maps every operator to its h.c. -> trivial on hermitian L")
P("  classical scale invariance: dimensionless couplings untouched; mu^2 a spurion of dimension 2 (anomalous)")
P("  rephasing of t_R, b_R (flavour U(1)s): y_t -> e^{ia} y_t, y_b -> e^{ib} y_b")

P("\n" + "=" * 110)
P("(3) C under the coupling-space action of every element")
P("=" * 110)
lam, g, gp, yt, yb, al = sp.symbols('lambda g gprime y_t y_b alpha', real=True)
ytc, ybc = sp.symbols('Y_t Y_b')  # complex Yukawas
C = 6 * lam + sp.Rational(9, 4) * g**2 + sp.Rational(3, 4) * gp**2 - 6 * ytc * sp.conjugate(ytc) - 6 * ybc * sp.conjugate(ybc)
acts = {"gauge / B / L_i / CPT": {}, "C, CP, T (y -> y*)": {ytc: sp.conjugate(ytc), ybc: sp.conjugate(ybc)},
        "t_R, b_R rephasing": {ytc: sp.exp(sp.I * al) * ytc, ybc: sp.exp(-sp.I * al) * ybc},
        "sign flips g -> -g, g' -> -g'": {g: -g, gp: -gp}}
for k, m in acts.items():
    P(f"  {k:32s}: C invariant: {sp.simplify(C.subs(m, simultaneous=True) - C) == 0}")
P("  Every element acts DIAGONALLY on (lam, g, g', |y_t|, |y_b|): no element maps one operator into a different")
P("  one, so none relates lam or g to y_t, and C is an invariant (uncharged) function, free to take any value.")
P("  Gauge invariance is the one inhomogeneous symmetry: it ties the V-S-S, V-V-S-S, V-F-F, V^3, V^4 vertices")
P("  to one g per factor, but |H|^4 and (Q^dag H^c) t_R are separately invariant (checked above), so it leaves")
P("  lam and y_t independent.")

P("\n" + "=" * 110)
P("(4) Gildener-Weinberg (scale invariance + dimensional transmutation) with SM content")
P("=" * 110)
v, MW, MZ, Mt, Mh = smi.V, smi.MW, smi.MZ, smi.MT, smi.MH
B0 = (6 * MW**4 + 3 * MZ**4 - 12 * Mt**4) / (64 * math.pi**2 * v**4)
P(f"  B = (6 M_W^4 + 3 M_Z^4 - 12 m_t^4)/(64 pi^2 v^4) = {B0:.4e}  (< 0: no GW minimum; scalon m^2 = 8 B v^2 < 0)")
P("  GW fixes the scalon mass by STr M^4 (B), a relation among g^4, y_t^4 and lam^2-type terms, not C (STr M^2).")
P("  With SM content B < 0, so the relation is unavailable even before asking about C.")

P("\n" + "=" * 110)
P("(5) QCD-condensate EWSB scale factors (Referee D 1)")
P("=" * 110)
fpi = 0.0921
for nd in (1, 3):
    P(f"  n_d = {nd}: v / (sqrt(n_d) f_pi) = {v/(math.sqrt(nd)*fpi):.0f}")
P("  (f_pi held at 92.1 MeV for n_d = 3: [approx]; the chiral-limit f differs by several percent.)")

P("\n" + "=" * 110)
P("(6) F-b significance vs the y_t matching spread (Referee D 5); rows from c5_mt_budget / c7_mt_significance")
P("=" * 110)
MT_STAR = 169.535
slope = couplings_at_mt(Mt=Mt + 0.5)['yt'] - couplings_at_mt(Mt=Mt - 0.5)['yt']
base = [0.418, 0.037, 0.125, 0.086, 0.5, 0.11, 0.29]
dist = Mt - MT_STAR
for dy in (0.0005, 0.001, 0.003, 0.005, 0.0075, 0.01, 0.038):
    tot = math.sqrt(sum(r * r for r in base) + (dy / slope)**2)
    P(f"  delta y_t = {dy:6.4f} ({dy/slope:5.2f} GeV): {dist/tot:4.1f} sigma")
for target in (3.0, 2.0, 1.0):
    need = (dist / target)**2 - sum(r * r for r in base)
    P(f"  significance falls to {target:.0f} sigma at delta y_t = {math.sqrt(max(need, 0))*slope:.4f}")
P("  The spread between published matchings (Buttazzo 0.938 vs Jegerlehner 0.900 at equal inputs) is 0.038.")

with open(os.path.join(HERE, 'c9_symmetry_group_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
