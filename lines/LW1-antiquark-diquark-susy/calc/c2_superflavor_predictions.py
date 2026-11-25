"""LW1 calc 2: heavy-quark superflavor predictions (Savage & Wise 1990; Brambilla, Vairo, Roesch 2005).

Leading-order relation (m_Q -> infinity, heavy diquark pointlike 3bar):
    M(QQq, J=3/2) - M(QQq, J=1/2) = (3/4) [ M(Qbar q, 1^-) - M(Qbar q, 0^-) ]
Corrections are O(Lambda_QCD / m_Q) from heavy-quark symmetry and O(r_diquark * Lambda_QCD)
from finite diquark size; for charm these are not small.

Meson masses: PDG 2024 (Phys. Rev. D 110, 030001), MeV. Last digits [uncertain] as transcribed.
Comparison numbers:
  Xi_cc++ mass 3621.55 +- 0.23 +- 0.30 MeV, LHCb arXiv:1911.08594 (JHEP 02 (2020) 049).
  Lattice Xi_cc* - Xi_cc = 82.8(9.2) MeV, Omega_cc* - Omega_cc = 83.8(5.5) MeV,
    Brown, Detmold, Meinel, Orginos, arXiv:1409.0497.
  Lattice Xi_cc* - Xi_cc = 87(13)(13)(2) MeV, UKQCD, Flynn, Mescia, Tariq, hep-lat/0307025.
"""
mes = {
    "D0": 1864.84, "D*0": 2006.85,
    "D+": 1869.66, "D*+": 2010.26,
    "Ds": 1968.35, "Ds*": 2112.2,
    "B+": 5279.41, "B0": 5279.72, "B*": 5324.75,
    "Bs": 5366.93, "Bs*": 5415.4,
}
r = 0.75
rows = [
    ("Xi_cc++ (ccu)  <-> D0bar (cbar u)", mes["D*0"] - mes["D0"]),
    ("Xi_cc+  (ccd)  <-> D-    (cbar d)", mes["D*+"] - mes["D+"]),
    ("Omega_cc (ccs) <-> Ds-   (cbar s)", mes["Ds*"] - mes["Ds"]),
    ("Xi_bb   (bbu)  <-> B+    (bbar u)", mes["B*"] - mes["B+"]),
    ("Omega_bb (bbs) <-> Bs0   (bbar s)", mes["Bs*"] - mes["Bs"]),
]
print("LO superflavor hyperfine predictions  Delta_baryon = 3/4 Delta_meson")
for name, d in rows:
    print(f"  {name}: meson hf = {d:7.2f} MeV -> baryon 3/2-1/2 = {r*d:6.1f} MeV")

lat = {"Xi_cc (Brown+ 2014)": (82.8, 9.2, r * (mes['D*0'] - mes['D0'])),
       "Omega_cc (Brown+ 2014)": (83.8, 5.5, r * (mes['Ds*'] - mes['Ds'])),
       "Xi_cc (UKQCD 2003)": (87.0, (13**2 + 13**2 + 2**2) ** 0.5, r * (mes['D*0'] - mes['D0']))}
print("\nComparison with lattice QCD (no experimental J=3/2 doubly-charmed state yet):")
for k, (v, e, p) in lat.items():
    print(f"  {k}: lattice {v:.1f} +- {e:.1f};  LO superflavor {p:.1f};  (LO - lat)/LO = {(p - v)/p:+.2f};  pull = {(p - v)/e:+.1f} sigma(lat)")

# Expected size of the leading correction: Lambda/m_Q with Lambda ~ 0.3-0.5 GeV, m_c ~ 1.5 GeV pole-ish
for mQ, lab in [(1.5, "charm"), (4.8, "bottom")]:
    lo, hi = 0.3 / mQ, 0.5 / mQ
    print(f"  naive O(Lambda/m_Q) correction band, {lab}: {lo:.2f} - {hi:.2f}")

# Spin-averaged consistency: what superflavor says about the mass of the 3/2 state given LHCb Xi_cc++
m_xi = 3621.55
print(f"\nPredicted Xi_cc*++ mass (LO) = {m_xi + r*(mes['D*0']-mes['D0']):.0f} MeV; lattice-informed ~ {m_xi+83:.0f} MeV")
print("Falsifier: a measured Xi_cc*++ - Xi_cc++ outside ~[60, 125] MeV would break LO superflavor plus a 30-40% correction.")
