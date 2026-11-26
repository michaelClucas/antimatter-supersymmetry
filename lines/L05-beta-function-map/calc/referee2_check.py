# Referee 2 independent check of L05 CLAIM (a)-(c). Exact sympy rationals.
# Formulas (written from Machacek-Vaughn NPB 222 (1983) 83 and Martin-Vaughn hep-ph/9311340 eq. (2.x)):
#  non-SUSY, per field, b_ij (dg_i/dt = g_i^3/(16pi^2)^2 sum_j b_ij g_j^2):
#    Weyl: 2 S_i C_j + d_ij C(G_i) (10/3) S_i ; complex scalar: 4 S_i C_j + d_ij C(G_i)(2/3) S_i ;
#    real scalar: half a complex scalar ; gauge: -34/3 C(G_i)^2 d_ij
#  SUSY: per chiral 4 S_i C_j + 2 d_ij C(G_i) S_i ; vector multiplet -6 C(G_i)^2 d_ij
# Published tables typed in by referee 2 directly from the arXiv TeX sources fetched 2026-11-25.
from sympy import Rational as R, symbols, simplify, Matrix
import random

n = symbols('n')

# group data: list of ('U1', None) or ('SU', N)
def CG(g):
    return 0 if g[0] == 'U1' else g[1]

# rep data for SU(N): dim -> (T, C)
def suN(N, d):
    tab = {1: (0, 0), N: (R(1, 2), R(N*N-1, 2*N)), N*N-1: (N, N)}
    if N == 2:
        tab[3] = (2, 2); tab[4] = (5, R(15, 4))
    if N == 3:
        tab[6] = (R(5, 2), R(10, 3))
    return tab[d]

def SC(groups, rep):
    """rep = list per factor: dim for SU(N), hypercharge Y for U1 (GUT norm 3/5 Y^2). returns S_i, C_i lists"""
    dims, T, C = [], [], []
    for g, r in zip(groups, rep):
        if g[0] == 'U1':
            dims.append(1); T.append(R(3, 5)*r**2); C.append(R(3, 5)*r**2)
        else:
            t, c = suN(g[1], r); dims.append(r); T.append(t); C.append(c)
    tot = 1
    for d in dims: tot *= d
    S = [R(T[i])*R(tot, dims[i]) for i in range(len(groups))]
    return S, C

def bnon(groups, F=(), Sc=(), Sr=()):
    k = len(groups); b = Matrix.zeros(k, k)
    for i in range(k):
        b[i, i] += -R(34, 3)*CG(groups[i])**2
    for lst, w, wd in ((F, 2, R(10, 3)), (Sc, 4, R(2, 3)), (Sr, 2, R(1, 3))):
        for (rep, mult) in lst:
            S, C = SC(groups, rep)
            for i in range(k):
                for j in range(k):
                    b[i, j] += mult*w*S[i]*C[j]
                b[i, i] += mult*wd*CG(groups[i])*S[i]
    return b

def bsusy(groups, Ch):
    k = len(groups); b = Matrix.zeros(k, k)
    for i in range(k):
        b[i, i] += -6*CG(groups[i])**2
    for (rep, mult) in Ch:
        S, C = SC(groups, rep)
        for i in range(k):
            for j in range(k):
                b[i, j] += mult*4*S[i]*C[j]
            b[i, i] += mult*2*CG(groups[i])*S[i]
    return b

def ratios(A, B, groups):
    out = {}
    for i in range(len(groups)):
        for j in range(len(groups)):
            if i != j or groups[i][0] == 'U1':
                out[(i+1, j+1)] = 'n/a' if B[i, j] == 0 and A[i, j] == 0 else simplify(A[i, j]/B[i, j])
    return out

SMG = [('U1', None), ('SU', 2), ('SU', 3)]
gen = lambda m: [([R(1, 6), 2, 3], m), ([R(-2, 3), 1, 3], m), ([R(1, 3), 1, 3], m), ([R(-1, 2), 2, 1], m), ([1, 1, 1], m)]
H = ([R(1, 2), 2, 1], 1); Hc = ([R(-1, 2), 2, 1], 1)

SM = bnon(SMG, gen(n), [H]); MSSM = bsusy(SMG, gen(n) + [H, Hc])
print("SM b_ij(n_G):", SM.applyfunc(lambda x: x.expand()))
print("MSSM b_ij(n_G):", MSSM.applyfunc(lambda x: x.expand()))

# ---- published tables (referee 2 read them from TeX: MSS eq.(5) rows; MV eq. (4.5); FJJ b_ij)
MSS = 16*Matrix([[R(9, 800)+19*n/240, R(9, 160)+3*n/80, 11*n/60],
                 [R(3, 160)+n/80, -R(259, 96)+49*n/48, n/4],
                 [11*n/480, 3*n/32, -R(51, 8)+19*n/12]])
MV = Matrix([[R(199, 25), R(27, 5), R(88, 5)], [R(9, 5), 25, 24], [R(11, 5), 9, 14]])
FJJ = Matrix([[R(38, 15)*n+R(9, 25), R(6, 5)*n+R(9, 5), R(88, 15)*n],
              [R(2, 5)*n+R(3, 5), 14*n-17, 8*n], [R(11, 15)*n, 3*n, R(68, 3)*n-54]])
assert (SM-MSS).expand() == Matrix.zeros(3, 3)
assert (MSSM-FJJ).expand() == Matrix.zeros(3, 3)
assert MSSM.subs(n, 3) == MV
for nm, A, B in (("FJJ/MSS all n", FJJ, MSS), ("MV/MSS n=3", MV, MSS.subs(n, 3))):
    r = ratios(A, B, SMG); print(nm, r); assert all(v == 2 for v in r.values())
print("diag (2,2),(3,3) at n=3:", MV[1, 1]/MSS.subs(n, 3)[1, 1], MV[2, 2]/MSS.subs(n, 3)[2, 2])

# ---- counterexamples
def show(name, A, B, groups):
    r = ratios(A, B, groups); print(name, r); return r
r = show("2HDM->MSSM", MSSM.subs(n, 3), bnon(SMG, gen(3), [([R(1, 2), 2, 1], 2)]), SMG)
assert r[(1, 2)] == r[(2, 1)] == R(3, 2) and r[(1, 1)] == R(199, 104)
r = show("no H_d", bsusy(SMG, gen(3)+[H]), bnon(SMG, gen(3), [H]), SMG)
assert r[(1, 2)] == R(5, 3) and r[(1, 1)] == R(389, 199)
r = show("H_d -> 2nd Y=+1/2", bsusy(SMG, gen(3)+[H, H]), MSSM.subs(n, 3), SMG)
assert all(v == 1 for v in r.values())
r = show("VL scalar pair", bsusy(SMG, [H, Hc]), bnon(SMG, [], [H, Hc]), SMG)
T23 = [('SU', 2), ('SU', 3)]; W = [([2, 3], 2)]
r = show("(2,8) 1 chiral", bsusy(T23, W+[([2, 8], 1)]), bnon(T23, W, [([2, 8], 1)]), T23); assert r[(1, 2)] == R(8, 7)
r = show("(3,8) 1 chiral", bsusy(T23, W+[([3, 8], 1)]), bnon(T23, W, [([3, 8], 1)]), T23); assert r[(1, 2)] == R(26, 25)
# extra: one-doublet parent with an extra complex scalar in the real rep (8,3,0); minimal SUSY = one chiral (anomaly-free alone). (1,3,0) alone gives no off-diagonal entry.
r = show("SM+complex (8,3,0), minimal SUSY", bsusy(SMG, gen(3)+[H, Hc, ([0, 3, 8], 1)]),
         bnon(SMG, gen(3), [H, ([0, 3, 8], 1)]), SMG)
assert r[(1, 2)] == 2 and r[(2, 3)] != 2
# T_dbl: SM + independent conjugate of every Weyl and of H
Td = bnon(SMG, gen(6), [([R(1, 2), 2, 1], 2)])
print("T_dbl diag:", Td[1, 1], Td[2, 2]); r = ratios(MSSM.subs(n, 3), Td, SMG); assert all(v == 1 for v in r.values())

# ---- theorem on random theories with up to 4 factors incl. SU(2),SU(3),SU(4), one U(1), real scalars
random.seed(7)
for trial in range(300):
    groups = [('U1', None)] + random.sample([('SU', 2), ('SU', 3), ('SU', 4)], random.randint(1, 3))
    def rrep():
        rep = [random.choice([0, R(1, 2), R(-1, 3), 1, R(2, 3)])]
        for g in groups[1:]:
            rep.append(random.choice([1, g[1], g[1]**2-1] + ([3, 4] if g[1] == 2 else []) + ([6] if g[1] == 3 else [])))
        return rep
    F = [(rrep(), 1) for _ in range(random.randint(0, 5))]
    Sc = [(rrep(), 1) for _ in range(random.randint(0, 3))]
    Sr = []
    for _ in range(random.randint(0, 2)):   # real scalar: real rep, Y = 0 (adjoints / singlets / SU(2) triplet)
        rep = [0] + [random.choice([1, g[1]**2-1]) for g in groups[1:]]
        Sr.append((rep, 1))
    P = bsusy(groups, F + [(rp, 2*m) for rp, m in Sc] + Sr)
    T = bnon(groups, F, Sc, Sr)
    for k, v in ratios(P, T, groups).items():
        assert v == 2 or v == 'n/a', (trial, k, v)
print("Phi* theorem: 300 random theories, ratio 2 on all i!=j and abelian diag: OK")

# ---- three-loop: scheme-invariance of c_i(ij) and fully-mixed c_i(jk), checked symbolically
g1, g2, g3, t = symbols('g1 g2 g3 t')
k1, k2, k3, a1, m12, m13 = symbols('k1 k2 k3 a1 m12 m13')
bb = symbols('b1:4'); B = Matrix(3, 3, symbols('B11:14 B21:24 B31:34')); c = symbols('c111 c112 c113 c122 c123 c133')
gs = [g1, g2, g3]
def beta(i, g):
    s = bb[i]*g[i]**3 + g[i]**3*sum(B[i, j]*g[j]**2 for j in range(3))
    if i == 0:
        s += g1**3*(c[0]*g1**4 + c[1]*g1**2*g2**2 + c[2]*g1**2*g3**2 + c[3]*g2**4 + c[4]*g2**2*g3**2 + c[5]*g3**4)
    return s
G1 = g1 + k1*g1**3 + a1*g1**5 + m12*g1**3*g2**2 + m13*g1**3*g3**2
G2 = g2 + k2*g2**3; G3 = g3 + k3*g3**3
from sympy import diff, series, expand, Poly
eps = symbols('eps')
dG1 = sum(diff(G1, gs[i])*beta(i, gs) for i in range(3))   # only need beta_1 to 3 loops; beta_2,3 to 2 loops is enough at this order
# invert to order g^7: g1 = G1 - k1 G1^3 + ..., done by series in eps scaling
Gs = symbols('G1 G2 G3')
inv1 = Gs[0] - k1*Gs[0]**3 + (3*k1**2 - a1)*Gs[0]**5 - m12*Gs[0]**3*Gs[1]**2 - m13*Gs[0]**3*Gs[2]**2
inv2 = Gs[1] - k2*Gs[1]**3; inv3 = Gs[2] - k3*Gs[2]**3
sc = {Gs[0]: eps*Gs[0], Gs[1]: eps*Gs[1], Gs[2]: eps*Gs[2]}
e = expand(dG1.subs({g1: inv1.subs(sc, simultaneous=True), g2: inv2.subs(sc, simultaneous=True), g3: inv3.subs(sc, simultaneous=True)}, simultaneous=True))
e7 = e.coeff(eps, 7)
P7 = Poly(expand(e7), *Gs)
G1_, G2_, G3_ = Gs
for mono, name in (((5, 2, 0), 'c1(12)'), ((3, 2, 2), 'c1(23)'), ((5, 0, 2), 'c1(13)'), ((3, 4, 0), 'c1(22)'), ((7, 0, 0), 'c1(11)')):
    print(name, "new coefficient:", simplify(P7.coeff_monomial(G1_**mono[0]*G2_**mono[1]*G3_**mono[2])))

# ---- three-loop invariant entries from MSS (x64) and FJJ, n_G-linear parts
SMc = {'c1(23)': -R(64, 320), 'c2(13)': -R(64, 960), 'c3(12)': -R(64, 2560), 'c1(12)': -R(64*7, 6400),
       'c1(13)': -R(64*137, 14400), 'c2(21)': R(64*13, 1280), 'c2(23)': 13, 'c3(31)': R(64*77, 2880), 'c3(32)': 7}
SUc = {'c1(23)': -R(8, 5), 'c2(13)': -R(8, 15), 'c3(12)': -R(1, 5), 'c1(12)': -R(14, 25), 'c1(13)': -R(1096, 225),
       'c2(21)': R(2, 5), 'c2(23)': 8, 'c3(31)': R(22, 45), 'c3(32)': 2}
print("3-loop n_G-linear MSSM/SM:", {k: SUc[k]/SMc[k] for k in SMc})
