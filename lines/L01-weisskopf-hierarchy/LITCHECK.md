# L01 LITCHECK - Weisskopf mechanism vs the Higgs hierarchy

Checked 2026-11-25 against INSPIRE, arXiv full texts (PDF text extracted and searched), and Crossref. "Primary" means the statement was checked in the cited paper's own text, not a summary.

## 1. Citations

| # | Citation as given in the line | Verdict | Notes |
|---|---|---|---|
| 1 | Weisskopf, Phys. Rev. 56, 72 (1939), DOI 10.1103/PhysRev.56.72 | CONFIRMED | Crossref: "On the Self-Energy and the Electromagnetic Field of the Electron", pp. 72-85. The abstract states the self-energy of charged Bose particles is quadratically divergent, so the WORK.md section 4 item 2 claim (marked unverified there) is CONFIRMED. The Snowmass naturalness white paper (arXiv:2205.05708, sec. 2, refs [30,31]) also attributes the charged-scalar quadratic divergence to this 1939 paper and quotes Weisskopf's "new features at this critical length" remark. |
| 2 | Weisskopf, Z. Phys. 89, 27 (1934); erratum Z. Phys. 90, 817 (1934) | CONFIRMED (bibliographic); attribution WRONG | Crossref: "Über die Selbstenergie des Elektrons", Z. Phys. 89, 27-39, DOI 10.1007/BF01333228; "Berichtigung ...", Z. Phys. 90, 817-818, DOI 10.1007/BF01340744. Correction: WORK.md section 1 calls the no-sea quadratic divergence (Tneg) "the 1934 Weisskopf result before Furry's correction". Weisskopf's 1934 paper was already a hole-theory calculation; its error (a sign error found by Furry) made the hole-theory result come out as divergent as the one-electron theory. The one-electron Dirac-theory self-energy divergence is the 1930 Waller / Oppenheimer computation (Waller, Z. Phys. 62, 673 (1930): COULD NOT VERIFY details). Also: the logarithmic result itself first appeared in the 1934 erratum. The 1939 paper extended it to all orders and to Bose particles. PROPOSAL.md's "Weisskopf 1939 showed ... linear to logarithmic" should credit 1934 (erratum) for the one-loop result. |
| 3 | 't Hooft, NATO Sci. Ser. B 59, 135 (1980) | CONFIRMED | INSPIRE: "Naturalness, chiral symmetry, and spontaneous chiral symmetry breaking", pp. 135-157 (Cargese 1979). |
| 4 | Hamada, Kawai, Oda, PRD 87, 053009 (2013), arXiv:1210.2538 | CONFIRMED | Abstract: bare Higgs mass vanishes at cutoff ~10^23 GeV for M_t = 173 GeV, Planck scale for M_t = 170 GeV. Matches the line. Erratum PRD 89, 059901 (2014) exists. Not cited by the line but relevant: D.R.T. Jones, "Comment on 'Bare Higgs mass at Planck scale'", PRD 88, 098301 (2013), arXiv:1309.7335, disputes the two-loop quadratic-divergence coefficient. |
| 5 | Masina, Quiros, arXiv:1308.1242; journal PRD 88, 093003 (2013) | CONFIRMED | Journal ref verified (was marked unverified). Primary: potential V = -m^2 phi^2/2 + lambda phi^4/4 (eq. 8), C_V1 = 6 lambda + (9/4) g^2 + (3/4) g'^2 - 6 y_t^2 (eq. 12). Same normalization as the line's C, so "matches Masina-Quiros eq. 12" is CONFIRMED. "Around Planckian scales" (sec. I) and "slightly trans-Planckian" (sec. IV) are quoted correctly. Their eqs. 9-11 already state Veltman = Str M^2(phi)/phi^2 at large field. |
| 6 | Jegerlehner, arXiv:1305.6652 | CONFIRMED (content); journal ref WRONG | Title "The hierarchy problem of the electroweak Standard Model revisited". Primary: V = (m^2/2) H^2 + (lambda/24) H^4, C1 = 2 lambda + (3/2) g'^2 + (9/2) g^2 - 12 y_t^2 (eq. 4); with lambda_J = 6 lambda this is C1 = 2C, so the line's normalization claim is CONFIRMED. mu0 ≈ 7×10^16 GeV and y_t(M_Pl) = 0.3551 are in the text. Correction: Acta Phys. Polon. B 45, 1167 (2014) is a different paper, arXiv:1304.7813, "The Standard model as a low-energy effective theory: what is triggering the Higgs mechanism?" (whose abstract quotes mu0 ~ 1.4×10^16 GeV). INSPIRE lists no journal publication for 1305.6652; cite it as an arXiv preprint. |
| 7 | Buttazzo, Degrassi, Giardino, Giudice, Sala, Salvio, Strumia, JHEP 1312, 089 (2013), arXiv:1307.3536 | CONFIRMED | Primary: NNLO fits are eqs. (55)-(60) at mu = M_t; M_Pl values are eq. (61a-f): g1 = 0.6154, y_t = 0.3825, lambda = -0.0143, m(M_Pl) = 129.4 GeV. Appendix B is "SM RGE equations up to three loops", eqs. (95)-(104). The line's validation numbers and the 129.4 GeV discrepancy reference are accurate. g1 there is GUT-normalized (g1 = sqrt(5/3) g_Y). |
| 8 | Coleman, Weinberg, PRD 7, 1888 (1973), DOI 10.1103/PhysRevD.7.1888 | CONFIRMED | "Radiative Corrections as the Origin of Spontaneous Symmetry Breaking", pp. 1888-1910. |
| 9 | Weinberg, PRL 36, 294 (1976) | CONFIRMED | "Mass of the Higgs Boson". |
| 10 | Linde, JETP Lett. 23, 64 (1976) | CONFIRMED | "Dynamical Symmetry Restoration and Constraints on Masses and Coupling Constants in Gauge Theories" (Pisma ZhETF 23, 73). |
| 11 | Bardeen, FERMILAB-CONF-95-391-T (1995) | CONFIRMED (bibliographic); content COULD NOT VERIFY | INSPIRE: "On naturalness in the standard model". The paraphrase of the argument was not checked against the text. |

Not cited but should be: Veltman, "The Infrared - Ultraviolet Connection", Acta Phys. Polon. B 12, 437 (1981) (CONFIRMED on INSPIRE). This is the origin of the Veltman condition the line uses throughout.

Inputs (PDG 2024 via `tools/sm_inputs.py`) were not re-checked here.

Counts: 8 CONFIRMED, 2 WRONG (Jegerlehner journal ref; Weisskopf 1934 attribution), 1 partly unverified (Bardeen content).

## 2. Prior literature on the central claim

Central claim: SM antimatter gives no Weisskopf-type protection to m_h^2. The Veltman coefficient does not vanish below ~10^22.8 GeV. SM radiative EWSB fails.

- Weisskopf-to-hierarchy link is standard pedagogy. Murayama, hep-ph/0002232, sec. 1.3 "Positron Analogue" walks through exactly the Coulomb + pair-term cancellation (cites Weisskopf 1939), attributes delta m ∝ m to chiral symmetry, and then contrasts it with the Higgs, where only a new symmetry (SUSY) provides the analogous cancellation. The Snowmass naturalness white paper (Craig et al., arXiv:2205.05708, sec. 2) presents Weisskopf 1934/1939 as the first naturalness argument and notes that the charged scalar has no cancelling partner. So "the positron protects the electron mass, nothing in the SM protects the Higgs" is already the textbook framing. The line reaches the same conclusion.
- Veltman condition running: HKO (10^23 GeV for M_t = 173), Masina-Quiros (Planckian to slightly trans-Planckian, NNLO running), Jegerlehner (7×10^16 GeV, with lower y_t). Jegerlehner states in 1305.6652 (introduction) that his matching gives "a slightly lower value" of y_t. The scheme issue behind it is in Jegerlehner, Kalmykov, Kniehl, PLB 722, 123 (2013), arXiv:1212.4319 (tadpole-inclusive MS-bar top mass). So the line's "explanation" of Jegerlehner's early zero is already stated by Jegerlehner himself. Bednyakov, Fedoruk, Kazakov, PRD 113, 036018 (2026), arXiv:2509.03369, is a recent review of SM RG loop-order uncertainties and could be used for the theory error on mu0.
- Degrassi et al. (arXiv:1205.6497) and Buttazzo et al. give lambda(M_Pl) ≈ 0 and beta_lambda ≈ 0 near 10^17-10^18 GeV. These concern the quartic, not the Veltman coefficient. The line uses them correctly.
- SM radiative EWSB failure: Coleman-Weinberg 1973, Weinberg and Linde 1976 bounds. The top-mass exclusion of a CW Higgs is textbook. The MS-bar statement beta(m^2) ∝ m^2 is textbook (mass-independent scheme).
- No paper found that does the old-fashioned (time-ordered) decomposition of the Higgs top loop and states that both orderings are negative-definite pointwise. That observation is elementary: it is the fixed sign of a closed fermion loop for m_h < 2 m_t, written out in time orderings.

Was it established or ruled out? The SM-only protection of m_h^2 is ruled out in the standard literature (no symmetry protects a scalar mass; 't Hooft 1980). The Veltman zero location is established, with the line's number inside the published range (HKO 10^23, Masina-Quiros trans-Planckian).

## 3. Gate item 6 verdict

Restatement of known work. Each component is in the literature: Weisskopf reproduction (Weisskopf 1934/1939, Murayama 2000), chiral-symmetry reading ('t Hooft 1980, Murayama), Veltman running (HKO, Masina-Quiros, Jegerlehner), CW failure (1973/1976).

What the line adds, all minor:
1. An explicit time-ordered decomposition of the top-loop Higgs self-energy with a checked match to the covariant integrand. It shows both orderings are same-sign. Not found published as such, but it is a pedagogical restatement of the fermion-loop sign, not a new result.
2. An updated Veltman-zero scale with PDG 2024 inputs and 3-loop running (10^22.8 GeV) plus parametric derivatives (about 1.2 decades per GeV of M_t, M_t ≈ 169.4 GeV for a zero at M_Pl). This is a numerical update of HKO and Masina-Quiros, consistent with both.
3. A numerical reproduction of Jegerlehner's 7×10^16 GeV by lowering y_t(M_t) by 0.0286. The cause (lower y_t matching) is already stated by Jegerlehner.

No new derivation, constraint, or mechanism. "Nothing new physically" is the honest verdict.

## 4. Required corrections to WORK.md / PROPOSAL.md

1. Jegerlehner: drop "Acta Phys. Polon. B 45, 1167 (2014)" as the ref for 1305.6652. That ref is arXiv:1304.7813.
2. Weisskopf history: the one-loop log result is from the 1934 erratum. The no-sea quadratic divergence is the Waller/Oppenheimer 1930 one-electron result, not "Weisskopf 1934 before Furry's correction" (that was a hole-theory calculation with a sign error).
3. Mark as CONFIRMED: Weisskopf 1939 Bose quadratic divergence; Masina-Quiros PRD 88, 093003; Jegerlehner C1 = 2C normalization; Masina-Quiros eq. 12.
4. Add Veltman, Acta Phys. Polon. B 12, 437 (1981) and Murayama hep-ph/0002232 (sec. 1.3) as prior art for the framing. Consider citing Jones PRD 88, 098301 for the two-loop coefficient dispute.
