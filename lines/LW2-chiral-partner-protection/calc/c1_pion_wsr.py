"""LW2 c1: pion EM mass splitting as the SM's own finite scalar-mass cancellation (DGMLY 1967).

Checks:
 (a) symbolic: if spectral weights c_i obey sum c_i = 0 (WSR1) and sum c_i m_i^2 = 0 (WSR2),
     the photon-loop integral int_0^L2 dQ2 sum_i c_i Q2/(Q2+m_i^2) is finite as L2 -> inf;
     WSR1 alone leaves a log, neither leaves L2 (quadratic).
 (b) DGMLY closed form from rho + a1 + pion saturation, derived here (not copied).
 (c) numbers: measured Delta m_pi^2, naive-cutoff 'naturalness scale', DGMLY prediction (PDG a1, KSRF a1).
 (d) SUSY comparison: top/stop one-loop Higgs mass parameter with cutoff (Coleman-Weinberg),
     showing Lambda^2 cancels (Str M^2 field-independent) but a log survives (Str M^4 is not).
Inputs: PDG 2024 (RPP, Phys. Rev. D 110, 030001).
"""
import math
import sympy as sp

# ---------- (a) general sum-rule finiteness
# J(m2, L) = int_0^L dQ2 Q2/(Q2+m2) = L - m2 ln(1+L/m2). Large-L expansion (checked by sympy series):
#   J = L - m2 ln L + m2 ln m2 + O(1/L)
L, u, ms = sp.symbols('L u m2', positive=True)
J = L - ms * sp.log(1 + L / ms)
Jser = sp.series(sp.expand_log(J.subs(L, 1 / u), force=True), u, 0, 1).removeO()
print("(a) J(m2,L) large-L:", sp.simplify(Jser.subs(u, 1 / L)), " [= L - m2 ln L + m2 ln m2]")
cs = sp.symbols('c1:4'); mm = sp.symbols('M1:4', positive=True)
lin = sum(c for c in cs); lg = sum(c * m for c, m in zip(cs, mm))
print("    sum_i c_i J(m_i): coeff of L =", lin, "; coeff of ln L =", -lg,
      "; constant =", sum(c * m * sp.log(m) for c, m in zip(cs, mm)))
print("    => WSR1 (sum c = 0) kills Lambda^2; WSR2 (sum c m^2 = 0) kills ln Lambda; result finite = sum c_i m_i^2 ln m_i^2")

# ---------- (b) DGMLY: Pi_V = FV^2/(mV^2+Q2), Pi_A = fpi^2/Q2 + FA^2/(mA^2+Q2)
# Delta m^2 = -(3 alpha/(4 pi fpi^2)) int_0^inf dQ2 Q2 (Pi_V - Pi_A)
# weights: c_V = FV^2 (m=mV), c_A = -FA^2 (m=mA), c_pi = -fpi^2 (m=0)
FV, FA, fpi, mV, mA, al = sp.symbols('F_V F_A f_pi m_V m_A alpha', positive=True)
sol = sp.solve([sp.Eq(FV**2 - FA**2, fpi**2), sp.Eq(FV**2 * mV**2, FA**2 * mA**2)], [FV, FA], dict=True)[0]
print("(b) WSR1+WSR2 solution: F_V^2 =", sp.simplify(sol[FV]**2), ", F_A^2 =", sp.simplify(sol[FA]**2))
Ix = (FV**2 * mV**2 * sp.log(mV**2) - FA**2 * mA**2 * sp.log(mA**2)).subs(sol)
dm2 = -3 * al / (4 * sp.pi * fpi**2) * Ix
target = 3 * al / (4 * sp.pi) * mV**2 * mA**2 / (mA**2 - mV**2) * sp.log(mA**2 / mV**2)
print("    DGMLY closed form reproduced:", sp.simplify(sp.expand_log(dm2 - target, force=True)) == 0)
print("    pion-only (point-like, c_pi only): Delta m^2 = +(3 alpha/4 pi) Lambda^2 (quadratically divergent)")

# ---------- (c) numbers
alpha0 = 1 / 137.035999
mpic, mpi0 = 139.57039, 134.9768          # MeV, PDG 2024
mrho, ma1, da1 = 775.26, 1230.0, 40.0     # MeV, PDG 2024 (a1(1260) mass is a PDG estimate +-40)
dm2_meas = mpic**2 - mpi0**2
k = 3 * alpha0 / (4 * math.pi)
Lnat = math.sqrt(dm2_meas / k)
f = lambda V, A: k * V**2 * A**2 / (A**2 - V**2) * math.log(A**2 / V**2)
print(f"(c) measured m(pi+)^2 - m(pi0)^2 = {dm2_meas:.1f} MeV^2  (Delta m = {mpic - mpi0:.4f} MeV)")
print(f"    naive photon loop (3a/4pi) L^2 equals it at L_nat = {Lnat:.0f} MeV   [m_rho = {mrho}, m_a1 = {ma1}]")
for lab, A in (("PDG a1", ma1), ("a1-40", ma1 - da1), ("a1+40", ma1 + da1), ("KSRF a1=sqrt2*rho", math.sqrt(2) * mrho)):
    d = f(mrho, A)
    dm = math.sqrt(mpi0**2 + d) - mpi0
    print(f"    DGMLY [{lab:18s}] Delta m^2 = {d:7.1f} MeV^2 -> Delta m = {dm:.2f} MeV  (ratio to meas {d / dm2_meas:.2f})")
print("    note: m_u-m_d contributes to pi+ - pi0 only at O((m_u-m_d)^2), ~0.1 MeV [established, Gasser-Leutwyler]")

# ---------- (d) SUSY top/stop comparison (cutoff CW potential, large-Lambda form)
y, phi, mt2, Lam = sp.symbols('y phi mtilde2 Lambda', positive=True)
def Vpiece(n, M2):   # (1/32pi^2) n [Lambda^2 M^2 + M^4/2 (ln(M^2/Lambda^2) - 1/2)], n signed dof
    return n / (32 * sp.pi**2) * (Lam**2 * M2 + M2**2 / 2 * (sp.log(M2 / Lam**2) - sp.Rational(1, 2)))
Vtop = Vpiece(-12, y**2 * phi**2 / 2)
Vstop = Vpiece(12, mt2 + y**2 * phi**2 / 2)
d2 = lambda V: sp.limit(sp.diff(V, phi, 2), phi, 0)
quadpart = sp.simplify(sp.diff(Vtop + Vstop, phi, 2).coeff(Lam, 2).subs(phi, 0))
print("(d) top+stop: Lambda^2 coefficient of d2V/dphi2 at 0:", quadpart)
print("    top+stop: d2V/dphi2 at phi=0 =", sp.simplify(d2(Vtop) + d2(Vstop)),
      " = -(3 y^2/8pi^2) mtilde^2 ln(Lambda^2/mtilde^2): log survives in softly broken SUSY")
print("    => QCD (WSR1+WSR2) cancels both Lambda^2 and ln Lambda for pi+; soft SUSY cancels only Lambda^2.")
