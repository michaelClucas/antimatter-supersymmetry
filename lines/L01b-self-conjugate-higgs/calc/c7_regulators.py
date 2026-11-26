"""L01b cycle 7: correction of the cycle-4 regulator claim (Referee A c6 finding 2, Referee B c6 finding 2).

The Lambda^2-type coefficient per species is n_i * (1/2) d^2 M_i^2/dphi^2 times a regulator constant. The multiplicity
n_i of a massive vector is the number of physical-plus-unphysical transverse components:
  - 4D hard cutoff, Pauli-Villars, dimensional REDUCTION: n_V(transverse) = 3            -> R = 0.344 at M_t
  - dimensional regularization, read off at the d = 2 pole: n_V(transverse) = d - 1 = 1 -> different R
So the cycle-4 sentence "the same with the d = 2 pole of dim reg" was false; only cutoff and PV (and DRED) agree.
Caveat: a 4D hard cutoff on gauge loops is not gauge invariant; its agreement with PV holds for the
momentum routing of the one-loop effective potential (loop momentum = field momentum), not in general.
Run from this directory: python c7_regulators.py
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


phi, g, gp, lam, d, xi = sp.symbols('phi g gp lam d xi', positive=True)
mu2 = sp.symbols('mu2')
MW2, MZ2 = g**2 * phi**2 / 4, (g**2 + gp**2) * phi**2 / 4
mG2, mh2 = -mu2 + lam * phi**2, -mu2 + 3 * lam * phi**2


def gauge_dir(M2, nv):  # background R_xi, one real gauge direction: transverse, longitudinal, Goldstone, ghosts
    return nv * M2 + xi * M2 + (mG2 + xi * M2) - 2 * xi * M2


hdd = lambda e: sp.factor(sp.diff(e, phi, 2) / 2)
W = hdd(2 * gauge_dir(MW2, d - 1))
Zh = hdd(gauge_dir(MZ2, d - 1) + mh2)
P(f"Sector coefficients with transverse multiplicity d-1 (xi drops out):\n  W = {W}\n  Z+h = {Zh}")
P(f"  d=4 (cutoff, PV, DRED): W = {W.subs(d, 4)}, Z+h = {sp.expand(Zh.subs(d, 4))}")
P(f"  d=2 pole of DREG     : W = {W.subs(d, 2)}, Z+h = {sp.expand(Zh.subs(d, 2))}")


def R(f, nv):
    cw = (nv / 2) * f['g2']**2 + 2 * f['lam']
    cz = (nv / 4) * (f['g2']**2 + f['gY']**2) + 4 * f['lam']
    cf = 6 * f['yt']**2 + 6 * f['yb']**2 + 2 * f['ytau']**2
    return (cw + cz) / cf


s = run(nloops=3, mu_max=1e30)
P("\nR = C_bos/|C_ferm| (3-loop running, Buttazzo matching, PDG 2024)")
P("  log10 mu    R(n_V=3: cutoff/PV/DRED)   R(n_V=d-1=1: DREG d=2 pole)")
for l in (math.log10(smi.MT), 10, 16, math.log10(smi.M_PLANCK)):
    f = s(10**l)
    P(f"  {l:7.2f}     {R(f, 3):.3f}                      {R(f, 1):.3f}")
l3 = brentq(lambda l: R(s(10**l), 3) - 1, 15, 29)
try:
    l1 = f"10^{brentq(lambda l: R(s(10**l), 1) - 1, 15, 29.9):.2f} GeV"
except ValueError:
    l1 = "no crossing below 10^29.9 GeV"
P(f"  mu0 (R=1): n_V=3 -> 10^{l3:.2f} GeV ; n_V=1 -> {l1}")
P("\nConclusion: R and mu0 are regulator-dependent numbers, not observables. In d=4 DREG/MS-bar the term is absent.")
P("Cutoff and PV agree because both weight every physical dof of a 4D field equally; DREG's d=2 pole does not.")

with open(os.path.join(HERE, 'c7_regulators_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
