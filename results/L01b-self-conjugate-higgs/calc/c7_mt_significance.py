"""L01b cycle 7: significance of C(M_Pl) != 0 with the y_t-matching spread included (Referee A c6 finding 5,
Referee B c6 finding 8). Reuses the c5 budget rows (c5_mt_budget_out.txt) and adds an intermediate y_t matching
spread delta_y in place of Buttazzo's +-0.0005. The slope dy_t/dM_t is computed here.
delta_y = 0.003 is the referee's illustrative value; no published two-loop matching spread of that size was read.
Run from this directory: python c7_mt_significance.py
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools')))
import sm_inputs as smi  # noqa: E402
from rg_sm import couplings_at_mt  # noqa: E402

out = []


def P(s=""):
    print(s)
    out.append(str(s))


MT_STAR = 169.535  # c5_mt_budget_out.txt
slope = (couplings_at_mt(Mt=smi.MT + 0.5)['yt'] - couplings_at_mt(Mt=smi.MT - 0.5)['yt'])  # per GeV
P(f"dy_t(M_t)/dM_t = {slope:.5f} per GeV (Buttazzo fit)")
base = {"alpha_s": 0.418, "M_h": 0.037, "RGE order": 0.125, "Lambda^2 coeff C1->C2": 0.086,
        "MC vs pole": 0.5, "renormalon": 0.11, "experimental M_t": 0.29}
dist = smi.MT - MT_STAR
P(f"distance M_t - M_t* = {dist:.2f} GeV")
P("  delta y_t(matching)   equiv dM_t   total budget   significance")
for dy in (0.0005, 0.001, 0.002, 0.003, 0.004):
    rows = list(base.values()) + [dy / slope]
    tot = math.sqrt(sum(r * r for r in rows))
    P(f"  {dy:8.4f}             {dy/slope:6.3f}       {tot:6.3f}        {dist/tot:4.1f} sigma")
tot_x = math.sqrt(0.7**2 + 0.418**2 + 0.11**2 + 0.003**2 / slope**2)
P(f"cross-section pole mass 172.4 +- 0.7 (no MC term) with delta_y = 0.003: {(172.4-MT_STAR)/tot_x:.1f} sigma")
dJ = 0.038 / slope
P(f"Jegerlehner matching (delta_y = -0.038, {dJ:.1f} GeV equivalent): C(M_Pl) = 0 not excluded.")
P("Summary: 3.3-4.1 sigma within Buttazzo-type matching for delta_y in [0.0005, 0.003]; not excluded under Jegerlehner.")

with open(os.path.join(HERE, 'c7_mt_significance_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
