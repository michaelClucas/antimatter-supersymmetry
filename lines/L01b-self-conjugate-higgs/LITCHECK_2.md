# L01b LITCHECK 2 (claims i-v of the emerging negative result)

Checked 2026-11-25. Web/arXiv/ar5iv. Complements LITCHECK.md (which covered the citations and the Veltman-zero numbers). Status labels: CONFIRMED (stated in print), PARTIAL (ingredients in print, not the combined statement), NOT FOUND.

## (i) Antimatter operations preserve spin/statistics, so cannot be SUSY; only SUSY changes spin (CM / HLS)

**CONFIRMED (ingredients), PARTIAL (antimatter-specific statement).**
- Martin, SUSY primer, hep-ph/9709356, §1 around eq. (1.5): SUSY transformation turns bosonic into fermionic states; Q is a spin-1/2 fermionic operator. Same section cites Haag-Lopuszanski-Sohnius (ref [7]) and Coleman-Mandula (ref [8]) as the reason SUSY is the only allowed extension. §1 also says superpartners "cannot be identified with some other Standard Model state" (sneutrino-as-Higgs example).
- Primary: Coleman & Mandula, Phys. Rev. 159, 1251 (1967); Haag, Lopuszanski, Sohnius, Nucl. Phys. B88, 257 (1975). (Bibliographic data standard, not re-fetched.)
- arXiv:0807.3883 ("Electroweak Symmetry Breaking and BSM Physics (A Review)"): Q spinorial, so partners differ in spin; contrasts SUSY doubling with Dirac's antiparticle doubling. Closest printed contrast of antiparticles vs superpartners found. Section not pinned.
- C, P, T, CPT act within a Poincare irrep's spin label: textbook (Weinberg QFT vol. I ch. 2.6 / 5.8; not re-fetched here). No paper found that runs the full list (C, P, CP, T, CPT, Dirac sea, Feynman-Stueckelberg) against the λ_{Ht̃t̃} = y_t² relation; this exists only as forum-level discussion (PhysicsForums threads), not in print.

## (ii) Twin-Higgs-type same-spin protection unavailable because the antiparticle is not an independent field (H^c = iσ₂H*, |H|²+|H^c|² = 2|H|², H↔H^c is SU(2)_R custodial)

**PARTIAL.**
- Twin Higgs: Chacko, Goh, Harnik, hep-ph/0506256: Z₂ exchanges two independent copies H_A, H_B; the O(8) structure contains SM custodial SU(2). Left-right variant hep-ph/0512088 uses H_L, H_R doublets of SU(2)_L × SU(2)_R (independent fields).
- H^c = iσ₂H* and the SU(2)_L × SU(2)_R bidoublet form of the SM Higgs (custodial symmetry): standard, Sikivie-Susskind-Voloshin-Zakharov, Nucl. Phys. B173, 189 (1980) (bibliographic record confirmed; content not read).
- The specific argument "H^c cannot play H_B because it is the same field, |H|²+|H^c|² = 2|H|² is not SU(4)-enhanced, and H↔H^c is just an SU(2)_R element": NOT FOUND in print. It is a one-line corollary of the above, so treat as trivial-but-unpublished. Same for "antitop is the same Dirac field as the top, so cannot be a twin top". Searches for CP-conjugate / antiparticle mirror sectors in neutral naturalness (1810.01882, 1709.08636, 1806.10702, 1905.02203) found only independent twin sectors.

## (iii) No SM symmetry enforces C = 0; C(M_t) ≈ −4.07; zero at ~10^22.8 GeV

**CONFIRMED (qualitative and crossing); number not independently checked.**
- Veltman, Acta Phys. Polon. B12, 437 (1981) posed C = 0 as a condition precisely because no symmetry enforces it. Dawson, TASI Higgs lectures hep-ph/0512377: setting the SM scalar mass to zero restores no symmetry ('t Hooft criterion). arXiv:2101.06932 frames C = 0 as needing an unknown symmetry.
- Crossing: Hamada-Kawai-Oda arXiv:1210.2538 (~10^23 GeV at M_t = 173); Masina-Quiros arXiv:1308.1242 (slightly trans-Planckian); Jegerlehner arXiv:1305.6652 (~10^17, different matching). Already in LITCHECK.md §1.
- C(M_t) ≈ −4.07 is normalization-dependent (δμ² = CΛ²/16π²); not compared against a printed number. Order of magnitude consistent with 2m_W² + m_Z² + m_h² − 4m_t² < 0 at the weak scale.

## (iv) SM has antimatter-built protection only for composite scalars (pion EM mass via ρ/a1 Weinberg sum rules)

**CONFIRMED (physics), PARTIAL (framing).**
- Das, Guralnik, Mathur, Low, Young, PRL 18, 759 (1967) and Weinberg sum rules, PRL 18, 507 (1967) (standard; not re-fetched): finite π⁺−π⁰ splitting from ρ/a1.
- Used explicitly as the template for composite-Higgs protection: Contino TASI 2009, arXiv:1005.4269 (Higgs as composite pNGB; pion EM mass analogue); Harada-Tanabashi-Yamawaki hep-ph/0303193 (π⁺π⁰ mass difference as dynamical origin of little Higgs); TASI 2024, arXiv:2412.15744.
- The "antimatter-built" (q q̄ bound state) label for this mechanism: NOT FOUND in print; it is relabeling.

## (v) QCD q̄q condensate breaks EW symmetry in the SM, m_W ≈ g f_π/2 ≈ 30 MeV

**CONFIRMED.**
- Quigg & Shrock, arXiv:0901.3958, PRD 79, 096002 (2009), §II.A.1: M̄_W² = g² f̄_π²/4 (inline after eq. 2.5), M̄_W ≈ 28 MeV (eq. 2.7), with f̄_π ≈ 87 MeV (chiral-limit value). Cites Weinberg PRD 19, 1277 (1979), "see also" PRD 13, 974 (1976), and Susskind PRD 20, 2619 (1979) together as ref. [23].
- Note for WORK: use 28 MeV / f̄_π ≈ 87 MeV with the Quigg-Shrock citation, or say "≈ 30 MeV" explicitly as rounded.

## Gate item 6 verdict

All five component facts are in print or are textbook (i, iii, v CONFIRMED; ii, iv ingredients CONFIRMED). Nothing physics-new.

New, modest, framing only:
1. The explicit statement and refutation of the "antimatter as SUSY substitute" hypothesis as a two-part no-go: (a) every antimatter operation is spin/statistics-preserving, so CM/HLS exclude it from relating λ_{Ht̃t̃} to y_t²; (b) the same-spin escape (twin Z₂) fails because H^c and the antitop are not independent fields, H↔H^c lying inside custodial SU(2)_R. Part (b) was not found anywhere in print; part (a) only in forum-level form and in passing contrasts (0807.3883, Martin §1).
2. Grouping pion-EM-mass protection and QCD-induced EWSB under an "antimatter-built" label: relabeling of known results (Das et al. 1967; Quigg-Shrock 2009).

Recommend WORK present (1) as a pedagogical no-go assembled from standard results, citing Martin §1, CM/HLS, hep-ph/0506256, and Quigg-Shrock, and not claim new physics.
