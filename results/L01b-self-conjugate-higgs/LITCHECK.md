# L01b LITCHECK

Checked 2026-11-25 against INSPIRE records, arXiv abstracts/full text where noted.

## 1. Citations

| # | WORK citation | status | notes |
|---|---|---|---|
| 1 | Weisskopf, Phys. Rev. 56, 72 (1939) | CONFIRMED | "On the Self-Energy and the Electromagnetic Field of the Electron", pp. 72-85, DOI 10.1103/PhysRev.56.72 |
| 2 | Veltman, Acta Phys. Polon. B 12, 437 (1981) | CONFIRMED | "The Infrared - Ultraviolet Connection", pp. 437-457 |
| 3 | Einhorn & Jones, PRD 46, 5206 (1992) | CONFIRMED | "The Effective potential and quadratic divergences", pp. 5206-5208, DOI 10.1103/PhysRevD.46.5206. Title fits the scheme-dependence use; full text not read |
| 4 | Martin, "A Supersymmetry Primer", hep-ph/9709356 | CONFIRMED (sum rule); PARTIAL (log formula) | Eq. (7.1.13): STr(m²) = −2g Tr(T^a)D^a = 0 if U(1) traces vanish, matches the "needs Tr Y = 0" note. The stop-specific form −(3y_t²/8π²)(m_Q²+m_U²+A_t²) ln Λ was not located in the primer; the primer has only the generic eq. (1.13) Δm_H² = m_soft²[(λ/16π²) ln(Λ/m_soft)+...]. The stop formula is standard (any natural-SUSY paper) but cite it elsewhere or cite eq. (1.13) as the generic form |
| 5 | Hamada, Kawai, Oda, PRD 87, 053009 (2013), arXiv:1210.2538 | CONFIRMED | "Bare Higgs mass at Planck scale". Erratum PRD 89, 059901 (2014) exists, add it. Abstract: zero at ~10²³ GeV for M_t = 173 GeV, near Planck for M_t ≈ 170 GeV. Consistent with L01b's 10^22.83 and M_t = 169.5 GeV at M_Pl |
| 6 | Masina & Quiros, arXiv:1308.1242 | CONFIRMED | "On the Veltman Condition, the Hierarchy Problem and High-Scale Supersymmetry". Journal ref: PRD 88, 093003 (2013), DOI 10.1103/PhysRevD.88.093003 (fill in). "Slightly trans-Planckian" wording confirmed |
| 7 | Buttazzo et al., JHEP 1312, 089 (2013), arXiv:1307.3536 | CONFIRMED | "Investigating the near-criticality of the Higgs boson" |
| 8 | 't Hooft, NATO Sci. Ser. B 59, 135 (1980) | CONFIRMED | "Naturalness, chiral symmetry, and spontaneous chiral symmetry breaking", Cargese 1979, pp. 135-157 |

8 citations: 7 CONFIRMED, 1 CONFIRMED with a pointer issue (#4 log formula not in the primer). 0 WRONG.

Relevant literature WORK does not cite:
- Jegerlehner, arXiv:1305.6652, puts the one-loop Veltman zero at μ₀ ~ 7×10¹⁶ GeV (abstract ~10¹⁷), not 10²³. Different matching/inputs. WORK should mention the spread between Jegerlehner (~10¹⁷) and HKO/Masina-Quiros (~10²³, trans-Planckian), since L01b's number sides with one group.
- Masina-Quiros Fig. 1 plots the quartic, gauge and top-Yukawa pieces of C_V1(μ) separately vs μ (see 2b).
- Martin primer §7.4 eq. (7.4.1): sum rules decouple into separate sectors when states with given conserved quantum numbers do not mix (see 2a).

## 2. Novelty

**(a) MSSM quadratic-divergence cancellation holds separately by charge sector (neutral bosons vs Majorana neutralinos, charged bosons vs charginos).**
Mostly known. The tree-level supertrace sum rule holds block by block for every set of unbroken conserved quantum numbers, because the mass matrices are block diagonal in those charges (Martin primer §7.4, the selectron example eq. (7.4.1); this is the standard light-squark argument against tree-level SUSY breaking). Applying that to the field-dependent EW sector, with Q = 0 and Q = ±1 blocks, gives exactly L01b's §1b result. I found no paper that writes out the neutral/charged EW-ino vs gauge+Higgs split for the Higgs Λ² coefficient explicitly, so the explicit computation is not in print as far as I found, but it is a direct corollary of a textbook fact. The "self-conjugate bosons cancelled by self-conjugate (Majorana) fermions" reading follows from charge conservation: a Q = 0 sector can only contain self-conjugate states or particle-antiparticle pairs of other neutral charges. It is a labelling, not new physics.

**(b) SM Veltman cancellation split into "boson pair loops vs top sea" with fractions 34% (M_t), 79% (M_Pl).**
Known in substance. The split C = (6λ + 9/4g² + 3/4g'²) − 6y_t² is the Veltman condition itself (Veltman 1981). Masina-Quiros (1308.1242) Fig. 1 plots the gauge, quartic and top pieces vs scale. HKO (1210.2538) gives the zero and its M_t dependence. The specific ratios R = 0.344 and 0.790 are not printed in the sources I read (Masina-Quiros gives curves, Jegerlehner gives only the zero and coupling values), but they follow by arithmetic from published curves. The "pair vs sea" hole-theory language is a relabelling of the same terms. Decker-Pestieau, Bian and Chakraborty et al.: not checked in full text; nothing in the searches suggests they contain the ratio in this form.

**(c) Higgs self-conjugacy framed as an antimatter analogue of SUSY protection.**
No source found. Searches for the Higgs being "its own antiparticle" in connection with naturalness/quadratic divergences/SUSY returned nothing relevant. The supporting statement that a real scalar admits no linear symmetry forbidding h² is standard naturalness lore ('t Hooft 1980; generic in reviews), but the specific framing (a)/(b)/(c) and the conclusion that the parallel to Majorana gauginos breaks at (c) (no chiral phase, no U(1)_R analogue) is not in anything I found. It is a negative result built from known pieces.

## 3. Gate item 6 verdict

Restatement, with a small new framing.
- Restatement: the Veltman decomposition and its running zero (Veltman; HKO; Masina-Quiros), the per-sector supertrace (corollary of Martin §7.4-type sum rules), symmetry arguments (standard).
- New, modest: (i) the explicit statement that the MSSM electroweak Λ² cancellation closes separately in the Q = 0 (self-conjugate) and Q = ±1 sectors, and the observation that SUSY never uses the SM self-conjugate bosons to cancel the top; (ii) quoted fractions 34%/67%/79% and the falsifiable M_t = 169.5 GeV for C = 0 at M_Pl (HKO already gives ~170 GeV, so this sharpens rather than discovers); (iii) the self-conjugacy-vs-Majorana-gaugino framing and where it fails. None of these is a new physical result.
