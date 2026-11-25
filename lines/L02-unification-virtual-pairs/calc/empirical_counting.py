"""Empirical check that each charged Dirac fermion (particle+antiparticle) is counted exactly once in vacuum polarisation.
(1) Leptonic running of alpha from 0 to MZ at one loop: Delta alpha_lep = (alpha/3pi) sum_l [ln(MZ^2/m_l^2) - 5/3].
    Literature 3-loop value: 0.031498 (Steinhauser, PLB 429 (1998) 158, hep-ph/9803313).
(2) R-ratio sigma(e+e- -> hadrons)/sigma(e+e- -> mu+mu-), which by the dispersion relation fixes the hadronic running:
    R = N_c sum_q Q_q^2 (1 + alpha_s/pi + ...). Measured R ~ 3.8-3.9 between charm and Z region (PDG R-ratio plot).
Counting antiparticles a second time would double both.
"""
import math
import sm_path  # noqa: F401
import sm_inputs as smi
alpha0 = 1 / 137.035999  # alpha(0), CODATA; not in tools/sm_inputs.py
MZ = smi.MZ
ml = {"e": 0.51099895e-3, "mu": 0.1056583755, "tau": smi.MTAU}
d = sum(alpha0 / (3 * math.pi) * (math.log(MZ ** 2 / m ** 2) - 5 / 3) for m in ml.values())
print(f"Delta alpha_lep(MZ), 1-loop, each lepton counted once : {d:.5f}   (3-loop literature 0.031498)")
print(f"  same with antileptons counted a second time          : {2*d:.5f}")
for nf, qs in ((4, [2/3, -1/3, -1/3, 2/3]), (5, [2/3, -1/3, -1/3, 2/3, -1/3])):
    R0 = 3 * sum(q * q for q in qs)
    a_s = 0.18 if nf == 4 else 0.13
    print(f"R-ratio nf={nf}: LO {R0:.3f}, with (1+alpha_s/pi) {R0*(1+a_s/math.pi):.2f};  doubled counting {2*R0*(1+a_s/math.pi):.2f}")
