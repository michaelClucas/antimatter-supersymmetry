"""Can the SM break EW symmetry radiatively? Two checks.

(A) Coleman-Weinberg / Gildener-Weinberg: set the tree mass term to zero (classically scale-invariant SM).
    One-loop V = A phi^4 + B phi^4 ln(phi^2/mu^2),  B = (1/(64 pi^2 v^4)) sum_i n_i (-1)^F m_i^4.
    A minimum at phi = v with m_h^2 = V''(v) = 8 B v^2 exists only if B > 0.
(B) MS-bar running of the mass parameter m^2 (Buttazzo convention V = -(m^2/2)|H|^2 + ...):
    beta(m^2) = m^2 * gamma(couplings), so sign(m^2) is RG invariant in a mass-independent scheme.
    Checked numerically with rg_sm.py (3-loop m^2 RGE).
"""
import math
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rg_sm import run, smi  # noqa: E402

out = []
P = lambda s: (print(s), out.append(str(s)))

# (A) symbolic: minimum condition and m_h^2 = 8 B v^2
phi, A, B, mu, v = sp.symbols('phi A B mu v', positive=True)
Vf = A * phi**4 + B * phi**4 * sp.log(phi**2 / mu**2)
Asol = sp.solve(sp.diff(Vf, phi).subs(phi, v), A)[0]
mh2 = sp.simplify(sp.diff(Vf, phi, 2).subs(phi, v).subs(A, Asol))
P(f"(A) V = A phi^4 + B phi^4 ln(phi^2/mu^2); stationary at v => A = {Asol}; V''(v) = {mh2}")
P("    -> need B > 0 for a minimum; m_h^2 = 8 B v^2.")

V = smi.V
MW, MZ, MT, MH = smi.MW, smi.MZ, smi.MT, smi.MH
S_gauge = 6 * MW**4 + 3 * MZ**4
S_top = -12 * MT**4
S_h = MH**4  # Higgs itself (Goldstones massless at the minimum)
for label, S in (("W,Z,top", S_gauge + S_top), ("W,Z,top,h", S_gauge + S_top + S_h), ("W,Z only (no top)", S_gauge)):
    Bv = S / (64 * math.pi**2 * V**4)
    m2 = 8 * Bv * V**2
    msg = f"m_h = {math.sqrt(m2):.2f} GeV" if m2 > 0 else "B < 0: stationary point is a MAXIMUM, no radiative EWSB"
    P(f"    {label:20s}: sum n m^4 = {S:+.4e} GeV^4,  B = {Bv:+.3e},  m_h^2 = {m2:+.1f} GeV^2  -> {msg}")
mt_max = ((S_gauge + S_h) / 12) ** 0.25
P(f"    top pole mass above which B<0 (with W,Z,h): {mt_max:.1f} GeV  (measured {MT})")
P("    Pure-scale-invariant SM would also need m_h ~ 10 GeV (Weinberg/Linde-type bound, W,Z only),")
P("    in conflict with m_h = 125.2 GeV even if the top were absent.")

# (B) sign of m^2 under MS-bar running
f = run(nloops=3, mu_max=1e20)
P("\n(B) MS-bar m^2(mu) (sign convention: m^2 > 0 is the broken phase):")
for x in (2.237, 5, 10, 15, 19.09, 20):
    c = f(10**x)
    P(f"    log10 mu = {x:6.2f}: m(mu) = {math.sqrt(c['m2']):.2f} GeV   (m^2 > 0)")
P("    beta(m^2) is proportional to m^2 at every loop order (eq. 100 of 1307.3536): m^2 = 0 is a fixed")
P("    point and the sign cannot change under running. In the MSSM, m_Hu^2 changes sign because its beta")
P("    function contains additive soft masses (stop/squark masses), which the SM does not have.")

with open(__file__.replace('.py', '_out.txt'), 'w') as fh:
    fh.write("\n".join(out) + "\n")
