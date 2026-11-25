"""SM renormalization-group running, 1/2/3 loops, MS-bar, plus MSSM 1/2-loop gauge running for comparison.

Variables: x = (g1^2, g2^2, g3^2, yt^2, lam), t = ln(mu^2).  g1 is SU(5)-normalized (g1^2 = 5/3 gY^2).
Higgs potential V = -m^2/2 |H|^2 + lam |H|^4  (so m_H^2 = 2 lam v^2 at tree level).
Bottom, tau and light Yukawas set to zero (their effect on gauge running enters at 2 loops with y_b^2 ~ 3e-4).

Beta functions transcribed from Buttazzo et al., JHEP 1312 (2013) 089, arXiv:1307.3536, Appendix B, eqs. (96)-(101).
The 3-loop gauge terms were cross-checked by hand against Mihaila, Salomon, Steinhauser, PRL 108 (2012) 151602,
arXiv:1201.5868, eq. (5) (1-loop, 2-loop and several 3-loop coefficients agree after the change of
normalisation alpha/pi <-> g^2/(4pi)^2; see WORK.md section 2.1).
"""
import math
import sys
import os
import numpy as np
from scipy.integrate import solve_ivp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "tools"))
import sm_inputs as smi  # noqa: E402

K = 1.0 / (16.0 * math.pi ** 2)


def beta_sm(x, loops=3, qcd4=False, weights=None):
    """d x / d ln(mu^2) for x=(g1sq,g2sq,g3sq,ytsq,lam).

    weights: optional dict for the counting-weight test (only used at 1 loop for gauge betas);
    default None = the SM.
    """
    g1, g2, g3, yt, lam = x  # these are squares except lam
    # ---- gauge ----
    b1 = 41.0 / 10
    b2 = -19.0 / 6
    b3 = -7.0
    d1 = g1 ** 2 * K * b1
    d2 = g2 ** 2 * K * b2
    d3 = g3 ** 2 * K * b3
    if loops >= 2:
        d1 += g1 ** 2 * K ** 2 * (44 / 5 * g3 + 27 / 10 * g2 + 199 / 50 * g1 - 17 / 10 * yt)
        d2 += g2 ** 2 * K ** 2 * (12 * g3 + 35 / 6 * g2 + 9 / 10 * g1 - 3 / 2 * yt)
        d3 += g3 ** 2 * K ** 2 * (-26 * g3 + 9 / 2 * g2 + 11 / 10 * g1 - 2 * yt)
    if loops >= 3:
        d1 += g1 ** 2 * K ** 3 * (
            yt * (189 / 16 * yt - 29 / 5 * g3 - 471 / 32 * g2 - 2827 / 800 * g1)
            + lam * (-9 / 5 * lam + 9 / 10 * g2 + 27 / 50 * g1)
            + 297 / 5 * g3 ** 2 + 789 / 64 * g2 ** 2 - 388613 / 24000 * g1 ** 2
            - 3 / 5 * g3 * g2 - 137 / 75 * g3 * g1 + 123 / 160 * g2 * g1)
        d2 += g2 ** 2 * K ** 3 * (
            yt * (147 / 16 * yt - 7 * g3 - 729 / 32 * g2 - 593 / 160 * g1)
            + lam * (-3 * lam + 3 / 2 * g2 + 3 / 10 * g1)
            + 81 * g3 ** 2 + 324953 / 1728 * g2 ** 2 - 5597 / 1600 * g1 ** 2
            + 39 * g3 * g2 - 1 / 5 * g3 * g1 + 873 / 160 * g2 * g1)
        d3 += g3 ** 2 * K ** 3 * (
            yt * (15 * yt - 40 * g3 - 93 / 8 * g2 - 101 / 40 * g1)
            + 65 / 2 * g3 ** 2 + 109 / 8 * g2 ** 2 - 523 / 120 * g1 ** 2
            + 21 * g3 * g2 + 77 / 15 * g3 * g1 - 3 / 40 * g2 * g1)
        if qcd4:
            d3 += g3 ** 5 * K ** 4 * (-2472.28)
    # ---- top Yukawa (squared) ----
    dy = yt * K * (9 / 2 * yt - 8 * g3 - 9 / 4 * g2 - 17 / 20 * g1)
    if loops >= 2:
        dy += yt * K ** 2 * (
            yt * (-12 * yt - 12 * lam + 36 * g3 + 225 / 16 * g2 + 393 / 80 * g1)
            + 6 * lam ** 2 - 108 * g3 ** 2 - 23 / 4 * g2 ** 2 + 1187 / 600 * g1 ** 2
            + 9 * g3 * g2 + 19 / 15 * g3 * g1 - 9 / 20 * g2 * g1)
    if loops >= 3:
        dy += yt * K ** 3 * (
            yt ** 2 * (58.6028 * yt + 198 * lam - 157 * g3 - 1593 / 16 * g2 - 2437 / 80 * g1)
            + lam * yt * (15 / 4 * lam + 16 * g3 - 135 / 2 * g2 - 127 / 10 * g1)
            + yt * (363.764 * g3 ** 2 + 16.990 * g2 ** 2 - 24.422 * g1 ** 2 + 48.370 * g3 * g2
                    + 18.074 * g3 * g1 + 34.829 * g2 * g1)
            + lam ** 2 * (-36 * lam + 45 * g2 + 9 * g1)
            + lam * (-171 / 16 * g2 ** 2 - 1089 / 400 * g1 ** 2 + 117 / 40 * g2 * g1)
            - 619.35 * g3 ** 3 + 169.829 * g2 ** 3 + 16.099 * g1 ** 3 + 73.654 * g3 ** 2 * g2
            - 15.096 * g3 ** 2 * g1 - 21.072 * g3 * g2 ** 2 - 22.319 * g3 * g1 ** 2
            - 321 / 20 * g3 * g2 * g1 - 4.743 * g2 ** 2 * g1 - 4.442 * g2 * g1 ** 2)
    # ---- Higgs quartic ----
    dl = K * (lam * (12 * lam + 6 * yt - 9 / 2 * g2 - 9 / 10 * g1) - 3 * yt ** 2
              + 9 / 16 * g2 ** 2 + 27 / 400 * g1 ** 2 + 9 / 40 * g2 * g1)
    if loops >= 2:
        dl += K ** 2 * (
            lam ** 2 * (-156 * lam - 72 * yt + 54 * g2 + 54 / 5 * g1)
            + lam * yt * (-3 / 2 * yt + 40 * g3 + 45 / 4 * g2 + 17 / 4 * g1)
            + lam * (-73 / 16 * g2 ** 2 + 1887 / 400 * g1 ** 2 + 117 / 40 * g2 * g1)
            + yt ** 2 * (15 * yt - 16 * g3 - 4 / 5 * g1)
            + yt * (-9 / 8 * g2 ** 2 - 171 / 200 * g1 ** 2 + 63 / 20 * g2 * g1)
            + 305 / 32 * g2 ** 3 - 3411 / 4000 * g1 ** 3 - 289 / 160 * g2 ** 2 * g1
            - 1677 / 800 * g2 * g1 ** 2)
    if loops >= 3:
        dl += K ** 3 * (
            lam ** 3 * (6011.35 * lam + 873 * yt - 387.452 * g2 - 77.490 * g1)
            + lam ** 2 * yt * (1768.26 * yt + 160.77 * g3 - 359.539 * g2 - 63.869 * g1)
            + lam ** 2 * (-790.28 * g2 ** 2 - 185.532 * g1 ** 2 - 316.64 * g2 * g1)
            + lam * yt ** 2 * (-223.382 * yt - 662.866 * g3 - 5.470 * g2 - 21.015 * g1)
            + lam * yt * (356.968 * g3 ** 2 - 319.664 * g2 ** 2 - 74.8599 * g1 ** 2
                          + 15.1443 * g3 * g2 + 17.454 * g3 * g1 + 5.615 * g2 * g1)
            + lam * g2 ** 2 * (-57.144 * g3 + 865.483 * g2 + 79.638 * g1)
            + lam * g1 ** 2 * (-8.381 * g3 + 61.753 * g2 + 28.168 * g1)
            + yt ** 3 * (-243.149 * yt + 250.494 * g3 + 74.138 * g2 + 33.930 * g1)
            + yt ** 2 * (-50.201 * g3 ** 2 + 15.884 * g2 ** 2 + 15.948 * g1 ** 2
                         + 13.349 * g3 * g2 + 17.570 * g3 * g1 - 70.356 * g2 * g1)
            + yt * g3 * (16.464 * g2 ** 2 + 1.016 * g1 ** 2 + 11.386 * g2 * g1)
            + yt * g2 ** 2 * (62.500 * g2 + 13.041 * g1)
            + yt * g1 ** 2 * (10.627 * g2 + 11.117 * g1)
            + g3 * (7.536 * g2 ** 3 + 0.663 * g1 ** 3 + 1.507 * g2 ** 2 * g1 + 1.105 * g2 * g1 ** 2)
            - 114.091 * g2 ** 4 - 1.508 * g1 ** 4 - 37.889 * g2 ** 3 * g1 + 6.500 * g2 ** 2 * g1 ** 2
            - 1.543 * g2 * g1 ** 3)
    return np.array([d1, d2, d3, dy, dl])


# ---------------- MSSM (comparison only, never used in a mechanism) ----------------
B_MSSM = np.array([[199 / 25, 27 / 5, 88 / 5], [9 / 5, 25, 24], [11 / 5, 9, 14]])
b_MSSM = np.array([33 / 5, 1.0, -3.0])
d_top_MSSM = np.array([26 / 5, 6.0, 4.0])


def beta_mssm(x, loops=2):
    g = np.array(x[:3])
    yt = x[3]
    dg = g ** 2 * K * b_MSSM
    if loops >= 2:
        dg = dg + g ** 2 * K ** 2 * (B_MSSM @ g - d_top_MSSM * yt)
    dy = yt * K * (6 * yt - 13 / 15 * g[0] - 3 * g[1] - 16 / 3 * g[2])
    return np.array([dg[0], dg[1], dg[2], dy, 0.0])


# ---------------- inputs ----------------
def inputs_buttazzo_at_mt(Mt=smi.MT, Mh=smi.MH, as_mz=smi.ALPHA_S_MZ, MW=smi.MW):
    """NNLO MS-bar couplings at mu = Mt from the fit formulas of arXiv:1307.3536 eqs (55),(57)-(60)."""
    g2 = 0.64779 + 0.00004 * (Mt - 173.34) + 0.00011 * (MW - 80.384) / 0.014
    gY = 0.35830 + 0.00011 * (Mt - 173.34) - 0.00020 * (MW - 80.384) / 0.014
    g3 = 1.1666 + 0.00314 * (as_mz - 0.1184) / 0.0007 - 0.00046 * (Mt - 173.34)
    yt = 0.93690 + 0.00556 * (Mt - 173.34) - 0.00042 * (as_mz - 0.1184) / 0.0007
    lam = 0.12604 + 0.00206 * (Mh - 125.15) - 0.00004 * (Mt - 173.34)
    return Mt, np.array([5 / 3 * gY ** 2, g2 ** 2, g3 ** 2, yt ** 2, lam])


def inputs_pdg_at_mz(as_mz=smi.ALPHA_S_MZ, ainv=smi.ALPHA_EM_INV_MZ, s2w=smi.SIN2W_MZ):
    """PDG MS-bar gauge couplings at MZ (tools/sm_inputs.py). Top Yukawa / lambda are given approximate
    MZ values (yt(MZ) ~ 0.967, lam(MZ) ~ 0.13); they affect gauge running only at 2-3 loops.
    Caveat: PDG alpha_hat(MZ) and alpha_s(MZ) are 5-flavour (top decoupled) quantities; running them in the
    6-flavour SM from MZ is a scheme mismatch of order (alpha/pi) ln(Mt/MZ) ~ 0.1-0.4 in alpha^-1,
    quantified in WORK.md by comparing with the Buttazzo matched input set."""
    a_em = 1 / ainv
    a2 = a_em / s2w
    aY = a_em / (1 - s2w)
    a1 = 5 / 3 * aY
    g = [4 * math.pi * a for a in (a1, a2, as_mz)]
    return smi.MZ, np.array([g[0], g[1], g[2], 0.967 ** 2, 0.13])


def run(x0, mu0, mu1, loops=3, model="SM", qcd4=False, npts=400, msusy=None):
    """Run from mu0 to mu1; return (mu array, x array [5, n]). If model=='MSSM', run SM below msusy, MSSM above
    (with MS-bar -> DR-bar conversion alpha_i^-1 -> alpha_i^-1 - C2(G_i)/(12 pi) at msusy for loops>=2)."""
    t0, t1 = math.log(mu0 ** 2), math.log(mu1 ** 2)

    def solve(f, ta, tb, xa, n):
        ts = np.linspace(ta, tb, n)
        s = solve_ivp(lambda t, y: f(y), (ta, tb), xa, t_eval=ts, rtol=1e-10, atol=1e-13, method="DOP853")
        if not s.success:
            raise RuntimeError(f"RG integration failed: {s.message}")
        return s.t, s.y

    if model == "SM":
        ts, y = solve(lambda y: beta_sm(y, loops, qcd4), t0, t1, x0, npts)
        return np.exp(ts / 2), y
    tS = math.log(msusy ** 2)
    ta, ya = solve(lambda y: beta_sm(y, min(loops, 2)), t0, tS, x0, max(npts // 4, 20))
    xs = ya[:, -1].copy()
    if loops >= 2:
        C2 = np.array([0, 2, 3])
        ainv = 4 * math.pi / xs[:3] - C2 / (12 * math.pi)
        xs[:3] = 4 * math.pi / ainv
    sinb2 = 1 - 1 / (1 + 10 ** 2)  # tan(beta) = 10 (reference choice)
    xs[3] = xs[3] / sinb2
    tb, yb = solve(lambda y: beta_mssm(y, loops), tS, t1, xs, npts)
    return np.exp(np.concatenate([ta, tb]) / 2), np.concatenate([ya, yb], axis=1)


def alpha_inv(y):
    return 4 * math.pi / y[:3]
