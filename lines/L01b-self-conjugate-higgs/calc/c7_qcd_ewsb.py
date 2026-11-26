"""L01b cycle 7: EWSB by the QCD quark-antiquark condensate (Referee B c6 finding 6).

<q-bar_L q_R> != 0 carries weak isospin 1/2 and hypercharge, so it breaks SU(2)_L x U(1)_Y -> U(1)_em
[established; Weinberg 1979 / Susskind 1979 technicolor template; Quigg & Shrock, PRD 79, 096002 (2009),
arXiv:0901.3958]. The pions are eaten in proportion f_pi^2 / (v^2 + n_d f_pi^2), and the gauge boson masses get
  M_W^2 = g^2 (v^2 + n_d f_pi^2)/4,   M_Z^2 = M_W^2 / cos^2(theta_W)  (custodial SU(2) of QCD),
with f_pi = 92.1 MeV normalisation (f_pi+ = 130.2/sqrt 2) and n_d = number of quark doublets whose chiral symmetry
is broken by the condensate. With the Higgs vev switched off (mu^2 >= 0, all quarks massless) n_d = 3; in the real
world only (u,d) is light, n_d ~ 1. f_pi with 6 massless flavours is not the physical f_pi; taken equal here [approx].
Run from this directory: python c7_qcd_ewsb.py
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools')))
import sm_inputs as smi  # noqa: E402

out = []


def P(s=""):
    print(s)
    out.append(str(s))


fpi = 0.1302 / math.sqrt(2)  # GeV, PDG f_pi+ = 130.2 MeV
v = smi.V
g = 2 * smi.MW / v           # on-shell-ish g at the EW scale
cw = smi.MW / smi.MZ
P(f"f_pi = {fpi*1e3:.1f} MeV, g = 2M_W/v = {g:.4f}, cos(theta_W) = M_W/M_Z = {cw:.4f}")
for nd, lab in ((1, "one light doublet (u,d)"), (3, "Higgs off: all 3 quark doublets massless")):
    MW = g * math.sqrt(nd) * fpi / 2
    P(f"  {lab:42s}: M_W = g sqrt(n_d) f_pi/2 = {MW*1e3:5.1f} MeV, M_Z = {MW/cw*1e3:5.1f} MeV")
P(f"Real SM: QCD share of v^2 = f_pi^2/v^2 = {fpi**2/v**2:.2e}; shift of M_W = {smi.MW*(math.sqrt(1+fpi**2/v**2)-1)*1e6:.1f} keV")
P(f"Required for observed EWSB: M_W = {smi.MW} GeV, i.e. a condensate scale ~ v = {v:.1f} GeV, {v/fpi:.0f} x f_pi.")
P("This is the SM's own antimatter-condensate (q q-bar) EWSB mechanism. It exists, but at the QCD scale.")

with open(os.path.join(HERE, 'c7_qcd_ewsb_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
