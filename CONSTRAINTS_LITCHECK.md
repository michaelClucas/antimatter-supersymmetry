# CONSTRAINTS.md literature check

Checked 2026-11-25 against arXiv abstracts, INSPIRE-HEP records (journal/volume/page/DOI), PDG 2022/2024/2026 PDFs, and collaboration pages. CONSTRAINTS.md was not edited. Where PDG 2026 has superseded a PDG 2024 value, both are given; the file says "PDG 2024", so the 2024 value is what's being checked, and the 2026 number is listed for the overseer to decide on.

Status key: **CONFIRMED** / **CORRECTED** (correct value + source) / **COULD NOT VERIFY**.

---

## Part B

| ID | Status | Notes / source |
|---|---|---|
| B1 K0 mass difference | **CONFIRMED** | PDG value is `<6 × 10⁻¹⁹`, 90% CL, normalized to m_average. It is a PDG "Our Evaluation" (first entered in PDG 2012, still carried in 2024 and 2026 listings). It assumes CPT invariance in the decay and neglects non-ππ channels. Upgrade tag to [established], but note it is a PDG derived limit, not a single experiment. https://pdglive.lbl.gov/view/S011DMM |
| B2 BASE q/m | **CONFIRMED** | Borchert et al., Nature 601, 53 (2022), doi:10.1038/s41586-021-04203-w. |
| B3 BASE μ_pbar | **CONFIRMED** | Smorra et al., Nature 550, 371 (2017), doi:10.1038/nature24048. |
| B4 ALPHA 1S-2S | **CONFIRMED** | Ahmadi et al., Nature 557, 71 (2018), doi:10.1038/s41586-018-0017-2. |
| B5 ALPHA-g | **CONFIRMED** | Anderson et al., Nature 621, 716 (2023), doi:10.1038/s41586-023-06527-1. |
| B6 e⁻/e⁺ g-factor | **CONFIRMED** (reference correct; exact figure added) | Van Dyck, Schwinberg, Dehmelt, PRL 59, 26 (1987), doi:10.1103/PhysRevLett.59.26. Result: g(e⁻)/g(e⁺) = 1 + (0.5 ± 2.1) × 10⁻¹². PDG lists it as (g₊ − g₋)/g_avg = (−0.5 ± 2.1) × 10⁻¹². "Consistent at ~2 × 10⁻¹²" is right. Tag can become [established]. |
| B7 JILA eEDM | **CONFIRMED** | Roussy et al., Science 381, 46 (2023), doi:10.1126/science.adg4084, arXiv:2212.11841. |
| B8 Jarlskog J | **CONFIRMED** | PDG 2024 CKM review: J = 3.12 (+0.13 −0.12) × 10⁻⁵. PDG 2026: J = 3.16 (+0.13 −0.11) × 10⁻⁵. "≈ 3.1 × 10⁻⁵" is fine. |

## Part C

### C1
| Item | Status | Notes |
|---|---|---|
| m_H = 125.20 ± 0.11 GeV (PDG 2024) | **CONFIRMED** | PDG 2024 summary table: 125.20 ± 0.11 (S = 1.4). Update: PDG 2026 gives **125.13 ± 0.11 GeV** (S = 1.5), https://pdg.lbl.gov/2026/tables/rpp2026-sum-gauge-higgs-bosons.pdf |
| ATLAS Nature 607, 52; CMS Nature 607, 60 (2022) | **CONFIRMED** | doi:10.1038/s41586-022-04893-w; doi:10.1038/s41586-022-04892-x (both have later corrigenda: Nature 612, E24; Nature 623, E4). |

### C2
| Item | Status | Notes |
|---|---|---|
| M_Z = 91.1876(21) GeV | **CORRECTED (minor)** | 91.1876 ± 0.0021 is the LEP lineshape value. PDG 2024's world average including CDF is **91.1880 ± 0.0020 GeV** (PDG 2024 EW review eq. 10.58 and constants table). PDG 2026: 91.1879(20). Either is fine for RG input; say which. |
| M_W = 80.369(13) GeV | **CONFIRMED for PDG 2024**, but superseded | PDG 2024: 80.3692 ± 0.0133 GeV, CDF II excluded. PDG 2025 shows CMS but does not average it. **PDG 2026: M_W = 80.3625 ± 0.0077 GeV**, including CMS (Nature 652, 321 (2026), arXiv:2412.13872, M_W = 80.3602 ± 0.0099). Recommend switching to the 2026 value. https://pdgweb.lbl.gov/2026/reviews/rpp2026-rev-w-mass.pdf |
| m_t = 172.57 ± 0.29 GeV | **CONFIRMED** | PDG 2024 direct average. PDG 2026: **172.60 ± 0.27 GeV**. |
| G_F = 1.1663788(6) × 10⁻⁵ GeV⁻² | **CONFIRMED** | PDG 2024 EW review. v = (√2 G_F)^(−1/2) = 246.22 GeV follows. |

### C3 LHC SUSY [approx]
Run 2 headline numbers checked against the primary ATLAS papers (abstracts via INSPIRE). I could not read the values off the summary-plot images, and did not check CMS numbers.

| Item | Status | Source |
|---|---|---|
| Gluino ~2.2-2.4 TeV | **CONFIRMED** | ATLAS 0ℓ: 2.30 TeV (massless χ̃⁰₁), JHEP 02 (2021) 143, arXiv:2010.14293. |
| Degenerate 1st/2nd-gen squarks ~1.8-1.9 TeV | **CONFIRMED** | Same paper: 1.85 TeV. |
| Stop ~1.2-1.3 TeV | **CONFIRMED** | ATLAS all-hadronic: 400-1250 GeV excluded for m(χ̃⁰₁) < 200 GeV, EPJC 80, 737 (2020), arXiv:2004.14060. |
| Electroweakinos ~1.0-1.1 TeV | **CORRECTED (qualify)** | The ~1.06 TeV wino limit comes only from the fully hadronic boosted-boson search (PRD 104, 112010 (2021), arXiv:2108.07586), and it assumes particular branching ratios and m(LSP) < 400 GeV. Leptonic channels give less: WZ 3ℓ on-shell 640 GeV (EPJC 81, 1118 (2021), arXiv:2106.01676); Wh 1ℓbb 740 GeV (EPJC 80, 691 (2020), arXiv:1909.09226). Suggested text: "~0.65-1.06 TeV depending on decay mode." Higgsinos are much weaker (≤ 0.9 TeV hadronic, 210 GeV in 3ℓ). |
| Sleptons ~0.7 TeV | **CONFIRMED** | 700 GeV for mass-degenerate sleptons (ẽ, μ̃, L+R), massless LSP, EPJC 80, 123 (2020), arXiv:1908.08215. |
| ATLAS twiki URL | **CORRECTED** | `AtlasPublic/SupersymmetryPublicResults` is discontinued and redirects to https://twiki.cern.ch/twiki/bin/view/AtlasPublic/SearchesPublicResults. Latest ATLAS summary plots: ATL-PHYS-PUB-2024-014 (July 2024). |
| Run 3 status | **PARTIAL** | Through Nov 2026 I found only partial Run 3 SUSY results, with no general extension of the strong-production reach. Examples: ATLAS stop 2ℓ combining Run 2 with 53 fb⁻¹ at 13.6 TeV, m(t̃) < 1060 GeV in that channel, ~10% better than before (arXiv:2603.16191); ATLAS/CMS Run 3 long-lived slepton and displaced-lepton searches; ATLAS strong-production proceedings with 13.6 TeV data (arXiv:2601.19695). "Partial as of 2026" is accurate. CMS Run 3 SUSY list: COULD NOT VERIFY. |

### C4 Muon g-2
| Item | Status | Notes |
|---|---|---|
| Fermilab final 116 592 070.5(14.8) × 10⁻¹¹, 127 ppb | **CONFIRMED** | Written as 116 592 0705(148) × 10⁻¹². PRL 135, 101802 (2025), arXiv:2506.03069, doi:10.1103/7clf-sm2v. New world average (with BNL): 116 592 071.5(14.5) × 10⁻¹¹ (124 ppb). |
| WP2025 SM consistent | **CONFIRMED** | a_μ(SM) = 116 592 033(62) × 10⁻¹¹ (530 ppb); exp − SM = 38(63) × 10⁻¹¹. Aliberti et al., Phys. Rept. 1143 (2025), arXiv:2505.21476, doi:10.1016/j.physrep.2025.08.002. LO HVP from lattice QCD only. |

## Part D (PDG 2024)
| Item | Status | Notes |
|---|---|---|
| α_s(M_Z) = 0.1180 ± 0.0009 | **CONFIRMED** | PDG 2024 constants table; unchanged in PDG 2026. |
| α_em⁻¹(M_Z) MS-bar = 127.951 ± 0.009 | **CORRECTED** | 127.951 ± 0.009 is the **PDG 2022** value. **PDG 2024: α̂⁽⁵⁾(M_Z)⁻¹ = 127.930 ± 0.008** (EW review sec. 10.2), https://pdg.lbl.gov/2024/reviews/rpp2024-rev-standard-model.pdf. The mixed-edition inputs should be made consistent. The shift (0.021) is smaller than most RG uncertainties but larger than the quoted error. |
| sin²θ̂_W(M_Z) MS-bar = 0.23129 ± 0.00004 | **CONFIRMED** | PDG 2024 (global-fit value). PDG 2022 was 0.23122(4); **PDG 2026: 0.23122(6)**. |
| Amaldi, de Boer, Fürstenau PLB 260, 447 (1991) | **CONFIRMED** | doi:10.1016/0370-2693(91)91641-8. Abstract: MSSM unification at 10^(16.0±0.3) GeV. |
| Langacker & Luo PRD 44, 817 (1991) | **CONFIRMED** | doi:10.1103/PhysRevD.44.817. |
| Ellis, Kelley, Nanopoulos PLB 260, 131 (1991) | **CONFIRMED** | doi:10.1016/0370-2693(91)90980-5. |

## Part E
| ID | Status | Notes |
|---|---|---|
| E1 Ω_c h² = 0.1200 ± 0.0012 | **CONFIRMED** | Planck 2018 VI, A&A 641, A6 (2020), arXiv:1807.06209; PDG 2024 cosmological parameters table. |
| E2 Ω_b h² = 0.02237 ± 0.00015 | **CONFIRMED** | Same. |
| E3 η ≈ 6.1 × 10⁻¹⁰ | **CONFIRMED** | PDG 2024 BBN review (Fields, Molaro, Sarkar): η₁₀ = 6.12 ± 0.04 (Planck); CMB+BBN 6.115 ± 0.038. |
| E4 ρ_Λ ≈ (2.24 meV)⁴ ≈ 2.5 × 10⁻⁴⁷ GeV⁴ | **CONFIRMED** | Recomputed: ρ_c = 8.098 × 10⁻⁴⁷ h² GeV⁴, h = 0.674, Ω_Λ = 0.685 → 2.52 × 10⁻⁴⁷ GeV⁴ → (2.24 meV)⁴. |
| E5 Markevitch et al. ApJ 606, 819 (2004) | **CONFIRMED** | doi:10.1086/383178, arXiv:astro-ph/0309303. |
| E6 N_eff = 2.99 ± 0.17 | **CONFIRMED** (add qualifier) | Planck 2018 abstract: this is **with BAO** (TT,TE,EE+lowE+lensing+BAO), 68%. |
| E7 Planck Σm_ν < 0.12 eV | **CONFIRMED** | 95%, Planck 2018 abstract. |
| E7 DESI "≲ 0.07 eV" | **CORRECTED** | DESI DR2 BAO + CMB, ΛCDM: **Σm_ν < 0.064 eV (95%)**; 0.16 eV in w₀w_a. arXiv:2503.14738. Companion neutrino paper arXiv:2503.14744: 0.0642 eV, and 0.053 eV with a Feldman-Cousins treatment; it describes ~3σ tension with the normal-ordering minimum 0.059 eV. The bound is model-dependent (it relaxes in w₀w_a), so state the cosmology. |
| E8 KATRIN | **CONFIRMED** | Science 388 (6743), 180-185 (2025), doi:10.1126/science.adq9592, arXiv:2406.13516; m_ν < 0.45 eV (90% CL), 259 days. Data-taking reached 1000 days in late 2025; I found no final full-dataset result as of Nov 2026. Tag can become [established]. |
| E9 Cohen, De Rújula, Glashow ApJ 495, 539 (1998) | **CONFIRMED** | doi:10.1086/305328, arXiv:astro-ph/9707087. |
| E9 FIRAS μ | **CONFIRMED** | Fixsen et al., ApJ 473, 576 (1996), arXiv:astro-ph/9605054: \|μ\| < 9 × 10⁻⁵ and \|y\| < 15 × 10⁻⁶, both 95% CL. This is a COBE/FIRAS bound; "Planck/FIRAS" is a misattribution, so drop "Planck". The "Kawasaki et al." BBN photodisintegration citation has no specific paper; **COULD NOT VERIFY** as written, give an actual reference. |
| E9 Fermi-LAT antistars | **CONFIRMED** | Dupourqué, Tibaldo, von Ballmoos, PRD 103, 083016 (2021), arXiv:2103.10073. 14 candidates from 4FGL-DR2; for a disk-like population f < 2.5 × 10⁻⁶ at **95% CL** (1 per 4 × 10⁵ stars). Halo population: f < 0.2 (1 M☉) to 1.6 × 10⁻⁴ (10 M☉). Add "95% CL, disk population" and the tag can drop [uncertain]. |
| E9 Prantzos et al. RMP 83, 1001 (2011) | **CONFIRMED** | doi:10.1103/RevModPhys.83.1001. |
| E9 BESS-Polar | **CONFIRMED** (wording tightened) | Abe et al., PRL 108, 131301 (2012), arXiv:1201.2967. anti-He/He < 1.0 × 10⁻⁷ (combined BESS-Polar I+II, 1.6-14 GV, no spectrum assumed). With all BESS flights and antiHe assumed to have the He spectrum: 6.9 × 10⁻⁸ (95% CL). |
| E9 AMS-02 antihelium | **CONFIRMED** | No peer-reviewed AMS-02 antihelium paper found. Candidates (~ten events, ³He-bar and ⁴He-bar) appear only in talks by Ting et al. The only AMS antihelium journal paper is AMS-01, PLB 461, 387 (1999). The GAPS balloon is the planned independent test. |
| E10 Kajantie et al. PRL 77, 2887 (1996) | **CORRECTED (attribution of 72 GeV)** | The citation is correct (doi:10.1103/PhysRevLett.77.2887), but its abstract gives 70 < m_H,c < 95 GeV, "most likely ≈ 80 GeV". The 72 GeV endpoint is from Rummukainen, Tsypin, Kajantie, Laine, Shaposhnikov, NPB 532, 283 (1998), hep-lat/9805013 (m_H,c = 72(2) GeV). The 4D lattice cross-check is Csikor, Fodor, Heitger, PRL 82, 21 (1999). The conclusion (crossover at 125 GeV) is unchanged. |
| E10 D'Onofrio & Rummukainen PRD 93, 025003 (2016) | **CONFIRMED** | arXiv:1508.07161. |
| E10 Gavela et al. MPLA 9, 795 (1994) | **CONFIRMED** | hep-ph/9312215. |
| E10 Huet & Sather PRD 51, 379 (1995) | **CONFIRMED** | hep-ph/9404302. |
| E10 Aoki et al. Nature 443, 675 (2006) | **CONFIRMED** | hep-lat/0611014. |

## Part F
| ID | Status | Notes |
|---|---|---|
| F1 Super-K p → e⁺π⁰ | **CONFIRMED** | PRD 102, 112011 (2020), arXiv:2010.16098. I found no newer published e⁺π⁰ limit. |
| F2 't Hooft PRL 37, 8 (1976) | **CONFIRMED** (minor numeric note) | exp(−4π/α_W) with α_W(M_Z) ≈ 1/29.6 gives ≈ 10⁻¹⁶². The often-quoted ~10⁻¹⁶⁵ depends on which α_W is used. Write "~10⁻¹⁶²-10⁻¹⁶⁵". |

## Part G
| Item | Status | Notes |
|---|---|---|
| Veltman, Acta Phys. Polon. B 12, 437 (1981) | **CONFIRMED** | "The Infrared - Ultraviolet Connection" (INSPIRE 155775). |
| Veltman normalization | **CORRECTED** | "(3/2)(…)/v²" is not a standard normalization. The common cutoff form is δm_H² = (3Λ²/(8π²v²)) (m_H² + 2M_W² + M_Z² − 4m_t²), as in e.g. Kolda & Murayama, JHEP 07 (2000) 035, hep-ph/0003170. I took this form from memory and an arXiv:2101.06932 summary, not from Veltman's original, so the `tools/` code should still derive it. Other papers write Λ²/(16π²v²)·STr M², which differs by convention for Λ. The bracket with PDG 2024 masses is ≈ −8.2 × 10⁴ GeV², clearly nonzero either way. |
| Weisskopf, Phys. Rev. 56, 72 (1939) | **CONFIRMED** | doi:10.1103/PhysRev.56.72. The abstract states the self-energy is "only logarithmically infinite in positron theory". |
| Visser, Particles 1, 138 (2018) | **CONFIRMED** | Particles 1(1), 138-154 (2018), article 10, doi:10.3390/particles1010010, arXiv:1610.07264. Tag can become [established]. |
| SM dof count 28 / 90 | **CONFIRMED** | Arithmetic check: 16+9+2+1 = 28; 72+12+6 = 90. |
| Vacuum-energy ratios | **CONFIRMED** | (100 GeV)⁴/ρ_Λ ≈ 4 × 10⁵⁴; (200 MeV)⁴/ρ_Λ ≈ 6 × 10⁴³; M_Pl⁴/ρ_Λ ≈ 10¹²³ (non-reduced M_Pl; ~10¹²⁰ with reduced M_Pl). |

---

## Counts
- CONFIRMED: 47 (rows marked CONFIRMED above; Run 3 status counted separately as partial)
- CORRECTED: 10 (M_Z minor, ATLAS twiki URL, electroweakino range, α_em⁻¹ edition, DESI figure, FIRAS "Planck" attribution, 72 GeV endpoint attribution, Veltman normalization, F2 exponent (minor), M_W superseded by PDG 2026)
- COULD NOT VERIFY: 3 ("Kawasaki et al." with no specific paper, CMS SUSY numbers and Run 3 list, values printed only in summary-plot images)

## Missing constraints worth adding (all verified via INSPIRE)
1. **Neutron EDM**: d_n = (0.0 ± 1.1 ± 0.2) × 10⁻²⁶ e·cm, i.e. |d_n| < 1.8 × 10⁻²⁶ e·cm (90% CL). Abel et al. (nEDM@PSI), PRL 124, 081803 (2020), arXiv:2001.11966. This is the strong-CP / θ̄ bound, relevant to any line using QCD instantons (A1 allows them).
2. **CP violation in baryon decays (first observation)**: LHCb, Nature 643, 1223 (2025), arXiv:2503.16954 (Λ_b⁰ → pK⁻π⁺π⁻). This is an observed fact about matter vs antimatter baryons and should sit next to B8.
3. **Neutron-antineutron oscillation**: τ(n→n̄) > 4.7 × 10⁸ s (90% CL). Super-K, PRD 103, 012008 (2021), arXiv:2012.02607. This is the ΔB = 2 limit; F covers only ΔB = 1.
4. **Antiproton-to-electron mass ratio**: ASACUSA, Hori et al., Science 354, 610 (2016). An independent CPT test of antiproton mass.
5. **Antihydrogen hyperfine spectrum**: ALPHA, Nature 548, 66 (2017). A spectroscopy test complementary to B4.
6. **W mass, CMS**: Nature 652, 321 (2026), arXiv:2412.13872. This now drives the PDG 2026 average (see C2).
7. (Status note) BASE coherent single-antiproton spin spectroscopy, Latacz et al., Nature 644, 64 (2025), doi:10.1038/s41586-025-09323-1. The volume and page come from CERN/MPI-HD press pages and were not checked on INSPIRE. This is a method advance, not yet a tighter CPT bound; B3 stands.
