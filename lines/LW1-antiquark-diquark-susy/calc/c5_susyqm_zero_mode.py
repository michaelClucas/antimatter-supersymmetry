"""LW1 cycle 4, c5b: the LFHQCD supercharge (Brodsky, de Teramond, Dosch, Lorce, arXiv:1604.06746, eqs. 6-13)
is Witten SUSY quantum mechanics in the light-front radial variable x (zeta). There, unlike c5a,
{R, R^dag} IS the Hamiltonian (the LF mass-squared operator G). Questions:
  1. Does the partner degeneracy and the unpaired zero mode come out? (Model content, check numerically.)
  2. Is there a "protection" theorem? In SUSY QM, the zero mode E0 = 0 is exact for ANY superpotential W
     with normalisable exp(-int W). Test: deform W (SUSY-preserving) vs deform H directly (SUSY-breaking)
     by the same-size term and compare the shift of the ground state.

Superpotential (equivalent to the paper's R_lambda = Q + lambda S with q = -d/dx + f/x, up to the constant
shift in eq. 11): W(x) = lam x - g/x. With q = -d/dx + W:
  H_B = q^dag q = -d2 + W^2 + W'  ->  -d2 + lam^2 x^2 + g(g+1)/x^2 + lam(1-2g)   spectrum 4 lam (n+1)
  H_M = q q^dag = -d2 + W^2 - W'  ->  -d2 + lam^2 x^2 + g(g-1)/x^2 - lam(1+2g)   spectrum 4 lam n
H_M has the zero mode psi0 = x^g exp(-lam x^2/2) (annihilated by q^dag). Meson tower {0, 4lam, 8lam, ...},
partner tower {4lam, 8lam, ...}: equal except the unpaired zero mode (the pion in LFHQCD).
Units lam = 1. Finite differences, Dirichlet at both ends.
Caveat: this toy has the same sl(1|1) structure as the paper's G = {R, R^dag} (paired towers, one unpaired
zero mode). It does not reproduce the paper's L labels (there the 2D centrifugal term (4L^2-1)/(4x^2) and the
constant 2 lam (f -/+ 1/2) of eqs. 12-13 fix L_M = L_B + 1); only the index structure is tested.
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal

lam, g = 1.0, 1.0  # g = 1 <-> L_M = 0 meson tower (pion family) with an L_B = 0 partner tower
N, X = 6000, 9.0
x = np.linspace(X / N, X, N)
h = x[1] - x[0]


def spectrum(V, k=6):
    diag = 2.0 / h**2 + V
    off = -np.ones(N - 1) / h**2
    return eigh_tridiagonal(diag, off, select="i", select_range=(0, k - 1))[0]


def partners(W, dW):
    return spectrum(W**2 - dW), spectrum(W**2 + dW)  # (H_M, H_B)


W = lam * x - g / x
dW = lam + g / x**2
EM, EB = partners(W, dW)
print("1. Undeformed LFHQCD-type SUSY QM (lam = 1, g = 1)")
print("   H_M (meson side):  ", np.round(EM, 4), " exact 4n:", [4 * n for n in range(6)])
print("   H_B (baryon side): ", np.round(EB, 4), " exact 4(n+1):", [4 * (n + 1) for n in range(6)])
print(f"   pairing: H_M level n+1 vs H_B level n, max diff = {np.max(np.abs(EM[1:] - EB[:-1])):.2e};"
      f" unpaired zero mode E0 = {EM[0]:.2e}")

print("\n2. Protection test. Same-size deformation, two ways:")
print("   (a) SUSY-preserving: W -> W + eps x^3 (H_M = W^2 - W', H_B = W^2 + W' recomputed)")
print("   (b) SUSY-breaking:   H_M -> H_M + 2 eps lam x^4 (the leading term (a) adds to W^2), H_B unchanged")
print("   eps     E0(a)       E0(b)       pair split (a)   pair split (b)")
for eps in [0.0, 0.01, 0.03, 0.1]:
    Wa = W + eps * x**3
    dWa = dW + 3 * eps * x**2
    EMa, EBa = partners(Wa, dWa)
    EMb = spectrum(W**2 - dW + 2 * eps * lam * x**4)
    EBb = EB
    sa = np.max(np.abs(EMa[1:4] - EBa[0:3]))
    sb = np.max(np.abs(EMb[1:4] - EBb[0:3]))
    print(f"   {eps:<6} {EMa[0]:+.2e}   {EMb[0]:+.2e}   {sa:.2e}         {sb:.2e}")
print("   (a): E0 stays 0 to grid accuracy and towers stay paired for every eps. (b): E0 moves at O(eps).")
print("\n3. Explicit SUSY breaking by quark masses (paper eqs. 23-25): Delta M^2 depends on the constituents,")
print("   so each hadron gets its own shift. Then E0 = m_pi^2 != 0 and the pairing splits; the zero mode is")
print("   'protected' only in the chiral limit, which is the same statement as chiral symmetry (GMOR).")
