"""
L05 cycle 8: scope fixes and the cross-method gate-7 check.

Sections
  1. SM + complex scalar (8,3,0) (referee 2 finding 3b): still one Higgs doublet, but minimal SUSY != Phi*.
  2. Diagonal criterion with real scalars (referee 2 finding 6), derived symbolically.
  3. Conjugation blindness of b_i, b_ij: replacing ANY subset of image fields by their conjugates leaves b_i, b_ij
     unchanged (random test). Odd invariants: an example of a conjugation-odd quadratic-in-Casimir trace that is
     not an anomaly coefficient (referee 2 finding 2), so the blindness is a loop-order statement.
  4. Order dependence of the "H^c step" share of the B shift (referee 3 finding 3): all 6 orderings + Shapley value,
     and the order-independent log(r) share.
  5. Gate 7, cross-method: SUSY b_ij obtained by expanding the NSVZ formula (instanton derivation, no Feynman-diagram
     general formula) vs the SM tables of MSS 1201.5868 (direct diagrammatic, QGRAF/MINCER) and BPV 1210.6873
     (background-field diagrams). Tests b(SUSY) = 2 b(SM) on i != j and (1,1).
Conventions as c6_scope.py. Run from calc/: python c8_scope.py (output c8_scope.txt)
"""
import random, itertools, math
from sympy import Rational as R, Matrix, symbols, zeros, cancel, series, expand, simplify, log, nsimplify, S

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

nG = symbols("n_G")

class G:
    def __init__(self, factors):
        self.f = factors; self.n = len(factors)
    def field(self, per_factor):
        res = []
        for i in range(self.n):
            mult = 1
            for k in range(self.n):
                if k != i:
                    mult *= per_factor[k][0]
            res.append((per_factor[i][1]*mult, per_factor[i][2]))
        return res

def b1(th, F=(), Sc=(), Sr=()):
    v = [R(-11, 3)*th.f[i][0] for i in range(th.n)]
    for fl, w in ((F, R(2, 3)), (Sc, R(1, 3)), (Sr, R(1, 6))):
        for x in fl:
            for i in range(th.n):
                v[i] += w*x[i][0]
    return v

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
    r = {}
    for i in range(th.n):
        for j in range(th.n):
            if i != j or th.f[i][1]:
                r[(i+1, j+1)] = cancel(A[i, j]/B[i, j]) if B[i, j] != 0 else ("0/0" if A[i, j] == 0 else "x/0")
    return r

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

# ------------------------------------------------------------------ 1
P("1. SM + complex scalar (8,3,0) [SU(3) octet, SU(2) triplet, Y=0; a real rep]. Still exactly one Higgs doublet.")
X = f(3, 8, 0)
par = b2(SMG, gen(3), [H, X])
mini = b2s(SMG, gen(3) + [H, Hc, X])          # minimal SUSY: one chiral (8,3,0) is anomaly-free and Witten-safe
phis = b2s(SMG, gen(3) + [H, Hc, X, X])       # Phi*: two chirals
rm, rp = ratios(mini, par, SMG), ratios(phis, par, SMG)
P("   minimal SUSY / parent:", rm)
P("   Phi* / parent        :", rp)
assert rm[(2, 3)] == rm[(3, 2)] == R(18, 17)
assert all(v == 2 for v in rp.values())
P("   -> 18/17 on (2,3),(3,2) for minimal SUSY (referee 2 reproduced); Phi* gives 2. 'One Higgs doublet' is not enough;")
P("      the hypothesis is: the parent's only complex scalar is one |Y|=1/2 doublet (real scalars in real reps allowed,")
P("      see next line), equivalently: minimal SUSY completion = Phi*.")
# a real (8,3,0) scalar instead: minimal SUSY one chiral = Phi*
rr = ratios(b2s(SMG, gen(3) + [H, Hc, X]), b2(SMG, gen(3), [H], [X]), SMG)
assert all(v == 2 for v in rr.values())
P("   with a REAL (8,3,0) scalar in the parent, one chiral = Phi*, ratio 2 everywhere (asserted).")

# ------------------------------------------------------------------ 2
P("\n2. Non-abelian diagonal entry under Phi*: doubles iff 25 C(G) = 7 S_F - 4 S_Sc - 2 S_Sr")
CG, SF, Sc, Sr, Off = symbols("CG S_F S_c S_r Off")
diag_parent = -R(34, 3)*CG**2 + CG*(R(10, 3)*SF + R(2, 3)*Sc + R(1, 3)*Sr) + Off
# Phi*: chiral per Weyl and per real scalar, two per complex scalar; Off (S_iC_i-type part) doubles by the theorem
diag_susy = -6*CG**2 + 2*CG*(SF + Sr + 2*Sc) + 2*Off
cond = expand((diag_susy - 2*diag_parent)*3/(2*CG))
P("   (b_ii[Phi*] - 2 b_ii[T]) * 3/(2 C(G)) =", cond)
assert expand(cond - (25*CG - 7*SF + 4*Sc + 2*Sr)) == 0
P("   = (25 C(G) - 7 S_F + 4 S_Sc + 2 S_Sr): criterion with the real-scalar term (asserted).")

# ------------------------------------------------------------------ 3
P("\n3. Conjugation blindness, and its limit")
random.seed(8)
reps = [(1, 1), (2, 1), (1, 3), (2, 3), (3, 1), (1, 8), (3, 3), (2, 8), (3, 8)]
for _ in range(100):
    content = [(random.choice(reps), R(random.randint(-6, 6), 6)) for _ in range(random.randint(1, 7))]
    flip = [random.random() < 0.5 for _ in content]
    A = [f(*rep, Y) for (rep, Y) in content]
    B = [f(*rep, -Y if fl else Y) for ((rep, Y), fl) in zip(content, flip)]   # conjugate: Y -> -Y, 3 -> 3bar (same S, C)
    assert b2s(SMG, A) == b2s(SMG, B) and b2(SMG, A, A) == b2(SMG, B, B) and b1(SMG, A) == b1(SMG, B)
P("   100 random contents, random subsets conjugated: b_i and b_ij unchanged (Weyl, complex scalar, chiral) - asserted.")
P("   Reason: they depend on fields only through S_i(R), C_j(R) (quadratic in Y, T^a), which obey S(Rbar)=S(R), C(Rbar)=C(R).")
# odd invariant example: sum_f Y_f C2(f) C3(f) d(f) over one SM generation (Weyl, LH basis); conjugation flips its sign
def oddinv(fields):
    tot = 0
    for (d2, d3, Y) in fields:
        C2 = T2[d2][1]; C3 = T3[d3][1]
        tot += Y*C2*C3*d2*d3
    return tot
gen1 = [(2, 3, R(1, 6)), (1, 3, R(-2, 3)), (1, 3, R(1, 3)), (2, 1, R(-1, 2)), (1, 1, 1)]
v = oddinv(gen1)
P(f"   odd mixed trace sum_f Y C2 C3 d over one generation = {v} (not an anomaly coefficient; flips sign under conjugation)")
assert v != 0
P("   -> such traces can in principle enter higher-loop gauge betas; 'conjugate = duplicate' is proved only for b_i, b_ij")
P("      and the three-loop gauge-only entries actually compared in C4.5, not to all orders.")

# ------------------------------------------------------------------ 4
P("\n4. Order dependence of the 'H^c step' share of the B shift")
rr_ = symbols("r")
def Bof(r):
    return (1 - r/2)/(2 + r/5)
rSM = R(-1, 11)
steps = {"Hc": R(2), "Hchiral": R(3), "gaugino": R(11, 9)}
assert Bof(rSM) == R(115, 218) and Bof(rSM*2*3*R(11, 9)) == R(5, 7)
tot = Bof(rSM*2*3*R(11, 9)) - Bof(rSM)
P(f"   B: SM {Bof(rSM)} -> full {R(5, 7)}, total shift {tot} = {float(tot):.4f}")
def v(Sset):
    m = 1
    for k in Sset:
        m *= steps[k]
    return Bof(rSM*m) - Bof(rSM)
names = list(steps)
shap = {k: 0 for k in names}
P("   marginal increment of each step, by ordering:")
for perm in itertools.permutations(names):
    done = []; row = []
    for k in perm:
        inc = v(done + [k]) - v(done); shap[k] += inc/6; done.append(k)
        row.append(f"{k} {float(inc/tot)*100:5.1f}%")
    P("     " + " -> ".join(perm) + ":  " + ", ".join(row))
P("   Shapley shares (average over the 6 orderings):", {k: f"{float(shap[k]/tot)*100:.1f}%" for k in names})
assert sum(shap.values()) == tot
hc = [v([k for k in perm[:perm.index('Hc')]] + ['Hc']) - v([k for k in perm[:perm.index('Hc')]]) for perm in itertools.permutations(names)]
P(f"   H^c step range over orderings: {float(min(hc)/tot)*100:.1f}% .. {float(max(hc)/tot)*100:.1f}%;"
  f" Shapley {float(shap['Hc']/tot)*100:.1f}%")
P(f"   order-independent: in r the H^c step is a factor 2 of 22/3; log share ln2/ln(22/3) = {math.log(2)/math.log(22/3)*100:.1f}%")

# ------------------------------------------------------------------ 5
P("\n5. Gate 7 cross-method: NSVZ-expanded SUSY b_ij vs direct-diagrammatic SM tables")
# NSVZ (Novikov-Shifman-Vainshtein-Zakharov NPB 229 (1983) 381), per factor i, units 16 pi^2 = 1, no Yukawas:
#   beta_i = -g_i^3 [3 C(G_i) - sum_R S_i(R) (1 - gamma_R)] / (1 - 2 C(G_i) g_i^2),  gamma_R = -4 sum_j g_j^2 C_j(R)
# (NSVZ normalisation gamma = -C(R) alpha/pi; product-group form: Shifman, IJMPA 11 (1996) 5761, hep-ph/9606281 [citation from memory, uncertain]; the product form is also checked here by reproducing the FJJ / Martin-Vaughn MSSM table).
gs = symbols("g1 g2 g3", positive=True); eps = symbols("eps")
chis = gen(nG) + [H, Hc]
def nsvz_bij():
    M = zeros(3, 3)
    for i in range(3):
        CGi = SMG.f[i][0]
        num = 3*CGi
        for x in chis:
            gam = -4*sum(eps*gs[j]**2*x[j][1] for j in range(3))
            num -= x[i][0]*(1 - gam)
        beta = -num/(1 - 2*CGi*eps*gs[i]**2)       # beta_i / g_i^3, eps counts loops
        ser = series(beta, eps, 0, 2).removeO()
        two = expand(ser.coeff(eps, 1))
        for j in range(3):
            M[i, j] = expand(two.coeff(gs[j], 2))
    return M
NS = nsvz_bij()
assert (NS - MSSM).expand() == zeros(3, 3)
P("   NSVZ two-loop expansion reproduces the MSSM b_ij(n_G) of FJJ / Martin-Vaughn (asserted).")
SM_MSS = 16*Matrix([[R(9, 800)+19*nG/240, R(9, 160)+3*nG/80, 11*nG/60],
                    [R(3, 160)+nG/80, -R(259, 96)+49*nG/48, nG/4],
                    [11*nG/480, 3*nG/32, -R(51, 8)+19*nG/12]])
Nc, CF, TF, CA = 3, R(4, 3), R(1, 2), 3
SM_BPV = Matrix([
    [nG*(R(137, 900)*Nc + R(81, 100)) + R(9, 50), nG*(R(1, 20)*Nc + R(9, 20)) + R(9, 10), nG*R(11, 15)*CF*Nc],
    [nG*(R(1, 60)*Nc + R(3, 20)) + R(3, 10), nG*(R(49, 12)*Nc + R(49, 12)) - R(259, 6), nG*CF*Nc],
    [nG*R(11, 15)*TF, 3*TF*nG, nG*(R(40, 3)*CA*TF + 8*CF*TF) - R(34, 3)*CA**2]])
for nm, Tb in (("MSS 1201.5868 (QGRAF/MINCER diagrams)", SM_MSS), ("BPV 1210.6873 (background-field diagrams)", SM_BPV)):
    r = ratios(NS, Tb, SMG)
    assert all(v == 2 for v in r.values())
    P(f"   NSVZ / {nm}: ratios on i!=j and (1,1), all n_G: {sorted(set(map(str, r.values())))} -> PASS")
P("   Neither side uses the Machacek-Vaughn or Jones/Martin-Vaughn general two-loop formulas from which the theorem is proved.")
P("   This is still a mathematical consistency check (no measurement can test it).")

open(__file__.replace(".py", ".txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
