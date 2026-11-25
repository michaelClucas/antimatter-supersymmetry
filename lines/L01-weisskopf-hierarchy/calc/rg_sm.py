"""SM MS-bar RG runner: g1 (GUT norm), g2, g3, y_t, y_b, y_tau, lambda, m^2.

Convention (Buttazzo et al., arXiv:1307.3536, "Investigating the near-criticality of the Higgs boson"):
    V = -(m^2/2)|H|^2 + lambda |H|^4,   m_h^2 = 2 lambda v^2 at tree level,  g1^2 = (5/3) g_Y^2.
Beta functions transcribed from that paper's Appendix B, eqs. (96)-(103), written for d(coupling^2)/d ln mu^2:
    gauge, lambda, y_t: up to 3 loops (g3 also has the 4-loop pure-QCD term);
    y_b, y_tau: 2 loops;  m^2: 3 loops.  3-loop terms omit y_b, y_tau (as in the source).
Initial conditions at mu = M_t (top pole mass): Buttazzo et al. eqs. (55)-(60) (NNLO matching fits),
evaluated with PDG 2024 inputs from tools/sm_inputs.py. y_b, y_tau at M_t: approximate (see below).

Usage:
    from rg_sm import run, couplings_at_mt
    sol = run(nloops=3)           # returns callable: sol(log10_mu) -> dict
"""
import math
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp

_here = os.path.dirname(os.path.abspath(__file__))
for cand in (os.path.join(_here, '..', '..', '..', 'tools'), os.path.join(_here, '..', 'tools'), _here):
    if os.path.exists(os.path.join(cand, 'sm_inputs.py')):
        sys.path.insert(0, os.path.abspath(cand))
        break
import sm_inputs as smi  # noqa: E402

L1 = 1.0 / (16 * math.pi**2)
L2, L3, L4 = L1**2, L1**3, L1**4


def couplings_at_mt(Mh=smi.MH, Mt=smi.MT, als=smi.ALPHA_S_MZ, MW=smi.MW):
    """MS-bar couplings at mu = M_t, Buttazzo et al. eqs. (55)-(60)."""
    a3 = (als - 0.1184) / 0.0007
    lam = 0.12604 + 0.00206 * (Mh - 125.15) - 0.00004 * (Mt - 173.34)
    yt = 0.93690 + 0.00556 * (Mt - 173.34) - 0.00042 * a3
    g2 = 0.64779 + 0.00004 * (Mt - 173.34) + 0.00011 * (MW - 80.384) / 0.014
    gY = 0.35830 + 0.00011 * (Mt - 173.34) - 0.00020 * (MW - 80.384) / 0.014
    g3 = 1.1666 + 0.00314 * a3 - 0.00046 * (Mt - 173.34)
    m = 131.55 + 0.94 * (Mh - 125.15) + 0.17 * (Mt - 173.34)
    v = smi.V
    # small Yukawas, rough: m_b(M_t) ~ 2.75 GeV (4-loop QCD running of m_b(m_b)=4.18), m_tau ~ 1.75 GeV.
    # Their effect on everything computed here is < 1e-3 relative.
    yb = math.sqrt(2) * 2.75 / v
    ytau = math.sqrt(2) * 1.75 / v
    return dict(g1=math.sqrt(5 / 3) * gY, g2=g2, g3=g3, yt=yt, yb=yb, ytau=ytau, lam=lam, m2=m * m)


def _beta(t, s, nloops):
    G1, G2, G3, Yt, Yb, Ytau, lam, m2 = s
    # ---- gauge, eqs (96)-(98): d g^2 / d ln mu^2
    b1 = [G1**2 * 41 / 10,
          G1**2 * (44 * G3 / 5 + 27 * G2 / 10 + 199 * G1 / 50 - 17 * Yt / 10 - Yb / 2 - 3 * Ytau / 2),
          G1**2 * (Yt * (189 * Yt / 16 - 29 * G3 / 5 - 471 * G2 / 32 - 2827 * G1 / 800)
                   + lam * (-9 * lam / 5 + 9 * G2 / 10 + 27 * G1 / 50)
                   + 297 * G3**2 / 5 + 789 * G2**2 / 64 - 388613 * G1**2 / 24000
                   - 3 * G3 * G2 / 5 - 137 * G3 * G1 / 75 + 123 * G2 * G1 / 160)]
    b2 = [G2**2 * (-19 / 6),
          G2**2 * (12 * G3 + 35 * G2 / 6 + 9 * G1 / 10 - 3 * Yt / 2 - 3 * Yb / 2 - Ytau / 2),
          G2**2 * (Yt * (147 * Yt / 16 - 7 * G3 - 729 * G2 / 32 - 593 * G1 / 160)
                   + lam * (-3 * lam + 3 * G2 / 2 + 3 * G1 / 10)
                   + 81 * G3**2 + 324953 * G2**2 / 1728 - 5597 * G1**2 / 1600
                   + 39 * G3 * G2 - G3 * G1 / 5 + 873 * G2 * G1 / 160)]
    b3 = [G3**2 * (-7),
          G3**2 * (-26 * G3 + 9 * G2 / 2 + 11 * G1 / 10 - 2 * Yt - 2 * Yb),
          G3**2 * (Yt * (15 * Yt - 40 * G3 - 93 * G2 / 8 - 101 * G1 / 40)
                   + 65 * G3**2 / 2 + 109 * G2**2 / 8 - 523 * G1**2 / 120
                   + 21 * G3 * G2 + 77 * G3 * G1 / 15 - 3 * G2 * G1 / 40)]
    # ---- lambda, eq (99): d lambda / d ln mu^2
    bl = [lam * (12 * lam + 6 * Yt + 6 * Yb + 2 * Ytau - 9 * G2 / 2 - 9 * G1 / 10)
          - 3 * Yt**2 - 3 * Yb**2 - Ytau**2 + 9 * G2**2 / 16 + 27 * G1**2 / 400 + 9 * G2 * G1 / 40,
          lam**2 * (-156 * lam - 72 * Yt - 72 * Yb - 24 * Ytau + 54 * G2 + 54 * G1 / 5)
          + lam * Yt * (-3 * Yt / 2 - 21 * Yb + 40 * G3 + 45 * G2 / 4 + 17 * G1 / 4)
          + lam * Yb * (-3 * Yb / 2 + 40 * G3 + 45 * G2 / 4 + 5 * G1 / 4)
          + lam * Ytau * (-Ytau / 2 + 15 * G2 / 4 + 15 * G1 / 4)
          + lam * (-73 * G2**2 / 16 + 1887 * G1**2 / 400 + 117 * G2 * G1 / 40)
          + Yt**2 * (15 * Yt - 3 * Yb - 16 * G3 - 4 * G1 / 5)
          + Yt * (-9 * G2**2 / 8 - 171 * G1**2 / 200 + 63 * G2 * G1 / 20)
          + Yb**2 * (-3 * Yt + 15 * Yb - 16 * G3 + 2 * G1 / 5)
          + Yb * (-9 * G2**2 / 8 + 9 * G1**2 / 40 + 27 * G2 * G1 / 20)
          + Ytau**2 * (5 * Ytau - 6 * G1 / 5)
          + Ytau * (-3 * G2**2 / 8 - 9 * G1**2 / 8 + 33 * G2 * G1 / 20)
          + 305 * G2**3 / 32 - 3411 * G1**3 / 4000 - 289 * G2**2 * G1 / 160 - 1677 * G2 * G1**2 / 800,
          lam**3 * (6011.35 * lam + 873 * Yt - 387.452 * G2 - 77.490 * G1)
          + lam**2 * Yt * (1768.26 * Yt + 160.77 * G3 - 359.539 * G2 - 63.869 * G1)
          + lam**2 * (-790.28 * G2**2 - 185.532 * G1**2 - 316.64 * G2 * G1)
          + lam * Yt**2 * (-223.382 * Yt - 662.866 * G3 - 5.470 * G2 - 21.015 * G1)
          + lam * Yt * (356.968 * G3**2 - 319.664 * G2**2 - 74.8599 * G1**2 + 15.1443 * G3 * G2
                        + 17.454 * G3 * G1 + 5.615 * G2 * G1)
          + lam * G2**2 * (-57.144 * G3 + 865.483 * G2 + 79.638 * G1)
          + lam * G1**2 * (-8.381 * G3 + 61.753 * G2 + 28.168 * G1)
          + Yt**3 * (-243.149 * Yt + 250.494 * G3 + 74.138 * G2 + 33.930 * G1)
          + Yt**2 * (-50.201 * G3**2 + 15.884 * G2**2 + 15.948 * G1**2 + 13.349 * G3 * G2
                     + 17.570 * G3 * G1 - 70.356 * G2 * G1)
          + Yt * G3 * (16.464 * G2**2 + 1.016 * G1**2 + 11.386 * G2 * G1)
          + Yt * G2**2 * (62.500 * G2 + 13.041 * G1)
          + Yt * G1**2 * (10.627 * G2 + 11.117 * G1)
          + G3 * (7.536 * G2**3 + 0.663 * G1**3 + 1.507 * G2**2 * G1 + 1.105 * G2 * G1**2)
          - 114.091 * G2**4 - 1.508 * G1**4 - 37.889 * G2**3 * G1 + 6.500 * G2**2 * G1**2
          - 1.543 * G2 * G1**3]
    # ---- m^2, eq (100), 2 loops
    bm = [m2 * (6 * lam + 3 * Yt + 3 * Yb + Ytau - 9 * G2 / 4 - 9 * G1 / 20),
          m2 * (lam * (-30 * lam - 36 * Yt - 36 * Yb - 12 * Ytau + 36 * G2 + 36 * G1 / 5)
                + Yt * (-27 * Yt / 4 - 21 * Yb / 2 + 20 * G3 + 45 * G2 / 8 + 17 * G1 / 8)
                + Yb * (-27 * Yb / 4 + 20 * G3 + 45 * G2 / 8 + 5 * G1 / 8)
                + Ytau * (-9 * Ytau / 4 + 15 * G2 / 8 + 15 * G1 / 8)
                - 145 * G2**2 / 32 + 1671 * G1**2 / 800 + 9 * G2 * G1 / 16),
          m2 * (lam**2 * (1026 * lam + 297 * Yt / 2 - 192.822 * G2 - 38.564 * G1)
                + lam * Yt * (347.394 * Yt + 80.385 * G3 - 318.591 * G2 - 59.699 * G1)
                + lam * (-64.5145 * G2**2 - 65.8056 * G1**2 - 37.8231 * G2 * G1)
                + Yt**2 * (154.405 * Yt - 209.24 * G3 - 3.82928 * G2 - 7.50769 * G1)
                + Yt * (178.484 * G3**2 - 102.627 * G2**2 - 27.721 * G1**2 + 7.572 * G3 * G2
                        + 8.727 * G3 * G1 + 11.470 * G2 * G1)
                + G2**2 * (-28.572 * G3 + 301.724 * G2 + 9.931 * G1)
                + G1**2 * (-4.191 * G3 + 9.778 * G2 + 8.378 * G1))]
    # ---- y_t^2, eq (101)
    byt = [Yt * (9 * Yt / 2 + 3 * Yb / 2 + Ytau - 8 * G3 - 9 * G2 / 4 - 17 * G1 / 20),
           Yt * (Yt * (-12 * Yt - 11 * Yb / 4 - 9 * Ytau / 4 - 12 * lam + 36 * G3 + 225 * G2 / 16 + 393 * G1 / 80)
                 + Yb * (-Yb / 4 + 5 * Ytau / 4 + 4 * G3 + 99 * G2 / 16 + 7 * G1 / 80)
                 + Ytau * (-9 * Ytau / 4 + 15 * G2 / 8 + 15 * G1 / 8)
                 + 6 * lam**2 - 108 * G3**2 - 23 * G2**2 / 4 + 1187 * G1**2 / 600
                 + 9 * G3 * G2 + 19 * G3 * G1 / 15 - 9 * G2 * G1 / 20),
           Yt * (Yt**2 * (58.6028 * Yt + 198 * lam - 157 * G3 - 1593 * G2 / 16 - 2437 * G1 / 80)
                 + lam * Yt * (15 * lam / 4 + 16 * G3 - 135 * G2 / 2 - 127 * G1 / 10)
                 + Yt * (363.764 * G3**2 + 16.990 * G2**2 - 24.422 * G1**2 + 48.370 * G3 * G2
                         + 18.074 * G3 * G1 + 34.829 * G2 * G1)
                 + lam**2 * (-36 * lam + 45 * G2 + 9 * G1)
                 + lam * (-171 * G2**2 / 16 - 1089 * G1**2 / 400 + 117 * G2 * G1 / 40)
                 - 619.35 * G3**3 + 169.829 * G2**3 + 16.099 * G1**3 + 73.654 * G3**2 * G2
                 - 15.096 * G3**2 * G1 - 21.072 * G3 * G2**2 - 22.319 * G3 * G1**2
                 - 321 / 20 * G3 * G2 * G1 - 4.743 * G2**2 * G1 - 4.442 * G2 * G1**2)]
    # ---- y_b^2, y_tau^2, eqs (102)-(103), 2 loops
    byb = [Yb * (3 * Yt / 2 + 9 * Yb / 2 + Ytau - 8 * G3 - 9 * G2 / 4 - G1 / 4),
           Yb * (Yt * (-Yt / 4 - 11 * Yb / 4 + 5 * Ytau / 4 + 4 * G3 + 99 * G2 / 16 + 91 * G1 / 80)
                 + Yb * (-12 * Yb - 9 * Ytau / 4 - 12 * lam + 36 * G3 + 225 * G2 / 16 + 237 * G1 / 80)
                 + Ytau * (-9 * Ytau / 4 + 15 * G2 / 8 + 15 * G1 / 8)
                 + 6 * lam**2 - 108 * G3**2 - 23 * G2**2 / 4 - 127 * G1**2 / 600
                 + 9 * G3 * G2 + 31 * G3 * G1 / 15 - 27 * G2 * G1 / 20),
           0.0]
    bytau = [Ytau * (3 * Yt + 3 * Yb + 5 * Ytau / 2 - 9 * G2 / 4 - 9 * G1 / 4),
             Ytau * (6 * lam**2 - 23 * G2**2 / 4 + 1371 * G1**2 / 200 + 27 * G2 * G1 / 20
                     + Yt * (-27 * Yt / 4 + 3 * Yb / 2 - 27 * Ytau / 4 + 20 * G3 + 45 * G2 / 8 + 17 * G1 / 8)
                     + Yb * (-27 * Yb / 4 - 27 * Ytau / 4 + 20 * G3 + 45 * G2 / 8 + 5 * G1 / 8)
                     + Ytau * (-3 * Ytau - 12 * lam + 165 * G2 / 16 + 537 * G1 / 80)),
             0.0]
    pref = [L1, L2, L3]
    out = []
    for b in (b1, b2, b3, byt, byb, bytau, bl, bm):
        out.append(sum(pref[i] * b[i] for i in range(nloops)))
    if nloops >= 4:
        out[2] += L4 * G3**5 * (-2472.28)
    return out


def run(nloops=3, mu_max=1e20, inputs=None, **kw):
    """Integrate from M_t up to mu_max. Returns a function f(mu) -> dict of couplings (not squared)."""
    c = inputs if inputs is not None else couplings_at_mt(**kw)
    Mt = kw.get('Mt', smi.MT)
    s0 = [c['g1']**2, c['g2']**2, c['g3']**2, c['yt']**2, c['yb']**2, c['ytau']**2, c['lam'], c['m2']]
    t0, t1 = math.log(Mt**2), math.log(mu_max**2)
    sol = solve_ivp(_beta, (t0, t1), s0, args=(nloops,), dense_output=True, rtol=1e-10, atol=1e-13,
                    method='DOP853')

    def at(mu):
        G1, G2, G3, Yt, Yb, Ytau, lam, m2 = sol.sol(math.log(mu**2))
        return dict(g1=math.sqrt(G1), g2=math.sqrt(G2), g3=math.sqrt(G3), yt=math.sqrt(Yt),
                    yb=math.sqrt(Yb), ytau=math.sqrt(Ytau), lam=lam, m2=m2,
                    gY=math.sqrt(3 / 5 * G1))
    return at


if __name__ == '__main__':
    # Validation against Buttazzo et al. eq. (61): their inputs Mt=173.34, Mh=125.15, as=0.1184, MW=80.384
    MPL = 1.2209e19
    ref = dict(g1=0.6154, g2=0.5055, g3=0.4873, yt=0.3825, lam=-0.0143)
    kw = dict(Mh=125.15, Mt=173.34, als=0.1184, MW=80.384)
    print("Validation vs Buttazzo et al. (arXiv:1307.3536) eq. (61) at M_Pl = 1.22e19 GeV")
    print("  (their result: 3-loop RGEs, NNLO thresholds; m(M_Pl) = 129.4 GeV)")
    for n in (1, 2, 3):
        f = run(nloops=n, **kw)(MPL)
        print(f"  {n}-loop: " + "  ".join(f"{k}={f[k]:.4f} (ref {ref[k]:.4f})" for k in ref)
              + f"  m={math.sqrt(f['m2']):.1f}")
