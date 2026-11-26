"""L01b cycle 5: error budget for M_t* = the top pole mass at which the one-loop Veltman coefficient C vanishes
at mu = M_Pl (Buttazzo matching, 3-loop RGEs). Answers Referee 1 (c4) finding 3b/3c.

Each source is converted to an equivalent shift of M_t* (or of the measured M_t), then combined in quadrature.
Non-computed entries are literature numbers, labelled in WORK.md:
  MC-vs-pole interpretation ~0.5 GeV (Hoang, arXiv:2004.12915), pole-mass renormalon ambiguity ~0.11 GeV
  (Beneke, Marquard, Nason, Steinhauser, arXiv:1605.03609), y_t matching theory +-0.0005 (Buttazzo et al. 1307.3536,
  [uncertain: value as transcribed]).
"""
import math
import os
import sys

from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools')))
import sm_inputs as smi  # noqa: E402
from rg_sm import run, couplings_at_mt  # noqa: E402

out = []


def P(s=""):
    print(s)
    out.append(str(s))


MPL = smi.M_PLANCK
LPL = math.log10(MPL)


def C_at(l, nloops=3, dyt=0.0, **kw):
    c = couplings_at_mt(**kw)
    c['yt'] += dyt
    f = run(nloops=nloops, mu_max=10**(l + 0.1), inputs=c, Mt=kw.get('Mt', smi.MT))(10**l)
    return 6 * f['lam'] + 2.25 * f['g2']**2 + 0.75 * f['gY']**2 - 6 * f['yt']**2 - 6 * f['yb']**2 - 2 * f['ytau']**2


def Mt_star(l=LPL, nloops=3, dyt=0.0, **kw):
    return brentq(lambda m: C_at(l, nloops, dyt, Mt=m, **kw), 160.0, 175.0, xtol=1e-4)


m0 = Mt_star()
P(f"Central: C(M_Pl) = 0 needs M_t* = {m0:.3f} GeV (3-loop RGE, Buttazzo matching, als=0.1180, M_h=125.20)")
P(f"Measured direct M_t = {smi.MT} +- 0.29 GeV; distance = {smi.MT - m0:.2f} GeV")

rows = []
d = (Mt_star(als=smi.ALPHA_S_MZ + 0.0009) - Mt_star(als=smi.ALPHA_S_MZ - 0.0009)) / 2
rows.append(("alpha_s(M_Z) +-0.0009 [computed]", abs(d)))
d = (Mt_star(Mh=smi.MH + 0.11) - Mt_star(Mh=smi.MH - 0.11)) / 2
rows.append(("M_h +-0.11 [computed]", abs(d)))
d = (Mt_star(dyt=+0.0005) - Mt_star(dyt=-0.0005)) / 2
rows.append(("y_t(M_t) matching theory +-0.0005 [lit, Buttazzo]", abs(d)))
d = Mt_star(nloops=2) - m0
rows.append(("RGE order 2-loop vs 3-loop [computed]", abs(d)))
# scheme of the Lambda^2 coefficient itself: Jegerlehner's C2 vs C1 moved his zero by log10(1.4/1.1)=0.105 dec.
# convert with the local slope d log10(mu0)/dM_t at M_t*.
dl = (math.log10(1.4e16) - math.log10(1.1e16))
slope_pts = []
for m in (m0 - 0.2, m0 + 0.2):
    slope_pts.append(brentq(lambda l, mm=m: C_at(l, Mt=mm), 17, 21))
slope = (slope_pts[1] - slope_pts[0]) / 0.4
rows.append((f"Lambda^2 coeff. 1-loop vs 2-loop (C1->C2 shift {dl:.2f} dec, slope {slope:.2f} dec/GeV) [lit+computed]",
             abs(dl / slope)))
rows.append(("MC mass vs pole mass interpretation [lit, Hoang 2004.12915]", 0.5))
rows.append(("pole-mass renormalon ambiguity [lit, Beneke et al. 1605.03609]", 0.11))
rows.append(("experimental, direct M_t (PDG 2024)", 0.29))
# curvature of y_t(M_t) beyond the linear Buttazzo fit: y_t ~ M_t * (1 - (4/3pi) als(M_t)), als running only
a = 0.108
curv = 0.93 * (4 / (3 * math.pi)) * (7 * a**2 / (2 * math.pi)) * ((m0 - 173.34) / 173.34)**2 / 2
rows.append((f"linear-fit extrapolation (curvature est. dy={curv:.1e}) [computed, crude]", curv / 0.00556))

P("\nSource                                                                    equiv. dM_t (GeV)")
for name, v in rows:
    P(f"  {name:72s} {v:6.3f}")
tot = math.sqrt(sum(v * v for _, v in rows))
P(f"  {'quadrature total':72s} {tot:6.3f}")
P(f"\nSignificance of C(M_Pl) != 0 within Buttazzo-type matching: {(smi.MT - m0)/tot:.1f} sigma "
  f"(experimental-only: {(smi.MT - m0)/0.29:.1f} sigma)")
P("Not included: the Jegerlehner matching spread (Delta y_t = -0.038 vs Buttazzo at equal inputs, ~6.8 GeV "
  "equivalent, see c5_jegerlehner_out.txt). If that matching is admitted, the condition at M_Pl is not excluded.")

with open(os.path.join(HERE, 'c5_mt_budget_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
