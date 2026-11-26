"""
L05 cycle 6: scope of the two-loop doubling theorem, and the gate-7 consistency check against published tables.

Conventions as in beta_map.py / c4_doubling.py:
  dg_i/dt = g_i^3/(16pi^2) b_i + g_i^3/(16pi^2)^2 sum_j b_ij g_j^2 + ...,  g_1 GUT-normalised.
Per-field two-loop weights (Machacek-Vaughn NPB 222 (1983) 83; Luo-Wang-Xiao PRD 67 (2003) 065019,
hep-ph/0211440, eq. (30) with the product-group rules (106)-(110)):
  Weyl fermion   2 S_i C_j + delta_ij (10/3) C(G_i) S_i
  complex scalar 4 S_i C_j + delta_ij (2/3)  C(G_i) S_i
  real scalar    2 S_i C_j + delta_ij (1/3)  C(G_i) S_i
  gauge          -(34/3) C(G_i)^2 delta_ij
SUSY (Jones PRD 25 (1982) 581; Martin-Vaughn PRD 50 (1994) 2282, hep-ph/9311340):
  -6 C(G_i)^2 delta_ij + sum_chiral [4 S_i C_j + 2 C(G_i) S_i delta_ij]

Sections:
  1. Published tables (gate item 7): SM from Mihaila-Salomon-Steinhauser arXiv:1201.5868 eq. (5) and
     Bednyakov-Pikelner-Velizhanin arXiv:1210.6873 eqs. (4.3)-(4.5); MSSM from Martin-Vaughn hep-ph/9311340 eq. (4.5)
     and Ferreira-Jack-Jones hep-ph/9605440. Each SM table x each MSSM table is tested against b(SUSY) = 2 b(SM)
     on i != j and (1,1).
  2. Scope counterexamples (referee 1, cycle 5, finding 1).
  3. Phi* theorem on 200 random contents (fixed seed).
Run from calc/: python c6_scope.py  (output c6_scope.txt)
"""
import random
from sympy import Rational as R, Matrix, symbols, expand, zeros, cancel

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

nG = symbols("n_G")

# ---------------------------------------------------------------- generic machinery, product group of up to 3 factors
class G:
    """factors: list of (CG, abelian). A field is a list over factors of (S_i, C_i)."""
    def __init__(self, factors):
        self.f = factors; self.n = len(factors)
    def field(self, per_factor):
        """per_factor: list of (dim, T, C) for each factor; S_i = T_i * prod_{k != i} dim_k."""
        res = []
        for i in range(self.n):
            mult = 1
            for k in range(self.n):
                if k != i:
                    mult *= per_factor[k][0]
            res.append((per_factor[i][1]*mult, per_factor[i][2]))
        return res

def b2(th, F=(), Sc=(), Sr=()):
    M = zeros(th.n, th.n)
    for fl, w, wd in ((F, 2, R(10, 3)), (Sc, 4, R(2, 3)), (Sr, 2, R(1, 3))):
        for x in fl:
            for i in range(th.n):
                for j in range(th.n):
                    M[i, j] += w*x[i][0]*x[j][1] + (wd*th.f[i][0]*x[i][0] if i == j else 0)
    for i in range(th.n):
        M[i, i] -= R(34, 3)*th.f[i][0]**2
    return M

def b2s(th, Ch):
    M = zeros(th.n, th.n)
    for x in Ch:
        for i in range(th.n):
            for j in range(th.n):
                M[i, j] += 4*x[i][0]*x[j][1] + (2*th.f[i][0]*x[i][0] if i == j else 0)
    for i in range(th.n):
        M[i, i] -= 6*th.f[i][0]**2
    return M

def ratios(A, B, th):
    """A/B on every i != j and abelian i = j; '0/0' where both vanish"""
    r = {}
    for i in range(th.n):
        for j in range(th.n):
            if i != j or th.f[i][1]:
                r[(i+1, j+1)] = cancel(A[i, j]/B[i, j]) if B[i, j] != 0 else ("0/0" if A[i, j] == 0 else "x/0")
    return r

def all2(r):
    return all(v == 2 or v == "0/0" for v in r.values())

# SM group, GUT-normalised U(1)
SMG = G([(0, True), (2, False), (3, False)])
T2 = {1: (0, 0), 2: (R(1, 2), R(3, 4)), 3: (2, 2)}
T3 = {1: (0, 0), 3: (R(1, 2), R(4, 3)), 8: (3, 3)}
def f(d2, d3, Y):
    y = R(3, 5)*Y**2
    return SMG.field([(1, y, y), (d2, *T2[d2]), (d3, *T3[d3])])
Q, uc, dc, L, ec = f(2, 3, R(1, 6)), f(1, 3, R(-2, 3)), f(1, 3, R(1, 3)), f(2, 1, R(-1, 2)), f(1, 1, 1)
H, Hc = f(2, 1, R(1, 2)), f(2, 1, R(-1, 2))
def gen(k):
    return [[(s*k, c) for (s, c) in x] for x in (Q, uc, dc, L, ec)]

SM = b2(SMG, gen(nG), [H])
MSSM = b2s(SMG, gen(nG) + [H, Hc])

# ---------------------------------------------------------------- 1. published tables
P("1. Gate item 7: published two-loop gauge tables vs b_ij(SUSY) = 2 b_ij(one-doublet parent), i != j and (1,1)")
# (a) Mihaila-Salomon-Steinhauser, arXiv:1201.5868 eq. (5): b = 16 x their alpha/pi coefficient (from TeX source, cycle 4)
SM_MSS = 16*Matrix([[R(9, 800)+19*nG/240, R(9, 160)+3*nG/80, 11*nG/60],
                    [R(3, 160)+nG/80, -R(259, 96)+49*nG/48, nG/4],
                    [11*nG/480, 3*nG/32, -R(51, 8)+19*nG/12]])
# (b) Bednyakov-Pikelner-Velizhanin, arXiv:1210.6873v4 eqs. (4.3)-(4.5), a_i = g_i^2/(16pi^2), beta = d a/d ln mu^2
#     = a_i^2 (b_i + sum_j b_ij a_j): read off with N_c = 3, C_F = 4/3, T_F = 1/2, C_A = 3, Yukawas and lambda dropped.
Nc, CF, TF, CA = 3, R(4, 3), R(1, 2), 3
SM_BPV = Matrix([
    [nG*(R(137, 900)*Nc + R(81, 100)) + R(9, 50), nG*(R(1, 20)*Nc + R(9, 20)) + R(9, 10), nG*R(11, 15)*CF*Nc],
    [nG*(R(1, 60)*Nc + R(3, 20)) + R(3, 10), nG*(R(49, 12)*Nc + R(49, 12)) - R(259, 6), nG*CF*Nc],
    [nG*R(11, 15)*TF, 3*TF*nG, nG*(R(40, 3)*CA*TF + 8*CF*TF) - R(34, 3)*CA**2]])
# one-loop cross-check of the BPV normalisation: beta_1 = a_1^2 (n_G(11 N_c/45 + 3/5) + 1/10) = 41/10 at n_G = 3
assert (nG*(R(11, 45)*Nc + R(3, 5)) + R(1, 10)).subs(nG, 3) == R(41, 10)
# (c) Martin-Vaughn, hep-ph/9311340 eq. (4.5), n_G = 3 (arXiv version read cycle 6; printed in the same row = i convention)
MSSM_MV = Matrix([[R(199, 25), R(27, 5), R(88, 5)], [R(9, 5), 25, 24], [R(11, 5), 9, 14]])
# (d) Ferreira-Jack-Jones, hep-ph/9605440, b_ij(n_g) (from TeX source, cycle 4)
MSSM_FJJ = Matrix([[R(38, 15)*nG+R(9, 25), R(6, 5)*nG+R(9, 5), R(88, 15)*nG],
                   [R(2, 5)*nG+R(3, 5), 14*nG-17, 8*nG],
                   [R(11, 15)*nG, 3*nG, R(68, 3)*nG-54]])
assert (SM - SM_MSS).expand() == zeros(3, 3)
assert (SM - SM_BPV).expand() == zeros(3, 3)
assert (MSSM - MSSM_FJJ).expand() == zeros(3, 3)
assert MSSM.subs(nG, 3) == MSSM_MV
P("   field-content formulas reproduce all four tables (MSS, BPV for all n_G; FJJ for all n_G; MV at n_G = 3): OK")
for sn, S_ in (("MSS 1201.5868", SM_MSS), ("BPV 1210.6873", SM_BPV)):
    for mn, M_, sub in (("MV 9311340", MSSM_MV, True), ("FJJ 9605440", MSSM_FJJ, False)):
        Sx = S_.subs(nG, 3) if sub else S_
        r = ratios(M_, Sx, SMG)
        ok = all2(r)
        P(f"   {mn} / {sn}{' (n_G=3)' if sub else ' (all n_G)'}: ratios {sorted(set(map(str, r.values())))}  -> {'PASS' if ok else 'FAIL'}")
        assert ok
        d = [(M_[i, i]/Sx[i, i]) for i in (1, 2)]
        if sub:
            P(f"      non-abelian diagonal ratios (not covered by the theorem): b22 {d[0]}, b33 {d[1]}")

# ---------------------------------------------------------------- 2. scope counterexamples
P("\n2. Scope: the doubling needs a one-doublet SM-like parent (exactly one complex doublet -> H + H^c)")
r = ratios(MSSM, SM, SMG); assert all2(r)
P("   SM (one doublet) -> MSSM, all n_G:", sorted(set(map(str, r.values()))))
# (a) 2HDM parent -> MSSM (minimal SUSY of two doublets is one chiral each; H_d plays the role of the second doublet)
H2HDM = b2(SMG, gen(3), [H, H])  # two Y = +1/2 doublets; (H1, H2^c) gives identical numbers since S, C are conj-blind
r = ratios(MSSM.subs(nG, 3), H2HDM, SMG)
P("   2HDM parent -> MSSM:", r)
assert r[(1, 2)] == r[(2, 1)] == R(3, 2) and r[(1, 1)] == R(199, 104)
assert r[(1, 3)] == r[(3, 1)] == r[(2, 3)] == r[(3, 2)] == 2
P("      -> (1,2),(2,1) = 3/2, (1,1) = 199/104; colour-mixed entries stay 2 (the Higgs is colourless).")
# (b) vector-like complex scalar pair (2,1,+1/2) + (2,1,-1/2): minimal SUSY = two chirals (each higgsino is the
#     other's anomaly partner), Phi* would need four
D, Dc = f(2, 1, R(1, 2)), f(2, 1, R(-1, 2))
r = ratios(b2s(SMG, [D, Dc]), b2(SMG, [], [D, Dc]), SMG)
P("   vector-like scalar pair (2,1,+-1/2), minimal SUSY = 2 chirals:", {k: v for k, v in r.items() if v != "0/0"})
assert all(v == 1 for v in r.values() if v != "0/0")
# toy SU(2) x SU(3) with Weyl (2,3) + (2,3bar) (anomaly-free, Witten-safe: 6 doublets)
T23 = G([(2, False), (3, False)])
def g23(d2, d3):
    return T23.field([(d2, *T2[d2]), (d3, *T3[d3])])
W = [g23(2, 3), g23(2, 3)]  # (2,3) and (2,3bar): identical S, C
# (c) complex scalar in the pseudoreal rep (2,8,0): one chiral (2,8) has 8 doublets (Witten-safe) and no SU(3)^3
#     anomaly (adjoint), so minimal SUSY is ONE chiral
P8 = g23(2, 8)
r = ratios(b2s(T23, W + [P8]), b2(T23, W, [P8]), T23)
P("   complex scalar (2,8,0) pseudoreal, minimal SUSY = 1 chiral:", r)
assert r[(1, 2)] == r[(2, 1)] == R(8, 7)
r = ratios(b2s(T23, W + [P8, P8]), b2(T23, W, [P8]), T23)
P("      same with Phi* (2 chirals):", r); assert all2(r)
# (d) complex scalar in the real rep (3,8): minimal SUSY = one chiral
X = g23(3, 8)
r = ratios(b2s(T23, W + [X]), b2(T23, W, [X]), T23)
P("   complex scalar (3,8) real rep, minimal SUSY = 1 chiral:", r)
assert r[(1, 2)] == r[(2, 1)] == R(26, 25)
r = ratios(b2s(T23, W + [X, X]), b2(T23, W, [X]), T23)
P("      same with Phi* (2 chirals):", r); assert all2(r)
# (e) SM with H only as one chiral (no second doublet)
r = ratios(b2s(SMG, gen(3) + [H]), SM.subs(nG, 3), SMG)
P("   SM -> SUSY with H only (no H_d):", r)
assert r[(1, 2)] == r[(2, 1)] == R(5, 3) and r[(1, 1)] == R(389, 199)
# (f) b_ij cannot tell H^c from a second Y = +1/2 doublet
assert b2s(SMG, gen(3) + [H, H]) == MSSM.subs(nG, 3)
P("   MSSM content with H_d replaced by a second Y=+1/2 doublet chiral: identical b_ij (asserted)")

# ---------------------------------------------------------------- 3. Phi* theorem, random contents
P("\n3. Phi* theorem (two chirals per complex scalar, one per Weyl / real scalar) on 200 random SM-group contents")
random.seed(20261125)
reps = [(1, 1), (2, 1), (1, 3), (2, 3), (3, 1), (1, 8), (3, 3), (2, 8), (3, 8)]
realreps = [(3, 1), (1, 8), (3, 8)]
for _ in range(200):
    Fs = [f(*random.choice(reps), R(random.randint(-6, 6), 6)) for _ in range(random.randint(0, 6))]
    Scs = [f(*random.choice(reps), R(random.randint(-6, 6), 6)) for _ in range(random.randint(0, 4))]
    Srs = [f(*random.choice(realreps), 0) for _ in range(random.randint(0, 3))]
    A = b2s(SMG, Fs + Srs + Scs + Scs)
    B = b2(SMG, Fs, Scs, Srs)
    assert all2(ratios(A, B, SMG))
P("   ratio 2 on every i != j and (1,1): OK (seed 20261125)")

open(__file__.replace(".py", ".txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
