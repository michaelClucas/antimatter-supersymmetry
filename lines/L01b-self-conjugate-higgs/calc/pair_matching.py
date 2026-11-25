"""L01b task 1 + 3: SUSY Higgs-mass cancellation in particle/antiparticle (pair) language, and the SM analogue.

Everything is one loop. Two equivalent Hamiltonian (old-fashioned PT / hole theory) representations are used:

 (Z) zero external momentum: m_h^2 shift = d^2/dphi^2 of the phi-dependent vacuum energy
       E0(phi) = sum_bosons n_i int d^3k/(2pi)^3 omega_i/2   (zero-point energy of boson pair fluctuations)
               - sum_fermions n_i int d^3k/(2pi)^3 omega_i/2  (Dirac-sea energy, C-symmetrized)
     omega_i = sqrt(k^2 + M_i^2(phi)), n_i = real degrees of freedom (Landau gauge for W, Z: 3 polarizations).
     This is the effective potential; with a 3-momentum cutoff K the K^2 term is C K^2/(8 pi^2) in
     Sigma_hh at fixed v (= shift of the |H|^2 coefficient x 2... see L01 calc/veltman_running.py for factor 2s;
     only RATIOS and ZEROS are used below, which are convention independent).

 (T) Higgs at rest (energy m_h), time-ordered orderings: top F (h -> t tbar) and B (vacuum Z-graph),
     stop seagull (equal-time stop-antistop pair at one vertex), stop bubbles F/B (h -> stop antistop).
     Cross-checked against covariant integrands with k0 Wick-rotated.

Conventions: V = -mu^2|H|^2 + lambda|H|^4, H0 = (v+h)/sqrt2, phi = v + h, m_h^2 = 2 lambda v^2.
M^2(phi) = a phi^2 + b. Per-species Lambda^2 coefficient C_i = n_i (+-1) a_i; C = sum C_i
 = 6 lambda + 9/4 g^2 + 3/4 g'^2 - 6 y_t^2 (L01 normalization).
"""
import math
import os
import sys

import numpy as np
import sympy as sp
from scipy.integrate import quad

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools')))
import sm_inputs as smi  # noqa: E402
from rg_sm import couplings_at_mt  # noqa: E402

out = []


def P(s=""):
    print(s)
    out.append(str(s))


# ---------------------------------------------------------------- couplings
v = smi.V
cMt = couplings_at_mt()
ms = dict(lam=cMt['lam'], g=cMt['g2'], gp=cMt['g1'] * math.sqrt(3 / 5), y=cMt['yt'])   # MS-bar at mu = M_t
pole = dict(lam=smi.MH**2 / (2 * v**2), g=2 * smi.MW / v, gp=2 * math.sqrt(smi.MZ**2 - smi.MW**2) / v,
            y=math.sqrt(2) * smi.MT / v)                                              # tree-level from pole masses

# ---------------------------------------------------------------- species table (particle / antiparticle resolved)
# (label, self-conjugate?, real dof n, sign, a(couplings))
SM_SPECIES = [
    ("W+ (3 pol.)", "charged pair", 3, +1, lambda c: c['g']**2 / 4),
    ("W- (3 pol.)", "charged pair", 3, +1, lambda c: c['g']**2 / 4),
    ("G+", "charged pair", 1, +1, lambda c: c['lam']),
    ("G-", "charged pair", 1, +1, lambda c: c['lam']),
    ("Z  (3 pol.)", "self-conjugate", 3, +1, lambda c: (c['g']**2 + c['gp']**2) / 4),
    ("G0", "self-conjugate", 1, +1, lambda c: c['lam']),
    ("h", "self-conjugate", 1, +1, lambda c: 3 * c['lam']),
    ("photon (2 pol.)", "self-conjugate", 2, +1, lambda c: 0.0),
    ("t_L , t_L-bar (3 col.)", "fermion pair (sea)", 6, -1, lambda c: c['y']**2 / 2),
    ("t_R , t_R-bar (3 col.)", "fermion pair (sea)", 6, -1, lambda c: c['y']**2 / 2),
]
STOPS = [  # SUSY comparison target only (not SM content)
    ("stop_L , stop_L* (3 col.)", "charged pair", 6, +1, lambda c: c['y']**2 / 2),
    ("stop_R , stop_R* (3 col.)", "charged pair", 6, +1, lambda c: c['y']**2 / 2),
]

P("=" * 100)
P("PART 1. Lambda^2 (K^2) coefficient by species, particle/antiparticle resolved  [C_i = n_i (+-) a_i]")
P("=" * 100)
for tag, c in (("MS-bar couplings at mu = M_t", ms), ("tree-level couplings from PDG pole masses", pole)):
    P(f"\n-- {tag}: lambda={c['lam']:.5f} g={c['g']:.5f} g'={c['gp']:.5f} y_t={c['y']:.5f}")
    groups = {}
    for name, cls, n, s, a in SM_SPECIES:
        Ci = n * s * a(c)
        groups.setdefault(cls, [0, 0.0])
        groups[cls][0] += n
        groups[cls][1] += Ci
        P(f"   {name:28s} {cls:20s} n={n:2d}  C_i = {Ci:+.4f}")
    Cb = groups['charged pair'][1] + groups['self-conjugate'][1]
    Ct = groups['fermion pair (sea)'][1]
    nb = groups['charged pair'][0] + groups['self-conjugate'][0] - 2   # photon has a = 0
    P(f"   charged boson pairs  (W+W-, G+G-)  n={groups['charged pair'][0]:2d}  C = {groups['charged pair'][1]:+.4f}")
    P(f"   self-conjugate bosons (Z, G0, h)   n={groups['self-conjugate'][0]-2:2d}  C = {groups['self-conjugate'][1]:+.4f}  (photon excluded, a=0)")
    P(f"   top sea pairs                      n={groups['fermion pair (sea)'][0]:2d}  C = {Ct:+.4f}")
    Cs = sum(n * s * a(c) for _, _, n, s, a in STOPS)
    P(f"   [SUSY target] stop/antistop pairs  n=12  C = {Cs:+.4f}  -> top + stops = {Ct + Cs:+.2e}")
    P(f"   SM total C = {Cb + Ct:+.4f}")
    P(f"   matching ratio R = C_bosons / |C_top| = {Cb/abs(Ct):.4f}   (SUSY: stops give R = 1 exactly)")
    P(f"   massive-boson real dof coupling to h: {nb} (vs 12 top-sea dof, 12 stop dof)")
    P(f"   mean coupling a per boson dof = {Cb/nb:.4f};  top/stop a = y^2/2 = {c['y']**2/2:.4f};  ratio {Cb/nb/(c['y']**2/2):.3f}")
    P(f"   'stop-equivalent' number of boson dof (C_bos / (y^2/2)) = {Cb/(c['y']**2/2):.2f} of the 12 needed")
    P(f"   |C| top alone -> top + SM bosons: {abs(Ct):.4f} -> {abs(Cb+Ct):.4f}  (reduction {100*(1-abs(Cb+Ct)/abs(Ct)):.1f}%)")

# ---------------------------------------------------------------- PART 2: mode-by-mode (hole theory) at zero momentum
P("\n" + "=" * 100)
P("PART 2. Mode-by-mode vacuum-energy (Dirac sea + boson zero-point) integrand d(d^2E0/dphi^2)/dk at phi = v")
P("=" * 100)
P("   per real dof: d^2/dphi^2 (omega/2) = a/(2 omega) - a^2 phi^2/(2 omega^3) [+ b-terms inside omega]")
P("   times k^2/(2 pi^2). Leading large-k term a k/(4pi^2) per dof -> C_i K^2/(8 pi^2).")


def mode(k, n, s, a, M2):
    w = math.sqrt(k * k + M2)
    return n * s * (a / (2 * w) - a * a * v * v / (2 * w**3)) * k * k / (2 * math.pi**2)


c = pole
mh2, MW2, MZ2, mt2 = smi.MH**2, smi.MW**2, smi.MZ**2, smi.MT**2
# Landau gauge masses at the minimum: G masses vanish (-mu^2 + lambda v^2 = 0), h mass m_h
sm_modes = [(6, +1, c['g']**2 / 4, MW2), (3, +1, (c['g']**2 + c['gp']**2) / 4, MZ2),
            (1, +1, 3 * c['lam'], mh2), (3, +1, c['lam'], 0.0), (12, -1, c['y']**2 / 2, mt2)]
P(f"   {'k/GeV':>9s} {'top sea':>12s} {'W+Z (pairs)':>12s} {'h+G (scalars)':>14s} {'SM bosons/|top|':>16s} {'stops(soft=0)':>14s} {'top+stops':>11s}")
for k in (10, 50, 100, 200, 500, 1e3, 1e4, 1e5, 1e6):
    t = mode(k, 12, -1, c['y']**2 / 2, mt2)
    wz = mode(k, 6, +1, c['g']**2 / 4, MW2) + mode(k, 3, +1, (c['g']**2 + c['gp']**2) / 4, MZ2)
    hg = mode(k, 1, +1, 3 * c['lam'], mh2) + mode(k, 3, +1, c['lam'], 0.0)
    st = mode(k, 12, +1, c['y']**2 / 2, mt2)
    P(f"   {k:9.0f} {t:+12.4e} {wz:+12.4e} {hg:+14.4e} {(wz+hg)/abs(t):16.4f} {st:+14.4e} {t+st:+11.1e}")
P("   -> With exact SUSY masses (m_stop = m_t) the stop/antistop zero-point modes cancel the top-sea modes at EVERY k")
P("      (not only the K^2 term). SM boson pairs have the right sign at every k but cancel only a fraction;")
P("      the fraction -> R (Part 1) as k -> infinity. At k ~ m_t the h/G modes become negative (their a^2 v^2 term).")

# ---------------------------------------------------------------- PART 3: on-shell time orderings, top vs stops
P("\n" + "=" * 100)
P("PART 3. Higgs at rest, time-ordered pieces of Sigma_hh: top (F, B) vs stops (seagull, F, B), soft mass m_s")
P("=" * 100)
p_, m_, mh_, y_ = sp.symbols('p m m_h y', positive=True)
E = sp.sqrt(p_**2 + m_**2)
I2, Z2 = sp.eye(2), sp.zeros(2)
blk = lambda A, B_, C_, D: sp.Matrix(sp.BlockMatrix([[A, B_], [C_, D]]))
beta = blk(I2, Z2, Z2, -I2)
alz = blk(Z2, sp.Matrix([[1, 0], [0, -1]]), sp.Matrix([[1, 0], [0, -1]]), Z2)
Hd = alz * p_ + beta * m_
Lp, Lm = (sp.eye(4) + Hd / E) / 2, (sp.eye(4) - Hd / E) / 2
S = sp.simplify((Lp * beta * Lm * beta).trace())
M2top = 3 * (y_**2 / 2) * S / (2 * mh_)
meas = p_**2 / (2 * sp.pi**2)
Ftop = 2 * mh_ * meas * M2top / (mh_ - 2 * E)
Btop = 2 * mh_ * meas * M2top / (-(mh_ + 2 * E))
P(f"   top spin sum |u^+ beta v|^2 = {S}")
P(f"   top F (h -> t tbar):          large-p dSigma/dp -> {sp.limit(Ftop / p_, p_, sp.oo)} * p")
P(f"   top B (vacuum t tbar Z-graph): large-p dSigma/dp -> {sp.limit(Btop / p_, p_, sp.oo)} * p")

# stops: two complex fields x 3 colours, M^2 = y^2 phi^2/2 + ms^2; seagull coupling d^2M^2/dh^2 = y^2 per real dof... :
# V = sum_real (1/2) M^2(phi) chi^2  -> seagull: a <chi^2>, a = y^2/2 per real dof, <chi^2> = int 1/(2 w)
# cubic: d^3V/dh dchi dchi = 2 a v ; real-dof bubble with identical pair: (1/2) c^2 int 1/(4w^2) [1/(mh-2w) - 1/(mh+2w)]
ms_ = sp.symbols('m_s', positive=True)
Ms2 = m_**2 + ms_**2   # stop mass^2 = m_t^2 (F-term part y^2 v^2/2) + soft^2, both stops, A_t = 0
ws = sp.sqrt(p_**2 + Ms2)
a_st = y_**2 / 2
vv = sp.symbols('v', positive=True)
seag = 12 * a_st * meas / (2 * ws)
cub = 2 * a_st * vv
Fst = 12 * sp.Rational(1, 2) * cub**2 * meas / (4 * ws**2) / (mh_ - 2 * ws)
Bst = 12 * sp.Rational(1, 2) * cub**2 * meas / (4 * ws**2) / (-(mh_ + 2 * ws))
P(f"   stop seagull (equal-time stop-antistop pair): large-p -> {sp.limit(seag / p_, p_, sp.oo)} * p")
P(f"   stop F, B bubbles (h -> stop antistop; vacuum pair): large-p ~ p^-1 (log only): "
  f"{sp.limit(Fst * p_, p_, sp.oo)}/p, {sp.limit(Bst * p_, p_, sp.oo)}/p")
tot = Ftop + Btop + seag + Fst + Bst
# numeric with y = sqrt2 m/v (m = m_t)
num = {m_: smi.MT, mh_: smi.MH, vv: v}
num[y_] = math.sqrt(2) * smi.MT / v
for msoft in (0.0, 1000.0):
    f = sp.lambdify(p_, tot.subs(num).subs(ms_, msoft), 'math')
    ft = sp.lambdify(p_, (Ftop + Btop).subs(num), 'math')
    P(f"   m_soft = {msoft:6.0f} GeV:   p      top(F+B)      top+stops(all orderings)   p*(top+stops)")
    for pp in (100, 1e3, 1e4, 1e5, 1e6):
        P(f"        {pp:10.0f}  {ft(pp):+12.4e}  {f(pp):+14.4e}            {pp*f(pp):+.4e}")
yv = math.sqrt(2) * smi.MT / v
P("   expected from Part 4 (m_Q = m_U = m_s, A_t = 0): d Sigma/dp -> -(3 y^2/(4 pi^2)) m_s^2 / p")
P(f"   = {-3*yv**2*1000.0**2/(4*math.pi**2):+.4e} / p for m_s = 1 TeV  (compare last column)")

# covariant cross-check of the stop bubble (scalar loop) at fixed |p|
def stop_bubble_cov(pp, M2, mh, c3):
    """Per real dof, vertex -i c3 (V = c3/2 h chi^2): -i Sigma = (1/2)(-i c3)^2 int i/D1 i/D2 = (c3^2/2) int d^4k/(2pi)^4 /(D1 D2).
    k0 = i w: Sigma = -(c3^2/2) int dw/(2pi) 1/(D1 D2) per d^3k/(2pi)^3; delta m^2 = +Sigma. 12 real stop dof."""
    def integrand(wE):
        k0 = 1j * wE
        return 1.0 / ((k0**2 - pp**2 - M2) * ((k0 + mh)**2 - pp**2 - M2))
    re = quad(lambda w: integrand(w).real, -np.inf, np.inf, limit=400)[0]
    return 12 * 0.5 * c3**2 * (-re) / (2 * np.pi) * pp**2 / (2 * np.pi**2)


fF = sp.lambdify(p_, (Fst + Bst).subs(num).subs(ms_, 300.0), 'math')
c3n = float(cub.subs(num))
P("   covariant (k0 Wick-rotated) vs time-ordered stop bubble F+B, m_s = 300 GeV:")
for pp in (50.0, 300.0, 3000.0):
    P(f"     p = {pp:7.1f}:  covariant {stop_bubble_cov(pp, smi.MT**2 + 300.0**2, smi.MH, c3n):+.6e}   F+B {fF(pp):+.6e}")

# ---------------------------------------------------------------- PART 4: SUSY identities (effective potential)
P("\n" + "=" * 100)
P("PART 4. SUSY comparison target: supertrace identities, top/stop and electroweak sectors")
P("=" * 100)
phi, yy, mQ, mU, At = sp.symbols('phi y m_Q m_U A_t', positive=True)
Mst = sp.Matrix([[mQ**2 + yy**2 * phi**2 / 2, yy * At * phi / sp.sqrt(2)],
                 [yy * At * phi / sp.sqrt(2), mU**2 + yy**2 * phi**2 / 2]])
STr2 = 6 * Mst.trace() - 12 * yy**2 * phi**2 / 2
STr4 = 6 * (Mst * Mst).trace() - 12 * (yy**2 * phi**2 / 2)**2
P(f"   STr M^2 (stops 2 complex x 3 col = 12 real dof; top 12 dof) = {sp.simplify(STr2)}  (phi-independent: no Lambda^2)")
logcoef = sp.expand(-sp.diff(STr4, phi, 2).subs(phi, 0) / (64 * sp.pi**2) * 2)   # V1 ⊃ -(ln Lambda^2/64pi^2) STr M^4
P(f"   ln(Lambda^2) coefficient of d^2V/dphi^2 at phi=0: {sp.factor(logcoef)}")
P("     -> delta m_H^2 (|H|^2 coeff = (1/2) d^2V/dphi^2... per ln Lambda): -(3 y^2/8pi^2)(m_Q^2 + m_U^2 + A_t^2) ln(Lambda/m)")
P("        the standard MSSM result (e.g. Martin, hep-ph/9709356). Only the SOFT mass, which splits stop from top, survives.")

# Electroweak sector of the MSSM: gauge bosons + Higgs scalars (D-term quartics) vs gauginos + higgsinos
g, gp, vu, vd, M1, M2, mu = sp.symbols('g gp v_u v_d M_1 M_2 mu', positive=True)
re_ = sp.symbols('x0:8', real=True)
Hu = sp.Matrix([re_[0] + sp.I * re_[1], re_[2] + sp.I * re_[3]]) / sp.sqrt(2)       # (Hu+, Hu0), Y = +1/2
Hdv = sp.Matrix([re_[4] + sp.I * re_[5], re_[6] + sp.I * re_[7]]) / sp.sqrt(2)      # (Hd0, Hd-), Y = -1/2
nHu = (Hu.H * Hu)[0]
nHd = (Hdv.H * Hdv)[0]
# Hu^dagger Hd with SU(2) contraction for the doublet structure (Hu+,Hu0),(Hd0,Hd-): |Hu^+ Hd^0* + Hu^0 Hd^-*|^2
# Martin eq. (8.1.x): V_D = (g^2+g'^2)/8 (|Hu|^2-|Hd|^2)^2 + g^2/2 |Hu^+ Hd^0* + Hu^0 Hd^-*|^2
cross = Hu[0] * sp.conjugate(Hdv[0]) + Hu[1] * sp.conjugate(Hdv[1])
VD = (g**2 + gp**2) / 8 * (nHu - nHd)**2 + g**2 / 2 * sp.expand(cross * sp.conjugate(cross))
VD = sp.expand(VD)
bg = {re_[0]: 0, re_[1]: 0, re_[2]: vu, re_[3]: 0, re_[4]: vd, re_[5]: 0, re_[6]: 0, re_[7]: 0}
TrS = sp.simplify(sum(sp.diff(VD, x, 2) for x in re_).subs(bg))
TrV = 3 * (2 * g**2 * (vu**2 + vd**2) / 4 + (g**2 + gp**2) * (vu**2 + vd**2) / 4)
Nmat = sp.Matrix([[M1, 0, -gp * vd / 2, gp * vu / 2], [0, M2, g * vd / 2, -g * vu / 2],
                  [-gp * vd / 2, g * vd / 2, 0, -mu], [gp * vu / 2, -g * vu / 2, -mu, 0]])
Xmat = sp.Matrix([[M2, g * vu / sp.sqrt(2)], [g * vd / sp.sqrt(2), mu]])
TrN = sp.expand((Nmat.T * Nmat).trace())
TrC = sp.expand((Xmat.T * Xmat).trace())
soft = M1**2 + M2**2 + 2 * mu**2
ferm = sp.expand(2 * TrN + 4 * TrC - 2 * (M1**2 + M2**2 + 2 * mu**2) - 4 * (M2**2 + mu**2))  # field-dependent part only
P(f"   Higgs scalars (8 real, D-term quartics) Tr M_S^2 (field-dependent) = {sp.factor(TrS)}")
P(f"   gauge bosons  3 x Tr M_V^2                                 = {sp.factor(TrV)}")
P(f"   neutralinos (4 Majorana, self-conjugate) 2 Tr M^+M (field-dep.) = {sp.factor(sp.expand(2*TrN - 2*(M1**2+M2**2+2*mu**2)))}")
P(f"   charginos   (2 Dirac, charged pairs)     4 Tr X^+X (field-dep.) = {sp.factor(sp.expand(4*TrC - 4*(M2**2+mu**2)))}")
P(f"   STr (bosons - fermions) = {sp.simplify(TrS + TrV - ferm)}")
P("   -> In SUSY the SM-like boson loops (W, Z, h, Goldstones) are themselves cancelled, by electroweakinos.")
P("      The self-conjugate bosons (Z, photon, neutral Higgs) are partnered by self-conjugate (Majorana) neutralinos;")
P("      the charged pairs (W+-, H+-) by charged Dirac pairs (charginos). Self-conjugacy is carried across the multiplet.")
gauge_sc = 3 * (g**2 + gp**2) * (vu**2 + vd**2) / 4
P(f"   e.g. Z alone ({sp.factor(gauge_sc)}) vs gaugino-higgsino neutralino mixing part; total cancels only summed with scalars.")

with open(os.path.join(HERE, 'pair_matching_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(out) + "\n")
