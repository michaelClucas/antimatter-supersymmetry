"""LW1 cycle 6, c6a: the antiquark -> diquark supercharge is not a symmetry of a QCD-inspired Hamiltonian.

Replaces the one-mode, spinless-antiquark toy of c5a (referee 1, cycle 5, finding 1).

Part A. Quark-level toy with 3 lattice momentum modes (3-site ring, crystal momentum k = 0,1,2 ~ p = 0,+p0,-p0)
        and spin-1/2 antiquarks. Distinguishable flavours: spectator s, diquark quarks u and d, antiquark abar.
        Single-particle space = colour(3) x spin(2) x momentum(3) = 18.
        Meson sector  |s abar>  : 18^2 = 324 states.  Baryon sector |s u d> : 18^3 = 5832 states.
        Local scalar colour-3bar diquark D^dag_{a,P} = sum_k eps_abc (u^dag_{b up,k} d^dag_{c dn,P-k} - (up<->dn))/norm.
        Supercharge Q_sigma = sum_{a,P} D^dag_{a,P} abar_{a,sigma,P}  (sigma = antiquark spin; Q_sigma is spin-1/2).
        Checks: spin-1/2 transformation; colour singlet; momentum conservation; {Q_s, Q_t^dag} in both sectors;
        whether {Q,Q^dag} contains anything proportional to P or to the kinetic energy; [H,Q] with
        H = relativistic kinetic energy + constituent masses + contact colour-magnetic hyperfine term
        V_ij = -kappa (lambda_i . lambda_j)(S_i . S_j)/(m_i m_j) x contact.
Part B. Heavy-source model with physical calibration: light quark q + static-ish 3bar source X, where
        X = heavy antiquark Qbar (spin 1/2, mass m_Q) or compact heavy diquark (QQ) (spin 1, mass 2 m_Q).
        Same hyperfine form, kappa fixed by D*-D (charm) or B*-B (bottom); source recoil p^2/(2 m_X).
        Supercharges Q_{m,sigma} = sum_{a,P} D^dag_{a,m,P} Qbar_{a,sigma,P}. Decompose
        [H, Q] = delta Q + B, delta = best constant offset (removable by subtracting the separately conserved
        heavy-quark number); B is the genuine breaking. Report B in MeV, split into hyperfine and recoil, and
        its scaling with m_Q.
Model status: constituent-quark / De Rujula-Georgi-Glashow-type Hamiltonian, PRD 12, 147 (1975). It is
QCD-inspired, not QCD. [established model form; parameter choices are illustrative and stated]
"""
import numpy as np
import scipy.sparse as sp

np.set_printoptions(precision=4, suppress=True)
NK = 3
KVAL = np.array([0.0, 1.0, -1.0])           # physical momentum in units of p0 for crystal momentum k = 0,1,2

# ----------------------------------------------------------------------------- small building blocks
lam = np.zeros((8, 3, 3), complex)
lam[0][0, 1] = lam[0][1, 0] = 1
lam[1][0, 1] = -1j; lam[1][1, 0] = 1j
lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1
lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
LAM_Q = list(lam)                              # quark (3):        lambda
LAM_QB = [-l.conj() for l in lam]              # antitriplet (3bar): -lambda^*
S12 = [np.array([[0, 1], [1, 0]]) / 2, np.array([[0, -1j], [1j, 0]]) / 2, np.diag([0.5, -0.5])]
s2 = np.sqrt(2)
S1 = [np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / s2,
      np.array([[0, -1j, 0], [1j, 0, -1j], [0, 1j, 0]]) / s2,
      np.diag([1.0, 0.0, -1.0])]
SHIFT = [np.roll(np.eye(NK), q, axis=0) for q in range(NK)]   # |k> -> |k+q mod 3>


def emb(ops, slot, dims):
    """Embed a single-particle operator into a multi-particle tensor product (sparse)."""
    m = None
    for i, d in enumerate(dims):
        x = sp.csr_matrix(ops) if i == slot else sp.identity(d, format="csr")
        m = x if m is None else sp.kron(m, x, format="csr")
    return m


def sp1(colour, spin, mom):
    """single-particle operator colour (x) spin (x) momentum"""
    return np.kron(np.kron(colour, spin), mom)


def opnorm(m):
    m = m.toarray() if sp.issparse(m) else m
    return float(np.linalg.norm(m, 2))


def maxabs(m):
    m = m.tocoo() if sp.issparse(m) else sp.coo_matrix(m)
    return 0.0 if m.nnz == 0 else float(np.max(np.abs(m.data)))


def hyperfine(i, j, dims, lams, spins, kappa, mi, mj, w=1.0):
    """V_ij = -w kappa (lambda_i.lambda_j)(S_i.S_j)/(m_i m_j) x contact(i,j)."""
    I3, Ik = np.eye(3), np.eye(NK)
    ds = [len(spins[x][0]) for x in (i, j)]
    LL = sum(emb(sp1(lams[i][A], np.eye(ds[0]), Ik), i, dims) @ emb(sp1(lams[j][A], np.eye(ds[1]), Ik), j, dims)
             for A in range(8))
    SS = sum(emb(sp1(I3, spins[i][x], Ik), i, dims) @ emb(sp1(I3, spins[j][x], Ik), j, dims) for x in range(3))
    C = sum(emb(sp1(I3, np.eye(ds[0]), SHIFT[q]), i, dims) @ emb(sp1(I3, np.eye(ds[1]), SHIFT[(-q) % NK]), j, dims)
            for q in range(NK)) / NK
    return (-w * kappa / (mi * mj)) * (LL @ SS @ C)


def kinetic(slot, dims, m, p0, spin_dim, nonrel=False):
    e = (m + (KVAL * p0) ** 2 / (2 * m)) if nonrel else np.sqrt((KVAL * p0) ** 2 + m ** 2)
    return emb(sp1(np.eye(3), np.eye(spin_dim), np.diag(e)), slot, dims)


eps = np.zeros((3, 3, 3))
for (i, j, k), sg in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]:
    eps[i, j, k] = sg


def idx(c, s, k, sd=2):
    return (c * sd + s) * NK + k


# ============================================================================ PART A
print("=" * 86)
print("PART A. Quark-level toy: 3 momentum modes, spin-1/2 antiquark, local scalar 3bar diquark")
d1 = 3 * 2 * NK                       # 18
dimsM, dimsB = [d1, d1], [d1, d1, d1]  # meson: s, abar ; baryon: s, u, d
# diquark states |D_{a,P}> in H_u (x) H_d
Dst = np.zeros((3, NK, d1 * d1))
for a in range(3):
    for P in range(NK):
        v = np.zeros(d1 * d1)
        for b in range(3):
            for c in range(3):
                if eps[a, b, c] == 0:
                    continue
                for k in range(NK):
                    kk = (P - k) % NK
                    v[idx(b, 0, k) * d1 + idx(c, 1, kk)] += eps[a, b, c]
                    v[idx(b, 1, k) * d1 + idx(c, 0, kk)] -= eps[a, b, c]
        Dst[a, P] = v / np.linalg.norm(v)
gram = np.array([[Dst[a, P] @ Dst[b, Q] for b in range(3) for Q in range(NK)] for a in range(3) for P in range(NK)])
print(f"  diquark states orthonormal: max|<D|D'> - delta| = {np.max(np.abs(gram - np.eye(9))):.1e}")
Mops = []
for sg in range(2):
    M = np.zeros((d1 * d1, d1))
    for a in range(3):
        for P in range(NK):
            M[:, idx(a, sg, P)] += Dst[a, P]
    Mops.append(sp.csr_matrix(M))
Q = [sp.kron(sp.identity(d1, format="csr"), Mops[sg], format="csr") for sg in range(2)]   # baryon <- meson

# spin
SzM = emb(sp1(np.eye(3), S12[2], np.eye(NK)), 0, dimsM) + emb(sp1(np.eye(3), S12[2], np.eye(NK)), 1, dimsM)
SzB = sum(emb(sp1(np.eye(3), S12[2], np.eye(NK)), i, dimsB) for i in range(3))
SpM = sum(emb(sp1(np.eye(3), S12[0] + 1j * S12[1], np.eye(NK)), i, dimsM) for i in range(2))
SpB = sum(emb(sp1(np.eye(3), S12[0] + 1j * S12[1], np.eye(NK)), i, dimsB) for i in range(3))
for sg, sz in [(0, 0.5), (1, -0.5)]:
    print(f"  [S_z, Q_{'up' if sg == 0 else 'dn'}] + ({sz:+.1f}) Q = {maxabs(SzB @ Q[sg] - Q[sg] @ SzM + sz * Q[sg]):.1e}"
          "   (Q_sigma lowers S_z by the removed antiquark spin)")
r_up = SpB @ Q[0] - Q[0] @ SpM
r_dn = SpB @ Q[1] - Q[1] @ SpM
print(f"  [S_+, Q_up] + Q_dn = {maxabs(r_up + Q[1]):.1e},  [S_+, Q_dn] = {maxabs(r_dn):.1e}"
      "  -> (Q_dn, -Q_up) is a spin-1/2 doublet (the antiquark annihilator's transformation)")
# colour singlet
cs = 0.0
for A in range(8):
    TM = emb(sp1(LAM_Q[A] / 2, np.eye(2), np.eye(NK)), 0, dimsM) + emb(sp1(LAM_QB[A] / 2, np.eye(2), np.eye(NK)), 1, dimsM)
    TB = sum(emb(sp1(LAM_Q[A] / 2, np.eye(2), np.eye(NK)), i, dimsB) for i in range(3))
    cs = max(cs, maxabs(TB @ Q[0] - Q[0] @ TM))
print(f"  max_A |[T_A, Q]| = {cs:.1e}  (colour singlet)")
# momentum (crystal momentum mod 3 -> translation operator)
tr = np.diag(np.exp(2j * np.pi * np.arange(NK) / NK))
TrM = emb(sp1(np.eye(3), np.eye(2), tr), 0, dimsM) @ emb(sp1(np.eye(3), np.eye(2), tr), 1, dimsM)
TrB = emb(sp1(np.eye(3), np.eye(2), tr), 0, dimsB) @ emb(sp1(np.eye(3), np.eye(2), tr), 1, dimsB) @ \
    emb(sp1(np.eye(3), np.eye(2), tr), 2, dimsB)
print(f"  |T Q - Q T| (translation) = {maxabs(TrB @ Q[0] - Q[0] @ TrM):.1e}  (Q conserves total momentum)")

# anticommutator, meson sector: {Q_s, Q_t^dag} = Q_t^dag Q_s (Q^dag annihilates the meson sector: no u,d present)
print("\n  {Q_s, Q_t^dag} on the meson sector (|s abar>):")
nab = [[emb(sp1(np.eye(3), np.outer(np.eye(2)[t], np.eye(2)[s]), np.eye(NK)), 1, dimsM) for s in range(2)] for t in range(2)]
for s in range(2):
    for t in range(2):
        A = Q[t].conj().T @ Q[s]
        print(f"    s={s} t={t}: |{{Q_s,Q_t^dag}} - abar^dag_t abar_s (summed over colour, momentum)| = {maxabs(A - nab[t][s]):.1e}")
Atot = (Q[0].conj().T @ Q[0] + Q[1].conj().T @ Q[1]).toarray()
p0A = 0.35
Hkin_M = (kinetic(0, dimsM, 0.50, p0A, 2) + kinetic(1, dimsM, 0.33, p0A, 2)).toarray()
Kc = np.round(np.angle(np.diag(TrM.toarray())) / (2 * np.pi / NK)).astype(int) % NK
basis = [np.eye(324).ravel(), Hkin_M.ravel(), np.diag(np.where(Kc == 1, 1.0, np.where(Kc == 2, -1.0, 0.0))).ravel()]
coef, *_ = np.linalg.lstsq(np.array(basis).T, Atot.ravel(), rcond=None)
print(f"  sum_s {{Q_s,Q_s^dag}} = N_abar = 1 on every meson state: max dev {np.max(np.abs(Atot - np.eye(324))):.1e}")
print(f"  least-squares fit sum_s {{Q_s,Q_s^dag}} = c0 + c1 H_kin + c2 P:  c0 = {coef[0].real:.4f}, "
      f"c1 = {coef[1].real:+.1e}, c2 = {coef[2].real:+.1e}")
for K in range(NK):
    sel = np.where(Kc == K)[0]
    ev = np.linalg.eigvalsh(Atot[np.ix_(sel, sel)])
    ek = np.linalg.eigvalsh(Hkin_M[np.ix_(sel, sel)])
    print(f"    total crystal momentum K={K}: spec {{Q,Q^dag}} = {np.unique(np.round(ev, 6))},"
          f"  H_kin range [{ek.min():.3f}, {ek.max():.3f}] GeV")
B_A = (Q[0] @ Q[0].conj().T + Q[1] @ Q[1].conj().T)
trB = B_A.diagonal().sum().real
Pi = B_A / 2
print(f"  baryon sector: sum_s Q_s Q_s^dag = 2 Pi, Pi = projector onto (s quark) x (local scalar diquark):"
      f" Tr = {trB:.0f} = 2 x 18 x 9, ||Pi^2 - Pi|| = {maxabs(Pi @ Pi - Pi):.1e}")
print("  => {Q,Q^dag} is a number/projector operator, identical in every momentum sector. Nothing ~ P or H.")
print("     This is a property of the local, derivative-free Q chosen here [argument]; it is not an")
print("     independent reason for the absence of protection (see Part B and WORK.md sec. 19).")

# Hamiltonian
ms, mq, mab = 0.50, 0.33, 0.33
kap = 0.40 * ms * mab / (16 / 3)        # contact s-abar hyperfine splitting set to 0.40 GeV (K*-K scale)
lamsM = [LAM_Q, LAM_QB]; spinsM = [S12, S12]
lamsB = [LAM_Q, LAM_Q, LAM_Q]; spinsB = [S12, S12, S12]
HM0 = kinetic(0, dimsM, ms, p0A, 2) + kinetic(1, dimsM, mab, p0A, 2)
HB0 = kinetic(0, dimsB, ms, p0A, 2) + kinetic(1, dimsB, mq, p0A, 2) + kinetic(2, dimsB, mq, p0A, 2)
VM = hyperfine(0, 1, dimsM, lamsM, spinsM, kap, ms, mab)
VB = hyperfine(0, 1, dimsB, lamsB, spinsB, kap, ms, mq) + hyperfine(0, 2, dimsB, lamsB, spinsB, kap, ms, mq) + \
    hyperfine(1, 2, dimsB, lamsB, spinsB, kap, mq, mq)
print(f"\n  H = sqrt(p^2+m^2) per constituent + contact colour-magnetic V_ij; m_s={ms}, m_u=m_d=m_abar={mq} GeV,"
      f" p0={p0A} GeV, kappa={kap:.4f} GeV^3")


def comm_report(HM, HB, lab):
    out = []
    for sg in range(2):
        C = (HB @ Q[sg] - Q[sg] @ HM).toarray()
        Qd = Q[sg].toarray()
        delta = np.real(np.trace(Qd.conj().T @ C) / np.trace(Qd.conj().T @ Qd))
        Bm = C - delta * Qd
        out.append((opnorm(C), delta, opnorm(Bm)))
    n, dl, b = out[0]
    print(f"   {lab:28s} ||[H,Q]|| = {1000*n:7.1f} MeV, best offset delta = {1000*dl:7.1f} MeV, "
          f"||[H,Q] - delta Q|| = {1000*b:6.1f} MeV")
    return out[0]


comm_report(HM0, HB0, "kinetic + masses only:")
comm_report(VM, VB, "hyperfine only:")
comm_report(HM0 + VM, HB0 + VB, "full H:")
# physical test: is Q|meson ground state> an eigenstate of H_B?
from scipy.sparse.linalg import eigsh  # noqa: E402
HM, HB = (HM0 + VM).toarray(), (HB0 + VB).tocsr()
e, v = np.linalg.eigh(HM)
eB = eigsh(HB, k=1, which="SA")[0]
for sg in range(2):
    for j in range(len(e)):   # first state of the ground multiplet with nonzero image
        if abs(e[j] - e[0]) > 1e-9:
            break
        w = Q[sg] @ v[:, j]
        if np.linalg.norm(w) > 1e-6:
            break
    if np.linalg.norm(w) < 1e-6:
        continue
    w = w / np.linalg.norm(w)
    Hw = HB @ w
    Ew = np.real(w.conj() @ Hw)
    sE = np.sqrt(max(np.real(Hw.conj() @ Hw) - Ew ** 2, 0))
    print(f"   meson ground state E_M = {1000*e[0]:.0f} MeV (deg. {np.sum(np.abs(e - e[0]) < 1e-9)}); "
          f"Q_{['up','dn'][sg]}|M>: <H_B> = {1000*Ew:.0f} MeV, energy spread sigma_E = {1000*sE:.0f} MeV; "
          f"baryon ground E_B = {1000*eB[0]:.0f} MeV")
    break
print("   sigma_E > 0: Q maps the meson ground state onto a superposition of baryon eigenstates, so Q is not")
print("   a symmetry even after subtracting a constant offset. [established for this model]")

# ============================================================================ PART B
print("\n" + "=" * 86)
print("PART B. Heavy-source model, calibrated: q + Qbar (spin 1/2)  vs  q + (QQ)_3bar (spin 1, compact)")
MQ = 0.33                        # light constituent mass (GeV)
P0 = 0.40                        # light-dof momentum scale ~ Lambda_QCD (GeV) [assumption]
dq = 3 * 2 * NK
dXm, dXb = 3 * 2 * NK, 3 * 3 * NK
dimsM2, dimsB2 = [dq, dXm], [dq, dXb]


def heavy_model(mQ, DeltaM, p0=P0, hf=True, recoil=True):
    """Return (HM, HB, list of Q_{m,sigma}); kappa from the meson hyperfine splitting DeltaM (GeV)."""
    kapQ = DeltaM * MQ * mQ / (16 / 3)
    mD = 2 * mQ
    HM = kinetic(0, dimsM2, MQ, p0, 2)
    HB = kinetic(0, dimsB2, MQ, p0, 2)
    pm = p0 if recoil else 0.0
    HM = HM + kinetic(1, dimsM2, mQ, pm, 2, nonrel=True)
    HB = HB + kinetic(1, dimsB2, mD, pm, 3, nonrel=True)
    if hf:
        HM = HM + hyperfine(0, 1, dimsM2, [LAM_Q, LAM_QB], [S12, S12], kapQ, MQ, mQ)
        # q-(QQ): sum over the two heavy quarks, projected on (3bar, spin 1) = (1/2)(1/2) x 2 = 1/2 of the
        # operator written with the diquark colour and spin generators (WORK.md sec. 19)
        HB = HB + hyperfine(0, 1, dimsB2, [LAM_Q, LAM_QB], [S12, S1], kapQ, MQ, mQ, w=0.5)
    Qs = []
    for m in range(3):
        for sg in range(2):
            M = np.zeros((dXb, dXm))
            for a in range(3):
                for k in range(NK):
                    M[idx(a, m, k, 3), idx(a, sg, k, 2)] = 1.0
            Qs.append(sp.kron(sp.identity(dq, format="csr"), sp.csr_matrix(M), format="csr"))
    return HM.toarray(), HB.toarray(), Qs


def breaking(HM, HB, Qs):
    best = []
    for Qm in Qs:
        Qd = Qm.toarray()
        C = HB @ Qd - Qd @ HM
        delta = np.real(np.trace(Qd.T @ C) / np.trace(Qd.T @ Qd))
        best.append((delta, opnorm(C - delta * Qd)))
    return best[0][0], max(b for _, b in best)


def spectra(HM, HB):
    """colour-singlet, P=0 lowest levels: meson J=0,1 and baryon J=1/2,3/2 splittings (MeV)"""
    em, eb = np.linalg.eigvalsh(HM), np.linalg.eigvalsh(HB)
    return em, eb


rows = []
for lab, mQ, DM in [("charm  (m_c = M(J/psi)/2)", 1.5485, 0.142014), ("bottom (m_b = M(Y1S)/2)", 4.7302, 0.04534)]:
    HM, HB, Qs = heavy_model(mQ, DM)
    delta, Bfull = breaking(HM, HB, Qs)
    _, Bhf = breaking(*heavy_model(mQ, DM, recoil=False))
    _, Brec = breaking(*heavy_model(mQ, DM, hf=False))
    # hyperfine levels in the colour-singlet ground configuration (contact eigenvalue 1):
    hfM = (16 / 3) * (DM * MQ * mQ / (16 / 3)) / (MQ * mQ)
    print(f"  {lab}: offset delta = {1000*delta:6.0f} MeV (= m_(QQ) - m_Qbar + recoil difference; removable by"
          f" subtracting the conserved heavy-quark number)")
    print(f"     genuine breaking ||[H,Q] - delta Q||: hyperfine only {1000*Bhf:5.1f} MeV, recoil only {1000*Brec:5.1f} MeV,"
          f" both {1000*Bfull:5.1f} MeV")
    print(f"     kappa convention: contact eigenvalue 1 gives {1000*hfM:.1f} MeV -> {750*hfM:.1f} MeV by the analytic 3/4"
          f" formula. NOT the model's ground-state splitting (58 MeV charm); recalibrated in c8_breaking_recalibrated.py")
    rows.append((lab, Bfull, Bhf, Brec))
print("\n  Scaling with the heavy mass (kappa ~ 1/m_Q from heavy-quark spin symmetry, D*-D scaled as m_c/m_Q):")
for mQ in [1.5485, 4.7302, 15.0, 50.0, 500.0]:
    DM = 0.142014 * 1.5485 / mQ
    HM, HB, Qs = heavy_model(mQ, DM)
    delta, Bf = breaking(HM, HB, Qs)
    print(f"    m_Q = {mQ:7.2f} GeV: ||B|| = {1000*Bf:7.2f} MeV,  m_Q ||B|| = {1000*Bf*mQ:7.1f} MeV GeV,  offset {delta:7.2f} GeV")
print("  NOTE (cycle 8): the 1/m_Q here is imposed through DM ~ 1/m_Q (HQET input), not derived; ||B|| is mostly")
print("  heavy-quark spin breaking whose pattern superflavor predicts. See c8_breaking_recalibrated.py for the split.")
print("  => [H, Q] = delta Q + B with B = O(Lambda^2/m_Q) -> 0 only as m_Q -> infinity. At physical charm the")
print("     breaking is O(100 MeV), at bottom O(30 MeV), i.e. ~25% and ~8% of the light-dof energy Lambda-bar ~ 0.4 GeV.")
print("     Q is never a symmetry of H itself: the offset delta ~ m_Q cannot be removed by any light-sector dynamics.")
