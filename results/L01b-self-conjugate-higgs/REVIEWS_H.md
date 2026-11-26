# Referee H (numbers and reproducibility), cycle 9 fix round 4

**Verdict: MAJOR** (one gate-7 logic problem; every number reproduces; no FATAL error; no BSM content found)

Read: OVERSEER_PROMPT.md (scope, honesty, gate), CONSTRAINTS.md, PROPOSAL.md, WORK.md, calc/. Other REVIEWS files and LITCHECK files not read. Independent check: `calc/refH_check.py` -> `calc/refH_check_out.txt` (no imports from the line's scripts; uses `tools/rg_sm.run()` only for 2/3-loop running, with initial conditions typed in independently; own 1-loop RGEs).

## 1. Script reruns (from inside calc/, 300 s timeout)

All 14 line scripts and refA-refD run with exit 0 in 0-3 s each. Every output is byte-identical to the committed version (checked with `git status`/`git diff HEAD` after the rerun: no calc/ file modified).

| script | rc | output vs HEAD |
|---|---|---|
| pair_matching, symmetry_scan, matching_running | 0 | identical |
| c4_rxi_split, c4_regulator_running | 0 | identical |
| c5_jegerlehner, c5_mt_budget | 0 | identical |
| c7_same_spin, c7_regulators, c7_qcd_ewsb, c7_mt_significance | 0 | identical |
| c9_symmetry_group, c9_twin_antimatter, c9_C_measured | 0 | identical |
| refA-refD | 0 | identical |

Reproducibility nits:
- R1. 15 of the scripts open and overwrite their own committed `*_out.txt`. A rerun therefore cannot be compared to "the committed .txt" on disk, only to git HEAD. Harmless in a git repo, but the WORK.md phrase "reproduced byte for byte" needs git to be checkable. Suggest writing to stdout or a temp path, or saying so.
- R2. `matching_running_out.txt` still prints the withdrawn experimental-error-only significances ("-10.5 sigma", "-12.5 sigma", "-19.8 sigma"). WORK.md §5b says "10.5σ stays withdrawn", but the committed output still contains it with no flag. Add a "(withdrawn, see c5_mt_budget)" label in the script.

## 2. Independent recomputation (refH_check_out.txt)

| quantity | line (WORK.md) | refH | status |
|---|---|---|---|
| Veltman bracket, PDG 2024 | ~ -8.2e4 GeV² (CONSTRAINTS G) | -82213 | ok |
| C_pole(M_t) | -4.068 ± 0.020 (205σ); ± 0.040 with MC (103σ) | -4.0683; 0.0199 (205σ); 0.0395 (103σ) | ok |
| C_pole = 0 at m_t | 96.1 GeV | 96.06 | ok |
| MS-bar couplings at M_t (Buttazzo fits) | y_t 0.93286, λ 0.12617 | 0.93286, 0.12617, g 0.64764, g' 0.35843 | ok |
| C_MS(M_t) | -3.426 ± 0.020 (172σ); ± 0.050 (69σ) | -3.4259; 0.0199 (172σ); 0.0496 (69.1σ) | ok arithmetically, see F2 |
| C_MS with Jegerlehner y_t 0.9005 | -3.070 | -3.0700 | ok |
| R(M_t) | 0.344 | 0.3441 | ok |
| own crude matching (QCD-only 3-loop pole->MS-bar y_t, tree λ, 1-loop g, g' from CONSTRAINTS D) | (n/a) | C = -3.398, R = 0.349 | consistent with Buttazzo-based -3.426 |
| y_t* for C(M_t)=0 | 0.547, κ_t 0.59 | 0.5470 (hand), 0.586 | ok |
| zero of C, 1-loop | 10^26.79 | own RGEs: 10^26.78 | ok |
| zero of C, 2-loop | 10^22.98 | 10^22.984, slope +0.0204 | ok |
| zero of C, 3-loop | 10^22.83, slope +0.0203 | 10^22.833, slope +0.0203 | ok |
| zero, M_t ± 0.29 | ±0.35 decades | 22.483 / 23.178 | ok |
| max C on [M_t, M_Pl] | -0.183 | -0.182 (finer grid; C(M_Pl) = -0.1819) | ok |
| zero with y_t(M_t) = 0.9005 | 10^16.15, slope +0.024 | 10^16.151, +0.0240 | ok |
| zero from crude own matching | (n/a) | 10^22.09 | crossing scale depends on the matching, as the line says |
| M_t* budget quadrature | 0.74 GeV, 4.1σ | 0.7465, 3.035/0.7465 = 4.07 | ok |
| h self-loop share | 3λ = 0.378, 7.2%; 6λ 14.5% | 0.3785/5.2214 = 7.25%; 14.5% | ok |
| custodial-limit C | -8.742 (script) | 1.701 - 10.443 = -8.742 | ok |
| GW B | -4.39e-3 | -4.387e-3 (hand) | ok |
| QCD EWSB | 30 MeV, 52 MeV, v/f_π ≈ 2700, share 1.4e-7 | script uses f_π = 92.1 MeV: 30.1, 52.1, 2674, 1.40e-7 | ok (2674 rounds to 2700; √3 case 1544, text "1540") |

**1-loop betas in tools/rg_sm.py checked by hand** (convention d(g²)/d ln μ², g1 GUT-normalized): b = (41/10, -19/6, -7) ok; λ: 12λ² + 6λY_t - 3Y_t² - λ(9/2 g2² + 9/10 G1) + 9/16 G2² + 9/40 G2 G1 + 27/400 G1² ok (= 1/2 of the standard 16π² dλ/d ln μ with g'² = 3/5 G1); y_t²: 9/2 Y_t + 3/2 Y_b + Y_τ - 8G3 - 9/4 G2 - 17/20 G1 ok; y_b², y_τ² ok; m²: 6λ + 3Y_t - 9/4 G2 - 9/20 G1 ok. Independent 1-loop integration reproduces 10^26.78. 2- and 3-loop coefficients not checked term by term (taken from the transcription; the script's own validation vs Buttazzo eq. (61) was not rerun by me).

**C normalization:** (3/v²)(m_h² + 2M_W² + M_Z² - 4m_t²) = 6λ + 9/4 g² + 3/4 g'² - 6y_t² checked by hand (2M_W² + M_Z² term gives 6/4 g² + 3/4 g² + 3/4 g'²). Consistent with CONSTRAINTS G.

## 3. Findings

**F1 (MAJOR, gate 7 logic).** G7 part (i) is not a falsifier of the claim. The CLAIM (item 6, F-b) says explicitly that the no-go allows an accidental zero of C at one scale ("The no-go allows an accidental zero, so F-b cannot test it either way"). By the same logic a measurement giving C(M_t) = 0 within errors would be an accidental zero at M_t and would not contradict "no symmetry enforces C = 0". Yet the "What would falsify the claim" bullet lists C(M_t) = 0 as a falsifier. The two statements contradict each other. Only G7 (ii), an RG-invariant zero (C = 0 with dC/d ln μ = 0 over a range), bears on the no-go, and (ii) is satisfied by any generic trajectory: a transverse crossing is what one expects with or without the claim. So the 69σ / 103σ numbers, while correct, test nothing the no-go predicts. Gate 7 is at best met as a weak consistency check; the overseer must rule, and the CLAIM should drop (i) as a falsifier or explain why a zero at M_t specifically would signal a symmetry.

**F2 (MINOR, uncertainty propagation).** The arithmetic of 69σ and 103σ is right (rows add in quadrature; the dominant MS-bar rows are MC 0.031 and y_t spread 0.034). But:
- the 0.003 y_t spread used for "≥ 69σ" is the one §5b calls "not justified independently" and widens for F-b. With the line's own Buttazzo-Jegerlehner spread 0.038 the MS-bar significance is 8.0σ (σ = 0.427), not 69σ. The headline "at least 69σ" in the CLAIM statement and in §6 should be replaced by the matching-spread-robust statement, e.g. "C(M_t) lies between -3.07 and -4.07 in every determination; ≥ 8σ from zero even at the Buttazzo-Jegerlehner spread", or "C_pole = 0 needs m_t = 96 GeV".
- the quoted σ's do not contain the scheme difference between the two determinations themselves: pole minus MS-bar = -0.642, i.e. 13-16 of the quoted σ. C(M_t) is a convention-dependent number; the σ's measure input errors at fixed convention only. Say so next to the table.
- "slope/σ ≈ 90" (item 6, G7 ii) uses PDG input errors only; the y_t-matching alternative moves the slope from 0.0203 to 0.0240 (≈ 18 of those σ). Sign is robust; the "90" is not meaningful.

**F3 (MINOR, reproducibility).** R1 and R2 above.

**F4 (nit).** max C on [M_t, M_Pl] = -0.183 is a 0.01-decade grid that stops just below M_Pl; finer grid gives -0.182 = C(M_Pl). Cosmetic.

No FATAL error. No BSM content entered any computation I reran: SUSY/twin objects are comparison targets or counterfactuals, labelled as such.

## 4. Per-gate-item table

| gate item | status | note |
|---|---|---|
| 1. specific claim about a SUSY result | met | negative result for #1 (and #4), stated as a strong argument, not a proof |
| 2. SM content only | met | twin H_B and stops appear only as labelled counterfactual/comparison (c9_twin_antimatter, pair_matching Part 4) |
| 3. every quantitative step has runnable, reproducing calc | met | all 14 scripts rerun, byte-identical to HEAD; all CLAIM/§5/§10 numbers checked (table §2). Nits R1, R2 |
| 4. every CONSTRAINTS item addressed | met | §10 covers A1-A3, B1-B10, C1-C4, D, E1-E10 (N/A with reason: no cosmology/DM claim), F1-F3, G, H1-H4. C3 addressed trivially (no superpartners used), acceptable for a negative result |
| 5. three independent referees with no fatal finding | not assessed here | this report: no fatal finding, MAJOR on gate 7 |
| 6. literature check | open | WORK.md itself lists novelty items 1-2 as "pending LITCHECK" |
| 7. falsifiable prediction or consistency check | weakly met at best | F1: part (i) contradicts the line's own "accidental zero allowed"; part (ii) is generic. Numbers correct but overstated (F2). Overseer ruling needed |
