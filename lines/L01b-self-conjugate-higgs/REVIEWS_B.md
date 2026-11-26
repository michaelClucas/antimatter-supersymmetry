# L01b - Referee B (adversarial, physics framing), cycle 5

Read: OVERSEER_PROMPT Scope, CONSTRAINTS.md, PROPOSAL.md, WORK.md (all), calc/ outputs (grep-level for symmetry_scan, c4_rxi_split, pair_matching). Did not read REVIEWS.md or LITCHECK.md. Arithmetic not redone; one check script added: `calc/refB_check.py` -> `calc/refB_check_out.txt`.

## Verdict: MAJOR ISSUES (fixable)

No fatal error. The arithmetic and the gauge-invariance work look sound, and the line is honest that the antimatter vocabulary is a re-expression. The problems are in what the negative result is a negative result *about*: the no-go is stated against a regulator-dependent target, it omits the one in-SM candidate protection mechanism (classical scale invariance, which the line itself invokes for #4), and the headline "fails at (c) alone" is broader than what was shown.

## Findings

### 1. [MAJOR] No-go is incomplete: classical scale invariance (Bardeen) is an in-SM candidate and is not addressed
- **Location:** CLAIM 4-5; Section 4; Section 6 "Fails: No symmetry".
- **Problem:** The symmetry scan covers only linear internal symmetries (C, P, CP, Z2s, U(1)s, custodial). The standard in-SM candidate for protecting m_h² is classical scale invariance at μ² = 0 (Bardeen, FERMILAB-CONF-95-391-T, 1995; also Meissner-Nicolai 2007, Aoki-Iso 2012). It is broken only by the trace anomaly, which in a mass-independent scheme makes m² multiplicatively renormalized: β(m²) ∝ m². The line states exactly this in Section 7 ("In MS-bar β(m²) ∝ m² at all orders") to dispose of SUSY #4, but never confronts it as a candidate for SUSY #1. In d = 4 dim reg with no heavy SM thresholds, this is the SM's version of "m_h² is protected": corrections are ∝ m_h² ln, which is the same form as SUSY's soft-mass logs (Section 1a). So under the regulator CONSTRAINTS G treats as physical, the SM and SUSY look alike for result #1 within SM field content, and the difference only reappears once heavy states (BSM, or gravity at M_Pl) are added.
- **Fix:** Add a section on scale invariance. Either (i) argue it does not count as "reproducing SUSY #1" because SUSY's statement is protection against heavy thresholds that couple to H, and the SM provides none to test, so the SUSY #1 question has no SM-internal observable; or (ii) concede that within the SM spectrum, m_h² is multiplicatively renormalized in DR, and that this holds without any antimatter input. Both make the line's negative result conditional on a statement about UV physics the scope forbids. Say so in CLAIM.

### 2. [MAJOR] The quantitative result R has no physical observable; "regulator independent" overstates H2
- **Location:** CLAIM 1, 3; closing "What survives is a gauge-invariant, quantitative statement of how far the SM boson sectors fall short"; Section 6; Appendix C4.2.
- **Problem:** The three regulators cited (hard cutoff, Pauli-Villars, the d = 2 pole of DR) are the three that by construction keep power divergences. They agree on the Λ² coefficient because that coefficient is fixed by STr M²(φ) in any regulator that sees it. Agreement among them is not H2 regulator independence of a physical claim; d = 4 MS-bar returns nothing. Worse, C does not measure sensitivity to physical heavy thresholds either: a real heavy state S with portal κ|H|²|S|² shifts m_h² by ~κ M_S²/16π², independent of C. Only a UV completion that regulates SM loops PV-style (heavy partners of every SM field with SM couplings) gives δm² ∝ C M². That is a BSM assumption. So "the bosons cancel about a third of the top" is a statement about a regulator artefact. Section 6 "Not claimed" admits there is no d = 4 DR observable, but the CLAIM headline and item 1 present R as physical.
- **Fix:** In CLAIM 1, replace "regulator independent" with "the same in every regulator that retains a Λ² term; absent in d = 4 DR; no SM observable". Recast R as the ratio of one-loop supertrace coefficients, a property of the Lagrangian with no measurement attached. Drop "quantitative statement of how far the SM boson sectors fall short" or qualify it the same way.

### 3. [MAJOR] "Fails at (c) alone" is broader than what was shown; scalars can be protected, including inside the SM
- **Location:** CLAIM 5; Section 4 "Why there is no protection".
- **Problem:** What Section 4 proves is that a spin-0 mass bilinear is invariant under every *linear* internal symmetry. That is correct ('t Hooft) and is the right reason self-conjugacy is irrelevant. But the CLAIM reads it as "the analogue fails because bosons carry no chirality", and that does not follow. Scalars can be protected by:
  - a nonlinearly realized shift symmetry. The SM itself has this: the Goldstones G±, G⁰ are exactly massless scalars (physical mass zero, gauge-parameter mass only), protected by the spontaneously broken SU(2)×U(1). That is an in-SM counterexample to "bosons have no protection". h is the radial mode and is not protected, and the line should say exactly that;
  - gauge symmetry in higher dimensions (gauge-Higgs unification, H = A_5). BSM, so out of scope, but should be named as excluded;
  - SUSY itself, which does not protect the scalar by chirality. It ties m_φ to m_ψ, and m_ψ is protected by chiral/R symmetry. The scalar-side cancellation is the holomorphy of the superpotential plus non-renormalization (the line uses this correctly in 1a, but CLAIM 5 does not reflect it);
  - scale invariance (Finding 1).
  The SM also has protected vector bosons (photon, gluon massless; W, Z masses ∝ g v, multiplicative), so "bosons carry no chirality" cannot be the operative obstruction as stated.
- **Fix:** Restate CLAIM 5 as: "(a) and (b) are irrelevant. The precise obstruction is that h is neither a Goldstone of any SM symmetry nor tied by any SM symmetry to a chirally protected fermion mass; the spin-0 bilinear h² is invariant under all linear internal symmetries ((c))." Then add a short table of the four known scalar-protection mechanisms, each with its SM status (shift: h not a pNGB without new fields; SUSY: no partners, C3; extra-dim gauge: BSM; scale: Finding 1).

### 4. [MAJOR] Not yet a rigorous no-go; a short rigorous version is available
- **Location:** CLAIM 4; Section 4 scan; Section 6.
- **Problem:** "C is invariant under every candidate symmetry" is a finite scan of hand-picked symmetries. That is evidence, not proof that SM antimatter cannot reproduce SUSY #1. The RG test only shows that C = 0 is not RG invariant for a regulator-dependent C.
- **Fix:** A rigorous version is short. (i) The SM has one scalar multiplet H. Any internal symmetry that commutes with the gauge group and acts linearly acts on H by a unitary matrix, and H†H is invariant. QED for linear internal symmetries. Particle-antiparticle maps (C, CP, CPT) map H†H to itself. (ii) Spacetime extensions: by Coleman-Mandula and Haag-Łopuszański-Sohnius the only options are SUSY (requires partners, excluded by A1/C3) and conformal symmetry (Finding 1). (iii) Nonlinear realization: h would need to be a Goldstone of a larger spontaneously broken group, which needs new fields (composite or pNGB Higgs, BSM). (iv) State that the target is "protection against heavy thresholds", which cannot be posed within the SM spectrum (Finding 1/2). That chain counts as a "strong argument"; the current scan does not.

### 5. [MINOR] The "exact Z2" that "protects the fermion mass" is a gauge transformation times (−1)^F
- **Location:** Section 4, bullet "h → −h with t_R → −t_R is an exact SM symmetry"; CLAIM 5 "(b) protects fermion masses".
- **Problem:** `calc/refB_check_out.txt`: the Z2 acts on every field exactly as the SU(2)_L centre times (−1)^F. The first is a gauge transformation, the second a 2π rotation. It has no physical content beyond gauge invariance and Lorentz invariance, and "it forbids a bare Dirac mass" just restates that Q̄_L t_R is not gauge invariant. What protects fermion masses is the chiral symmetry acting on t_R alone (broken only by y_t). Observation (b), L↔R symmetry of y h ψ̄ψ, follows from hermiticity of a real Yukawa and is not a symmetry.
- **Fix:** Replace with: "m_t is protected by the chiral U(1) of t_R, broken only by y_t; (b) is hermiticity and protects nothing." Drop the Z2 or label it trivial.

### 6. [MINOR-MODERATE] SUSY #4 coverage omits the in-SM dynamical EWSB by the QCD condensate
- **Location:** CLAIM 6; Section 7 cw_radiative_ewsb.
- **Problem:** "The SM has no radiative EWSB" is correct for Coleman-Weinberg and for RG sign flips in a mass-independent scheme. But at μ² ≥ 0 the SM vacuum still breaks SU(2)×U(1) through the QCD quark condensate (⟨q̄q⟩ ≠ 0 carries weak isospin; e.g. Quigg & Shrock, PRD 79, 096002 (2009)), with v of order f_π, about 100 MeV, and a top-condensate-induced tadpole for H. This is an SM-internal, non-perturbative, partly antimatter (q q̄ pair condensate) mechanism, closer to the line's theme than anything in Sections 1-4. It fails quantitatively (v ~ 0.1 GeV vs 246 GeV) but must be addressed. Also, the #4 discussion uses no antimatter structure at all. Say that, so it is not read as part of the antimatter analysis.
- **Fix:** Add a paragraph: QCD-condensate EWSB exists in the SM, gives v ~ f_π, and does not reproduce #4. Cite Quigg-Shrock. Note that the "sign of m² is RG invariant" statement holds in a mass-independent scheme with no heavy thresholds.

### 7. [MODERATE] Antimatter framing is not load-bearing; the line is the Veltman condition plus a standard naturalness no-go (H3)
- **Location:** throughout; "What is new" 1.
- **Problem:** The line concedes this (Section 1), and it is acceptable for a negative result. But "What is new" item 1, "the framing... is not in print; its precise failure point is new as a statement", claims novelty for a framing that turns out to be irrelevant at every step. (a) is irrelevant, (b) is hermiticity, and (c) is 't Hooft naturalness. Items 2-3 are about Jegerlehner's matching and ξ-independence, which have nothing to do with antimatter.
- **Fix:** State plainly in CLAIM: "No step uses antimatter structure. Hole-theory and time-ordered forms reproduce covariant results and add nothing (H3). The answer to D2 is that observations (a)-(c) are each either irrelevant or a restatement of standard naturalness." Demote novelty item 1.

### 8. [MODERATE] The 4.1σ headline for F-b mixes a scheme-dependent target with a selectively chosen error budget
- **Location:** CLAIM F-b; Section 5b.
- **Problem:** C(M_Pl) is a regulator-dependent quantity (Finding 2). M_Pl as a cutoff is a gravitational (non-SM) input. The budget excludes the y_t-matching spread (~6.8 GeV equivalent), which the line itself identifies as the dominant ambiguity and which removes the tension. Quoting 4.1σ with that excluded is misleading, even with the caveat.
- **Fix:** Headline as "4.1σ under Buttazzo matching; not excluded under Jegerlehner matching; the dominant uncertainty is the on-shell → MS-bar y_t conversion". Mark F-b as a statement about a cutoff-scheme coefficient at a non-SM scale.

### 9. [MINOR] CLAIM 2 "self-conjugacy makes no difference" is argued by numerical near-equality of two sectors
- **Location:** CLAIM 2.
- **Problem:** "The charged W± sector and the self-conjugate Z + h sector do so equally". At M_t these are 0.882 vs 0.916. That is a numerical coincidence of different coupling combinations (H1) and is not the argument. The real argument is basis independence of the trace (L01 §4.4), which the line has.
- **Fix:** Rest CLAIM 2 on basis independence (W± = rotated real W1, W2), and drop "equally".

### 10. [NOTE] Scope / BSM
- No BSM content in any mechanism. SUSY appears only as a comparison target (A1 ok). M_Pl and μ₀ > M_Pl are used as reference scales; Section 6 "Not claimed" correctly declines a physical reading of μ₀. A2 is handled. H1 flags are present for the μ₀ sector equality and R4.

## What a passing version needs
1. CLAIM recast: target = "a symmetry or structure in SM antimatter that makes m_h² insensitive to heavy thresholds".
2. The rigorous four-step no-go of Finding 4, including scale invariance (Finding 1) and nonlinear realization (Finding 3).
3. R and C(M_Pl) labelled as cutoff-scheme coefficients with no SM observable (Findings 2, 8).
4. QCD-condensate EWSB addressed for #4 (Finding 6).
5. Antimatter framing declared non-load-bearing in CLAIM (Finding 7).
