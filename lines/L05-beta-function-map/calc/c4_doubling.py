"""
L05 cycle 4: analytic derivation and generality test of the two-loop doubling identity
  b_ij[Phi(T)] = 2 b_ij[T]   (i != j, and i = j abelian)

Conventions (same as beta_map.py):
  dg_i/dt = g_i^3/(16pi^2) b_i + g_i^3/(16pi^2)^2 [ sum_j b_ij g_j^2 - sum_f c_i^f y_f^2 ] + g_i^3/(16pi^2)^3 [3-loop]
  S_i(X) = Dynkin index of X under G_i times dim of X under the other factors
  C_i(X) = quadratic Casimir of X under G_i (U(1): C = q^2, S = q^2 * dim)

Two-loop component formula (Machacek-Vaughn NPB 222 (1983) 83, product-group form), Weyl fermions F,
complex scalars S_c, real scalars S_r:
  b_ij = delta_ij [ -34/3 C(G_i)^2 + 10/3 C(G_i) sum_F S_i + 2/3 C(G_i) sum_Sc S_i + 1/3 C(G_i) sum_Sr S_i ]
         + 2 sum_F S_i C_j + 4 sum_Sc S_i C_j + 2 sum_Sr S_i C_j
  Yukawa: c_i = (1/d(G_i)) sum over Yukawa component triples |Y|^2 * (C_i of the two FERMION legs)
Checked below against the SM matrix and n_G dependence of Mihaila-Salomon-Steinhauser (arXiv:1201.5868, eq. 5,
read from the arXiv TeX source).

SUSY formula (Jones PRD 25 (1982) 581; Martin-Vaughn hep-ph/9311340):
  b_ij = -6 C(G_i)^2 delta_ij + sum_chiral S_i [ 4 C_j + 2 C(G_i) delta_ij ]
  c_i = (1/d(G_i)) Y^{ijk}Y_{ijk} C(k)   (all three legs)
Checked below against Ferreira-Jack-Jones hep-ph/9605440 eq. (b_ij with general n_g, read from TeX source).

Run: python c4_doubling.py  (output c4_doubling.txt)
"""
from sympy import Rational as R, Matrix, symbols, simplify, expand, zeros, Poly

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

# ---------------------------------------------------------------------------
# 0. Symbolic per-multiplet weights (the derivation)
# ---------------------------------------------------------------------------
P("0. Symbolic derivation: contribution of one field X (indices S_i, C_j) to b_ij, plus delta_ij pieces with C(G_i)=CG")
Si, Cj, CG, d = symbols("S_i C_j CG delta")
weyl = 2*Si*Cj + d*R(10, 3)*CG*Si
cscal = 4*Si*Cj + d*R(2, 3)*CG*Si
rscal = 2*Si*Cj + d*R(1, 3)*CG*Si
# gaugino-matter-scalar Yukawa  -sqrt2 g_j phi^* T^a psi lambda_j^a : sum|Y|^2 = 2 g_j^2 d(R) C_j(R);
# MV Yukawa term weights the two fermion legs psi (C_i(R)) and lambda_j (C_i(adj_j) = delta_ij CG)
gaugino_yuk = -(2*Si*Cj + d*2*CG*Si)
chiral_components = expand(weyl + cscal + gaugino_yuk)
chiral_susy = 4*Si*Cj + d*2*CG*Si
P("   Weyl fermion        :", weyl)
P("   complex scalar      :", cscal)
P("   real scalar         :", rscal)
P("   gaugino Yukawa      :", gaugino_yuk)
P("   chiral (components) :", chiral_components)
P("   chiral (SUSY form)  :", chiral_susy)
assert simplify(chiral_components - chiral_susy) == 0
# vector multiplet: gauge -34/3 CG^2 + Majorana adjoint Weyl (S=CG, C=CG): (2 + 10/3) CG^2 = 16/3 CG^2
vec = -R(34, 3)*CG**2 + R(16, 3)*CG**2
assert vec == -6*CG**2
P("   vector multiplet    :", vec, " (= -34/3 + 16/3 for the Majorana gaugino)")
P("   off-diagonal (delta=0): chiral/Weyl = 2, (2 chiral)/(complex scalar) = 2, chiral/(real scalar) = 2")
assert chiral_susy.subs(d, 0) == 2*weyl.subs(d, 0)
assert 2*chiral_susy.subs(d, 0) == 2*cscal.subs(d, 0)
assert chiral_susy.subs(d, 0) == 2*rscal.subs(d, 0)
P("   one chiral per complex scalar gives ratio", chiral_susy.subs(d, 0)/cscal.subs(d, 0), "(doubling FAILS)")

# ---------------------------------------------------------------------------
# Generic machinery
# ---------------------------------------------------------------------------
class Theory:
    """groups: list of (name, CG, dimG, abelian). Fields: dict name -> list over groups of (dim, S, C)."""
    def __init__(self, groups):
        self.g = groups
        self.n = len(groups)
    def rep(self, dims_idx):
        """dims_idx: list over groups of (dim_i, T_i, C_i) for the rep under each factor separately.
        Returns list of (S_i, C_i) with S_i = T_i * prod_{k!=i} dim_k."""
        res = []
        for i in range(self.n):
            dim_i, T_i, C_i = dims_idx[i]
            mult = 1
            for k in range(self.n):
                if k != i:
                    mult *= dims_idx[k][0]
            res.append((T_i*mult, C_i))
        return res

def b1(th, weyls, cs, rs=(), susy=False, chirals=()):
    v = []
    for i, (nm, CGi, dG, ab) in enumerate(th.g):
        if susy:
            v.append(-3*CGi + sum(x[i][0] for x in chirals))
        else:
            v.append(-R(11, 3)*CGi + R(2, 3)*sum(x[i][0] for x in weyls)
                     + R(1, 3)*sum(x[i][0] for x in cs) + R(1, 6)*sum(x[i][0] for x in rs))
    return Matrix(v)

def b2_mv(th, weyls, cs, rs=()):
    n = th.n; M = zeros(n, n)
    for i, (nm, CGi, dG, ab) in enumerate(th.g):
        for j in range(n):
            v = 2*sum(x[i][0]*x[j][1] for x in weyls) + 4*sum(x[i][0]*x[j][1] for x in cs) \
                + 2*sum(x[i][0]*x[j][1] for x in rs)
            if i == j:
                v += -R(34, 3)*CGi**2 + R(10, 3)*CGi*sum(x[i][0] for x in weyls) \
                     + R(2, 3)*CGi*sum(x[i][0] for x in cs) + R(1, 3)*CGi*sum(x[i][0] for x in rs)
            M[i, j] = v
    return M

def b2_susy(th, chirals):
    n = th.n; M = zeros(n, n)
    for i, (nm, CGi, dG, ab) in enumerate(th.g):
        for j in range(n):
            v = 4*sum(x[i][0]*x[j][1] for x in chirals)
            if i == j:
                v += -6*CGi**2 + 2*CGi*sum(x[i][0] for x in chirals)
            M[i, j] = v
    return M

def b2_susy_components(th, chirals):
    """components: Weyl + complex scalar per chiral, Majorana adjoint gaugino, gaugino Yukawas"""
    n = th.n
    gauginos = []
    for k, (nm, CGk, dG, ab) in enumerate(th.g):
        if CGk == 0 and ab:
            # U(1) gaugino: neutral singlet, S = C = 0 everywhere
            gauginos.append([(0, 0)]*n)
        else:
            rep = []
            for i in range(n):
                rep.append((CGk, CGk) if i == k else (0, 0))  # S_i = CG_i * dim(other)=1 ; C_i = CG_i on its own factor
            gauginos.append(rep)
    M = b2_mv(th, list(chirals) + gauginos, list(chirals))
    for i, (nm, CGi, dG, ab) in enumerate(th.g):
        for j in range(n):
            M[i, j] += -2*sum(x[i][0]*x[j][1] for x in chirals)
            if i == j:
                M[i, j] += -2*CGi*sum(x[i][0] for x in chirals)
    return M

def offdiag_ratio(A, Bm, th):
    rows = []
    for i in range(th.n):
        for j in range(th.n):
            if i != j or th.g[i][3]:
                rows.append(((i+1, j+1), A[i, j], Bm[i, j], (A[i, j]/Bm[i, j]) if Bm[i, j] != 0 else ("0=0" if A[i, j] == 0 else "inf")))
    return rows

# ---------------------------------------------------------------------------
# 1. SM and MSSM, with general n_G, checked against MSS and FJJ
# ---------------------------------------------------------------------------
P("\n1. SM / MSSM two-loop gauge matrices with general n_G (checks against literature)")
nG = symbols("n_G")
th = Theory([("U1", 0, 1, True), ("SU2", 2, 3, False), ("SU3", 3, 8, False)])
def U1(Y):  # GUT-normalised
    return R(3, 5)*Y**2
def f(d2, d3, Y):
    T2 = {1: 0, 2: R(1, 2)}[d2]; C2 = {1: 0, 2: R(3, 4)}[d2]
    T3 = {1: 0, 3: R(1, 2)}[d3]; C3 = {1: 0, 3: R(4, 3)}[d3]
    return th.rep([(1, U1(Y), U1(Y)), (d2, T2, C2), (d3, T3, C3)])
Q, uc, dc, L, ec = f(2, 3, R(1, 6)), f(1, 3, R(-2, 3)), f(1, 3, R(1, 3)), f(2, 1, R(-1, 2)), f(1, 1, 1)
H, Hc = f(2, 1, R(1, 2)), f(2, 1, R(-1, 2))
gen = [Q, uc, dc, L, ec]
def scale(rep, k):
    return [(s*k, c) for (s, c) in rep]
matter_n = [scale(x, nG) for x in gen]  # n_G copies (indices linear in multiplicity)

SM2 = b2_mv(th, matter_n, [H])
MS2 = b2_susy(th, matter_n + [H, Hc])
MS2c = b2_susy_components(th, matter_n + [H, Hc])
assert (MS2 - MS2c).expand() == zeros(3, 3)
P("   SM b_ij(n_G)   =", [[expand(x) for x in SM2.row(i)] for i in range(3)])
P("   MSSM b_ij(n_G) =", [[expand(x) for x in MS2.row(i)] for i in range(3)])
# Mihaila-Salomon-Steinhauser 1201.5868 eq.(5): two-loop coeffs of (alpha_j/pi) in beta_i = mu^2 d(alpha_i/pi)/dmu^2,
# b_ij = 16 * coefficient
MSS2 = 16*Matrix([[R(9, 800)+19*nG/240, R(9, 160)+3*nG/80, 11*nG/60],
                  [R(3, 160)+nG/80, -R(259, 96)+49*nG/48, nG/4],
                  [11*nG/480, 3*nG/32, -R(51, 8)+19*nG/12]])
assert (SM2 - MSS2).expand() == zeros(3, 3)
P("   SM matrix == 16 x MSS 1201.5868 eq.(5) two-loop coefficients, for all n_G: OK")
FJJ2 = Matrix([[R(38, 15)*nG+R(9, 25), R(6, 5)*nG+R(9, 5), R(88, 15)*nG],
               [R(2, 5)*nG+R(3, 5), 14*nG-17, 8*nG],
               [R(11, 15)*nG, 3*nG, R(68, 3)*nG-54]])
assert (MS2 - FJJ2).expand() == zeros(3, 3)
P("   MSSM matrix == Ferreira-Jack-Jones hep-ph/9605440 b_ij(n_g), for all n_g: OK")
D = (MS2 - 2*SM2).expand()
P("   MSSM - 2 SM (all n_G) =", D.tolist())
for i in range(3):
    for j in range(3):
        if i != j or i == 0:
            assert D[i, j] == 0
P("   => off-diagonal and (1,1) doubling holds identically in n_G (term by term: matter part and Higgs part separately)")
P("   diagonal remainder (2,2), (3,3):", D[1, 1], ",", D[2, 2])

# Split SM off-diagonal into fermion part and Higgs part, and show the H^c role
SMf = b2_mv(th, matter_n, [])
SMh = b2_mv(th, [], [H]) - b2_mv(th, [], [])
MSf = b2_susy(th, matter_n) - b2_susy(th, [])
MSh1 = b2_susy(th, [H]) - b2_susy(th, [])
MSh2 = b2_susy(th, [H, Hc]) - b2_susy(th, [])
P("   off-diag Higgs part: SM (one complex doublet) =", [SMh[0, 1], SMh[1, 0]],
  "; one chiral H =", [MSh1[0, 1], MSh1[1, 0]], "; chiral H + H^c =", [MSh2[0, 1], MSh2[1, 0]])
assert MSh2[0, 1] == 2*SMh[0, 1] and MSh1[0, 1] == SMh[0, 1]
# second doublet with SAME hypercharge also doubles (S, C identical) -> doubling is conjugation-blind
H2 = f(2, 1, R(1, 2))
MSh2b = b2_susy(th, [H, H2]) - b2_susy(th, [])
assert MSh2b[0, 1] == MSh2[0, 1] and MSh2b[1, 0] == MSh2[1, 0]
P("   H + (second Y=+1/2 doublet) gives the same off-diagonal numbers as H + H^c: the identity sees only (S_i, C_j),")
P("   which are invariant under R -> conj(R). The conjugate is selected by higgsino anomaly cancellation, not by b_ij.")
# ratios without H^c (Phi without the conjugate step), n_G = 3
noHc = b2_susy(th, [scale(x, 3) for x in gen] + [H])
SM3 = SM2.subs(nG, 3)
P("   n_G=3, Phi without H^c: off-diagonal ratios MSSM'/SM =",
  [(i+1, j+1, noHc[i, j]/SM3[i, j]) for i in range(3) for j in range(3) if (i != j or i == 0) and SM3[i, j] != 0])

# Diagonal condition
P("   non-abelian diagonal doubles iff 25 C(G) = 7 sum_F S - 4 sum_Sc S (from -6C^2+2C(SF+2Sc) = 2(-34/3 C^2 + 10/3 C SF + 2/3 C Sc))")
for i, nm in [(1, "SU2"), (2, "SU3")]:
    SF = sum(x[i][0] for x in [scale(y, 3) for y in gen]); Sc = H[i][0]
    P(f"     {nm}: 25C = {25*th.g[i][1]},  7 S_F - 4 S_c = {7*SF - 4*Sc}")

# ---------------------------------------------------------------------------
# 2. Yukawa (gauge-Yukawa) part
# ---------------------------------------------------------------------------
P("\n2. Two-loop Yukawa coefficients c_i (full result)")
# component triples: y_t Q H u^c : 3 colours x (2 SU(2) eps components) = 6
def c_sm(legs_f, N):
    return [R(N)*sum(l[i][1] for l in legs_f)/th.g[i][2] for i in range(3)]
def c_susy(legs, N):
    return [2*R(N)*sum(l[i][1] for l in legs)/th.g[i][2] for i in range(3)]
for nm, (a, b_, h, N) in {"t": (Q, uc, H, 6), "b": (Q, dc, Hc, 6), "tau": (L, ec, Hc, 2)}.items():
    cs_, cm = c_sm([a, b_], N), c_susy([a, b_, h], N)
    hl = [2*R(N)*h[i][1]/th.g[i][2] for i in range(3)]
    P(f"   y_{nm}: SM {cs_}  MSSM {cm}  MSSM - 2 SM = {[cm[i]-2*cs_[i] for i in range(3)]} = Higgs-leg term {hl}")
    assert all(cm[i] - 2*cs_[i] == hl[i] for i in range(3))
assert c_susy([Q, uc, H], 6) == [R(26, 5), 6, 4] and c_susy([Q, dc, Hc], 6) == [R(14, 5), 6, 4] \
    and c_susy([L, ec, Hc], 2) == [R(18, 5), 2, 0]
P("   MSSM a_i match FJJ hep-ph/9605440 (26/5,6,4)trT, (14/5,6,4)trB, (18/5,2,0)trE: OK")
P("   => fermion legs double exactly; the Higgs leg (absent in non-SUSY two-loop Yukawa term) is extra. c_3 doubles")
P("      because the Higgs is colourless. Full b_ij g_j^2 - c y^2 does NOT double unless the Higgs-leg term is dropped.")
P("      (Also y_f^MSSM = y_f^SM / sin(beta) or cos(beta), so even c_3 y^2 is not 2x numerically.)")

# ---------------------------------------------------------------------------
# 3. Antimatter phrasing: SM (+) CP-conjugate copy as independent fields
# ---------------------------------------------------------------------------
P("\n3. Antimatter phrasing tests (n_G = 3)")
def conj(rep):
    return rep  # S_i, C_i invariant under R -> conj(R); hypercharge flips sign, squared
m3 = [scale(x, 3) for x in gen]
SMd2 = b2_mv(th, m3 + [conj(x) for x in m3], [H, conj(H)])
MS3 = MS2.subs(nG, 3)
P("   A. T_dbl = SM matter + Higgs and an independent CP-conjugate copy of each (vector-like doubling, gauge fields once)")
P("      b_ij(T_dbl) =", SMd2.tolist())
P("      MSSM b_ij   =", MS3.tolist())
P("      equal entries:", [(i+1, j+1) for i in range(3) for j in range(3) if SMd2[i, j] == MS3[i, j]])
assert all(SMd2[i, j] == MS3[i, j] for i in range(3) for j in range(3) if i != j or i == 0)
SMd1 = b1(th, m3 + [conj(x) for x in m3], [H, conj(H)])
MS1 = b1(th, None, None, susy=True, chirals=m3 + [H, Hc])
P("      one loop: b(T_dbl) =", list(SMd1), " b(MSSM) =", list(MS1))
P("      one-loop b_2, b_3 coincide: condition 2C(G) = sum_F S - 4 sum_Sc S [T_dbl vs MSSM]:",
  [(nm, 2*th.g[i][1], sum(x[i][0] for x in m3) - 4*H[i][0]) for i, nm in [(1, "SU2"), (2, "SU3")]])
P("      -> holds for SU(2), SU(3) only because n_G = 3 (SU(3): 6 = 2 n_G; SU(2): 4 = 2 n_G - 2); b_1 differs (41/5 vs 33/5).")
P("   B. per-state form: each Weyl field = particle states (R,h=-1/2) + antiparticle states (conj R,h=+1/2), weight 1 each;")
P("      each complex scalar = particle + antiparticle states, weight 2 each. b_ij(off) = sum_states w S_i C_j.")
P("      MSSM chiral multiplet: 1+1 (fermion) + 2+2 (scalar) - 2 (gaugino Yukawa) = 4 = 2 x (Weyl 1+1).")
P("      So off-diagonal MSSM = SM with each state's weight doubled, equivalently SM states + CP-conjugate states counted")
P("      as independent fields (test A). Content: S, C are CPT-blind, so 'conjugate copy' = 'any copy'.")

# ---------------------------------------------------------------------------
# 4. Generality
# ---------------------------------------------------------------------------
P("\n4. Generality tests")
def test(name, thx, weyls, cs, rs, chirals, note=""):
    A = b2_susy(thx, chirals); B_ = b2_mv(thx, weyls, cs, rs)
    assert (A - b2_susy_components(thx, chirals)).expand() == zeros(thx.n, thx.n)
    rows = offdiag_ratio(A, B_, thx)
    diag = [(i+1, A[i, i], B_[i, i]) for i in range(thx.n) if not thx.g[i][3]]
    P(f"   {name}: {note}")
    P(f"      off-diag/abelian (i,j, SUSY, nonSUSY, ratio): {rows}")
    P(f"      non-abelian diag (i, SUSY, nonSUSY): {diag}")
    return rows

# (a) SM with n_H Higgs doublets (all Y=+1/2), Phi*: each doublet -> H_k + H_k^c
for nH in [0, 1, 2]:
    rows = test(f"SM, n_H={nH}", th, m3, [H]*nH, [], m3 + [H, Hc]*nH, "Phi*: each complex doublet -> two chirals")
    assert all(r[3] == 2 for r in rows if r[3] not in ("0=0",))
# (b) SU(5) 3x(5bar+10) + 5_H (+ real 24_H): simple group -> only diagonal
th5 = Theory([("SU5", 5, 24, False)])
def r5(T, C):
    return [(T, C)]
five, ten, adj = r5(R(1, 2), R(12, 5)), r5(R(3, 2), R(18, 5)), r5(5, 5)
test("SU(5) GUT: 3(5bar+10) + 5_H + real 24_H", th5, [scale(five, 3), scale(ten, 3)], [five], [adj],
     [scale(five, 3), scale(ten, 3), five, five, adj], "Phi*: 5_H -> 5_H + 5bar_H ; real 24_H -> one chiral 24")
P("      (simple group: no off-diagonal entries; diagonal is not doubled, as for SU(2), SU(3) in the SM)")
# (c) toy SU(2)xU(1): vector-like leptons + complex scalars
tht = Theory([("U1", 0, 1, True), ("SU2", 2, 3, False)])
def ft(d2, q):
    T2 = {1: 0, 2: R(1, 2), 3: 2}[d2]; C2 = {1: 0, 2: R(3, 4), 3: 2}[d2]
    return tht.rep([(1, q**2, q**2), (d2, T2, C2)])
wt = [ft(2, R(1, 2)), ft(2, -R(1, 2)), ft(1, 1), ft(1, -1)]
sc = [ft(2, R(1, 2)), ft(3, 1)]
rows = test("toy SU(2)xU(1), Weyl (2,+-1/2),(1,+-1); complex scalars (2,1/2),(3,1)", tht, wt, sc, [],
            wt + [ft(2, R(1, 2)), ft(2, -R(1, 2)), ft(3, 1), ft(3, -1)], "Phi*")
assert all(r[3] == 2 for r in rows)
# (d) counterexample: complex scalar in a REAL rep where minimal SUSY needs only one chiral multiplet
th23 = Theory([("SU2", 2, 3, False), ("SU3", 3, 8, False)])
X = th23.rep([(3, 2, 2), (8, 3, 3)])  # (3,8) real rep
wq = [th23.rep([(2, R(1, 2), R(3, 4)), (3, R(1, 2), R(4, 3))]), th23.rep([(2, R(1, 2), R(3, 4)), (3, R(1, 2), R(4, 3))])]
rows_min = test("toy SU(2)xSU(3), Weyl 2x(2,3) [+conj implied], complex scalar (3,8): MINIMAL SUSY (one chiral (3,8))",
                th23, wq, [X], [], wq + [X])
rows_phi = test("same, Phi* (two chirals (3,8))", th23, wq, [X], [], wq + [X, X])
assert any(r[3] != 2 for r in rows_min) and all(r[3] == 2 for r in rows_phi)
rows_real = test("same but scalar is REAL (3,8): minimal SUSY = one chiral", th23, wq, [], [X], wq + [X])
assert all(r[3] == 2 for r in rows_real)

P("\n   THEOREM (two loops, gauge part, any gauge group G = prod G_i, any matter): let T have Weyl fermions F,")
P("   complex scalars S_c, real scalars S_r. Let Phi*(T) = vector multiplets for each G_i + chiral multiplets")
P("   F u S_r u {s, s' : s in S_c} with s' any rep having the same (S_i, C_j) as s (e.g. conj(s)). Then")
P("   b_ij[Phi*(T)] = 2 b_ij[T] for all i != j and for every abelian i = j. Proof: per-field weights of section 0;")
P("   the delta_ij pieces are proportional to C(G_i), zero for U(1). Minimal supersymmetrization equals Phi*")
P("   exactly when every complex scalar needs a second chiral multiplet (anomaly / holomorphy), as for any scalar")
P("   with nonzero U(1) charge or in a complex rep; it fails for complex scalars in real reps (test d).")

open(__file__.replace(".py", ".txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
