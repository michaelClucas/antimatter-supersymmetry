# CONSTRAINTS

Literature-checked in cycle 1; see `CONSTRAINTS_LITCHECK.md` for item-by-item sources.

Every line of inquiry must survive every item in this file, addressed explicitly in writing before promotion.

Tags used below:
- **[established]** measured or proven, citation given
- **[uncertain]** number or citation the overseer could not fully verify at setup time; a literature checker must confirm or correct it
- **[approx]** order-of-magnitude summary of a body of results (e.g. LHC exclusion contours that depend on the model)

---

## Part A. Scope rules (override everything else)

### A1. Standard Model antimatter only

"Antimatter" means antimatter as described by the Standard Model, plus observed facts about it.

Allowed:
- SM fields and their antiparticles; gauge group SU(3)xSU(2)xU(1); the Higgs; CKM and PMNS CP violation (neutrino oscillations and nonzero neutrino masses are observed; the mass mechanism is not, see A2)
- Exact CPT symmetry (theorem of local Lorentz-invariant QFT)
- Dirac theory and its interpretations: Dirac sea / hole theory, Feynman-Stueckelberg (antiparticles as negative-energy states propagating backward in time), used only as equivalent descriptions of the same physics
- Anomalies, sphalerons, instantons, other non-perturbative SM effects
- Observed facts: baryon asymmetry of the universe, ALPHA-g 2023, CPT precision tests, measured masses and couplings

Not allowed (any line depending on these is scrapped):
- New particles or fields: superpartners, sterile / right-handed neutrinos, axions, extra Higgs doublets, mirror or twin sectors, dark-sector antimatter
- Leptogenesis via heavy neutrinos, GUT baryogenesis, any baryogenesis mechanism beyond the SM
- Majorana nature of neutrinos (not established)
- CPT violation, Lorentz violation, antigravity, Dirac-Milne or other matter-antimatter symmetric cosmologies, Boyle-Finn-Turok CPT-symmetric universe
- Any unobserved phenomenon, however well-motivated

SUSY may be used as a mathematical comparison target. Superpartners may never appear in a mechanism.

### A2. Neutrino mass caveat
Nonzero neutrino masses are observed. Their origin is not. A line may use measured Δm² and mixing angles and PMNS CP phase (with its large uncertainty). It may not assume a Dirac mass via right-handed neutrinos or a Majorana mass. If a calculation needs a neutrino mass term, it must state that the result is insensitive to the mechanism, or scrap.

### A3. Allowed reformulations of the SM
A line may work in a formulation mathematically equivalent to the SM in the sector used: division-algebra models (R⊗C⊗H⊗O; Dixon, Furey), Connes-Chamseddine noncommutative geometry / spectral action, Clifford-algebra formulations, fiber-bundle gauge theory, path-integral vs canonical, gauge choices, twistor / amplitude methods.

Conditions:
1. State, with citation or committed derivation, the map onto SM field content, gauge group and Lagrangian.
2. Extra states or relations the framework predicts or allows (extra generations, extra scalars, high-scale coupling relations, extra U(1)s, the spectral action's unification boundary condition, the NCG σ scalar) may not be used.
3. If equivalence is partial or disputed, say so and restrict to the equivalent part.
4. Any result must also hold in the standard formulation.

---

## Part B. Discrete-symmetry and antimatter-specific tests

| ID | Quantity | Value / limit | Source | Tag |
|---|---|---|---|---|
| B1 | K0 / anti-K0 mass difference | \|m(K0) − m(K0bar)\| / m_K < 6 × 10⁻¹⁹ (90% CL) | PDG Review of Particle Physics, 2024 (Phys. Rev. D 110, 030001), K0 listings | [established], exact figure [uncertain] |
| B2 | Antiproton / proton charge-to-mass ratio | R = (q/m)_pbar / (q/m)_p = −1.000 000 000 003(16), i.e. agreement at 16 ppt | BASE, Borchert et al., Nature 601, 53 (2022) | [established] |
| B3 | Antiproton magnetic moment | μ_pbar = −2.792 847 344 1(42) μ_N, 1.5 ppb | BASE, Smorra et al., Nature 550, 371 (2017) | [established] |
| B4 | Antihydrogen 1S–2S | agrees with hydrogen to ~2 × 10⁻¹² | ALPHA, Ahmadi et al., Nature 557, 71 (2018) | [established] |
| B5 | Antihydrogen gravity | a_g = (0.75 ± 0.13 (stat+syst) ± 0.16 (sim)) g; antimatter falls down, repulsive gravity excluded | ALPHA-g, Anderson et al., Nature 621, 716 (2023) | [established] |
| B6 | Electron / positron g-factor | consistent at ~2 × 10⁻¹² | Van Dyck, Schwinberg, Dehmelt, PRL 59, 26 (1987) | [uncertain] |
| B7 | Electron EDM | \|d_e\| < 4.1 × 10⁻³⁰ e·cm (90% CL) | JILA, Roussy et al., Science 381, 46 (2023), arXiv:2212.11841 | [established] |
| B8 | CKM CP violation size | Jarlskog invariant J ≈ 3.1 × 10⁻⁵ | PDG 2024 CKM review | [established] |
| B9 | Baryon CP violation (first observation) | Λ_b⁰ → pK⁻π⁺π⁻ | LHCb, Nature 643, 1223 (2025), arXiv:2503.16954 | [established] |
| B10 | Neutron EDM | \|d_n\| < 1.8 × 10⁻²⁶ e·cm (90% CL); bounds θ̄ ≲ 10⁻¹⁰ | Abel et al., PRL 124, 081803 (2020), arXiv:2001.11966 | [established] |

Consequence for any line: any mechanism that treats antiparticles differently from particles in mass, charge, magnetic moment, spectroscopy or gravitational coupling is dead at the levels above. Only CP-violating effects of CKM size (and PMNS) are available.

---

## Part C. Collider constraints

### C1. Higgs
- m_H = 125.20 ± 0.11 GeV (PDG 2024 average). The prompt's 125.1 GeV is within ~1σ; lines should use the PDG value. [established]
- Higgs couplings measured consistent with SM at the ~5-10% level for third-generation fermions and W/Z: ATLAS, Nature 607, 52 (2022); CMS, Nature 607, 60 (2022). [established]

### C2. Electroweak and top inputs (PDG 2024)
- M_Z = 91.1876(21) GeV (LEP lineshape; PDG 2024 world avg 91.1880(20)); M_W = 80.3692(133) GeV (PDG 2024, CDF II excluded). PDG 2026 updates: M_W = 80.3625(77) (includes CMS, arXiv:2412.13872), m_H = 125.13(11), m_t = 172.60(27). Cycle-1 lines use PDG 2024; shifts are below RG uncertainties. [established]
- m_t (pole, direct) = 172.57 ± 0.29 GeV [established]
- G_F = 1.1663788(6) × 10⁻⁵ GeV⁻², v = 246.22 GeV [established]

### C3. LHC SUSY exclusion limits [approx]
Full Run 2 (139-140 fb⁻¹, 13 TeV), simplified models, 95% CL. Exact values depend on the decay chain and LSP mass.
- Gluino: excluded up to ~2.2-2.4 TeV for light neutralino LSP
- First/second generation squarks (degenerate): up to ~1.8-1.9 TeV
- Top squark: up to ~1.2-1.3 TeV for massless LSP
- Electroweakinos (wino-like χ±/χ0 → WZ/Wh): ~0.65-1.06 TeV depending on decay mode (1.06 TeV only from the fully hadronic search, arXiv:2108.07586; 3ℓ WZ 640 GeV, arXiv:2106.01676). Higgsinos much weaker.
- Sleptons: up to ~0.7 TeV
Sources: ATLAS summary plots ATL-PHYS-PUB-2024-014 (https://twiki.cern.ch/twiki/bin/view/AtlasPublic/SearchesPublicResults); CMS SUSY public results (https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS). Run 3 (13.6 TeV) updates partial as of 2026 [uncertain].

Any line must explain why superpartner-like signatures are absent. A line that reproduces a SUSY result via SM-only physics automatically satisfies this, but must say so explicitly.

### C4. Muon g-2
- Fermilab final (2025): a_μ(exp) = 116 592 070.5(14.8) × 10⁻¹¹ (127 ppb). [uncertain on last digits]
- Theory Initiative White Paper 2025 (lattice HVP): a_μ(SM) consistent with experiment. [uncertain]
A former SUSY motivation (Δa_μ) is no longer an anomaly. Lines must not claim to explain it.

---

## Part D. Gauge couplings at M_Z (MS-bar, PDG 2024)

| Quantity | Value | Tag |
|---|---|---|
| α_s(M_Z) | 0.1180 ± 0.0009 | [established] |
| α_em⁻¹(M_Z) (MS-bar, 5 flavours) | 127.930 ± 0.008 (PDG 2024; 127.951 was PDG 2022) | [established] |
| sin²θ_W(M_Z) (MS-bar) | 0.23129 ± 0.00004 | [established] |

Derived: α₁ (GUT-normalized, 5/3 α_Y), α₂ obtained by standard relations. Lines must use `tools/` RG code and state loop order.

Reference facts:
- SM couplings do not meet at a point at 1 or 2 loops. MSSM with sparticle threshold ~1 TeV gives approximate unification at ~2 × 10¹⁶ GeV, α_GUT⁻¹ ≈ 24-25. Amaldi, de Boer, Fürstenau, PLB 260, 447 (1991); Langacker & Luo, PRD 44, 817 (1991); Ellis, Kelley, Nanopoulos, PLB 260, 131 (1991). [established]
- CPT implies particles and antiparticles contribute identically to beta functions (a Dirac fermion counts once as a field; particle and antiparticle are its two charge states). Any claim that "antiparticle contributions" change running must confront this. [established]

---

## Part E. Cosmology

| ID | Quantity | Value | Source | Tag |
|---|---|---|---|---|
| E1 | Cold dark matter density | Ω_c h² = 0.1200 ± 0.0012 | Planck 2018 VI, arXiv:1807.06209 (TT,TE,EE+lowE+lensing) | [established] |
| E2 | Baryon density | Ω_b h² = 0.02237 ± 0.00015 | same | [established] |
| E3 | Baryon-to-photon ratio | η = n_B/n_γ ≈ 6.1 × 10⁻¹⁰ | Planck 2018 + BBN; PDG BBN review (Fields, Molaro, Sarkar) | [established] |
| E4 | Dark energy density | ρ_Λ ≈ (2.24 meV)⁴ ≈ 2.5 × 10⁻⁴⁷ GeV⁴ | derived from Planck 2018 Ω_Λ ≈ 0.685, H₀ ≈ 67.4 | [established] |
| E5 | Dark matter properties | non-baryonic at BBN/CMB; cold; electrically neutral to high precision; self-interaction σ/m ≲ 1 cm²/g (cluster bounds) | Planck 2018; Bullet Cluster, Markevitch et al. ApJ 606, 819 (2004) | [established]/[approx] |
| E6 | N_eff | 2.99 ± 0.17 | Planck 2018 | [established] |
| E7 | Neutrino mass sum | Σm_ν < 0.12 eV (Planck 2018 + BAO); DESI DR2 + CMB: < 0.064 eV (95%, ΛCDM), 0.16 eV in w₀w_a; in tension with oscillation minimum 0.059 eV | Planck 2018; DESI DR2 arXiv:2503.14738, 2503.14744 | [established], cosmology-model dependent |
| E8 | Neutrino direct mass | m_ν < 0.45 eV (90% CL) | KATRIN, Science 388, 180 (2025), arXiv:2406.13516 | [uncertain] on journal ref |

### E9. Matter-antimatter symmetric cosmologies
- Antimatter domains in our universe must be at least ~Gpc in size, i.e. comparable to the observable universe, from the diffuse gamma-ray background produced at domain boundaries. Cohen, De Rújula, Glashow, ApJ 495, 539 (1998), arXiv:astro-ph/9707087. [established]
- CMB spectral distortions (μ, y) and BBN (photodisintegration of light elements by annihilation products) further constrain late annihilation. COBE/FIRAS |μ| < 9 × 10⁻⁵, |y| < 1.5 × 10⁻⁵ (95%; Fixsen et al. ApJ 473, 576 (1996)). BBN photodisintegration reference still needed. [established] for FIRAS
- No annihilation gamma lines from antimatter clouds or antistars: Fermi-LAT, Dupourqué, Tibaldo, von Ballmoos, PRD 103, 083016 (2021), arXiv:2103.10073, at most ~1 antistar per ~4 × 10⁵ stars in the solar neighbourhood (model dependent). [uncertain] on exact figure
- Galactic 511 keV positron annihilation line exists (INTEGRAL/SPI; Prantzos et al., Rev. Mod. Phys. 83, 1001 (2011)). Origin debated but compatible with astrophysical positron sources. [established] that it exists; any line using it must not require new physics.
- Cosmic-ray antinuclei: no confirmed antihelium. BESS-Polar II: anti-He/He < ~10⁻⁷. Abe et al., PRL 108, 131301 (2012). AMS-02 reported unconfirmed candidate events (conference talks only). [uncertain]

### E10. Baryogenesis inside the SM
- SM electroweak phase transition is a crossover for m_H ≳ 72 GeV, so no departure from equilibrium at the EW scale. Kajantie et al., PRL 77, 2887 (1996), hep-ph/9605288 (endpoint ≈80 GeV); endpoint 72(2) GeV from Rummukainen et al., NPB 532, 283 (1998), hep-lat/9805013; D'Onofrio, Rummukainen, PRD 93, 025003 (2016). [established]
- CKM CP violation is far too small for EW baryogenesis, by ~10 orders of magnitude in naive estimates. Gavela, Hernández, Orloff, Pène, Mod. Phys. Lett. A 9, 795 (1994), hep-ph/9312215; Huet & Sather, PRD 51, 379 (1995). [established]
- Therefore: the observed baryon asymmetry is an observed fact the SM does not explain. Lines may use η as an input. They may not claim an SM mechanism produced it unless they overturn the two results above with a committed calculation.
- QCD transition is a crossover at physical quark masses (Aoki et al., Nature 443, 675 (2006)). No first-order QCD transition is available for nugget formation.

---

## Part F. Proton and baryon number

| ID | Quantity | Value | Source | Tag |
|---|---|---|---|---|
| F1 | p → e⁺π⁰ | τ/B > 2.4 × 10³⁴ yr (90% CL) | Super-Kamiokande, PRD 102, 112011 (2020), arXiv:2010.16098 | [established] |
| F3 | n → n̄ (ΔB = 2) | τ > 4.7 × 10⁸ s (90% CL) | Super-K, PRD 103, 012008 (2021), arXiv:2012.02607 | [established] |
| F2 | SM B+L violation | sphaleron / instanton; B−L conserved; zero-temperature rate ∝ exp(−4π/α_W) ~ 10⁻¹⁶⁵ | 't Hooft, PRL 37, 8 (1976) | [established] |

---

## Part G. Hierarchy and vacuum energy reference facts

- Veltman condition (one-loop quadratic divergence, cutoff): δm_H² = (3Λ²/(8π²v²))(m_H² + 2M_W² + M_Z² − 4m_t²) (e.g. Kolda & Murayama hep-ph/0003170; conventions for Λ vary). Bracket ≈ −8.2 × 10⁴ GeV² with PDG masses. Veltman, Acta Phys. Polon. B 12, 437 (1981). [established]. Convention note (corrected cycle 2): with V ⊃ −μ²|H|² and C = 6λ + (9/4)g² + (3/4)g'² − 6y_t² = (3/v²)(bracket), δμ² = CΛ²/(16π²), and since m_h² = 2μ², δm_h² = CΛ²/(8π²) = 3Λ²/(8π²v²)(bracket), the standard form. A line quoting CΛ²/(16π²) must call it δμ², not δm_h². Lines must state which they use. The sign and the zero of the bracket are convention-independent.
- In dimensional regularization there is no quadratic divergence; the hierarchy problem is restated as sensitivity to heavy thresholds. A line that "solves" the hierarchy problem by choice of regulator alone is not a result. [established, standard]
- Electron self-energy: in single-particle Dirac theory the self-mass diverges linearly; including the Dirac sea (positron) contributions it becomes logarithmic. Weisskopf, Phys. Rev. 56, 72 (1939). Modern reading: chiral symmetry protects fermion masses. [established]
- Pauli's vacuum-energy cancellation conditions: Σ(−1)^F g_i m_i^{2k} = 0 for k = 0, 1, 2 and Σ(−1)^F g_i m_i⁴ ln m_i = 0. SM degree-of-freedom count: 28 bosonic (16 gluon, 9 massive W/Z, 2 photon, 1 Higgs), 90 fermionic (72 quark, 12 charged lepton, 6 for left-handed neutrinos with no ν_R). Pauli 1951 lectures; Visser, Particles 1, 138 (2018), arXiv:1610.07264. [uncertain] on journal ref.
- Observed vacuum energy (E4) is ~10⁻¹²³ of naive M_Pl⁴. The SM electroweak contribution ~(100 GeV)⁴ alone is ~10⁵⁵ times too large; QCD condensate ~(200 MeV)⁴ ~10⁴⁴ times too large. [established]

---

## Part H. Methodology constraints

- H1. No numerology. A numerical coincidence without a mechanism derived from the SM Lagrangian (or an equivalent formulation) is not a result.
- H2. Regulator independence. Physical claims must hold in at least two regularization schemes or be stated as scheme-dependent.
- H3. Interpretations are not mechanisms. Dirac sea and Feynman-Stueckelberg pictures give identical S-matrix elements to standard QFT. A line using them must derive something that also holds in the standard formulation (A3.4 applies to interpretations as well).
- H4. Every quantitative claim has a committed, runnable script in `lines/<id>/calc/`.
