"""Particle/antiparticle state counting in the one-loop gauge beta coefficients, and what reweighting would be needed.

Part 1: enumerate every SM on-shell state (particle AND antiparticle, each helicity) with its (SU3 rep, SU2 rep, Y),
compute b_i from a per-state rule and check it equals the field-theory b_i = (41/10, -19/6, -7).
Part 2: sympy: b_i(wV, wF, wS) with independent weights on gauge, fermion and scalar loops; show wF cancels from the
unification condition; solve for the wS or wV that would be needed.
Part 3: 2-loop gauge-only numerical check of 'antiparticles double counted' (wF=2) and 'particles only' (wF=wS=1/2).
"""
from fractions import Fraction as Fr
import math
import numpy as np
import sympy as sp
import sm_path  # noqa: F401
import sm_inputs as smi

# Dynkin indices T(R): fundamental 1/2, singlet 0. GUT-normalised U(1): T = (3/5) Y^2 (Y with Q = T3 + Y).
def T3(d):
    return Fr(1, 2) if d == 3 else Fr(0)
def T2(d):
    return Fr(1, 2) if d == 2 else Fr(0)

# One generation, left-handed Weyl fields: (SU3 dim, SU2 dim, Y). Their CP conjugates are the right-handed antistates.
gen = [("Q", 3, 2, Fr(1, 6)), ("u^c", 3, 1, Fr(-2, 3)), ("d^c", 3, 1, Fr(1, 3)),
       ("L", 1, 2, Fr(-1, 2)), ("e^c", 1, 1, Fr(1))]
# NB: no nu^c (A1/A2)

states = []  # (name, kind, n_states_per_component, su3dim, su2dim, Y, mult)
for g in range(3):
    for (n, d3, d2, Y) in gen:
        # each Weyl field: 1 particle helicity state + 1 antiparticle helicity state; components = d3*d2
        states.append((n, "fermion-particle", d3, d2, Y))
        states.append((n + "-bar", "fermion-antiparticle", d3, d2, -Y))   # conjugate rep: same T, opposite Y
# Higgs doublet: complex scalar, Y=1/2. Particle states and antiparticle states.
states.append(("H", "scalar-particle", 1, 2, Fr(1, 2)))
states.append(("H-bar", "scalar-antiparticle", 1, 2, Fr(-1, 2)))

# Per-state rule: each fermionic helicity state contributes (1/3) T(R) * (number of OTHER-group components),
# each scalar particle-or-antiparticle state contributes (1/6) T(R) * (...).
w = {"fermion-particle": Fr(1, 3), "fermion-antiparticle": Fr(1, 3), "scalar-particle": Fr(1, 6), "scalar-antiparticle": Fr(1, 6)}
bV = [Fr(0), Fr(-22, 3), Fr(-11)]

def b_from_states(wfac=None):
    wfac = wfac or {}
    b = [Fr(0)] * 3
    for (n, kind, d3, d2, Y) in states:
        f = w[kind] * wfac.get(kind, 1)
        b[0] += f * Fr(3, 5) * Y ** 2 * d3 * d2
        b[1] += f * T2(d2) * d3
        b[2] += f * T3(d3) * d2
    return [bV[i] + b[i] for i in range(3)]

b = b_from_states()
print("Part 1. b_i from explicit particle+antiparticle state sum:", [str(x) for x in b], " (SM: 41/10, -19/6, -7)")
assert b == [Fr(41, 10), Fr(-19, 6), Fr(-7)]
print("  Sum over fermion states of Y   =", sum(d3 * d2 * Y for (_, k, d3, d2, Y) in states if k.startswith("fermion")),
      "(C-odd piece cancels between particle and antiparticle)")
print("  Sum of Y^2 over particles only =", sum(d3 * d2 * Y ** 2 for (_, k, d3, d2, Y) in states if k == "fermion-particle"),
      "; over antiparticles only =", sum(d3 * d2 * Y ** 2 for (_, k, d3, d2, Y) in states if k == "fermion-antiparticle"))
bf_part = [x - y for x, y in zip(b_from_states({"fermion-antiparticle": 2}), b)]
print("  Extra contribution if antifermion states counted twice: Delta b =", [str(x) for x in bf_part], "(equal for i=1,2,3)")
bs_part = [x - y for x, y in zip(b_from_states({"scalar-antiparticle": 2}), b)]
print("  Extra contribution if anti-Higgs states counted twice:  Delta b =", [str(x) for x in bs_part])

# Part 2
wV, wF, wS = sp.symbols("w_V w_F w_S", positive=True)
bVs = sp.Matrix([0, sp.Rational(-22, 3), -11])
bFs = sp.Matrix([4, 4, 4])
bSs = sp.Matrix([sp.Rational(1, 10), sp.Rational(1, 6), 0])
bb = wV * bVs + wF * bFs + wS * bSs
a1, a2, a3 = smi.gauge_couplings_mz()
A = [1 / a1, 1 / a2, 1 / a3]
R_meas = (A[1] - A[2]) / (A[0] - A[1])
Bratio = sp.simplify((bb[1] - bb[2]) / (bb[0] - bb[1]))
print("\nPart 2. one-loop B-ratio (b2-b3)/(b1-b2) =", Bratio, " -> depends on w_F?", sp.diff(Bratio, wF) == 0 and "no" or "yes")
print(f"  measured (a2^-1-a3^-1)/(a1^-1-a2^-1) at MZ = {R_meas:.4f};  SM value = {float(Bratio.subs({wV:1,wS:1})):.4f};  MSSM value = {(1+3)/(33/5-1):.4f}")
sol_S = sp.solve(sp.Eq(Bratio.subs(wV, 1), sp.Rational(str(round(R_meas, 6)))), wS)
sol_V = sp.solve(sp.Eq(Bratio.subs(wS, 1), sp.Rational(str(round(R_meas, 6)))), wV)
print(f"  scalar-loop weight needed (w_V=1): w_S = {[float(s) for s in sol_S]}  (i.e. ~{float(sol_S[0]):.1f} Higgs doublets)")
print(f"  gauge-loop weight needed  (w_S=1): w_V = {[float(s) for s in sol_V]}")
# scale for the w_S solution
ws = float(sol_S[0])
bnum = np.array([float(x) for x in bb.subs({wV: 1, wF: 1, wS: ws})])
lnM = (A[0] - A[1]) / ((bnum[0] - bnum[1]) / (2 * math.pi))
print(f"  with that w_S: unification at 10^{math.log10(smi.MZ*math.exp(lnM)):.2f} GeV, alpha^-1 = {A[0]-bnum[0]/(2*math.pi)*lnM:.2f}")

# Part 3: 2-loop gauge-only running with weights (two-loop coefficients split by sector)
K = 1 / (16 * math.pi ** 2)
BV = np.array([[0, 0, 0], [0, -136 / 3, 0], [0, 0, -102]])
BF = np.array([[19 / 15, 3 / 5, 44 / 15], [1 / 5, 49 / 3, 4], [11 / 30, 3 / 2, 76 / 3]])  # per generation
BS = np.array([[9 / 50, 9 / 10, 0], [3 / 10, 13 / 6, 0], [0, 0, 0]])
assert np.allclose(BV + 3 * BF + BS, [[199 / 50, 27 / 10, 44 / 5], [9 / 10, 35 / 6, 12], [11 / 10, 9 / 2, -26]])

def run2(wF_, wS_, mu1=1e19, n=20000):
    b1 = np.array([0, -22 / 3, -11]) + wF_ * np.array([4, 4, 4]) + wS_ * np.array([0.1, 1 / 6, 0])
    B = BV + wF_ * 3 * BF + wS_ * BS
    g = 4 * math.pi * np.array([a1, a2, a3])
    ts = np.linspace(math.log(smi.MZ ** 2), math.log(mu1 ** 2), n)
    dt = ts[1] - ts[0]
    out = []
    for t in ts:
        out.append(4 * math.pi / g)
        f = lambda gg: gg ** 2 * K * b1 + gg ** 2 * K ** 2 * (B @ gg)
        k1 = f(g); k2 = f(g + dt / 2 * k1); k3 = f(g + dt / 2 * k2); k4 = f(g + dt * k3)
        g = g + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if np.any(g <= 0) or np.any(g > 4 * math.pi * 4):
            break
    out = np.array(out).T
    lmu = ts[:out.shape[1]] / 2 / math.log(10)
    spread = out.max(0) - out.min(0)
    k = np.argmin(np.where(lmu > 8, spread, np.inf))
    return lmu[k], spread[k], out[:, k].mean()

print("\nPart 3. two-loop gauge-only running (no Yukawa) with sector weights:")
for lab, wf_, ws_ in (("SM (w_F=1, w_S=1)", 1, 1), ("antifermion states counted twice (w_F=3/2)", 1.5, 1),
                      ("every fermion field counted twice (w_F=2)", 2, 1),
                      ("particles only, no antiparticles (w_F=w_S=1/2)", 0.5, 0.5),
                      ("antifermion + anti-Higgs states twice (w_F=w_S=3/2)", 1.5, 1.5),
                      (f"w_S = {ws:.2f} (1-loop solution)", 1, ws)):
    l, s, m = run2(wf_, ws_)
    print(f"  {lab:55s}: best point 10^{l:.2f} GeV, spread {s:.2f} (rel {s/m*100:.1f}%)")
