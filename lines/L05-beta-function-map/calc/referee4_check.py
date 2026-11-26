"""Referee 4 independent check (written from scratch; does not import the line's scripts).
Part 1: two-loop gauge b_ij from the general Machacek-Vaughn (non-SUSY) and Jones/Martin-Vaughn (SUSY)
        formulas, SM vs MSSM, and the counterexample SM + complex (8,3,0) with its minimal SUSY completion.
Part 2: one-loop Yukawa beta of y_t from the general Weyl/real-scalar formula, split into leg, vertex and
        scalar-trace pieces, for the SM (one doublet H, down Yukawa via H^c) and for a 2HDM-II.
Units: 16 pi^2 = 1. g1 GUT-normalised. Run: python referee4_check.py
"""
import sympy as sp
R = sp.Rational

# ---------- Part 1 ----------
CG = {1: 0, 2: 2, 3: 3}
def dyn(n):  # Dynkin index and Casimir of SU(n) irreps used here: dims 1, n(fund), n^2-1 (adj)
    return {1: (0, 0), n: (R(1, 2), R(n * n - 1, 2 * n)), n * n - 1: (n, n)}

def SC(d3, d2, Y):
    """S_i (index x dims of other factors) and C_i for a field (d3, d2, Y)."""
    s3, c3 = dyn(3)[d3]; s2, c2 = dyn(2)[d2]
    S = {1: R(3, 5) * Y**2 * d3 * d2, 2: s2 * d3, 3: s3 * d2}
    C = {1: R(3, 5) * Y**2, 2: c2, 3: c3}
    return S, C

def nonsusy(weyl, cplx):
    b = {i: -R(11, 3) * CG[i] for i in CG}
    bij = {(i, j): (-R(34, 3) * CG[i]**2 if i == j else 0) for i in CG for j in CG}
    for f, w1, wd, wo in [(weyl, R(2, 3), R(10, 3), 2), (cplx, R(1, 3), R(2, 3), 4)]:
        for fld in f:
            S, C = SC(*fld)
            for i in CG:
                b[i] += w1 * S[i]
                for j in CG:
                    bij[i, j] += S[i] * (wo * C[j] + (wd * CG[i] if i == j else 0))
    return b, bij

def susy(chirals):
    b = {i: -3 * CG[i] for i in CG}
    bij = {(i, j): (-6 * CG[i]**2 if i == j else 0) for i in CG for j in CG}
    for fld in chirals:
        S, C = SC(*fld)
        for i in CG:
            b[i] += S[i]
            for j in CG:
                bij[i, j] += S[i] * (4 * C[j] + (2 * CG[i] if i == j else 0))
    return b, bij

gen = [(3, 2, R(1, 6)), (3, 1, R(-2, 3)), (3, 1, R(1, 3)), (1, 2, R(-1, 2)), (1, 1, R(1))]  # LH Weyl
SMw = gen * 3
H = (1, 2, R(1, 2)); Hc = (1, 2, R(-1, 2))
bS, BS = nonsusy(SMw, [H])
bM, BM = susy(SMw + [H, Hc])
print("SM   b =", [bS[i] for i in CG], " b_ij =", [[BS[i, j] for j in CG] for i in CG])
print("MSSM b =", [bM[i] for i in CG], " b_ij =", [[BM[i, j] for j in CG] for i in CG])
assert [bS[i] for i in CG] == [R(41, 10), R(-19, 6), -7]
assert [bM[i] for i in CG] == [R(33, 5), 1, -3]
assert BS[1, 2] == R(27, 10) and BS[3, 3] == -26 and BM[2, 2] == 25 and BM[3, 3] == 14
rat = {k: sp.nsimplify(BM[k] / BS[k]) for k in BS}
print("MSSM/SM ratios:", rat)
assert all(rat[k] == 2 for k in rat if k[0] != k[1] or k == (1, 1))
# conjugation blindness of the image: H_d = H^c vs duplicate H' (Y=+1/2)
assert susy(SMw + [H, H]) == susy(SMw + [H, Hc])
print("H_d = H^c vs duplicate H': identical b_i, b_ij (asserted)")
# counterexample: parent SM + complex (8,3,0); minimal SUSY completion adds ONE chiral (8,3,0) (real rep)
X = (8, 3, 0)
# extend dyn tables: SU(3) adjoint dim 8 and SU(2) adjoint dim 3 already covered
bP, BP = nonsusy(SMw, [H, X])
bQ, BQ = susy(SMw + [H, Hc, X])
r2 = {k: BQ[k] / BP[k] for k in BP}
print("SM+cplx(8,3,0) -> min SUSY ratios (2,3),(3,2):", r2[2, 3], r2[3, 2])
assert r2[2, 3] == R(18, 17) and r2[3, 2] == R(18, 17)
bQ2, BQ2 = susy(SMw + [H, Hc, X, X])
assert all(BQ2[k] / BP[k] == 2 for k in BP if k[0] != k[1] or k == (1, 1))
print("with Phi* (two chirals for the complex scalar): ratio 2 restored (asserted)")

# ---------- Part 2 ----------
yt, yb = sp.symbols('y_t y_b', positive=True)
# Weyl fermions psi = (t, b, tc, bc); colour is diagonal for Yukawas; colour factor 3 enters fermion traces.
def build(model):
    # complex scalar components (each -> two real fields r, s with phi=(r+is)/sqrt2)
    # model 'SM': H=(Hp,H0). up: yt (t H0 - b Hp) tc ; down: yb (H0* b + Hp* t) bc
    # model '2HDM': Hu=(Hup,Hu0) for up; Hd=(Hd0,Hdm) Y=-1/2 for down: yb (Hd0 b - Hdm t) bc
    t, b, tc, bc = range(4)
    if model == 'SM':
        comps = ['Hp', 'H0']
        terms = [('H0', False, t, tc, yt), ('Hp', False, b, tc, -yt),
                 ('H0', True, b, bc, yb), ('Hp', True, t, bc, yb)]
    else:
        comps = ['Hup', 'Hu0', 'Hd0', 'Hdm']
        terms = [('Hu0', False, t, tc, yt), ('Hup', False, b, tc, -yt),
                 ('Hd0', False, b, bc, yb), ('Hdm', False, t, bc, -yb)]
    mats = []
    for c in comps:
        for part in ('r', 's'):
            M = sp.zeros(4, 4)
            for (cc, conj, i, j, y) in terms:
                if cc != c:
                    continue
                # phi = (r + i s)/sqrt2 ; phi* = (r - i s)/sqrt2
                f = 1 / sp.sqrt(2) if part == 'r' else (-sp.I if conj else sp.I) / sp.sqrt(2)
                M[i, j] += y * f; M[j, i] += y * f
            mats.append(M)
    return mats

def beta_pieces(model):
    Ys = build(model)
    col = sp.diag(3, 3, 3, 3)  # colour multiplicity of each Weyl field in fermion traces
    Y2F = sum((Y.H * Y for Y in Ys), sp.zeros(4, 4))
    out = []
    for Ya in Ys:
        legs = (Y2F.T * Ya + Ya * Y2F) / 2
        vert = 2 * sum((Yb * Ya.H * Yb for Yb in Ys), sp.zeros(4, 4))
        trace = sum((Yb * (R(1, 2) * (col * (Yb.H * Ya + Ya.H * Yb)).trace()) for Yb in Ys), sp.zeros(4, 4))
        out.append((Ya, legs, vert, trace))
    return out

def coef_tt(model):
    # entry (t, tc) of the Y^a with nonzero (t,tc) real part (the r-component of H0 or Hu0)
    for Ya, legs, vert, trace in beta_pieces(model):
        if Ya[0, 2] != 0 and Ya[0, 2].is_real:
            y0 = Ya[0, 2]
            return [sp.expand(sp.simplify(X[0, 2] / y0)) for X in (legs, vert, trace)]

for model in ('SM', '2HDM'):
    legs, vert, trace = coef_tt(model)
    tot = sp.expand(legs + vert + trace)
    print(f"{model}: beta_yt/yt  legs = {legs},  vertex = {vert},  scalar trace = {trace},  total = {tot}")
    if model == 'SM':
        assert tot == R(9, 2) * yt**2 + R(3, 2) * yb**2
        assert vert == -2 * yb**2
    else:
        assert tot == R(9, 2) * yt**2 + R(1, 2) * yb**2
        assert vert == 0
print("SM vertex -2 y_b^2 confirmed; it is absent when up and down Yukawas use different doublets (2HDM-II).")
print("Note: a type-I 2HDM (both Yukawas on one doublet, second doublet uncoupled) has the SM Yukawa matrices, so the")
print("same vertex term: it tracks 'one field in both Yukawas', which with Y=+1/2 forces H^c in the down Yukawa.")
