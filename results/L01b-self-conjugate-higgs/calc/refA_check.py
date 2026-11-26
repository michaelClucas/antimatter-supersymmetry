"""Referee A (cycle 6) independent checks for L01b. Run from this directory: python refA_check.py"""
import math
import os
import sys

import sympy as sp
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools')))
import sm_inputs as smi  # noqa: E402
from rg_sm import run, couplings_at_mt  # noqa: E402

out = []


def P(s=""):
    print(s)
    out.append(str(s))


# ---------------- 1. sector coefficients, own derivation
phi, g, gp, lam, y, mu2, xi, xiW, xiZ, d = sp.symbols('phi g gp lam y mu2 xi xiW xiZ d', positive=True)
MW2 = g**2 * phi**2 / 4
MZ2 = (g**2 + gp**2) * phi**2 / 4
mh2 = -mu2 + 3 * lam * phi**2
mG2 = -mu2 + lam * phi**2
mt2 = y**2 * phi**2 / 2
half_dd = lambda e: sp.simplify(sp.diff(e, phi, 2) / 2)

# (i) background-field R_xi: per real gauge direction: (d-1) transverse M^2, longitudinal xi M^2,
# Goldstone mG2 + xi M^2, ghost pair -2 xi M^2
def gauge_dir(M2, x, nv=3):
    return nv * M2 + x * M2 + (mG2 + x * M2) - 2 * x * M2

W = 2 * gauge_dir(MW2, xiW)
Z = gauge_dir(MZ2, xiZ)
H = mh2
T = -4 * 3 * mt2
P("1. Sector Lambda^2 coefficients C_i = (1/2) d^2/dphi^2 STr M^2")
P(f"  BG R_xi : W = {half_dd(W)},  Z = {half_dd(Z)},  h = {half_dd(H)},  top = {half_dd(T)}")
# (ii) Fermi gauge: mixed (A_L, G) block has k^4 + mG2 k^2 + xi mG2 M^2 -> two roots, sum = mG2; ghosts massless
def fermi_dir(M2, x):
    k2 = sp.symbols('k2')
    roots = sp.solve(k2**2 - mG2 * k2 + x * mG2 * M2, k2)
    return 3 * M2 + sp.simplify(sum(roots))

P(f"  Fermi   : W = {half_dd(2 * fermi_dir(MW2, xiW))},  Z = {half_dd(fermi_dir(MZ2, xiZ))}")
# (iii) d-dependent vector multiplicity (d-1): residue at d = 2 weights transverse vectors by 1, not 3
Wd = 2 * gauge_dir(MW2, xiW, nv=d - 1)
Zd = gauge_dir(MZ2, xiZ, nv=d - 1)
P(f"  vector weight (d-1): W = {sp.factor(half_dd(Wd))},  Z = {sp.factor(half_dd(Zd))}  (d=2: W={half_dd(Wd).subs(d, 2)}, Z={half_dd(Zd).subs(d, 2)})")

# ---------------- 2. one-loop beta of C on C = 0
g3 = sp.symbols('g3', positive=True)
bg = -sp.Rational(19, 6) * g**3
bgp = sp.Rational(41, 6) * gp**3
by = y * (sp.Rational(9, 2) * y**2 - 8 * g3**2 - sp.Rational(9, 4) * g**2 - sp.Rational(17, 12) * gp**2)
blam = 24 * lam**2 - 6 * y**4 + sp.Rational(3, 8) * (2 * g**4 + (g**2 + gp**2)**2) + lam * (12 * y**2 - 9 * g**2 - 3 * gp**2)
C = 6 * lam + sp.Rational(9, 4) * g**2 + sp.Rational(3, 4) * gp**2 - 6 * y**2
bC = 6 * blam + sp.diff(C, g) * bg + sp.diff(C, gp) * bgp + sp.diff(C, y) * by
lam0 = sp.solve(C, lam)[0]
bC0 = sp.expand(bC.subs(lam, lam0))
claimed = 33 * g**4 + sp.Rational(63, 2) * g**2 * gp**2 - 162 * g**2 * y**2 + 96 * g3**2 * y**2 + 17 * gp**4 - 46 * gp**2 * y**2 + 126 * y**4
P(f"\n2. 16pi^2 beta_C on C=0: {bC0}\n   difference from WORK sec.4 polynomial: {sp.simplify(bC0 - claimed)}")


# ---------------- 3. numerics
def sectors(f):
    cw = 1.5 * f['g2']**2 + 2 * f['lam']
    cz = 0.75 * (f['g2']**2 + f['gY']**2) + 4 * f['lam']
    cf = 6 * f['yt']**2 + 6 * f['yb']**2 + 2 * f['ytau']**2
    return cw, cz, cf


def Cval(l, n=3, **kw):
    f = run(nloops=n, mu_max=10**(l + 0.1), **kw)(10**l)
    cw, cz, cf = sectors(f)
    return cw + cz - cf


P("\n3. Sectors and R (3-loop, Buttazzo matching, PDG 2024)")
s = run(nloops=3, mu_max=1e24)
for l in (math.log10(smi.MT), 10, 16, math.log10(smi.M_PLANCK), 22.83):
    cw, cz, cf = sectors(s(10**l))
    P(f"  log10mu={l:6.2f}  W={cw:.3f} Z+h={cz:.3f} ferm={cf:.3f}  R={(cw+cz)/cf:.3f}  (W {cw/cf:.3f}, Z+h {cz/cf:.3f})")
for n in (3, 2, 1):
    P(f"  mu0 ({n}-loop RGE): 10^{brentq(lambda l: Cval(l, n), 15, 30):.2f}")
c = couplings_at_mt()
P(f"  y_t(M_t) = {c['yt']:.4f}, lam(M_t) = {c['lam']:.4f}")
LPL = math.log10(smi.M_PLANCK)
mts = brentq(lambda m: Cval(LPL, Mt=m), 160, 175, xtol=1e-4)
P(f"  M_t* (C(M_Pl)=0) = {mts:.3f} GeV; distance {smi.MT - mts:.2f} GeV")
dals = abs(brentq(lambda m: Cval(LPL, Mt=m, als=0.1189), 160, 175) - brentq(lambda m: Cval(LPL, Mt=m, als=0.1171), 160, 175)) / 2
P(f"  dM_t* from alpha_s +-0.0009: {dals:.3f} GeV")
# alternative budget: add the indirect (cross-section) pole-mass determination spread, PDG 2024 ~ 172.4 +- 0.7
for lab, extra in (("as quoted", []), ("+ yt matching 2-loop EW spread 0.003 in y_t (~0.54 GeV)", [0.003 / 0.00556])):
    rows = [0.418, 0.037, 0.087, 0.125, 0.086, 0.5, 0.11, 0.29] + extra
    tot = math.sqrt(sum(r * r for r in rows))
    P(f"  budget {lab}: total {tot:.3f} GeV -> {(smi.MT - mts)/tot:.1f} sigma")
P("  using indirect sigma(tt) pole mass 172.4 +- 0.7 GeV alone: "
  f"{(172.4 - mts)/math.hypot(0.7, 0.418, 0.11):.1f} sigma (+ alpha_s, renormalon; no MC term)")

# R with d=2-pole vector weight 1
f = s(smi.MT)
cw1 = 0.5 * f['g2']**2 + 2 * f['lam']
cz1 = 0.25 * (f['g2']**2 + f['gY']**2) + 4 * f['lam']
_, _, cf = sectors(f)
P(f"\n4. R(M_t) if transverse vectors weighted by d-1 = 1 at the d=2 pole: {(cw1+cz1)/cf:.3f} (vs 0.344)")

with open(os.path.join(HERE, 'refA_check_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
