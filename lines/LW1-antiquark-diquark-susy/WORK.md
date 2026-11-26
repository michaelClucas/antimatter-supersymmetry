# LW1 WORK

Labels: [established] / [conjecture] / [speculation]. Scripts in `calc/`, outputs in matching `.txt`.

## CLAIM (cycle 8, supersedes the cycle-6 CLAIM; history in sec. 17-23)

**Which SUSY result this bears on.** C1 bears on SUSY result #1 (Higgs-mass protection). It is a no-go for hadronic boson-fermion maps (heavy-quark superflavor, LFHQCD hadronic SUSY) as a Higgs-protection mechanism, not a general theorem about SM antimatter. Antimatter is not load-bearing in C1: arguments (a)-(c) below make no use of the fermionic member being an antiquark. C2 (#6) has no evidential weight. The line does not reproduce any SUSY result.

**Object.** The SM realises an approximate boson-fermion map in hadrons: every supermultiplet pairs a matter object with an antimatter object in the same colour representation (antiquark ↔ 3̄ diquark, or quark ↔ 3 anti-diquark). The supercharge is Q_σ = Σ_a D_a† q̄_{a,σ} (light version, LFHQCD) or Q_{m,σ} = Σ_a D_{a,m}† Q̄_{a,σ} (heavy-quark superflavor, Q̄ ↔ (QQ)_3̄). A world without antiquarks has no mesons and therefore none of these multiplets; that is a statement about the hadron spectrum, not a reason C1 holds. [established]

**C1 (SUSY #1, negative).** Hadronic superflavor / LFHQCD SUSY cannot cancel the UV-sensitive corrections to m_h² the way SUSY does, for three reasons:
- (a) Compositeness [established]. The bosonic members (diquark correlations inside baryons) and the hadrons they sit in are bound states of size ~1/Λ_QCD. Above ~1 GeV the propagating degrees of freedom are quarks and gluons; there is no diquark field to run in a loop. So the symmetry is absent, not softly broken, at the scales Λ_UV ≫ 1 GeV that drive δm_h² ∝ Λ_UV². This is the difference from soft-broken MSSM, where [H,Q] ≠ 0 too but the partners are elementary fields up to the UV, which leaves δm_h² = O(m_soft²) (sec. 24).
- (b) The Higgs is a singlet under Q [established]. Q acts on colour-3̄ constituents and changes baryon number by one; the Higgs carries neither colour nor baryon number, so Q maps H to nothing. The Higgs couples to quarks through Yukawas; the SM Lagrangian has no H-diquark coupling (diquarks are not fields), so there is no partner loop whose coupling is tied to y_t by Q.
- (c) HLS [established theorem, caveats sec. 19]. An exact fermionic symmetry of a Lorentz-invariant S-matrix has {Q, Q̄} ∝ P_μ (plus central charges): an exact version would be Poincaré SUSY with new elementary fields, excluded by scope rule A1.
- Size of the approximate breaking (context, not the argument) [established for the model; model is QCD-inspired, not QCD]. In the heavy sector, Q is approximate with genuine superflavor violation, isolated from heavy-quark spin breaking, of −13.6 MeV in Ξ_cc*−Ξ_cc (−13% of the 3/4 prediction) and −2.0 to −2.8 MeV (−7 to −8%) at bottom, with κ calibrated on the model's own ground state to D*−D = 142.0 MeV (c8_breaking_recalibrated, sec. 24). Dynamical lattice gives −24 MeV (−22%) at charm. In the light sector the breaking is O(Λ_QCD) (256 MeV in the c6 toy). The 1/m_Q scaling is the NRQCD chromomagnetic operator form (tree level c_F = 1), not a model result.
- Withdrawn: "[H,Q] ≠ 0, so Q cannot protect any mass" and the 102/33 MeV "genuine breaking" (sec. 24).

**C2 (SUSY #6) [established, weak].** All hadronic "superpartners" are known hadrons: 30/40 meson-baryon pairs in the Nielsen-Brodsky tables have both members observed (29 without a J^P conflict). The tables were built from known states, so this has no evidential weight. In tetraquark slots with an observed baryon, 1 state (π1(1600)) is unambiguously exotic. Hadronic SUSY says nothing about why elementary superpartners are absent.

**C3 (control, negative) [established for the models used].** The cancellation of light-flavour SU(3) breaking between superflavor partners (r_SF = +4.0 ± 1.6 MeV of 101 MeV) is not evidence for superflavor. In the additive quark model r is trivially zero for every pair (it is a double difference of quark-mass sums), so "AQM reproduces r_SF" is a definitional fact, not a fit. Two hyperfine-model fits with no superflavor tie give −13 and +14 MeV. Strange quarks next to a heavy source (D_s*, B_s, Ω_cc) give |r| ≤ 14 MeV, strange quarks in a light diquark 10-80 MeV: heavy-quark symmetry in general. Inputs Ξ_cc⁺ (PRL 137, 021902 (2026)) and Ω_cc⁺ (arXiv:2609.21921) are observed states (sec. 25).

**Falsifiable predictions.** P1 and P2 test the QCD heavy-quark relation (BVR 2005), not the SUSY claim C1 or C2: no outcome of P1/P2 can falsify C1. Numbers below are this line's evaluation.
- **P1.** M(Ξ_cc*⁺⁺) − M(Ξ_cc⁺⁺) = 107 ± 32 MeV (LO superflavor, 30% power-counting band, not a Gaussian error); dynamical lattice 83 ± 9 MeV; the recalibrated c8 model gives 93 MeV. So M(Ξ_cc*⁺⁺) ≈ 3705-3728 MeV. [established relation; band is a conjecture] **Status 2026-11-25: unmeasured.** LHCb has completed the spin-1/2 family (Ξ_cc⁺⁺, Ξ_cc⁺, Ω_cc⁺) but states that the spin-3/2 states remain to be observed (CERN EP newsletter, sec. 25). No pass/fail. Kill: Δ outside roughly [40, 170] MeV (naive 2× band) or ratio [Ξ_cc*−Ξ_cc]/[D*−D] far outside 0.5-0.9. The band contains every model estimate known to the line; LO alone is already disfavoured by lattice (Ω_cc: 4.4σ_lat). A measurement with ≤ 5 MeV error separates LO from lattice at 2.3σ. Expected decay Ξ_cc*⁺⁺ → Ξ_cc⁺⁺γ (Ξ_cc π threshold 135-138 MeV). [experimental feasibility: conjecture]
- **P2.** M(Ξ_bb*) − M(Ξ_bb) = 30 ± 4 MeV (lattice-calibrated refinement of BVR's 34 ± 4; B* − B⁺ = 45.34 MeV used; isospin-averaged 45.19 shifts the LO value from 34.0 to 33.9). Ξ_bb unobserved; untested. The c8 model calibrated on B*−B gives 31.2 MeV. [conjecture]
- **Consistency check.** u/d/s superpartner differences M(QQq) − M(Q̄q) agree to 7.2 MeV against a ~14 MeV 1/m_c allowance (sec. 14). Passes, but the AQM passes it trivially (C3).

**What is new** (LITCHECK sec. 3; restatement otherwise):
1. The #1 negative stated explicitly for hadronic SUSY via compositeness + Higgs-singlet + HLS (LITCHECK item 4 found no paper stating the hierarchy-problem consequence; search not exhaustive). New only as an explicit statement; no new physics.
2. In a calibrated constituent model, genuine superflavor violation separated from the heavy-quark spin breaking superflavor organises (sec. 24): −13% (charm), −7 to −8% (bottom) in the 3/4 relation.
3. The C3 control (a "partner cancellation" from cycle 4 is not superflavor-specific).
4. The lattice-calibrated Ξ_bb* number (P2). Minor refinement of BVR.
Known and not claimed: the antiquark ↔ diquark map (Miyazawa 1966, Catto-Gürsey 1985, Lichtenberg 1999, Dosch et al. 2015), the 3/4 relation and P1 (Savage-Wise 1990, BVR 2005, Fleming-Mehen 2006).

**Status.** Documented negative result for #1 (for hadronic boson-fermion maps only) plus a restated QCD prediction, still untested. Does not reproduce any SUSY result.

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
- **Ξ_bb* − Ξ_bb = 30 ± 4 MeV.** (Corrected cycle 6: a refinement of BVR, not "the line's real prediction". It is within 1σ of LO and lattice, so it does not discriminate; the κ calibration on Brown+ charm vs Brown+ bottom is correlated. Spread over five lattice charm inputs added in c6_xibb_budget: range 28.3-33.6, total still ±4.) Original text: charm-calibrated 1/m_Q-type correction transported to bottom, enveloping the 1/m_Q and 1/(m_Q v) scalings, plus BVR's 10% for unmodelled α_s²(m_b v) terms. It is 1.0σ below LO (34.0) and 0.5σ from lattice (34.6 ± 7.8).
- Updated falsifier for charm: Ξ_cc* − Ξ_cc outside [75, 138] MeV at 1σ, or [43, 170] at 2σ. The old [60, 125] band was ad hoc. Use the 2σ band as the kill criterion. (Corrected cycle 6: the ±32 is a power-counting estimate, so the "2σ" band is naive, not a Gaussian interval. The 1σ upper edge 139 MeV is above the Ξ_cc⁺⁺π⁰ (135.0) and Ξ_cc⁺π⁺ (138.0) thresholds.)

Experimental status [established, INSPIRE 2026-11-25]: Ξ_cc⁺⁺ observed (LHCb 2017, mass 3621.55 ± 0.38 MeV, 2019). Ξ_cc⁺ observed in Run 3 (LHCb, PRL 137, 021902 (2026)). Ω_cc⁺ observed (LHCb, arXiv:2609.21921, 3725.9 MeV). **No J = 3/2 doubly heavy baryon has been observed or searched for in a published LHCb analysis.** For every central estimate Δ < m_π⁰ (but not across the whole band; see c6_xibb_budget), so Ξ_cc* decays only by M1 to Ξ_cc γ, with a photon of ~80-110 MeV in the rest frame (width ~keV-tens of keV, Cui et al. PRD 97, 034018). This is experimentally hard at LHCb. The falsifier is real but not near-term. [established kinematics; experimental feasibility is a conjecture]

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

(Corrected cycle 6: the 15-mode toy below has one spatial mode and a SPINLESS antiquark, so its Q is a spin-0 fermionic operator and it cannot say anything about P_μ. Replaced by c6_hq_commutator Part A, sec. 18.) QCD level [established as an identity, numerically checked in a 15-mode Fock space]: the diquark is not a field. Writing D_a† ∝ ε_abc(u†_{b↑} d†_{c↓} − u†_{b↓} d†_{c↑}) (normalised so ⟨0|D_a D_a†|0⟩ = 1), the supercharge is cubic in quark operators,

    Q = Σ_a D_a† ā_a ∝ Σ ε_abc u†_b d†_c ā_a  (spin-singlet contraction implied),

and c5a verifies: Q is a colour singlet, changes fermion number by 3, and
{Q, Q†} = Σ_a D_a†D_a + Σ_ab ā_b† ā_a [D_b, D_a†] exactly, with [D_b, D_a†] = δ_ab − K_ab, where K is a quark bilinear (Pauli blocking; max deviation 2 in the test space). The eigenvalues of {Q, Q†} in the 2q+1q̄ sector are 0.5, 1, 1.5, 2. So it is not even a clean number operator, but it commutes with N_q, N_q̄ and colour, and contains no derivative.

Comparison with Poincaré SUSY (corrected cycle 6: "no P_μ" is an [argument], not numerically checked by c5a; "internal" is the wrong label, since Q_s carries spin 1/2 and does not commute with rotations; HLS relabelled; see sec. 19) [established + argument]:
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
- (Corrected cycle 6: error is ±1.6 MeV with the full Ξ_cc⁺ error; the "genuine partner cancellation" reading is withdrawn, because the additive quark model gives the same cancellation with no superflavor. See sec. 20.) This is a genuine partner cancellation of a nonperturbative, flavour-dependent contribution, at the 96% level. It protects a mass difference between partners, not an absolute mass. Superflavor relates states whose masses differ by m_Q + E_bind ≈ 1.75 GeV. In #1 language: the analogue of "the scalar mass inherits the fermion's protection" is "the baryon's light-sector energy equals the meson's". The masses themselves get no protection. [conjecture on the interpretation]
- (Corrected cycle 6: the δ ≈ m_d − m_u match is removed; δ is an effective hadronic parameter and m_d − m_u is a scheme-dependent current-mass difference. The baryon isospin sign is 0.8σ from zero. Any physical reading below is [speculation].) QED breaks superflavor explicitly: the cc diquark has charge +4/3 and c̄ has −2/3. A two-parameter decomposition [conjecture, zero d.o.f., plausibility only] gives E_c = α⟨1/r⟩ = 3.2 ± 0.8 MeV (⟨1/r⟩⁻¹ ≈ 0.45 fm) and δ = 2.7 ± 0.6 MeV ≈ m_d − m_u. It explains why the isospin splittings have opposite sign: D⁺ − D⁰ = +4.8 and Ξ_cc⁺ − Ξ_cc⁺⁺ = −1.6 MeV. So the SM's own gauge interactions break this supersymmetry at the MeV level, because the partners carry different electric charge. That is the opposite of SUSY, where partners carry identical gauge charges by construction. [established kinematics; interpretation is a conjecture]
- T_cc⁺ test. Superflavor also maps c (3) ↔ c̄c̄ (3), so T_cc = cc ū d̄ is the partner of the anti-Λ_c. Then M(T_cc) = M(Λ_c) + M̄(Ξ_cc) − M̄(D), the Eichten-Quigg-type relation (PRL 119, 202002 (2017), arXiv:1707.09575, title and abstract checked). This gives 4005 MeV at LO (3990 with the lattice hyperfine). Observed 3874.7 MeV (LHCb, Nat. Commun. 13, 3351 (2022), arXiv:2109.01056, title/journal checked; 0.36 MeV below D*⁺D⁰; δm_pole = −360 ± 40 keV, confirmed by referee 1). The miss is +115 to +130 MeV, 3%. The size is that of a 1/m_c correction, but it flips the qualitative call: superflavor at LO says unbound, nature says bound. [established numbers]
- T_bb (predicted deeply bound) and Ξ_bb are unobserved. Under ruling R1 they are not evidence.

### 15. #6: hadronic supermultiplets, counted (c5d)

Assignments from Nielsen & Brodsky, arXiv:1802.09652 (Tables 4-7, read from the PDF this cycle; Greek letters reconstructed from mass and J^P). The tetraquark rule (T = R B⁻, L_T = L_B) is from 1604.06746 sec. 2.3. Their earlier light candidates (1604.06746) were f0(980) for N, a1(1260) for Δ, and two I = 0 states (Greek lost; probably ω(1420)/ω(1650) [unverified]) for N(1520). The later paper changed N's partner to f0(500). The assignments are not stable. Double-heavy extension: Nielsen, Brodsky, de Téramond, Dosch, Navarra, Zou, PRD 98, 034002 (2018), arXiv:1805.11567 (checked).

(Corrected cycle 6, c6_census: 30/40 both observed, not 31. The row χ_c2(3556)/"Ξ_cc(3621) as 3/2⁺" used the unobserved J = 3/2 Ξ_cc*, a ruling-R1 breach; it is now PRED. Double-heavy n = 1. Max light |ΔM| = 254 MeV is K2(1770)/Λ(1520); h1/N is 227 MeV. EXO counted only where the baryon is observed: 1 (π1(1600)). QQB = 13 over all rows, 10 in rows with an observed baryon. J^P conflicts: D(2600) is 1⁻ in PDG (slot needs 2⁻), D0(2550) is 0⁻ per LHCb (slot needs 1⁺). Selection bias makes the count non-evidential.) Meson-baryon pairs: 40 rows, **31 with both members observed**, 4 with a predicted (unobserved) meson, 4 with a predicted baryon (all Ξ_bb-type or Ξ_cc(3900)), 1 with an unconfirmed meson (f2(1640)).

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
- (Corrected cycle 6: the next bullet's headline is overstated. Replaced by "Q is not a symmetry ([H,Q] ≠ 0), and HLS forbids an exact version"; see CLAIM C1 and sec. 19.) Bearing on #1: negative result strengthened from "composite, so no UV control" to "wrong algebra: {Q,Q†} has no P_μ, so no loop-momentum cancellation is possible even in principle". Bearing on #6: no explanatory power beyond "the partners were already observed".
- Novelty [conjecture, not lit-checked]: the explicit cubic QCD supercharge and its non-canonical anticommutator, the HLS classification argument, and the u/d/s residual and T_cc numbers as SUSY-analogue tests. The individual physics facts are known (Catto-Gürsey; Eichten-Quigg; LHCb masses).
- Constraints: same as section 11. The only new inputs are hadron masses (PDG 2024, LHCb 2022/2026). No BSM, no unobserved state used as evidence (Ξ_bb, T_bb, B_s0(5800) etc. only listed as unconfirmed). H1: no fitted numerology. The isospin decomposition is explicitly zero-d.o.f. and labelled plausibility only.
- Open: a referee should check the Greek-letter reconstruction in c5d against the 1802.09652 PDF, and the T_cc pole value (keV digits).

## Cycle 6: fix round (referee 1, cycle 5)

New scripts: `calc/c6_hq_commutator.py`, `calc/c6_superflavor_control.py`, `calc/c6_census.py`, `calc/c6_xibb_budget.py`. c5_superflavor_protection.py (Ξ_cc⁺ error, isospin text) and c5_supercharge_algebra.py (docstring and closing lines) were patched. All twelve scripts were rerun from inside `calc/` and their `.txt` outputs regenerated.

### 18. {Q, Q†} with momentum and spin (c6a, Part A)

Toy: 3-site ring (crystal momentum k = 0, 1, 2), distinguishable flavours s (spectator), u, d (diquark) and q̄ (antiquark), each with colour 3 × spin 2 × momentum 3 = 18 states. Meson sector |s q̄⟩: 324 states. Baryon sector |s u d⟩: 5832 states. Local scalar 3̄ diquark D†_{a,P} = Σ_k ε_abc (u†_{b↑,k} d†_{c↓,P−k} − ↑↔↓)/norm. Q_σ = Σ_{a,P} D†_{a,P} q̄_{a,σ,P}.

Results [established for the toy]:
- Q_σ lowers S_z by the removed antiquark spin, [S_+, Q_↑] = −Q_↓, [S_+, Q_↓] = 0: (Q_↓, −Q_↑) is a genuine spin-1/2 doublet. Colour singlet and momentum-conserving to machine precision.
- Meson sector: {Q_σ, Q_τ†} = Σ_{a,P} q̄†_{a,τ,P} q̄_{a,σ,P} exactly, so Σ_σ{Q_σ, Q_σ†} = N_q̄ = 1 on every meson state. A least-squares fit to c0 + c1 H_kin + c2 P gives c0 = 1, c1 ~ 1e-16, c2 ~ 1e-19. Its spectrum is {1} in each total-momentum sector, while H_kin ranges over 0.83-1.09 GeV.
- Baryon sector: Σ_σ Q_σ Q_σ† = 2Π, Π the projector onto (s quark) ⊗ (local scalar diquark).
- So {Q, Q†} contains nothing proportional to P or H. [argument] This follows because Q is a local product with no derivative. It restates that Q is a non-relativistic ladder operator. It is not an independent reason why Q fails to protect masses. That reason is sec. 19.

### 19. [H, Q] ≠ 0: the actual reason (c6a, Parts A and B)

Hamiltonian (QCD-inspired constituent model; De Rújula, Georgi, Glashow, PRD 12, 147 (1975) for the hyperfine form) [established model form]:
H = Σ_i (constituent mass + kinetic energy) + Σ_{i<j} V_ij,  V_ij = −κ (λ_i·λ_j)(S_i·S_j)/(m_i m_j) × contact,
with λ → −λ* for 3̄ objects. For the q-(QQ) pair the sum over the two heavy quarks, projected on (3̄, spin 1), gives the same operator with weight 1/2 in terms of the diquark generators, because the projector factorises into colour ⊗ spin and P λ_1 P = λ_D/2, P S_1 P = S_D/2. That reproduces the 3/4 rule (c1).

Part A (light map, q̄ ↔ [ud], m_s = 0.50, m_u = m_d = m_q̄ = 0.33 GeV, p0 = 0.35 GeV, κ set so the s-q̄ contact splitting is 0.40 GeV):

| H | ‖[H,Q]‖ | best offset δ | ‖[H,Q] − δQ‖ |
|---|---|---|---|
| kinetic + masses | 550 MeV | 431 MeV | 174 MeV |
| hyperfine only | 327 MeV | −227 MeV | 224 MeV |
| full | 412 MeV | 203 MeV | 256 MeV |

Q applied to the meson ground state (648 MeV) gives a baryon-sector state with ⟨H_B⟩ = 1162 MeV and energy spread σ_E = 137 MeV (baryon ground state 1006 MeV). Q maps an eigenstate onto a superposition of eigenstates, so it is not a symmetry even up to a constant shift. [established for the model]

Part B (heavy map Q̄ ↔ (QQ)_3̄ spin 1, light quark m = 0.33 GeV, p0 = 0.40 GeV [assumption], κ fixed by D*−D or B*−B):

| | offset δ | ‖B‖ hyperfine only | ‖B‖ recoil only | ‖B‖ both |
|---|---|---|---|---|
| charm (m_c = M(J/ψ)/2) | 1531 MeV | 100.4 MeV | 17.2 MeV | 101.6 MeV |
| bottom (m_b = M(Υ)/2) | 4725 MeV | 32.1 MeV | 5.6 MeV | 32.5 MeV |

With κ scaled as 1/m_Q, m_Q‖B‖ = 157 MeV·GeV for m_Q from 1.5 to 500 GeV. So [H, Q] = δQ + B with B = O(Λ²/m_Q). [established for the model]

Reading [established unless marked]:
1. Q is not conserved. The offset δ ≈ m_Q is removable only by subtracting the separately conserved heavy-quark number (what HQET does). The remainder B vanishes only at m_Q → ∞. At physical charm it is ~100 MeV, ~25% of the light-dof energy Λ̄ ≈ 0.4 GeV. At bottom it is ~33 MeV. For the light map there is no heavy limit at all and the breaking is O(Λ_QCD).
2. The hadron data say the same without a model: the partners are non-degenerate (sec. 14, 15).
3. HLS (Nucl. Phys. B 88, 257 (1975)) closes the door on an exact version: an exact fermionic symmetry of a Lorentz-invariant S-matrix must have {Q, Q̄} ∝ P_μ plus central charges. QCD has no such symmetry. Caveats: HLS assumes a Lorentz-invariant S-matrix of asymptotic states (here hadrons), and Q acts on confined constituents, so HLS applies to any hadron-level image of Q. In the heavy-quark limit the fixed heavy-quark velocity breaks boosts, which is why superflavor can be an exact symmetry of the m_Q → ∞ effective theory without contradicting HLS. "Q is not an exact symmetry of QCD" is [established] (data + this section). Only "no QCD-level improvement changes the classification" stays [conjecture].
4. Label: Q is a non-relativistic spectrum-generating superalgebra whose anticommutator is not proportional to P. It is not "internal", since it carries spin 1/2.
5. Consequence for #1: a symmetry that protects a mass must commute with H. This one does not. A hypothetical exact Bose-Fermi symmetry with equal couplings would cancel loops however its algebra was written, and HLS then forces it to be Poincaré SUSY. Plus compositeness above ~1 GeV. That is the full negative.

### 20. Control for the SU(3)-breaking cancellation (c6b)

Corrected error first: Ξ_cc⁺ total +2.09/−1.56 MeV (0.83 stat, 0.26 syst, +1.90/−1.30 lifetime), symmetrised 1.83. r_SF = +4.0 ± 1.6 MeV (1.2 MeV if the Ω_cc⁺ ext and lifetime terms are treated as correlated with the Ξ_cc masses; 1.6 quoted).

Controls, residual r = Δ_s(X) − (D_s − ⟨D⟩), Δ_s = strange minus non-strange member:

| pair | relation to D | r (MeV) |
|---|---|---|
| Ω_cc − Ξ_cc | superflavor | +4.0 |
| D_s* − D* | HQ spin | +2.5 |
| B_s − B | HQ flavour | −13.7 |
| B_s* − B* | HQ spin+flavour | −10.4 |
| K* − ρ, φ − K* | none | +17.2, +24.8 |
| Σ* − Δ, Ξ* − Σ*, Ω − Ξ* | none | +51.5, +47.7, +38.0 |
| Ξ_c′ − Σ_c, Ξ_c* − Σ_c*, Ω_c − Ξ_c′, Ω_c* − Ξ_c* | none (light spin-1 diquark) | +23.9, +26.4, +15.7, +19.2 |
| Ξ_b′ − Σ_b, Ξ_b* − Σ_b*, Ω_b − Ξ_b′ | none | +20.8, +20.2, +9.7 |
| Ξ_c − Λ_c, Ξ_b − Λ_b | none (light spin-0 diquark) | +81.5, +73.7 |

Non-superflavor, non-heavy-symmetry pairs: n = 14, median |r| = 24 MeV, range 10-82. [established numbers; PDG 2024 masses transcribed]

Models:
- Additive quark model (SU(3) breaking, no superflavor): r = 0 for every pair, by construction. Its fit to 34 ground-state hadrons has rms 89 MeV. Its error on the 17 control residuals has rms 36 MeV.
- DGG hyperfine model, meson and baryon coefficients free (no superflavor tie; the tie would be A_B/A_M = 0.5, fits give 0.35): (3a) common light masses + constants, rms 20 MeV, r_SF = −13.2 MeV. (3b) Griffiths-style separate meson/baryon light masses, rms 23 MeV, r_SF = +14.2 MeV. Both get the control residuals badly wrong (rms ~50 MeV), so they bracket a generic expectation of |r_SF| ≲ 15 MeV rather than predict it.

Verdict [established for these models]: the observed r_SF = +4.0 ± 1.6 MeV is reproduced by the additive quark model with no superflavor. **It is not evidence for superflavor.** The "96% partner cancellation" language of sec. 14 and 17 is withdrawn. What the data show is a pattern: strange quarks next to a heavy source (D_s*, B_s, Ω_cc) give |r| ≤ 14 MeV, strange quarks inside a light diquark give 10-80 MeV. That is heavy-quark symmetry in general (light-heavy spin coupling suppressed by 1/m_Q), of which superflavor is one instance. "Superflavor protects differences, not masses" stays as a statement of what the symmetry would do. The SUSY-protection analogy is dropped.

Isospin (finding 5): Ξ_cc⁺ − Ξ_cc⁺⁺ = −1.58 ± 1.87 MeV is 0.8σ from zero, so "opposite sign" is not established. The zero-d.o.f. solve E_c = 3.2 ± 0.9, δ = 2.7 ± 0.6 MeV is kept as arithmetic only. The δ ≈ m_d − m_u comparison is removed. [speculation: any physical reading]

### 21. Bookkeeping (c6c, c6d)

- Census: 30/40 both observed (29/40 without the D(2600) J^P conflict). Double-heavy n = 1. Light max |ΔM| = 254 MeV is K2(1770)/Λ(1520); h1/N is 227 MeV. QQB: 13 over all rows (c5d "status counts" line), 10 in rows with an observed baryon (c5d's stats line printed n = 11 because it still counted the Ξ_cc* row as observed). The headline number is 13 slots, 10 usable. EXO in rows with an observed baryon: 1 (π1(1600)); Zc(3900) sits in a row whose baryon is unobserved. Tetraquark-slot conflict: D0(2550) is 0⁻ (LHCb), slot needs 1⁺. Selection bias: the tables were built from known states, so the observed fraction carries no evidential weight.
- Ξ_bb budget: κ from each of five dynamical charm inputs (Brown+ Ξ_cc and Ω_cc, Alexandrou-Kallidonis, PACS-CS, Mathur-Padmanath Ω_cc 76(6)(6)) and two scalings gives 28.3-33.6 MeV. Adding that spread to c4's ±3.7 leaves 30 ± 4 MeV. Called a refinement, not a test.
- Ξ_cc* thresholds: Ξ_cc⁺⁺π⁰ at 135.0, Ξ_cc⁺π⁺ at 138.0 MeV. The EFT 1σ upper edge (139) is above both, so "M1 only" holds for central values only.
- T_cc (finding 10): this line's LO 4005 MeV vs Eichten-Quigg's 3978 MeV differ by 27 MeV. EQ include a hyperfine term between the cc diquark and the light antidiquark and use their own inputs; I have not checked their full text, so the difference is noted, not reconciled. Both are 100+ MeV above the observed 3874.7, so "LO superflavor says unbound" is unaffected.
- Metz et al. quartet (¹⁹⁴Pt, ¹⁹⁵Pt, ¹⁹⁵Au, ¹⁹⁶Au): referee 1 confirms from memory. Abstract not re-checked this cycle; tag changed to [referee-confirmed, abstract not re-read].
- Framing (finding 9): superflavor maps Q̄ ↔ QQ and equally Q ↔ Q̄Q̄ (used for T_cc). Which member is "the antiquark" depends on the C convention. Convention-independent wording (used in CLAIM and PROPOSAL): every supermultiplet pairs a matter object with an antimatter object in the same colour representation, so a world without antiquarks has none.

### 22. Response to referee 1 (cycle 5)

| # | Finding | Response |
|---|---|---|
| 1 | Toy cannot show "no P_μ"; spinless antiquark; "internal" wrong; real reason is [H,Q] ≠ 0 | Accepted. New toy with 3 momentum modes and spin-1/2 antiquarks (sec. 18): Q is a spin-1/2 doublet; {Q,Q†} has no P or H component, labelled [argument] and demoted. [H,Q] computed explicitly with a colour-magnetic Hamiltonian (sec. 19): breaking 102 MeV (charm), 33 MeV (bottom), O(Λ²/m_Q); 256 MeV for the light map. #1 negative restated as (i) not conserved, (ii) HLS forbids an exact version, (iii) composite bosons. "Internal" replaced. c5a docstring says the old toy antiquark is spinless. |
| 2 | Ξ_cc* counted as observed (R1) | Accepted. 30/40, double-heavy n = 1, EXO with observed baryon = 1 (c6_census). |
| 3 | 96% cancellation not specific to superflavor | Accepted, and the answer is that it is not evidence for superflavor at all. Controls (17 pairs) and three models (AQM, two DGG fits) in sec. 20. SUSY-protection wording dropped. |
| 4 | Ξ_cc⁺ error | Fixed: +2.09/−1.56, residual 4.0 ± 1.6 (c5c patched, c6b). |
| 5 | Isospin numerology | m_d − m_u match removed, sign stated as 0.8σ, readings labelled [speculation]. |
| 6 | HLS label | "Not exact" now [established]; HLS caveats (asymptotic hadron states, confined constituents, heavy-quark escape) stated in sec. 19. |
| 7 | Error budgets | 2σ band called naive; threshold caveat added; Ξ_bb called a refinement; lattice-input spread added (c6_xibb_budget). |
| 8 | Bookkeeping | Max |ΔM| label, QQB 13 vs 10, J^P conflicts flagged, selection bias stated (sec. 21). |
| 9 | Antimatter framing | Convention-independent wording adopted (CLAIM, PROPOSAL). |
| 10 | T_cc vs Eichten-Quigg | Difference noted, not reconciled; conclusion unaffected (sec. 21). |
| Inputs | T_cc keV tag, Metz tag | T_cc tag replaced by −360 ± 40 keV. Metz tag downgraded to referee-confirmed. |

### 23. CONSTRAINTS checklist (cycle 6, replaces sec. 11)

| ID | Status | How |
|---|---|---|
| A1 | Pass | Only quarks, antiquarks, gluons. Diquarks are qq correlations inside hadrons (lattice: hep-lat/0609004, arXiv:2106.09080), not fields. The c6a "diquark modes" are composite states built from quark operators (Part A) or a stated constituent-model approximation (Part B). No superpartner in any mechanism. Unobserved states (Ξ_cc*, Ξ_bb, T_bb) are predictions only, never evidence (R1, now also in the census). |
| A2 | Pass | No neutrino input. |
| A3 | Pass with caveat | pNRQCD/NRQCD/HQET are EFTs of QCD. LFHQCD and the DGG/AQM constituent models are models, not equivalent reformulations. They are labelled as such and used only as controls or illustrations. The [H,Q] ≠ 0 conclusion does not depend on them: the data and HLS give it independently. |
| B1-B4 | Pass | All relations are C-symmetric: antihadron spectra identical. No particle-antiparticle mass, q/m, moment or spectroscopy difference. |
| B5 | Pass | No gravitational claim. |
| B6 | Pass | No lepton g-factor effect. |
| B7, B10 | Pass | No CP- or T-odd operator. The hyperfine term is P- and T-even. θ̄ not used. |
| B8, B9 | Pass | CKM not used. Baryon CP violation untouched. |
| C1, C2 | Pass (N/A) | No Higgs or EW input. #1 is addressed only as a negative statement. |
| C3 | Pass | All "partners" are observed hadrons or QCD-predicted states below 11 GeV. Consistent with LHC nulls. Does not explain the absence of elementary superpartners (CLAIM C2). |
| C4 | Pass | No g-2 claim. |
| D | Pass | α_s(M_Z) = 0.1180 for 2-loop running in c4. Diquarks add nothing to beta functions. No unification claim. |
| E2, E3 | Pass | η, Ω_b not used. |
| E4 | Pass | No vacuum-energy claim. |
| E6-E8 | Pass | No neutrino or N_eff content. |
| E9 | Pass | No symmetric cosmology or antimatter domains. |
| E10 | Pass | No baryogenesis claim. Q changes B by 1 only as a spectral map between sectors, not a process. |
| F1, F3 | Pass | No B-violating transition. Q relates spectra; it is not in the Hamiltonian. |
| F2 | Pass | No sphaleron/instanton use. |
| G | Pass | Hierarchy only as a negative statement. No regulator-based claim, no Veltman bracket used. |
| H1 | Pass | 3/4 from spin-colour algebra (c1). The c6b models are fitted controls and labelled; the cycle-4 numerology (δ ≈ m_d − m_u, "96% protection") is withdrawn. |
| H2 | Pass | No loop integrals. LL vs NLL c_F difference is inside the stated band. |
| H3 | Pass | No interpretation-based mechanism. |
| H4 | Pass | c1-c6 committed with `.txt` outputs, all rerun this cycle from `calc/`. |
(E1, E5: dark matter is out of scope by directive D1; no DM claim is made.)

## Cycle 8: fix round 2 (referee 2, cycle 7)

New scripts: `calc/c8_breaking_recalibrated.py`, `calc/c8_experimental_status.py`. `calc/c6_hq_commutator.py` patched (the "142 → 106.5 (3/4 rule)" line is now labelled as the analytic formula at contact eigenvalue 1, not the model spectrum; the scaling table is labelled as imposed). All fourteen line scripts (c1-c8, not referee*) rerun from inside `calc/`, `.txt` outputs regenerated, all exit 0.

### 24. Superflavor breaking, separated and recalibrated (c8a)

Same model as sec. 19 Part B, worked in the colour-singlet sector (reproduces c6: ‖B‖ = 101.6 MeV, and referee 2's 57.9 MeV ground-state D*−D at the c6 κ).

Calibration [established for the model]. κ is now fixed so that the model's own ground state (colour singlet, total momentum 0, lowest J = 0 and J = 1) has D*⁰ − D⁰ = 142.0 MeV. This needs 2.05× the c6 κ, because the contact operator has eigenvalue 1/3 on the kinetic ground configuration. Results (MeV):

| | meson J=1−0 | baryon 3/2−1/2 | ratio | r_hf = Δ_B − ¾Δ_M | r_avg |
|---|---|---|---|---|---|
| charm (κ from D*−D) | 142.0 | 92.9 | 0.654 | −13.6 (−12.8%) | +4.1 |
| bottom (same κ, predicted) | 37.3 (PDG 45.34, −18%) | 26.0 | 0.697 | −2.0 (−7.0%) | +0.6 |
| bottom (κ from B*−B⁺ = 45.34) | 45.3 | 31.2 | 0.689 | −2.8 (−8.2%) | |
| dynamical lattice, charm (Brown+ 2014) | 142.0 (input) | 82.8 ± 9.2 | 0.583 | −23.7 (−22%) | |

r_avg = (M̄_B − M̄_M) − (m_(QQ) − m_Q̄), with spin-averaged masses. Both residuals vanish at leading order in superflavor.

Decomposition of the commutator at the calibrated κ [established for the model]: [H, Q] = δQ + [V_hf, Q] + ([K_X, Q] − δ_X Q). The light-quark kinetic term commutes with Q exactly.

| | δ | ‖[V_hf, Q]‖ (HQ spin breaking) | ‖recoil‖ (genuine) |
|---|---|---|---|
| charm | 1531 MeV | 206 MeV | 17.2 MeV |
| bottom | 4725 MeV | 68 MeV | 5.6 MeV |

Reading:
1. [V_hf, Q] is heavy-quark spin breaking. Its meson and baryon matrix elements are tied by the superflavor Clebsch 1/2, which is the 3/4 rule; at first order in the spin-breaking spurion superflavor predicts its pattern (BVR spurion analysis). So its norm is not superflavor violation. The cycle-6 "genuine breaking 102/33 MeV" was this term (at a miscalibrated κ) and is withdrawn. [established]
2. Genuine superflavor violation in the model is the recoil operator (the source kinetic energy p²/(2m_X) has m_X = m_Q vs 2m_Q, not of superflavor-covariant form) and the observable residuals r_hf, r_avg. r_hf comes mainly from second order in the hyperfine spurion (it mixes the ground configuration with excited ones, with different strength in the two sectors; −18.5 MeV with recoil switched off). The quoted superflavor-violation measure is r_hf: −13% at charm, −7 to −8% at bottom. Referee 2 found −8% / −3% at the uncalibrated κ; calibration roughly doubles the hyperfine coupling and the second-order effect grows with it. [established for the model]
3. The model's −13% has the same sign as lattice's −22% and is about 60% of it. The model is QCD-inspired with illustrative m_q = 0.33, p0 = 0.40 GeV, so this agreement is not evidence. [numbers established; interpretation conjecture]
4. 1/m_Q scaling is not derived by the model. The hyperfine operator V ∝ κ/(m_q m_Q) is the tree-level NRQCD chromomagnetic term c_F g σ·B/(2m_Q) with c_F = 1, so holding κ fixed (one coupling) gives Δ_M ∝ 1/m_Q. The fixed-κ scan gives exponents −1.02 for Δ_M and −1.00 for ‖[V_hf,Q]‖ and ‖recoil‖, which only shows consistency. The one model output is the bottom splitting predicted from the charm κ (37.3 vs 45.3 MeV, −18%); the miss comes from the same second-order mixing, and c_F running is neglected. [established: HQET scaling; model output as stated]
5. Toy limitation: r_hf and r_avg scale as m_Q⁻² in the scan. That is a property of this toy (the ground configuration has both constituents at zero momentum, so the first-order source recoil vanishes). In QCD the source kinetic energy (λ₁-type terms) differs between meson and baryon at O(Λ²/m_Q), so superflavor violation starts at O(Λ/m_Q) relative to the splittings. That is why the P1 band stays at 30% (c4) and not at the model's 13%. [established as HQET power counting]
6. Sec. 19 reading 5 ("a symmetry that protects a mass must commute with H") is withdrawn. Approximate symmetries protect masses up to their breaking (chiral symmetry: m_π² ∝ m_q; soft-broken MSSM: δm_h² = O(m_soft²) with [H,Q] ≠ 0). C1 now rests on compositeness, the Higgs being a Q-singlet, and HLS (CLAIM).

### 25. Experimental status of doubly heavy baryons (c8b, checked 2026-11-25)

Sources read this cycle: LHCb, arXiv:2609.21921 (Ω_cc⁺ observation, submitted 18 Sep 2026, preprint); LHCb, arXiv:2603.28456 = PRL 137 (2026) 021902 (Ξ_cc⁺ with the Run 3 detector); CERN EP newsletter, "LHCb completes a long-awaited family of doubly charmed baryons" (ep-news-wp.web.cern.ch/lhcb-completes-long-awaited-family-doubly-charmed-baryons/) and "Doubly charmed baryon doublet completed with upgraded LHCb" (same site).

| State | Mass (MeV) | Status |
|---|---|---|
| Ξ_cc⁺⁺ (1/2⁺) | 3621.55 ± 0.38 | observed (LHCb 2017; mass arXiv:1911.08594) |
| Ξ_cc⁺ (1/2⁺) | 3619.97 +2.09/−1.56 | observed, > 7σ, Λ_c⁺K⁻π⁺, 6.9 fb⁻¹ of 2024 Run 3 data |
| Ω_cc⁺ (1/2⁺) | 3725.9 ± 1.25 | observed, 8.7σ global, Ω_c⁰π⁺, 6.3 fb⁻¹; Ω_cc⁺ − Ξ_cc⁺⁺ = 104.3 (EP news: "about 104 MeV") |
| Ξ_cc*, Ω_cc* (3/2⁺) | none | not observed. EP news: the spin-1/2 ground-state family is complete, spin-3/2 states remain to be observed |
| Ξ_bb, Ξ_bb*, Ω_bb, Ξ_bc, T_bb | none | not observed |

Result:
- P1 (107 ± 32 MeV; lattice 83 ± 9 MeV): **no measurement of Ξ_cc* or of Ξ_cc* − Ξ_cc exists, so pass/fail cannot be assigned.** The referee's sources complete the spin-1/2 family; they do not measure a J = 3/2 state. [established, from the sources above]
- P2: Ξ_bb unobserved; untested.
- R1: Ξ_cc⁺ (published PRL) and Ω_cc⁺ (8.7σ LHCb preprint) are observed states and may count as evidence. They were already inputs to c6b (C3), which therefore does not violate R1. Ξ_cc*, Ω_cc*, Ξ_bb(*), T_bb remain predictions only.

### 26. Response to referee 2 (cycle 7)

| # | Finding | Response |
|---|---|---|
| 1 | 102/33 MeV is HQ spin breaking that superflavor predicts | Accepted. c8a splits [H,Q] into offset, [V_hf,Q] (HQ spin breaking, superflavor-tied: 206/68 MeV at calibrated κ) and recoil (17.2/5.6 MeV). Superflavor violation is now quoted as the residual of the 3/4 relation: r_hf = −13.6 MeV (−13%) charm, −2.0 to −2.8 MeV (−7 to −8%) bottom; spin-averaged residual +4.1 / +0.6 MeV. 102/33 withdrawn (sec. 24). |
| 2 | Model not calibrated to D*−D | Accepted. κ fixed on the model's own ground state (142.0 MeV), 2.05× the c6 value. Bottom given both as a prediction from the charm κ (37.3 MeV, −18%) and recalibrated on B*−B. c6 print line relabelled as the analytic contact-eigenvalue-1 formula. |
| 3 | 1/m_Q inserted | Accepted. Stated as the NRQCD chromomagnetic operator form (tree-level c_F = 1); the fixed-κ scan only shows consistency; the bottom splitting from the charm κ is the one model output. The toy's m_Q⁻² residual scaling is flagged as an artifact; in QCD it is O(Λ/m_Q) relative (sec. 24 items 4-5). |
| 4 | "[H,Q] ≠ 0 ⇒ no protection" false | Accepted. C1 rebuilt on (a) compositeness, (b) Higgs singlet under Q with no H-diquark coupling, (c) HLS. [H,Q] ≠ 0 recast as "Q is approximate", sizes given as context. "Any scalar mass, Higgs or hadronic" removed. Sec. 19 reading 5 withdrawn. Contrast with soft-broken MSSM stated in (a). |
| 5 | {Q,Q†} not evidence | Agreed; not cited in CLAIM. |
| 6 | AQM r = 0 trivially | C3 now says trivially zero (double difference of quark-mass sums). Ω_cc⁺ input confirmed observed (sec. 25). |
| 7 | B*−B choice | CLAIM P2 states B* − B⁺ = 45.34 MeV; isospin-averaged 45.19 gives 33.9 vs 34.0 MeV. |
| 8 | P1/P2 do not test C1 | Accepted. CLAIM says P1/P2 test the QCD relation, not C1/C2, and notes that LO is already disfavoured by lattice and the band contains all models. |
| 9 | P2 transport | Kept as [conjecture]; the c8 model calibrated on B*−B gives 31.2 MeV, inside 30 ± 4. |
| 10 | Gate item 1 | Added at the top of CLAIM: bears on #1; no-go for hadronic boson-fermion maps as Higgs protection, not a theorem about SM antimatter; antimatter not load-bearing in C1. |
| 11 | R1 / BSM OK | Updated for the new observations (sec. 25). |
| Exp. | LHCb 2026 / CERN EP | Read. Ξ_cc⁺ and Ω_cc⁺ observed; no J = 3/2 state; P1 untested (sec. 25). |

### 27. CONSTRAINTS checklist (cycle 8, replaces sec. 23)

| ID | Status | How |
|---|---|---|
| A1 | Pass | Only quarks, antiquarks, gluons. Diquarks are qq correlations inside hadrons (lattice: hep-lat/0609004, arXiv:2106.09080), not fields. No superpartner in any mechanism; C1(c) uses HLS only to say an exact version would need new fields, which A1 excludes. Observed: Ξ_cc⁺⁺, Ξ_cc⁺, Ω_cc⁺ (sec. 25). Unobserved Ξ_cc*, Ω_cc*, Ξ_bb(*), T_bb are predictions only (R1). |
| A2 | Pass | No neutrino input. |
| A3 | Pass with caveat | pNRQCD/NRQCD/HQET are EFTs of QCD. LFHQCD and the DGG/AQM constituent models (c6, c8a) are models, labelled as such, used for illustration and controls. C1 does not depend on them: (a)-(c) are model-independent. |
| B1-B4 | Pass | All relations C-symmetric; no particle-antiparticle mass, q/m, moment or spectroscopy difference. |
| B5 | Pass | No gravitational claim. |
| B6 | Pass | No lepton g-factor effect. |
| B7, B10 | Pass | No CP- or T-odd operator. Hyperfine term P- and T-even. θ̄ not used. |
| B8, B9 | Pass | CKM not used. |
| C1 | Pass | m_h = 125.1 GeV not used numerically. C1(b) uses only that the Higgs is a colour-singlet, B = 0 doublet that couples to quarks through Yukawas. |
| C2 | Pass (N/A) | No EW/top input. |
| C3 | Pass | All partners are observed hadrons or QCD-predicted states below 11 GeV. Does not explain the absence of elementary superpartners. |
| C4 | Pass | No g-2 claim. |
| D | Pass | α_s(M_Z) = 0.1180 in c4. No beta-function or unification claim. |
| E2, E3 | Pass | Not used. |
| E4 | Pass | No vacuum-energy claim. |
| E6-E8 | Pass | No neutrino or N_eff content. |
| E9, E10 | Pass | No cosmology or baryogenesis claim. Q changes B by 1 only as a spectral map, not a process. |
| F1-F3 | Pass | No B-violating transition. |
| G | Pass | Hierarchy only as a negative statement. The MSSM contrast (δm_h² = O(m_soft²) after the Λ² cancellation) is the standard soft-breaking result, used qualitatively; no regulator-based number. |
| H1 | Pass | 3/4 from spin-colour algebra (c1, referee 2 (1)). c8a has one fitted coupling κ (on D*−D, stated) and gives the bottom splitting as output; m_q and p0 illustrative and stated. No numerology. |
| H2 | Pass | No loop integrals. |
| H3 | Pass | No interpretation-based mechanism. |
| H4 | Pass | c1-c8 with `.txt` outputs, rerun this cycle from `calc/`. |
(E1, E5: dark matter out of scope by directive D1.)
