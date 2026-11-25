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

## Cycle 3 update (literature check + subleading calculation)

Sources and verdicts: `LITCHECK.md`. Script: `calc/c4_subleading.py`, output `calc/c4_subleading.txt`.

### 8. Corrections to earlier sections

- Section 2: the 3/4 coefficient should be credited to Brambilla-Vairo-Rösch 2005 (eq. 35) and Fleming-Mehen 2006 (eq. 2), not to Savage-Wise alone. BVR state that the Savage-Wise formula is off by a factor 1/2 (missing colour normalization of the 3̄ state). [established, per BVR text]
- Section 2: the UKQCD number (Flynn-Mescia-Tariq) is from **quenched** QCD. Dynamical results: Brown+ 82.8(9.2), Alexandrou-Kallidonis 76(31) (from masses), PACS-CS 103(36) (from masses). [established]
- Section 5: Catto-Gürsey is CONFIRMED (Nuovo Cim. A 86, 201 (1985), DOI 10.1007/BF02902548). Drop the [unverified] tag.
- Section 6: diquark lattice evidence now cited: Alexandrou-de Forcrand-Lucini PRL 97, 222002 (2006); Francis et al. JHEP 05 (2022) 062. [established]
- PROPOSAL and section 5, "the SM's only realised SUSY": **overstated**. Nuclear dynamical supersymmetry (Iachello PRL 44, 772 (1980); Metz et al. PRL 83, 1542 (1999)) is another approximate Bose-Fermi symmetry in SM matter. Restrict the claim to "the only one whose fermionic member is an elementary SM field (the antiquark)". [established that the counterexample is in the literature]

### 9. Subleading corrections (c4)

What exists in the literature [established]: BVR eq. (35) generalises the relation across flavours, with chromomagnetic coefficients c_F, and quotes the error as O(α_s², Λ/m_Q). Fleming-Mehen name the leading correction operators (α_s²-suppressed 4-heavy-quark + B operators) but give no number. Mehen-Tiburzi show chiral corrections are small. **No published closed-form NLO value exists.** So c4 does four things:

| Step | Ξ_cc* − Ξ_cc (MeV) | Ξ_bb* − Ξ_bb (MeV) | Status |
|---|---|---|---|
| (A) LO, same flavour | 106.5 | 34.0 | [established] |
| (B) BVR eq. 35, LL c_F, cross-flavour | 121.8 (from B) | 29.7 (from D) | [established formula]. BVR at NLL: 133 / 27 |
| (B) BVR prescription | 114 ± 34 (reproduces BVR 120 ± 40) | 34.0 ± 3.4 (BVR 34 ± 4) | [established] |
| (C) Meson-sector calibration | Δ_B/Δ_D measured is 14% above LO-HQET (LL) scaling | | [conjecture: proxy for size] |
| (D) Lattice-calibrated: R_Q = (3/4)(1 + κ/s_Q), κ fixed by dynamical lattice R_cc = 0.588(61), s_Q = m_Q or m_Q v_Q | input | **30.4 ± 3.7** (Ω_bb 32-34) | [conjecture: one-parameter model] |
| Lattice (Brown+) | 82.8 ± 9.2 (dynamical mean 83.5 ± 8.6) | 34.6 ± 7.8 | [established] |

Corrected predictions [conjecture, error model stated in the script]:
- **Ξ_cc*⁺⁺ − Ξ_cc⁺⁺ = 107 ± 32 MeV** from the EFT alone (LO ± 30% power counting, the FM/BVR estimate). The lattice value 83 MeV sits at −22%, a −0.7σ pull. No EFT calculation beats this band, because the charm correction is not computable in closed form. With the lattice as calibration: 83 ± 9 MeV, i.e. M(Ξ_cc*⁺⁺) ≈ 3705 ± 9 MeV. The LO value is 3728 ± 32 MeV.
- **Ξ_bb* − Ξ_bb = 30 ± 4 MeV.** This is the line's real prediction after corrections: charm-calibrated 1/m_Q-type correction transported to bottom, enveloping the 1/m_Q and 1/(m_Q v) scalings, plus BVR's 10% for unmodelled α_s²(m_b v) terms. It is 1.0σ below LO (34.0) and 0.5σ from lattice (34.6 ± 7.8).
- Updated falsifier for charm: Ξ_cc* − Ξ_cc outside [75, 138] MeV at 1σ, or [43, 170] at 2σ. The old [60, 125] band was ad hoc. Use the 2σ band as the kill criterion.

Experimental status [established, INSPIRE 2026-11-25]: Ξ_cc⁺⁺ observed (LHCb 2017, mass 3621.55 ± 0.38 MeV, 2019). Ξ_cc⁺ observed in Run 3 (LHCb, PRL 137, 021902 (2026)). Ω_cc⁺ observed (LHCb, arXiv:2609.21921, 3725.9 MeV). **No J = 3/2 doubly heavy baryon has been observed or searched for in a published LHCb analysis.** For every central estimate Δ < m_π⁰, so Ξ_cc* decays only by M1 to Ξ_cc γ, with a photon of ~80-110 MeV in the rest frame (width ~keV-tens of keV, Cui et al. PRD 97, 034018). This is experimentally hard at LHCb. The falsifier is real but not near-term. [established kinematics; experimental feasibility is a conjecture]

### 10. Status after cycle 3

The physics is correct and QCD-derived in the heavy-quark sector. The prediction is a restatement of BVR 2005 at LO. The corrected numbers above add a lattice-calibrated Ξ_bb* value. Novelty (gate 6) fails except for the explicit #1 negative argument. Recommendation [conjecture]: fold into S1 or close as a documented negative appendix.

### 11. CONSTRAINTS checklist (complete, cycle 3)

| ID | Addressed | How |
|---|---|---|
| A1 | Pass | Only quarks, antiquarks, gluons. Diquarks are qq correlations in QCD bound states (lattice-supported, hep-lat/0609004), not fields. No superpartners in any mechanism; SUSY appears only as a comparison target. |
| A2 | Pass | No neutrino mass or PMNS input. |
| A3 | Pass with caveat | pNRQCD/NRQCD/HQET are EFTs of QCD (systematic expansions, not reformulations), so this is the SM sector. LFHQCD (section 3) is a semiclassical model, not an equivalent reformulation. It is labelled as such, and no hard claim rests on it. |
| B1 | Pass | Spectral relations are C-symmetric: anti-baryon/anti-meson spectra identical. No K⁰ mass splitting implied. |
| B2 | Pass | No particle/antiparticle q/m difference. |
| B3 | Pass | No antiproton moment difference. Hadronic magnetic moments are C-even. |
| B4 | Pass | No antihydrogen spectroscopy effect. |
| B5 | Pass | No gravitational claim. |
| B6 | Pass | No lepton g-factor effect. |
| B7 | Pass | No CP-violating operator introduced. No eEDM. |
| B8 | Pass | CKM not used. Strong-interaction spectra only. |
| B9 | Pass | Baryon CP violation (Λ_b) untouched. The relation is CP-even. |
| B10 | Pass | θ̄ not used. The hyperfine relation is P- and T-even. |
| C1 | N/A, pass | No Higgs input. #1 is treated only as a negative argument. |
| C2 | N/A, pass | No EW inputs. α_s(M_Z) from tools/sm_inputs.py (D). |
| C3 | Pass | All "partners" are observed or QCD-predicted hadrons at ≤ 11 GeV. No missing-energy signature. Consistent with LHC nulls; does not explain the absence of elementary superpartners (stated in section 4). |
| C4 | Pass | Not used. No g-2 claim. |
| D | Pass | α_s(M_Z) = 0.1180 used for 2-loop QCD running in c4 (loop order stated). Diquarks add nothing to beta functions. No unification claim. |
| E1 | Pass | No DM claim. The section 4 argument gives no stable neutral candidate. |
| E2, E3 | Pass | η and Ω_b not used or altered. |
| E4 | Pass | No vacuum-energy claim. The symmetry acts on bound states. |
| E5 | Pass | No DM properties claimed. |
| E6, E7, E8 | Pass | No neutrino or N_eff content. |
| E9 | Pass | No symmetric cosmology or antimatter domains. |
| E10 | Pass | No baryogenesis claim. QCD crossover not used. |
| F1 | Pass | No B violation. Baryon-meson "SUSY" relates spectra of different B. It is not a transition operator. |
| F2 | Pass | No sphaleron/instanton use. |
| F3 | Pass | No ΔB = 2 process. |
| G | Pass | Hierarchy only as a negative statement. No regulator-based claim. No Veltman-bracket number used. |
| H1 | Pass | 3/4 from spin-colour algebra (c1). The c4 correction model has one parameter, is fitted to lattice charm data and tested on bottom. It is labelled [conjecture]. |
| H2 | Pass | No loop integrals in c4. LL c_F is scheme-independent at LL. BVR quote NLL. The difference is part of the stated band. |
| H3 | Pass | No interpretation-based mechanism. |
| H4 | Pass | c1-c4 committed with .txt outputs. c4 imports tools/sm_inputs.py. |

## Cycle 4: constructive extension

Explorer, cycle 4 (D3, D5). Goal: push the SM-realised, antiquark-built supersymmetries as far as they go toward SUSY results #1 and #6. Scripts: `calc/c5_supercharge_algebra.py`, `calc/c5_susyqm_zero_mode.py`, `calc/c5_superflavor_protection.py`, `calc/c5_hadronic_supermultiplets.py`, each with a `.txt` output.

### 12. The supercharge in QCD variables (c5a)

Constituent level [established algebra, numerically checked]: with antiquark modes d_{a,s} (colour a in 3̄, spin s) and scalar 3̄ diquark modes D_a,

    Q_s = Σ_a D_a† d_{a,s},   {Q_s, Q_t†} = δ_st N_D + Σ_a d_{a,t}† d_{a,s},   {Q_s, Q_t} = 0.

Q_s is a colour singlet, fermionic, carries spin 1/2 and baryon number +1. The anticommutator is number and spin operators. With Q_{iα} = D_i† d_α for all boson modes i and fermion modes α, the algebra closes on u(m|n), the same superalgebra type as Iachello's nuclear U(6|m) (Catto-Gürsey 1985 for the hadronic case). With H = m_D N_D + m_d̄ N_d̄ + (colour-singlet light part), c5a checks [H, Q] = (m_D − m_d̄) Q: Q is a ladder operator with a fixed energy offset, not a conserved charge.

QCD level [established as an identity, numerically checked in a 15-mode Fock space]: the diquark is not a field. Writing D_a† ∝ ε_abc(u†_{b↑} d†_{c↓} − u†_{b↓} d†_{c↑}) (normalised so ⟨0|D_a D_a†|0⟩ = 1), the supercharge is cubic in quark operators,

    Q = Σ_a D_a† ā_a ∝ Σ ε_abc u†_b d†_c ā_a  (spin-singlet contraction implied),

and c5a verifies: Q is a colour singlet, changes fermion number by 3, and
{Q, Q†} = Σ_a D_a†D_a + Σ_ab ā_b† ā_a [D_b, D_a†] exactly, with [D_b, D_a†] = δ_ab − K_ab, where K is a quark bilinear (Pauli blocking; max deviation 2 in the test space). The eigenvalues of {Q, Q†} in the 2q+1q̄ sector are 0.5, 1, 1.5, 2. So it is not even a clean number operator, but it commutes with N_q, N_q̄ and colour, and contains no derivative.

Comparison with Poincaré SUSY [established + argument]:
- In the field theory each mode operator becomes ∫d³x of a local product with no derivative, so {Q, Q†} is ∫d³x of densities. No P_μ appears. Poincaré SUSY has {Q_α, Q̄_β̇} = 2σ^μ_αβ̇ P_μ, which is what makes H = (1/4)Σ{Q, Q†} and forces boson and fermion loops to match at every momentum.
- Haag-Łopuszański-Sohnius (Nucl. Phys. B 88, 257 (1975); cited in 1604.06746's reference list): a fermionic charge that commutes with the S-matrix of an interacting 4D relativistic theory must have {Q, Q̄} ∝ P_μ (plus central charges). Our {Q, Q†} is not of that form and is not central. So Q cannot be an exact symmetry of QCD. [conjecture as stated, follows from the theorem; the escape is that in the heavy-quark limit boosts are broken by the fixed heavy-quark velocity, so HLS does not constrain superflavor there]
- Classification: **internal, spectrum-generating (dynamical) supersymmetry**. It is the same type as nuclear SUSY, not spacetime SUSY. [established for the constituent algebra; conjecture that no QCD-level improvement changes this, supported by HLS]

Consequence for #1: the mechanism by which SUSY protects scalar masses (equal boson and fermion couplings integrated over all loop momenta, enforced by {Q, Q̄} = 2σ·P) has no counterpart, because nothing ties Q to the momentum integral. This sharpens the cycle-1 compositeness argument (section 4): even before compositeness, the algebra is the wrong type.

### 13. LFHQCD supercharge: here {R, R†} IS the Hamiltonian (c5b)

Brodsky-de Téramond-Dosch-Lorcé (1604.06746, eqs. 6-13, checked in the paper's text this cycle) build G = {R_λ, R_λ†}, with R_λ = Q + λS acting on (meson, baryon) wave functions in the light-front radial variable. This is Witten SUSY quantum mechanics: sl(1|1), one dimension, not 4D spacetime SUSY. Because the Hamiltonian is an anticommutator, there is a real protection theorem:

- c5b (toy with the same index structure, W = λx − g/x): partner towers {0, 4λ, 8λ, …} and {4λ, 8λ, …}, paired to 1e-5, one unpaired zero mode. [established, standard SUSY QM]
- Protection test: deform the superpotential (W → W + εx³) and E0 stays 0 to 1e-6 with the towers still paired, for ε up to 0.1. Add the same-size term directly to H, which breaks SUSY, and E0 shifts by +0.07 to +0.54 and the pairing splits by O(1). [established numerically]
- In LFHQCD the zero mode is the pion, so the model "protects" m_π = 0 in the chiral limit. With quark masses (eqs. 23-25 of the paper) each hadron gets its own ΔM², so SUSY is explicitly broken and m_π ≠ 0. That is the same content as chiral symmetry (GMOR). [conjecture: the SUSY-QM zero mode re-encodes Goldstone protection and adds no independent protection]

This is the one place where an antiquark-built SUSY reproduces the logic of #1: a mass (the pion's) set to zero by an index theorem and stable under deformations that keep the supercharge. It protects a composite at Λ_QCD in a semiclassical model, not the Higgs. [conjecture]

### 14. What heavy-quark superflavor actually protects, with data (c5c)

At leading order, the light degrees of freedom see the same static 3̄ source in Q̄q and (QQ)q. So the whole light-sector energy (Λ̄ ≈ 0.4 GeV, including light-flavour SU(3) breaking) cancels in the superpartner difference Δ_q = M(QQq) − M(Q̄q), which must be independent of q. Observed states only:

| q | M(QQq) − M(Q̄q) [MeV] |
|---|---|
| u: Ξ_cc⁺⁺ − D⁰ | 1756.7 ± 0.4 |
| d: Ξ_cc⁺ − D⁺ | 1750.3 ± 1.6 |
| s: Ω_cc⁺ − D_s⁺ | 1757.6 ± 1.3 |

- SU(3) breaking: 101.1 MeV in mesons (D_s − ⟨D⟩), 105.1 MeV in baryons (Ω_cc − ⟨Ξ_cc⟩). Residual not cancelled: **+4.0 ± 1.5 MeV, i.e. 4% of the breaking**. [established numbers; Ω_cc⁺ mass is from a 2026 preprint, arXiv:2609.21921]
- This is a genuine partner cancellation of a nonperturbative, flavour-dependent contribution, at the 96% level. It protects a mass difference between partners, not an absolute mass. Superflavor relates states whose masses differ by m_Q + E_bind ≈ 1.75 GeV. In #1 language: the analogue of "the scalar mass inherits the fermion's protection" is "the baryon's light-sector energy equals the meson's". The masses themselves get no protection. [conjecture on the interpretation]
- QED breaks superflavor explicitly: the cc diquark has charge +4/3 and c̄ has −2/3. A two-parameter decomposition [conjecture, zero d.o.f., plausibility only] gives E_c = α⟨1/r⟩ = 3.2 ± 0.8 MeV (⟨1/r⟩⁻¹ ≈ 0.45 fm) and δ = 2.7 ± 0.6 MeV ≈ m_d − m_u. It explains why the isospin splittings have opposite sign: D⁺ − D⁰ = +4.8 and Ξ_cc⁺ − Ξ_cc⁺⁺ = −1.6 MeV. So the SM's own gauge interactions break this supersymmetry at the MeV level, because the partners carry different electric charge. That is the opposite of SUSY, where partners carry identical gauge charges by construction. [established kinematics; interpretation is a conjecture]
- T_cc⁺ test. Superflavor also maps c (3) ↔ c̄c̄ (3), so T_cc = cc ū d̄ is the partner of the anti-Λ_c. Then M(T_cc) = M(Λ_c) + M̄(Ξ_cc) − M̄(D), the Eichten-Quigg-type relation (PRL 119, 202002 (2017), arXiv:1707.09575, title and abstract checked). This gives 4005 MeV at LO (3990 with the lattice hyperfine). Observed 3874.7 MeV (LHCb, Nat. Commun. 13, 3351 (2022), arXiv:2109.01056, title/journal checked; 0.36 MeV below D*⁺D⁰ [keV digits uncertain, from memory]). The miss is +115 to +130 MeV, 3%. The size is that of a 1/m_c correction, but it flips the qualitative call: superflavor at LO says unbound, nature says bound. [established numbers]
- T_bb (predicted deeply bound) and Ξ_bb are unobserved. Under ruling R1 they are not evidence.

### 15. #6: hadronic supermultiplets, counted (c5d)

Assignments from Nielsen & Brodsky, arXiv:1802.09652 (Tables 4-7, read from the PDF this cycle; Greek letters reconstructed from mass and J^P). The tetraquark rule (T = R B⁻, L_T = L_B) is from 1604.06746 sec. 2.3. Their earlier light candidates (1604.06746) were f0(980) for N, a1(1260) for Δ, and two I = 0 states (Greek lost; probably ω(1420)/ω(1650) [unverified]) for N(1520). The later paper changed N's partner to f0(500). The assignments are not stable. Double-heavy extension: Nielsen, Brodsky, de Téramond, Dosch, Navarra, Zou, PRD 98, 034002 (2018), arXiv:1805.11567 (checked).

Meson-baryon pairs: 40 rows, **31 with both members observed**, 4 with a predicted (unobserved) meson, 4 with a predicted baryon (all Ξ_bb-type or Ξ_cc(3900)), 1 with an unconfirmed meson (f2(1640)).

| sector | n | mean \|ΔM/M\| | mean \|ΔM\| | max \|ΔM\| |
|---|---|---|---|---|
| light | 15 | 6.9% | 97 MeV | 254 MeV (h1/N) |
| charm | 8 | 2.1% | 54 MeV | 136 MeV |
| bottom | 6 | 1.4% | 81 MeV | 112 MeV |
| double heavy | 2 | 2.3% | 81 MeV | 96 MeV |

Heavy-sector percentages are diluted by the heavy mass, so the MeV column is the fair measure: splittings are 50-100 MeV everywhere, i.e. 10-25% of √λ ≈ 0.5 GeV. [established numbers, PDG 2024 masses transcribed, last digits uncertain]

Tetraquark slots (the members with no conventional interpretation, the closest analogue of "superpartners nobody had seen"):
- 40 rows: 11 empty (no candidate), 6 predicted and unobserved, 23 filled with observed states.
- Of the 23: **2 are unambiguously non-q̄q** (π1(1600), exotic 1⁻⁺; Zc(3900), charged hidden charm, which shares a slot with X(3872)). 8 are established states with debated structure (f0(500), f0(980)/a0(980), K0*(1430), f0(1370)/a0(1450), f1(1420)/a1(1420), D0*(2300) twice, D_s0*(2317)). **13 are standard q̄q states relabelled as tetraquarks** (a1(1260), K1(1400), K2(1820), K1(1650), D0(2550), D_s1(2536), B_J(5732) twice, B_J(5840), χ_c0, χ_c1, χ_b0, χ_b1).
- Four observed states fill two partner slots each: D0*(2300), B_J(5732), K1(1270), Ξ_cc(3621).
- The LFHQCD map conflicts with QCD-derived superflavor. Superflavor pairs Ξ_cc with D (c̄ → cc, light quark spectator). LFHQCD pairs Ξ_cc with h_c(3525) (c̄ → [cq]). Both are "antiquark → diquark" maps but with different diquarks. Only the superflavor one follows from the QCD Lagrangian (pNRQCD).

Verdict on #6 [conjecture, based on the count]: the meson↔baryon half of hadronic SUSY is fully "confirmed" in the trivial sense that the partners are known hadrons, at a 50-100 MeV splitting. The genuinely new members predicted by the extended (tetraquark) multiplets are mostly relabelled ordinary mesons. Only 2 of 23 are confirmed exotics, and 6 predicted members are unobserved. This does not give a mechanism for #6 in the SUSY sense. The SM's realised SUSY has no missing partners because its partners were already in the hadron list. That is the cycle-1 statement, now quantified. It says nothing about why elementary superpartners are absent.

### 16. Nuclear supersymmetry: belongs here or not?

Iachello (PRL 44, 772 (1980)) and the Metz et al. quartet (PRL 83, 1542 (1999): ¹⁹⁴Pt, ¹⁹⁵Pt, ¹⁹⁵Au, ¹⁹⁶Au [quartet members from memory, unverified]) use bosons that are correlated nucleon pairs (in the Pt-Au region, proton-hole and neutron-hole pairs below Z = 82, N = 126) and fermions that are odd nucleons. A nuclear "hole" is a missing nucleon in a filled shell (a many-body quasiparticle with B = −1 relative to the reference nucleus). It is not an antinucleon: it does not annihilate and has no antiparticle quantum numbers. No antiquark or antinucleon enters. **Decision: nuclear SUSY is not built on antimatter and is out of scope as a mechanism for this line.** [established as to content; decision is mine] Keep it only as the algebraic template. Its supercharges b†a (boson creation × fermion annihilation) have exactly the form of section 12 with the antiquark replaced by a nucleon. It is the best-tested example that this class of SUSY is internal and spectrum-generating (H = function of Casimirs of U(m|n)), which supports section 12's classification. Only the hadronic version has an antimatter fermion.

### 17. Status after cycle 4

- New [established/numerical]: explicit QCD-level supercharge and its anticommutator (number/colour densities, no P_μ); the SM-realised antiquark-diquark SUSY is internal and spectrum-generating. HLS forbids it from being an exact spacetime symmetry of QCD.
- New [established numbers]: superflavor cancels 96% of the light-flavour SU(3) breaking between superpartners (residual 4.0 ± 1.5 MeV). This is the only quantitative "partner cancellation" found, and it protects differences, not masses.
- New [established numbers]: T_cc LO superflavor miss of +115 to +130 MeV (wrong side of threshold). #6 count: 31/40 meson-baryon pairs observed; 2/23 tetraquark slots are confirmed exotics, 13/23 are relabelled q̄q.
- LFHQCD's SUSY QM has a real zero-mode protection (pion), and it coincides with chiral symmetry.
- Bearing on #1: negative result strengthened from "composite, so no UV control" to "wrong algebra: {Q,Q†} has no P_μ, so no loop-momentum cancellation is possible even in principle". Bearing on #6: no explanatory power beyond "the partners were already observed".
- Novelty [conjecture, not lit-checked]: the explicit cubic QCD supercharge and its non-canonical anticommutator, the HLS classification argument, and the u/d/s residual and T_cc numbers as SUSY-analogue tests. The individual physics facts are known (Catto-Gürsey; Eichten-Quigg; LHCb masses).
- Constraints: same as section 11. The only new inputs are hadron masses (PDG 2024, LHCb 2022/2026). No BSM, no unobserved state used as evidence (Ξ_bb, T_bb, B_s0(5800) etc. only listed as unconfirmed). H1: no fitted numerology. The isospin decomposition is explicitly zero-d.o.f. and labelled plausibility only.
- Open: a referee should check the Greek-letter reconstruction in c5d against the 1802.09652 PDF, and the T_cc pole value (keV digits).
