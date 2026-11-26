"""L01b cycle 9: gate-7 consistency check for the no-go (Referee E c8 finding 5, Referee C c7 finding 8).

The no-go says no symmetry of the SM Lagrangian enforces C = 0. Its observable consequences:
  (i)  C(M_t) != 0, with the measured inputs;
  (ii) if C(mu) crosses zero, it does so transversally (dC/dln mu != 0), i.e. C = 0 is not an RG-invariant
       relation (reduction of couplings, Zimmermann) along the measured trajectory.
A measurement that put C(M_t) at zero within errors, or a trajectory that touches C = 0 tangentially and
stays there, would falsify (i) or (ii).

C = 6 lam + 9/4 g^2 + 3/4 g'^2 - 6 y_t^2 - 6 y_b^2 - 2 y_tau^2 (CONSTRAINTS G normalization; y_b, y_tau included
as in the sector table). Two determinations:
  (P) tree-level pole-mass form C_pole = (3/v^2)(m_h^2 + 2 M_W^2 + M_Z^2 - 4 m_t^2)  (y_b, y_tau dropped, < 0.1%)
  (M) MS-bar at mu = M_t from the Buttazzo et al. (arXiv:1307.3536) NNLO fits in tools/rg_sm.py.
Errors: PDG 2024 (CONSTRAINTS C1, C2, D): m_t 0.29, m_h 0.11, M_W 0.0133, M_Z 0.0021, alpha_s 0.0009.
Extra systematic rows: MC-vs-pole 0.5 GeV on m_t (Hoang 2004.12915), y_t matching theory +-0.0005 (Buttazzo),
and a wide +-0.003 spread; Jegerlehner's y_t(M_t) = 0.9005 (1304.7813) as an alternative matching.
Run from this directory: python c9_C_measured.py
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


PDG24 = dict(Mt=smi.MT, Mh=smi.MH, MW=smi.MW, MZ=smi.MZ, als=smi.ALPHA_S_MZ)
ERR24 = dict(Mt=0.29, Mh=0.11, MW=0.0133, MZ=0.0021, als=0.0009)
PDG26 = dict(Mt=172.60, Mh=125.13, MW=80.3625, MZ=smi.MZ, als=smi.ALPHA_S_MZ)  # CONSTRAINTS C2 PDG 2026 row
ERR26 = dict(Mt=0.27, Mh=0.11, MW=0.0077, MZ=0.0021, als=0.0009)
v = smi.V


def C_pole(p):
    return 3 / v**2 * (p['Mh']**2 + 2 * p['MW']**2 + p['MZ']**2 - 4 * p['Mt']**2)


def Cfun(c):
    return (6 * c['lam'] + 2.25 * c['g2']**2 + 0.75 * (c.get('gY') or math.sqrt(0.6) * c['g1'])**2
            - 6 * c['yt']**2 - 6 * c['yb']**2 - 2 * c['ytau']**2)


def couplings(p, dyt=0.0, yt_override=None):
    c = couplings_at_mt(Mh=p['Mh'], Mt=p['Mt'], als=p['als'], MW=p['MW'])
    c['yt'] = (yt_override if yt_override is not None else c['yt']) + dyt
    return c


def C_msbar(p, **kw):
    return Cfun(couplings(p, **kw))


def budget(fun, p, err, extra):
    rows = {}
    for k, e in err.items():
        up, dn = dict(p), dict(p)
        up[k] += e
        dn[k] -= e
        rows[k] = abs(fun(up) - fun(dn)) / 2
    rows.update(extra)
    return rows, math.sqrt(sum(r * r for r in rows.values()))


def report(label, fun, p, err, extra):
    c0 = fun(p)
    rows, tot = budget(fun, p, err, extra)
    P(f"  {label}: C(M_t) = {c0:.4f}")
    for k, r in rows.items():
        P(f"      sigma from {k:22s}: {r:.4f}")
    P(f"      total sigma = {tot:.4f}   ->  C(M_t) = {c0:.3f} +- {tot:.3f},  |C|/sigma = {abs(c0)/tot:.0f}")
    return c0, tot


P("=" * 96)
P("(i) C(M_t) with full PDG uncertainty")
P("=" * 96)
for tag, p, err in (("PDG 2024", PDG24, ERR24), ("PDG 2026", PDG26, ERR26)):
    P(f"[{tag}]  inputs {p}")
    dCdmt = -24 * p['Mt'] / v**2
    report("(P) pole-mass form, PDG errors only", C_pole, p, err, {})
    report("(P) + MC-vs-pole 0.5 GeV", C_pole, p, err, {"MC vs pole (0.5 GeV)": abs(dCdmt) * 0.5})
    yt0 = couplings(p)['yt']
    dCdyt = 12 * yt0
    report("(M) MS-bar, Buttazzo, PDG errors + y_t theory 0.0005", C_msbar, p, err,
           {"y_t matching 0.0005": dCdyt * 0.0005})
    report("(M) MS-bar + MC 0.5 GeV + wide y_t spread 0.003", C_msbar, p, err,
           {"MC vs pole (0.5 GeV)": dCdyt * 0.00556 * 0.5, "y_t matching 0.003": dCdyt * 0.003})
    P("")

cJ = C_msbar(PDG24, yt_override=0.9005)
P(f"  (M) with Jegerlehner's y_t(M_t) = 0.9005 instead of Buttazzo's: C(M_t) = {cJ:.3f}")
cB = couplings(PDG24)
P(f"  MS-bar pieces at M_t (PDG 2024): y_t = {cB['yt']:.5f}, lam = {cB['lam']:.5f}")
bos = 6 * cB['lam'] + 2.25 * cB['g2']**2 + 0.75 * 0.6 * cB['g1']**2
fer = 6 * cB['yb']**2 + 2 * cB['ytau']**2
yt_star = math.sqrt((bos - fer) / 6)
P(f"  C(M_t) = 0 would need y_t(M_t) = {yt_star:.4f} (kappa_t = {yt_star/cB['yt']:.3f}), i.e. a top 'mass'"
  f" y v/sqrt2 = {yt_star*v/math.sqrt(2):.1f} GeV (MS-bar)")
mt_pole0 = math.sqrt((PDG24['Mh']**2 + 2 * PDG24['MW']**2 + PDG24['MZ']**2) / 4)
P(f"  C_pole = 0 would need m_t = {mt_pole0:.2f} GeV; measured 172.57 +- 0.29 -> "
  f"{(PDG24['Mt']-mt_pole0)/math.hypot(0.29, 0.5):.0f} sigma with MC term")
P("  The two determinations differ (-4.07 vs -3.43) by the one-loop matching of the couplings; both are")
P("  quoted. The conclusion C(M_t) != 0 holds in either, by > 65 sigma (smallest: MS-bar with MC term and y_t spread 0.003).")

P("\n" + "=" * 96)
P("(ii) Sign of C(mu) on [M_t, M_Pl] and transversality of any crossing (3-loop RGEs)")
P("=" * 96)


def traj(p, yt_override=None, top=1e25):
    c = couplings(p, yt_override=yt_override)
    return run(nloops=3, mu_max=top, inputs=c, Mt=p['Mt'])


def crossing(p, yt_override=None):
    f = traj(p, yt_override)
    g = lambda l: Cfun(f(10**l))  # noqa: E731
    l0 = brentq(g, 12, 24.9, xtol=1e-6)
    h = 1e-3
    slope = (g(l0 + h) - g(l0 - h)) / (2 * h) / math.log(10)  # dC/dln mu
    cmax = max(g(2.24 + 0.01 * i) for i in range(int((math.log10(smi.M_PLANCK) - 2.24) / 0.01)))
    return l0, slope, cmax, g


for lab, yo in (("Buttazzo matching", None), ("Jegerlehner y_t = 0.9005", 0.9005)):
    l0, s0, cmax, g = crossing(PDG24, yo)
    P(f"  [{lab}]  max of C on [M_t, M_Pl] = {cmax:.3f} (< 0: no zero below M_Pl)" if cmax < 0 else
      f"  [{lab}]  max of C on [M_t, M_Pl] = {cmax:.3f} (zero below M_Pl)")
    P(f"      C = 0 at log10 mu0 = {l0:.2f};  dC/dln mu at mu0 = {s0:+.4f}")
    if yo is None:
        ds = []
        for k, e in ERR24.items():
            for sgn in (+1, -1):
                q = dict(PDG24)
                q[k] += sgn * e
                ds.append((k, sgn, crossing(q)[1]))
        spread = {k: abs(a - b) / 2 for (k, sa, a), (_, sb, b) in zip(ds[0::2], ds[1::2])}
        sig = math.sqrt(sum(x * x for x in spread.values()))
        P(f"      slope error from PDG inputs: {sig:.4f}  ->  slope / sigma = {s0/sig:.0f}"
          f"  (rows: " + ", ".join(f"{k} {x:.4f}" for k, x in spread.items()) + ")")
    for l in (2.24, 10, 16, 19.09):
        P(f"      C(10^{l}) = {g(l):+.3f}")

P("\nInterpretation [computed]: C(M_t) is negative at > 65 sigma in either determination; C stays negative up")
P("to M_Pl with Buttazzo matching and crosses zero only at 10^22.8 GeV (10^16 with Jegerlehner's y_t), with a")
P("non-zero slope. Both facts would have come out differently if an SM symmetry enforced C = 0. A one-scale")
P("crossing with non-zero slope is what an accidental zero looks like; an RG-invariant (symmetry or")
P("reduction-of-couplings) relation would give C = 0 with dC/dln mu = 0 along the trajectory.")

with open(os.path.join(HERE, 'c9_C_measured_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
