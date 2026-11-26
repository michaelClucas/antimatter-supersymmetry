# LITCHECK_3 (c10): the 7 c9 citations in WORK.md

Source: INSPIRE-HEP literature API (titles, authors, publication_info, arXiv ids, abstracts), queried 2026-11-25. Full texts not re-read; use checks rely on abstracts plus standard content.

| # | Citation as in WORK.md | Bibliographic status | Use in WORK.md | Use status |
|---|---|---|---|---|
| 1 | Chacko, Goh, Harnik, "The Twin Higgs: Natural Electroweak Breaking from Mirror Symmetry", PRL 96, 231802 (2006), hep-ph/0506256 | Confirmed (INSPIRE: same title, authors, PRL 96 231802, 2006, hep-ph/0506256) | §4d header, item 5 line 24: Z₂ to mirror copy, U(4) → U(3) with 7 Goldstones, Λ² top term cancelled by same-spin twin top | Matches the paper's mechanism |
| 2 | Arkani-Hamed, Cohen, Georgi, "Electroweak symmetry breaking from dimensional deconstruction", PLB 513, 232 (2001), hep-ph/0105239 | Confirmed (PLB 513, 232-240, 2001) | §4d: "little Higgs collective breaking" | Matches: this is the original little Higgs paper, where the Higgs is a pNGB whose quadratic divergence is removed by collective breaking. Needs new fields, as WORK.md says |
| 3 | Burdman, Chacko, Goh, Harnik, "Folded supersymmetry and the LEP paradox", JHEP 0702, 009 (2007), hep-ph/0609152 | Confirmed (JHEP 02 (2007) 009; "0702, 009" is the old-style equivalent) | §4d and route table: spin-changing partners, uncoloured under SM colour, new fields | Matches: folded squarks are scalar top partners charged under a mirror colour, not SM colour |
| 4 | Gildener & Weinberg, "Symmetry breaking and scalar bosons", PRD 13, 3333 (1976) | Confirmed (INSPIRE capitalizes "Symmetry Breaking and Scalar Bosons") | line 189: tree μ² = 0, scalon mass m² = 8Bv² from STr M⁴, B < 0 with SM content so no GW vacuum | Matches the GW construction (flat direction, one-loop V = Bφ⁴(ln φ²/v² − 1/2), m_S² = 8Bv² with B ∝ Σ(3M_V⁴ + M_S⁴ − 4m_F⁴)). The numerical B is the repo's own computation, not checked here |
| 5a | Zimmermann, "Reduction in the number of coupling parameters", Commun. Math. Phys. 97, 211 (1985) | Confirmed (INSPIRE title "Reduction in the Number of Coupling Parameters", CMP 97, 211, 1985) | S5, item 6: RG-invariant coupling relations can exist without a symmetry | Matches: abstract gives a spinor-pseudoscalar example where reduction fixes the quartic in terms of the Yukawa with no symmetry involved |
| 5b | Kubo, Sibold, Zimmermann, Nucl. Phys. B 259, 331 (1985) | Confirmed (NPB 259, 331-350, 1985). Title not given in WORK.md; it is "Higgs and Top Mass from Reduction of Couplings" | same | Matches. Note: KSZ apply reduction to the SM itself and predict m_H ≈ 61 GeV, m_t ≈ 81 GeV (±10-15%), both excluded by measurement. That directly supports WORK.md's point that the measured trajectory, not the polynomial, rules out an RG-invariant SM relation |
| 6 | Volkov & Akulov, PLB 46, 109 (1973) | Confirmed (PLB 46, 109-110, 1973). Title not given in WORK.md; it is "Is the Neutrino a Goldstone Particle?" | S3, item 4: nonlinear realization of SUSY needs at least a goldstino | Matches: the paper builds the nonlinear (goldstino) Lagrangian |
| 7 | de Wit & Freedman, "Phenomenology of Goldstone neutrinos", PRL 35, 827 (1975) | Confirmed (PRL 35, 827, 1975; DOI 10.1103/PhysRevLett.35.827) | S3, item 4, referee table: "neutrino-as-goldstino excluded by low-energy theorems" | Matches in substance, see note below |

## Note on #7 (checked specifically)

The APS abstract: the paper studies the hypothesis that the physical neutrino is the Goldstone fermion of spontaneously broken SUSY, derives the low-energy theorems, and finds the resulting β-decay end-of-spectrum behaviour in strong disagreement with experiment (neutral-current phenomenology was acceptable). So the exclusion is: low-energy theorems fix goldstino couplings, and those predictions contradict β-decay data. WORK.md's "excluded by low-energy theorems" compresses this; "excluded by low-energy theorems confronted with β-decay spectra" would be more exact. Not a substantive error. Later work (e.g. Bardeen-Visnjic 1982) also argues against neutrino-as-goldstino; not needed for the claim.

## Corrections applied to WORK.md

None needed. All volumes, pages, years and arXiv ids match INSPIRE. Each line in the c9 reference list was marked "[verified c10]". The "[from memory, not re-read]" tag on de Wit-Freedman in S3 was replaced with "[verified c10]".

## Substantive issues

None. Minor wording only (#7 above).
