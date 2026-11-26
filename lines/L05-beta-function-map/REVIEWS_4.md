# L05 Referee 4 (fresh, adversarial; confirming referee on the cycle-8 CLAIM)

Read before the verdict: OVERSEER_PROMPT.md, CONSTRAINTS.md, STATE.md (D4), PROPOSAL.md, WORK.md (CLAIM, §2, C4.5, C8, cycle-8 checklist), calc/. REVIEWS*.md and LITCHECK.md were read only after the verdict was formed, to check whether earlier findings were addressed.

## Verdict: MINOR ISSUES ONLY (on correctness). Gate recommendation: FAIL (item 7) as currently argued; items 1-6 PASS.

No fatal error and no BSM content in a mechanism. Every number I checked reproduces, and my own independent script confirms the theorem, the main counterexample and the SM Yukawa vertex term. The only gate problem is item 7: the cross-method check is a mathematical identity check whose outcome was fixed before it was run.

## Gate items

**1. Specific claim about a SUSY result.** PASS. D4 is answered precisely: the gauge-only coefficients (b_i, b_ij) are conjugation-blind, so no map judged by them can single out antimatter. The positive part is the exact two-loop homothety b_ij(Φ*(T)) = 2 b_ij(T) on i ≠ j and (1,1), with its scope stated. The negative for #2 (SM b's in every equivalent formulation, no unification) is standard and labelled as standard.

**2. SM-only content.** PASS. H^c as an independent field, Φ*, T_dbl, the 2HDMs, the MSSM and the toy parents appear only as comparison targets, and the cycle-8 checklist flags each as A1-forbidden in a mechanism. In C8, higgsinos are used only to say which SUSY completion exists.

**3. Runnable scripts.** PASS. From inside calc/, with timeouts: beta_map, c4_doubling, c4_threeloop (111 s), c6_scope, c8_scope, c8_yukawa and running all exit 0. Each output matches its committed .txt exactly. I did not run referee1/2_check.py, as instructed. Spot checks against the text: b = (41/10, −19/6, −7) and (33/5, 1, −3); diagonal ratios 30/7 and −7/13; 18/17 for SM + complex (8,3,0); the Yukawa tables and the g⁴ ratios 10972/3561, ..., 8/9; the Shapley shares; the criterion 25C(G) = 7S_F − 4S_c − 2S_r. All agree. I re-derived the criterion by hand from the general formulas: (b_ii[Φ*] − 2b_ii[T]) = (2C/3)(25C − 7S_F + 4S_c + 2S_r).

**4. CONSTRAINTS.** PASS. All items A1-H4 are addressed in writing, including E1 and E5, which are out of scope per D1. C1 now cites 125.20.

**5. Own adversarial check** (`calc/referee4_check.py`, output `calc/referee4_check.txt`). I wrote it from scratch from the Machacek-Vaughn and Jones/Martin-Vaughn general formulas and from the general Weyl/real-scalar one-loop Yukawa formula. It does not import the line's code.
- SM → MSSM: the ratios are exactly 2 on all six off-diagonal entries and on (1,1), with 30/7 and −7/13 on the diagonal. H_d = H^c and a duplicate Y = +1/2 doublet give identical b_i and b_ij.
- Counterexample: for SM + complex (8,3,0) with its minimal SUSY completion (one chiral), the ratio is 18/17 on (2,3) and (3,2). Φ* (two chirals) restores 2. Confirmed.
- Yukawa: from 4×4 Weyl matrices with 4 (SM) or 8 (2HDM-II) real scalars, 16π²β_yt/y_t splits into legs (3/2 y_t² + 1/2 y_b²), vertex and scalar trace. For the SM the vertex is −2y_b² and the trace is 3y_t² + 3y_b², which totals the standard 9/2 y_t² + 3/2 y_b². For the 2HDM-II the vertex is 0 and the total is 9/2 y_t² + 1/2 y_b². Confirmed.

Attacks on the narrowed claim:

- **F1 [MINOR] The three-loop part of (b) is asserted, not computed.** (b) says the compared three-loop gauge-only entries are unchanged under conjugating *any subset* of image fields. c8_scope §3 tests only b_i and b_ij. The line has no general-content three-loop formula, because C4.5 uses the published SM and MSSM tables. For a fixed theory those entries do depend only on S and C. But conjugating a subset of chiral fermions generally breaks anomaly cancellation, as the duplicate higgsino in C8.2 shows. At three loops, two-triangle self-energy topologies carry group factors equal to products of triangle traces such as Tr(Y T^aT^b), i.e. squared anomaly coefficients. These vanish in anomaly-free theories and need not vanish otherwise. My statement that such terms appear in the three-loop β is from memory and not verified. Fix: restrict the three-loop sentence of (b) to anomaly-free images (all named examples, H^c vs H′ scalar and T_dbl vs duplicate, are anomaly-free), or tag it as a conjecture. The b_i, b_ij statement is unaffected.
- **F2 [MINOR, wording, mainly for STATE.md] "The vertex term exists only because H^c ≡ H\*".** It is correct that the term exists only because one doublet appears in both Yukawas. A type-I 2HDM (both Yukawas on one doublet) has the same Yukawa matrices as the SM and therefore the same −2y_b². The conjugate enters only because a Y = +1/2 doublet must appear as H^c in the down Yukawa. So the term tracks "one field in both Yukawas", which is hypercharge bookkeeping, and calling it an "antimatter identity" does not add to that. WORK.md (b′3) words this correctly ("share that one field"). The overseer gloss in STATE.md ("antimatter identity") overstates it. No change to the line is needed beyond keeping that wording.
- **F3 [MINOR] Scheme class in the A3.4 argument.** Invariance of b_ij is shown only for redefinitions G_i = g_i + O(g_i³). A one-loop mixed redefinition g_i(1 + a g_j²) keeps β_i ∝ g_i, generates g_i g_j⁴ terms and changes the two-loop form. b_i, and so B and the one-loop negative, are fully invariant, and the two-loop non-unification is a physical statement from measured inputs. So nothing breaks, but "every equivalent formulation has the SM b_ij" should say "in schemes related to MS-bar by g_i-diagonal redefinitions".
- **F4 [MINOR] Citation hygiene.** The SM and MSSM two-loop g⁴ Yukawa entries and the MSSM two-loop Yukawa part are "as recalled, not re-read". The values I recall match: SM y_t (1187/600, −23/4, −108, −9/20, 19/15, 9) and MSSM y_t (2743/450, 15/2, −16/9, 1, 136/45, 8). They should still be read against a primary source before promotion.

**6. Novelty.** PASS, with LITCHECK's caveat. A quick web search found the standard SM and MSSM b_ij matrices printed side by side (e.g. arXiv:1104.2046, 1907.10238), from which the factor 2 can be read directly. None of them state the factor or its scope. No counter-evidence. The identity is elementary (two lines from per-field weights). Its novelty is "unprinted", not "deep".

**7. Is the cross-method check (MSS/BPV SM tables vs NSVZ-expanded SUSY) non-circular and falsifiable? No.**
- It is non-circular only in the narrow sense that neither side calls the general formulas from which the theorem is proved. But the MSS and BPV two-loop entries were themselves validated against Machacek-Vaughn, and the two-loop NSVZ expansion is algebraically identical to Jones' two-loop formula. So both sides equal the general-formula values by construction, and the result was known before the check was run.
- The only way it could fail is a transcription or arithmetic error. No measurement, and no correct calculation, can come out differently. That is a verification of the proof, not a "prediction or consistency check that could be tested or falsified" in the gate's sense.
- Options:
  - The overseer records gate 7 as waived or not met. The line says this honestly in CLAIM (c).
  - Adopt a data-dependent check that belongs to the negative result: with PDG inputs and SM b_i, b_ij (invariant across equivalent formulations), the two-loop couplings miss a common point (spread 3.20 in α⁻¹, running.py). Improved α_s or sin²θ_W measurements could in principle change this. That check is genuinely falsifiable, but standard.
  - Compute an outcome not known in advance, such as REVIEWS_3's C4.6 4(b) three-loop scalar weight. That would still be mathematical.

## Earlier findings (checked after the verdict)
REVIEWS_3 findings 1 (class of maps), 2 (A3.4), 5 (RG-commutation wording) and 6 (E1/E5, C1 label) are addressed in the cycle-8 CLAIM, §2.6 and the checklist. Finding 4 (weak gate 7) is acknowledged in CLAIM (c) but not resolved, and this report agrees with it. REVIEWS and REVIEWS_2 report no fatal error, consistent with this one.
