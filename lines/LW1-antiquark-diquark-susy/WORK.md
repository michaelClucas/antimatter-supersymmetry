# LW1 WORK

Labels: [established] / [conjecture] / [speculation]. Scripts in `calc/`, outputs in matching `.txt`.

## 1. Why the antiquark is the fermionic member

- SU(3)_c: 3 x 3 = 3bar (antisymmetric) + 6 (symmetric). The antisymmetric diquark has the same Casimir (4/3) as an antiquark, and <T_x . T_q> = -4/3 in the colour singlet for x = antiquark or 3bar diquark. Verified numerically in `calc/c1_color_and_spin.py`. [established]
- So, as seen by the remaining quark, a qbar and a [qq]_3bar are the same colour source. A meson (q qbar) and a baryon (q [qq]) differ only in replacing a spin-1/2 3bar object by a spin-0 or spin-1 3bar object. That is a fermion <-> boson exchange of the constituent. [established]
- The antiquark is essential: without it there is no fermionic 3bar constituent in the SM, and the meson side of every pair vanishes. Under C the whole structure maps to (antiquark, anti-diquark in 3) with identical spectra, so it is C- and CPT-symmetric. [established]

## 2. Heavy-quark superflavor (QCD-derived)

- In the m_Q -> infinity limit, the light degrees of freedom see only a static 3bar source; its spin decouples (heavy-quark spin symmetry). A heavy antiquark and a compact (QQ)_3bar diquark are then interchangeable. Savage & Wise 1990; derived within pNRQCD by Brambilla, Vairo, Roesch 2005 (arXiv:hep-ph/0506065). [established]
- Hyperfine relation at leading order: Delta(QQq; 3/2 - 1/2) = (3/4) Delta(Qbar q; 1 - 0). Derived in `calc/c1_color_and_spin.py`: meson spin factor 1, baryon factor (1/2)(3/2) = 3/4, the 1/2 because each heavy quark carries half the diquark colour-magnetic coupling. [established, reproduces Savage-Wise]
- Numbers (`calc/c2_superflavor_predictions.txt`, PDG 2024 meson masses):
  - Xi_cc*++ - Xi_cc++ = 106.5 MeV; Omega_cc* - Omega_cc = 107.9 MeV
  - Xi_bb* - Xi_bb = 34.0 MeV; Omega_bb* - Omega_bb = 36.4 MeV
- Comparison with lattice QCD: Xi_cc 82.8(9.2) MeV, Omega_cc 83.8(5.5) MeV (Brown, Detmold, Meinel, Orginos, arXiv:1409.0497); Xi_cc 87(13)(13)(2) MeV (UKQCD, hep-lat/0307025). LO superflavor overshoots by 18-22%, inside the naive O(Lambda/m_c) = 0.2-0.33 band. [established numbers; interpretation of the gap as 1/m_c correction is [conjecture]]
- Measured anchor: Xi_cc++ = 3621.55 +- 0.23 +- 0.30 MeV (LHCb, arXiv:1911.08594). The J=3/2 partner is predicted at ~3705-3728 MeV. **Falsifier**: a measured splitting outside ~[60, 125] MeV. [conjecture on the band edges]

## 3. Light-hadron supersymmetry (model level)

- LFHQCD formulas (arXiv:1604.06746): mesons M^2 = 4 lam (n+L_M) + 2 lam s, baryons M^2 = 4 lam (n+L_B+1) + 2 lam s, partners at L_M = L_B + 1. The pion is the zero mode with no partner. [established as the model's content]
- My independent fit (`calc/c3_lfhqcd_light_spectrum.txt`, state assignments following the paper, [conjecture] for L >= 1 baryons):
  - sqrt(lam): mesons 0.551 GeV, baryons 0.513 GeV; ratio of lam = 1.16. The paper quotes 0.524(23) and 0.509(15); the difference is state selection.
  - Pairs, dM/M: rho3/Delta(1700) -1.2%, a4/Delta(1950) +1.9%, a2/Delta(1232) +6.8%, pi2/N(1520) +9.8%, b1/N(939) +26.8%.
  - The s = 1 (rho-Delta) family works at a few percent. The s = 0 (pi-N) family is off by 10-27%, worst at the ground state.
- Status: this is a semiclassical holographic model with one fitted scale, not a theorem of QCD. Only the heavy-quark version (section 2) is QCD-derived. [established]

## 4. What this does and does not do for the SUSY results

- **#6 null results**: in hadronic SUSY every "superpartner" is an already observed hadron (or a predicted QCD state such as Xi_cc*). The SM's only realised boson-fermion multiplets need no new particles, so their existence is consistent with the LHC nulls. [established] This does not explain why elementary superpartners are absent; it only shows the SM already has the one SUSY-like spectrum nature exhibits. [conjecture on its significance]
- **#1 hierarchy, negative**: SUSY cancels quadratic sensitivity because boson and fermion loops have equal couplings up to the cutoff. Here the bosons (diquarks) are composite: above ~1 GeV they resolve into quarks, which are fermions, so there is no bosonic partner loop in the UV. The Higgs couples to quarks via Yukawas, not to diquarks as elementary fields. The breaking scale measured in section 3 is of order sqrt(lam) ~ 0.5 GeV itself, i.e. maximal. So antiquark-diquark SUSY cannot stabilise m_H. [conjecture; argument is standard compositeness reasoning, no calculation committed because no quantitative claim is made]
- **#2 unification**: diquarks are not independent fields and add nothing to beta functions (CONSTRAINTS D: CPT, each Dirac fermion counted once). No effect. [established]
- **#3 dark matter**: no stable neutral state beyond the proton/neutron family arises; superflavor partners decay strongly or weakly. No candidate. [established]
- **#4 radiative EWSB, #5 vacuum energy**: the symmetry acts on bound states at Lambda_QCD, not on the vacuum zero-point sum over elementary modes. No effect. [conjecture, trivially expected]

## 5. Verdict for this line

Positive structural statement: the SM's only realised supersymmetry pairs the antiquark with the 3bar diquark, and in the heavy-quark limit this follows from QCD and makes a testable prediction (Xi_cc* - Xi_cc). [established]

Negative statement: this SUSY-like structure is emergent at Lambda_QCD and cannot reproduce SUSY results #1-#5. [conjecture, fairly strong]

Novelty: the physics is known (Miyazawa 1966; Catto-Gursey 1985 [unverified citation: Nuovo Cim. A 86, 201 (1985)]; Savage-Wise 1990; Brodsky et al. 2015-16). What this line adds is the framing in this experiment's terms, an independent fit showing the s=0 vs s=1 asymmetry, and the explicit negative argument against using it for the hierarchy problem.

## 6. Dead ends / caveats

- Diquark clustering in light baryons is a model assumption. Lattice evidence for good (scalar 3bar) diquark correlations exists but I have not verified specific references. [unverified]
- Superflavor corrections for charm are not small; the prediction is LO only. A subleading pNRQCD calculation of the correction would sharpen the falsifier.
- Meson masses transcribed from PDG 2024 by hand; last digits [uncertain] but splittings are robust at the MeV level.

## 7. CONSTRAINTS checklist

- **A1**: only QCD quarks, antiquarks, gluons. Diquarks are qq correlations, not fields. No BSM. Pass.
- **A2**: no neutrino masses used. Pass.
- **A3**: LFHQCD is a model, not an equivalent reformulation; flagged, and hard claims restricted to the pNRQCD/HQET sector, which is an EFT of QCD. Pass with caveat.
- **B1-B8**: structure is C- and CPT-symmetric; predicts identical antibaryon/anti-meson spectra. No particle-antiparticle differences. Pass.
- **C1, C2**: no Higgs or EW inputs used. **C3**: addressed in section 4 (no new states). **C4**: not used.
- **D**: no claim about running; diquarks do not enter beta functions. Pass.
- **E1-E10**: no cosmological claim; no DM candidate claimed; no baryogenesis claim. Pass.
- **F1, F2**: baryon number conserved; superflavor relates states of different B but is a spectral relation, not a B-violating process. Pass.
- **G**: hierarchy discussed only as a negative argument; no regulator-based claim. Pass.
- **H1**: the 3/4 ratio is derived from spin and colour algebra, not fitted. The LFHQCD fit has one parameter and is presented as a test, not a result. **H2**: no loop integrals. **H3**: no interpretation-based mechanism. **H4**: scripts c1-c3 committed with outputs. Pass.
