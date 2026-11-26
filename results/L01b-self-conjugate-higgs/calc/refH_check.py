"""Referee H independent check of L01b numbers. No imports from the line's calc/ scripts.

Inputs typed in from CONSTRAINTS.md (PDG 2024). Running: own 1-loop RGEs (written here) and, for the
3-loop zero, tools/rg_sm.py's run() fed with initial conditions transcribed here (not via couplings_at_mt).

C = 6 lam + 9/4 g^2 + 3/4 g'^2 - 6 y_t^2 - 6 y_b^2 - 2 y_tau^2   (CONSTRAINTS G normalization)
Run from this directory: python refH_check.py   (prints only; writes refH_check_out.txt)
"""
import math
import os
import sys

from scipy.integrate import solve_ivp
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
out = []


def P(s=""):
    print(s)
    out.append(str(s))


# ---- PDG 2024 inputs from CONSTRAINTS.md C1, C2, D
Mt, dMt = 172.57, 0.29
Mh, dMh = 125.20, 0.11
MW, dMW = 80.3692, 0.0133
MZ, dMZ = 91.1876, 0.0021
GF = 1.1663788e-5
als, dals = 0.1180, 0.0009
aem_inv, s2w = 127.930, 0.23129
v = (math.sqrt(2) * GF) ** -0.5
MPL = 1.220890e19

P(f"v = {v:.4f} GeV")

# ================= (1) pole-mass form =================
def Cpole(mt=Mt, mh=Mh, mw=MW, mz=MZ):
    return 3 / v**2 * (mh**2 + 2 * mw**2 + mz**2 - 4 * mt**2)


c0 = Cpole()
br = (Mh**2 + 2 * MW**2 + MZ**2 - 4 * Mt**2)
P(f"(1) Veltman bracket = {br:.1f} GeV^2 (CONSTRAINTS G: ~ -8.2e4)")
d = {k: abs(f(+1) - f(-1)) / 2 for k, f in {
    'Mt': lambda s: Cpole(mt=Mt + s * dMt), 'Mh': lambda s: Cpole(mh=Mh + s * dMh),
    'MW': lambda s: Cpole(mw=MW + s * dMW), 'MZ': lambda s: Cpole(mz=MZ + s * dMZ)}.items()}
sig = math.sqrt(sum(x * x for x in d.values()))
dCdmt = 24 * Mt / v**2
sigMC = math.hypot(sig, dCdmt * 0.5)
P(f"    C_pole(M_t) = {c0:.4f}; sigma(PDG) = {sig:.4f} -> {abs(c0)/sig:.0f} sigma; "
  f"+0.5 GeV MC: sigma = {sigMC:.4f} -> {abs(c0)/sigMC:.0f} sigma")
P(f"    rows: " + ", ".join(f"{k} {x:.4f}" for k, x in d.items()) + f", MC {dCdmt*0.5:.4f}")
mt0 = math.sqrt((Mh**2 + 2 * MW**2 + MZ**2) / 4)
P(f"    C_pole = 0 at m_t = {mt0:.2f} GeV")

# ================= (2) MS-bar at M_t, Buttazzo et al. 1307.3536 eqs (55)-(60), transcribed here ======
a3 = (als - 0.1184) / 0.0007


def buttazzo(mt=Mt, mh=Mh, mw=MW, al=als):
    a = (al - 0.1184) / 0.0007
    return dict(lam=0.12604 + 0.00206 * (mh - 125.15) - 0.00004 * (mt - 173.34),
                yt=0.93690 + 0.00556 * (mt - 173.34) - 0.00042 * a,
                g2=0.64779 + 0.00004 * (mt - 173.34) + 0.00011 * (mw - 80.384) / 0.014,
                gY=0.35830 + 0.00011 * (mt - 173.34) - 0.00020 * (mw - 80.384) / 0.014,
                g3=1.1666 + 0.00314 * a - 0.00046 * (mt - 173.34))


yb, ytau = math.sqrt(2) * 2.75 / v, math.sqrt(2) * 1.75 / v  # small; same rough values as tools/rg_sm


def Cms(c, yb_=yb, ytau_=ytau):
    bos = 6 * c['lam'] + 2.25 * c['g2']**2 + 0.75 * c['gY']**2
    fer = 6 * c['yt']**2 + 6 * yb_**2 + 2 * ytau_**2
    return bos - fer, bos, fer


cb = buttazzo()
C_ms, bos, fer = Cms(cb)
P(f"(2) Buttazzo fits at M_t: y_t={cb['yt']:.5f} lam={cb['lam']:.5f} g={cb['g2']:.5f} g'={cb['gY']:.5f}")
P(f"    C_MS(M_t) = {C_ms:.4f};  boson sum = {bos:.4f}, fermion sum = {fer:.4f};  R = {bos/fer:.4f}")
rows = {}
for k, dd in (('Mt', dMt), ('Mh', dMh), ('MW', dMW), ('als', dals)):
    up = Cms(buttazzo(**{{'Mt': 'mt', 'Mh': 'mh', 'MW': 'mw', 'als': 'al'}[k]: {'Mt': Mt, 'Mh': Mh, 'MW': MW, 'als': als}[k] + dd}))[0]
    dn = Cms(buttazzo(**{{'Mt': 'mt', 'Mh': 'mh', 'MW': 'mw', 'als': 'al'}[k]: {'Mt': Mt, 'Mh': Mh, 'MW': MW, 'als': als}[k] - dd}))[0]
    rows[k] = abs(up - dn) / 2
dCdyt = 12 * cb['yt']
for lab, extra in (("PDG + y_t th 0.0005", {'yt_th': dCdyt * 0.0005}),
                   ("PDG + MC 0.5 + y_t 0.003", {'MC': dCdyt * 0.00556 * 0.5, 'yt_th': dCdyt * 0.003}),
                   ("PDG + MC 0.5 + y_t 0.038 (Buttazzo-Jegerlehner spread)",
                    {'MC': dCdyt * 0.00556 * 0.5, 'yt_th': dCdyt * 0.038})):
    r = dict(rows)
    r.update(extra)
    s = math.sqrt(sum(x * x for x in r.values()))
    P(f"    {lab:55s}: sigma = {s:.4f} -> |C|/sigma = {abs(C_ms)/s:.1f}")
P(f"    rows: " + ", ".join(f"{k} {x:.4f}" for k, x in rows.items()))
P(f"    pole form minus MS-bar form = {c0 - C_ms:+.3f} (scheme difference, not inside any quoted sigma)")
P(f"    with Jegerlehner y_t = 0.9005: C_MS = {Cms(dict(cb, yt=0.9005))[0]:.4f}")

# ================= (3) crude own matching, independent of Buttazzo fits =================
# alpha_s(M_Z) -> alpha_s(M_t), 2-loop, nf=5 (then 6 above M_t is irrelevant here)
def run_as(a0, mu0, mu1, nf=5):
    b0 = 11 - 2 * nf / 3
    b1 = 102 - 38 * nf / 3
    f = lambda t, a: [-(b0 * a[0]**2 / (2 * math.pi) + b1 * a[0]**3 / (8 * math.pi**2))]  # noqa: E731
    return solve_ivp(f, (math.log(mu0), math.log(mu1)), [a0], rtol=1e-11).y[0][-1]


as_mt = run_as(als, MZ, Mt)
# pole -> MS-bar m_t(m_t), 3-loop QCD (Melnikov-van Ritbergen; Chetyrkin-Steinhauser), n_l = 5
def mbar_from_pole(M):
    m = M / 1.06
    for _ in range(50):
        a = run_as(als, MZ, m) / math.pi
        m = M / (1 + 4 / 3 * a + (13.4434 - 1.0414 * 5) * a**2 + (190.595 - 26.655 * 5 + 0.6527 * 25) * a**3)
    return m


mm = mbar_from_pole(Mt)
# m(mu) = m(m) (as(mu)/as(m))^(4/b0), 1-loop QCD mass running
b0 = 11 - 2 * 5 / 3
m_at_Mt = mm * (as_mt / run_as(als, MZ, mm)) ** (4 / b0 / 1)
yt_qcd = math.sqrt(2) * m_at_Mt / v
# gauge couplings: MS-bar at MZ from CONSTRAINTS D, 1-loop to M_t
aem = 1 / aem_inv
g2_mz2 = 4 * math.pi * aem / s2w
gY_mz2 = 4 * math.pi * aem / (1 - s2w)
L = math.log(Mt / MZ) / (8 * math.pi**2)
g2_mt2 = g2_mz2 / (1 - (-19 / 6) * g2_mz2 * L)
gY_mt2 = gY_mz2 / (1 - (41 / 6) * gY_mz2 * L)
lam_tree = Mh**2 / (2 * v**2)
c_own = dict(lam=lam_tree, yt=yt_qcd, g2=math.sqrt(g2_mt2), gY=math.sqrt(gY_mt2))
C_own = Cms(c_own)
P(f"(3) own crude matching (QCD-only y_t, tree lam, 1-loop g,g'): as(M_t)={as_mt:.4f}, mbar(mbar)={mm:.2f}, "
  f"y_t={yt_qcd:.4f}, lam={lam_tree:.4f}, g={c_own['g2']:.4f}, g'={c_own['gY']:.4f}")
P(f"    C_own(M_t) = {C_own[0]:.4f}, R = {C_own[1]/C_own[2]:.4f}")

# ================= (4) zero of C: own 1-loop RGEs (d g / d ln mu) =================
k = 1 / (16 * math.pi**2)


def beta1(t, s):
    g1, g2, g3, yt, lam = s  # g1 = g' (hypercharge, SM normalization)
    return [k * 41 / 6 * g1**3, k * (-19 / 6) * g2**3, k * (-7) * g3**3,
            k * yt * (9 / 2 * yt**2 - 8 * g3**2 - 9 / 4 * g2**2 - 17 / 12 * g1**2),
            k * (24 * lam**2 + 12 * lam * yt**2 - 6 * yt**4 - 3 * lam * (3 * g2**2 + g1**2)
                 + 3 / 8 * (2 * g2**4 + (g2**2 + g1**2)**2))]


s0 = [cb['gY'], cb['g2'], cb['g3'], cb['yt'], cb['lam']]
sol = solve_ivp(beta1, (math.log(Mt), math.log(1e30)), s0, dense_output=True, rtol=1e-11, atol=1e-13)


def C1(l10):
    g1, g2, g3, yt, lam = sol.sol(l10 * math.log(10))
    return 6 * lam + 2.25 * g2**2 + 0.75 * g1**2 - 6 * yt**2  # y_b, y_tau dropped (< 1e-3)


z1 = brentq(C1, 15, 29.9)
P(f"(4) own 1-loop RGEs (no y_b, y_tau): C = 0 at log10 mu = {z1:.2f}  (line: 26.79 at 1 loop)")

# ---- 3-loop with tools/rg_sm.run(), initial conditions from (2), not couplings_at_mt
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools')))
from rg_sm import run  # noqa: E402

ini = dict(g1=math.sqrt(5 / 3) * cb['gY'], g2=cb['g2'], g3=cb['g3'], yt=cb['yt'], yb=yb, ytau=ytau,
           lam=cb['lam'], m2=(131.55 + 0.94 * (Mh - 125.15) + 0.17 * (Mt - 173.34))**2)


def zero3(ini, nl=3):
    f = run(nloops=nl, mu_max=1e28, inputs=ini, Mt=Mt)

    def C(l):
        c = f(10**l)
        return Cms(dict(lam=c['lam'], yt=c['yt'], g2=c['g2'], gY=c['gY']), c['yb'], c['ytau'])[0]
    z = brentq(C, 12, 27.9, xtol=1e-7)
    h = 1e-3
    slope = (C(z + h) - C(z - h)) / (2 * h) / math.log(10)
    cmax = max(C(2.24 + 0.005 * i) for i in range(int((math.log10(MPL) - 2.24) / 0.005) + 1))
    return z, slope, cmax, C


for nl in (2, 3):
    z, s, cm, C = zero3(ini, nl)
    P(f"    tools/rg_sm {nl}-loop: C = 0 at log10 mu = {z:.3f}, dC/dln mu = {s:+.4f}, max C on [M_t, M_Pl] = {cm:.3f}")
z, s, cm, C = zero3(ini, 3)
P(f"    3-loop: C(M_Pl) = {C(math.log10(MPL)):+.4f}")
iniJ = dict(ini, yt=0.9005)
zJ, sJ, cmJ, _ = zero3(iniJ, 3)
P(f"    3-loop, y_t(M_t) = 0.9005: zero at log10 mu = {zJ:.3f}, slope {sJ:+.4f}")
# own-matching start for the zero (crude)
iniO = dict(ini, yt=yt_qcd, lam=lam_tree, g2=c_own['g2'], g1=math.sqrt(5 / 3) * c_own['gY'])
zO, sO, _, _ = zero3(iniO, 3)
P(f"    3-loop, own crude matching start: zero at log10 mu = {zO:.3f}, slope {sO:+.4f}")
# dependence of the zero on M_t via the fits
for dm in (-dMt, dMt):
    c2 = buttazzo(mt=Mt + dm)
    i2 = dict(ini, g1=math.sqrt(5 / 3) * c2['gY'], g2=c2['g2'], g3=c2['g3'], yt=c2['yt'], lam=c2['lam'])
    f = run(nloops=3, mu_max=1e28, inputs=i2, Mt=Mt + dm)
    zz = brentq(lambda l: Cms(dict(lam=f(10**l)['lam'], yt=f(10**l)['yt'], g2=f(10**l)['g2'],
                                   gY=f(10**l)['gY']), f(10**l)['yb'], f(10**l)['ytau'])[0], 12, 27.9)
    P(f"    M_t {Mt+dm:.2f}: zero at {zz:.3f}")

with open(os.path.join(HERE, 'refH_check_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
