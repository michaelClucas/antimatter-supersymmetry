"""Cross-check this line's runner (rg_sm3.py) against the shared runner tools/rg_sm.py (CONSTRAINTS D).
Same inputs: Buttazzo et al. 1307.3536 NNLO fits at mu = M_t with PDG-2024 values from tools/sm_inputs.py.
Differences expected: tools/rg_sm.py keeps y_b, y_tau (2 loops) and the m^2 equation; rg_sm3.py sets y_b = y_tau = 0.
"""
import math
import numpy as np
import sm_path  # noqa: F401
import rg_sm as tools_rg
from rg_sm3 import inputs_buttazzo_at_mt, run, alpha_inv

mu0, x0 = inputs_buttazzo_at_mt()
scales = [1e10, 10 ** 13.05, 10 ** 14.25, 10 ** 16.47, 1.2209e19]
worst = 0.0
for loops in (1, 2, 3):
    f_tools = tools_rg.run(nloops=loops, mu_max=2e19)
    print(f"{loops}-loop:")
    for mu in scales:
        _, y = run(x0, mu0, mu, loops=loops, npts=3)
        a_line = alpha_inv(y[:, -1:])[:, 0]
        c = f_tools(mu)
        a_tools = np.array([4 * math.pi / c[k] ** 2 for k in ("g1", "g2", "g3")])
        d = a_line - a_tools
        worst = max(worst, np.abs(d).max())
        print(f"  mu=10^{math.log10(mu):5.2f}: line {a_line.round(4)}  tools {a_tools.round(4)}  diff {np.abs(d).max():.1e}")
print(f"max |Delta alpha^-1| = {worst:.1e}  (non-unification gap is 3.2; y_b, y_tau omitted in rg_sm3.py)")
