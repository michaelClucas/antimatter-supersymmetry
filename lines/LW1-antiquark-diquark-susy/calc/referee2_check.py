"""Referee 2 (cycle 7) independent checks for LW1.

(1) 3/4 rule from scratch: project sum_i S_i T_i^a of two heavy quarks onto (3bar antisym colour) x (spin 1).
(2) Part B model of c6_hq_commutator rebuilt independently:
    - ||B|| over the full space vs restricted to colour-singlet states,
    - the model's baryon/meson hyperfine ratio (does the superflavor relation hold despite ||B|| ~ 100 MeV?),
    - whether m_Q ||B|| = const is an output or an input.
(3) P1/P2 arithmetic with PDG inputs.
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)
lam = np.zeros((8, 3, 3), complex)
lam[0][0, 1] = lam[0][1, 0] = 1
lam[1][0, 1] = -1j; lam[1][1, 0] = 1j
lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1
lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
T3 = [l / 2 for l in lam]
T3b = [-l.conj() / 2 for l in lam]
s = [np.array([[0, 1], [1, 0]]) / 2, np.array([[0, -1j], [1j, 0]]) / 2, np.diag([0.5, -0.5])]
r2 = np.sqrt(2)
S1 = [np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / r2, np.array([[0, -1j, 0], [1j, 0, -1j], [0, 1j, 0]]) / r2,
      np.diag([1.0, 0, -1.0])]
I2, I3 = np.eye(2), np.eye(3)

# ---------------------------------------------------------------- (1) 3/4 rule
print("(1) 3/4 rule from heavy-quark spin + colour algebra")
# colour antisym 3bar basis of 3x3: |a> = eps_abc |b c>/sqrt2
eps = np.zeros((3, 3, 3))
for (i, j, k), g in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]:
    eps[i, j, k] = g
Vc = np.array([eps[a].ravel() / r2 for a in range(3)]).T          # 9x3
# spin-1 triplet basis of 2x2
Vs = np.array([[1, 0, 0, 0], [0, 1 / r2, 1 / r2, 0], [0, 0, 0, 1]]).T  # 4x3
V = np.kron(Vc, Vs)                                                 # (9*4) x 9 ; ordering c1 c2 s1 s2 -> fix
# reorder: build operators in (c1 c2) x (s1 s2) ordering
def two(opc1, ops1):  # heavy quark 1 operator colour (x) spin in (c1,c2)x(s1,s2) ordering
    return np.kron(np.kron(opc1, I3), np.kron(ops1, I2))
TD = [Vc.T.conj() @ (np.kron(t, I3) + np.kron(I3, t)) @ Vc for t in T3]
SD = [Vs.T @ (np.kron(x, I2) + np.kron(I2, x)) @ Vs for x in s]
# is TD the 3bar rep? compare Casimir and with -lambda*/2 up to basis
print("   Casimir of diquark colour:", np.round(np.real(sum(t @ t for t in TD)[0, 0]), 4), "(3bar: 4/3)")
proj = [V.T.conj() @ two(T3[A], s[x]) @ V for A in range(8) for x in range(3)]
full = [np.kron(TD[A], SD[x]) for A in range(8) for x in range(3)]
ratio = [np.vdot(f, p).real / np.vdot(f, f).real for f, p in zip(full, proj)]
dev = max(np.abs(p - r * f).max() for p, f, r in zip(proj, full, ratio))
print(f"   P (S_1 T_1^a) P = c S_D T_D^a with c = {np.mean(ratio):.4f} (max deviation {dev:.1e}); two quarks -> {2*np.mean(ratio):.2f}")
# hyperfine energies with coupling A (S_src . S_q) for meson, (1/2)(S_D . S_q) baryon
SS = lambda Sa, Sb: sum(np.kron(a, b) for a, b in zip(Sa, Sb))
em = np.linalg.eigvalsh(SS(s, s)); eb = np.linalg.eigvalsh(0.5 * SS(S1, s))
print(f"   meson S.S levels {np.unique(np.round(em,4))} -> split {em.max()-em.min():.3f};"
      f"  baryon (1/2)S_D.S_q levels {np.unique(np.round(eb,4))} -> split {eb.max()-eb.min():.3f}  => ratio {(eb.max()-eb.min())/(em.max()-em.min()):.3f}")

# ---------------------------------------------------------------- (2) Part B rebuild
print("\n(2) Part B model rebuilt (3 momentum modes, contact hyperfine, same parameters as c6)")
NK = 3; K = np.array([0., 1., -1.]); Ik = np.eye(NK)
SH = [np.roll(Ik, q, axis=0) for q in range(NK)]
MQ, P0 = 0.33, 0.40


def build(mQ, DM, hf=True, rec=True):
    kap = DM * MQ * mQ / (16 / 3)
    lq = lambda c, sp, k: np.kron(np.kron(c, sp), k)
    dq, dm, db = 18, 18, 27
    Eq = np.diag(np.sqrt((K * P0) ** 2 + MQ ** 2))
    pm = P0 if rec else 0.0
    HM = np.kron(lq(I3, I2, Eq), np.eye(dm)) + np.kron(np.eye(dq), lq(I3, I2, np.diag(mQ + (K * pm) ** 2 / (2 * mQ))))
    HB = np.kron(lq(I3, I2, Eq), np.eye(db)) + np.kron(np.eye(dq), lq(I3, np.eye(3), np.diag(2 * mQ + (K * pm) ** 2 / (4 * mQ))))
    C = lambda ds: sum(np.kron(lq(I3, I2, SH[q]), lq(I3, np.eye(ds), SH[(-q) % NK])) for q in range(NK)) / NK
    if hf:
        LLm = sum(np.kron(lq(2 * T3[A], I2, Ik), lq(2 * T3b[A], I2, Ik)) for A in range(8))
        SSm = sum(np.kron(lq(I3, s[x], Ik), lq(I3, s[x], Ik)) for x in range(3))
        LLb = sum(np.kron(lq(2 * T3[A], I2, Ik), lq(2 * T3b[A], np.eye(3), Ik)) for A in range(8))
        SSb = sum(np.kron(lq(I3, s[x], Ik), lq(I3, S1[x], Ik)) for x in range(3))
        HM = HM - kap / (MQ * mQ) * LLm @ SSm @ C(2)
        HB = HB - 0.5 * kap / (MQ * mQ) * LLb @ SSb @ C(3)
    Qs = []
    for m in range(3):
        for sg in range(2):
            M = np.zeros((27, 18))
            for a in range(3):
                for k in range(NK):
                    M[(a * 3 + m) * NK + k, (a * 2 + sg) * NK + k] = 1
            Qs.append(np.kron(np.eye(dq), M))
    # colour-singlet projectors
    def csing(Tl, Th, d):
        Cas = sum((np.kron(lq(t1, I2, Ik), np.eye(d)) + np.kron(np.eye(18), lq(t2, np.eye(d // (3 * NK)), Ik))) @
                  (np.kron(lq(t1, I2, Ik), np.eye(d)) + np.kron(np.eye(18), lq(t2, np.eye(d // (3 * NK)), Ik)))
                  for t1, t2 in zip(Tl, Th))
        w, v = np.linalg.eigh(Cas)
        return v[:, np.abs(w) < 1e-9]
    Pm, Pb = csing(T3, T3b, 18), csing(T3, T3b, 27)
    return HM, HB, Qs, Pm, Pb


def breaking(HM, HB, Qs, Pm=None, Pb=None):
    out = []
    for Q in Qs:
        Cm = HB @ Q - Q @ HM
        if Pm is not None:
            Cm, Q = Pb.T @ Cm @ Pm, Pb.T @ Q @ Pm
        d = np.real(np.trace(Q.T @ Cm) / np.trace(Q.T @ Q))
        out.append(np.linalg.norm(Cm - d * Q, 2))
    return max(out)


def split_levels(H, P, ):
    e = np.linalg.eigvalsh(P.T @ H @ P)
    return e


for lab, mQ, DM in [("charm", 1.5485, 0.142014), ("bottom", 4.7302, 0.04534)]:
    HM, HB, Qs, Pm, Pb = build(mQ, DM)
    print(f"   {lab}: ||B|| full space {1000*breaking(HM,HB,Qs):6.1f} MeV;  colour-singlet only {1000*breaking(HM,HB,Qs,Pm,Pb):6.1f} MeV")
    Hm0, Hb0, Qs0, _, _ = build(mQ, DM, hf=False)
    print(f"      recoil-only breaking (singlet): {1000*breaking(Hm0,Hb0,Qs0,Pm,Pb):5.1f} MeV;"
          f"  hyperfine-only (singlet): {1000*breaking(*build(mQ,DM,rec=False)[:3],Pm,Pb):5.1f} MeV")
    # model spectra: meson J=1 - J=0 and baryon J=3/2 - J=1/2 in ground configuration (singlet, total P=0 lowest)
    em = np.linalg.eigvalsh(Pm.T @ HM @ Pm); eb = np.linalg.eigvalsh(Pb.T @ HB @ Pb)
    # lowest levels with degeneracies
    def lv(e):
        u, c = np.unique(np.round(e, 7), return_counts=True)
        return list(zip(1000 * u[:4], c[:4]))
    print(f"      lowest meson levels (MeV, deg): {[(round(a,1),b) for a,b in lv(em)]}")
    print(f"      lowest baryon levels (MeV, deg): {[(round(a,1),b) for a,b in lv(eb)]}")

print("   Scaling: kappa_eff/(m_q m_Q) = DM*(3/16)*16/3 ... hyperfine coefficient = DM by construction;"
      " c6 sets DM = 142 MeV * m_c/m_Q, so m_Q ||B_hf|| = const is an input, not an output.")

# ---------------------------------------------------------------- (3) arithmetic
print("\n(3) P1/P2 arithmetic")
pdg = {"D*0-D0": 142.014, "D*+-D+": 140.603, "Ds*-Ds": 143.8, "B*-B": 45.21}
for k, v in pdg.items():
    print(f"   3/4 x {k} ({v}) = {0.75*v:.1f} MeV")
print(f"   B*-B as used in c2 (5324.75-5279.41) = {5324.75-5279.41:.2f}; vs isospin-avg B (5279.565): {5324.75-5279.565:.2f}")
Rcc = 82.8 / 142.014
for name, ratio_mass in [("1/m_Q", 1.5485 / 4.7302)]:
    k = Rcc / 0.75 - 1
    Rbb = 0.75 * (1 + k * ratio_mass)
    print(f"   R_cc(lat) = {Rcc:.3f}; kappa/s_c = {k:+.3f}; 1/m_Q transport: R_bb = {Rbb:.3f} -> Xi_bb*-Xi_bb = {Rbb*45.21:.1f} MeV")
for lab, f in [("alpha_s(mv) ratio ~0.67", 0.67), ("alpha_s^2 ratio ~0.45", 0.45), ("no reduction (1.0)", 1.0)]:
    Rbb = 0.75 * (1 + (Rcc / 0.75 - 1) * f)
    print(f"   alt. transport {lab}: Xi_bb*-Xi_bb = {Rbb*45.21:.1f} MeV")

# ---------------------------------------------------------------- (2b) does the c6 model reproduce its own calibration?
print("\n(2b) Model spectrum in the colour-singlet, total-momentum-0 sector, with J identified")
lq = lambda c, sp_, k: np.kron(np.kron(c, sp_), k)
tr = np.diag(np.exp(2j * np.pi * np.arange(NK) / NK))
for lab, mQ, DM, rec in [("charm", 1.5485, 0.142014, True), ("charm, no recoil", 1.5485, 0.142014, False),
                         ("bottom", 4.7302, 0.04534, True)]:
    HM, HB, Qs, Pm, Pb = build(mQ, DM, rec=rec)
    res = []
    for H, P, dsrc, Ssrc in [(HM, Pm, 2, s), (HB, Pb, 3, S1)]:
        Tr = np.kron(lq(I3, I2, tr), lq(I3, np.eye(dsrc), tr))
        J = [np.kron(lq(I3, s[x], Ik), np.eye(3 * dsrc * NK)) + np.kron(np.eye(18), lq(I3, Ssrc[x], Ik)) for x in range(3)]
        J2 = sum(j @ j for j in J)
        w, v = np.linalg.eigh(P.conj().T @ ((Tr + Tr.conj().T) / 2) @ P)
        P0s = P @ v[:, np.abs(w - 1) < 1e-8]           # singlet and total crystal momentum 0
        e, u = np.linalg.eigh(P0s.conj().T @ H @ P0s)
        lev = []
        for i in range(len(e)):
            jj = np.real(u[:, i].conj() @ P0s.conj().T @ J2 @ P0s @ u[:, i])
            Jv = (-1 + np.sqrt(1 + 4 * jj)) / 2
            if not lev or abs(e[i] - lev[-1][0]) > 1e-7:
                lev.append([e[i], Jv, 1])
            else:
                lev[-1][2] += 1
        res.append(lev[:3])
    m, b = res
    print(f"   {lab}: meson levels (MeV,J,deg) {[(round(1000*x,1), round(j,2), d) for x,j,d in m]}")
    print(f"   {'':{len(lab)}}  baryon levels (MeV,J,deg) {[(round(1000*x,1), round(j,2), d) for x,j,d in b]}")
    dm_ = m[1][0] - m[0][0]; db_ = b[1][0] - b[0][0]
    print(f"   {'':{len(lab)}}  ground hyperfine: meson {1000*dm_:.1f} MeV (calibration target {1000*DM:.1f}), baryon {1000*db_:.1f} MeV, ratio {db_/dm_:.3f}")
