"""L04 step 2: Pauli supertrace sums for the SM with measured masses, compared to rho_Lambda.
Weights s_i = (-1)^F g_i with physical (unitary-gauge) d.o.f.  Run: python sm_pauli_sums.py"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'tools'))
from sm_inputs import MZ, MW, MH, MT, MB, MC, MTAU, RHO_LAMBDA_GEV4, M_PLANCK

# PDG 2024 light masses (GeV); light quarks MS-bar at 2 GeV. They are irrelevant at the 1e-6 level for m^2, m^4 sums.
MU_Q, MD_Q, MS_Q = 2.16e-3, 4.70e-3, 93.5e-3
ME, MMU = 0.51099895e-3, 0.1056583755
# Neutrinos: PDG 2024 NuFIT-style central values, normal ordering, lightest = 0 [approx]
DM21, DM31 = 7.53e-5, 2.51e-3          # eV^2
mnu = [0.0, math.sqrt(DM21) * 1e-9, math.sqrt(DM31) * 1e-9]   # GeV

# (name, mass GeV, signed weight, spin class) ; spin class 'V' vector, 'S' scalar, 'F' fermion
def spectrum(nu_dof=2):
    sp = [("gluon", 0.0, +16, 'V'), ("photon", 0.0, +2, 'V'),
          ("W+-", MW, +6, 'V'), ("Z", MZ, +3, 'V'), ("h", MH, +1, 'S')]
    for n, m in [("u", MU_Q), ("d", MD_Q), ("s", MS_Q), ("c", MC), ("b", MB), ("t", MT)]:
        sp.append((n, m, -12, 'F'))          # 3 colours x 4 (Dirac: 2 spin x particle/antiparticle)
    for n, m in [("e", ME), ("mu", MMU), ("tau", MTAU)]:
        sp.append((n, m, -4, 'F'))
    for i, m in enumerate(mnu):
        sp.append((f"nu{i+1}", m, -nu_dof, 'F'))
    return sp

def sums(sp, mu=1.0):
    S0 = sum(w for _, m, w, _ in sp)
    S2 = sum(w * m**2 for _, m, w, _ in sp)
    S4 = sum(w * m**4 for _, m, w, _ in sp)
    S4L = sum(w * m**4 * math.log(m**2 / mu**2) for _, m, w, _ in sp if m > 0)
    return S0, S2, S4, S4L

def rho_dimreg(sp, mu):
    """MS-bar one-loop vacuum energy at the physical vacuum (Landau gauge, Goldstones massless at tree minimum).
    Per d.o.f. constant: 3/2 for scalars and fermions, 5/6 for massive vectors (scheme constant)."""
    tot = 0.0
    for _, m, w, c in sp:
        if m == 0: continue
        cst = 5/6 if c == 'V' else 3/2
        tot += w * m**4 * (math.log(m**2 / mu**2) - cst)
    return tot / (64 * math.pi**2)

pi2 = math.pi**2
out = []
P = lambda *a: out.append(" ".join(str(x) for x in a))
sp = spectrum()
nb = sum(w for _, _, w, _ in sp if w > 0); nf = -sum(w for _, _, w, _ in sp if w < 0)
P(f"d.o.f.: bosonic {nb}, fermionic {nf} (nu_L only: 2 each)")
S0, S2, S4, S4L = sums(sp, mu=1.0)
P(f"Str 1            = {S0}")
P(f"Str m^2          = {S2:.6e} GeV^2")
P(f"Str m^4          = {S4:.6e} GeV^4")
P(f"Str m^4 ln(m^2/GeV^2) = {S4L:.6e} GeV^4  (unit-dependent because Str m^4 != 0)")
P("\nContributions to Str m^4 by species (GeV^4):")
for n, m, w, c in sp:
    if m > 0 and abs(w * m**4) > 1e3: P(f"   {n:6s} {w:+4d} x m^4 = {w*m**4:+.4e}")
bos4 = sum(w * m**4 for _, m, w, _ in sp if w > 0); fer4 = sum(w * m**4 for _, m, w, _ in sp if w < 0)
P(f"   bosons {bos4:.4e}, fermions {fer4:.4e}, ratio |F/B| = {abs(fer4/bos4):.2f}")
bos2 = sum(w * m**2 for _, m, w, _ in sp if w > 0); fer2 = sum(w * m**2 for _, m, w, _ in sp if w < 0)
P(f"   Str m^2: bosons {bos2:.4e}, fermions {fer2:.4e}, ratio |F/B| = {abs(fer2/bos2):.2f}")
nu4 = sum(w * m**4 for n, m, w, _ in sp if n.startswith('nu'))
P(f"   neutrino part of Str m^4 = {nu4:.3e} GeV^4 ; /(64 pi^2) = {nu4/(64*pi2):.3e} vs rho_Lambda {RHO_LAMBDA_GEV4:.1e}")

P("\nDirac vs (excluded) nu_R counting: Str 1 with 4 d.o.f. per neutrino =", sums(spectrum(4))[0])

P("\nHard cutoff terms (per Visser eq. structure): rho = [Str1 L^4 + Str m^2 L^2]/(16 pi^2) - Str m^4/(64 pi^2) ln(L^2) + finite")
for name, L in [("1 TeV", 1e3), ("M_Pl", M_PLANCK)]:
    q4 = S0 * L**4 / (16 * pi2); q2 = S2 * L**2 / (16 * pi2); lg = -S4 * math.log(4 * L**2) / (64 * pi2)
    P(f"  Lambda={name}: quartic {q4:.3e}, quadratic {q2:.3e}, log {lg:.3e} GeV^4;"
      f" ratios to rho_Lambda: {abs(q4)/RHO_LAMBDA_GEV4:.1e}, {abs(q2)/RHO_LAMBDA_GEV4:.1e}, {abs(lg)/RHO_LAMBDA_GEV4:.1e}")

P("\nDim-reg (MS-bar), Lorentz invariant: rho(mu) = sum s_i m_i^4 [ln(m_i^2/mu^2) - c_i]/(64 pi^2)")
for mu in [MZ, MT, 1e3, 1e10, M_PLANCK]:
    r = rho_dimreg(sp, mu)
    P(f"  mu = {mu:.4g} GeV: rho = {r:+.4e} GeV^4,  |rho|/rho_Lambda = {abs(r)/RHO_LAMBDA_GEV4:.2e}")
# mu* where it vanishes: d rho/d ln mu^2 = -Str m^4/(64 pi^2) so rho is linear in ln mu^2
r1 = rho_dimreg(sp, 1.0)
lnmu2 = r1 / (S4 / (64 * pi2))   # rho(mu) = rho(1) - S4 ln(mu^2)/(64 pi^2)
mustar = math.exp(lnmu2 / 2)
assert abs(rho_dimreg(sp, mustar)) < 1e-6 * abs(r1)
P(f"  rho(mu)=0 at mu* = {mustar:.3f} GeV (scheme/scale artifact: bare Lambda counterterm absorbs mu-dependence)")
P(f"  d rho / d ln mu = -Str m^4/(32 pi^2) = {-S4/(32*pi2):+.3e} GeV^4  -> rho_Lambda tuned to 1 part in {abs(S4/(32*pi2))/RHO_LAMBDA_GEV4:.1e} per e-fold")

P("\nWeak-scale normalisations:  Str m^4/(64 pi^2) / rho_Lambda =", f"{abs(S4)/(64*pi2)/RHO_LAMBDA_GEV4:.2e}")
P("Classical Higgs potential depth lambda v^4/4 =", f"{(MH**2/(2*246.22**2))*246.22**4/4:.3e} GeV^4 (not a Pauli sum; CONSTRAINTS G)")
others4 = fer4 + 12 * MT**4; others2 = fer2 + 12 * MT**2
P(f"Top mass that would give Str m^4 = 0 (other masses fixed): {((bos4 + others4)/12)**0.25:.1f} GeV;"
  f" Str m^2 = 0: {((bos2 + others2)/12)**0.5:.1f} GeV (measured {MT})")
P("Neutrino sector alone, dim-reg, sum s m^4 [ln(m^2/mu^2) - 3/2]/(64 pi^2):")
for mu in [1e-9, 1e-6, 1.0]:
    r = sum(w * m**4 * (math.log(m**2/mu**2) - 1.5) for n, m, w, _ in sp if n.startswith('nu') and m > 0) / (64*pi2)
    P(f"   mu={mu:.0e} GeV: {r:+.3e} GeV^4 = {abs(r)/RHO_LAMBDA_GEV4:.1e} rho_Lambda")
txt = "\n".join(out); print(txt)
open(os.path.join(os.path.dirname(__file__), 'sm_pauli_sums_out.txt'), 'w').write(txt + "\n")
