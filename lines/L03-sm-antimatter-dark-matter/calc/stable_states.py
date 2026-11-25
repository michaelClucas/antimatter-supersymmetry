"""Line L03: which SM states (particles, antiparticles, bound states) are stable, and can any be
cold, neutral, non-baryonic dark matter?  Also: SM 'R-parity' is trivial; B-L anomaly coefficients.

Run: python stable_states.py  (writes stable_states_output.txt)
"""
from fractions import Fraction as F
import math, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "tools"))
import sm_inputs as smi

out = []
def p(s=""):
    print(s); out.append(s)

# ---------------------------------------------------------------------------------------
# 1. SM fields with charges. (name, spin, B, L, Q list, multiplicity of states per generation)
# Weyl fermions are listed as left-handed fields; antiparticles have all charges negated.
FIELDS = [
    # name, 2s, B, L, Y (hypercharge, Q = T3 + Y), colour dim, SU(2) dim
    ("Q_L", 1, F(1, 3), 0, F(1, 6), 3, 2),
    ("u^c", 1, F(-1, 3), 0, F(-2, 3), 3, 1),
    ("d^c", 1, F(-1, 3), 0, F(1, 3), 3, 1),
    ("L_L", 1, 0, 1, F(-1, 2), 1, 2),
    ("e^c", 1, 0, -1, F(1, 1), 1, 1),
]
BOSONS = [("g", 2, 0, 0), ("W", 2, 0, 0), ("B", 2, 0, 0), ("H", 0, 0, 0)]

p("1. 'R-parity' of every SM field: R = (-1)^{3(B-L)+2s}")
for name, two_s, B, L, *_ in FIELDS:
    e = 3 * (B - L) + two_s
    p(f"   {name:5s}: 3(B-L)+2s = {e}  -> R = {1 - 2*(int(e) % 2):+d}")
for name, two_s, B, L in BOSONS:
    e = 3 * (B - L) + two_s
    p(f"   {name:5s}: 3(B-L)+2s = {e}  -> R = {1 - 2*(int(e) % 2):+d}")
p("   Every SM field (and its antiparticle, which flips B,L but not 2s mod 2) has R=+1, so every")
p("   SM state, elementary or composite, has R=+1. R-parity restricted to the SM is the identity")
p("   map: this is the identity (-1)^{2s} = (-1)^{3B+L} (spin-statistics + SM charge assignments).")
p("   It cannot stabilise anything beyond what (-1)^F, B, L already do.")
p()

# ---------------------------------------------------------------------------------------
# 2. Anomaly coefficients of B, L, B-L (sum over LH Weyl fields, 1 generation, x3 later)
def anom(charge_fn):
    su2 = su3 = y2 = grav = cubic = F(0)
    for name, two_s, B, L, Y, nc, nw in FIELDS:
        q = charge_fn(B, L)
        if nw == 2:
            su2 += q * nc * F(1, 2)  # T(fund)=1/2, times number of colours
        if nc == 3:
            su3 += q * nw * F(1, 2)
        y2 += q * nc * nw * Y * Y
        grav += q * nc * nw
        cubic += q ** 3 * nc * nw
    return su2, su3, y2, grav, cubic

p("2. Anomaly coefficients per generation, global U(1) x (gauge)^2, x gravity^2, U(1)^3 (no nu_R):")
for lab, fn in [("B", lambda B, L: B), ("L", lambda B, L: L), ("B-L", lambda B, L: B - L)]:
    a = anom(fn)
    p(f"   {lab:4s}: SU(2)^2 {str(a[0]):>5}  SU(3)^2 {str(a[1]):>5}  U(1)_Y^2 {str(a[2]):>6}  grav^2 {str(a[3]):>4}  self^3 {str(a[4]):>4}")
p("   B and L each have SU(2)^2 and U(1)_Y^2 anomalies (sphalerons/instantons violate B+L).")
p("   B-L: gauge anomalies cancel -> conserved by all SM gauge dynamics. Without nu_R its")
p("   mixed gravitational anomaly is -1 per generation (-3 total): B-L is a global symmetry with a")
p("   gravitational anomaly (irrelevant numerically, but 'exact' is only exact w.r.t. SM gauge fields).")
p("   Also: whether B-L survives neutrino-mass generation is unknown (Majorana mass breaks it by 2; A2).")
p()

# ---------------------------------------------------------------------------------------
# 3. Stable states and the lightest state in each sector of conserved charges (Q, B, L, (-1)^F)
me, mp, mn = 0.51099895e-3, 0.93827209, 0.93956542
mL = 1.115683
mH_atom = mp + me - 13.6e-9
md = 1.87561294
p("3. Lightest SM state in each sector of exactly/effectively conserved charges (T=0):")
rows = [
    ("Q!=0", "e-/e+ (Q=-+1)", me, "charged: couples to photons, not DM (E5)"),
    ("B=0,L!=0,Q=0", "lightest nu / nubar", None, "neutral, stable, HOT relic (see 4)"),
    ("F odd, Q=0, B=0", "lightest nu / nubar", None, "same"),
    ("B=+-1", "p / pbar", mp, "charged"),
    ("B=+-1, Q=0", "H / anti-H atom", mH_atom, "neutral but ionised before z~1100: baryonic (see 5)"),
    ("B=+-2, Q=0", "2H / anti-2H atom (or S/Sbar if it exists and m_S<1876.12 MeV)", md + me, "baryonic unless S exists"),
    ("all zero", "photon", 0.0, "radiation"),
]
for sec, st, m, note in rows:
    ms = "  m_nu<0.45 eV" if m is None else f"  m={1e3*m:9.3f} MeV"
    p(f"   {sec:18s} {st:60s}{ms}  {note}")
p("   Theorem used: in a theory whose only exact/effective conserved charges are Q, B, L, (-1)^F")
p("   and 4-momentum, the only absolutely stable single-particle states are the lightest state in each")
p("   charge sector; heavier states decay into lighter ones of equal charges (phase space permitting).")
p("   Unstable SM states (mu, tau, pi, K, n [880 s], W, Z, H, t, glueball-like states, positronium,")
p("   protonium, sphalerons) cannot be relic DM (lifetimes << 13.8 Gyr).")
p("   Topological defects: vacuum manifold of SU(2)xU(1)->U(1)_em is S^3; pi_0=pi_1=pi_2(S^3)=0,")
p("   so no stable domain walls, strings or monopoles in the SM.")
p()

# ---------------------------------------------------------------------------------------
# 4. Relic (anti)neutrinos: the only neutral, stable, non-baryonic SM relic
p("4. Relic neutrinos + antineutrinos (SM, existing, stable): Omega_nu h^2 = sum m_nu / 93.14 eV")
for S in (0.059, 0.072, 0.12, 3 * 0.45):
    p(f"   sum m = {S:5.3f} eV -> Omega_nu h^2 = {S/93.14:.2e}  (fraction of Omega_c h^2 = {S/93.14/smi.OMEGA_C_H2:.3f})")
p("   Even at the KATRIN-limit-saturating 3x0.45 eV, Omega_nu h^2 = 0.0145 < 0.12, and nu are hot")
p("   (relativistic at matter-radiation equality for m < ~1 eV); hot DM at this level is excluded by")
p("   structure formation. A lepton asymmetry (antineutrino excess) only raises n_nu via a chemical")
p("   potential, bounded by N_eff (E6); it does not make them cold.")
p()

# ---------------------------------------------------------------------------------------
# 5. CMB: antibaryons count as baryons
T0 = 2.7255
omega_gamma_h2 = 2.4728e-5 * (T0 / 2.7255) ** 4
zstar = 1089.9
def R(omb):
    return 3 * omb / (4 * omega_gamma_h2) / (1 + zstar)
p("5. CMB baryon loading R = 3 rho_b / (4 rho_gamma) at z*=1090:")
p(f"   Omega_b h^2 = {smi.OMEGA_B_H2}: R = {R(smi.OMEGA_B_H2):.3f}")
p(f"   If the 0.12 of DM were antibaryonic plasma (pbar, e+): R = {R(smi.OMEGA_B_H2+smi.OMEGA_C_H2):.3f}")
p("   Thomson cross section sigma_T = (8pi/3) alpha^2/m_e^2 depends on charge squared and mass,")
p("   identical for e+ and e- (CPT, B2/B6); pbar-e+ Coulomb coupling identical to p-e-. So the")
p("   acoustic physics measures rho(baryons)+rho(antibaryons) and gets 0.0224, not 0.142.")
p("   Ratio of R values = %.1f: excluded by the observed odd/even peak heights." % (R(smi.OMEGA_B_H2 + smi.OMEGA_C_H2) / R(smi.OMEGA_B_H2)))
p()

# ---------------------------------------------------------------------------------------
# 6. Sexaquark (uuddss, B=2, Q=0, S=-2) stability windows [hypothetical, existence unobserved]
p("6. Sexaquark S (hypothetical) mass windows:")
p(f"   m_S < m(2H atom) = m_d + m_e = {1e3*(md+me):.2f} MeV : absolutely stable")
p(f"   m_S < m_p + m_e + m_Lambda = {1e3*(mp+me+mL):.2f} MeV : decay needs Delta S = 2 (doubly weak), tau >> t_U (Farrar)")
p(f"   m_S < 2 m_Lambda = {2e3*mL:.2f} MeV : strong decay forbidden")
p(f"   m_S < 2 m_p = {2e3*mp:.2f} MeV : nuclei can't convert pp->S, but nn/np/pp->S+... depends on m_S vs 2m_N - binding")
p("   Gross et al. 1803.10242: thermal DM abundance would need m_S ~ 1.2 GeV, excluded by 16O stability.")
p("   BaBar 1810.04724: B(Upsilon(2S,3S)->S Lbar Lbar) < 1.2-1.4e-7 for m_S < 2.05 GeV.")
p("   Lattice (SU(3)-symmetric point, m_pi ~ 420 MeV) 2103.01054: H dibaryon bound by ~4.6 MeV only.")
p()

# ---------------------------------------------------------------------------------------
# 7. Required yield
p("7. Required number yield for Omega h^2 = 0.12 as a function of relic mass m:")
s0 = 2891.2; rc = 1.05368e-5
for m in (0.9389, 1.88, 1e3):
    Y = smi.OMEGA_C_H2 * rc / (m * s0)
    p(f"   m = {m:8.4f} GeV: Y = n/s = {Y:.3e}")

with open(os.path.join(os.path.dirname(__file__), "stable_states_output.txt"), "w") as f:
    f.write("\n".join(out) + "\n")
