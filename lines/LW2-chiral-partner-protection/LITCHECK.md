# LW2 LITCHECK (literature checker, 2026-11-25)

Sources: INSPIRE API (bibliographic records, abstracts), arXiv full texts of 0801.2562, 1307.7879, 1005.4269, 1506.01961, 1811.04279 (pdftotext + grep), web search for BHL numbers.

## 1. Citations

| # | Citation as given in WORK.md | Verdict |
|---|---|---|
| 1 | Das, Guralnik, Mathur, Low, Young, PRL 18, 759 (1967), doi:10.1103/PhysRevLett.18.759 | CONFIRMED. "Electromagnetic mass difference of pions", pp. 759-761. Contino 1005.4269 eq. (90) attributes the ρ/a1 formula to it ("first derived in 1967 by Das et al."). |
| 2 | Weinberg, PRL 18, 507 (1967), doi:10.1103/PhysRevLett.18.507 | CONFIRMED. "Precise relations between the spectra of vector and axial vector mesons", pp. 507-509. |
| 3 | Bardeen, Hill, Lindner, PRD 41, 1647 (1990), doi:10.1103/PhysRevD.41.1647 | CONFIRMED (bibliography). Title "Minimal Dynamical Symmetry Breaking of the Standard Model". "BHL ~218 GeV at 10¹⁹ GeV": CONFIRMED via secondary sources (OSTI top-condensate review: ~218 GeV at Λ = 10¹⁹ GeV, rising as Λ decreases; Yamawaki hep-ph/9603277: ~220 GeV at Planck cutoff). Original table not read directly. |
| 4 | Gasser & Leutwyler, Ann. Phys. 158, 142 (1984) | CONFIRMED. "Chiral Perturbation Theory to One Loop", doi:10.1016/0003-4916(84)90242-2. "Unverified page" flag can be dropped: page 142 is correct. Specific claim (m_u−m_d piece ≈ 0.1 MeV) not checked against the text. |
| 5 | Gaillard & Lee, PRD 10, 897 (1974) | CONFIRMED. "Rare Decay Modes of the K-Mesons in Gauge Theories". Giudice 0801.2562 §6 cites it (ref. [54]) as the charm-mass-from-naturalness argument, as the line claims. |
| 6 | CMS arXiv:1411.3441 | CONFIRMED. Spin-parity and anomalous HVV couplings, 7+8 TeV; published PRD 92, 012004 (2015). Add journal ref. |
| 7 | ATLAS arXiv:1506.05669 | CONFIRMED. Spin and parity in diboson decays; EPJC 75, 476 (2015), erratum EPJC 76, 152 (2016). Add journal ref. |
| 8 | Caprini, Colangelo, Leutwyler, PRL 96, 132001 (2006), hep-ph/0512364 | CONFIRMED. "Mass and width of the lowest resonance in QCD". Pole 441 − i272 MeV matches the published value (441 +16/−8, 272 +9/−12.5; from memory of abstract text, abstract on INSPIRE truncated before the numbers). |
| 9 | Quigg & Shrock, PRD 79, 096002 (2009), arXiv:0901.3958 | CONFIRMED. "Gedanken Worlds without Higgs: QCD-Induced Electroweak Symmetry Breaking". |
| 10 | Contino arXiv:1005.4269 | CONFIRMED. "The Higgs as a Composite Nambu-Goldstone Boson" (TASI 2009, published 2011 in TASI proceedings p. 235). |
| 11 | Panico & Wulzer arXiv:1506.01961 | CONFIRMED. "The Composite Nambu-Goldstone Higgs", Lect. Notes Phys. 913 (2016). |
| 12 | Csáki, Lombardo, Telem 1811.04279 (named in task, not in WORK.md) | CONFIRMED. "TASI lectures on non-supersymmetric BSM models". |
| 13 | Giudice 0801.2562, 1307.7879 (named in task) | CONFIRMED. "Naturally Speaking: The Naturalness Criterion and Physics at the LHC"; "Naturalness after LHC8" (PoS EPS-HEP2013, 163). |

Count: 13 checked, 13 CONFIRMED bibliographically, 0 WRONG. Minor: two LHC refs lack journal info; BHL 218 GeV confirmed only through secondary sources.

## 2. Novelty

(a) Pion EM mass protected by ρ/a1 via WSRs as the template for Higgs-mass protection. NOT NEW. Contino 1005.4269 §3.2 "Comparing with QCD: the pion potential" derives the DGMLY formula (eq. 90) from ρ/a1 saturation of both WSRs as the QCD prototype of the composite-Higgs potential. Panico-Wulzer 1506.01961 §5.3 "The Weinberg sum rules" / §5.3.2 "The Higgs potential and the Weinberg sum rules" imposes WSR-like conditions on top partners to make the Higgs potential finite. Panico-Wulzer §3.3.2-3.3.3 (around eq. 3.3.63) compare top partners directly with stops/gluinos ("completely analogous situation ... in supersymmetric models"). Csáki-Lombardo-Telem §3.1 contrasts same-spin partner cancellation (collective breaking) with opposite-spin SUSY partners. Giudice 0801.2562 §6 puts the pion/ρ case next to SUSY as a naturalness example. The explicit row-by-row dictionary WSR1/WSR2 ↔ Str 1 / Str M² with F² weights was not found in this form, but it is a restatement of known content.

(b) WSR1 removes Λ², WSR2 removes ln Λ; soft SUSY leaves a log. Each half is stated: Panico-Wulzer §5.3.2 (eqs. 5.3.9-5.3.10) say the first conditions kill the quadratic divergence and a further condition kills the log; composite-Higgs papers (e.g. Marzocca-Serone-Shu 1205.0770; Pomarol-Riva 1205.6434) note that imposing only the first sum rule leaves log sensitivity. The soft-SUSY log is textbook. A sentence explicitly saying "the pion EM mass is therefore protected more strongly than soft SUSY protects m_h" was not found in the reviews checked. Status: the comparison is a trivial juxtaposition of known statements; at most a framing novelty, not a result. Also note the comparison is not like-for-like: WSR2 holds because the symmetry breaking (⟨q̄q⟩) is spontaneous/soft enough that Π_V − Π_A ~ 1/Q⁶; the analogous statement in SUSY is that a supersoft (Dirac-gaugino) breaking also gives finite scalar masses (Fox-Nelson-Weiner hep-ph/0206096, cited from memory, unverified). So "stronger than SUSY" holds only against MSSM-type soft breaking.

(c) h and G⁰ as chiral partners, m_h/v (λ) only log-sensitive, μ² carries the Λ². NOT NEW. m_h² = 2λv² with logarithmic running of λ and the hierarchy problem residing in the H†H coefficient is standard (e.g. Giudice 0801.2562 §2-3; any SM RG treatment). The explicit cutoff S − P computation is a check, not new content.

(d) Λ_nat = 851 MeV vs partners at 775/1230 MeV. NOT NEW. Giudice 0801.2562 §6 "The Paths Chosen by Nature", eq. (7): (3α/4π)Λ² must not exceed (35.5 MeV)², so Λ < 850 MeV, and "the ρ meson exists (M = 770 MeV)". Repeated in Giudice 1307.7879 (intro: "naturalness of the pion mass difference is cured by the coming of the rho meson"). The line's Gaillard-Lee charm remark is in the same Giudice section.

(e) Pure-SM top condensation needs m_t ≈ 235-246 GeV. NOT NEW; consistent with BHL (~218 GeV at 10¹⁹, higher for lower Λ; ~230 GeV around 10¹⁵ is commonly quoted). The line's 1-loop Landau-pole criterion gives values ~15-20 GeV higher than BHL's full-RG compositeness boundary condition; WORK.md should state that its number is a cruder criterion, not a disagreement with BHL. Exclusion by m_t = 172.6 GeV is well known (and by m_h = 125 GeV).

## 3. Gate item 6 verdict

Nothing physically new. Every substantive claim (DGMLY finiteness from both WSRs, pion/ρ as a naturalness success at 850 vs 770 MeV, WSR-type sum rules for top partners in composite Higgs, top/stop analogy, λ log-only vs μ² quadratic, BHL failure, QCD-induced EWSB size) is in the cited literature. The only original element is the presentation: a literal WSR ↔ supertrace table and the one-line "removes ln Λ too, unlike MSSM soft breaking" contrast. Recommend labelling §4 items as "known; repo re-derivation", and qualifying the "stronger than soft SUSY" claim (supersoft SUSY breaking also gives finite masses).

## 4. Numbers

PDG inputs: m_π± = 139.57039 MeV, m_π⁰ = 134.9768 MeV → Δm² = 1261.16 MeV², Δm = 4.5936 MeV. Matches WORK.md. m_ρ = 775.26 MeV, m_a1 = 1230 ± 40 MeV (PDG estimate), f_π = 130.2/√2 = 92.1 MeV. Matches.

Formula: Δm² = (3α/4π) m_ρ² m_a1²/(m_a1² − m_ρ²) ln(m_a1²/m_ρ²) is CONFIRMED (Contino 1005.4269 eq. 90, identical form; no f_π dependence once both WSRs are used).

Recomputed (α = 1/137.036): m_a1 = 1230 → 1603.7 MeV² (1.27× measured); range 1190-1270 → 1559-1648 MeV²; KSRF m_a1 = √2 m_ρ → 1451.5 MeV². Δm via √(m_π0² + Δm²) − m_π0 gives 5.82 / 5.27 MeV (WORK.md values); via Δm²/(m_π+ + m_π0) gives 5.84 / 5.29 MeV. No discrepancy beyond this convention. Contino gets 5.8 MeV with m_ρ = 770, m_a1 = 1260. Λ_nat = 850.8 MeV, matches Giudice's 850 MeV.
