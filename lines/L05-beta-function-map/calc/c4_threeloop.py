"""
L05 cycle 4: does the two-loop doubling identity extend to three loops?

Sources (coefficients transcribed from the arXiv TeX sources, not from memory):
  SM, MS-bar: Mihaila, Salomon, Steinhauser, PRL 108 (2012) 151602, arXiv:1201.5868, eq. (5).
     beta_i = mu^2 d(alpha_i/pi)/dmu^2 = (alpha_i/pi)^2 { ... + sum (alpha_j/pi)(alpha_k/pi) X_ijk + ... }, GUT-normalised alpha_1.
     Conversion to dg_i/dt = g_i^3/(16pi^2)^3 * c_i(jk) g_j^2 g_k^2:  c = 64 X  (two-loop: b = 16 X, checked in c4_doubling.py).
     alpha_t/pi = 4 y_t^2/(16 pi^2), so the same factor 64 applies to alpha_t alpha_j terms.  y_b = y_tau = 0 in eq. (5).
  MSSM, DRED: Ferreira, Jack, Jones, PLB 387 (1996) 80, hep-ph/9605440, eq. (3.x) 'eva', same g-convention as ours
     (their b_ij matrix reproduced exactly in c4_doubling.py).
Scheme: SM is MS-bar, MSSM is DR-bar. Three-loop gauge coefficients are scheme dependent. The one-loop conversion
  g_DR = g_MS (1 + C(G) g^2/(96 pi^2))  (Martin & Vaughn, PLB 318 (1993) 331, hep-ph/9308222; formula [unverified from
  full text], consistent with the standard alpha_s^DR = alpha_s^MS (1 + alpha_s/(4 pi)))
  shifts c_i(jj), j != i, by -2 k_j b_ij and the diagonal c_i(ii) as well (derived in section 0, cycle 6); a two-loop
  mixed term g_i -> g_i(1 + m g_i^2 g_j^2) shifts c_i(jj) by +2 m b_j. Only c_i(ij) and fully mixed c_i(jk) are invariant
  under every redefinition compatible with beta_i ~ g_i^3; section 6 compares exactly those entries.
Run: python c4_threeloop.py  (output c4_threeloop.txt)
"""
from sympy import Rational as R, symbols, expand, Poly, simplify, Matrix

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

n = symbols("n_G")
# pair keys: (j,k) with j<=k, 1=U1(GUT), 2=SU2, 3=SU3
MSS = {
    1: {(1, 1): R(489, 512000) - 29*n/2400 - 209*n**2/8640, (1, 2): R(783, 51200) - 7*n/6400, (1, 3): -137*n/14400,
        (2, 2): R(3401, 20480) + 83*n/1920 - 11*n**2/960, (2, 3): -n/320, (3, 3): 275*n/576 - 121*n**2/2160},
    2: {(1, 1): R(163, 102400) - 7*n/960 - 11*n**2/2880, (1, 2): R(561, 10240) + 13*n/1280, (1, 3): -n/960,
        (2, 2): -R(667111, 110592) + 1603*n/432 - 415*n**2/1728, (2, 3): 13*n/64, (3, 3): 125*n/192 - 11*n**2/144},
    3: {(1, 1): -13*n/7680 - 121*n**2/17280, (1, 2): -n/2560, (1, 3): 77*n/2880,
        (2, 2): 241*n/1536 - 11*n**2/384, (2, 3): 7*n/64, (3, 3): -R(2857, 128) + 5033*n/576 - 325*n**2/864},
}
MSS_t = {1: {1: -R(2827, 51200), 2: -R(471, 2048), 3: -R(29, 320)},
         2: {1: -R(593, 10240), 2: -R(729, 2048), 3: -R(7, 64)},
         3: {1: -R(101, 2560), 2: -R(93, 512), 3: -R(5, 8)}}
SM = {i: {k: expand(64*v) for k, v in d.items()} for i, d in MSS.items()}
SMt = {i: {j: 64*v for j, v in d.items()} for i, d in MSS_t.items()}

# FJJ: beta^(3)_{g_i} = g_i^3 [ ... ]  pure-gauge and gauge x trT parts
FJJ = {
    1: {(3, 3): -(R(88, 5)*n**2 - R(572, 9)*n), (2, 2): -(R(18, 5)*n**2 - R(9, 5)*n - R(54, 5)),
        (1, 1): -(R(38, 5)*n**2 + R(1261, 225)*n + R(54, 125)), (1, 3): -R(1096, 225)*n, (2, 3): -R(8, 5)*n,
        (1, 2): -(R(27, 25) + R(14, 25)*n)},
    2: {(3, 3): -(24*n**2 - R(260, 3)*n), (2, 2): -(26*n**2 - 123*n + 100), (1, 1): -(R(6, 5)*n**2 + R(169, 75)*n + R(18, 25)),
        (1, 2): R(2, 5)*n + R(3, 5), (2, 3): 8*n, (1, 3): -R(8, 15)*n},
    3: {(3, 3): -(44*n**2 - R(3236, 9)*n + 567), (2, 3): 2*n, (1, 3): R(22, 45)*n, (1, 1): -(R(11, 5)*n**2 + R(217, 225)*n),
        (2, 2): -(9*n**2 - 18*n), (1, 2): -R(1, 5)*n},
}
FJJt = {1: {1: -R(169, 75), 2: -R(87, 5), 3: -R(352, 15)},
        2: {1: -R(29, 5), 2: -33, 3: -32},
        3: {1: -R(44, 15), 2: -12, 3: -R(104, 3)}}

# two-loop b_ij (for scheme conversion), from c4_doubling.py (asserted there against FJJ / MSS)
b2_MSSM = Matrix([[R(38, 15)*n + R(9, 25), R(6, 5)*n + R(9, 5), R(88, 15)*n],
                  [R(2, 5)*n + R(3, 5), 14*n - 17, 8*n],
                  [R(11, 15)*n, 3*n, R(68, 3)*n - 54]])
CG = {1: 0, 2: 2, 3: 3}

# --- derive the scheme shift symbolically for a 2-coupling toy (cycle 6: diagonal and two-loop terms included) ----
# Background-field structure: beta_i is proportional to g_i^3, so the allowed redefinitions are
#   G_i = g_i [1 + k_i g_i^2 + e (a_i g_i^4 + m_i g_i^2 g_j^2)]  (and the same with i <-> j),
# i.e. G_i - g_i is proportional to g_i^3. Terms like g_i g_j^4 are excluded (they would spoil beta_i ~ g_i^3).
P("0. Scheme shift of three-loop coefficients (units 16pi^2 = 1) under the background-field-compatible redefinition")
P("   G_i = g_i + e k_i g_i^3 + e^2 (a_i g_i^5 + m_i g_i^3 g_j^2), same for j")
gi, gj, ki, kj, bi, bj, bii, bij, bji, bjj, e = symbols("g_i g_j k_i k_j b_i b_j b_ii b_ij b_ji b_jj e")
ai, aj, mi, mj = symbols("a_i a_j m_i m_j")
c = symbols("c0:6")
def beta_i(a, b_):  # generic up to three loops, i-coupling a, other b_
    return e*a**3*bi + e**2*a**3*(bii*a**2 + bij*b_**2) + e**3*a**3*(c[0]*a**4 + c[1]*a**2*b_**2 + c[2]*b_**4)
def beta_j(a, b_):
    return e*b_**3*bj + e**2*b_**3*(bjj*b_**2 + bji*a**2)
Gi, Gj = symbols("G_i G_j")
Gi_of_g = gi + e*ki*gi**3 + e**2*(ai*gi**5 + mi*gi**3*gj**2)
Gj_of_g = gj + e*kj*gj**3 + e**2*(aj*gj**5 + mj*gj**3*gi**2)
# beta'_i = dG_i/dt = (dG_i/dg_i) beta_i + (dG_i/dg_j) beta_j, then re-express in G (invert to O(e^2))
bp = expand(Gi_of_g.diff(gi)*beta_i(gi, gj) + Gi_of_g.diff(gj)*beta_j(gi, gj))
# inverse to O(e^2): g_i = G_i - e k_i G_i^3 + e^2 (3 k_i^2 - a_i) G_i^5 - e^2 m_i G_i^3 G_j^2
gi_G = Gi - e*ki*Gi**3 + e**2*((3*ki**2 - ai)*Gi**5 - mi*Gi**3*Gj**2)
gj_G = Gj - e*kj*Gj**3 + e**2*((3*kj**2 - aj)*Gj**5 - mj*Gj**3*Gi**2)
assert expand(Gi_of_g.subs({gi: gi_G, gj: gj_G}, simultaneous=True)).coeff(e, 1) == 0
bp = expand(bp.subs({gi: gi_G, gj: gj_G}, simultaneous=True))
bp = sum(bp.coeff(e, n)*e**n for n in range(4))
bp1, bp2, bp3 = (expand(bp.coeff(e, n)) for n in (1, 2, 3))
assert simplify(bp1 - bi*Gi**3) == 0
assert simplify(bp2 - Gi**3*(bii*Gi**2 + bij*Gj**2)) == 0      # two-loop coefficients are invariant
d_ii = simplify(bp3.coeff(Gi, 7).coeff(Gj, 0) - c[0])
d_ij = simplify(bp3.coeff(Gi, 5).coeff(Gj, 2) - c[1])
d_jj = simplify(bp3.coeff(Gi, 3).coeff(Gj, 4) - c[2])
P("   shift of c_i(ii)  [G_i^7]      :", d_ii)
P("   shift of c_i(ij)  [G_i^5 G_j^2]:", d_ij)
P("   shift of c_i(jj)  [G_i^3 G_j^4]:", d_jj)
assert simplify(d_ij) == 0
assert simplify(d_jj - (-2*kj*bij + 2*mi*bj)) == 0
P("   => c_i(ij) (g_i^5 g_j^2) is invariant. c_i(ii) and c_i(jj) shift (diagonal: one-loop k_i and two-loop a_i terms;")
P("      c_i(jj): one-loop k_j term -2 k_j b_ij AND two-loop mixed term +2 m_i b_j). The mixed m_i can carry n_G, so an")
P("      n_G^2 piece of c_i(jj) is NOT protected by the one-loop conversion alone.")
P("   Fully mixed c_i(jk), j != k both != i (three-coupling theory): an allowed term m_ij g_i^3 g_j^2 in G_i shifts only")
P("      c_i(jj) (by 2 m_ij b_j); k_j, k_k shift only c_i(jj), c_i(kk); the two-loop b_ij g_i^3 g_j^2 is linear in g_j^2,")
P("      so no product of shifts yields g_i^3 g_j^2 g_k^2. A G_i - g_i term ~ g_i g_j^2 g_k^2 would, but it is not ~ g_i^3.")
P("      So c_i(jk) is invariant as well.")
P("   Scheme-invariant three-loop entries therefore: c_i(ij) = coefficient of g_i^5 g_j^2, and c_i(jk) fully mixed.")

def mssm_ms(i, key):
    v = FJJ[i][key]
    j, k = key
    if j == k and j != i:
        v = v - 2*R(-CG[j], 6)*b2_MSSM[i-1, j-1]   # DR -> MS: k_j = -C(G_j)/6
    return expand(v)

P("\n1. Pure-gauge three-loop coefficients c_i(jk) of g_i^3 g_j^2 g_k^2, n_G general and n_G = 3")
P("   'mixed' = at least one of j,k differs from i, plus all of i = 1 (abelian), the analogue of the 2-loop identity")
rows = []
for i in (1, 2, 3):
    for key in sorted(SM[i]):
        mixed = (key != (i, i)) or i == 1
        s, m_dr, m_ms = SM[i][key], expand(FJJ[i][key]), mssm_ms(i, key)
        s3, d3, ms3 = s.subs(n, 3), m_dr.subs(n, 3), m_ms.subs(n, 3)
        r_dr = (d3/s3) if s3 != 0 else None
        r_ms = (ms3/s3) if s3 != 0 else None
        rows.append((i, key, mixed, s, m_dr, m_ms, s3, d3, ms3, r_dr, r_ms))
        P(f"   i={i} jk={key} {'mixed' if mixed else 'diag '}  SM(MS)={s}  MSSM(DR)={m_dr}  MSSM(MS)={m_ms}")
        P(f"        n_G=3: SM {s3} ({float(s3):.4g})  MSSM DR {d3} ({float(d3):.4g})  ratio DR/SM {r_dr}"
          f"{'' if r_dr is None else f' ({float(r_dr):.4g})'}   MSSM MS {ms3}  ratio {r_ms}{'' if r_ms is None else f' ({float(r_ms):.4g})'}")

P("\n2. Is there a uniform ratio on the mixed block?")
for lab, idx in (("DR/SM", 9), ("MS/SM", 10)):
    rs = sorted(set(r[idx] for r in rows if r[2] and r[idx] is not None))
    P(f"   {lab} ratios on mixed entries (n_G=3):", [f"{float(x):.4g}" for x in rs])
    P(f"   uniform? {len(rs) == 1}")
# n_G-structure: compare polynomial coefficients (n^0: gauge+Higgs(+gaugino/higgsino), n^1, n^2)
P("\n3. Coefficient-by-coefficient in n_G (n^1: one matter loop; n^2: two matter loops) for mixed entries")
for r in rows:
    if not r[2]:
        continue
    ps, pm = Poly(r[3], n), Poly(r[5], n)
    cs = [ps.coeff_monomial(n**p) for p in range(3)]
    cm = [pm.coeff_monomial(n**p) for p in range(3)]
    rat = [(cm[p]/cs[p] if cs[p] != 0 else ("0" if cm[p] == 0 else "x/0")) for p in range(3)]
    P(f"   i={r[0]} jk={r[1]}: SM [n^0,n^1,n^2]={cs}  MSSM(MS)={cm}  ratio={rat}")

P("\n4. Gauge x top-Yukawa three-loop terms g_i^3 g_j^2 y_t^2 (SM: n_t=1; MSSM: tr T, DRED)")
for i in (1, 2, 3):
    for j in (1, 2, 3):
        s, m = SMt[i][j], FJJt[i][j]
        P(f"   i={i} j={j}: SM {s} ({float(s):.4g})  MSSM {m} ({float(m):.4g})  ratio {m/s} ({float(m/s):.4g})")
P("   (y_t^MSSM = y_t^SM/sin beta in addition; scheme shift of these terms not applied)")

P("\n5. Structure of the uniform pieces")
# (a) two-matter-loop (n_G^2) mixed pieces factorise as kappa * b_ij^(matter) * b_j^(matter), per generation
bSMm = {(1, 1): R(19, 15), (1, 2): R(3, 5), (1, 3): R(44, 15), (2, 1): R(1, 5), (2, 3): 4, (3, 1): R(11, 30), (3, 2): R(3, 2)}
b1SMm, b1MSm = R(4, 3), 2  # one-loop matter per generation, every factor (complete SU(5) multiplets)
for r in rows:
    i, (j, k) = r[0], r[1]
    if r[2] and j == k and j != i or (i == 1 and (j, k) == (1, 1)):
        n2s = Poly(r[3], n).coeff_monomial(n**2); n2m = Poly(r[5], n).coeff_monomial(n**2)
        ks = n2s/(bSMm[(i, j)]*b1SMm); km = n2m/(2*bSMm[(i, j)]*b1MSm)
        P(f"   n^2 part i={i} jj={j}{j}: SM kappa = {ks}, MSSM kappa = {km}")
        assert ks == -R(11, 12) and km == -R(3, 2)
P("   => n^2 part = kappa b_ij^m b_j^m with kappa_SM = -11/12, kappa_MSSM = -3/2; ratio = 2 (b_ij doubling) x 3/2")
P("      (one-loop matter chiral/Weyl) x 18/11 (kappa ratio) = 54/11 on every mixed entry. These are c_i(jj) entries: invariant only under the ONE-LOOP MS<->DR conversion; a two-loop mixed term m_i g_i^3 g_j^2 with n_G-dependent m_i shifts them (section 0), so 54/11 is scheme-dependent.")
# (b) fully mixed (i,j,k distinct): only Q contributes in both; per-field weight
SQ = {1: R(1, 10), 2: R(3, 2), 3: 1}; CQ = {1: R(1, 60), 2: R(3, 4), 3: R(4, 3)}
for i, (j, k) in [(1, (2, 3)), (2, (1, 3)), (3, (1, 2))]:
    w = SQ[i]*CQ[j]*CQ[k]
    s = Poly(SM[i][(j, k)], n).coeff_monomial(n); m = Poly(FJJ[i][(j, k)], n).coeff_monomial(n)
    P(f"   i={i} jk={(j, k)}: S_i C_j C_k (Q) = {w};  SM weight per Weyl = {s/w}, MSSM weight per chiral = {m/w}")
    assert s/w == -2 and m/w == -16
P("   => fully-mixed g_i^3 g_j^2 g_k^2 term: -2 S_i C_j C_k per Weyl, -16 per chiral: ratio 8 = 2^3, invariant under any redefinition g_j -> g_j(1 + k_j g_j^2).")
P("      The SM has no scalar charged under all three factors, so the scalar weight is not tested by these entries.")


P("\n6. Scheme-invariant entries (cycle 6, referee 1 finding 3c): n_G^1 parts of c_i(ij) and fully mixed c_i(jk)")
inv = {}
for i, j in [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]:
    key = tuple(sorted((i, j)))
    s1 = Poly(SM[i][key], n).coeff_monomial(n); m1 = Poly(FJJ[i][key], n).coeff_monomial(n)
    inv[(i, j)] = m1/s1
    P(f"   c_{i}({i}{j}) [g_{i}^5 g_{j}^2]: SM n^1 {s1}  MSSM n^1 {m1}  ratio {m1/s1}")
for i, key in [(1, (2, 3)), (2, (1, 3)), (3, (1, 2))]:
    s1 = Poly(SM[i][key], n).coeff_monomial(n); m1 = Poly(FJJ[i][key], n).coeff_monomial(n)
    inv[(i, key)] = m1/s1
    P(f"   c_{i}{key} fully mixed: SM n^1 {s1}  MSSM n^1 {m1}  ratio {m1/s1}")
assert inv[(3, 1)] == inv[(3, 2)] == R(2, 7)
assert inv[(2, 1)] == inv[(2, 3)] == R(8, 13)
assert inv[(1, 2)] == inv[(1, 3)] == 8
assert inv[(1, (2, 3))] == inv[(2, (1, 3))] == inv[(3, (1, 2))] == 8
P("   => scheme-invariant entries already disagree: 8 (U(1) row and fully mixed) vs 8/13 (SU(2) row) vs 2/7 (SU(3) row).")
P("      No uniform three-loop factor exists in ANY scheme related to MS/DR by a background-field-compatible redefinition.")

open(__file__.replace(".py", ".txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
