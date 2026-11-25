"""L05: exact (sympy Rational) beta-function coefficients for the SM and for its image under the
chiral-completion map Phi, written in the CP-conjugate (all left-handed Weyl) labelling.

Conventions
  d g_i / d ln mu = g_i^3/(16 pi^2) b_i + g_i^3/(16 pi^2)^2 [ sum_j b_ij g_j^2 - sum_f c_i^f y_f^2 ]
  g1 GUT-normalised: T_1(field) = (3/5) Y^2 * dim, Y = Q - T3.
  S_i(field) = Dynkin index under G_i times the dimension under the other factors.
  C_i(field) = quadratic Casimir under G_i  (C_1 = (3/5) Y^2).

Sections
  1. Field content in conjugate labelling (Q, u^c, d^c, L, e^c, H; gauge fields self-conjugate).
  2. One loop: standard formula, Nielsen-Hughes per-helicity-state formula, split into
     self-conjugate / particle / antiparticle state contributions, spin / orbital split.
  3. Phi: Weyl field -> chiral multiplet; complex scalar H -> chiral H and chiral H^c (= i s2 H*);
     real gauge field -> vector multiplet (Majorana gaugino). One loop via NSVZ and via components.
  4. Unification ratio B = (b2-b3)/(b1-b2) for SM, Phi(SM), and each partial piece of Phi.
  5. Two loop b_ij: component (Machacek-Vaughn) formula for SM; for Phi(SM) both the SUSY formula and
     components + gaugino-Yukawa term, checked equal.
  6. Two-loop Yukawa coefficients c_i^f and their transformation under Phi.
"""
from sympy import Rational as R, Matrix, nsimplify

# ---------------- 1. field content (one generation of matter, conjugate labelling) ----------------
# (name, kind, dim3, dim2, Y, multiplicity, label)
# kind: 'weyl' = left-handed Weyl field; 'cscalar' = complex scalar.  Gauge fields handled via C(G).
NG = 3
MATTER = [
    ("Q",   "weyl", 3, 2, R(1, 6),  NG, "particle field"),
    ("u^c", "weyl", 3, 1, R(-2, 3), NG, "antiparticle field (LH anti-up)"),
    ("d^c", "weyl", 3, 1, R(1, 3),  NG, "antiparticle field (LH anti-down)"),
    ("L",   "weyl", 1, 2, R(-1, 2), NG, "particle field"),
    ("e^c", "weyl", 1, 1, R(1),     NG, "antiparticle field (LH positron)"),
]
HIGGS = [("H", "cscalar", 1, 2, R(1, 2), 1, "complex doublet; H^c = i s2 H* has Y=-1/2")]
CG = [R(0), R(2), R(3)]  # C(G) for U(1), SU(2), SU(3)

T_FUND = R(1, 2)
CAS = {3: R(4, 3), 2: R(3, 4), 1: R(0)}


def S(f, i):
    _, _, d3, d2, Y, m, _ = f
    if i == 0:
        return m * R(3, 5) * Y**2 * d3 * d2
    if i == 1:
        return m * (T_FUND if d2 == 2 else 0) * d3
    return m * (T_FUND if d3 == 3 else 0) * d2


def C(f, i):
    _, _, d3, d2, Y, _, _ = f
    return [R(3, 5) * Y**2, CAS[d2], CAS[d3]][i]


def vec(fn):
    return Matrix([fn(i) for i in range(3)])


def b1loop(fields, cg_coef, w_weyl, w_cs):
    return vec(lambda i: cg_coef * CG[i]
               + sum(w_weyl * S(f, i) for f in fields if f[1] == "weyl")
               + sum(w_cs * S(f, i) for f in fields if f[1] == "cscalar"))


def Bratio(b):
    return (b[1] - b[2]) / (b[0] - b[1])


def show(name, b):
    B = Bratio(b)
    print(f"  {name:48s} b = ({b[0]}, {b[1]}, {b[2]})   B = {B} = {float(B):.4f}")


print("=" * 100)
print("1. SM one loop, standard formula  b = -11/3 C(G) + 2/3 sum_Weyl S + 1/3 sum_cscalar S")
SM = MATTER + HIGGS
b_sm = b1loop(SM, R(-11, 3), R(2, 3), R(1, 3))
show("SM", b_sm)
assert list(b_sm) == [R(41, 10), R(-19, 6), R(-7)]

# ---------------- 2. Nielsen-Hughes per-helicity-state form ----------------
# b = -(1/2) sum_states (-1)^{2s} [(2s)^2 - 1/3] T(state)
# Each one-particle helicity state is counted once.  A Weyl field psi in R has two states:
# particle (R, h=-1/2) and antiparticle (Rbar, h=+1/2).  A complex scalar: particle (R) and antiparticle (Rbar).
# A real gauge field: two helicity states, both in the (real) adjoint = self-conjugate.


def nh(s, T):
    return -R(1, 2) * (-1)**int(2 * s) * ((2 * s)**2 - R(1, 3)) * T


def nh_spin(s, T):
    return -R(1, 2) * (-1)**int(2 * s) * (2 * s)**2 * T


def nh_orb(s, T):
    return R(1, 6) * (-1)**int(2 * s) * T


def states(fields, gauge=True, gaugino=False, scalar_partners=False, extra_chiral_fermions=()):
    """List of (s, i -> T_i, class) one-particle helicity states."""
    st = []
    if gauge:
        for _ in range(2):
            st.append((1, lambda i: CG[i], "selfconj"))
    if gaugino:
        for _ in range(2):
            st.append((R(1, 2), lambda i: CG[i], "selfconj"))
    for f in fields:
        s = R(1, 2) if f[1] == "weyl" else 0
        st.append((s, (lambda i, f=f: S(f, i)), "particle"))
        st.append((s, (lambda i, f=f: S(f, i)), "antiparticle"))
    return st


def nh_sum(st, fn=nh, cls=None):
    return vec(lambda i: sum(fn(s, T(i)) for (s, T, c) in st if cls is None or c == cls))


st_sm = states(SM)
b_nh = nh_sum(st_sm)
print("\n2. Nielsen-Hughes per-state form reproduces SM:", list(b_nh), b_nh == b_sm)
assert b_nh == b_sm
b_sc = nh_sum(st_sm, cls="selfconj")
b_part = nh_sum(st_sm, cls="particle")
b_anti = nh_sum(st_sm, cls="antiparticle")
print("   split by CPT class of the one-particle state:")
show("self-conjugate states (gauge bosons)", b_sc)
show("particle states", b_part)
show("antiparticle states  [definition (i)]", b_anti)
assert b_part == b_anti  # CPT: (R,h) <-> (Rbar,-h), T(R)=T(Rbar), formula even in h
assert b_sc + b_part + b_anti == b_sm
# antiparticle states of the antiparticle FIELDS u^c,d^c,e^c are particle states u_R,d_R,e_R:
anti_fields = [f for f in MATTER if f[0].endswith("^c")]
part_fields = [f for f in MATTER if not f[0].endswith("^c")]
print("   split by FIELD label in conjugate basis [definition (ii)] (each field = its 2 states):")
show("antiparticle fields u^c,d^c,e^c (= SU(5) 5bar+10 pieces)", b1loop(anti_fields, 0, R(2, 3), 0))
show("particle fields Q,L", b1loop(part_fields, 0, R(2, 3), 0))
print("   spin / orbital split  b = -2 Str(s^2 T) + (1/6) Str(T):")
b_spin = nh_sum(st_sm, nh_spin)
b_orb = nh_sum(st_sm, nh_orb)
show("SM spin (paramagnetic) part", b_spin)
show("SM orbital (diamagnetic) part = Str(T)/6", b_orb)
assert b_spin + b_orb == b_sm

# ---------------- 3. the map Phi ----------------
print("\n3. Phi: Weyl -> chiral, H -> chiral H and chiral H^c, gauge -> vector multiplet")
Hc = ("H^c", "cscalar", 1, 2, R(-1, 2), 1, "conjugate doublet promoted to independent field")
CHIRAL = MATTER + HIGGS + [Hc]  # chiral superfields (labelled by rep of their scalar/fermion)
b_nsvz = vec(lambda i: -3 * CG[i] + sum(S(f, i) for f in CHIRAL))
show("Phi(SM) via NSVZ  -3C(G) + sum_chiral S", b_nsvz)
assert list(b_nsvz) == [R(33, 5), 1, -3]
# components: gauge + Majorana gaugino + Weyl fermion and complex scalar for every chiral superfield
comp_fields = [(n, "weyl", d3, d2, Y, m, l) for (n, k, d3, d2, Y, m, l) in CHIRAL] + \
              [(n + "~", "cscalar", d3, d2, Y, m, l) for (n, k, d3, d2, Y, m, l) in CHIRAL]
st_mssm = states(comp_fields, gaugino=True)
b_comp = nh_sum(st_mssm)
print("   components via Nielsen-Hughes:", list(b_comp), b_comp == b_nsvz)
assert b_comp == b_nsvz
print("   orbital part of Phi(SM) = Str(T)/6 :", list(nh_sum(st_mssm, nh_orb)), "(cancels in every supermultiplet)")
assert nh_sum(st_mssm, nh_orb) == Matrix([0, 0, 0])
d_spin = b_nsvz - b_spin
print("   b[Phi(SM)] - b_spin[SM] =", list(d_spin),
      "= C(G) (Majorana gauginos) + 2 S(H) (Dirac higgsino pair):",
      list(vec(lambda i: CG[i] + 2 * S(HIGGS[0], i))))
assert d_spin == vec(lambda i: CG[i] + 2 * S(HIGGS[0], i))

# ---------------- 4. unification ratio, partial maps ----------------
print("\n4. B = (b2-b3)/(b1-b2). Complete SU(5) multiplets (each generation) shift b by k(1,1,1) and drop out.")
per_gen = b1loop([(n, k, d3, d2, Y, 1, l) for (n, k, d3, d2, Y, m, l) in MATTER], 0, R(2, 3), 0)
print("   one SM generation (Weyl):", list(per_gen), " as chiral multiplets:",
      list(b1loop([(n, k, d3, d2, Y, 1, l) for (n, k, d3, d2, Y, m, l) in MATTER], 0, 1, 0)))
print("   General: B = (c - n h/2)/(2c + n h/5), c = gauge weight, h = weight per Higgs doublet, n = # doublets")


def Bgen(c, h, n):
    return (c - n * h / 2) / (2 * c + n * h / 5)


rows = [
    ("SM", R(-11, 3), R(1, 3), 1),
    ("gauge -> vector multiplet only", R(-3), R(1, 3), 1),
    ("H^c promoted to independent field only (antimatter step)", R(-11, 3), R(1, 3), 2),
    ("H -> chiral only (adds higgsino)", R(-11, 3), R(1), 1),
    ("H, H^c both chiral (no gaugino)", R(-11, 3), R(1), 2),
    ("full Phi(SM) = MSSM", R(-3), R(1), 2),
    ("SM spin part only", R(-4), R(0), 1),
    ("pure gauge + complete multiplets", R(-11, 3), R(0), 0),
]
for name, c, h, n in rows:
    B = Bgen(c, h, n)
    print(f"   {name:58s} r = nh/c = {str(n*h/c):6s} B = {str(B):8s} = {float(B):.4f}")
assert Bgen(R(-11, 3), R(1, 3), 1) == Bratio(b_sm) and Bgen(R(-3), R(1), 2) == Bratio(b_nsvz)
assert Bratio(b_spin) == R(1, 2)
print("   B for antiparticle-state part alone (def. i):", Bratio(b_anti), "=", float(Bratio(b_anti)))
print("   Ratio r_MSSM/r_SM =", (2 * R(1) / -3) / (R(1, 3) / R(-11, 3)),
      "= 2 (H^c doubling) x 3 (scalar -> chiral) x 11/9 (vector -> vector multiplet)")

# ---------------- 5. two loop b_ij ----------------
print("\n5. Two loop b_ij")


def bij_components(weyls, cscalars, gauge_coef=R(-34, 3), gaugino=False):
    M = Matrix.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            d = 1 if i == j else 0
            v = gauge_coef * CG[i]**2 * d
            if gaugino:  # Weyl fermion in adjoint of G_i: (2 C_j + 10/3 C_i delta) C_i delta
                v += (2 * CG[i] * d + R(10, 3) * CG[i] * d) * CG[i] * d
            v += sum((2 * C(f, j) + R(10, 3) * CG[i] * d) * S(f, i) for f in weyls)
            v += sum((4 * C(f, j) + R(2, 3) * CG[i] * d) * S(f, i) for f in cscalars)
            M[i, j] = v
    return M


B_SM = bij_components(MATTER, HIGGS)
print("   SM b_ij =", B_SM.tolist())
assert B_SM == Matrix([[R(199, 50), R(27, 10), R(44, 5)], [R(9, 10), R(35, 6), 12], [R(11, 10), R(9, 2), -26]])
B_SUSY = Matrix(3, 3, lambda i, j: -6 * CG[i]**2 * (1 if i == j else 0)
                + sum((4 * C(f, j) + 2 * CG[i] * (1 if i == j else 0)) * S(f, i) for f in CHIRAL))
print("   Phi(SM) b_ij (SUSY formula -6C^2 d + sum_chiral (4C_j + 2C_i d) S_i) =", B_SUSY.tolist())
assert B_SUSY == Matrix([[R(199, 25), R(27, 5), R(88, 5)], [R(9, 5), 25, 24], [R(11, 5), 9, 14]])
B_comp = bij_components(CHIRAL, CHIRAL, gaugino=True)
Delta = Matrix(3, 3, lambda i, j: -2 * sum(S(f, i) * C(f, j) + (1 if i == j else 0) * CG[i] * S(f, i)
                                            for f in CHIRAL))
print("   components (MV, no Yukawa) =", B_comp.tolist())
print("   gaugino-Yukawa term -2 sum_Phi [S_i C_j + d_ij C_i S_i] =", Delta.tolist())
assert B_comp + Delta == B_SUSY
print("   components + gaugino Yukawa == SUSY formula: True")
print("   Per-field coefficient map (S_i weight on C_j, on C_i delta):")
print("     SM Weyl (2, 10/3) -> chiral (4, 2);  SM complex scalar (4, 2/3) -> chiral (4, 2);  gauge -34/3 -> -6")
# B-like ratio at 2 loops is not a constant; print b_ij row differences for record
print("   SM b_ij - Phi(SM) b_ij =", (B_SM - B_SUSY).tolist())

# ---------------- 6. Yukawa two-loop coefficients ----------------
print("\n6. Two-loop Yukawa coefficients c_i^f (subtracted in d g_i).")
print("   Conjugate labelling: SM  y_t Q H^c u^c, y_b Q H d^c, y_tau L H e^c.  Phi: H^c -> H_u, H -> H_d.")
dG = [1, 3, 8]
F = {f[0]: f for f in MATTER + HIGGS + [Hc]}
yuk = {"t": ("Q", "u^c", "H^c", 6), "b": ("Q", "d^c", "H", 6), "tau": ("L", "e^c", "H", 2)}
known_sm = {"t": [R(17, 10), R(3, 2), 2], "b": [R(1, 2), R(3, 2), 2], "tau": [R(3, 2), R(1, 2), 0]}
known_mssm = {"t": [R(26, 5), 6, 4], "b": [R(14, 5), 6, 4], "tau": [R(18, 5), 2, 0]}
for y, (f1, f2, h, N) in yuk.items():
    sm = [R(N, dG[i]) * (C(F[f1], i) + C(F[f2], i)) for i in range(3)]
    ms = [2 * R(N, dG[i]) * (C(F[f1], i) + C(F[f2], i) + C(F[h], i)) for i in range(3)]
    assert sm == known_sm[y] and ms == known_mssm[y]
    hl = [2 * R(N, dG[i]) * C(F[h], i) for i in range(3)]
    print(f"   y_{y:3s}: SM c = {[str(x) for x in sm]}   Phi(SM) c = {[str(x) for x in ms]}"
          f"   = 2*SM + {[str(x) for x in hl]} (Higgs leg)")
print("   SM: only the two fermion legs carry Casimirs (weight 1). SUSY: all three legs (weight 2).")
print("\nAll assertions passed.")

# ---------------- 7. two-loop homothety identity ----------------
print("\n7. Two-loop identity: Phi(SM) b_ij = 2 * SM b_ij for all i != j, and for (1,1).")
D = B_SUSY - 2 * B_SM
print("   Phi(SM) b_ij - 2 SM b_ij =", D.tolist())
for i in range(3):
    for j in range(3):
        if i != j or i == 0:
            assert D[i, j] == 0
W = vec(lambda i: sum(S(f, i) for f in MATTER))
SH = vec(lambda i: S(HIGGS[0], i))
diag = [CG[i] * (R(50, 3) * CG[i] - R(14, 3) * W[i] + R(8, 3) * SH[i]) for i in range(3)]
assert all(D[i, i] == diag[i] for i in range(3))
print("   diagonal remainder = C_i [50/3 C_i - 14/3 W_i + 8/3 S_H,i] =", diag)
# same map WITHOUT promoting H^c: off-diagonal is no longer a uniform multiple
CH_noHc = MATTER + HIGGS
B_noHc = Matrix(3, 3, lambda i, j: -6 * CG[i]**2 * (1 if i == j else 0)
                + sum((4 * C(f, j) + 2 * CG[i] * (1 if i == j else 0)) * S(f, i) for f in CH_noHc))
ratios = {(i, j): B_noHc[i, j] / B_SM[i, j] for i in range(3) for j in range(3) if i != j}
print("   without H^c as independent field, off-diagonal ratios Phi'/SM =",
      {k: str(v) for k, v in ratios.items()})
assert len(set(ratios.values())) > 1
print("   -> uniform factor 2 requires H and H^c to be separate chiral fields.")
print("\nAll assertions (incl. section 7) passed.")
