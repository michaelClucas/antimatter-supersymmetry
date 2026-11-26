"""L01b task 4: running of the pair-matching ratio R(mu) = C_bosons / |C_fermion seas| with tools/rg_sm.py.

R = 1 is the Veltman condition C = 0 (one-loop Lambda^2 coefficient, Landau gauge), restated as
"boson pair fluctuations (charged pairs + self-conjugate quanta) match the fermion Dirac-sea fluctuations".
Split: self-conjugate bosons (Z, h, G0):  3/4 (g^2 + g'^2) + 3 lambda + lambda
       charged pairs (W+W-, G+G-):        3/2 g^2 + 2 lambda
       fermion seas: 6 y_t^2 + 6 y_b^2 + 2 y_tau^2
Also: the falsifiable M_t values (pole) at which R = 1 exactly at M_Pl and at 10^16 GeV, and loop-order /
input dependence of the crossing scale.
"""
import math
import os
import sys

from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools')))
import sm_inputs as smi  # noqa: E402
from rg_sm import run  # noqa: E402

out = []


def P(s=""):
    print(s)
    out.append(str(s))


def pieces(c):
    sc = 0.75 * (c['g2']**2 + c['gY']**2) + 4 * c['lam']
    ch = 1.5 * c['g2']**2 + 2 * c['lam']
    fs = 6 * c['yt']**2 + 6 * c['yb']**2 + 2 * c['ytau']**2
    return sc, ch, fs


def crossing(nloops=3, **kw):
    f = run(nloops=nloops, mu_max=1e32, **kw)

    def C(l):
        sc, ch, fs = pieces(f(10**l))
        return sc + ch - fs
    return brentq(C, 12, 31.5), f


MPL = smi.M_PLANCK
P("R(mu) = (self-conjugate + charged-pair boson pieces) / fermion-sea piece, 3-loop MS-bar, PDG 2024 central inputs")
l0, f = crossing(3)
P(f"{'log10 mu':>9s} {'self-conj':>10s} {'charged':>9s} {'ferm sea':>9s} {'R':>7s} {'1-R':>7s} {'lambda':>9s}")
for l in (math.log10(smi.MT), 4, 6, 8, 10, 12, 14, 16, 18, math.log10(MPL), 20, 22, l0, 24, 26):
    c = f(10**l)
    sc, ch, fs = pieces(c)
    P(f"{l:9.2f} {sc:+10.4f} {ch:+9.4f} {fs:9.4f} {(sc+ch)/fs:7.4f} {1-(sc+ch)/fs:+7.4f} {c['lam']:+9.5f}")
P(f"\nR = 1 (C = 0) at log10(mu0/GeV) = {l0:.3f} (3-loop)")
for n in (1, 2):
    P(f"   {n}-loop RGEs: log10 mu0 = {crossing(n)[0]:.3f}")

P("\nInput dependence of the crossing (3-loop):")
for kw in (dict(Mt=smi.MT - 0.29), dict(Mt=smi.MT + 0.29), dict(als=smi.ALPHA_S_MZ - 0.0009),
           dict(als=smi.ALPHA_S_MZ + 0.0009), dict(Mh=smi.MH - 0.11), dict(Mh=smi.MH + 0.11)):
    P(f"   {kw}: log10 mu0 = {crossing(3, **kw)[0]:.3f}")


def Mt_for_zero_at(mu):
    def g(Mt):
        ff = run(nloops=3, mu_max=mu * 1.01, Mt=Mt)
        sc, ch, fs = pieces(ff(mu))
        return sc + ch - fs
    return brentq(g, 160.0, 175.0)


P("\nM_t (pole) at which boson pairs exactly match fermion seas (R = 1), other inputs central:")
P("   [WITHDRAWN c4/c10: the sigma values below use the experimental M_t error (0.29 GeV) only and are not a")
P("    significance. See c5_mt_budget_out.txt (0.74 GeV budget, 4.1 sigma) and c7_mt_significance_out.txt.]")
for name, mu in (("M_Pl = 1.22e19 GeV", MPL), ("reduced M_Pl = 2.4e18 GeV", 2.435e18), ("10^16 GeV", 1e16)):
    mt = Mt_for_zero_at(mu)
    P(f"   R = 1 at {name:26s}: M_t = {mt:.2f} GeV  ({(mt - smi.MT)/0.29:+.1f} 'sigma' from {smi.MT} +- 0.29,"
      f" withdrawn)")
v = smi.V
br = smi.MH**2 + 2 * smi.MW**2 + smi.MZ**2
P(f"   R = 1 at the EW scale (tree, pole masses): m_t = sqrt((m_h^2+2M_W^2+M_Z^2)/4) = {math.sqrt(br/4):.1f} GeV,"
  f" or m_h = {math.sqrt(4*smi.MT**2 - 2*smi.MW**2 - smi.MZ**2):.1f} GeV at the measured m_t")

with open(os.path.join(HERE, 'matching_running_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
