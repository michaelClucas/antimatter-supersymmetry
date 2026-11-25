"""L04 step 2d: running-coupling supertraces in the SM, using the shared runner tools/rg_sm.py.
Loop order: 3-loop MS-bar RGEs for gauge, y_t, lambda (rg_sm.run(nloops=3)); NNLO matching at M_t
(Buttazzo et al. arXiv:1307.3536 eqs. 55-60) with PDG 2024 inputs from tools/sm_inputs.py.
A 1-loop run from the same runner is printed for comparison only.
Convention V = -m^2|H|^2/2 + lambda |H|^4, m_h^2 = 2 lambda v^2. g' = g_Y.
Quantities (dimensionless, couplings at scale mu, LANDAU GAUGE field-dependent masses):
  A_vac  = Str M^4 / v^4 at the EW vacuum (Goldstones massless): 4 l^2 + (3/16)(2g^4+(g^2+g'^2)^2) - 3 yt^4
  A_phi  = Str M^4(phi)/phi^4 at large background phi (h: 3 l phi^2, 3 Goldstones: l phi^2): 12 l^2 + (3/16)(...) - 3 yt^4
  B_vac  = Str M^2 / v^2 at vacuum: 2 l + (9g^2+3g'^2)/4 - 6 yt^2   (Pauli quadratic condition)
  B_phi  = Str M^2(phi)/phi^2 = 6 l + (3/4)(3g^2+g'^2) - 6 yt^2  = (3/v^2)(m_h^2+2M_W^2+M_Z^2-4m_t^2) (Veltman)
  b1L    = 16pi^2 dlambda/dln mu, one-loop formula evaluated on the 3-loop couplings
  bfull  = 16pi^2 dlambda/dln mu, numerical derivative of the 3-loop lambda(mu)
Run from calc/: python sm_running_supertrace.py"""
import math, os, sys
import numpy as np
import sympy as sp
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import sm_inputs as smi  # noqa: E402
import rg_sm  # noqa: E402

out = []
P = lambda *a: out.append(" ".join(str(x) for x in a))

# --- symbolic identity (Landau gauge field-dependent masses, Landau-gauge gamma_H)
l, g, gp, yt = sp.symbols('lambda g gp y_t', positive=True)
A_phi = 12*l**2 + sp.Rational(3, 16)*(2*g**4 + (g**2+gp**2)**2) - 3*yt**4
beta_l_1loop = 24*l**2 - 6*yt**4 + sp.Rational(3, 8)*(2*g**4 + (g**2+gp**2)**2) + l*(12*yt**2 - 9*g**2 - 3*gp**2)
gammaH_landau = 3*yt**2 - sp.Rational(9, 4)*g**2 - sp.Rational(3, 4)*gp**2   # 16pi^2 gamma_H, Landau gauge
P("Identity (Landau gauge): 16pi^2 beta_lambda - 4 lambda (16pi^2 gamma_H^Landau) - 2 Str M^4(phi)/phi^4 =",
  sp.simplify(beta_l_1loop - 4*l*gammaH_landau - 2*A_phi))
phi = sp.symbols('phi', positive=True)
M2 = {'h': (3*l*phi**2, 1), 'G': (l*phi**2, 3), 'W': (g**2*phi**2/4, 6), 'Z': ((g**2+gp**2)*phi**2/4, 3), 't': (yt**2*phi**2/2, -12)}
P("Str M^4(phi)/phi^4 from Landau-gauge field-dependent masses minus A_phi =",
  sp.simplify(sum(w*m2**2 for m2, w in M2.values())/phi**4 - A_phi))
P("Str M^2(phi)/phi^2 =", sp.expand(sum(w*m2 for m2, w in M2.values())/phi**2))
P("16pi^2 beta_lambda - 2 A_phi =", sp.factor(sp.simplify(beta_l_1loop - 2*A_phi)),
  " (vanishes with lambda, so A_phi and beta_lambda cross zero close together by construction)")


def quantities(c):
    lam, y, g2, gY = c['lam'], c['yt'], c['g2'], c['gY']
    G = 3/16*(2*g2**4 + (g2**2+gY**2)**2)
    b1 = 24*lam**2 - 6*y**4 + 3/8*(2*g2**4 + (g2**2+gY**2)**2) + lam*(12*y**2 - 9*g2**2 - 3*gY**2)
    return dict(lam=lam, A_vac=4*lam**2 + G - 3*y**4, A_phi=12*lam**2 + G - 3*y**4,
                B_vac=2*lam + (9*g2**2+3*gY**2)/4 - 6*y**2, B_phi=6*lam + 0.75*(3*g2**2+gY**2) - 6*y**2,
                b1L=b1, gauge=G, top=3*y**4)


MUMAX = 1e25
c0 = rg_sm.couplings_at_mt()
P(f"\nInputs at mu=M_t={smi.MT} (rg_sm.couplings_at_mt, PDG 2024): lambda={c0['lam']:.5f} yt={c0['yt']:.5f} "
  f"g2={c0['g2']:.5f} gY={math.sqrt(3/5)*c0['g1']:.5f} g3={c0['g3']:.5f}")

runs = {n: rg_sm.run(nloops=n, mu_max=MUMAX) for n in (1, 3)}


def Q(n, lmu):
    f = runs[n]
    q = quantities(f(10**lmu))
    h = 1e-3
    q['bfull'] = 16*math.pi**2*(f(10**(lmu+h))['lam'] - f(10**(lmu-h))['lam'])/(2*h*math.log(10))
    return q


def zero(n, key, lo=math.log10(smi.MT)+0.01, hi=math.log10(MUMAX)-0.01):
    xs = np.linspace(lo, hi, 600); v = [Q(n, x)[key] for x in xs]
    for i in range(len(xs)-1):
        if v[i]*v[i+1] < 0:
            return brentq(lambda x: Q(n, x)[key], xs[i], xs[i+1], xtol=1e-6)
    return None


P("\n3-loop running (rg_sm.run(nloops=3)):")
P(" log10(mu)   lambda     A_vac      A_phi      B_vac      B_phi(Veltman)  16pi^2 b_lam(full)")
for e in [math.log10(smi.MT), 3, 5, 8, 10, 12, 14, 16, 17, 18, 19, 20, 22, 23, 24]:
    q = Q(3, e)
    P(f" {e:7.2f}  {q['lam']:+.5f}  {q['A_vac']:+.5f}  {q['A_phi']:+.5f}  {q['B_vac']:+.5f}  {q['B_phi']:+.5f}       {q['bfull']:+.5f}")
P(f"\nA_vac(M_t) v^4 = {Q(3, math.log10(smi.MT))['A_vac']*smi.V**4:.3e} GeV^4 (MS-bar couplings at M_t)")
P(f"\nZero crossings, log10(mu/GeV)   [3-loop]   [1-loop, same runner, comparison only]")
for key, lab in [('lam', 'lambda'), ('bfull', 'beta_lambda (full 3-loop)'), ('b1L', 'beta_lambda (1-loop formula)'),
                 ('A_phi', 'A_phi = Str M^4(phi)/phi^4'), ('A_vac', 'A_vac = Str M^4/v^4'),
                 ('B_vac', 'B_vac = Str M^2/v^2'), ('B_phi', 'B_phi (Veltman)')]:
    z3, z1 = zero(3, key), zero(1, key)
    f = lambda z: f"{z:6.2f}" if z is not None else "  none"
    P(f"  {lab:32s} {f(z3)}     {f(z1)}")

P("\nm_t sensitivity of the Veltman zero (3-loop running, one-loop Veltman combination B_phi):")
for mt in [smi.MT - 0.29, smi.MT, smi.MT + 0.29, 173.0, 173.34]:
    f = rg_sm.run(nloops=3, mu_max=1e30, Mt=mt)
    xs = np.linspace(math.log10(mt)+0.01, 29.9, 600)
    v = [quantities(f(10**x))['B_phi'] for x in xs]
    z = None
    for i in range(len(xs)-1):
        if v[i]*v[i+1] < 0:
            z = brentq(lambda x: quantities(f(10**x))['B_phi'], xs[i], xs[i+1]); break
    P(f"  m_t = {mt:.2f} GeV: B_phi = 0 at log10(mu) = " + (f"{z:.2f}" if z else "none below 1e30"))
P("Literature: Hamada-Kawai-Oda (arXiv:1210.2538) bare-mass coefficient zero ~1e23 GeV at M_t = 173 GeV (2-loop);")
P("Jegerlehner (arXiv:1304.7813) reports a much lower crossing with different matching. Scale is scheme/m_t sensitive.")
txt = "\n".join(out); print(txt)
open(os.path.join(HERE, 'sm_running_supertrace_out.txt'), 'w').write(txt + "\n")
