"""L05: what the map Phi does to the running.  Two-loop gauge RGEs with one-loop Yukawa running (t, b, tau),
from M_Z, inputs from tools/sm_inputs.py (PDG 2024).  y_t, y_b, y_tau at M_Z obtained by running
tools/rg_sm.py (Buttazzo et al. matching at M_t) down to M_Z at 2 loops.

Models
  SM          : SM b_i, b_ij, c_i^f (exact values asserted in beta_map.py)
  Phi(SM)@M_S : SM below M_S, Phi(SM) (= MSSM content) above, couplings continuous at M_S
                (no threshold corrections, MS-bar -> DR-bar shift ignored: [approx], O(0.1) in alpha^-1).
                tan(beta) = 10 for the Yukawa matching at M_S (affects gauge running only at 2 loops via c_i^f).
Outputs: pairwise crossing scales, minimal spread of alpha_i^-1 above 10^10 GeV, and the alpha_s(M_Z) for which
alpha_3 passes exactly through the alpha_1 = alpha_2 crossing.  Also one-loop alpha_s predicted from B for each
partial map of beta_map.py section 4.
"""
import math
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

TOOLS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools")
sys.path.insert(0, os.path.abspath(TOOLS))
import sm_inputs as smi  # noqa: E402
import rg_sm  # noqa: E402

K = 1 / (16 * math.pi**2)
SM = dict(b=np.array([41 / 10, -19 / 6, -7]),
          bij=np.array([[199 / 50, 27 / 10, 44 / 5], [9 / 10, 35 / 6, 12], [11 / 10, 9 / 2, -26]]),
          c=np.array([[17 / 10, 3 / 2, 2], [1 / 2, 3 / 2, 2], [3 / 2, 1 / 2, 0]]))  # rows t, b, tau
PHI = dict(b=np.array([33 / 5, 1, -3]),
           bij=np.array([[199 / 25, 27 / 5, 88 / 5], [9 / 5, 25, 24], [11 / 5, 9, 14]]),
           c=np.array([[26 / 5, 6, 4], [14 / 5, 6, 4], [18 / 5, 2, 0]]))


def yuk_beta(model, g2, y2):
    """One-loop d y_f^2 / d ln mu (y2 = squares)."""
    G1, G2, G3 = g2
    t, b, ta = y2
    if model == "SM":
        bt = t * (9 / 2 * t + 3 / 2 * b + ta - 8 * G3 - 9 / 4 * G2 - 17 / 20 * G1)
        bb = b * (3 / 2 * t + 9 / 2 * b + ta - 8 * G3 - 9 / 4 * G2 - 1 / 4 * G1)
        bta = ta * (3 * t + 3 * b + 5 / 2 * ta - 9 / 4 * G2 - 9 / 4 * G1)
    else:
        bt = t * (6 * t + b - 16 / 3 * G3 - 3 * G2 - 13 / 15 * G1)
        bb = b * (t + 6 * b + ta - 16 / 3 * G3 - 3 * G2 - 7 / 15 * G1)
        bta = ta * (3 * b + 4 * ta - 3 * G2 - 9 / 5 * G1)
    return 2 * K * np.array([bt, bb, bta])  # d y^2/dlnmu = 2 y dy/dlnmu, and dy/dlnmu = K y (...)/2? see note


# note: standard form 16pi^2 dy/dlnmu = y (...)  =>  d y^2/dlnmu = 2 K y^2 (...)  -> matches above.


def rhs(lnmu, s, ms, loops):
    g2 = s[:3]
    y2 = s[3:]
    model = PHI if (ms is not None and lnmu > math.log(ms)) else SM
    name = "PHI" if model is PHI else "SM"
    out = np.zeros(6)
    for i in range(3):
        d = K * model["b"][i]
        if loops >= 2:
            d += K**2 * (model["bij"][i] @ g2 - model["c"][:, i] @ y2)
        out[i] = 2 * g2[i]**2 * d  # d g^2/dlnmu = 2 g^2 (g^2 [...])
    out[3:] = yuk_beta(name, g2, y2)
    return out


def yukawas_mz():
    at = rg_sm.run(nloops=2, mu_max=smi.MZ)
    c = at(smi.MZ)
    return c["yt"], c["yb"], c["ytau"]


YMZ = yukawas_mz()


def run(as_mz=smi.ALPHA_S_MZ, ms=None, loops=2, tanb=10.0, mu_max=1e19):
    a1, a2, _ = smi.gauge_couplings_mz()
    g2 = [4 * math.pi * a1, 4 * math.pi * a2, 4 * math.pi * as_mz]
    yt, yb, yta = YMZ
    s0 = np.array(g2 + [yt**2, yb**2, yta**2])
    t0, t1 = math.log(smi.MZ), math.log(mu_max)
    if ms is None or ms <= smi.MZ * 1.0000001:
        if ms is not None:  # Phi(SM) from M_Z: convert Yukawas at M_Z
            sb, cb = tanb / math.sqrt(1 + tanb**2), 1 / math.sqrt(1 + tanb**2)
            s0[3] /= sb**2
            s0[4] /= cb**2
            s0[5] /= cb**2
            ms = smi.MZ * 0.999999
        sol = solve_ivp(rhs, (t0, t1), s0, args=(ms, loops), dense_output=True, rtol=1e-9, atol=1e-12)
        return sol.sol
    # two stages with Yukawa matching at M_S
    s1 = solve_ivp(rhs, (t0, math.log(ms)), s0, args=(None, loops), rtol=1e-9, atol=1e-12).y[:, -1]
    sb, cb = tanb / math.sqrt(1 + tanb**2), 1 / math.sqrt(1 + tanb**2)
    s1[3] /= sb**2
    s1[4] /= cb**2
    s1[5] /= cb**2
    sol2 = solve_ivp(rhs, (math.log(ms), t1), s1, args=(ms * 0.999999, loops), dense_output=True,
                     rtol=1e-9, atol=1e-12)
    lo = solve_ivp(rhs, (t0, math.log(ms)), s0, args=(None, loops), dense_output=True, rtol=1e-9, atol=1e-12)

    def f(t):
        t = np.atleast_1d(t)
        return np.where(t <= math.log(ms), lo.sol(np.minimum(t, math.log(ms))), sol2.sol(np.maximum(t, math.log(ms))))
    return f


def ainv(sol, lmu10):
    t = np.asarray(lmu10) * math.log(10)
    s = sol(t)
    return 4 * math.pi / s[:3]


def analyse(**kw):
    sol = run(**kw)
    l = np.linspace(math.log10(smi.MZ), 19, 6000)
    a = ainv(sol, l)
    res = {}
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        d = a[i] - a[j]
        k = np.where(np.sign(d[:-1]) != np.sign(d[1:]))[0]
        res[(i, j)] = None if len(k) == 0 else (l[k[0]], a[i][k[0]])
    sel = l > 10
    sp = (a.max(0) - a.min(0))
    k = np.argmin(np.where(sel, sp, np.inf))
    res["best"] = (l[k], sp[k], a[:, k].mean())
    return res, l, a


def dA3(as_mz, **kw):
    res, l, a = analyse(as_mz=as_mz, **kw)
    if res[(0, 1)] is None:
        return float("nan")
    l12, a12 = res[(0, 1)]
    return np.interp(l12, l, a[2]) - a12


def fmt(res):
    s = []
    for k, n in (((0, 1), "M12"), ((0, 2), "M13"), ((1, 2), "M23")):
        s.append(f"{n}=10^{res[k][0]:.2f}" if res[k] else f"{n}=none")
    lb, sp, mean = res["best"]
    s.append(f"min spread {sp:.2f} at 10^{lb:.2f} (mean a^-1 {mean:.2f})")
    return "  ".join(s)


if __name__ == "__main__":
    a1, a2, a3 = smi.gauge_couplings_mz()
    A = [1 / a1, 1 / a2, 1 / a3]
    print(f"alpha^-1(MZ) = {A[0]:.3f}, {A[1]:.3f}, {A[2]:.3f};  y_t, y_b, y_tau (MZ) = "
          + ", ".join(f"{y:.4f}" for y in YMZ))
    Bdata = (A[1] - A[2]) / (A[0] - A[1])
    print(f"B required by data at one loop, (a2^-1 - a3^-1)/(a1^-1 - a2^-1) at MZ = {Bdata:.4f}")
    print("\nOne-loop alpha_s(MZ) predicted by exact unification for each B (all fields at MZ):")
    for name, B in (("SM", 115 / 218), ("gauge->vector only", 95 / 178), ("H^c promoted only", 5 / 9),
                    ("H->chiral only", 125 / 214), ("H,H^c chiral, no gaugino", 35 / 52),
                    ("full Phi(SM)", 5 / 7)):
        a3inv = A[1] - B * (A[0] - A[1])
        print(f"   {name:28s} B={B:.4f}  alpha_s = {1 / a3inv:.4f}")
    print("\nTwo-loop gauge + one-loop Yukawa running from MZ:")
    cases = [("SM", None), ("Phi(SM) from M_Z", smi.MZ), ("Phi(SM) from 1 TeV", 1e3), ("Phi(SM) from 3 TeV", 3e3),
             ("Phi(SM) from 10 TeV", 1e4)]
    for name, ms in cases:
        for loops in (1, 2):
            res, _, _ = analyse(ms=ms, loops=loops)
            print(f"  {name:22s} {loops}-loop: {fmt(res)}")
        lo, hi = (0.05, 0.16)
        try:
            asp = brentq(lambda x: dA3(x, ms=ms, loops=2), lo, hi, xtol=1e-6)
            print(f"  {'':22s} alpha_s(MZ) for exact unification (2-loop): {asp:.4f}  (measured 0.1180 +- 0.0009)")
        except ValueError as e:
            print("   brentq failed:", e)
    # sample table for plotting / record
    print("\nalpha_i^-1 at selected scales (2-loop):")
    for name, ms in (("SM", None), ("Phi(SM)@1TeV", 1e3)):
        sol = run(ms=ms, loops=2)
        for lm in (2, 4, 8, 12, 14, 16, 17):
            v = ainv(sol, [lm])[:, 0]
            print(f"  {name:14s} 10^{lm:<2d} GeV: {v[0]:7.2f} {v[1]:7.2f} {v[2]:7.2f}")
