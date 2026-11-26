# L05 REVIEWS

## Referee 1 (cycle 5)

**Verdict: MINOR ISSUES ONLY**

Independent check: `calc/referee1_check.py` (output `calc/referee1_check.txt`), written from the general formulas, not from the line's scripts. MV two-loop gauge coefficients per Weyl fermion 2S_iC_j + δ_ij(10/3)C(G)S_i, per complex scalar 4S_iC_j + δ_ij(2/3)C(G)S_i, per real scalar 2S_iC_j + δ_ij(1/3)C(G)S_i, gauge −(34/3)C(G)²δ_ij (Luo-Wang-Xiao form of Machacek-Vaughn). SUSY: −6C(G)²δ_ij + Σ_chiral(4S_iC_j + 2C(G)S_iδ_ij) (Martin-Vaughn / Jones).

What survives:
- (i) Reproduced both textbook matrices from field content. MSSM/SM = 2 exactly on all six off-diagonal entries and b_11; b_22, b_33 ratios 30/7, −7/13. Correct.
- (ii) Φ* theorem: ratio 2 on off-diagonal + abelian entries for 200 random gauge contents (random reps, U(1) charges, Weyl, complex and real scalars). Correct. 26/25 counterexample reproduced.
- (iii) Top-Yukawa term: SM (17/10, 3/2, 2) from fermion legs at weight 1, MSSM (26/5, 6, 4) from all three legs at weight 2; MSSM − 2·SM = (9/5, 3, 0) = Higgs leg. Correct.
- (iv) Three-loop SM entries spot-checked against the known values (g_3⁷: 65/2 SM, 347/3 MSSM; g_3⁵g_2²: 21 SM, 6 MSSM). The non-uniformity is robust, more so than WORK argues (finding 3).
- (v) Scope: no non-SM content enters any mechanism. H^c-as-independent-field and T_dbl are explicitly flagged as A1-forbidden second doublet / mirror doubling. A1 pass. No experimental consequence exists, and WORK says so honestly. The only checkable consequences are mathematical (the identity on other Φ* pairs).
- Citations spot-checked from my own knowledge (MV NPB 222, 83; Martin-Vaughn PRD 50, 2282 + erratum PRD 78, 039903; Ferreira-Jack-Jones PLB 387, 80; Jack-Jones-North hep-ph/9606323; Mihaila-Salomon-Steinhauser 1201.5868 and 1208.3357; Martin-Vaughn PLB 318, 331; Jack-Jones-Kord PLB 579, 180). No wrong IDs found.

### Findings

1. **[Moderate] C4.4, last paragraph: the claim that minimal SUSY agrees with Φ* "for any U(1)-charged scalar and any scalar in a complex rep" is false.** The set where minimal SUSY ≠ Φ* is larger than "complex scalars in real reps". Counterexamples (referee1_check.txt):
   - A vector-like pair of complex scalars (R and R̄, e.g. (2,1,±1/2)). Minimal SUSY is 2 chirals, each higgsino is the other's anomaly partner, and the ratio is **1**. This is exactly the 2HDM. With the 2HDM as parent, MSSM/2HDM off-diagonal ratios are **3/2** for (1,2), (2,1) and **199/104** for (1,1).
   - A complex scalar in a pseudoreal rep with no U(1) charge, e.g. (2,8,0). One chiral has 8 SU(2) doublets, so it is Witten-safe and SU(3)³-safe, and minimal SUSY is one chiral. Ratio **8/7**.
   Fix: say "Φ* and minimal SUSY agree when the complex scalars carry no anomaly-free vector-like pairing among themselves and each one's fermion partner needs a new conjugate partner. The SM's single doublet is such a case." Also state plainly that the doubling depends on taking the one-doublet SM as the parent. The same MSSM is not 2× its 2HDM parent. This strengthens (v): the "2" belongs to the choice of parent, not to antimatter.

2. **[Minor] Stale "iff" in §2.3 and §4 item 3.** "The uniform factor 2 holds only if H^c is counted as an independent field" and "this uniformity holds iff H^c is an independent field" contradict C4.2. There, b_ij cannot tell H^c from a second Y = +1/2 doublet, and any extra content with the same Σ S_iC_j would also work. §2.3 also gives the no-H_d ratios as "5/3 or 2" and omits b_11 = 389/199 (reproduced). Fix: replace "iff H^c" with "iff a second doublet chiral multiplet with |Y| = 1/2 is present (H^c is one choice)", and add 389/199.

3. **[Minor] C4.5 / c4_threeloop.py §0: the scheme statement is incomplete, and the robust argument is missed.**
   (a) "Only c_i(jj), j ≠ i, shifts" is wrong for the diagonal. g_i → g_i(1 + k_i g_i²) shifts c_i(ii) by −2k_i b_ii − 3k_i² b_i (referee check). The script never tests the g_i⁷ coefficient. This does not affect the mixed table, since k_1 = 0, but the printed claim is false.
   (b) The full MS↔DR relation has two-loop mixed terms g_i(1 + k g_i²g_j²), with n_G-dependent k from matter loops. These shift c_i(jj) by 2k b_j (referee check), which can add an n_G² piece. So "54/11 is invariant under the MS↔DR conversion" is shown only for the one-loop conversion. Fix: qualify it, or cite the two-loop product-group DR/MS conversion.
   (c) Strengthening: c_i(ij) (g_i⁵g_j²) and the fully mixed c_i(jk) are invariant under every redefinition that keeps β_i ∝ g_i³ (background-field structure). Those invariant entries already disagree: 8 (fully mixed) vs 2/7 (c_3(13), c_3(23)) vs 8/13 (c_2(12), c_2(23)) on the n_G¹ parts. So (iv) holds in every such scheme, not just in the two printed ones. Add this sentence.

4. **[Minor] Stale literature tags in WORK §2.5, §3, C4.1 not updated after LITCHECK.**
   - Langacker-Polonsky is quoted as "≈ 0.13". Their eq. (8) gives 0.125 for m_t = 138 GeV.
   - MV page, Jones, and Hughes are still marked [unverified] although LITCHECK confirmed them.
   - Jones PRD 25, 581 is described as "two-loop SUSY gauge betas". It is primarily the non-SUSY G1×G2 result with a SUSY extension.
   - The Martin-Vaughn erratum is not listed.
   - The anomaly argument is pointed to Martin §6.1. It is in §1.3.
   Fix per LITCHECK.

5. **[Minor] c4_doubling.py toy label "Weyl 2x(2,3) [+conj implied]".** Two Weyl (2,3) without a (2,3̄) are SU(3)³-anomalous. The numbers (200, 208) correspond to one (2,3) plus one (2,3̄) (same S, C). Fix the label.

6. **[Note] Novelty and framing.** The doubling identity is a two-line consequence of the per-field weight table (chiral 4 = 2 × Weyl 2 = complex scalar 4). Finding 1 shows it is a property of the parent→Φ* pair, not of the MSSM alone. Claim (v) stands: the antimatter phrasing is true but carries no antimatter-specific content, and no structure-preserving map specific to antimatter exists. No real (experimental) checkable consequence exists. WORK's §4.7/C4.6(c) already says this. Keep the line's final verdict as "negative result plus an elementary, apparently unprinted identity".
