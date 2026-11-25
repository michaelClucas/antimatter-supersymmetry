"""Order-of-magnitude proton lifetime if a gauge-mediated d=6 operator sat at the crossing scales.
tau ~ M_X^4 / (alpha_G^2 m_p^5) (dimensional estimate; hadronic matrix elements, renormalisation factors and
flavour factors move this by O(1-10)). Super-K bound tau(p->e+pi0) > 2.4e34 yr (CONSTRAINTS F1).
NB: in the SM-only setting there is NO X boson; these numbers only show what a unification scale would imply.
"""
import math
mp = 0.938272
hbar_s = 6.582119569e-25  # GeV s
yr = 3.15576e7
from unification import analyse  # scales computed live (inputs from tools/sm_inputs.py), not hard-coded
o = analyse("SM", 3, "A")
m = analyse("MSSM", 2, "A", msusy=2000.0)
cases = [("SM 3-loop M12", 10 ** o["M12"][0], o["M12"][1]), ("SM 3-loop M13 (best point)", 10 ** o["M13"][0], o["M13"][1]),
         ("SM 3-loop M23", 10 ** o["M23"][0], o["M23"][1]), ("MSSM 2-loop Ms=2TeV (reference)", 10 ** m["best"][0], m["best"][2])]
for lab, M, ainv in cases:
    tau = M ** 4 * ainv ** 2 / mp ** 5 * hbar_s / yr
    print(f"{lab:35s}: M={M:.2e} GeV, alpha^-1={ainv:.1f} -> tau ~ {tau:.1e} yr  ({'excluded' if tau < 2.4e34 else 'allowed'} vs 2.4e34 yr)")
# scale needed
ainv = 42.0
Mmin = (2.4e34 * yr / hbar_s * mp ** 5 / ainv ** 2) ** 0.25
print(f"minimal M_X for tau > 2.4e34 yr with alpha^-1=42: {Mmin:.1e} GeV")
