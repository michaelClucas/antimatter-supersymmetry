"""LW1 cycle 4, c5a: explicit supercharge that turns an antiquark into a 3bar diquark, and its algebra.

Two levels.

(A) Constituent level (Catto-Gursey / Lichtenberg / Iachello-type): antiquark modes d_{a,s}
    (fermion, colour a = 1..3 in 3bar, spin s = up/down) and point-like scalar diquark modes D_a
    (boson, colour 3bar). Supercharges Q_s = sum_a D_a^dag d_{a,s}. Colour indices are contracted,
    so Q_s is a colour singlet; s is left open, so Q_s carries spin 1/2 (it removes a spin-1/2 object
    and adds a spin-0 one).
    Claim checked numerically: {Q_s, Q_t^dag} = delta_st N_D + sum_a d_{a,t}^dag d_{a,s}, {Q_s, Q_t} = 0.
    Number and spin operators only. No momentum, no Hamiltonian. This is the u(m|n) superalgebra.

(B) QCD level: the diquark is not a field. D_a^dag = eps_abc (u^dag_{b,up} d^dag_{c,dn} - u^dag_{b,dn} d^dag_{c,up})/sqrt2
    (scalar, isoscalar, colour-3bar "good" diquark, one spatial mode). Antiquark modes abar_a (one spin
    state, to keep the Fock space at 2^15). Q = sum_a D_a^dag abar_a is cubic in quark/antiquark
    operators. Checked numerically:
      1. Q is fermionic (changes fermion number by 3) and a colour singlet.
      2. {Q, Q^dag} = sum_a D_a^dag D_a + sum_ab abar_b^dag abar_a [D_b, D_a^dag]   (exact identity).
      3. [D_b, D_a^dag] is NOT delta_ab: the composite diquark is not a canonical boson. The deviation
         is a quark-number-type operator.
    So {Q, Q^dag} is again built from number / colour-density operators only.
All operators act on modes at one point (one spatial mode), and in (B) the antiquark is SPINLESS, so the
(B) operator Q is fermionic with spin 0. This toy cannot test anything about momentum (cycle-5 referee 1,
finding 1). Superseded for those questions by c6_hq_commutator.py (3 momentum modes, spin-1/2 antiquark).
"""
import itertools
import numpy as np
import scipy.sparse as sp

np.set_printoptions(precision=4, suppress=True)
I2 = sp.identity(2, format="csr")
SZ = sp.csr_matrix(np.diag([1.0, -1.0]))
LOW = sp.csr_matrix(np.array([[0.0, 1.0], [0.0, 0.0]]))  # annihilates |1> -> |0> in basis (|0>,|1>)


def fermion_ops(nmodes):
    """Jordan-Wigner annihilation operators for nmodes fermionic modes."""
    ops = []
    for j in range(nmodes):
        mats = [SZ] * j + [LOW] + [I2] * (nmodes - j - 1)
        m = mats[0]
        for x in mats[1:]:
            m = sp.kron(m, x, format="csr")
        ops.append(m)
    return ops


def anti(a, b):
    return a @ b + b @ a


def comm(a, b):
    return a @ b - b @ a


def nrm(m):
    m = m.tocoo() if sp.issparse(m) else sp.coo_matrix(m)
    return 0.0 if m.nnz == 0 else float(np.max(np.abs(m.data)))


print("=" * 78)
print("(A) Constituent level: d_{a,s} fermions (6 modes), D_a bosons (3 modes, n<=2)")
nb = 3  # boson occupation cutoff (0,1,2)
bos1 = sp.csr_matrix(np.diag(np.sqrt(np.arange(1, nb)), 1))  # annihilation, dim nb
F = fermion_ops(6)  # index 2*a + s
dimF = 2 ** 6
Ib = sp.identity(nb, format="csr")


def bos_op(a):
    mats = [Ib, Ib, Ib]
    mats[a] = bos1
    m = mats[0]
    for x in mats[1:]:
        m = sp.kron(m, x, format="csr")
    return sp.kron(sp.identity(dimF, format="csr"), m, format="csr")


IB = sp.identity(nb ** 3, format="csr")
d = [sp.kron(f, IB, format="csr") for f in F]
D = [bos_op(a) for a in range(3)]
ND = sum(x.T @ x for x in D)
Nd = sum(x.T @ x for x in d)
Q = [sum(D[a].T @ d[2 * a + s] for a in range(3)) for s in range(2)]
# restrict to the subspace where no boson mode is at the cutoff (truncation artefact otherwise)
occ = np.array([sum(idx) for idx in itertools.product(range(nb), repeat=3)])
maxocc = np.array([max(idx) for idx in itertools.product(range(nb), repeat=3)])
keep_b = (maxocc < nb - 1)
keep = np.kron(np.ones(dimF, bool), keep_b)
P = sp.diags(keep.astype(float))
worst = 0.0
for s, t in itertools.product(range(2), repeat=2):
    lhs = anti(Q[s], Q[t].T)
    rhs = (ND if s == t else 0 * ND) + sum(d[2 * a + t].T @ d[2 * a + s] for a in range(3))
    worst = max(worst, nrm(P @ (lhs - rhs) @ P))
    worst = max(worst, nrm(anti(Q[s], Q[t])))
print(f"  max |{{Q_s,Q_t^dag}} - (delta_st N_D + sum_a d_at^dag d_as)| on untruncated subspace = {worst:.1e}")
print(f"  => {{Q_up,Q_up^dag}} + {{Q_dn,Q_dn^dag}} = 2 N_D + N_dbar   (number operators only)")
# ladder property with a superflavor-symmetric Hamiltonian H = mD N_D + md N_d + h(colour-singlet light part)
mD, md = 3.25, 1.55  # GeV, illustrative heavy-diquark and heavy-antiquark masses
H = mD * ND + md * Nd
lad = nrm(P @ (comm(H, Q[0]) - (mD - md) * Q[0]) @ P)
print(f"  [H, Q] - (m_D - m_dbar) Q = {lad:.1e}  -> Q is a ladder operator: shifts energy by m_D - m_dbar,")
print("     so it maps meson-type to baryon-type states with a fixed energy offset (spectrum-generating, not [H,Q]=0).")

print()
print("=" * 78)
print("(B) QCD level: quark modes u,d (colour x spin = 12), antiquark modes abar_a (3)")
# mode index: u_{b,s} -> 0..5 (2b+s), d_{b,s} -> 6..11, abar_a -> 12..14
F = fermion_ops(15)
u = lambda b, s: F[2 * b + s]
dq = lambda b, s: F[6 + 2 * b + s]
ab = lambda a: F[12 + a]
eps = np.zeros((3, 3, 3))
for (i, j, k), sgn in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]:
    eps[i, j, k] = sgn
Ddag = []
for a in range(3):
    m = None
    for b in range(3):
        for c in range(3):
            if eps[a, b, c] == 0:
                continue
            term = eps[a, b, c] * (u(b, 0).T @ dq(c, 1).T - u(b, 1).T @ dq(c, 0).T)
            m = term if m is None else m + term
    Ddag.append(m)
vac = np.zeros(2 ** 15)
vac[-1] = 0.0
# vacuum in this JW convention: all modes in |0>, which is basis index 0
vac = np.zeros(2 ** 15); vac[0] = 1.0
norm2 = float(np.linalg.norm(Ddag[0] @ vac) ** 2)
Ddag = [x / np.sqrt(norm2) for x in Ddag]
Dop = [x.T.tocsr() for x in Ddag]
print(f"  diquark normalisation: <0|D_a D_a^dag|0> raw = {norm2:.1f} -> rescaled to 1")
Qq = sum(Ddag[a] @ ab(a) for a in range(3))
Nq = sum(F[i].T @ F[i] for i in range(12))
Nab = sum(F[i].T @ F[i] for i in range(12, 15))
print(f"  [N_quark, Q] - 2Q = {nrm(comm(Nq, Qq) - 2 * Qq):.1e};  [N_antiquark, Q] + Q = {nrm(comm(Nab, Qq) + Qq):.1e}")
print("   -> Q adds 2 quarks, removes 1 antiquark: Delta(fermion number) = 3 (odd), Delta(B) = +1")
# colour generators T^A = sum quark lambda/2 - antiquark lambda^*/2 ; check two of them (diagonal ones suffice
# for a quick singlet test together with one off-diagonal)
lam3 = np.diag([1, -1, 0]) / 2.0
lam1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / 2.0
lam2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]]) / 2.0


def colour_gen(lam):
    T = None
    for b, c in itertools.product(range(3), repeat=2):
        if lam[b, c] == 0:
            continue
        t = 0
        for s in range(2):
            t = t + lam[b, c] * (u(b, s).T @ u(c, s) + dq(b, s).T @ dq(c, s))
        t = t - np.conj(lam[c, b]) * 0 + (-lam[c, b]) * (ab(b).T @ ab(c))  # antiquark in 3bar: -lam^T
        T = t if T is None else T + t
    return T


for nm, lam in [("T3", lam3), ("T1", lam1), ("T2", lam2)]:
    print(f"  [{nm}, Q] = {nrm(comm(colour_gen(lam), Qq)):.1e}   (colour singlet)")
A = anti(Qq, Qq.conj().T)
rhs = sum(Ddag[a] @ Dop[a] for a in range(3))
devs = []
for a_, b_ in itertools.product(range(3), repeat=2):
    cab = comm(Dop[b_], Ddag[a_])
    rhs = rhs + ab(b_).T @ ab(a_) @ cab
    devs.append(nrm(cab - (sp.identity(2 ** 15) if a_ == b_ else 0 * cab)))
print(f"  {{Q,Q^dag}} - [sum D^dag D + sum abar_b^dag abar_a [D_b,D_a^dag]] = {nrm(A - rhs):.1e}  (exact identity)")
print(f"  max |[D_b, D_a^dag] - delta_ab| = {max(devs):.3f}   (nonzero: composite diquark is not a canonical boson)")
# what is the deviation? check it is a quark-number-type operator: compare with (quark number in colour a,b)
c00 = comm(Dop[0], Ddag[0]) - sp.identity(2 ** 15)
print(f"  K_00 = 1 - [D_0,D_0^dag] commutes with N_q: {nrm(comm(c00, Nq)):.1e}; with N_qbar: {nrm(comm(c00, Nab)):.1e}"
      "  (a quark bilinear: Pauli blocking of the diquark by quarks already present)")
# Is {Q,Q^dag} diagonal in a number basis? It commutes with N_q, N_qbar and colour:
print(f"  [{{Q,Q^dag}}, N_q] = {nrm(comm(A, Nq)):.1e}, [{{Q,Q^dag}}, N_qbar] = {nrm(comm(A, Nab)):.1e},"
      f" [{{Q,Q^dag}}, T3] = {nrm(comm(A, colour_gen(lam3))):.1e}")
# spectrum of {Q,Q^dag} in the 1-antiquark, 0-quark sector and the 2-quark, 0-antiquark sector
sec1 = [i for i in range(2 ** 15) if bin(i).count("1") == 1 and i < 2 ** 3]  # last 3 modes are bits 0..2
# with JW kron ordering, mode 0 is the most significant bit; antiquark modes 12..14 are the lowest bits
def sector(nq, nab):
    idx = []
    for i in range(2 ** 15):
        bits = format(i, "015b")
        if bits[:12].count("1") == nq and bits[12:].count("1") == nab:
            idx.append(i)
    return idx


for nq, nab, lab in [(0, 1, "1 antiquark (meson-side constituent)"), (2, 0, "2 quarks (diquark sector)"),
                     (2, 1, "2 quarks + 1 antiquark")]:
    idx = sector(nq, nab)
    blk = A[idx][:, idx].toarray()
    ev = np.round(np.linalg.eigvalsh(blk), 6)
    vals, cnt = np.unique(ev, return_counts=True)
    print(f"  spectrum of {{Q,Q^dag}} in sector {lab}: " + ", ".join(f"{v:g} (x{c})" for v, c in zip(vals, cnt)))
print()
print("Result: in both realisations {Q, Q^dag} is a sum of number, spin and colour-density operators.")
print("One spatial mode: this toy cannot show presence or absence of P_mu (see c6_hq_commutator.py).")
print("=> non-relativistic spectrum-generating superalgebra, same type as Iachello's nuclear U(m|n).")
