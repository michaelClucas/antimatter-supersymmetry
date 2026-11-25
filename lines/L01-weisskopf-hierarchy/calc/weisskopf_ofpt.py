"""Weisskopf (1939) electron self-energy in hole theory, old-fashioned (time-ordered) perturbation theory.

Electron at rest, Coulomb gauge, sharp cutoff K on photon 3-momentum k. Natural Heaviside-Lorentz units,
e^2 = 4 pi alpha. Spin-averaged over the rest spinor (makes every integrand a rotation scalar, so k is put along z).
All integrands are per d^3k/(2pi)^3 = k^2 dk/(2 pi^2).

Pieces (Dirac Hamiltonian H(p) = alpha.p + beta m, E = sqrt(k^2+m^2), Lam_pm(p) = (1 pm H(p)/E)/2):
  C1  one-electron Coulomb self-energy        (1/2) e^2/k^2 * <1>
  Cs  Coulomb exchange with the filled sea    (1/2) e^2/k^2 * <-2 Lam_-(k)>
      C1 + Cs = (1/2) e^2/k^2 <Lam_+ - Lam_->  (hole-theory Coulomb term)
  Ta  transverse, electron-only intermediate state e(-k)+gamma(k):
        (e^2/2k) sum_pol <a.eps Lam_+(-k) a.eps> / (m - E - k)
  Tb  transverse, pair intermediate state: vacuum fluctuation e(0,s) ebar(-k) gamma(k) that is
      Pauli-blocked by the electron present; removing it from the vacuum energy gives
        + (e^2/2k) sum_pol <a.eps Lam_-(k) a.eps> / (m + E + k)
  Tneg (only for comparison) one-electron Dirac theory WITHOUT a sea, where the electron may jump
      into negative-energy states: (e^2/2k) sum_pol <a.eps Lam_-(-k) a.eps>/(m + E - k)  -> quadratic divergence.
"""
import sympy as sp

k, m, alpha = sp.symbols('k m alpha', positive=True)
e2 = 4 * sp.pi * alpha
E = sp.sqrt(k**2 + m**2)

I2 = sp.eye(2)
Z2 = sp.zeros(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])


def blk(a, b, c, d):
    return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))


beta = blk(I2, Z2, Z2, -I2)
al = [blk(Z2, s, s, Z2) for s in (sx, sy, sz)]
P0 = (sp.eye(4) + beta) / 2  # positive-energy rest projector (2 spin states)


def H(pz):
    return al[2] * pz + beta * m


def Lam(sign, pz):
    return (sp.eye(4) + sign * H(pz) / sp.sqrt(pz**2 + m**2)) / 2


def avg(X):
    """spin-averaged expectation in the electron-at-rest state"""
    return sp.simplify((P0 * X).trace() / 2)


eps = [al[0], al[1]]  # alpha.eps for the two transverse polarizations of k || z


def polsum(L):
    return sp.simplify(sum(avg(a * L * a) for a in eps))


meas = k**2 / (2 * sp.pi**2)  # d^3k/(2pi)^3 -> dk

C1 = meas * sp.Rational(1, 2) * e2 / k**2
Cs = meas * sp.Rational(1, 2) * e2 / k**2 * avg(-2 * Lam(-1, k))
Ta = meas * e2 / (2 * k) * polsum(Lam(+1, -k)) / (m - E - k)
Tb = meas * e2 / (2 * k) * polsum(Lam(-1, k)) / (m + E + k)
Tneg = meas * e2 / (2 * k) * polsum(Lam(-1, -k)) / (m + E - k)

pieces = {'C1 (one-electron Coulomb)': C1, 'Cs (sea exchange Coulomb)': Cs,
          'Ta (e + gamma intermediate)': Ta, 'Tb (Pauli-blocked pair)': Tb,
          'Tneg (no-sea neg-energy jump)': Tneg}

out = []
P = lambda s: (print(s), out.append(str(s)))
P("Integrands d(delta m)/dk and their large-k expansion (x = 1/k):")
x = sp.symbols('x', positive=True)
for name, f in pieces.items():
    f = sp.simplify(f)
    ser = sp.series(f.subs(k, 1 / x), x, 0, 2).removeO()
    P(f"  {name:32s} = {f}")
    P(f"      large k: {sp.simplify(ser.subs(x, 1/k))}")

hole_total = sp.simplify(C1 + Cs + Ta + Tb)
P("\nHole-theory total integrand (C1+Cs+Ta+Tb):")
P(f"  {hole_total}")
ser = sp.series(hole_total.subs(k, 1 / x), x, 0, 3).removeO()
P(f"  large-k expansion: {sp.expand(sp.simplify(ser.subs(x, 1/k)))}")
P(f"  O(k^0) term (would be a LINEAR divergence): {sp.limit(hole_total, k, sp.oo)}")
P(f"  coefficient of 1/k (log divergence): {sp.simplify(sp.limit(hole_total * k, k, sp.oo))}"
  f"   expected 3 alpha m/(2 pi) = {3*alpha*m/(2*sp.pi)}")

P("\nLinear-divergence bookkeeping (k -> infinity limit of each integrand, i.e. coefficient of K):")
for name, f in pieces.items():
    P(f"  {name:32s}: {sp.limit(f, k, sp.oo)}")
P(f"  Coulomb  C1 + Cs : {sp.limit(C1 + Cs, k, sp.oo)}")
P(f"  Transverse Ta + Tb: {sp.limit(Ta + Tb, k, sp.oo)}")
P(f"  Tneg / k as k->inf (quadratic divergence coefficient of K^2/2): {sp.limit(Tneg / k, k, sp.oo)}")

P("\nChiral-symmetry check: hole-theory integrand at m = 0:")
P(f"  {sp.simplify(hole_total.subs(m, 0))}   (vanishes identically -> delta m proportional to m)")
P(f"  Ta+Tb at m=0: {sp.simplify((Ta+Tb).subs(m, 0))};  C1+Cs at m=0: {sp.simplify((C1+Cs).subs(m, 0))}")
P(f"  one-electron theory C1+Ta at m=0: {sp.simplify((C1+Ta).subs(m, 0))}  (nonzero -> mass generated from m=0)")

# finite part with cutoff K (numerical): delta m/m - (3 alpha/2pi) ln(K/m) -> constant
import mpmath as mp
fnum = sp.lambdify((k,), (hole_total / (alpha * m / sp.pi)).subs(m, 1), 'mpmath')
for Kv in (1e2, 1e4, 1e6):
    I = mp.quad(fnum, [0, 1, 10, Kv])
    P(f"  K/m = {Kv:8.0e}: delta m / (alpha m/pi) = {float(I):.6f};  minus (3/2) ln(K/m) = {float(I - 1.5*mp.log(Kv)):.6f}")
P("  -> delta m = (3 alpha/2pi) m [ln(K/m) + c], c = (2/3)*(constant above); c is cutoff-scheme dependent.")

with open(__file__.replace('.py', '_out.txt'), 'w') as fh:
    fh.write("\n".join(out) + "\n")
