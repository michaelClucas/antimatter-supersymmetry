# Referee F (fresh, adversarial) - L01b, cycle 9 CLAIM

**Verdict: MINOR.** No fatal error, no BSM content. All 14 line scripts run and reproduce their saved outputs byte for byte. My independent script (`calc/refF_check.py`, no imports from the line or `tools/`) reproduces C(M_t), its error, the C = 0 thresholds, the sector split, the 1-loop crossing, the H^c rank argument, the twin counterfactual, and the CW B. The findings below are about logic and wording, chiefly that the gate-7 falsifier (i) is inconsistent with CLAIM item 6.

Files read: OVERSEER_PROMPT.md (scope, gate), CONSTRAINTS.md, PROPOSAL.md, WORK.md, `calc/`. Prior REVIEWS were read only after this verdict was written (see the last section).

## Per-gate-item table

| gate item | status | note |
|---|---|---|
| 1. specific claim about a SUSY result | PASS | Negative result for #1 in its symmetry form, plus #4. Narrowed explicitly to "no symmetry enforces the cancellation"; accidental zeros are allowed (item 6). See F3. |
| 2. SM content only | PASS | Stops, superpotential, H_B/t_B, little Higgs, folded SUSY appear only as comparison targets or labelled counterfactuals. No reformulation used. Hole theory / F-S treated as re-expressions (H3). |
| 3. every quantitative step has a runnable calc reproducing numbers | PASS, with F5 | 14/14 scripts run in 0-3 s from inside `calc/`, outputs identical to committed. Numbers I spot-checked in WORK match the outputs. §7 numbers (78.6 GeV, 9.8 GeV, Weisskopf 3α/2π) live in L01's `calc/`, outside this folder. |
| 4. every CONSTRAINTS item addressed | PASS | §10 covers A1-A3, B1-B10, C1-C4, D, E1-E10, F1-F3, G, H1-H4. E1/E5 "not applicable" is justified (D1 removed #3). |
| 5. three referees find no fatal error / BSM | this report: none found | - |
| 6. literature novelty | not assessed here | WORK says novelty items 1-2 are "pending LITCHECK". |
| 7. falsifiable check (retrodiction accepted) | PASS on numbers; wording flaw F1 | C(M_t) computed correctly in both forms; error propagation correct. Falsifier (i) as written is logically inconsistent with item 6. |

## Independent recomputation (`calc/refF_check.py` → `calc/refF_check_out.txt`)

| quantity | line | referee F |
|---|---|---|
| C_pole(M_t) | −4.068 ± 0.020 (205σ); ± 0.040 with MC (103σ) | −4.0683 ± 0.0199 (205σ); ± 0.0395 (103σ) |
| C_MSbar(M_t), Buttazzo fits | −3.426 ± 0.020 (172σ); ± 0.050 wide (69σ) | −3.4259 ± 0.0199 (172σ); ± 0.0496 (69σ), fit formulas typed in independently |
| m_t for C_pole = 0 | 96.06 GeV | 96.06 GeV |
| y_t(M_t) for C = 0 | 0.5470, κ_t = 0.586 | 0.5470, 0.586 |
| C with Jegerlehner y_t 0.9005 | −3.070 | −3.070 |
| sectors W / Z+h / F, R | 0.882 / 0.916 / 5.223, 0.344 | 0.882 / 0.916 / 5.223, 0.344 |
| 3λ/6y_t², 6λ/6y_t² | 7.2%, 14.5% | 7.2%, 14.5% |
| 1-loop crossing μ₀ | 10^26.79 | 10^26.78 (own 1-loop RGE, y_b, y_τ dropped); max C on [M_t, M_Pl] = −0.405 < 0 |
| Jegerlehner y_t, 1-loop | (3-loop: 10^16.15) | 10^20.14 at 1 loop, slope +0.020 (consistent with the line's point that loop order matters) |
| Jacobian rank of (H^c, H) wrt H; \|H^c\|² − \|H\|²; H^c†H | 4; 0; 0 | 4; 0; 0 |
| H_B := H^c Hessian | {0,0,0,−4κ} (canonical h) | {0,0,0,−8κ} in φ = Re/Im H normalization = −4κ in h = √2φ. Three zeros, one radial ∝ κ: confirmed |
| CW B | −4.39×10⁻³ | −4.387×10⁻³ |
| QCD EWSB M_W; v/f_π; f_π²/v² | 30 / 52 MeV; 2673; 1.4×10⁻⁷ | 30.0 / 52.0 MeV; 2673; 1.40×10⁻⁷ |

Pole-form algebra checked by hand: 6λ = 3m_h²/v², 9/4 g² + 3/4 g'² = 3(2M_W² + M_Z²)/v², 6y_t² = 12m_t²/v². Swap check: Φ = (H^c, H), Φ(iσ₂)† = (H, −H^c), det = 1. Correct.

## Findings

**F1 (gate 7 logic, MINOR-to-MAJOR; fix is wording).** The CLAIM's falsifier (i), "a determination ... that put C(M_t) at zero within errors" would falsify the claim, contradicts item 6, which says the no-go allows an accidental zero at one scale. A zero at M_t is no less accidental than a zero at μ₀. So (i) cannot falsify the claim. What the measured C(M_t) ≠ 0 does is refute the negation ("an exact SM symmetry enforces C = 0") by modus tollens, and it does that without using items 1-5 at all. The 69σ-205σ figures measure how far the SM is from a fact that has been known since Veltman 1981. They do not test the enumeration. Only (ii) is a genuine falsifier of the claim as stated, and (ii) is weak: with Buttazzo matching the crossing is at 10^22.8 GeV, above M_Pl and scheme dependent. Fix: call (i) evidential ("C ≈ 0 at M_t would be strong evidence for an enforcing relation and would demand an explanation"), keep (ii) as the logical falsifier, and say plainly that the check tests the conclusion, not the argument. The numbers are right either way.

**F2 (antimatter content of the two departures is thin, MINOR, bears on gate 6).** Both departures follow from A1 plus CM/HLS, with no antimatter-specific input. "Every antimatter operation maps the SM field space onto itself without enlarging it" holds for every operation defined on SM fields, antimatter or not. The twin obstruction is "the SM has no second copy", which is A1. The H^c rank-4 computation is correct but only shows that H^c is not a second copy, which a one-line remark would also show. This is not an error, and the line admits the antimatter content is "the set of operations tested". But "What is new" item 2 should be weighed with this in mind.

**F3 (scope of the negative result, MINOR).** SUSY result #1 is the cancellation. The CLAIM narrows it to "in its symmetry form". With Jegerlehner's matching, C(μ) crosses zero at 10^16.15 GeV, below M_Pl, so a Veltman-condition zero inside the SM's range is not excluded. Jegerlehner argues this is how the SM handles the issue. The CLAIM mentions the crossing only parenthetically in item 6. One sentence in the Statement should say that a non-symmetric zero of C below M_Pl (Jegerlehner matching) is outside the claim, not refuted by it.

**F4 (tag inflation in item 2, MINOR).** `c9_symmetry_group.py` part (1) checks numerically that |H|², |H|⁴, (Q†H^c)t_R and (Q†H)b_R are invariant under random SU(2)_L and U(1)_Y elements. They are gauge invariant by construction, so the check cannot fail and carries no evidential weight. The load-bearing content of item 2 is the argument (a symmetry enforces a relation only by mapping one operator to a different one, or by forbidding one) plus the completeness of the enumerated group. Retag item 2 as [established + argument; numerical sanity check], not [computed].

**F5 (H4 locality, MINOR).** §7 numbers for #4 (top threshold 78.6 GeV, W/Z-only m_h = 9.8 GeV, B = −4.3×10⁻³ with m_h, the Weisskopf 3α/2π, the 8-digit time-ordering agreement) come from `lines/L01-weisskopf-hierarchy/calc/`, which exists and holds those scripts but sits outside this line's `calc/`. CONSTRAINTS H4 says "`lines/<id>/calc/`". B itself is recomputed here in `c9_symmetry_group.py` (−4.39×10⁻³), which covers the load-bearing #4 number. Either copy the L01 scripts in when promoting, or have the overseer rule that merge-by-reference meets H4.

**F6 (regulator dependence of the relation being tested, MINOR, no effect on conclusion).** The relation "C = 0" is regulator dependent: with d − 1 vector counting the gauge weights change (R(M_t) = 0.211). The no-go's diagonal-action argument covers any polynomial relation among (λ, g, g', y_t), so the claim is regulator independent, but G7 quotes only the cutoff/PV C. In the d = 2-pole counting, C(M_t) ≈ 5.223 × (0.211 − 1) ≈ −4.12, also far from zero. Add one line to G7.

**Checked and found sound:**
- Item 1. C, P, CP unitary and T, CPT antiunitary all commute with J². (−1)^F is preserved. The Weyl caveat is stated.
- Item 2's logic, given the enumerated group: every element acts diagonally on coupling space, so C is an invariant and nothing forces it to zero. The completeness caveat ("strong argument") is honest.
- Item 3 counterexamples. Gauge invariance leaves λ and y_t free (separately invariant operators). The pNGB route needs a larger coset. GW needs B > 0, and B < 0 here.
- Item 4 is scoped correctly (algebra classification only; goldstino needed; de Wit-Freedman cited from memory and flagged).
- Item 5 (a)-(d) verified independently. Note 5(b): in the counterfactual, m_h² = −4κ holds at the minimum with the quartic included. The quartic is implicit in "λ(…)²". Correct.
- Item 6. Crossing transverse; slope ±0.0002 from inputs (93σ) reproduced in the line output. My 1-loop crossing agrees with the line's 1-loop value.
- Item 7. Numbers reproduced. "Three massless doublets with f_π fixed" is correctly marked [approx].
- No BSM content smuggled into any mechanism. The H_B counterfactual is labelled and not used.

## Process note
The line's scripts write their `_out.txt` files on every run. Running them overwrote the committed outputs with identical content (verified by diff before and after), so nothing changed.

## Earlier reviews (read after writing the above)
I read REVIEWS_E.md and skimmed the findings in REVIEWS_C.md.
- E1 (twin/little Higgs omitted), E2 (custodial limit, iσ₂), E3 (h self-loop), E4 ((b) wording): **fixed**. §4d, the route table, D2 (a)/(b), and symmetry_scan/c9_twin outputs all match, and I verified the numbers independently.
- C1 (S2 lemma too general), C2, C3 (CM/HLS scope), C4 (reduction of couplings), C7 ("strong argument"): **fixed** in the text. The C1 replacement (item 2 enumeration) is sound as an argument, but its numerical check is tautological (my F4).
- **E5 / C8 (gate 7): only partly fixed.** E5 rejected F-b because "step 4 explicitly allows an accidental single-scale zero, so either outcome is consistent with the no-go". The replacement G7 (i), C(M_t) ≠ 0, has the same defect: an accidental zero at M_t is equally consistent with the no-go. The fix used E5's option (iii) plus a well-computed retrodiction, but the falsifier wording reintroduced the problem E5 named (my F1). Given the experimenter's ruling that a retrodiction is acceptable for item 7, this is a wording fix, not a reason to block.
