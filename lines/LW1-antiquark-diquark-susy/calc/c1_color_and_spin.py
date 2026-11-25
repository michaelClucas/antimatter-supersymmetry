"""LW1 calc 1: group theory behind antiquark <-> diquark exchange.

(a) Numerically verify that the antisymmetric part of 3x3 of SU(3)_c carries the same
    quadratic Casimir as the antiquark rep 3bar (C2 = 4/3), and the symmetric part is the 6 (C2 = 10/3).
    Also verify the color-singlet projection: an antisymmetric (3bar) diquark + quark makes a singlet,
    exactly like antiquark + quark.
(b) Spin algebra for the heavy-quark superflavor hyperfine ratio
    Delta(QQq: 3/2 - 1/2) / Delta(Qbar q: 1 - 0) = 3/4.
    Model: H_hf = (c / m_Q) * sum_i T_i.T_q (s_i . s_q) over heavy constituents i.
    For the meson, the heavy antiquark carries T = T(3bar). For the diquark in 3bar,
    each heavy quark's color-magnetic coupling to the light quark projected on the
    antisymmetric-color, symmetric-spin (S=1) diquark state equals half the diquark's total
    (T_1 + T_2 acting on 3bar = T(3bar), and T_1 = T_2 by exchange symmetry). Then
    sum_i (T_i.T_q) s_i -> (T_3bar.T_q)/2 * (s_1+s_2).
"""
import itertools
import numpy as np
import sympy as sp

# --- (a) Gell-Mann matrices
l = np.zeros((8, 3, 3), dtype=complex)
l[0][0, 1] = l[0][1, 0] = 1
l[1][0, 1] = -1j; l[1][1, 0] = 1j
l[2][0, 0] = 1; l[2][1, 1] = -1
l[3][0, 2] = l[3][2, 0] = 1
l[4][0, 2] = -1j; l[4][2, 0] = 1j
l[5][1, 2] = l[5][2, 1] = 1
l[6][1, 2] = -1j; l[6][2, 1] = 1j
l[7] = np.diag([1, 1, -2]) / np.sqrt(3)
T = l / 2
Tbar = -np.conj(T)  # antiquark generators
I3 = np.eye(3)

def casimir(gens):
    return sum(g @ g for g in gens)

C3 = casimir(T)
C3bar = casimir(Tbar)
print("(a) SU(3) colour")
print("  C2(3)    =", np.round(np.real(C3[0, 0]), 6))
print("  C2(3bar) =", np.round(np.real(C3bar[0, 0]), 6))

# two-quark generators on 3x3
T2 = np.array([np.kron(t, I3) + np.kron(I3, t) for t in T])
C2qq = casimir(T2)
# antisymmetrizer / symmetrizer
P = np.zeros((9, 9))
for i, j in itertools.product(range(3), range(3)):
    P[3 * j + i, 3 * i + j] = 1
A = (np.eye(9) - P) / 2
S = (np.eye(9) + P) / 2
evA = np.linalg.eigvalsh(A @ C2qq @ A)
evS = np.linalg.eigvalsh(S @ C2qq @ S)
print("  C2 on antisym(3x3) nonzero eigs:", sorted(set(np.round(evA[np.abs(evA) > 1e-9], 6))), " dim =", int(round(np.trace(A))))
print("  C2 on sym(3x3)     nonzero eigs:", sorted(set(np.round(evS[np.abs(evS) > 1e-9], 6))), " dim =", int(round(np.trace(S))))

# colour factor <T_d . T_q> in singlet for (3bar diquark)+(quark) vs (antiquark)+(quark)
# T_d.T_q = (C2(singlet) - C2(3bar) - C2(3))/2 = -4/3 in both cases
print("  <T_x.T_q> in singlet, x = antiquark or 3bar diquark: (0 - 4/3 - 4/3)/2 =", sp.Rational(0 - sp.Rational(4, 3) - sp.Rational(4, 3), 2))
# per-quark colour factor inside the diquark+quark singlet: T_1.T_q = T_2.T_q = (-4/3)/2
print("  per-heavy-quark factor T_i.T_q in (QQ)_3bar q singlet = -2/3 (half of -4/3)")

# --- (b) spin algebra with sympy
def SdotS(J, S1, S2):
    return sp.Rational(1, 2) * (J * (J + 1) - S1 * (S1 + 1) - S2 * (S2 + 1))

h = sp.Rational(1, 2)
meson = SdotS(1, h, h) - SdotS(0, h, h)
# baryon: heavy spin S=1 diquark with light quark; coupling (1/2) * S_d . s_q
baryon = sp.Rational(1, 2) * (SdotS(sp.Rational(3, 2), 1, h) - SdotS(h, 1, h))
print("\n(b) superflavor hyperfine ratio")
print("  meson  J=1 minus J=0      (units c T.T / m_Q):", meson)
print("  baryon J=3/2 minus J=1/2  (units c T.T / m_Q):", baryon)
print("  ratio baryon/meson =", sp.nsimplify(baryon / meson))
