# L05 - Referee 2 (independent, adversarial)

Read: OVERSEER_PROMPT.md (Scope, Verification gate), CONSTRAINTS.md, PROPOSAL.md, WORK.md, calc/*.py and outputs. REVIEWS.md, REVIEWS_*.md and LITCHECK.md were not read before this verdict was formed.

Own script: `calc/referee2_check.py` (output `calc/referee2_check.txt`). It was written from the general formulas, not adapted from the line's scripts:
- non-SUSY, Machacek-Vaughn per-field: Weyl 2S_iC_j + δ_ij (10/3)C(G)S_i; complex scalar 4S_iC_j + δ_ij (2/3)C(G)S_i; real scalar half of that; gauge −(34/3)C(G)².
- SUSY, Martin-Vaughn: per chiral 4S_iC_j + 2δ_ij C(G)S_i; vector multiplet −6C(G)².

Published tables were fetched by this referee as arXiv TeX sources on 2026-11-25 and read directly: 1201.5868 eq. (5) (rows of β₁, β₂, β₃, two- and three-loop gauge parts), hep-ph/9311340 eq. (4.5), hep-ph/9605440 b_ij and the three-loop β_g. BPV 1210.6873 was not fetched.

## Verdict: MINOR ISSUES ONLY (one moderate scoping issue in CLAIM (b), and one moderate note on gate 7 for the overseer)

No fatal error and no BSM content in any mechanism. Every number in CLAIM (a)-(c) and C4.5 that I checked reproduces.

## What was checked and reproduces

1. **Theorem (CLAIM (a)).** The per-field weights follow directly from MV and MV-SUSY. The two-line proof is correct: Weyl 2 → chiral 4, real scalar 2 → chiral 4, complex scalar 4 → two chirals 8. For i ≠ j only these terms enter. For an abelian i = j every δ_ij term is ∝ C(G_i) = 0. Tested on 300 random theories with 2-4 factors (U(1) × subsets of SU(2), SU(3), SU(4); fundamentals, adjoints, SU(2) 3 and 4, SU(3) 6; complex scalars; real scalars in real reps). Ratio 2 everywhere. My diagonal criterion, including real scalars, is 25C(G) = 7ΣF S − 4ΣSc S − 2ΣSr S. The line's version omits the real-scalar term (see finding 6).
2. **SM → MSSM, all n_G.** My formulas give SM b_ij(n) = [[19n/15+9/50, 3n/5+9/10, 44n/15], [n/5+3/10, 49n/3−259/6, 4n], [11n/30, 3n/2, 76n/3−102]] and MSSM = FJJ exactly. The ratio is 2 on all i ≠ j and (1,1). The diagonal ratios are 30/7 and −7/13.
3. **Published tables (CLAIM (c)).** MSS eq. (5) two-loop entries ×16 match the line's `SM_MSS` entry for entry. MV eq. (4.5) prints B⁽²⁾ = [[199/25, 27/5, 88/5], [9/5, 25, 24], [11/5, 9, 14]] in the row = i convention, with dg_a/dt = g_a³/(16π²)² Σ_b B_ab g_b². This confirms the CLAIM's note on the arXiv print. FJJ b_ij matches `MSSM_FJJ`. Both pairings I could check (FJJ/MSS for all n, MV/MSS at n = 3) give 2.
4. **Counterexamples, all reproduced:**
   - 2HDM → MSSM: 3/2, 3/2, 199/104, colour entries 2;
   - no H_d: 5/3, 389/199;
   - H_d replaced by a second Y = +1/2 doublet: identical b_ij;
   - vector-like pair: 1;
   - (2,8) with one chiral: 8/7;
   - (3,8) with one chiral: 26/25;
   - T_dbl: diagonal 57, 50, and off-diagonal plus (1,1) equal to the MSSM.
5. **Three-loop entries (C4.5), from the fetched TeX:**
   - n_G-linear MSSM/SM ratios: c₁(23), c₂(13), c₃(12), c₁(12), c₁(13) give 8; c₂(21), c₂(23) give 8/13; c₃(31), c₃(32) give 2/7;
   - the n_G⁰ parts of c₁(12) are 783/800 and −27/25.
   All as stated.
6. **Scheme statements.** Under G_i = g_i + k_i g_i³ + a_i g_i⁵ + m_ij g_i³g_j², the two-loop b_ij are invariant, c_i(ij) and the fully mixed c_i(jk) are invariant, and c_i(jj) shifts by −2k_j b_ij + 2m_ij b_j. The symbolic check in my script gives:
- c₁(12), c₁(13), c₁(23) unchanged;
- c₁(22) → c₁(22) − 2k₂b₁₂ + 2m₁₂b₂;
- c₁(11) → c₁(11) + 2a₁b₁ − 2k₁b₁₁ − 3k₁²b₁.

These are identical to `c4_threeloop.py` §0. (Two printed ratios in the output appear as floats, 0.615… = 8/13 and 0.2857… = 2/7, because they are Python int/int. This is cosmetic.) So "no uniform three-loop factor in any scheme of this class" holds, because 8 ≠ 8/13 ≠ 2/7 on invariant entries.
7. **Gate items.**
   - Item 1: a specific negative claim on result #2 is made.
   - Item 2: no BSM content in any mechanism. MSSM, Φ*, T_dbl and the toys are labelled comparison targets, and H^c-as-independent is flagged as a second doublet.
   - Item 3: the scripts exist and assert. I re-ran only my own script.
   - Item 4: the CONSTRAINTS checklist is complete.
   - Item 6: LITCHECK not read by design.
   - Item 7: see finding 3.

## Findings

**1. [Moderate] CLAIM (b) is stated more broadly than it is proved.** Location: CLAIM (b), first sentence ("No structure-preserving map from SM beta functions to SUSY beta functions is specific to antimatter").

The argument shows only that every quantity in the gauge coefficients b_i, b_ij (and the three-loop entries used) depends on content through quadratic invariants S_i, C_j, which cannot tell R from R̄. Other structure does tell them apart, and §4 item 3 itself lists the Yukawa structure as something Φ preserves:
- The SM Yukawa y_b Q H^c d^c is gauge-invariant only with the conjugate; with a second Y = +1/2 doublet it is forbidden by hypercharge.
- Anomaly cancellation (Tr Y³, Tr Y T₂²) is odd under R → R̄.

So the Yukawa sector and anomalies, both inputs to the full beta function (Yukawa terms c_i), are exactly where H^c is singled out as the conjugate, not a duplicate. A map that preserves Yukawa couplings or anomaly freedom is antimatter-specific in the sense the line rejects.

Fix: restrict the statement. "No structure-preserving map at the level of the gauge-coupling coefficients b_i, b_ij (and the three-loop gauge-only entries) can distinguish a CP conjugate from a duplicate. The conjugate is selected by anomaly cancellation and Yukawa/holomorphy, which are not beta-function data at this order." The line says the second half already (bullet 2). The first sentence needs to match.

**2. [Minor] Indistinguishability of conjugate and duplicate is a loop-order statement.** Location: CLAIM (b) bullet 1, C4.3.

The two-loop b_ij and the three-loop gauge coefficients involve only quadratic invariants, so for complex reps (3 vs 3̄, Y vs −Y) conjugate and duplicate give identical numbers. I confirmed this for H_d vs a second H, and for (2,3) vs (2,3̄). Cubic invariants are odd under conjugation: d^{abc}_R̄ = −d^{abc}_R, and Y → −Y flips Σ Y S_j(R) and Σ Y³. In higher-loop gauge beta functions of chiral theories they can appear in products over different fermion loops. For anomaly-free content the single-trace combinations vanish, but mixed traces such as Σ_f Y_f C_j(f) C_k(f) d(f) are not anomaly coefficients. Nothing in the line rules them out at higher orders.

Fix: write "S_i, C_j are CPT-blind, and these are the only invariants entering b_i, b_ij (and the three-loop gauge-only terms)". Do not state it unconditionally.

**3. [Moderate, for the overseer] Gate 7 test is close to circular and wider than its hypothesis.** Location: CLAIM (c).

- (a) All four tables are outputs of the same general MV / MV-SUSY formulas from which the theorem is proved in two lines. The "check" therefore tests transcription of those tables and of the formulas, not an independent prediction. A failure would only reveal a typo. The line says honestly that the check is mathematical and has no experimental consequence. Whether that meets "could be tested or falsified" is the overseer's call, not an error in the line.
- (b) CLAIM (c) says "one-Higgs-doublet parent". The correct hypothesis is the one in the CLAIM (a) Corollary: the parent's only complex scalar is one doublet. Counterexample, asserted in `referee2_check.py`: SM + a complex scalar in the real rep (8,3,0). It still has one Higgs doublet, and its minimal SUSY completion is MSSM + one chiral (8,3,0), anomaly-free on its own. That gives 18/17 on (2,3) and (3,2), not 2.

Fix: in CLAIM (c), replace "one-Higgs-doublet parent" with "a parent whose only complex scalar is one |Y| = 1/2 doublet (and with no real scalars)". Equivalently, "a parent for which minimal SUSY = Φ*".

**4. [Minor] Several U(1) factors are not covered.** Location: CLAIM (a), C4.4 ("every abelian i = j").

With more than one U(1) there is kinetic mixing, and the beta function is a matrix in charge space. It is not of the S_iC_j form used in the proof. The factor 2 very likely persists, because every term is a per-field weight (2, 4, 2 vs 4) times a charge polynomial and no C(G) appears for abelian factors. But this is not shown.

Fix: state "at most one U(1) factor", or add the generalized-charge version.

**5. [Minor] DR-bar for a non-SUSY parent.** Location: CLAIM (a), "same in MS-bar and DR-bar".

For a non-SUSY theory, DRED introduces ε-scalars with evanescent couplings. MS-bar/DR-bar equivalence is a coupling redefinition only when those couplings are treated as independent (Jack, Jones, Roberts and later work). The comparison actually used is SM in MS-bar with the MSSM in DR-bar, which is unaffected.

Fix: add "(non-SUSY theory in DRED: with evanescent couplings treated as independent)", or drop the DR-bar claim for the parent.

**6. [Minor] Diagonal criterion omits real scalars.** Location: C4.2, "A non-abelian diagonal entry doubles iff 25 C(G) = 7 Σ_F S − 4 Σ_Sc S".

Under Φ* the general condition is 25C(G) = 7Σ_F S − 4Σ_Sc S − 2Σ_Sr S. This is irrelevant for the SM, but C4.2 presents the criterion in general form.

Fix: add the −2Σ_Sr S term.

**7. [Note] The theorem is not about antimatter.** CLAIM (a) is a statement about supersymmetrization of an arbitrary gauge theory, and contains no antimatter content. Its relevance to the research question is only through the negative reading in (b). That is already stated, and it is fine for a negative result, but the line's positive content is SUSY bookkeeping, not an antimatter mechanism. The line does not claim otherwise.

## Not checked

- BPV 1210.6873 (not fetched).
- running.py numbers.
- Furey material.
- LITCHECK novelty.
