"""LW1 cycle 8, c8a: superflavor breaking, recalibrated and separated from heavy-quark spin breaking.

Answers referee 2 (cycle 7) findings 1-3.

Model: the c6 Part B heavy-source model (light quark q + 3bar source X; X = Qbar, spin 1/2, mass m_Q, or compact
(QQ)_3bar, spin 1, mass 2 m_Q), 3 momentum modes, contact colour-magnetic hyperfine term of De Rujula-Georgi-Glashow
form. Everything is done in the colour-singlet sector, where lambda_q.lambda_X = -16/3 for 3 x 3bar (referee 2
found the singlet-restricted ||B|| equal to the full-space one; checked again below). Q maps colour index to colour
index, so it maps singlet to singlet.

  V_M = +kappa (16/3)/(m_q m_Q)  S_q.S_Qbar  C          (meson)
  V_B = +kappa (16/3)/(m_q m_Q)  (1/2) S_q.S_D  C       (baryon; the 1/2 is the superflavor Clebsch, c1 / referee 2 (1))
  C   = contact operator, (1/NK) sum_q shift_q (x) shift_-q

Changes from c6:
 (i)  kappa is calibrated on the model's OWN ground-state spectrum (colour singlet, total momentum 0, lowest J=0 and
      J=1 meson levels) to D*0-D0 = 142.01 MeV. c6 set kappa by a contact-eigenvalue-1 convention, which gives a
      ground-state splitting of 58 MeV (referee 2, finding 2).
 (ii) The 1/m_Q dependence is not inserted through the target splitting. kappa is one coupling (fixed at charm); the
      1/m_Q comes from the operator form V ~ 1/(m_q m_Q), which is the NRQCD chromomagnetic term c_F g sigma.B/(2 m_Q)
      at tree level (c_F = 1). The bottom splitting is then a model PREDICTION, compared with B*-B.
 (iii) [H,Q] is split into: offset delta Q (removable with heavy-quark number), [V_hf, Q] (heavy-quark spin breaking
      whose meson/baryon matrix elements superflavor ties by the 1/2 Clebsch: the 3/4 rule), and [K_X, Q] (source
      recoil; the source kinetic energy p^2/(2 m_X) differs between m_X = m_Q and 2 m_Q, so this operator is NOT of
      superflavor-covariant form). Genuine superflavor violation = recoil operator + the observable residuals
        hyperfine residual   r_hf  = Delta_B - (3/4) Delta_M
        spin-average residual r_avg = (Mbar_B - Mbar_M) - (m_(QQ) - m_Qbar)
      both zero at leading order in superflavor.
"""
import numpy as np
from scipy.optimize import brentq

NK = 3
KV = np.array([0.0, 1.0, -1.0])
MQL, P0 = 0.33, 0.40                       # light constituent mass, light-dof momentum scale (GeV) [assumptions, as c6]
I2, I3, Ik = np.eye(2), np.eye(3), np.eye(NK)
s12 = [np.array([[0, 1], [1, 0]]) / 2, np.array([[0, -1j], [1j, 0]]) / 2, np.diag([0.5, -0.5])]
r2 = np.sqrt(2)
s1 = [np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / r2, np.array([[0, -1j, 0], [1j, 0, -1j], [0, 1j, 0]]) / r2,
      np.diag([1.0, 0, -1.0])]
SH = [np.roll(Ik, q, axis=0) for q in range(NK)]
TR = np.diag(np.exp(2j * np.pi * np.arange(NK) / NK))
DSTAR_D = 0.142014                       # PDG 2024 D*0 - D0
BSTAR_B = 0.04534                        # PDG 2024 B* - B+ (as in c2); isospin-averaged B gives 45.19
MC, MB = 1.5485, 4.7302                  # M(J/psi)/2, M(Upsilon 1S)/2 (as c6)


def kron(*a):
    out = a[0]
    for x in a[1:]:
        out = np.kron(out, x)
    return out


def parts(mQ, kap, p0=P0):
    """colour-singlet operators. Ordering: light (spin 2 x mom NK) (x) source (spin ds x mom NK)."""
    out = {}
    for lab, ds, Ss, mX, w in [("M", 2, s12, mQ, 1.0), ("B", 3, s1, 2 * mQ, 0.5)]:
        Ids = np.eye(ds)
        Kq = kron(I2, np.diag(np.sqrt((KV * p0) ** 2 + MQL ** 2)), Ids, Ik)
        KX = kron(I2, Ik, Ids, np.diag(mX + (KV * p0) ** 2 / (2 * mX)))
        SS = sum(kron(s12[x], Ik, Ss[x], Ik) for x in range(3))
        C = sum(kron(I2, SH[q], Ids, SH[(-q) % NK]) for q in range(NK)) / NK
        V = w * kap * (16 / 3) / (MQL * mQ) * SS @ C
        J = [kron(s12[x], Ik, Ids, Ik) + kron(I2, Ik, Ss[x], Ik) for x in range(3)]
        out[lab] = dict(Kq=Kq, KX=KX, V=V, J2=sum(j @ j for j in J), T=kron(I2, TR, Ids, TR), ds=ds, mX=mX)
    Qs = []
    for m in range(3):
        for sg in range(2):
            M = np.zeros((3, 2)); M[m, sg] = 1
            Qs.append(kron(I2, Ik, M, Ik))
    return out, Qs


def levels(d, H):
    """lowest two J levels in the total-momentum-0 sector: returns dict J -> lowest energy"""
    w, v = np.linalg.eigh((d["T"] + d["T"].conj().T).real / 2)
    P = v[:, np.abs(w - 1) < 1e-8]
    e, u = np.linalg.eigh(P.conj().T @ H @ P)
    vec = P @ u
    j2 = np.real(np.einsum("ij,ik,kj->j", vec.conj(), d["J2"], vec))
    J = np.round((-1 + np.sqrt(1 + 4 * j2)) / 2 * 2) / 2
    low = {}
    for ei, Ji in zip(e, J):
        low.setdefault(Ji, ei)
    return low


def spectrum(mQ, kap, p0=P0, rec=True):
    d, Qs = parts(mQ, kap, p0)
    res = {}
    for lab in "MB":
        x = d[lab]
        KX = x["KX"] if rec else kron(I2, Ik, np.eye(x["ds"]), np.eye(NK) * x["mX"])
        res[lab] = levels(x, x["Kq"] + KX + x["V"])
    M, B = res["M"], res["B"]
    dM, dB = M[1.0] - M[0.0], B[1.5] - B[0.5]
    mbM, mbB = (M[0.0] + 3 * M[1.0]) / 4, (2 * B[0.5] + 4 * B[1.5]) / 6
    return dict(dM=dM, dB=dB, R=dB / dM, rhf=dB - 0.75 * dM, ravg=(mbB - mbM) - mQ)


def norms(mQ, kap, p0=P0):
    d, Qs = parts(mQ, kap, p0)
    M, B = d["M"], d["B"]
    out = {"tot": 0, "hf": 0, "rec": 0, "kq": 0}
    for Q in Qs:
        def c(opB, opM):
            return opB @ Q - Q @ opM
        Ctot = c(B["Kq"] + B["KX"] + B["V"], M["Kq"] + M["KX"] + M["V"])
        delta = np.real(np.trace(Q.T @ Ctot) / np.trace(Q.T @ Q))
        out["delta"] = delta
        out["tot"] = max(out["tot"], np.linalg.norm(Ctot - delta * Q, 2))
        out["hf"] = max(out["hf"], np.linalg.norm(c(B["V"], M["V"]), 2))
        CX = c(B["KX"], M["KX"])
        dX = np.real(np.trace(Q.T @ CX) / np.trace(Q.T @ Q))
        out["rec"] = max(out["rec"], np.linalg.norm(CX - dX * Q, 2))
        out["kq"] = max(out["kq"], np.linalg.norm(c(B["Kq"], M["Kq"]), 2))
    return out


kap_c6 = DSTAR_D * MQL * MC / (16 / 3)
print("=" * 90)
print("c8a. Superflavor breaking, recalibrated (colour-singlet sector)")
print("-" * 90)
n6 = norms(MC, kap_c6)
s6 = spectrum(MC, kap_c6)
print(f"Check vs c6/referee 2 at the c6 kappa ({kap_c6:.5f} GeV^3): ||B|| = {1000*n6['tot']:.1f} MeV "
      f"(c6: 101.6), ground-state D*-D = {1000*s6['dM']:.1f} MeV (referee 2: 57.9), ratio {s6['R']:.3f} (0.691)")
print(f"   light-quark kinetic term commutes with Q: ||[K_q,Q]|| = {n6['kq']:.1e}")

kc = brentq(lambda k: spectrum(MC, k)["dM"] - DSTAR_D, 0.2 * kap_c6, 20 * kap_c6, xtol=1e-12)
print(f"\n(1) Calibration on the model's own ground state: kappa = {kc:.5f} GeV^3 = {kc/kap_c6:.3f} x c6 value")
rows = {}
for lab, mQ in [("charm", MC), ("bottom", MB)]:
    s = spectrum(mQ, kc); n = norms(mQ, kc); s0 = spectrum(mQ, kc, rec=False)
    rows[lab] = (s, n, s0)
    print(f"  {lab:6s} m_Q={mQ:.4f}: meson J=1-0 {1000*s['dM']:6.1f} MeV, baryon 3/2-1/2 {1000*s['dB']:6.1f} MeV,"
          f" ratio {s['R']:.3f} (LO superflavor 0.750)")
sb = rows["bottom"][0]
print(f"  bottom meson splitting is a model PREDICTION from the charm kappa: {1000*sb['dM']:.1f} MeV vs PDG "
      f"B*-B {1000*BSTAR_B:.2f} MeV ({100*(sb['dM']/BSTAR_B-1):+.0f}%)")

kb = brentq(lambda k: spectrum(MB, k)["dM"] - BSTAR_B, 0.2 * kap_c6, 40 * kap_c6, xtol=1e-12)
sbb = spectrum(MB, kb)
print(f"  bottom recalibrated on its own (kappa_b = {kb:.5f} = {kb/kc:.3f} kappa_c): meson {1000*sbb['dM']:.2f}, baryon "
      f"{1000*sbb['dB']:.1f} MeV, ratio {sbb['R']:.3f}, r_hf = {1000*sbb['rhf']:+.1f} MeV ({100*sbb['rhf']/(0.75*sbb['dM']):+.1f}%)")
print(f"  for comparison, dynamical lattice (Brown+ 2014): Xi_cc*-Xi_cc = 82.8 +- 9.2 MeV -> ratio {82.8/142.014:.3f},"
      f" r_hf = {82.8-0.75*142.014:+.1f} MeV ({100*(82.8/106.51-1):+.0f}%)")

print("\n(2) Decomposition of [H,Q] = delta Q + [V_hf,Q] + ([K_X,Q] - delta_X Q)   (operator norms, max over Q_{m,s})")
for lab in rows:
    s, n, s0 = rows[lab]
    print(f"  {lab:6s}: delta = {1000*n['delta']:6.0f} MeV;  ||[V_hf,Q]|| = {1000*n['hf']:6.1f} MeV (HQ spin breaking,"
          f" superflavor-covariant at first order);  ||recoil|| = {1000*n['rec']:5.1f} MeV (genuine);"
          f"  total ||B|| = {1000*n['tot']:6.1f} MeV")

print("\n(3) Observable superflavor residuals (zero at LO superflavor)")
for lab in rows:
    s, n, s0 = rows[lab]
    print(f"  {lab:6s}: r_hf = Delta_B - (3/4)Delta_M = {1000*s['rhf']:+6.1f} MeV ({100*s['rhf']/(0.75*s['dM']):+5.1f}% of the"
          f" 3/4 prediction);  without recoil {1000*s0['rhf']:+6.1f} MeV")
    print(f"          r_avg = (Mbar_B - Mbar_M) - m_Q = {1000*s['ravg']:+6.1f} MeV;  without recoil {1000*s0['ravg']:+6.1f} MeV")

print("\n(4) Scaling with m_Q at FIXED kappa (1/m_Q from the operator form, not from the target). Fitted exponents are output.")
ms = np.array([MC, MB, 15.0, 50.0, 150.0])
tab = []
for mQ in ms:
    s, n = spectrum(mQ, kc), norms(mQ, kc)
    tab.append((s["dM"], abs(s["rhf"]), abs(s["ravg"]), n["hf"], n["rec"]))
    print(f"   m_Q = {mQ:7.2f}: Delta_M {1000*s['dM']:7.2f}  |r_hf| {1000*abs(s['rhf']):7.3f}  |r_avg| {1000*abs(s['ravg']):7.3f}"
          f"  ||[V,Q]|| {1000*n['hf']:7.2f}  ||rec|| {1000*n['rec']:6.2f}  (MeV)")
tab = np.array(tab)
lm = np.log(ms[2:])
for i, nm in enumerate(["Delta_M", "|r_hf|", "|r_avg|", "||[V_hf,Q]||", "||recoil||"]):
    p = np.polyfit(lm, np.log(tab[2:, i]), 1)[0]
    print(f"   {nm:13s} ~ m_Q^{p:+.2f}   (fit over m_Q = 15-150 GeV)")
print("""
Reading:
 - The hyperfine piece of [H,Q] is heavy-quark spin breaking. Its meson/baryon matrix elements are tied by the
   superflavor Clebsch 1/2 (the 3/4 rule), so its norm is NOT a measure of superflavor violation.
 - Genuine superflavor violation in this model: the recoil operator (source mass m_Q vs 2 m_Q) and the observable
   residuals r_hf, r_avg. r_hf comes from second order in the hyperfine spurion (it mixes the ground configuration
   with excited ones, differently in the two sectors) plus recoil, i.e. O(Lambda^2/m_Q^2)-type effects that LO
   superflavor does not constrain.
 - Toy limitation: the ground configuration has both constituents at zero momentum, so the first-order source
   recoil <p^2>/(2 m_X) vanishes there and r_avg, r_hf start at O(1/m_Q^2). In QCD the source kinetic energy
   (lambda_1-type terms) differs between meson and baryon at O(Lambda^2/m_Q), so the real genuine breaking starts at
   O(Lambda/m_Q) relative to the hyperfine splitting; the 1/m_Q^2 exponents above are a property of this toy.
 - The charm calibration needs 2.05x the c6 kappa because the contact term has eigenvalue 1/3 on the kinetic ground
   configuration and mixes in excited configurations at second order; that same mixing is what makes the bottom
   prediction from the charm kappa 18% low.
 - Model status: QCD-inspired constituent model, illustrative parameters (m_q = 0.33, p0 = 0.40 GeV).""")
