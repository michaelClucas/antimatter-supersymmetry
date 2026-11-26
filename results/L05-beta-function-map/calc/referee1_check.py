"""Referee 1 (cycle 5) independent check of L05 claims (i)-(iii), counterexamples, scheme shift.
Written from the general formulas, not from beta_map.py / c4_doubling.py.
MV (Weyl F, complex scalars Sc, real scalars Sr), convention dg_i/dt = g_i^3/(16pi^2)^2 sum_j b_ij g_j^2:
  b_ij = sum_F (2 S_i C_j + d_ij 10/3 CG S_i) + sum_Sc (4 S_i C_j + d_ij 2/3 CG S_i)
       + sum_Sr (2 S_i C_j + d_ij 1/3 CG S_i) - d_ij 34/3 CG^2
SUSY (Martin-Vaughn / Jones): b_ij = -6 CG^2 d_ij + sum_chiral (4 S_i C_j + 2 CG S_i d_ij)
"""
import random
from sympy import Rational as R, Matrix, symbols, expand, zeros

T2 = {1: 0, 2: R(1, 2), 3: 2}; C2 = {1: 0, 2: R(3, 4), 3: 2}
T3 = {1: 0, 3: R(1, 2), 8: 3}; C3 = {1: 0, 3: R(4, 3), 8: 3}
CG = [0, 2, 3]

def SC(f):
    d2, d3, Y = f
    S = [R(3, 5)*Y**2*d2*d3, T2[d2]*d3, T3[d3]*d2]
    C = [R(3, 5)*Y**2, C2[d2], C3[d3]]
    return S, C

def b_nonsusy(F, Sc, Sr=()):
    b = zeros(3, 3)
    for fl, w, wd in ((F, 2, R(10, 3)), (Sc, 4, R(2, 3)), (Sr, 2, R(1, 3))):
        for f in fl:
            S, C = SC(f)
            for i in range(3):
                for j in range(3):
                    b[i, j] += w*S[i]*C[j] + (wd*CG[i]*S[i] if i == j else 0)
    for i in range(3):
        b[i, i] -= R(34, 3)*CG[i]**2
    return b

def b_susy(Ch):
    b = zeros(3, 3)
    for f in Ch:
        S, C = SC(f)
        for i in range(3):
            for j in range(3):
                b[i, j] += 4*S[i]*C[j] + (2*CG[i]*S[i] if i == j else 0)
    for i in range(3):
        b[i, i] -= 6*CG[i]**2
    return b

def offab(A, B):
    """ratios A/B on off-diagonal entries and (1,1); None where B=0 and A=0"""
    out = {}
    for i in range(3):
        for j in range(3):
            if i != j or i == 0:
                out[(i+1, j+1)] = (A[i, j]/B[i, j]) if B[i, j] != 0 else ('0/0' if A[i, j] == 0 else 'x/0')
    return out

gen = [(2, 3, R(1, 6)), (1, 3, R(-2, 3)), (1, 3, R(1, 3)), (2, 1, R(-1, 2)), (1, 1, 1)]  # Q u^c d^c L e^c
H, Hc = (2, 1, R(1, 2)), (2, 1, R(-1, 2))
SM = b_nonsusy(gen*3, [H])
MSSM = b_susy(gen*3 + [H, Hc])
print("SM b_ij  =", SM.tolist())
print("MSSM b_ij=", MSSM.tolist())
assert SM == Matrix([[R(199, 50), R(27, 10), R(44, 5)], [R(9, 10), R(35, 6), 12], [R(11, 10), R(9, 2), -26]])
assert MSSM == Matrix([[R(199, 25), R(27, 5), R(88, 5)], [R(9, 5), 25, 24], [R(11, 5), 9, 14]])
r = offab(MSSM, SM); print("(i) MSSM/SM off-diag+(1,1):", r); assert set(r.values()) == {2}
print("    diag ratios b22, b33:", MSSM[1, 1]/SM[1, 1], MSSM[2, 2]/SM[2, 2])

# (ii) theorem on random content under Phi*; real scalars only in real reps
random.seed(1)
realreps = [(1, 1, 0), (3, 1, 0), (1, 8, 0), (3, 8, 0)]
anyrep = [(a, b) for a in (1, 2, 3) for b in (1, 3, 8)]
for trial in range(200):
    F = [(*random.choice(anyrep), R(random.randint(-6, 6), 6)) for _ in range(random.randint(0, 6))]
    Sc = [(*random.choice(anyrep), R(random.randint(-6, 6), 6)) for _ in range(random.randint(0, 4))]
    Sr = [random.choice(realreps) for _ in range(random.randint(0, 3))]
    conj = [(a, b, -y) for (a, b, y) in Sc]
    A, B = b_susy(F + Sr + Sc + conj), b_nonsusy(F, Sc, Sr)
    for k, v in offab(A, B).items():
        assert v in (2, '0/0'), (F, Sc, Sr, k, v)
print("(ii) Phi* theorem: ratio 2 on off-diag+(1,1) for 200 random contents: OK")

# counterexamples to 'minimal SUSY = Phi*'
X = (3, 8, 0); W = [(2, 3, 0), (2, 3, 0)]
print("  complex (3,8) real rep, one chiral:", offab(b_susy(W + [X]), b_nonsusy(W, [X])))
twoHDM = b_nonsusy(gen*3, [H, H])  # two Y=+1/2 doublets (equivalently H1, H2^c)
print("  2HDM parent -> MSSM (minimal: one chiral per doublet):", offab(MSSM, twoHDM))
D = (2, 1, R(1, 2)); Dc = (2, 1, R(-1, 2))
print("  vector-like scalar pair (2,1,+-1/2) only, minimal SUSY = 2 chirals:", offab(b_susy([D, Dc]), b_nonsusy([], [D, Dc])))
P0 = (2, 1, 0)
print("  two Y=0 complex doublets (pseudoreal), minimal = 2 chirals (Witten-safe):",
      offab(b_susy([P0, P0]), b_nonsusy([], [P0, P0])))
print("  SM, H only as one chiral (no H_d):", offab(b_susy(gen*3 + [H]), SM))

# (iii) Yukawa, top term y_t Q H u^c: 6 component terms (3 colours x eps). c_i = w * 6 * sum_legs C_i(leg) / d(G_i)
# MV (Weyl): fermion legs only, weight 1; SUSY: all three legs, weight 2.
dG = [1, 3, 8]
def leg(f, i): return 6*SC(f)[1][i]/dG[i]
c_sm = [leg(gen[0], i) + leg(gen[1], i) for i in range(3)]
c_su = [2*(leg(gen[0], i) + leg(gen[1], i) + leg(H, i)) for i in range(3)]
print("(iii) top: SM", c_sm, " MSSM", c_su, " MSSM-2SM", [c_su[i] - 2*c_sm[i] for i in range(3)])
assert all(abs(float(a-b))<1e-12 for a,b in zip(c_sm+c_su,[R(17,10),R(3,2),2,R(26,5),6,4]))  # float from sympy/py mix, values exact
P8 = (2, 8, 0)  # pseudoreal; one chiral has 8 doublets -> Witten-safe, SU(3)^3-safe: minimal = 1 chiral
print("  complex (2,8,0) pseudoreal, minimal = one chiral, with Weyl (2,3)x2:", offab(b_susy(W + [P8]), b_nonsusy(W, [P8])))
# scheme: does a diagonal rescaling g -> g(1+k g^2) shift the diagonal 3-loop coefficient?
g, G, k, b1, b2, b3, e = symbols("g G k b1 b2 b3 e")
beta = e*b1*g**3 + e**2*b2*g**5 + e**3*b3*g**7
g_of = G - e*k*G**3 + 3*e**2*k**2*G**5 - 12*e**3*k**3*G**7
bp = expand(((1 + 3*e*k*g**2)*beta).subs(g, g_of))
print("scheme: new 2-loop", expand(bp.coeff(e, 2)).coeff(G, 5), "; shift of 3-loop diag coeff:",
      expand(bp.coeff(e, 3)).coeff(G, 7) - b3)
# mixed two-loop-order redefinition g_i -> g_i(1 + k g_i^2 g_j^2): shift of c_i(jj)
gi, gj, Gi, bi, bj, bij = symbols("g_i g_j G_i b_i b_j b_ij")
bi_ = e*bi*gi**3 + e**2*bij*gi**3*gj**2
gi_of = Gi - e**2*k*Gi**3*gj**2
bpi = expand((bi_ + e**2*k*(3*gi**2*gj**2*bi_ + 2*gi**3*gj*(e*bj*gj**3))).subs(gi, gi_of))
print("mixed 2-loop redefinition: 3-loop shift coeff of G_i^3 g_j^4:", expand(bpi.coeff(e, 3)).coeff(Gi, 3).coeff(gj, 4),
      "; of G_i^5 g_j^2:", expand(bpi.coeff(e, 3)).coeff(Gi, 5).coeff(gj, 2))

