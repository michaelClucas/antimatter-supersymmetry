"""Referee G independent checks for L01b (numpy + sympy only, no imports from tools/ or other calc scripts).

(1) H^c = i sigma2 H*: |H|^2 + |H^c|^2 = 2|H|^2, H^c^dag H = 0, real Jacobian rank 4 (finite differences).
(2) H -> H^c alone is NOT a symmetry of the Yukawa sector: it maps the top operator to a b-type operator,
    so it needs t_R <-> b_R and y_t = y_b (custodial limit) to be a symmetry.
(3) Charge conjugation of Dirac spinors commutes with Lorentz: (i g2) S* (i g2)^-1 = S for random boosts+rotations.
(4) Sector totals of C from field-dependent masses: W 3/2 g^2 + 2 lam, Z+h 3/4(g^2+g'^2) + 4 lam,
    fermions -6 y_t^2 - 6 y_b^2 - 2 y_tau^2, and C = (3/v^2)(m_h^2 + 2 M_W^2 + M_Z^2 - 4 m_t^2) at tree level.
(5) Twin counterfactual H_B := H^c: Hessian eigenvalues {0,0,0,-4 kappa} (independent derivation).
(6) "Second-order" rewriting of a fermion loop as a bosonic determinant: for any D with g5 D g5 = -D,
    det(D + m)^2 = det(m^2 - D^2), so ln Z_F = +1/2 Tr ln(m^2 - D^2) while a boson gives -1/2 Tr ln(...).
    The map from fermion loop to boson-operator determinant exists inside SM content but keeps the
    statistics sign: it cannot cancel anything.
Run from this directory: python refG_check.py
"""
import numpy as np
import sympy as sp

rng = np.random.default_rng(20261125)
out = []


def P(s=""):
    print(s)
    out.append(str(s))


eps = np.array([[0, 1], [-1, 0]], dtype=complex)  # i sigma2


def Hc(H):
    return eps @ H.conj()


# (1)
P("(1) H^c identities")
worst = 0.0
for _ in range(1000):
    H = rng.normal(size=2) + 1j * rng.normal(size=2)
    worst = max(worst, abs(np.vdot(H, H).real + np.vdot(Hc(H), Hc(H)).real - 2 * np.vdot(H, H).real),
                abs(np.vdot(Hc(H), H)))
P(f"  max |(|H|^2+|H^c|^2-2|H|^2)|, |H^c^dag H| over 1000 random H: {worst:.2e}")


def realmap(x):
    H = np.array([x[0] + 1j * x[1], x[2] + 1j * x[3]])
    v = np.concatenate([H, Hc(H)])
    return np.concatenate([v.real, v.imag])


x0 = rng.normal(size=4)
Jn = np.array([(realmap(x0 + 1e-6 * e) - realmap(x0 - 1e-6 * e)) / 2e-6 for e in np.eye(4)]).T
P(f"  Jacobian shape {Jn.shape}, numerical rank {np.linalg.matrix_rank(Jn, tol=1e-8)}  (claim: 4)")

# (2)
P("\n(2) Is H -> H^c (fermions untouched) a symmetry of the Yukawa operators?")
Q = rng.normal(size=2) + 1j * rng.normal(size=2)
t, b = complex(*rng.normal(size=2)), complex(*rng.normal(size=2))
H = rng.normal(size=2) + 1j * rng.normal(size=2)
Ot = lambda H, t: np.vdot(Q, Hc(H)) * t  # noqa: E731
Ob = lambda H, b: np.vdot(Q, H) * b  # noqa: E731
P(f"  O_t(H^c, t) / O_b(H, t) = {Ot(Hc(H), t) / Ob(H, t):.6f}   (H^c^c = -H: top operator -> -(bottom-type operator with t_R))")
P("  So H -> H^c alone maps (Q^dag H^c) t_R to -(Q^dag H) t_R, a different operator with hypercharge mismatch;")
P("  it is a symmetry only combined with t_R <-> b_R and y_t = y_b, g' = 0: the custodial element, as WORK sec. 4d says.")

# (3)
P("\n(3) Charge conjugation commutes with Lorentz on Dirac spinors (Dirac rep)")
s = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])]
I2, Z2 = np.eye(2), np.zeros((2, 2))
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gs = [np.block([[Z2, si], [-si, Z2]]).astype(complex) for si in s]
gam = [g0] + gs
Sig = lambda m, n: 0.25 * (gam[m] @ gam[n] - gam[n] @ gam[m])  # noqa: E731


def expm(A):
    w, V = np.linalg.eig(A)
    return V @ np.diag(np.exp(w)) @ np.linalg.inv(V)


Cm = 1j * gs[1]
worst = 0.0
for _ in range(200):
    w = rng.normal(size=(4, 4)); w = w - w.T  # real antisymmetric omega_{mn}
    S = expm(0.5 * sum(w[m, n] * Sig(m, n) for m in range(4) for n in range(4)))
    worst = max(worst, np.abs(Cm @ S.conj() @ np.linalg.inv(Cm) - S).max())
P(f"  max |(i g2) S* (i g2)^-1 - S| over 200 random Lorentz elements: {worst:.2e}")

# (4)
P("\n(4) Sector totals of C from field-dependent masses (C_i = 1/2 d^2/dphi^2 STr M_i^2)")
phi, g, gp, lam, yt, yb, ytau, mu2 = sp.symbols("phi g gp lam y_t y_b y_tau mu2", positive=True)
MW2, MZ2 = g**2 * phi**2 / 4, (g**2 + gp**2) * phi**2 / 4
mh2, mG2 = 3 * lam * phi**2 - mu2, lam * phi**2 - mu2
mt2, mb2, mtau2 = yt**2 * phi**2 / 2, yb**2 * phi**2 / 2, ytau**2 * phi**2 / 2
half_d2 = lambda e: sp.simplify(sp.diff(e, phi, 2) / 2)  # noqa: E731
CW = half_d2(6 * MW2 + 2 * mG2)
CZ = half_d2(3 * MZ2 + mG2 + mh2)
CF = half_d2(-12 * mt2 - 12 * mb2 - 4 * mtau2)
P(f"  W sector   = {CW}")
P(f"  Z+h sector = {CZ}")
P(f"  fermions   = {CF}")
Ctot = sp.expand(CW + CZ + CF)
P(f"  total C    = {Ctot}")
v = sp.symbols("v", positive=True)
tree = {g: 2 * sp.Symbol("MW") / v, gp: 2 * sp.sqrt(sp.Symbol("MZ")**2 - sp.Symbol("MW")**2) / v,
        lam: sp.Symbol("mh")**2 / (2 * v**2), yt: sp.sqrt(2) * sp.Symbol("mt") / v, yb: 0, ytau: 0}
P(f"  C at tree level in masses = {sp.factor(sp.simplify(Ctot.subs(tree)))}")
P("  (claim: (3/v^2)(m_h^2 + 2 M_W^2 + M_Z^2 - 4 m_t^2))")
num = dict(MW=80.3692, MZ=91.1876, mh=125.20, mt=172.57, v=246.22)
bracket = num["mh"]**2 + 2 * num["MW"]**2 + num["MZ"]**2 - 4 * num["mt"]**2
P(f"  pole-mass form with PDG 2024 centrals: bracket = {bracket:.4e} GeV^2, C = {3*bracket/num['v']**2:.3f}  (WORK: -4.068)")

# (5)
P("\n(5) Twin counterfactual H_B := H^c, independent derivation")
k, l = sp.symbols("kappa lambda", real=True)
p = sp.symbols("p1:5", real=True)
r2 = sum(pi**2 for pi in p) / 2  # |H|^2
V = k * 2 * r2 + l * (2 * r2)**2
hmin2 = sp.simplify(sp.solve(sp.diff(V.subs({p[1]: 0, p[2]: 0, p[3]: 0}), p[0]) / p[0], p[0])[0]**2)
Hs = sp.hessian(V, p).subs({p[1]: 0, p[2]: 0, p[3]: 0}).subs(p[0]**2, hmin2)
P(f"  vev^2 = {hmin2};  Hessian eigenvalues = {sp.simplify(Hs).eigenvals()}")

# (6)
P("\n(6) Fermion determinant vs squared (bosonic) operator, random chiral D")
n = 6
A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
D = np.block([[np.zeros((n, n)), A], [-A.conj().T, np.zeros((n, n))]])  # anti-hermitian, g5 D g5 = -D
g5 = np.diag([1] * n + [-1] * n)
m = 0.7
P(f"  |g5 D g5 + D| = {np.abs(g5 @ D @ g5 + D).max():.1e}")
lhs = 2 * np.log(np.linalg.det(D + m * np.eye(2 * n)))
rhs = np.log(np.linalg.det(m**2 * np.eye(2 * n) - D @ D))
P(f"  2 ln det(D+m) = {lhs.real:.10f}{lhs.imag:+.2e}i ;  ln det(m^2 - D^2) = {rhs.real:.10f}{rhs.imag:+.2e}i")
P("  => ln Z_F = +1/2 Tr ln(m^2 - D^2), ln Z_B = -1/2 Tr ln(m^2 - D^2): equal operators, opposite sign.")
P("  The second-order / worldline rewriting maps the top loop onto a bosonic operator with the same")
P("  field-dependent mass m_t^2(h) and keeps (-1)^F. No cancellation follows from it.")

with open("refG_check_out.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(out) + "\n")
