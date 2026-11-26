"""LW1 cycle 4, c5c: what heavy-quark superflavor actually protects, tested on observed states only.

Superflavor (heavy antiquark Qbar <-> heavy 3bar diquark (QQ), BVR hep-ph/0506065) says the light degrees of
freedom see the same static 3bar source. So every light-quark contribution to the mass (kinetic, binding,
light-quark mass, light-flavour SU(3) breaking) is identical in M(QQq) and M(Qbar q) and cancels in
    Delta_q = Mbar(QQq) - Mbar(Qbar q),
which must be independent of the light flavour q at leading order. This is the closest analogue of a
"partner cancellation": a large, nonperturbative light-sector contribution (~100 MeV of SU(3) breaking, plus
the full ~0.3-0.5 GeV light-dof energy Lambda-bar) drops out between superpartners. It protects a DIFFERENCE,
not an absolute mass. [established that this follows at LO; numbers below are data]

Tests:
 (1) q = u, d, s with the three observed doubly charmed baryons.
 (2) Isospin: QED breaks superflavor explicitly, because the diquark (cc) has charge +4/3 and the antiquark
     cbar has -2/3. Two-parameter decomposition (zero d.o.f., a consistency/plausibility check, not a test).
 (3) T_cc+ (cc ubar dbar) as superflavor partner of Lambda_c-bar: c (3) <-> cbar cbar (3), light [ud] spin 0.
     M(T_cc) = M(Lambda_c) + Mbar(Xi_cc) - Mbar(D)   (Eichten-Quigg-type relation, PRL 119, 202002 (2017)).
Masses in MeV. Meson masses PDG 2024 (transcribed; last digit [uncertain], immaterial here).
"""
import numpy as np

# observed inputs (value, sigma)
D0, Dp, Ds = (1864.84, 0.05), (1869.66, 0.05), (1968.35, 0.07)
Dst0, Dstp, Dsst = (2006.85, 0.05), (2010.26, 0.05), (2112.2, 0.4)
Xicc_pp = (3621.55, 0.38)          # LHCb JHEP 02 (2020) 049
Xicc_p = (3619.97, 1.83)           # LHCb PRL 137, 021902 (2026); 0.83 stat, 0.26 syst, +1.90/-1.30 lifetime -> +2.09/-1.56 (cycle 6 fix)
Omcc_p = (3725.9, 1.3)             # LHCb arXiv:2609.21921 (preprint), errors in quadrature
Lc = (2286.46, 0.14)               # PDG 2024
DstpD0_thr = Dstp[0] + D0[0]
Tcc = (DstpD0_thr - 0.36, 0.04)    # LHCb Nat. Commun. 13, 3351 (2022): delta m_pole ~ -360 keV [uncertain keV digits]


def q(*e):
    return float(np.sqrt(sum(x * x for x in e)))


print("(1) Light-flavour independence of the superpartner difference")
rows = [("u", Xicc_pp, D0, Dst0), ("d", Xicc_p, Dp, Dstp), ("s", Omcc_p, Ds, Dsst)]
print("   q   M(QQq)-M(Qbar q) [J=1/2 vs 0-]   spin-avg version (Delta_B = 3/4 Delta_M)")
vals, valsa = [], []
for nm, B, M, Mst in rows:
    d1 = B[0] - M[0]
    e1 = q(B[1], M[1])
    dM = Mst[0] - M[0]
    # spin-averaged: Mbar_B = M_1/2 + (2/3) Delta_B, Mbar_M = M_0 + (3/4) Delta_M, Delta_B = (3/4) Delta_M
    d2 = d1 + (2 / 3) * 0.75 * dM - 0.75 * dM
    vals.append((d1, e1)); valsa.append((d2, e1))
    print(f"   {nm}   {d1:8.2f} +- {e1:4.2f}                    {d2:8.2f} +- {e1:4.2f}")
mes_su3 = Ds[0] - 0.5 * (D0[0] + Dp[0])
bar_su3 = Omcc_p[0] - 0.5 * (Xicc_pp[0] + Xicc_p[0])
res = vals[2][0] - 0.5 * (vals[0][0] + vals[1][0])
eres = q(vals[2][1], 0.5 * vals[0][1], 0.5 * vals[1][1])
print(f"   SU(3) breaking in mesons  D_s - <D>      = {mes_su3:6.1f} MeV")
print(f"   SU(3) breaking in baryons Om_cc - <Xi_cc> = {bar_su3:6.1f} MeV")
print(f"   residual (non-cancelled part) = {res:+.1f} +- {eres:.1f} MeV = {100*res/mes_su3:+.1f}% of the SU(3) breaking")
spread = max(v for v, _ in vals) - min(v for v, _ in vals)
print(f"   spread of Delta_q over u,d,s = {spread:.1f} MeV on a ~1755 MeV difference")
print(f"   for scale: light-dof energy Lambda-bar ~ Mbar(D) - M(J/psi)/2 = {0.25*(D0[0]+3*Dst0[0]) - 1548.5:.0f} MeV"
      " [conjecture: crude m_c]; it cancels in Delta_q entirely at LO")

print("\n(2) Isospin: QED breaks superflavor (charge of cc = +4/3, of cbar = -2/3)")
print("   Model [conjecture]: M = ... + delta*(n_d - n_u) + E_c * (Q_heavy x Q_light), E_c = alpha<1/r> same in both")
print("   D+ - D0 = delta + (2/3) E_c ;  Xi_cc+ - Xi_cc++ = delta - (4/3) E_c")
a = Dp[0] - D0[0]; ea = q(Dp[1], D0[1])
b = Xicc_p[0] - Xicc_pp[0]; eb = q(Xicc_p[1], Xicc_pp[1])
Ec = (a - b) / 2.0; eEc = q(ea, eb) / 2
dl = (2 * a + b) / 3.0; edl = q(2 * ea / 3, eb / 3)
print(f"   data: D+ - D0 = {a:.2f} +- {ea:.2f}, Xi_cc+ - Xi_cc++ = {b:+.2f} +- {eb:.2f}")
print(f"   => E_c = {Ec:.2f} +- {eEc:.2f} MeV (<1/r>^-1 = {197.327/ (Ec*137.036) :.2f} fm), delta = {dl:.2f} +- {edl:.2f} MeV")
print("   Zero d.o.f.: plausibility only. delta is an effective hadronic parameter, not the MS-bar m_d - m_u")
print("   (cycle 6: that comparison removed, [speculation]). Superflavor without QED predicts equal isospin")
print(f"   splittings; the data have opposite signs, but the baryon sign is only {abs(b)/eb:.1f} sigma from zero.")

print("\n(3) T_cc+ as superflavor partner of the anti-Lambda_c (both have light [ud]-type spin-0 dof)")
dM = 0.5 * ((Dst0[0] - D0[0]) + (Dstp[0] - Dp[0]))
MbarD = 0.25 * (0.5 * (D0[0] + Dp[0]) + 3 * 0.5 * (Dst0[0] + Dstp[0]))
Xi = 0.5 * (Xicc_pp[0] + Xicc_p[0])
for lab, dB in [("LO 3/4", 0.75 * dM), ("lattice 83.5", 83.5)]:
    MbarXi = Xi + (2 / 3) * dB
    pred = Lc[0] + MbarXi - MbarD
    print(f"   Delta_B = {lab:12s}: Mbar(Xi_cc) = {MbarXi:.1f}, Mbar(D) = {MbarD:.1f}, M(T_cc) = {pred:.0f} MeV;"
          f" observed {Tcc[0]:.1f}; miss {pred-Tcc[0]:+.0f} MeV ({100*(pred-Tcc[0])/Tcc[0]:+.1f}%)")
print(f"   D*+ D0 threshold = {DstpD0_thr:.2f}. LO superflavor puts T_cc ~110-130 MeV ABOVE threshold (unbound);")
print("   it is observed 0.36 MeV BELOW. Miss ~3% of the mass, ~1/m_c-sized, but it flips the qualitative")
print("   prediction (Eichten-Quigg 2017 also expected cc-ubar-dbar to dissociate). T_bb: Xi_bb unobserved,")
print("   so the relation cannot be evaluated from data (ruling R1: no unobserved states as evidence).")
