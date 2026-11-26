"""Referee F independent check for L01b. Imports nothing from the line or from tools/.

(1) C(M_t) in two ways:
    (P) tree pole-mass form (3/v^2)(m_h^2 + 2 M_W^2 + M_Z^2 - 4 m_t^2), with linear error propagation.
    (M) MS-bar at mu = M_t from the Buttazzo et al. (arXiv:1307.3536) NNLO fit formulas, typed in here
        independently (eqs. for lambda, y_t, g2, gY, g3 at mu = M_t).
(2) m_t and y_t(M_t) needed for C = 0.
(3) One-loop SM RGE (own implementation, y_t, lambda, g', g, g3) from M_t: sign of C on [M_t, M_Pl]
    and the one-loop crossing scale (line quotes 10^26.79 at 1 loop), plus the slope at the crossing.
(4) H^c = i sigma2 H*: Jacobian rank, |H^c|^2 = |H|^2, H^c^dag H = 0; twin counterfactual Hessian.
(5) CW coefficient B = 3(2 M_W^4 + M_Z^4 - 4 m_t^4)/(64 pi^2 v^4).
(6) Sector numbers at M_t: 3 lambda / 6 y_t^2, R.
Run from this directory: python refF_check.py
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

v = 246.22
Mt, Mh, MW, MZ, als = 172.57, 125.20, 80.3692, 91.1876, 0.1180
eMt, eMh, eMW, eMZ = 0.29, 0.11, 0.0133, 0.0021
MPL = 1.22e19

print("(1P) pole form")
def Cp(mt=Mt, mh=Mh, mw=MW, mz=MZ):
    return 3 / v**2 * (mh**2 + 2 * mw**2 + mz**2 - 4 * mt**2)
c0 = Cp()
d = {'mt': 24 * Mt / v**2 * eMt, 'mh': 6 * Mh / v**2 * eMh, 'mw': 12 * MW / v**2 * eMW, 'mz': 6 * MZ / v**2 * eMZ}
s = math.sqrt(sum(x * x for x in d.values()))
sMC = math.hypot(s, 24 * Mt / v**2 * 0.5)
print(f"  C_pole = {c0:.4f} +- {s:.4f} (PDG) -> {abs(c0)/s:.0f} sigma; +MC 0.5 GeV: +- {sMC:.4f} -> {abs(c0)/sMC:.0f} sigma")
mt0 = math.sqrt((Mh**2 + 2 * MW**2 + MZ**2) / 4)
print(f"  C_pole = 0 needs m_t = {mt0:.2f} GeV")

print("(1M) MS-bar at M_t, Buttazzo fit formulas")
def msbar(mt=Mt, mh=Mh, mw=MW, a=als):
    lam = 0.12604 + 0.00206 * (mh - 125.15) - 0.00004 * (mt - 173.34)
    yt = 0.93690 + 0.00556 * (mt - 173.34) - 0.00042 * (a - 0.1184) / 0.0007
    g2 = 0.64779 + 0.00004 * (mt - 173.34) + 0.00011 * (mw - 80.384) / 0.014
    gY = 0.35830 + 0.00011 * (mt - 173.34) - 0.00020 * (mw - 80.384) / 0.014
    g3 = 1.1666 + 0.00314 * (a - 0.1184) / 0.0007 - 0.00046 * (mt - 173.34)
    return dict(lam=lam, yt=yt, g2=g2, gY=gY, g3=g3)
def Cm(c, yb=0.0156, ytau=0.0100):
    return 6 * c['lam'] + 2.25 * c['g2']**2 + 0.75 * c['gY']**2 - 6 * c['yt']**2 - 6 * yb**2 - 2 * ytau**2
c = msbar()
cm = Cm(c)
rows = []
for k, e in (('mt', eMt), ('mh', eMh), ('mw', eMW), ('a', 0.0009)):
    rows.append(abs(Cm(msbar(**{k: {'mt': Mt, 'mh': Mh, 'mw': MW, 'a': als}[k] + e})) -
                    Cm(msbar(**{k: {'mt': Mt, 'mh': Mh, 'mw': MW, 'a': als}[k] - e}))) / 2)
sm = math.sqrt(sum(r * r for r in rows) + (12 * c['yt'] * 0.0005)**2)
smw = math.sqrt(sum(r * r for r in rows) + (12 * c['yt'] * 0.003)**2 + (12 * c['yt'] * 0.00556 * 0.5)**2)
print(f"  couplings: {', '.join(f'{k}={x:.5f}' for k, x in c.items())}")
print(f"  C_MSbar = {cm:.4f} +- {sm:.4f} -> {abs(cm)/sm:.0f} sigma; wide (MC 0.5, dyt 0.003): +- {smw:.4f} -> {abs(cm)/smw:.0f} sigma")
bos = 6 * c['lam'] + 2.25 * c['g2']**2 + 0.75 * c['gY']**2
ytstar = math.sqrt((bos - 6 * 0.0156**2 - 2 * 0.01**2) / 6)
print(f"  C = 0 needs y_t(M_t) = {ytstar:.4f}, kappa_t = {ytstar/c['yt']:.3f}")
print(f"  Jegerlehner y_t = 0.9005: C = {Cm(dict(c, yt=0.9005)):.3f}")
print(f"  pole - MSbar difference = {c0 - cm:.3f} (one-loop matching, both far from 0)")

print("(6) sectors at M_t")
W = 1.5 * c['g2']**2 + 2 * c['lam']
Z = 0.75 * (c['g2']**2 + c['gY']**2) + 4 * c['lam']
F = 6 * c['yt']**2 + 6 * 0.0156**2 + 2 * 0.01**2
print(f"  W {W:.3f}  Z+h {Z:.3f}  F {F:.3f}  R = {(W+Z)/F:.3f}  3lam/6yt^2 = {3*c['lam']/(6*c['yt']**2):.3f}"
      f"  6lam/6yt^2 = {c['lam']/c['yt']**2:.3f}")

print("(3) own 1-loop RGE")
def beta(t, x):
    gp, g, g3, yt, lam = x
    k = 1 / (16 * math.pi**2)
    return [k * 41 / 6 * gp**3, k * (-19 / 6) * g**3, k * (-7) * g3**3,
            k * yt * (4.5 * yt**2 - 8 * g3**2 - 2.25 * g**2 - 17 / 12 * gp**2),
            k * (24 * lam**2 + 12 * lam * yt**2 - 6 * yt**4 - 3 * lam * (3 * g**2 + gp**2)
                 + 3 / 8 * (2 * g**4 + (g**2 + gp**2)**2))]
def run(yt0):
    x0 = [c['gY'], c['g2'], c['g3'], yt0, c['lam']]
    return solve_ivp(beta, [math.log(Mt), math.log(1e30)], x0, dense_output=True, rtol=1e-10, atol=1e-12)
def Cof(sol, l10):
    gp, g, g3, yt, lam = sol.sol(l10 * math.log(10))
    return 6 * lam + 2.25 * g**2 + 0.75 * gp**2 - 6 * yt**2
for lab, y0 in (("Buttazzo y_t", c['yt']), ("Jegerlehner y_t 0.9005", 0.9005)):
    sol = run(y0)
    grid = np.linspace(math.log10(Mt), math.log10(MPL), 2000)
    cmax = max(Cof(sol, l) for l in grid)
    l0 = brentq(lambda l: Cof(sol, l), math.log10(Mt), 29.9)
    h = 1e-3
    slope = (Cof(sol, l0 + h) - Cof(sol, l0 - h)) / (2 * h) / math.log(10)
    print(f"  [{lab}] 1-loop: max C on [M_t, M_Pl] = {cmax:+.3f}; C = 0 at 10^{l0:.2f}, dC/dln mu = {slope:+.4f}")

print("(4) H^c and twin counterfactual")
s2 = np.array([[0, -1j], [1j, 0]])
def Hc(H):
    return 1j * s2 @ H.conj()
def real8(phi):
    H = np.array([phi[0] + 1j * phi[1], phi[2] + 1j * phi[3]])
    return np.concatenate([Hc(H).real, Hc(H).imag, H.real, H.imag])
rng = np.random.default_rng(7)
phi = rng.normal(size=4)
J = np.zeros((8, 4))
for i in range(4):
    e = np.zeros(4); e[i] = 1e-6
    J[:, i] = (real8(phi + e) - real8(phi - e)) / 2e-6
H = np.array([phi[0] + 1j * phi[1], phi[2] + 1j * phi[3]])
print(f"  Jacobian rank of (H^c, H) wrt H: {np.linalg.matrix_rank(J, tol=1e-6)};"
      f" |H^c|^2-|H|^2 = {np.vdot(Hc(H), Hc(H)).real - np.vdot(H, H).real:.1e}; |H^c^dag H| = {abs(np.vdot(Hc(H), H)):.1e}")
kap, lq = -1.0, 0.3
def V(p):
    H = np.array([p[0] + 1j * p[1], p[2] + 1j * p[3]])
    n = np.vdot(H, H).real + np.vdot(Hc(H), Hc(H)).real
    return kap * n + lq * n**2
nmin = -kap / (2 * lq)  # minimum of kap n + lq n^2 in n = 2|H|^2
p0 = np.array([math.sqrt(nmin / 2), 0, 0, 0])
eps = 1e-4
Hs = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        ei = np.zeros(4); ei[i] = eps
        ej = np.zeros(4); ej[j] = eps
        Hs[i, j] = (V(p0 + ei + ej) - V(p0 + ei - ej) - V(p0 - ei + ej) + V(p0 - ei - ej)) / (4 * eps**2)
ev = np.sort(np.linalg.eigvalsh(Hs))
print(f"  H_B := H^c, kappa = {kap}: Hessian eigenvalues (complex-field normalization) = {np.round(ev, 6)};"
      f" ratio nonzero/kappa = {ev[-1]/kap:.3f}")

print("(5) CW B")
B = 3 * (2 * MW**4 + MZ**4 - 4 * Mt**4) / (64 * math.pi**2 * v**4)
print(f"  B = {B:.3e}")
print(f"  QCD EWSB: M_W = g f_pi/2 = {0.6517*92.1/2:.1f} MeV; x sqrt3 = {0.6517*92.1*math.sqrt(3)/2:.1f} MeV;"
      f" v/f_pi = {v/0.0921:.0f}; f_pi^2/v^2 = {(0.0921/v)**2:.2e}")
