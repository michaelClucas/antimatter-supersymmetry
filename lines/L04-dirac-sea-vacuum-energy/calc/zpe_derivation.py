"""L04 step 1: zero-point energy of a free real scalar d.o.f. and of a Dirac field (hole-theory sea),
hard 3-momentum cutoff vs dimensional regularization. Run: python zpe_derivation.py"""
import sympy as sp

k, m, L, mu = sp.symbols('k m Lambda mu', positive=True)
eps = sp.symbols('epsilon')

# --- (a) Dirac sea: single-particle Dirac Hamiltonian h(k) = alpha.k + beta m (Dirac rep), k along z
I2 = sp.eye(2); Z2 = sp.zeros(2)
sz = sp.Matrix([[1, 0], [0, -1]])
alpha_z = sp.Matrix(sp.BlockMatrix([[Z2, sz], [sz, Z2]]))
beta = sp.Matrix(sp.BlockMatrix([[I2, Z2], [Z2, -I2]]))
h = alpha_z * k + beta * m
ev = h.eigenvals()
print("Dirac h(k) eigenvalues {value: multiplicity}:", ev)
omega = sp.sqrt(k**2 + m**2)
neg = [e for e in ev if sp.simplify(e + omega) == 0]
E_sea = sum(e * ev[e] for e in neg)
print("Hole theory: filled sea energy per k =", sp.simplify(E_sea))
# Charge-conjugation-symmetric (Heisenberg) ordering: E_vac = 1/2 (sum over negative - sum over positive)
E_sym = sp.Rational(1, 2) * (sum(e * ev[e] for e in ev if sp.simplify(e + omega) == 0)
                             - sum(e * ev[e] for e in ev if sp.simplify(e - omega) == 0))
print("Symmetrized (b b^dag - b^dag b)/2 ordering: E_vac per k =", sp.simplify(E_sym))
print("   (note: this line restates the single-particle sum in the symmetrized form; it is not an independent derivation)")
print("=> per real d.o.f. (Dirac field = 4 d.o.f.): -omega/2; per scalar d.o.f.: +omega/2")
print("   Normal ordering sets it to 0 by subtracting a c-number = choice of bare cosmological constant.")

# --- (a2) where the sign comes from: operator algebra of one mode, no reference to antiparticles
w = sp.symbols('omega', positive=True)
bF = sp.Matrix([[0, 1], [0, 0]])                       # fermion mode, {b, b^dag} = 1
HF = w / 2 * (bF.T * bF - bF * bF.T)                    # antisymmetrized fermion Hamiltonian
Ntr = 8
aB = sp.Matrix(Ntr, Ntr, lambda i, j: sp.sqrt(j) if i == j - 1 else 0)   # truncated boson mode
HB = w / 2 * (aB.T * aB + aB * aB.T)                   # symmetrized boson Hamiltonian
print("one fermion mode, H = w/2 (b^dag b - b b^dag): eigenvalues", list(HF.eigenvals()), "-> vacuum -w/2")
print("one boson mode,   H = w/2 (a^dag a + a a^dag): vacuum level", sp.simplify(HB[0, 0]),
      "(truncation only affects the top level)")
print("Complex scalar = 2 boson modes per k (particle + antiparticle): vacuum +w, positive.")
print("Weyl fermion = 2 fermion modes per k: vacuum -w. Dirac = 4 fermion modes: -2w.")
print("=> sign set by the (anti)commutator, i.e. statistics; having a distinct antiparticle does not change it.\n")

# --- (b) hard cutoff, per bosonic d.o.f.:  rho = 1/2 int d^3k/(2pi)^3 omega,  p = 1/2 int d^3k/(2pi)^3 k^2/(3 omega)
rho = sp.integrate(k**2 * omega, (k, 0, L)) / (4 * sp.pi**2)
p = sp.integrate(k**4 / omega, (k, 0, L)) / (12 * sp.pi**2)
x = sp.symbols('x', positive=True)  # x = m/Lambda
def expand_small(expr):
    e = sp.simplify(expr.subs(m, x * L)).rewrite(sp.log)
    return sp.series(e, x, 0, 6).removeO()
rho_s = expand_small(rho)
p_s = expand_small(p)
rho_s = sp.expand(sp.expand_log(rho_s.subs(x, m / L), force=True))
p_s = sp.expand(sp.expand_log(p_s.subs(x, m / L), force=True))
print("cutoff rho per boson d.o.f. (to O(m^4)):", sp.collect(rho_s, [L, sp.log(m)]))
print("cutoff p   per boson d.o.f. (to O(m^4)):", sp.collect(p_s, [L, sp.log(m)]))
print("rho + p =", sp.collect(sp.simplify(sp.expand(rho_s + p_s)), [L, sp.log(m)]))
# Pauli conditions: sum over species with weight s_i = (-1)^F g_i
print("Species sum of rho: Lambda^4 coefficient ~ Str 1, Lambda^2 ~ Str m^2, ln Lambda ~ Str m^4, finite ~ Str m^4 ln m^2")
c4 = sp.limit(rho_s / L**4, L, sp.oo)
print("  coefficient of Lambda^4:", c4, "   of m^2 Lambda^2:", sp.simplify(rho_s.coeff(L, 2) / m**2),
      "   of m^4 ln Lambda:", sp.simplify(sp.expand(rho_s).coeff(sp.log(L)) / m**4))

# --- (c) dimensional regularization: n = 3 - 2 eps spatial dims
n = 3 - 2 * eps
I_n = sp.gamma(-(n + 1) / 2) / ((4 * sp.pi)**(n / 2) * sp.gamma(sp.Rational(-1, 2))) * m**(n + 1)
rho_dr = sp.Rational(1, 2) * mu**(2 * eps) * I_n
ser = sp.expand(sp.expand_log(sp.series(rho_dr, eps, 0, 1).removeO(), force=True))
pole = sp.simplify(ser.coeff(eps, -1))
fin = sp.simplify(ser.coeff(eps, 0))
print("dim-reg rho per boson d.o.f. = pole/eps + finite")
print('  pole coefficient:', pole, '   finite:', fin)
# MS-bar: mu^2 -> mu^2 e^gamma /(4 pi); show finite part = m^4/(64 pi^2)(ln(m^2/mubar^2) - 3/2)
mub = sp.symbols('mubar', positive=True)
fin_ms = sp.simplify(sp.expand_log(fin.subs(mu, mub * sp.exp(sp.EulerGamma / 2) / sp.sqrt(4 * sp.pi)), force=True))
target = m**4 / (64 * sp.pi**2) * (sp.log(m**2 / mub**2) - sp.Rational(3, 2))
print("  MS-bar finite part minus m^4/(64pi^2)(ln(m^2/mubar^2)-3/2) =", sp.simplify(sp.expand_log(fin_ms - target, force=True)))
# pressure in dim reg: p = -(1/n) * ... use p = 1/2 int k^2/(n omega); int d^nk k^2/omega = n/(n+1)... check rho+p=0
I_p = sp.gamma(-(n + 1) / 2) / ((4 * sp.pi)**(n / 2) * sp.gamma(sp.Rational(1, 2))) * m**(n + 1) * (n / 2) / n
# int d^nk/(2pi)^n k^2 (k^2+m^2)^(-1/2) = (n/2) Gamma(-(n+1)/2)/Gamma(1/2) m^(n+1)/(4pi)^(n/2)
p_dr = sp.Rational(1, 2) * mu**(2 * eps) * I_p
print("  dim-reg rho + p (exact in eps):", sp.simplify(sp.gammasimp(rho_dr + p_dr)))
print("  => w = -1 exactly; only Str m^4 (pole / mu-dependence) and Str m^4 ln m^2 (finite) conditions remain.")
