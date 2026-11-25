# L05 LITCHECK

Checked 2026-11-25 against INSPIRE records, arXiv abstracts, and full text of Martin primer, Martin-Vaughn and Langacker-Polonsky.

## 1. Citations

| # | WORK citation | status | notes |
|---|---|---|---|
| 1 | Nielsen, Am. J. Phys. 49, 1171 (1981) | CONFIRMED | "Asymptotic freedom as a spin effect", DOI 10.1119/1.12565 |
| 2 | Hughes, PLB 97, 246 (1980) | CONFIRMED | "Some comments on asymptotic freedom", pp. 246-248 |
| 3 | Hughes, NPB 186, 376 (1981) | CONFIRMED | "More comments on asymptotic freedom", pp. 376-396 |
| 4 | NSVZ, NPB 229, 381 (1983) | CONFIRMED | "Exact Gell-Mann-Low function of supersymmetric Yang-Mills theories from instanton calculus" |
| 5 | Machacek & Vaughn, NPB 222, 83 (1983) | CONFIRMED | Paper I, "Wave function renormalization", pp. 83-103; contains the two-loop gauge beta functions. Page is correct, drop "[unverified page]" |
| 6 | Jones, PRD 25, 581 (1982) | CONFIRMED | "The two loop beta function for a G1 x G2 gauge theory". Abstract: general fermions and scalars, "extension to supersymmetric models is also given". WORK's description ("two-loop SUSY gauge betas") is incomplete: it is primarily the non-SUSY product-group result, with a SUSY extension |
| 7 | Martin & Vaughn, PRD 50, 2282 (1994), hep-ph/9311340 | CONFIRMED | §IV gives MSSM two-loop b_ij. Note: printed in the transposed convention (first row 199/25, 9/5, 11/5). Erratum PRD 78, 039903 (2008) exists, add it |
| 8 | Martin, hep-ph/9709356, §6.1 | CONFIRMED | §6.1 "The superpotential and supersymmetric interactions" writes W_MSSM with ū, d̄, ē, H_u, H_d; holomorphy argument there. The anomaly argument for two doublets is in §1.3 (Tr[T₃²Y] = Tr[Y³] = 0), not §6.1 |
| 9 | Amaldi, de Boer, Fürstenau | CONFIRMED | PLB 260, 447 (1991) (via Langacker-Polonsky ref list) |
| 10 | Langacker & Luo | CONFIRMED | PRD 44, 817 (1991) (via LP ref list) |
| 11 | Ellis, Kelley, Nanopoulos | CONFIRMED | PLB 249, 441 (1990) (via LP ref list) |
| 12 | Georgi, Quinn, Weinberg, PRL 33, 451 (1974) | CONFIRMED | "Hierarchy of interactions in unified gauge theories" |
| 13 | Furey, PLB 742, 195 (2015), arXiv:1603.04078, DOI 10.1016/j.physletb.2015.01.023 | CONFIRMED | "Charge quantization from a number operator". arXiv ID was posted after publication, but INSPIRE links it to this PLB |
| 14 | Langacker & Polonsky, PRD 47, 4028 (1993), hep-ph/9210235 | CONFIRMED (paper); WRONG (number) | Paper is "Uncertainties in coupling constant unification". Their eq. (8): α_s(M_Z) = 0.125 ± 0.001 ± ... for m_t = 138 GeV, M_SUSY = m_h0 = M_Z. Not "≈ 0.13". Write "0.125 (m_t = 138 GeV)"; the higher m_t pushes it up, so L05's 0.129 is not in conflict, but the quoted number should be theirs |
| 15 | Jack, Jones, Kord, hep-ph/0308231 | CONFIRMED (exists); content not checked | PLB 579, 180 (2004), "Three loop soft running, benchmark points and semiperturbative unification". Whether it prints the MSSM 3-loop gauge betas in full was not checked |
| 16 | Phi(SM) = MSSM content "standard construction" | CONFIRMED | Martin primer Table 1.1 / §6.1 |

16 citations: 14 CONFIRMED clean, 1 CONFIRMED with description fix (#6), 1 with wrong quoted number (#14). Section pointers: #8 anomaly argument is §1.3.

## 2. Novelty

**Identity: MSSM b_ij = 2 × SM b_ij for all i ≠ j and for (1,1).**
Arithmetic checked: ratios are exactly 2 for the six off-diagonal entries and b₁₁; b₂₂ ratio 30/7, b₃₃ ratio −7/13. Both matrices appear side by side in many places (Martin-Vaughn §IV for MSSM, Machacek-Vaughn/Jones for SM, Langacker-Polonsky, every unification review). I searched for "twice", "factor of 2/two" in Langacker-Polonsky and Martin-Vaughn full text (no hit) and ran several web searches for an explicit statement (no hit). Not found stated anywhere. It is a two-line consequence of the general formulas (per chiral multiplet off-diagonal weight 4C_jS_i vs 2C_jS_i per Weyl fermion and 4C_jS_i per complex scalar, with Higgs doubled), so specialists could derive it on sight, but I found no printed statement. The "holds only if H^c is independent" refinement is also unprinted as far as I found.

**Mapping SM in conjugate-Weyl basis onto MSSM chiral multiplets, described as an "antimatter" map.**
The map itself is the textbook MSSM construction (Martin primer §1.3, §6.1; every SUSY review notes that ū, d̄, ē are the left-handed antiparticle fields). Calling it an antimatter map: not found anywhere. Labelling only.

**Spin-part decomposition b_MSSM = b_spin(SM) + C(G) + 2S(H) (gauginos + Dirac higgsino) and Str(T) = 0 per supermultiplet.**
Str(T) = 0 per supermultiplet is a known consequence of the Nielsen-Hughes form and is used in SUSY non-renormalization discussions. The specific decomposition statement was not found printed.

**Proposition 1 (CPT relabelling cannot change b or B).** Trivial and implicit everywhere (CPT, D in CONSTRAINTS). Not new.

**Partial-map table (H^c promotion alone gives B = 0.556, 15% of the shift).** Equivalent to known one-loop B for 2HDM (r = −2/11): the two-Higgs-doublet SM b and its poor unification are standard. Framing as "antimatter step" is new labelling only.

## 3. Gate item 6 verdict

Mainly a restatement in antimatter labelling. What is new, as far as the literature search reaches:
1. The exact two-loop identity b_ij^MSSM = 2 b_ij^SM for i ≠ j and (1,1), and that the uniform factor needs the second doublet. Elementary, unprinted. This is the line's one citable new statement.
2. The spin/orbital decomposition attributing all of MSSM B − 1/2 to the Dirac higgsino. Elementary, not found printed.
Everything else (the map, B values, running, 2HDM step, Prop. 1) is standard.
