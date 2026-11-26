"""
L05 cycle 8: does the Yukawa sector / anomaly cancellation carry an antimatter-specific (conjugation-sensitive) map
from the SM onto the MSSM?  Exact sympy throughout; third generation only (y_t, y_b, y_tau), as in the line.

Sections
  1. Operator selection. Which cubic gauge-invariant Yukawa (SM) / holomorphic superpotential (SUSY) operators exist
     when the second doublet is the conjugate (Y = -1/2) or a duplicate (Y = +1/2).
  2. Anomalies of the higgsino sector: Tr Y^3, Tr Y, SU(2)^2 U(1), SU(3)^2 U(1), Witten parity.
  3. One-loop Yukawa betas computed from the general component formula (Machacek-Vaughn NPB 236 (1984) 221;
     Luo-Wang-Xiao PRD 67 (2003) 065019 eq. (33), two-component fermions, kappa = 1/2) with explicit real scalar
     components, for: SM (one doublet H, down/lepton via H^c = i sigma2 H*), 2HDM-II (independent H_u, H_d),
     2HDM with a duplicate Y=+1/2 doublet H' used through H'^c. And from the SUSY formula
     beta_Y = Y gamma + perms, gamma = 1/2 Y Y* - 2 g^2 C (Martin-Vaughn PRD 50 (1994) 2282) for the MSSM.
     Decomposition into leg wave-function terms and vertex terms.
  4. Two-loop pure-gauge (g^4) terms of the Yukawa betas: SM / 2HDM-II from Luo-Wang-Xiao eq. (35) g^4 terms with
     product-group rules; MSSM from the two-loop chiral anomalous dimension (Martin-Vaughn eq. (2.4)). Ratios.
  5. Two-loop Yukawa-dependent MSSM terms (SUSY side only; the SM two-loop Yukawa^4 and g^2 Yukawa^2 terms were not
     recomputed here).
Run from calc/: python c8_yukawa.py  (output c8_yukawa.txt)
"""
import itertools
from sympy import Rational as R, sqrt, I, symbols, zeros, Matrix, expand, conjugate, simplify, Poly, nsimplify, S

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

yt, yb, yl = symbols("y_t y_b y_tau", positive=True)
g1, g2, g3 = symbols("g1 g2 g3", positive=True)
GS = (g1, g2, g3)

# ---------------------------------------------------------------- field data (LH Weyl basis), GUT-normalised U(1)
# rep: (d2, d3, Y)
REP = {"Q": (2, 3, R(1, 6)), "u": (1, 3, R(-2, 3)), "d": (1, 3, R(1, 3)), "L": (2, 1, R(-1, 2)), "e": (1, 1, 1),
       "H": (2, 1, R(1, 2)), "Hc": (2, 1, R(-1, 2)), "Hp": (2, 1, R(1, 2))}
C2 = {1: 0, 2: R(3, 4)}; C3 = {1: 0, 3: R(4, 3)}
def cas(name):
    d2, d3, Y = REP[name]
    return (R(3, 5)*Y**2, C2[d2], C3[d3])
def Csum(name):
    c = cas(name)
    return sum(GS[a]**2*c[a] for a in range(3))

# ---------------------------------------------------------------- 1. operator selection
P("1. Operator selection (hypercharge + SU(2) doublet count + colour); third generation")
def allowed(fields):
    d2 = sum(1 for x in fields if REP[x][0] == 2); Y = sum(REP[x][2] for x in fields)
    col = [REP[x][1] for x in fields]
    colour_ok = col.count(3) in (0, 2)   # one 3 and one 3bar (Q with u/d); trivially true here
    return d2 in (0, 2) and Y == 0 and colour_ok
ops = [("Q", "u"), ("Q", "d"), ("L", "e")]
P("   SM (one doublet H; H^c = i sigma2 H* has Y=-1/2 and is the SAME field):")
for f1, f2 in ops:
    w = [s for s in ("H", "Hc") if allowed((f1, f2, s))]
    P(f"     {f1} {f2} x: allowed with {w}")
assert allowed(("Q", "u", "H")) and allowed(("Q", "d", "Hc")) and allowed(("L", "e", "Hc"))
assert not allowed(("Q", "d", "H")) and not allowed(("Q", "u", "Hc"))
P("   -> with one doublet, u-type mass needs H, d-type and lepton masses need its conjugate H^c: the SM is forced to use both.")
P("   SUSY (holomorphic W: chiral superfields only, no conjugates). Second doublet = conjugate-type H_d (Y=-1/2):")
for f1, f2 in ops:
    P(f"     {f1} {f2} x: {[s for s in ('H', 'Hc') if allowed((f1, f2, s))]}")
P("   Second doublet = duplicate H' (Y=+1/2):")
for f1, f2 in ops:
    P(f"     {f1} {f2} x: {[s for s in ('H', 'Hp') if allowed((f1, f2, s))]}")
assert not any(allowed((a, b, s)) for (a, b) in ops[1:] for s in ("H", "Hp"))
P("   -> with a duplicate, y_b = y_tau = 0 is forced in W; with the conjugate-type H_d all three SM Yukawas map one-to-one.")
P("   In a NON-SUSY theory a duplicate H' (Y=+1/2) can give d, e masses through H'^c: H_d <-> H'^c is a field redefinition.")
P("   So conjugate vs duplicate is distinguishable only on the SUSY side (holomorphy fixes which superfield carries Y=-1/2).")

# ---------------------------------------------------------------- 2. anomalies
P("\n2. Higgsino anomalies (LH Weyl higgsinos; SM fermions are anomaly-free by themselves)")
def anom(names):
    tY3 = sum(REP[n][2]**3*REP[n][0]*REP[n][1] for n in names)
    tY = sum(REP[n][2]*REP[n][0]*REP[n][1] for n in names)
    t22Y = sum(REP[n][2]*R(1, 2)*REP[n][1] for n in names if REP[n][0] == 2)
    t33Y = sum(REP[n][2]*R(1, 2)*REP[n][0] for n in names if REP[n][1] == 3)
    ndbl = sum(REP[n][1] for n in names if REP[n][0] == 2)
    return tY3, tY, t22Y, t33Y, ndbl
smgen = ["Q", "u", "d", "L", "e"]
base = anom(smgen)
assert base[:4] == (0, 0, 0, 0) and base[4] == 4
P("   one SM generation: Tr Y^3 = Tr Y = SU(2)^2U(1) = SU(3)^2U(1) = 0, doublets = 4 (x3 generations = 12, even)")
for lab, hs in (("H~ only", ["H"]), ("H~ + H~_d (conjugate)", ["H", "Hc"]), ("H~ + H~' (duplicate)", ["H", "Hp"])):
    a = anom(hs)
    P(f"   {lab:24s}: Tr Y^3 = {a[0]}, Tr Y = {a[1]}, SU(2)^2U(1) = {a[2]}, Witten doublets added = {a[4]} ({'odd' if a[4] % 2 else 'even'})")
assert anom(["H", "Hc"])[:4] == (0, 0, 0, 0) and anom(["H", "Hc"])[4] % 2 == 0
assert anom(["H", "Hp"])[0] != 0 and anom(["H"])[4] % 2 == 1
P("   -> only the conjugate pair cancels all anomalies; the duplicate cancels Witten parity but not Tr Y^3, Tr Y, SU(2)^2U(1).")
P("      The anomaly-free pair H~_u, H~_d is one Dirac fermion whose particle and antiparticle carry H and H^c charges.")

# ---------------------------------------------------------------- 3. one-loop, component level
P("\n3. One-loop Yukawa betas from component formulas")
# Weyl fermion index list
ferm = [("Q", c, a) for c in range(3) for a in range(2)] + [("u", c, None) for c in range(3)] + \
       [("d", c, None) for c in range(3)] + [("L", None, a) for a in range(2)] + [("e", None, None)]
fidx = {k: i for i, k in enumerate(ferm)}
NF = len(ferm)

def build(model):
    """model: 'SM', '2HDM', 'DUP'. Returns list of real scalars and list of Yukawa matrices Y^a (NF x NF), with
    -L = 1/2 Y^a_ij psi_i psi_j phi_a + h.c."""
    # complex doublets present
    doublets = {"SM": ["H"], "2HDM": ["Hu", "Hd"], "DUP": ["H", "Hp"]}[model]
    reals = [(dname, comp, part) for dname in doublets for comp in range(2) for part in (0, 1)]
    ridx = {k: i for i, k in enumerate(reals)}
    NS = len(reals)
    Y = [zeros(NF, NF) for _ in range(NS)]
    def field(dname, comp, conj):
        """complex component as vector over reals: z = (phi_re + i phi_im)/sqrt2"""
        v = [0]*NS
        v[ridx[(dname, comp, 0)]] = 1/sqrt(2)
        v[ridx[(dname, comp, 1)]] = (-I if conj else I)/sqrt(2)
        return v
    def add(coef, fa, fb, vec):
        i, j = fidx[fa], fidx[fb]
        for a in range(NS):
            if vec[a] != 0:
                Y[a][i, j] += coef*vec[a]; Y[a][j, i] += coef*vec[a]
    up = {"SM": "H", "2HDM": "Hu", "DUP": "H"}[model]
    # conjugate doublet components: X^c = (X_2*, -X_1*)  (index 0 = upper)
    def dn(comp):
        if model == "SM":
            return ("H", 1 - comp, True, 1 if comp == 0 else -1)
        if model == "2HDM":
            return ("Hd", comp, False, 1)
        return ("Hp", 1 - comp, True, 1 if comp == 0 else -1)
    for c in range(3):
        # y_t eps_{ab} Q^a X^b u, eps_{01} = +1
        add(yt, ("Q", c, 0), ("u", c, None), field(up, 1, False))
        add(-yt, ("Q", c, 1), ("u", c, None), field(up, 0, False))
        for qa, b, sgn in ((0, 1, 1), (1, 0, -1)):
            dname, comp, cj, s2 = dn(b)
            add(sgn*s2*yb, ("Q", c, qa), ("d", c, None), field(dname, comp, cj))
    for la, b, sgn in ((0, 1, 1), (1, 0, -1)):
        dname, comp, cj, s2 = dn(b)
        add(sgn*s2*yl, ("L", None, la), ("e", None, None), field(dname, comp, cj))
    return reals, Y

def dag(M):
    return M.conjugate().T

def beta1(Y):
    NS = len(Y)
    Y2F = zeros(NF, NF)
    for b in range(NS):
        Y2F += dag(Y[b])*Y[b]
    Y2Fs = Y2F.conjugate()
    res = []
    for a in range(NS):
        t = R(1, 2)*(Y2Fs*Y[a] + Y[a]*Y2F)
        for b in range(NS):
            t += 2*Y[b]*dag(Y[a])*Y[b]
            t += Y[b]*R(1, 2)*((dag(Y[a])*Y[b]).trace() + (dag(Y[b])*Y[a]).trace())   # 2 kappa Y2^{ab}(S), kappa = 1/2
        res.append(t.applyfunc(lambda z: expand(simplify(z))))
    return res

def extract(model):
    reals, Y = build(model)
    B = beta1(Y)
    # read beta_{y} from one entry, then assert the full tensor equals the predicted pattern
    coeffs = {}
    for yname, ys, (fa, fb) in (("y_t", yt, (("Q", 0, 0), ("u", 0, None))), ("y_b", yb, (("Q", 0, 0), ("d", 0, None))),
                                 ("y_tau", yl, (("L", None, 0), ("e", None, None)))):
        i, j = fidx[fa], fidx[fb]
        for a in range(len(Y)):
            if Y[a][i, j] != 0:
                coeffs[yname] = expand(simplify(B[a][i, j]/Y[a][i, j]*ys))
                break
    # consistency: beta^a == sum_y (beta_y/y) * dY^a/dy * y   for all a
    for a in range(len(Y)):
        pred = Y[a].applyfunc(lambda z: expand(z.diff(yt)*coeffs["y_t"] + z.diff(yb)*coeffs["y_b"] + z.diff(yl)*coeffs["y_tau"]))
        assert (B[a] - pred).applyfunc(lambda z: simplify(z)) == zeros(NF, NF), (model, a)
    return {k: expand(v/{"y_t": yt, "y_b": yb, "y_tau": yl}[k]) for k, v in coeffs.items()}

res = {m: extract(m) for m in ("SM", "2HDM", "DUP")}
def row(e):
    return tuple(Poly(e, yt, yb, yl).coeff_monomial(m) for m in (yt**2, yb**2, yl**2))
P("   Yukawa part of 16pi^2 beta_y / y, coefficients of (y_t^2, y_b^2, y_tau^2):")
for m in res:
    P(f"     {m:5s}: " + ", ".join(f"{k} {row(v)}" for k, v in res[m].items()))
SMk = {"y_t": (R(9, 2), R(3, 2), 1), "y_b": (R(3, 2), R(9, 2), 1), "y_tau": (3, 3, R(5, 2))}
for k in SMk:
    assert row(res["SM"][k]) == SMk[k]
P("   SM reproduces the standard one-loop result y_t(3/2 y_t^2 - 3/2 y_b^2 + Y2(S)), Y2(S)=3y_t^2+3y_b^2+y_tau^2, etc. (asserted)")
assert all(row(res["2HDM"][k]) == row(res["DUP"][k]) for k in SMk)
P("   2HDM-II (H_u, H_d with Y=-1/2) and duplicate (H, H' with Y=+1/2, down via H'^c): identical (asserted) - field redefinition.")

# leg decomposition (non-SUSY): fermion legs 1/2 Y2(F), scalar leg Y2(S), vertex 2 Y^b Y^{+a} Y^b
WF_F = {"y_t": (R(3, 2), R(1, 2), 0), "y_b": (R(1, 2), R(3, 2), 0), "y_tau": (0, 0, R(3, 2))}  # Q:1/2(t+b), u:t, d:b, L:1/2 l, e:l
WF_H2 = {"y_t": (3, 0, 0), "y_b": (0, 3, 1), "y_tau": (0, 3, 1)}          # gamma(H_u) = 3y_t^2, gamma(H_d) = 3y_b^2 + y_tau^2
WF_SM = {"y_t": (3, 3, 1), "y_b": (3, 3, 1), "y_tau": (3, 3, 1)}           # Y2(S) of the single H
VTX = {"y_t": (0, -2, 0), "y_b": (-2, 0, 0), "y_tau": (0, 0, 0)}
add3 = lambda *vs: tuple(sum(x) for x in zip(*vs))
for k in SMk:
    assert row(res["2HDM"][k]) == add3(WF_F[k], WF_H2[k])
    assert row(res["SM"][k]) == add3(WF_F[k], WF_SM[k], VTX[k])
P("   decomposition (asserted):  2HDM-II = fermion legs + own-doublet leg;  SM = fermion legs + Y2(S) + vertex")
P("     identification terms SM - 2HDM-II:", {k: tuple(a - b for a, b in zip(row(res['SM'][k]), row(res['2HDM'][k]))) for k in SMk})
P("     = [Y2(S) - gamma(own doublet)] + vertex, vertex = -2 y_b^2 in beta_t, -2 y_t^2 in beta_b, 0 in beta_tau")
P("   sum rule: Y2(S)_SM = gamma_Yuk(H_u) + gamma_Yuk(H_d) = 3y_t^2 + (3y_b^2 + y_tau^2): the SM Higgs leg sees both")
P("     MSSM Higgs legs because H^c is the conjugate of the same field. The vertex term exists only for that reason")
P("     (it is a charged-scalar exchange between the y_t and y_b vertices, which share the single H).")

# SUSY one loop
sfs = ferm + [("Hu", None, a) for a in range(2)] + [("Hd", None, a) for a in range(2)]
sidx = {k: i for i, k in enumerate(sfs)}; NSF = len(sfs)
Yt = {}
def addW(coef, a, b, c):
    for p in itertools.permutations((sidx[a], sidx[b], sidx[c])):
        Yt[p] = Yt.get(p, 0) + coef
for c in range(3):
    for qa, h, s in ((0, 1, 1), (1, 0, -1)):
        addW(s*yt, ("Q", c, qa), ("Hu", None, h), ("u", c, None))
        addW(s*yb, ("Q", c, qa), ("Hd", None, h), ("d", c, None))
for la, h, s in ((0, 1, 1), (1, 0, -1)):
    addW(s*yl, ("L", None, la), ("Hd", None, h), ("e", None, None))
gam = zeros(NSF, NSF)
for (i, p, q), v in Yt.items():
    for j in range(NSF):
        w = Yt.get((j, p, q), 0)
        if w:
            gam[i, j] += R(1, 2)*conjugate(v)*w
gam = gam.applyfunc(expand)
def ssusy(i, j, k):
    t = 0
    for p in range(NSF):
        t += Yt.get((i, j, p), 0)*gam[p, k] + Yt.get((i, p, k), 0)*gam[p, j] + Yt.get((p, j, k), 0)*gam[p, i]
    return expand(t)
susy = {}
for yname, ys, trip in (("y_t", yt, (("Q", 0, 0), ("Hu", None, 1), ("u", 0, None))),
                        ("y_b", yb, (("Q", 0, 0), ("Hd", None, 1), ("d", 0, None))),
                        ("y_tau", yl, (("L", None, 0), ("Hd", None, 1), ("e", None, None)))):
    ijk = tuple(sidx[x] for x in trip)
    susy[yname] = expand(ssusy(*ijk)/Yt[ijk])
P("   MSSM (Yukawa part):", ", ".join(f"{k} {row(v)}" for k, v in susy.items()))
MSk = {"y_t": (6, 1, 0), "y_b": (1, 6, 1), "y_tau": (0, 3, 4)}
for k in MSk:
    assert row(susy[k]) == MSk[k]
    assert row(susy[k]) == add3(tuple(2*x for x in WF_F[k]), WF_H2[k])
P("   MSSM = 2 x (fermion-leg terms) + (own-doublet leg), vertex 0 (non-renormalisation)  [asserted]")
P("   So under H -> H_u, H^c -> H_d:  fermion legs DOUBLE exactly; the SM Higgs leg Y2(S) SPLITS into gamma(H_u)+gamma(H_d)")
P("   (each Yukawa keeps only its own doublet's share); the SM vertex term (-2) is DROPPED.")

# gauge parts, one loop
P("   gauge part, one loop: SM -3 sum_{fermion legs} C,  MSSM -2 sum_{all three legs} C")
for yname, legs in (("y_t", ("Q", "u", "H")), ("y_b", ("Q", "d", "Hc")), ("y_tau", ("L", "e", "Hc"))):
    sm = -3*(Csum(legs[0]) + Csum(legs[1])); ms = -2*(Csum(legs[0]) + Csum(legs[1]) + Csum(legs[2]))
    P(f"     {yname}: SM {sm},  MSSM {ms},  MSSM - (2/3) SM = {expand(ms - R(2, 3)*sm)} (= -2 C(Higgs leg))")
    assert expand(ms - R(2, 3)*sm + 2*Csum(legs[2])) == 0
assert expand(-3*(Csum("Q") + Csum("u")) + R(17, 20)*g1**2 + R(9, 4)*g2**2 + 8*g3**2) == 0
P("   -> fermion-leg gauge terms scale by 2/3 (not 2); the Higgs leg is new; C(H) = C(H^c): the gauge part is conjugation-blind.")

# ---------------------------------------------------------------- 4. two-loop g^4 terms
P("\n4. Two-loop pure-gauge (g^4) terms of 16pi^2... beta_y / y")
kap = R(1, 2)
CGv = (0, 2, 3)
def SF(nG=3):   # sum over Weyl fermions of Dynkin index (GUT U(1)): per generation (2, 2, 2)
    return (2*nG, 2*nG, 2*nG)
def SSreal(ndoublets):  # real-scalar counting: complex doublet -> (3/5, 1, 0)
    return (R(3, 5)*ndoublets, ndoublets, 0)
def lwx_g4(f1, f2, s, ndbl):
    """Luo-Wang-Xiao eq. (35), g^4 terms, product-group rules: products of two Casimirs on different lines -> products
    of sums; single-line self-energy insertions (C(G), S2) -> sum over the factor."""
    sf, ss = SF(), SSreal(ndbl)
    cf1, cf2, cs = cas(f1), cas(f2), cas(s)
    Cf1, Cf2, Cs = Csum(f1), Csum(f2), Csum(s)
    t = -R(3, 2)*(Cf1**2 + Cf2**2) + 6*Cs*(Cf1 + Cf2) - R(21, 2)*Cs**2
    for a in range(3):
        t += GS[a]**4*(-R(97, 6)*CGv[a] + R(10, 3)*kap*sf[a] + R(11, 12)*ss[a])*(cf1[a] + cf2[a])
        t += GS[a]**4*cs[a]*(R(49, 4)*CGv[a] - 2*kap*sf[a] - R(1, 4)*ss[a])
    return expand(t)
def susy_g4(legs, nH=2):
    S_R = (R(33, 5), 7, 6) if nH == 2 else None   # MSSM: b_i + 3 C(G) = sum S
    t = 0
    for x in legs:
        c = cas(x)
        t += 2*sum(GS[a]**4*c[a]*(S_R[a] - 3*CGv[a]) for a in range(3)) + 4*Csum(x)**2
    return expand(t)
mon = [g1**4, g2**4, g3**4, g1**2*g2**2, g1**2*g3**2, g2**2*g3**2]
def co(e):
    p = Poly(e, *GS)
    return [p.coeff_monomial(m) for m in mon]
SMt = lwx_g4("Q", "u", "H", 1)
known_t = [R(1187, 600), R(-23, 4), -108, R(-9, 20), R(19, 15), 9]
assert co(SMt) == known_t
P("   SM y_t g^4 terms (g1^4, g2^4, g3^4, g1g2, g1g3, g2g3):", co(SMt))
P("     = (1187/600, -23/4, -108, -9/20, 19/15, 9), the standard SM values (as recalled, not re-read); the g3^4 entry -108 equals")
P("       -2(202/3 - 20 n_f/9), n_f = 6, the two-loop QCD quark-mass anomalous dimension (Nachtmann-Wetzel NPB 187 (1981) 333)")
assert -2*(R(202, 3) - R(20, 9)*6) == -108
MSt = susy_g4(("Q", "u", "H"))
assert co(MSt) == [R(2743, 450), R(15, 2), R(-16, 9), 1, R(136, 45), 8]
P("   MSSM y_t g^4 terms:", co(MSt), "(agree with the standard MSSM values as recalled by the author; not re-read from a paper this cycle)")
for yname, legs in (("y_t", ("Q", "u", "H")), ("y_b", ("Q", "d", "Hc")), ("y_tau", ("L", "e", "Hc"))):
    s1, s2, ms = co(lwx_g4(legs[0], legs[1], legs[2], 1)), co(lwx_g4(legs[0], legs[1], legs[2], 2)), co(susy_g4(legs))
    rat = [(m/s if s != 0 else ("0/0" if m == 0 else "x/0")) for m, s in zip(ms, s1)]
    P(f"   {yname}: SM {s1}")
    P(f"          2HDM-II {s2}")
    P(f"          MSSM {ms}")
    P(f"          MSSM/SM {rat}")
    # conjugation blindness: replacing Hc by H (Y -> -Y) in the leg list changes nothing
    if legs[2] == "Hc":
        assert lwx_g4(legs[0], legs[1], "H", 1) == lwx_g4(legs[0], legs[1], "Hc", 1)
P("   -> no uniform factor (ratios differ entry by entry, with sign flips); all g^4 terms depend only on Casimirs,")
P("      so they are conjugation-blind (H^c vs H: identical, asserted).")

# ---------------------------------------------------------------- 5. two-loop MSSM Yukawa-dependent (SUSY side)
P("\n5. MSSM two-loop Yukawa-dependent terms (Martin-Vaughn gamma^(2), legs summed; SUSY side only)")
def gamma2_yuk(i):
    """-1/2 Y_imn Y^npq Y_pqr Y^mri  +  sum_a g_a^2 Y_ipq Y^ipq [2C_a(p) - C_a(i)], diagonal element i"""
    t = 0
    for (a_, m, n), v1 in Yt.items():
        if a_ != i:
            continue
        for (n2, p, q), v2 in Yt.items():
            if n2 != n:
                continue
            for (p2, q2, r), v3 in Yt.items():
                if (p2, q2) != (p, q):
                    continue
                v4 = Yt.get((m, r, i), 0)
                if v4:
                    t += -R(1, 2)*conjugate(v1)*v2*conjugate(v3)*v4
    for (a_, p, q), v in Yt.items():
        if a_ != i:
            continue
        nm_p, nm_i = sfs[p][0], sfs[i][0]
        nm_p = {"Hu": "H", "Hd": "Hc"}.get(nm_p, nm_p); nm_i = {"Hu": "H", "Hd": "Hc"}.get(nm_i, nm_i)
        t += conjugate(v)*v*(2*Csum(nm_p) - Csum(nm_i))
    return expand(t)
tops = (("Q", 0, 0), ("Hu", None, 1), ("u", 0, None))
yt2 = expand(sum(gamma2_yuk(sidx[x]) for x in tops))
P("   MSSM beta^(2)_{y_t}/y_t, Yukawa-dependent part:", yt2)
expect = -22*yt**4 - 5*yb**4 - 5*yt**2*yb**2 - yb**2*yl**2 + (R(6, 5)*g1**2 + 6*g2**2 + 16*g3**2)*yt**2 + R(2, 5)*g1**2*yb**2
assert expand(yt2 - expect) == 0
P("   = -22y_t^4 - 5y_b^4 - 5y_t^2y_b^2 - y_b^2y_tau^2 + (6/5g1^2 + 6g2^2 + 16g3^2)y_t^2 + 2/5 g1^2 y_b^2 (asserted against")
P("     the standard MSSM result as recalled, e.g. Barger-Berger-Ohmann PRD 47 (1993) 1093; not re-read this cycle)")
P("   The SM two-loop Yukawa^4 and g^2 Yukawa^2 terms were not recomputed here.")

open(__file__.replace(".py", ".txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
