"""Nucleon-antinucleon freeze-out in the SM early universe (line L03).

Solves the Boltzmann equation for nucleons N = (p, n) and antinucleons Nbar
after the QCD crossover, in two cases:
  (1) symmetric universe, Y_N = Y_Nbar (no baryon asymmetry)  -> Kolb & Turner check
  (2) observed asymmetry, Y_N - Y_Nbar = Y_B = eta * n_gamma / s (eta from tools/sm_inputs.py)

Annihilation input: OBELIX/LEAR data give beta*sigma_ann(pbar p) ~ 40 mb (c=1) for
p_lab = 50-175 MeV/c (Carbonell, Protasov, Zenoni, PLB 397, 345 (1997), nucl-th/9806032).
We take <sigma v> = const and scan 20-120 mb to cover isospin channel differences,
P-wave growth at the higher momenta relevant at T ~ 20-40 MeV, and plasma effects.
We also run sigma v = 1/m_pi^2 (Kolb & Turner's estimate).

Units: GeV, natural units. 1 mb = 2.56819 GeV^-2.
"""
import math, sys, os
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.special import kn, kve

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "tools"))
import sm_inputs as smi

MB_TO_GEV2 = 1.0 / 0.389379  # 1 mb in GeV^-2
M_N = 0.9389  # GeV, isospin-averaged nucleon mass
G_N = 4.0     # p and n, 2 spin states each (per species N or Nbar)
M_PL = smi.M_PLANCK
M_PI = 0.13957

# ---------------- g*(T), g*s(T): ideal gas of SM species, T < ~150 MeV ----------------
# (name, internal dof, statistics +1 fermion / -1 boson, mass GeV)
SPECIES = [
    ("photon", 2, -1, 0.0),
    ("nu (3 LH nu + 3 nubar)", 6, +1, 0.0),  # treated as coupled; fine for T > ~2 MeV
    ("e+-", 4, +1, 0.000511),
    ("mu+-", 4, +1, 0.10566),
    ("pi+-", 2, -1, 0.13957),
    ("pi0", 1, -1, 0.13498),
    ("K", 4, -1, 0.4957),
    ("eta", 1, -1, 0.5479),
    ("rho", 9, -1, 0.775),
    ("omega", 3, -1, 0.7827),
]


def _rho_s(g, stat, m, T):
    """Energy density and entropy density / T^3 normalised so that massless boson gives g."""
    if m == 0.0:
        fac = 7.0 / 8.0 if stat == +1 else 1.0
        return g * fac, g * fac
    z = m / T
    if z > 40:
        return 0.0, 0.0
    f = lambda u: 1.0 / (math.exp(u) + stat)
    # rho = g/(2pi^2) T^4 int u^2 sqrt(u^2-z^2) f du over u>z ; p similar
    rho = quad(lambda u: u * u * math.sqrt(u * u - z * z) * f(u), z, z + 60)[0]
    p = quad(lambda u: (u * u - z * z) ** 1.5 / 3.0 * f(u), z, z + 60)[0]
    grho = g * rho / (2 * math.pi ** 2) / (math.pi ** 2 / 30.0)
    gs = g * (rho + p) / (2 * math.pi ** 2) / (2 * math.pi ** 2 / 45.0)
    return grho, gs


def gstar(T):
    gr = gs = 0.0
    for _, g, st, m in SPECIES:
        a, b = _rho_s(g, st, m, T)
        gr += a
        gs += b
    return gr, gs


_Tgrid = np.logspace(np.log10(0.0008), np.log10(0.16), 200)
_G = np.array([gstar(T) for T in _Tgrid])
_lnT = np.log(_Tgrid)


def gs_of_T(T):
    return np.interp(np.log(T), _lnT, _G[:, 1])


def g_of_T(T):
    return np.interp(np.log(T), _lnT, _G[:, 0])


def gstar_half(T):
    """Gondolo-Gelmini g_*^{1/2} = (g*s/sqrt(g*)) (1 + (1/3) dln g*s / dln T)."""
    dln = np.gradient(np.log(_G[:, 1]), _lnT)
    d = np.interp(np.log(T), _lnT, dln)
    return gs_of_T(T) / math.sqrt(g_of_T(T)) * (1.0 + d / 3.0)


def entropy(T):
    return 2 * math.pi ** 2 / 45.0 * gs_of_T(T) * T ** 3


def Yeq(x):
    """Equilibrium yield of N (or Nbar) at zero chemical potential, full Bessel form."""
    T = M_N / x
    n = G_N / (2 * math.pi ** 2) * M_N ** 2 * T * kn(2, x)
    return n / entropy(T)


def lnYeq(x):
    T = M_N / x
    return (math.log(G_N / (2 * math.pi ** 2) * M_N ** 2 * T * kve(2, x)) - x
            - math.log(entropy(T)))


def lam(x, sv):
    T = M_N / x
    return math.sqrt(math.pi / 45.0) * M_PL * M_N * gstar_half(T) * sv / x ** 2


X0, X1 = 8.0, 900.0  # T from 117 MeV (just below QCD crossover) to ~1 MeV


def solve_symmetric(sv):
    # use u = ln Y
    def rhs(x, u):
        Y = math.exp(u[0])
        ye = Yeq(x)
        return [-lam(x, sv) * (Y - ye * ye / Y)]
    sol = solve_ivp(rhs, (X0, X1), [math.log(Yeq(X0))], method="Radau", rtol=1e-9, atol=1e-12,
                    dense_output=True)
    Yinf = math.exp(sol.y[0, -1])
    # freeze-out x_f: where Y exceeds Yeq by factor 2.5 (Y - Yeq = 1.5 Yeq)
    xs = np.linspace(X0, 80, 4000)
    xf = next((x for x in xs if math.exp(sol.sol(x)[0]) > 2.5 * Yeq(x)), float("nan"))
    return Yinf, xf


def solve_asymmetric(sv, YB):
    """ln Ybar; Y_N = Ybar + YB. Equilibrium: Y_N Y_Nbar = Yeq^2 (mu_N = -mu_Nbar)."""
    def rhs(x, u):
        Yb = math.exp(u[0]) if u[0] > -700 else 0.0
        return [-lam(x, sv) * (Yb + YB - math.exp(2 * lnYeq(x) - u[0]))]
    ye0 = Yeq(X0)
    Yb0 = 0.5 * (-YB + math.sqrt(YB * YB + 4 * ye0 * ye0))
    sol = solve_ivp(rhs, (X0, X1), [math.log(Yb0)], method="Radau", rtol=1e-10, atol=1e-6)
    return sol.y[0, -1]  # ln Ybar(final)


def omega_h2(Y, m=M_N):
    T0 = 2.7255 / 1.160452e13  # K -> GeV
    s0 = 2 * math.pi ** 2 / 45.0 * (2 + 7.0 / 8.0 * 6 * 4.0 / 11.0) * T0 ** 3  # GeV^3
    s0_cm3 = s0 / (1.97327e-14) ** 3
    rho_c_over_h2 = 1.05368e-5  # GeV cm^-3
    return m * Y * s0_cm3 / rho_c_over_h2, s0_cm3


if __name__ == "__main__":
    out = []
    p = lambda s="": (print(s), out.append(s))
    p("g*(T) check (should be ~10.75 at T=5 MeV, ~14 at T=50 MeV, rising with pions):")
    for T in [0.005, 0.02, 0.05, 0.1, 0.15]:
        gr, gs = gstar(T)
        p(f"  T={1e3*T:6.1f} MeV  g*={gr:6.2f}  g*s={gs:6.2f}  g*^1/2(GG)={gstar_half(T):5.2f}")
    _, s0 = omega_h2(1.0)
    p(f"s0 = {s0:.1f} cm^-3")
    n_gamma_over_s = (2 * 1.2020569 / math.pi ** 2) / (2 * math.pi ** 2 / 45 * (2 + 7 / 8 * 6 * 4 / 11))
    YB = smi.ETA_B * n_gamma_over_s
    p(f"Y_B = eta * n_gamma/s = {smi.ETA_B:.2e} * {n_gamma_over_s:.4f} = {YB:.3e}")
    p("")
    p("(1) SYMMETRIC universe (no asymmetry): relic Y = n_N/s = n_Nbar/s")
    p(f"{'sigma v':>22} {'x_f':>6} {'T_f/MeV':>8} {'Y_N=Y_Nbar':>11} {'eta_sym':>10} {'Omega h2 (N+Nbar)':>18} {'ratio to 0.12':>14}")
    cases = [("1/m_pi^2", 1 / M_PI ** 2)] + [(f"{s:.0f} mb", s * MB_TO_GEV2) for s in (20, 40, 60, 120)]
    for name, sv in cases:
        Y, xf = solve_symmetric(sv)
        om, _ = omega_h2(2 * Y)
        eta_sym = Y / n_gamma_over_s
        p(f"{name:>10} ({sv/MB_TO_GEV2:6.1f} mb) {xf:6.1f} {1e3*M_N/xf:8.1f} {Y:11.3e} {eta_sym:10.2e} {om:18.3e} {om/smi.OMEGA_C_H2:14.2e}")
    p("")
    p("(2) OBSERVED asymmetry: relic antinucleons Y_Nbar")
    for name, sv in cases:
        lnYb = solve_asymmetric(sv, YB)
        p(f"{name:>10}: ln(Y_Nbar) = {lnYb:.4e}  -> log10 = {lnYb/math.log(10):.4e}  (i.e. Y_Nbar ~ 10^({lnYb/math.log(10):.3g}))")
    # Interpretation check: with the asymmetry, Nbar never freezes out before T ~ 1 MeV.
    # It tracks chemical equilibrium Y_Nbar = Yeq^2 / Y_N ~ Yeq^2 / Y_B, which is sigma v independent.
    lneq = 2 * lnYeq(X1) - math.log(YB)
    p(f"chemical-equilibrium value at x={X1:.0f} (T={1e3*M_N/X1:.2f} MeV): ln(Yeq^2/Y_B) = {lneq:.4e}")
    for name, sv in cases[:1] + cases[2:3]:
        p(f"  {name}: Gamma_ann(Nbar)/H ~ lambda*Y_B*x at x={X1:.0f}: {lam(X1, sv)*YB*X1:.2e}  (>>1: still in equilibrium)")
    p("  -> the asymmetric antinucleon yield is set by Yeq^2/Y_B ~ exp(-2 m_N/T) down to T << 1 MeV;")
    p("     the number above is an upper bound on the true relic (which keeps falling).")
    p("")
    p("Required for Omega h^2 = 0.12 with m = m_N: Y_tot =",)
    Yreq = smi.OMEGA_C_H2 / omega_h2(1.0)[0]
    p(f"  Y_tot = {Yreq:.3e}  (= {Yreq/YB:.2f} x Y_B)")
    with open(os.path.join(os.path.dirname(__file__), "freezeout_output.txt"), "w") as f:
        f.write("\n".join(out) + "\n")
