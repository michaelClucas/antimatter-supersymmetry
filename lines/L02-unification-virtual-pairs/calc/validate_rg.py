"""Validate rg_sm3.py against Buttazzo et al. arXiv:1307.3536 eq. (61): couplings at M_Pl with their central inputs
(Mt=173.34, Mh=125.15, alpha_s=0.1184, MW=80.384). Published: g1=0.6154 g2=0.5055 g3=0.4873 yt=0.3825 lam=-0.0143."""
import numpy as np
from rg_sm3 import inputs_buttazzo_at_mt, run
mu0, x0 = inputs_buttazzo_at_mt(173.34, 125.15, 0.1184, 80.384)
pub = dict(g1=0.6154, g2=0.5055, g3=0.4873, yt=0.3825, lam=-0.0143)
for MPl in (1.2209e19, 2.435e18):
    for loops, q4 in ((1, False), (2, False), (3, False), (3, True)):
        mu, y = run(x0, mu0, MPl, loops=loops, qcd4=q4, npts=3)
        g = np.sqrt(y[:4, -1])
        print(f"MPl={MPl:.3e} loops={loops} qcd4={q4}: g1={g[0]:.4f} g2={g[1]:.4f} g3={g[2]:.4f} yt={g[3]:.4f} lam={y[4,-1]:.4f}")
print("published (61):", pub)
