"""L04 step 2b/3: running-coupling supertraces in the SM (one-loop RGEs, top Yukawa only).
Convention V = -m^2|H|^2/2 + lambda |H|^4, m_h^2 = 2 lambda v^2 (Buttazzo et al. arXiv:1307.3536).
Quantities (dimensionless, couplings at scale mu):
  A_vac  = Str M^4 / v^4 at the EW vacuum (Goldstones massless): 4 l^2 + (3/16)(2g^4+(g^2+g'^2)^2) - 3 yt^4
  A_phi  = Str M^4(phi)/phi^4 at large background phi (h: 3 l phi^2, 3 Goldstones: l phi^2): 12 l^2 + (3/16)(...) - 3 yt^4
  B_vac  = Str M^2 / v^2 at vacuum: 2 l + (9g^2+3g'^2)/4 - 6 yt^2   (Pauli quadratic condition)
  B_phi  = Str M^2(phi)/phi^2 = 6 l + (3/4)(3g^2+g'^2) - 6 yt^2  = (3/v^2)(m_h^2+2M_W^2+M_Z^2-4m_t^2) (Veltman)
Run: python sm_running_supertrace.py"""
import math, os
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

out = []
P = lambda *a: out.append(" ".join(str(x) for x in a))

# --- symbolic identity: one-loop beta_lambda (without anomalous-dimension part) = 2 * A_phi
l, g, gp, yt = sp.symbols('lambda g gp y_t', positive=True)
A_phi = 12*l**2 + sp.Rational(3, 16)*(2*g**4 + (g**2+gp**2)**2) - 3*yt**4
beta_l_nonanom = 24*l**2 - 6*yt**4 + sp.Rational(3, 8)*(2*g**4 + (g**2+gp**2)**2)
P("Identity check 16pi^2 beta_lambda|_(no gamma) - 2 Str M^4(phi)/phi^4 =", sp.simplify(beta_l_nonanom - 2*A_phi))
# and field-dependent masses -> A_phi
phi = sp.symbols('phi', positive=True)
M2 = {'h': (3*l*phi**2, 1), 'G': (l*phi**2, 3), 'W': (g**2*phi**2/4, 6), 'Z': ((g**2+gp**2)*phi**2/4, 3), 't': (yt**2*phi**2/2, -12)}
P("Str M^4(phi)/phi^4 from field-dependent masses minus A_phi =",
  sp.simplify(sum(w*m2**2 for m2, w in M2.values())/phi**4 - A_phi))
P("Str M^2(phi)/phi^2 =", sp.expand(sum(w*m2 for m2, w in M2.values())/phi**2))

# --- inputs at mu = M_t: Buttazzo et al. fits (eqs. 55-60 of 1307.3536) shifted to PDG 2024 inputs
Mt, Mh, a3, MW = 172.57, 125.20, 0.1180, 80.369
lam0 = 0.12604 + 0.00206*(Mh-125.15) - 0.00004*(Mt-173.34)
yt0 = 0.93690 + 0.00556*(Mt-173.34) - 0.00042*(a3-0.1184)/0.0007
g20 = 0.64779 + 0.00004*(Mt-173.34) + 0.00011*(MW-80.384)/0.014
gY0 = 0.35830 + 0.00011*(Mt-173.34) - 0.00020*(MW-80.384)/0.014
g30 = 1.1666 + 0.00314*(a3-0.1184)/0.0007 - 0.00046*(Mt-173.34)
P(f"\nInputs at mu=M_t: lambda={lam0:.5f} yt={yt0:.5f} g2={g20:.5f} gY={gY0:.5f} g3={g30:.5f}")

k = 1/(16*math.pi**2)
def rge(t, y):
    gY, g2, g3, yt, lam = y
    return [k*41/6*gY**3, -k*19/6*g2**3, -k*7*g3**3,
            k*yt*(4.5*yt**2 - 8*g3**2 - 2.25*g2**2 - 17/12*gY**2),
            k*(24*lam**2 - 6*yt**4 + 3/8*(2*g2**4 + (g2**2+gY**2)**2) + lam*(12*yt**2 - 9*g2**2 - 3*gY**2))]

t0, t1 = math.log(Mt), math.log(1e20)
sol = solve_ivp(rge, (t0, t1), [gY0, g20, g30, yt0, lam0], dense_output=True, rtol=1e-10, atol=1e-12)
def Q(t):
    gY, g2, g3, yt, lam = sol.sol(t)
    G = 3/16*(2*g2**4 + (g2**2+gY**2)**2)
    return dict(lam=lam, A_vac=4*lam**2 + G - 3*yt**4, A_phi=12*lam**2 + G - 3*yt**4,
                B_vac=2*lam + (9*g2**2+3*gY**2)/4 - 6*yt**2, B_phi=6*lam + 0.75*(3*g2**2+gY**2) - 6*yt**2,
                gauge=G, top=3*yt**4)
P("\n log10(mu)   lambda     A_vac      A_phi      B_vac      B_phi(Veltman)   gauge-part  3yt^4")
for e in [math.log10(Mt), 3, 5, 8, 10, 12, 14, 16, 17, 18, 19, 20]:
    q = Q(e*math.log(10))
    P(f" {e:7.2f}  {q['lam']:+.5f}  {q['A_vac']:+.5f}  {q['A_phi']:+.5f}  {q['B_vac']:+.5f}  {q['B_phi']:+.5f}        {q['gauge']:.5f}   {q['top']:.5f}")
def zero(key):
    ts = np.linspace(t0, t1, 4000); v = [Q(t)[key] for t in ts]
    for i in range(len(ts)-1):
        if v[i]*v[i+1] < 0:
            return math.exp(brentq(lambda t: Q(t)[key], ts[i], ts[i+1]))
    return None
for key in ['lam', 'A_vac', 'A_phi', 'B_vac', 'B_phi']:
    z = zero(key)
    P(f"zero crossing of {key:6s}: " + (f"mu = {z:.3e} GeV" if z else "none below 1e20 GeV"))
P("\nCalibration: Buttazzo et al. (3-loop RGE, 2-loop matching) find lambda=0 at ~1e10 GeV and beta_lambda=0 at ~1e17-1e18 GeV;")
P("the one-loop numbers above are only indicative of where these crossings sit.")
txt = "\n".join(out); print(txt)
open(os.path.join(os.path.dirname(__file__), 'sm_running_supertrace_out.txt'), 'w').write(txt + "\n")
