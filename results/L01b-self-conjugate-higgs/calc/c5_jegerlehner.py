"""L01b cycle 5: why Jegerlehner puts the Veltman zero at ~1.4e16 GeV (arXiv:1304.7813) / ~7e16 (arXiv:1305.6652)
while this line (and HKO 1210.2538, Masina-Quiros 1308.1242) gets ~1e23 GeV.

C = 6 lam + 9/4 g^2 + 3/4 g'^2 - 6 yt^2 - 6 yb^2 - 2 ytau^2   (Buttazzo normalization V = lam |H|^4).
Jegerlehner: V = m^2/2 phi^2 + lamJ/24 phi^4 with phi = sqrt2 |H|  ->  lam = lamJ/6, and his C1 = 2 C (his eq. 29).

Inputs:
 (A) this line: Buttazzo et al. 1307.3536 NNLO matching at M_t, PDG 2024 inputs (tools/rg_sm.py).
 (B) Buttazzo matching with Jegerlehner's physical inputs (M_t = 173.5, M_H = 126, alpha_s = 0.1184, M_W = 80.385).
 (J) Jegerlehner 1304.7813 Table 1, MS-bar couplings at M_Z and at M_t (his matching: on-shell -> MS-bar
     with tadpoles included, Fleischer-Jegerlehner scheme; his column "lambda" = lamJ, cross-checked by
     reproducing his C1 column). Run with our 1/2/3-loop RGEs.
 Then: swap one coupling at a time between (J) and (B) at mu = M_t to attribute the shift.
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


def Cval(c):
    gY = c.get('gY', math.sqrt(3 / 5) * c['g1'])
    return 6 * c['lam'] + 2.25 * c['g2']**2 + 0.75 * gY**2 - 6 * c['yt']**2 - 6 * c['yb']**2 - 2 * c['ytau']**2


def zero(inputs, mu_start, nloops=3):
    f = run(nloops=nloops, mu_max=1e32, inputs=inputs, Mt=mu_start)
    g = lambda l: Cval(f(10**l))  # noqa: E731
    lo = math.log10(mu_start) + 0.01
    if g(lo) * g(31.5) > 0:
        return float('nan'), f
    return brentq(g, lo, 31.5), f


def jtable(row):
    """Jegerlehner 1304.7813 Table 1 rows: g3, g2, g1(=g'), yt, yb, ytau, lamJ, C1."""
    g3, g2, gp, yt, yb, ytau, lamJ, C1 = row
    return dict(g1=math.sqrt(5 / 3) * gp, g2=g2, g3=g3, yt=yt, yb=yb, ytau=ytau, lam=lamJ / 6, m2=1e4), C1


J_MZ = (1.2200, 0.6530, 0.3497, 0.9347, 0.0238, 0.0104, 0.8070, -6.768)
J_MT = (1.1644, 0.6496, 0.3509, 0.9002, 0.0227, 0.0104, 0.7373, -6.110)
J_MT_POLE = 173.5
MPL = 1.2209e19

P("Normalization check: Jegerlehner's C1 column vs 2*C from his own couplings")
for name, row in (("M_Z", J_MZ), ("M_t", J_MT)):
    c, C1 = jtable(row)
    P(f"  {name}: 2C = {2*Cval(c):+.3f}   his C1 = {C1:+.3f}")
P("  (M_t row: 0.06 mismatch in his table, likely rounding/typo; M_Z row exact. Both starting points run below.)")

P("\n(A) Buttazzo matching, PDG 2024 (M_t=172.57, M_h=125.20, als=0.1180):")
cA = couplings_at_mt()
P(f"  at M_t: yt={cA['yt']:.4f} lam={cA['lam']:.4f} g2={cA['g2']:.4f} g'={math.sqrt(3/5)*cA['g1']:.4f} g3={cA['g3']:.4f}")
for n in (1, 2, 3):
    P(f"  {n}-loop RGE: log10 mu0 = {zero(cA, smi.MT, n)[0]:.2f}")

P("\n(B) Buttazzo matching, Jegerlehner's physical inputs (M_t=173.5, M_H=126, als=0.1184, M_W=80.385):")
kwB = dict(Mt=173.5, Mh=126.0, als=0.1184, MW=80.385)
cB = couplings_at_mt(**kwB)
P(f"  at M_t: yt={cB['yt']:.4f} lam={cB['lam']:.4f} g2={cB['g2']:.4f} g'={math.sqrt(3/5)*cB['g1']:.4f} g3={cB['g3']:.4f}")
for n in (1, 2, 3):
    P(f"  {n}-loop RGE: log10 mu0 = {zero(cB, 173.5, n)[0]:.2f}")

P("\n(J) Jegerlehner Table 1 couplings, our RGEs (his result: mu0 = 1.4e16 -> log10 = 16.15):")
for name, row, mu in (("from M_Z", J_MZ, smi.MZ), ("from M_t", J_MT, J_MT_POLE)):
    c, _ = jtable(row)
    for n in (1, 2, 3):
        l0, f = zero(c, mu, n)
        cp = f(MPL)
        P(f"  {name}, {n}-loop: log10 mu0 = {l0:.2f};  at M_Pl yt={cp['yt']:.4f} lamJ={6*cp['lam']:.4f} "
          f"g2={cp['g2']:.4f} g'={cp['gY']:.4f}  (his: yt 0.3510, lamJ 0.1405, g2 0.5068, g' 0.4589)")

def Rval(c):
    gY = c.get('gY', math.sqrt(3 / 5) * c['g1'])
    bos = 6 * c['lam'] + 2.25 * c['g2']**2 + 0.75 * gY**2
    return bos / (bos - Cval(c))


cJt, _ = jtable(J_MT)
fJ = zero(jtable(J_MZ)[0], smi.MZ)[1]
P(f"\nR = C_bos/|C_ferm| at M_t: (A) {Rval(cA):.3f};  (J) his M_t row {Rval(cJt):.3f};  "
  f"(J) M_Z row run to 173.5 {Rval(fJ(173.5)):.3f}")

P("\nAttribution at mu = M_t = 173.5: start from (B) and replace one coupling by Jegerlehner's value (3-loop):")
cJ, _ = jtable(J_MT)
base = zero(cB, 173.5)[0]
P(f"  (B) baseline: {base:.2f}")
for keys in (['yt'], ['lam'], ['g1'], ['g2'], ['g3'], ['yt', 'lam'], ['yt', 'g1'], ['yt', 'lam', 'g1', 'g2', 'g3']):
    c = dict(cB)
    for k in keys:
        c[k] = cJ[k]
    P(f"  replace {'+'.join(keys):>16s}: log10 mu0 = {zero(c, 173.5)[0]:.2f}")
P(f"  Delta y_t(M_t) (J - B) = {cJ['yt'] - cB['yt']:+.4f};  Buttazzo slope dy_t/dM_t = 0.00556/GeV "
  f"-> equivalent Delta M_t = {(cJ['yt'] - cB['yt'])/0.00556:+.1f} GeV")

P("\nDelta y_t(M_t) needed on (A) to put mu0 at Jegerlehner's scales (3-loop):")
for target, lab in ((math.log10(1.4e16), "1.4e16 (1304.7813)"), (math.log10(7e16), "7e16 (1305.6652 text)"),
                    (math.log10(MPL), "M_Pl")):
    def h(dy, t=target):
        c = dict(cA)
        c['yt'] = cA['yt'] + dy
        return zero(c, smi.MT)[0] - t
    dy = brentq(h, -0.06, 0.0)
    P(f"  mu0 = {lab:22s}: Delta y_t = {dy:+.4f}  (y_t(M_t) = {cA['yt']+dy:.4f})")

with open(os.path.join(HERE, 'c5_jegerlehner_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
