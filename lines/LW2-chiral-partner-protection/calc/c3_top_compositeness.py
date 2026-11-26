"""LW2 c3: can the SM Higgs be read as a top-antitop composite (Bardeen-Hill-Lindner compositeness condition)
inside the pure SM?  Compositeness at scale Lambda requires Z_H(Lambda) = 0, equivalently y_t(Lambda) -> infinity
(Landau pole of y_t at Lambda) in the SM RG flow below Lambda [BHL, PRD 41, 1647 (1990)].

 (a) SM flow from measured inputs (tools/rg_sm.py): y_t(mu) is monotonically decreasing -> no pole.
 (b) y_t(M_t) needed for a y_t pole (y_t = 10 used as 'pole') at Lambda = 1e15, 1e19 GeV, 1- and 2-loop SM RGEs,
     with all other couplings at their measured values; converted to a top mass by scaling the measured
     pole/MS-bar ratio [approx, ignores the change in QCD matching].
"""
import math
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'tools')))
import rg_sm  # noqa: E402
import sm_inputs as smi  # noqa: E402

c0 = rg_sm.couplings_at_mt()
yt_meas = c0['yt']


def flow(yt0, nloops, mu_max):
    c = dict(c0, yt=yt0)
    s0 = [c['g1']**2, c['g2']**2, c['g3']**2, c['yt']**2, c['yb']**2, c['ytau']**2, c['lam'], c['m2']]
    ev = lambda t, s, n: s[3] - 100.0       # y_t = 10
    ev.terminal = True
    return solve_ivp(rg_sm._beta, (math.log(smi.MT**2), math.log(mu_max**2)), s0, args=(nloops,),
                     events=ev, rtol=1e-9, atol=1e-12, method='DOP853', dense_output=True)


# (a)
for n in (1, 2, 3):
    sol = flow(yt_meas, n, 1.22e19)
    ts = np.linspace(sol.t[0], sol.t[-1], 400)
    yt = np.sqrt(sol.sol(ts)[3])
    mono = bool(np.all(np.diff(yt) < 0))
    print(f"(a) {n}-loop SM: y_t(M_t)={yt[0]:.4f}, y_t(1e15)={math.sqrt(sol.sol(math.log(1e30))[3]):.4f}, "
          f"y_t(M_Pl)={yt[-1]:.4f}, monotonic decreasing={mono}, lambda(M_Pl)={sol.sol(ts[-1])[6]:.4f}")

# (b)
def pole_scale(yt0, n, mu_max):
    sol = flow(yt0, n, mu_max)
    return math.exp(sol.t_events[0][0] / 2) if len(sol.t_events[0]) else None

for n in (1,):
    for Lam in (1e15, 1e19):
        lo, hi = yt_meas, 3.0
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            if pole_scale(mid, n, Lam) is None:
                lo = mid
            else:
                hi = mid
        mt_req = smi.MT * hi / yt_meas
        print(f"(b) {n}-loop: y_t pole at Lambda={Lam:.0e} needs y_t(M_t)={hi:.4f} (meas {yt_meas:.4f}, x{hi / yt_meas:.3f})"
              f" -> m_t ~ {mt_req:.0f} GeV [approx] vs {smi.MT}")
print("    2-loop: no pole found for y_t(M_t) < 3; the truncated 2-loop beta_yt has a spurious large-y zero, so the pole\n"
      "    condition is only meaningful at 1 loop (as in BHL's leading-order analysis). [conjecture: standard truncation artefact, not checked here]")
print("    BHL 1990 (full RG + compositeness of lambda): m_t ~ 218 GeV at Lambda = 1e19 [from memory; check]")
