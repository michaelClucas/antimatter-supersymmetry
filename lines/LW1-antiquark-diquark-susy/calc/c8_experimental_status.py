"""LW1 cycle 8, c8b: experimental status of the doubly heavy baryons (checked 2026-11-25) and what it does to P1/P2.

Sources read this cycle:
  LHCb, "Observation of the doubly charmed baryon Omega_cc+", arXiv:2609.21921 (submitted 18 Sep 2026, preprint):
      M = 3725.9 +- 1.0 (stat) +- 0.2 (syst) +- 0.4 (lifetime) +- 0.6 (ext) MeV, 8.7 sigma global, Omega_c0 pi+.
  LHCb, "Observation of the doubly charmed baryon Xi_cc+ with the LHCb Run 3 detector", arXiv:2603.28456,
      PRL 137 (2026) 021902: M = 3619.97 +- 0.83 +- 0.26 +1.90/-1.30 (lifetime) MeV, > 7 sigma, Lambda_c+ K- pi+.
  LHCb, Xi_cc++ mass 3621.55 +- 0.23 +- 0.30 MeV, arXiv:1911.08594, JHEP 02 (2020) 049.
  CERN EP newsletter, "LHCb completes a long-awaited family of doubly charmed baryons"
      (ep-news-wp.web.cern.ch/lhcb-completes-long-awaited-family-doubly-charmed-baryons/): the spin-1/2 ground-state
      family is complete; spin-3/2 states "remain to be observed". Doubly-beauty baryons: not observed.
"""
obs = {
    "Xi_cc++ (ccu, 1/2+)": (3621.55, (0.23**2 + 0.30**2) ** 0.5, "observed 2017; mass 1911.08594"),
    "Xi_cc+  (ccd, 1/2+)": (3619.97, ((0.83**2 + 0.26**2 + 1.90**2) ** 0.5, (0.83**2 + 0.26**2 + 1.30**2) ** 0.5),
                            "observed 2026, 2603.28456 / PRL 137, 021902"),
    "Omega_cc+ (ccs, 1/2+)": (3725.9, (1.0**2 + 0.2**2 + 0.4**2 + 0.6**2) ** 0.5, "observed 2026, 2609.21921 (preprint)"),
}
unobs = ["Xi_cc*++, Xi_cc*+ (3/2+)", "Omega_cc*+ (3/2+)", "Xi_bb, Xi_bb* (all)", "Omega_bb", "Xi_bc, Omega_bc", "T_bb"]
print("Doubly heavy baryons, status 2026-11-25")
for k, (m, e, note) in obs.items():
    es = f"+{e[0]:.2f}/-{e[1]:.2f}" if isinstance(e, tuple) else f"+-{e:.2f}"
    print(f"  {k:22s} {m:8.2f} {es:>13s} MeV   {note}")
print("  not observed:", "; ".join(unobs))
print(f"\n  Omega_cc+ - Xi_cc++ = {3725.9 - 3621.55:.1f} MeV (CERN EP: 'about 104 MeV heavier')")

print("\nP1 (Xi_cc* - Xi_cc): NO measurement exists. Pass/fail cannot be assigned.")
D = 142.014
for lab, x, e in [("LO superflavor (this line)", 0.75 * D, 32.0), ("dynamical lattice (Brown+ 2014)", 82.8, 9.2)]:
    print(f"  {lab:32s} {x:6.1f} +- {e:4.1f} MeV  -> M(Xi_cc*++) = {3621.55 + x:.0f} MeV")
print(f"  LO - lattice = {0.75*D-82.8:.1f} MeV. A measurement with total error <= 5 MeV separates them at "
      f"{(0.75*D-82.8)/(5**2+9.2**2)**0.5:.1f} sigma (lattice error included) and tests the 3/4 relation itself.")
print("  Omega_cc* - Omega_cc: LO 3/4 x (Ds*-Ds) = 107.9 MeV; lattice 83.8 +- 5.5 MeV; unmeasured.")
print("\nP2 (Xi_bb* - Xi_bb = 30 +- 4 MeV): Xi_bb itself unobserved; untested.")
print("\nR1 status change: Xi_cc+ (PRL 137, 021902) and Omega_cc+ (arXiv:2609.21921, 8.7 sigma) are observed states and may")
print("count as evidence (they were already used as inputs in c6b). Xi_cc*, Omega_cc*, Xi_bb(*), T_bb stay predictions only.")
