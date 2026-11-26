# LW1 referee report 2 (cycle 7, independent)

Read: OVERSEER_PROMPT scope + gate, CONSTRAINTS.md, STATE R1, PROPOSAL.md, WORK.md, calc/. REVIEWS.md and LITCHECK.md not read.
Own script: `calc/referee2_check.py`, output `calc/referee2_check.txt`.

## Verdict: MAJOR ISSUES (fixable)

No fatal error, no BSM content. The heavy-quark relation P1 and the arithmetic are right. The headline quantitative part of C1 (the "102/33 MeV breaking, O(Λ²/m_Q)" numbers) measures the wrong thing, the model is not calibrated the way the text says, and the inference "[H,Q] ≠ 0 ⇒ cannot protect any mass" is invalid as stated (soft-broken MSSM is a counterexample). The #1 negative survives, but on compositeness, not on the commutator.

## Reproduction

All 12 scripts rerun from `calc/` (timeout 300 s each): exit 0, outputs identical to committed `.txt` apart from a UTF-8 BOM in the committed files.

## Findings

**1. [MAJOR] The "genuine breaking" ‖B‖ = 102 / 33 MeV is heavy-quark spin breaking, not superflavor breaking.** WORK sec. 19 Part B, CLAIM C1, STATE.
In c6 Part B, ‖B‖ is 100.4 MeV from the hyperfine term and 17.2 MeV from recoil (charm). The hyperfine term breaks heavy-quark *spin* symmetry (it is what splits D from D*), but its meson and baryon matrix elements are tied by superflavor: that tie is exactly the 3/4 rule (BVR spurion analysis), and the model builds it in with w = 1/2. So most of ‖B‖ is breaking whose pattern superflavor predicts, and it is the same breaking the line then uses for P1. Calling it "the genuine breaking" of Q and using it to argue Q protects nothing contradicts using Q to predict Ξ_cc* − Ξ_cc. What superflavor does not predict in this model is the ratio's deviation from 3/4: from the model's own spectrum (finding 2), 0.69 vs 0.75 at charm and 0.72 at bottom, i.e. ~8% and ~3% of the splitting, plus the recoil piece (17 / 6 MeV).
Fix: split B into a spin-covariant spurion part and a remainder. Quote the remainder (or the deviation of observable relations) as superflavor breaking, and quote ‖B_hf‖ as heavy-quark spin breaking.

**2. [MAJOR] The Part B model is not calibrated to D*−D as stated.** c6_hq_commutator.py Part B, WORK sec. 19 ("κ fixed by D*−D or B*−B").
κ is set assuming contact eigenvalue 1. In the actual colour-singlet, total-momentum-0 ground configuration the model gives (referee2_check (2b)): charm meson J=1 − J=0 = 57.9 MeV (target 142.0), baryon 3/2 − 1/2 = 40.0 MeV; bottom 16.3 MeV (target 45.3), baryon 11.8 MeV. The printed line "meson hyperfine input 142.0 → baryon 106.5 (3/4 rule)" is an analytic formula, not the model's spectrum. ‖B‖ is an operator norm dominated by the configuration with contact eigenvalue 1, so it is not a ground-state quantity either. (Colour-octet states do not inflate it: the singlet-restricted norm is the same, 101.6 / 32.5 MeV.)
Fix: either calibrate κ on the model's ground-state splitting, or state that ‖B‖ is a max over the model space with κ set by a contact-eigenvalue-1 convention, and drop "calibrated".

**3. [MAJOR] "m_Q‖B‖ = const ⇒ B = O(Λ²/m_Q)" is an input, not a result.** c6 scaling table, CLAIM C1 ("[established for the model]").
The scan sets D*−D ∝ m_c/m_Q, so the hyperfine coefficient ∝ 1/m_Q by construction; ‖B_hf‖ ∝ 1/m_Q follows trivially. Only the recoil piece p0²/m_Q is model output, and that is also trivial. The 1/m_Q scaling is correct (standard heavy-quark symmetry) but the script does not test it.
Fix: say the scaling is imposed from HQET and the script only shows the model is consistent with it.

**4. [MAJOR] "[H,Q] ≠ 0, so it cannot protect any mass" does not follow.** CLAIM C1 first sentence; sec. 19 reading 5 ("a symmetry that protects a mass must commute with H").
Approximate symmetries protect masses up to their breaking: chiral symmetry protects m_π² ∝ m_q; soft-broken MSSM SUSY has [H,Q] ≠ 0 and still removes Λ² sensitivity of m_h, leaving O(m_soft²). By the line's criterion the MSSM would not protect the Higgs either. Superflavor itself relates hadron mass splittings to O(breaking) (that is P1). Also "any scalar mass, ... hadronic" is too broad.
The #1 negative is still right for different reasons the line already lists: (a) the bosonic members are composite and do not exist as degrees of freedom above ~1 GeV, so there is no UV boson loop and the symmetry is absent (not softly broken) at the scales that matter for δm_h²; (b) the Higgs is a singlet under Q and couples to quarks, not to diquark fields; (c) HLS: an exact version would have to be Poincaré SUSY with new fields.
Fix: lead C1 with (a)-(c). Recast [H,Q] ≠ 0 as "Q is approximate, with breaking O(Λ/m_Q) in the heavy sector and O(1) in the light sector", and limit the claim to "cannot cancel UV-sensitive corrections the way SUSY does". Remove "Higgs or hadronic" / "any".

**5. [MINOR] {Q,Q†} without P or H.** Sec. 18. The computation is correct (Σ_σ{Q_σ,Q_σ†} = N_q̄ on the meson sector to machine precision; baryon side 2Π) and the line already demotes it to [argument]. Its content is that Q is a bilinear in normalized mode operators, so the result is fixed before any computation. Fine as written; do not cite it as evidence.

**6. [MINOR] Control C3.** AQM r = 0 is automatic for any additive mass formula (r is a double difference of quark-mass sums), so "AQM reproduces r_SF" is a definitional fact. The conclusion (small r_SF is not superflavor-specific) is right. Say "trivially zero" so it is not read as a fit result. The Ω_cc⁺ input is a real observation (LHCb, announced June 2026, arXiv:2609.21921), so R1 is not violated.

**7. [MINOR] Inputs.** I rederived 3/4 independently: P(S₁T₁ᵃ)P = (1/4) S_D T_Dᵃ on (3̄, spin 1), two quarks → 1/2; meson S·S split 1, baryon (1/2)S_D·S_q split 3/4. This matches BVR (a factor 1/2 from Savage-Wise). D*⁰−D⁰ = 142.01 → 106.5 MeV, D_s*−D_s 143.8 → 107.9: correct. c2 uses B* − B⁺ = 45.34 MeV. PDG quotes m_B* − m_B ≈ 45.2 (isospin-averaged B); 3/4 of that is 33.9 vs 34.0 MeV. Immaterial, but state which B is used.

**8. [MODERATE] P1 discrimination and link to the claim.** The kill band [43, 170] MeV ("2σ", naive) contains every model estimate I know of. Lattice already sits at −22%, and Ω_cc LO vs lattice is a 4.4σ(lat) pull (c2 output), so LO alone is already disfavoured without the band. More important for gate 7: no outcome of P1 or P2 can falsify C1 or C2. They test HQ symmetry in QCD. Gate 7 is formally met by a QCD prediction that is a restatement (BVR 2005).
Fix: say explicitly that P1/P2 test the QCD relation, not the SUSY claim.

**9. [MINOR] P2 transport.** I checked the error with other scalings of the charm correction to bottom (referee2_check (3)): 1/m_Q → 31.4, α_s(mv)-like → 28.9, α_s²-like → 30.5, unsuppressed → 26.4 MeV. 30 ± 4 covers all but the extreme case, which is marginal. Acceptable as labelled [conjecture].

**10. [MODERATE] Gate item 1: what SUSY result this bears on.** The negative is for one candidate mechanism, hadronic superflavor/LFHQCD SUSY, against SUSY #1. It is not "SM antimatter cannot reproduce #1". Antimatter is not load-bearing in the C1 argument: compositeness, Higgs-singlet and HLS make no use of the fermionic member being an antiquark, and the line itself notes Q ↔ Q̄Q̄ works equally well. "A world without antiquarks has none" is true because such a world has no mesons. C2 (#6) is acknowledged to have no evidential weight. The CLAIM "Status" line ("does not reproduce any SUSY result") is honest. Gate 1 needs one sentence: "no-go for hadronic boson-fermion maps as a Higgs-protection mechanism; not a general theorem about SM antimatter".

**11. [OK] R1 / BSM / numerology.** Ξ_cc*, Ξ_bb and T_bb appear only as predictions. The census excludes Ξ_cc* from the observed count. No superpartners appear in any mechanism. The cycle-4 numerology (δ ≈ m_d − m_u, "96% protection") is withdrawn. The P2 κ fit is one parameter on one lattice input and is labelled. No H1 violation remains.

## Required before promotion
Findings 1-4 (rewrite C1's quantitative bullet and its logic). Findings 8 and 10 are one-sentence scope fixes.
