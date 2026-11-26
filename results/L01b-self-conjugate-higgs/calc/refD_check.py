"""Referee D independent checks for L01b (numbers + reproducibility).

Uses only tools/sm_inputs.py and tools/rg_sm.py (couplings_at_mt, run). Sector formulas, R, crossing,
M_t*, d=2 counting, CW, QCD-condensate W mass and the one-loop beta_C polynomial are recomputed here
from scratch, plus an independent 1-loop RGE integrator for the 1-loop mu0.
"""
import math
import os
import sys

import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools')))
import sm_inputs as smi  # noqa: E402
from rg_sm import run, couplings_at_mt  # noqa: E402

MPL = smi.M_PLANCK


def sectors(c, nV=3):
    g, gp, lam = c['g2'], c['gY'], c['lam']
    W = 2 * nV * g**2 / 4 + 2 * lam               # W+-: 2*nV dof * g^2/4 ; G+-: 2*lam
    Zh = nV * (g**2 + gp**2) / 4 + 3 * lam + lam  # Z: nV*(g^2+g'^2)/4 ; h: 3 lam ; G0: lam
    F = 12 * c['yt']**2 / 2 + 12 * c['yb']**2 / 2 + 4 * c['ytau']**2 / 2
    return W, Zh, F


def Cval(c, nV=3):
    W, Zh, F = sectors(c, nV)
    return W + Zh - F


c0 = couplings_at_mt(); c0['gY'] = math.sqrt(3 / 5) * c0['g1']
W, Zh, F = sectors(c0)
print(f"M_t: g2={c0['g2']:.5f} gY={c0['gY']:.5f} g3={c0['g3']:.4f} yt={c0['yt']:.5f} lam={c0['lam']:.5f}")
print(f"M_t sectors: W={W:.4f} Zh={Zh:.4f} F={F:.4f} R={(W + Zh) / F:.4f} C={W + Zh - F:.4f}")
# Veltman-mass form at tree level with pole masses (cross-check of the normalization only)
v = smi.V
print(f"(3/v^2)(mh^2+2MW^2+MZ^2-4mt^2) with pole masses = "
      f"{3 / v**2 * (smi.MH**2 + 2 * smi.MW**2 + smi.MZ**2 - 4 * smi.MT**2):.4f}")
W2, Zh2, F2 = sectors(c0, nV=1)
print(f"d=2 pole (n_V=1): R(M_t)={(W2 + Zh2) / F2:.4f}")

f3 = run(nloops=3, mu_max=1e32)
for L in (10, 16, math.log10(MPL)):
    W, Zh, F = sectors(f3(10**L))
    print(f"log10 mu={L:.2f}: Zh={Zh:.4f} W={W:.4f} F={F:.4f} R={(W + Zh) / F:.4f}")
l0 = brentq(lambda L: Cval(f3(10**L)), 18, 30)
h = 1e-3
dC = (Cval(f3(10**(l0 + h))) - Cval(f3(10**(l0 - h)))) / (2 * h * math.log(10))
print(f"3-loop mu0 = 10^{l0:.3f}, dC/dln mu = {dC:+.4f}")
for n in (1, 2):
    fn = run(nloops=n, mu_max=1e32)
    print(f"{n}-loop (rg_sm) mu0 = 10^{brentq(lambda L: Cval(fn(10**L)), 18, 31.9):.2f}")
Ls = [2.24 + 0.05 * i for i in range(int((31.9 - 2.24) / 0.05))]
cmax = max((Cval(f3(10**L), nV=1), L) for L in Ls)
print(f"n_V=1: max C over 10^2.24..10^31.9 = {cmax[0]:+.4f} at 10^{cmax[1]:.2f}")


# Independent 1-loop RGEs (gY non-GUT normalized, V = lam|H|^4), yb, ytau kept at 1 loop
def beta1(t, s):
    g1, g2, g3, yt, yb, ytau, lam = s
    k = 1 / (16 * math.pi**2)
    Y2 = 3 * yt**2 + 3 * yb**2 + ytau**2
    return [k * 41 / 6 * g1**3, k * (-19 / 6) * g2**3, k * (-7) * g3**3,
            k * yt * (1.5 * yt**2 - 1.5 * yb**2 + Y2 - 17 / 12 * g1**2 - 9 / 4 * g2**2 - 8 * g3**2),
            k * yb * (1.5 * yb**2 - 1.5 * yt**2 + Y2 - 5 / 12 * g1**2 - 9 / 4 * g2**2 - 8 * g3**2),
            k * ytau * (1.5 * ytau**2 + Y2 - 15 / 4 * g1**2 - 9 / 4 * g2**2),
            k * (24 * lam**2 - 6 * yt**4 - 6 * yb**4 - 2 * ytau**4 + 3 / 8 * (2 * g2**4 + (g2**2 + g1**2)**2)
                 + lam * (4 * Y2 - 9 * g2**2 - 3 * g1**2))]


s0 = [c0['gY'], c0['g2'], c0['g3'], c0['yt'], c0['yb'], c0['ytau'], c0['lam']]
sol = solve_ivp(beta1, (math.log(smi.MT), math.log(1e32)), s0, dense_output=True, rtol=1e-10, atol=1e-13)


def Cown(L):
    gY, g2, g3, yt, yb, ytau, lam = sol.sol(L * math.log(10))
    return Cval(dict(g2=g2, gY=gY, yt=yt, yb=yb, ytau=ytau, lam=lam))


print(f"own 1-loop RGE mu0 = 10^{brentq(Cown, 18, 31.9):.2f}")


def Cpl(Mt, **kw):
    return Cval(run(nloops=3, mu_max=2e19, Mt=Mt, **kw)(MPL))


mts = brentq(lambda m: Cpl(m), 165, 175)
print(f"M_t* (C(M_Pl)=0) = {mts:.3f} GeV; distance = {smi.MT - mts:.3f}")
for da in (+0.0009, -0.0009):
    m2 = brentq(lambda m: Cpl(m, als=smi.ALPHA_S_MZ + da), 160, 180)
    print(f"  alpha_s {da:+.4f}: M_t* = {m2:.3f} (shift {m2 - mts:+.3f})")
for dmh in (+0.11,):
    m2 = brentq(lambda m: Cpl(m, Mh=smi.MH + dmh), 160, 180)
    print(f"  M_h +0.11: M_t* shift {m2 - mts:+.3f}")
m2l = brentq(lambda m: Cval(run(nloops=2, mu_max=2e19, Mt=m)(MPL)), 160, 180)
print(f"  2-loop RGE: M_t* shift {m2l - mts:+.3f}")
base = [0.42, 0.50, 0.29, 0.13, 0.11, 0.09, 0.09, 0.04]
for dy in (0.0005, 0.003, 0.004):
    b = base.copy(); b[5] = dy / 0.00556
    tot = math.sqrt(sum(x * x for x in b))
    print(f"  dy={dy}: budget {tot:.3f}, signif {(smi.MT - mts) / tot:.2f} sigma")
b = [0.42, 0.70, 0.13, 0.11, 0.003 / 0.00556, 0.09, 0.04]
print(f"  sigma(tt) pole 172.4+-0.7, dy=0.003: {(172.4 - mts) / math.sqrt(sum(x * x for x in b)):.2f} sigma")

# Coleman-Weinberg, mu^2 = 0
B = (6 * smi.MW**4 + 3 * smi.MZ**4 - 12 * smi.MT**4) / (64 * math.pi**2 * v**4)
print(f"CW B = {B:.3e}; top threshold m_t = {((2 * smi.MW**4 + smi.MZ**4) / 4)**0.25:.1f} GeV; "
      f"W,Z-only m_h = sqrt(8 B_WZ) v = "
      f"{math.sqrt(8 * 3 * (2 * smi.MW**4 + smi.MZ**4) / (64 * math.pi**2 * v**4)) * v:.2f} GeV; "
      f"tree mu = {smi.MH / math.sqrt(2):.2f}")

# QCD condensate
fpi = 0.0921
g = 2 * smi.MW / v
for nd in (1, 3):
    print(f"QCD EWSB n_d={nd}: M_W = {g * math.sqrt(nd) * fpi / 2 * 1e3:.2f} MeV")
print(f"f_pi^2/v^2 = {(fpi / v)**2:.3e}; dM_W = {smi.MW * 0.5 * (fpi / v)**2 * 1e6:.2f} keV; v/f_pi = {v / fpi:.0f}")

# one-loop beta_C on C=0 (yb = ytau = 0), 16 pi^2 units
g2, gp, g3, y, lam = sp.symbols('g gp g3 y lam', positive=True)
dg2 = -sp.Rational(19, 3) * g2**4
dgp2 = sp.Rational(41, 3) * gp**4
dy2 = 2 * y**2 * (sp.Rational(9, 2) * y**2 - sp.Rational(17, 12) * gp**2 - sp.Rational(9, 4) * g2**2 - 8 * g3**2)
blam = 24 * lam**2 - 6 * y**4 + sp.Rational(3, 8) * (2 * g2**4 + (g2**2 + gp**2)**2) + lam * (12 * y**2 - 9 * g2**2 - 3 * gp**2)
bC = 6 * blam + sp.Rational(9, 4) * dg2 + sp.Rational(3, 4) * dgp2 - 6 * dy2
lam0 = (6 * y**2 - sp.Rational(9, 4) * g2**2 - sp.Rational(3, 4) * gp**2) / 6
claimed = (33 * g2**4 + sp.Rational(63, 2) * g2**2 * gp**2 - 162 * g2**2 * y**2 + 96 * g3**2 * y**2
           + 17 * gp**4 - 46 * gp**2 * y**2 + 126 * y**4)
print("beta_C on C=0:", sp.expand(bC.subs(lam, lam0)))
print("difference from WORK S5 polynomial:", sp.simplify(sp.expand(bC.subs(lam, lam0)) - claimed))
