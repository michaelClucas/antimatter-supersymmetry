# L01b WORK - Self-conjugate Higgs vs SUSY's Higgs-mass protection

Single line for SUSY #1 (Higgs-mass protection) and #4 (radiative EWSB). L01-weisskopf-hierarchy is merged in by reference (Section 7).

Tags (CONSTRAINTS convention, refined per Referee 1 c4 finding 7):
- **[established]**: published or textbook result, citation given.
- **[computed]**: derived or computed in this line, with a committed script and saved output.
- **[conjecture]**: argued but not proven. **[speculation]**: outside what the line can test.

---

## CLAIM

**Target.** SUSY result #1 in its symmetry form: SUSY makes m_h² insensitive to the UV because an operator Q that commutes with the Hamiltonian and changes spin by 1/2 ties every boson coupling of H to a fermion coupling, e.g. λ_{H t̃ t̃} = y_t² (F-term of W = y_t H Q U). That relation is what cancels the top's Λ² term against the stops'. Result #4 (radiative EWSB) is treated in item 7.

**Statement (negative result; a strong argument, not a formal proof).** No symmetry of the SM Lagrangian, and in particular no antimatter operation (C, CP, CPT, the Dirac-sea and Feynman-Stueckelberg readings), enforces a relation that cancels the top's Λ² contribution to m_h². This covers both known protection patterns: SUSY's boson-fermion relation (needs a spin-changing operator) and twin-Higgs-type same-spin protection (needs an independent partner field). SM antimatter supplies neither, because every antimatter operation is spin-preserving and maps the SM field space onto itself without enlarging it: the antiparticle doublet H^c = iσ₂H* is a function of H, so |H|² + |H^c|² = 2|H|². Empirically, C(M_t) = −3.43 ± 0.05 (MS-bar) or −4.07 ± 0.04 (pole-mass form), at least 69σ from zero, and C(μ) crosses zero, if at all, transversally. "Within SM content" is not a formal class of theories, so the enumeration below (items 2-6) is exhaustive only over the known mechanisms; that is why this is labelled a strong argument [established ingredients; assembly and checks computed, `calc/c7_same_spin_out.txt`, `calc/c9_*_out.txt`].

1. **Every SM antimatter operation preserves spin.** C, P and CP are unitary and T and CPT antiunitary; all commute with J² (C, P commute with J; T, CPT send J → −J). They map a spin-j particle to a spin-j antiparticle with the same statistics. For the Dirac 4-spinor, ψ^c = iγ²ψ* transforms with the same Lorentz matrix as ψ (deviation 2.5×10⁻¹⁶). For the SM's Weyl fields, C maps (1/2,0) to (0,1/2): spin and statistics are kept, the chiral representation is exchanged. The Dirac-sea and Feynman-Stueckelberg pictures relabel the same Fock space (H3). [established; computed check S1 for the spinor part, argument for the boson part]
2. **The symmetry group of the SM Lagrangian acts diagonally on the couplings in C** (replaces the cycle-7 lemma "spin-preserving maps cannot relate y_t to λ, g", which holds only for global, homogeneous, linear maps; Referee C). The group is SU(3)×SU(2)×U(1)_Y gauge; the accidental global U(1)_B, U(1)_{Le,Lμ,Lτ} (B+L anomalous); approximate custodial SU(2)_R (exact only for g' → 0, y_t = y_b); flavour rephasings; exact CPT, and C, P, CP, T, each broken; classical scale invariance (broken by μ², anomalous). `calc/c9_symmetry_group.py` checks with random group elements that each Higgs-sector operator |H|², |H|⁴, (Q†H^c)t_R, (Q†H)b_R is mapped to itself (up to a phase or hermitian conjugation absorbed by the coupling), never to a different operator. So each element acts on (λ, g, g', |y_t|, |y_b|) as the identity, and C is an invariant, uncharged function that no element can force to zero. In the custodial limit (g' → 0, y_t = y_b = y) C = 9/4 g² + 6λ − 12y², further from zero, with no relation imposed. [computed]
3. **The four counterexample classes to the old lemma, each unavailable with SM content** (§4c):
   - *Gauge invariance* is inhomogeneous and does tie couplings across field-type classes, but only the vertices of one gauge field (V S S, V V S S, V F F, V³, V⁴) to one g. |H|⁴ and (Q†H^c)t_R are separately gauge invariant, so it leaves λ and y_t free. The SM gauge group is fixed by A1. [computed check + established]
   - *Nonlinear / pNGB realization* ties h-VV to hh-VV and h-tt to hh-tt and can keep m_h out of the Λ² term, but only if h is a Goldstone of a larger spontaneously broken group. In the SM, h is the radial mode of the O(4) of H and G±, G⁰ are its only Goldstones (eaten). Needs new strong dynamics or new fields (LW2 §3). [established]
   - *Scale invariance plus dimensional transmutation (Gildener-Weinberg)* fixes the scalon mass through STr M⁴ (B), not C. With SM content B = −4.39×10⁻³ < 0, so the GW vacuum does not exist; the measured SM has tree μ² ≠ 0. [computed]
   - *Twin Z₂ / same-spin partners* (Chacko-Goh-Harnik; little Higgs collective breaking) is the closest structural cousin of a particle↔antiparticle exchange. It needs an independent mirror copy (H_B, t_B). Item 5 shows antimatter cannot be that copy. [computed, §4d]
   - (Higher-dimensional Lorentz symmetry relating a 4D scalar to a 4D vector, gauge-Higgs unification, is 4D spin-changing and needs extra dimensions: BSM.)
4. **The only 4D spin-changing symmetry algebra is SUSY, and every realization needs new states.** Coleman-Mandula and Haag-Łopuszański-Sohnius classify symmetries of a non-trivial S-matrix (unbroken, linearly realized on asymptotic states); their usable output here is the algebra classification: a spin-changing symmetry algebra of a 4D relativistic QFT is super-Poincaré or superconformal. They do not by themselves cover broken symmetries or relations among Lagrangian couplings, and gluons are not asymptotic states. Every realization of SUSY needs new states: linear ones need superpartners (the SM has no colour-triplet scalar for the top, no octet fermion for the gluon; 28 bosonic vs 90 fermionic dof; only H ~ L* matches); nonlinear ones (Volkov-Akulov) need at least a goldstino. The old proposal that the neutrino is the goldstino is excluded by low-energy theorems (de Wit and Freedman 1975). Under A1 the decisive argument is the enumeration of item 2; CM/HLS explain why there is nothing else to look for. [established theorems; computed scan S3-S4]
5. **SM antimatter cannot play the twin** (§4d, `calc/c9_twin_antimatter_out.txt`). In twin Higgs, a Z₂ maps |H_A|² ↔ |H_B|², two different operators, and forces their coefficients equal; the top-loop Λ² term becomes κ(|H_A|² + |H_B|²), U(4) invariant on 8 real fields, and the light h is one of 7 Goldstone directions whose mass the κ term never reaches. With SM antimatter: (a) H^c = iσ₂H* has rank-4 Jacobian with respect to H's 4 real fields, H^c†H ≡ 0 and |H^c|² = |H|², so the space of Higgs bilinears is 1-dimensional and C, CP, CPT map it to itself, imposing nothing; (b) setting H_B := H^c gives κ(|H|² + |H^c|²) = 2κ|H|², mass eigenvalues {0, 0, 0, −4κ}: three eaten Goldstones and h as the radial mode with m_h² ∝ κ, i.e. no protection; (c) the particle↔antiparticle swap of the bidoublet, (H^c, H) → (H, −H^c), is Φ → ΦR† with R = iσ₂ ∈ SU(2)_R (det 1), an ordinary custodial rotation that leaves Tr Φ†Φ = 2|H|² invariant for any coefficient; (d) the antitop is the same Dirac field as the top: its two states are already 2 of the 4 per colour in C_top = −6y_t², and C/CP/CPT map the top loop into itself. [computed]
6. **No accidental all-scale relation, checked on the measured trajectory.** Without a symmetry, C = 0 could hold at one scale. A relation could also be RG invariant without a symmetry (reduction of couplings, Zimmermann; Kubo-Sibold-Zimmermann), and the one-loop polynomial β_C on C = 0 has real zeros, so the polynomial alone does not exclude that. What excludes it for the SM is the measured flow: C < 0 on all of [M_t, M_Pl] (maximum −0.183, Buttazzo matching) and the 3-loop flow crosses C = 0 at μ₀ = 10^22.83 GeV with dC/dlnμ = +0.0203 ± 0.0002 (PDG input errors), i.e. transversally (10^16.15 GeV, slope +0.024, with Jegerlehner's y_t). The one-loop polynomial is scheme independent; the crossing scale is not (C is a cutoff coefficient evaluated with MS-bar couplings). [computed S5, `calc/c9_C_measured_out.txt`]
7. **SUSY #4.** The SM has no Coleman-Weinberg or RG-driven radiative EWSB (L01, §7). It does have one dynamical EWSB mechanism built from antimatter: the QCD quark-antiquark condensate ⟨q̄_L q_R⟩ carries weak isospin and breaks SU(2)×U(1). It gives M_W = g f_π/2 = 30 MeV for one light doublet and about 52 MeV [approx] with all three quark doublets massless, against the observed 80.4 GeV. Its share of v² in the real SM is 1.4×10⁻⁷. The condensate scale falls short by v/f_π ≈ 2700 (one doublet) or v/(√3 f_π) ≈ 1540 (three doublets). [established, Quigg-Shrock 2009; computed `calc/c7_qcd_ewsb_out.txt`, `calc/c9_symmetry_group_out.txt` (5)]

**Route table** (protection mechanisms for a scalar mass, and their SM status):

| mechanism | what it needs | SM status |
|---|---|---|
| SUSY (spin-1/2 generator, holomorphy plus non-renormalization) | superpartners, or at least a goldstino | absent (item 4) |
| twin Higgs Z₂, folded SUSY, little Higgs (same-spin or collective protection) | an independent mirror/partner copy (H_B, t_B; folded SUSY also spin-changing) or an enlarged global group | A1 forbids mirror/twin sectors; antimatter cannot be the copy (item 5) |
| shift symmetry / pNGB Higgs | h a Goldstone of a larger spontaneously broken group | h is the radial mode of H. A pNGB or composite h needs new strong dynamics (LW2 §3: QCD gives 0⁻ Goldstones and a heavy, broad 0⁺; t̄t compositeness needs m_t ≈ 235-246 GeV). BSM. |
| gauge-Higgs unification (H = A₅) | extra dimensions, enlarged gauge group | BSM |
| holomorphy | superfields, which means SUSY | absent |
| classical scale invariance (Bardeen 1995); Gildener-Weinberg | μ² = 0 at tree level; B > 0 | m² = 0 is RG invariant in a mass-independent scheme, but dilatations preserve spin and act on μ², not C. Anomalous. The measured spectrum needs a tree μ² = (88.5 GeV)², and with μ² = 0 the SM has B = −4.4×10⁻³ < 0: no GW minimum, no radiative EWSB. |
| custodial SU(2)_R (incl. the H ↔ H^c swap iσ₂) | none (it is in the SM, approximately) | leaves Tr Φ†Φ invariant for any coefficient; constrains nothing in C (item 5c) |

**Answer to D2.** The hypothesis was: h is its own antiparticle, its Yukawa acts symmetrically on L and R, and bosons carry no chirality, so an antimatter analogue of Weisskopf's protection might hold for the Higgs.
- (a) *Self-conjugacy.* The real h loop is gauge independent and carries the stop sign: 3λ = 0.378, 7.2% of the top term 6y_t² = 5.22 at M_t; all scalars together (h 3λ, G⁰ λ, G± 2λ) give 14.5%. Per real dof h gets 3λ and each Goldstone λ, and the factor 3 is the combinatorics of λh⁴/4, not self-conjugacy. Complex stops are protected in SUSY, and the trace is basis independent (W± = rotated real fields), so self-conjugacy is not what protects or fails to protect. The pure-scalar term δm_h² ∝ λΛ² = (m_h²/2v²)Λ² is proportional to m_h² but multiplied by Λ²/v², not a log. Weisskopf's softening came from δm ∝ m with chiral symmetry restored at m = 0; m_h² → 0 restores only scale symmetry (S6). [computed, `c9_twin_antimatter_out.txt` (E)]
- (b) *L↔R symmetry of y h ψ̄ψ.* Automatic for any Dirac mass, which always pairs L with R; for complex y the phase is removed by rephasing t_R. The top's Λ² term is ∝ |y_t|² either way, and parity itself is broken maximally by the SU(2)_L gauge coupling (9/4 g² in C). The custodial "L↔R" (SU(2)_R) rotates (t_R, b_R), not chirality. [established]
- (c) *Bosons carry no chirality.* True of MSSM scalars too, and of twin scalars. What it shows ('t Hooft) is that no internal linear symmetry protects a scalar bilinear.
- **The two departures.** SM antimatter fails against SUSY because every antimatter operation is spin-preserving (items 1, 4). It fails against twin Higgs, the strongest form of the hypothesis, because an antiparticle is not an independent field: H^c adds no degrees of freedom, the H ↔ H^c swap is an SU(2)_R rotation, and the antitop is already counted in the top loop (item 5). Protection by a discrete exchange needs a second copy of the fields, which the SM does not have. [computed + established]

**Illustration, not claim: how far short the SM falls.** The one-loop Λ² coefficient splits into gauge-independent sector totals (ξ-independent in R_ξ, background R_ξ and Fermi gauges): W sector 3/2 g² + 2λ, Z sector + h 3/4(g²+g'²) + 4λ, fermions −6y_t² − 6y_b² − 2y_τ². Both boson sectors carry the stop sign (spin-statistics, (−1)^{2J}). Their ratio to the fermion term is R = 0.344 at M_t and 0.790 at M_Pl, with R = 1 at 10^22.83 GeV (3-loop, Buttazzo matching; about 10^16 GeV with Jegerlehner's y_t, §5c). [computed]
- **R is not an observable.** It is the ratio of one-loop supertrace coefficients of the Lagrangian. Hard cutoff and Pauli-Villars agree on it (n_V = 3, also dimensional reduction). The d = 2 pole of dimensional regularization, with d − 1 vector polarizations, gives R(M_t) = 0.211 and no crossing below 10^29.9 GeV. In d = 4 MS-bar the term is absent. [computed `calc/c7_regulators_out.txt`]
- **What physical statement R supports.** If a UV completion regulated every SM loop uniformly (heavy copies of all SM fields with SM couplings, PV-style), then δm_h² ∝ C M². A real heavy state with a portal κ|H|²|S|² instead shifts m_h² by about κM_S²/16π², independent of C. So C ≠ 0 is a statement that the SM Lagrangian lacks the coupling relation. It does not measure any SM sensitivity to heavy thresholds, and the SM spectrum contains no heavy threshold to test. [established reasoning]

**Gate 7: falsifiable consistency check (G7, replaces F-b as the gate item).** The no-go says C is not symmetry-enforced to vanish. Its testable consequences are (i) C(M_t) ≠ 0 and (ii) any zero of C(μ) is a transverse crossing, not an RG-invariant locus. `calc/c9_C_measured.py` propagates the PDG 2024 errors on m_t (0.29), m_h (0.11), M_W (0.0133), M_Z (0.0021) and α_s (0.0009):

| determination | C(M_t) | σ | \|C\|/σ |
|---|---|---|---|
| pole-mass form (3/v²)(m_h² + 2M_W² + M_Z² − 4m_t²), PDG errors | −4.068 | 0.020 | 205 |
| same + MC-vs-pole 0.5 GeV on m_t | −4.068 | 0.040 | 103 |
| MS-bar at M_t (Buttazzo NNLO fits), PDG errors + y_t theory 0.0005 | −3.426 | 0.020 | 172 |
| same + MC 0.5 GeV + y_t matching spread 0.003 | −3.426 | 0.050 | 69 |
| MS-bar with Jegerlehner's y_t(M_t) = 0.9005 | −3.070 | | |
| PDG 2026 inputs (CONSTRAINTS C2): pole / MS-bar | −4.071 ± 0.039 / −3.429 ± 0.049 | | 105 / 70 |

- The m_t error dominates. C(M_t) = 0 would need a pole m_t = 96.1 GeV, or y_t(M_t) = 0.547 (κ_t = 0.59) at fixed boson couplings.
- (ii): the transverse crossing is in item 6 (slope/σ ≈ 90 from PDG input errors; scheme-dependent scale).
- **What would falsify the claim:** a determination of m_t, y_t (e.g. κ_t from tt̄h, measured consistent with 1 at the ~10% level, CONSTRAINTS C1) or the boson masses that put C(M_t) at zero within errors; or an evaluation of C(μ) along the measured trajectory with C = 0 and dC/dlnμ = 0 over a range of scales. Either would mean the SM couplings satisfy a relation the enumeration says nothing enforces. Status: the outcome is a retrodiction, already known, but it could have come out otherwise, and no allowed shift of the inputs or the matching (Jegerlehner's included) moves C(M_t) by more than 0.4 against a 3.4 offset. This is a consistency check of the kind a no-go can offer, not a novel prediction. [computed]

**Other checkable items (context, not the gate item):**
- **F-a (verification identity).** The sector totals are ξ-independent in the three gauge families computed (Nielsen identity with independent ξ_W, ξ_Z). Only a calculational error could falsify it.
- **F-b (HKO/Masina-Quiros consistency check, conditional on matching; not a test of this line).** C(M_Pl) = 0 needs M_t* = 169.54 GeV. The measured 172.57 GeV lies 4.1σ from it with Buttazzo's ±0.0005 y_t theory error, and 3.3σ at a spread of 0.003. Both ends rest on two judgement calls (the Δy_t range and the 0.5 GeV MC term). The significance falls to 3σ at Δy_t = 0.0038, 2σ at 0.0074 and 1σ at 0.0164; the spread between published matchings (Buttazzo vs Jegerlehner, 0.038) gives 0.4σ (`calc/c9_symmetry_group_out.txt` (6)). The no-go allows an accidental zero, so F-b cannot test it either way (Referee E).
- **F-c.** μ₀ is set by y_t(M_t). A settled two-loop matching decides between 10^16 and 10^23 GeV (cutoff/PV scheme only).
- **F-d (structural).** No SM-only mechanism yields λ_{H X X} = y_t² for any colour-triplet boson X, or an independent H_B. A colour-triplet scalar or a mirror Higgs at the LHC would be BSM and outside this line.

**What is new** (LITCHECK c4 §2-3, revised c9; novelty of items 1-2 [conjecture], pending LITCHECK):
1. An explanatory assembly of standard ingredients into a no-go for an antimatter analogue of SUSY's protection: the spin-preservation chain plus the symmetry-group enumeration. Each ingredient is textbook (Coleman-Mandula, HLS, 't Hooft naturalness, the Veltman RG flow).
2. The twin-Higgs comparison: the explicit statement and computation that SM antiparticles cannot serve as a same-spin partner because H^c is not an independent field (rank-4 Jacobian, |H|²+|H^c|² = 2|H|², H^c†H ≡ 0), the H ↔ H^c swap is the SU(2)_R element iσ₂, and the counterfactual (independent H_B: 7 Goldstones, κ-independent pNGB curvature; H_B := H^c: m_h² = −4κ).
3. The quantitative reconciliation of Jegerlehner's μ₀ ≈ 10^16 GeV with the ≈10^23 GeV of HKO/MQ: y_t(M_t) alone accounts for the shift (§5c).
4. The explicit ξ-independence of the sector split in three gauge families, and the correction that the d = 2 pole with d − 1 counting gives a different R.

**No step uses antimatter structure as a mechanism.** The antimatter content of the line is the set of operations tested (items 1, 5). Hole-theory and time-ordered forms (§1-3) reproduce covariant results and add nothing (H3).

**Status:** CONTINUE (fix round 4, cycle 9). Negative result for #1 and #4, stated as a strong argument. Referees: C, E (c8) MAJOR, D (c8) MINOR; no fatal finding, no BSM content. Response in §12.

---

Scripts and outputs (all non-referee scripts rerun cycle 9 from inside `calc/`; every output reproduced byte for byte except `symmetry_scan_out.txt` (custodial-limit lines corrected on purpose) and `c7_same_spin_out.txt` (3 added lines narrowing S2):
- `calc/pair_matching.py` → `pair_matching_out.txt` (species table, mode-by-mode, time orderings, SUSY comparison incl. sfermion D-terms)
- `calc/symmetry_scan.py` → `symmetry_scan_out.txt` (symmetry scan, bilinear structure, RG test)
- `calc/matching_running.py` → `matching_running_out.txt` (R(μ), μ₀)
- `calc/c4_rxi_split.py`, `calc/c4_regulator_running.py` (gauge and regulator independence; log-level R4)
- `calc/c5_jegerlehner.py` → `c5_jegerlehner_out.txt` (Jegerlehner vs HKO crossing)
- `calc/c5_mt_budget.py` → `c5_mt_budget_out.txt` (M_t* error budget)
- `calc/c7_same_spin.py` → `c7_same_spin_out.txt` (spin-preservation chain S1-S6)
- `calc/c7_regulators.py` → `c7_regulators_out.txt` (cutoff/PV vs DREG d = 2 pole with d − 1 vector counting)
- `calc/c7_qcd_ewsb.py` → `c7_qcd_ewsb_out.txt` (QCD-condensate EWSB scale)
- `calc/c7_mt_significance.py` → `c7_mt_significance_out.txt` (significance with y_t matching spread)
- `calc/c9_symmetry_group.py` → `c9_symmetry_group_out.txt` (SM symmetry group acting on Higgs-sector operators; GW B; QCD scale factors; F-b vs y_t spread)
- `calc/c9_twin_antimatter.py` → `c9_twin_antimatter_out.txt` (H^c not independent; twin counterfactual; H ↔ H^c = iσ₂ ∈ SU(2)_R; antitop counting; custodial limit with y_b; h self-loop share)
- `calc/c9_C_measured.py` → `c9_C_measured_out.txt` (gate 7: C(M_t) with PDG errors, sign on [M_t, M_Pl], transverse crossing)
- `calc/refA_check.py` … `calc/refD_check.py` (referee checks; not rerun by the fixer)

Inputs come from `tools/sm_inputs.py` (PDG 2024). Running uses `tools/rg_sm.py`: 3 loops for gauge couplings, y_t and λ, and 2 loops for y_b and y_τ, with Buttazzo et al. (arXiv:1307.3536) NNLO matching at M_t. Normalization follows CONSTRAINTS G: C = 6λ + 9/4 g² + 3/4 g'² − 6y_t² = (3/v²)(m_h² + 2M_W² + M_Z² − 4m_t²), δμ² = CΛ²/16π², δm_h² = CΛ²/8π². Prefactors are regulator dependent (H2), so only ratios, signs and zeros are used.

## 1. The SUSY cancellation, and what antimatter language adds (H3)

**Re-expression, not new content.** Sections 1-3 restate the known one-loop result in hole-theory and time-ordered language. In a one-loop vacuum-energy computation every term is a zero-point or Dirac-sea term by construction, so calling the Λ² pieces "pair terms" is a choice of vocabulary (Referee 1 c4 finding 4, accepted). The derived content of the line is in the CLAIM: the gauge-invariant sector split, the no-go of Section 4, and the crossing analysis of Section 5.

### 1a. Top/stop [established; bookkeeping checked in pair_matching.py Parts 2-4]
- Each top chirality state has a complex scalar partner (t̃_L, t̃_R) with the same multiplicity (2 real dof per colour) and the same field-dependent mass coefficient a = y_t²/2.
  - The equal quartics y_t² for t̃_L and t̃_R come from the two F-terms |∂W/∂U|² and |∂W/∂Q|² of the single superpotential term y_t H_u Q U, i.e. from holomorphy.
  - They do not come from an L↔R symmetry of the Yukawa. A Dirac mass always involves both chiralities equally. (Referee 1 c4 finding 7, accepted: the earlier "observation (b) is realized in SUSY" is withdrawn.)
- With m_t̃ = m_t, the stop and top integrands cancel at every loop momentum. This is trivial, because they are the same function with opposite sign (finding 4, accepted).
- Time orderings for an on-shell Higgs: the top's forward and backward (Z-graph) orderings each give −3y²k/4π². The stop seagull, an equal-time stop-antistop vacuum contraction, gives +3y²k/2π² and cancels both. The stop bubbles are log only. The time-ordered pieces agree with the Wick-rotated covariant integrand to 7 digits. [computed]
- The residual is a log.
  - The soft-mass log is −(3y_t²/8π²)(m_Q² + m_U² + A_t²) ln Λ [established, standard; Martin hep-ph/9709356 eq. (1.13) (checked in v7, 2016) gives the generic form m_soft² (λ/16π²) ln(Λ/m_soft); the stop-specific coefficient is verified symbolically in Part 4].
  - The p² (m_h²) log is the Higgs wave-function renormalization, γ_{H_u} ∋ 3y_t²/16π². It is **present in the MSSM too**: non-renormalization does not forbid Kähler renormalization, and no h-t-higgsino vertex exists. (Referee 1 c4 finding 5, accepted; the cycle-4 claim that "the top-higgsino loop removes it" was false and is deleted.)

### 1b. MSSM electroweak sector by charge [computed; pair_matching.py Part 4]
- **Gauge + Higgs subsector only:** the Q = 0 block (Z plus the neutral Higgs scalars against the neutralinos) and the Q = ±1 block (W±, H± against the charginos) each have vanishing field-dependent supertrace.
- **Full MSSM:** the sfermion D-term masses (g'²Y − g²T3)(|H_u⁰|² − |H_d⁰|²)/2 have no fermionic partner term. Per generation they give a Tr M² of (g² + g'²)(v_d² − v_u²)/4 × {1, −3, +3, −1} in the |Q| = {0, 1/3, 2/3, 1} sectors. These cancel only in the sum over the whole generation (Tr Y = Tr T3 = 0), which mixes charge sectors. So **the Q = 0 sector does not cancel on its own in the MSSM**.
- Where the block-by-block cancellation does hold (gauge + Higgs), it follows from [Q_em, SUSY] = 0: superpartners carry the same electric charge, and the mass matrices are block diagonal in Q [established; Martin hep-ph/9709356 §7.4].
- "Neutral" is not "self-conjugate". Sneutrinos are neutral and complex. Neutralinos are Majorana because no conserved charge forbids a Majorana mass, not because Z and h are self-conjugate; a neutral Dirac partner would cancel the same supertrace.
- **The cycle-4 claim "SUSY carries self-conjugacy sector by sector" is withdrawn** (Referee 1 c4 finding 1, accepted in full).

## 2. SM boson sectors against the fermion term

Gauge-invariant grouping (CLAIM table; c4_rxi_split). Values are MS-bar at μ = M_t.

| sector | C | fraction of \|C_ferm\| |
|---|---|---|
| W sector (W±, G±, ghosts) | +0.882 | 0.169 |
| Z sector + h (Z, G⁰, ghosts, h) | +0.916 | 0.175 |
| fermions (top dominates) | −5.223 | 1 |

- **Sign** [computed]: both boson sectors carry the stop sign. This is spin-statistics, (−1)^{2J} in STr, and has nothing to do with charge conjugation. L01 §4.4 shows the trace is basis independent: W± = (W1 ∓ iW2)/√2 is a unitary rotation of two real fields, so "which states are antiparticles" cannot affect C. [computed in L01 `veltman_running.py`]
- **Magnitude** [computed; cutoff/PV scheme, not an observable, see CLAIM]: R = 0.344 at M_t, so the total |C| drops from 5.22 to 3.43. At 10^10 GeV R = 0.508, i.e. the bosons fall short by a factor of 2 there. The cycle-4 text said "3× for μ ≲ 10^10", which was wrong at 10^10 (finding 7).
- **The h self-loop, credited (Referee E c8 finding 3)** [computed, `c9_twin_antimatter_out.txt` (E)]: the real h loop has no ξ in m_h²(φ), carries the stop sign, and gives 3λ = 0.378, 7.2% of the top term 6y_t² = 5.22. All scalars (h 3λ, G⁰ λ, G± 2λ) give 6λ = 0.757, 14.5%. Per real dof, h gets 3λ and each Goldstone λ; the factor 3 is the λh⁴/4 combinatorics, not self-conjugacy.
- **Landau-gauge artefacts, not used in any claim** (finding 6): the "13 boson dof vs 12 stop dof" count, the "mean a per dof = 0.138" and the "4.1 stop-equivalent dof". In unitary gauge the count is 10, and in R_ξ the ghosts enter with negative weight. The small-k negativity of the h + G modes in Part 2 is partly an artefact of the massless Landau-gauge Goldstones.
- **Statements about W⁺W⁻ or G⁺G⁻ separately are gauge dependent** (per-diagram weights (3+ξ)g²/2, −ξg²/2, …; c4_rxi_split). They are not made.
- **The SUSY comparison is about sectors, and they do not match.** In SUSY the colour-triplet top is cancelled within its own sector (stops). The SM version would need a cross-sector cancellation of colourless W/Z/h against the coloured top. The SM has no Yukawa-coupled self-conjugate fermion. Whatever the neutrino-mass mechanism, it contributes to C at order m_ν²/v² ~ 10⁻²⁵, so the conclusion does not depend on it (A2).

## 3. Weisskopf comparison (L01 merged)

| | electron (Weisskopf 1939) | Higgs (SM) |
|---|---|---|
| particle-only states | linear divergence | none with Λ² |
| pair/sea states | cancel the linear piece → log | top sea adds (both orderings −); boson sectors subtract |
| reason | chiral symmetry: δm ∝ m | no symmetry; C ≠ 0 except at μ₀ |
| self-sector term | (none) | h self-loop 3λ = 3m_h²/(2v²): ∝ m_h² but × Λ²/v², not a log; m_h² → 0 restores only scale symmetry |

- The Weisskopf hole-theory reproduction (linear → log, coefficient 3α/2π) is in L01 `calc/weisskopf_ofpt.py`.
- The two top-loop time orderings, both negative and agreeing with the covariant integrand to 8 digits, are in L01 `calc/higgs_top_ofpt.py`. [computed in L01]
- **Channel form of the Veltman condition** (both sides are 2C): Σ_boson sectors n_i ∂²M_i²/∂h² = Σ_fermions n_f ∂²M_f²/∂h², i.e. 3/2 g² + 2λ + 3/4(g² + g'²) + 4λ = 6y_t² + 6y_b² + 2y_τ². In the SM it holds, if at all, only for the total, and only at μ₀.

## 4. The same-spin obstruction (c7_same_spin.py; scan retained from symmetry_scan.py; c9 enumeration and twin section)

**4a. The chain [established theorems; computed checks where marked].** Details for CLAIM items 1, 4, 6. Item 2 (enumeration) is §4c, item 5 (twin) is §4d.
- **S1. Antimatter operations preserve spin.** [computed for spinors; argument for bosons] In the Dirac representation, the script checks that iγ² L* (iγ²)⁻¹ = L for random spinor Lorentz transformations L (max deviation 2.5×10⁻¹⁶). So ψ^c is a (1/2,0)⊕(0,1/2) field like ψ. γ⁰ J γ⁰ = J (parity) and T J* T⁻¹ = −J with T = iγ¹γ³ (time reversal, antiunitary). All of these preserve J² = 3/4. On bosons, φ → φ* and W⁺_μ ↔ −W⁻_μ keep scalars scalar and vectors vector. None changes (−1)^F = (−1)^{2j}. The Dirac sea and Feynman-Stueckelberg readings are not operators on the Hilbert space. They redescribe the same states (H3), and the hole of a spin-1/2 level is spin 1/2. For the SM's Weyl fields, C maps (1/2,0) to (0,1/2): the Lorentz representation is exchanged, spin and statistics are kept (Referee C c7 finding 6). The conclusion needs only J² and (−1)^F.
- **S2. Field-type classes (narrowed c9).** [argument] A *global, homogeneous, linear*, 4D spin- and statistics-preserving field map (C, P, T, CPT, flavour and custodial rotations) preserves the multiset of field types in each monomial, so its invariance conditions stay within each class: y_t (S F F), λ (S⁴). The cycle-7 version stated this for all spin-preserving maps; that is false (Referee C). Local gauge invariance (inhomogeneous), nonlinearly realized symmetries, scale invariance with dimensional transmutation, and a twin Z₂ acting on an enlarged field space all relate couplings across classes or remove the top Λ² term without a spin change. Each is treated in §4c-4d and shown unavailable with SM content. The decisive step is the enumeration of the actual SM symmetry group (§4c).
- **S3. Coleman-Mandula and HLS (scope narrowed c9).** These are S-matrix theorems: they classify symmetries that are unbroken, linearly realized on asymptotic one-particle states, with finitely many particles below any mass and non-trivial analytic scattering. SUSY's protection works when SUSY is broken, a Lagrangian relation can come from a symmetry that never acts on the S-matrix, and gluons are not asymptotic states (CM applies to the hadron/photon S-matrix). The usable output is the algebra classification: any spin-changing symmetry algebra of a 4D relativistic QFT is super-Poincaré or superconformal. Every realization needs new states: linear ones superpartners, nonlinear ones (Volkov & Akulov, PLB 46, 109 (1973)) at least a goldstino. Neutrino-as-goldstino, the one way SM content might seem to fill that role, is excluded by low-energy theorems (de Wit & Freedman, PRL 35, 827 (1975) [from memory, not re-read]). Coleman & Mandula, Phys. Rev. 159, 1251 (1967), restricts the bosonic symmetry algebra of a nontrivial S-matrix with a mass gap to Poincaré ⊕ internal, with internal generators commuting with J. Haag, Łopuszański & Sohnius, Nucl. Phys. B 88, 257 (1975), show that the only graded extension has spin-1/2 odd generators (SUSY), plus conformal symmetry when all particles are massless. C, P and T are discrete and not covered by CM, but S1 checks them directly. Caveat: the SM has massless photons and gluons, so CM's mass-gap assumption does not hold literally. The extra generators HLS allow in the massless case are conformal ones, which also preserve spin, so the conclusion stands [established; the massless extension is not re-derived here]. The script verifies that [J_z, Q_α] = ∓Q_α/2 shifts J_z by 1/2, and that the F-term of W = yHQU gives λ_{H t̃ t̃} = |y|² with m_t = y⟨H⟩, cancelling the top-sector ∂²STr M² (+6y² − 6y² = 0).
- **S4. SM content cannot fill supermultiplets.** Quantum-number scan: Q, u^c, d^c, e^c have no SM boson partner. Gluon, W and B have no SM fermion partner. Only H ~ L* matches. dof are 28 vs 90. [computed]
- **S5. No accidental relation (logic corrected c9, Referee C c7 finding 4).** [computed] One-loop 16π²β_C on C = 0: 33g⁴ + 63/2 g²g'² − 162g²y² + 96g₃²y² + 17g'⁴ − 46g'²y² + 126y⁴. This polynomial has real zeros, and reduction of couplings (Zimmermann, Commun. Math. Phys. 97, 211 (1985); Kubo, Sibold, Zimmermann, Nucl. Phys. B 259, 331 (1985)) gives RG-invariant relations without a symmetry, so the polynomial alone does not exclude an RG-invariant sub-variety of C = 0. What excludes it for the SM is the measured trajectory: C < 0 on [M_t, M_Pl] (max −0.183) and the 3-loop flow crosses zero at μ₀ = 10^22.83 GeV with dC/dlnμ = +0.0203 ± 0.0002 (`c9_C_measured_out.txt`). The one-loop polynomial is scheme independent; the 3-loop crossing scale is not. In SUSY, λ_{H t̃ t̃} = y_t² is preserved by running in DR-bar (not MS-bar) because it is an F-term identity [established].
- **S6. Classical scale invariance (Bardeen, "On naturalness in the standard model", FERMILAB-CONF-95-391-T, 1995 Ontake Summer Institute; report number and title verified on INSPIRE c7, text not read).** In a mass-independent scheme β_{μ²} ∝ μ², so μ² = 0 is RG invariant. This is the SM's own protection of μ² against SM-internal corrections [established]. It is not a SUSY analogue in the sense of the CLAIM. Dilatations commute with J², so they constrain the dimensionful μ² and leave C alone. They are anomalous. The measured spectrum has tree μ² = m_h²/2 ≠ 0. With μ² = 0, the SM CW potential has B = (6M_W⁴ + 3M_Z⁴ − 12m_t⁴)/(64π²v⁴) = −4.4×10⁻³ < 0 and no radiative EWSB (L01: −4.3×10⁻³ with m_h included). Whether μ² is "protected" against heavy thresholds cannot be posed inside the SM, which has none (Referee B c6 finding 1, option (i)) [established reasoning].

**4b. Retained operator scan (symmetry_scan.py) [computed, demoted to illustration].**
- C, P and CP map each Higgs-sector operator to its hermitian conjugate, by definition. h → −h alone forbids the Yukawa unless y_t → −y_t. U(1)_H, chiral U(1)_A, the PQ-like U(1) and custodial O(4) all allow μ²|H|².
- **Custodial limit, corrected c9 (Referee E c8 finding 2).** The cycle-8 script set only g' → 0 and dropped y_b. The custodial limit needs g' → 0 and y_t = y_b = y, giving C = 9/4 g² + 6λ − 12y² (−8.74 at M_t with y = y_t), further from zero, with no relation imposed. symmetry_scan.py now prints this.
- The Z₂ (h → −h, t_R → −t_R) is the SU(2)_L centre element times (−1)^F (refB_check). It is trivial, a gauge transformation times a 2π rotation, and is no longer cited as protecting anything. m_t is protected by the chiral U(1) of t_R, broken only by y_t.
- "C is invariant under every candidate" does not by itself prove anything for symmetries relating different fields: SUSY leaves the singlet C invariant and still forces λ_{Ht̃t̃} = y_t² (Referee A c6 finding 3). The general arguments are S2-S5.
- 't Hooft (NATO Sci. Ser. B 59, 135 (1980)): spin-0 bilinears φ*φ and h² are invariant under every linear internal symmetry, for real and complex scalars alike. A Weyl mass ψψ is not. This is observation (c), and it holds in the MSSM too. It rules out internal-symmetry protection of h²; it is not the point where the SM departs from SUSY.

**4c. The symmetry group of the SM Lagrangian (c9; `calc/c9_symmetry_group_out.txt`) [computed + established].** This replaces S2 as the load-bearing step.

| symmetry | status in SM | action on (λ, g, g', y_t, y_b) | relates distinct operators? |
|---|---|---|---|
| SU(3)×SU(2)×U(1)_Y gauge | exact (local) | identity | ties the gauge vertices of each factor to one g; \|H\|⁴ and (Q†H^c)t_R separately invariant |
| U(1)_B, U(1)_{Le,Lμ,Lτ} | accidental; B+L anomalous | identity | no |
| t_R, b_R (flavour) rephasings | broken only by Yukawas (spurions) | y → e^{iα}y | no |
| custodial SU(2)_R | approximate (g' = 0, y_t = y_b) | identity on λ, g | no; the H ↔ H^c swap is its element iσ₂ (§4d) |
| C, P, CP, T | each broken (C, P by SU(2)_L; CP by CKM) | y → y* or none | no; each operator → its h.c. |
| CPT | exact | identity on hermitian L | no |
| classical scale invariance | broken by μ², anomalous | identity on dimensionless couplings | no (acts on μ²) |

Every element maps each Higgs-sector operator to itself (checked with random group elements), so each acts diagonally on coupling space and C is an invariant, uncharged function. A symmetry can force a relation between two couplings only by mapping one operator into a different one (SUSY: (Q†H^c)t_R ↔ |H|²|t̃|²; twin: |H_A|² ↔ |H_B|²). No SM element does.

Counterexample classes to the old S2 (Referee C c8), each with why it is unavailable within SM content:
- **Gauge invariance.** It is inhomogeneous (A → A + ∂α) and does tie couplings across field-type classes: the V S S, V V S S, V F F, V³ and V⁴ vertices of one factor share one g. But |H|⁴ and (Q†H^c)t_R are each gauge invariant on their own (checked numerically), so any values of λ and y_t are allowed. A gauge symmetry that tied them would have to put H in a gauge multiplet (gauge-Higgs unification), which needs extra dimensions or an enlarged gauge group; A1 fixes the SM group.
- **Nonlinear / pNGB realization.** In a coset such as SO(5)/SO(4) the h-VV and hh-VV couplings, and h-tt and hh-tt, are fixed together, and h's mass is shielded from the Λ² term because h is a Goldstone. In the SM the scalar manifold is the 4 real components of H with an O(4)-invariant potential; h is the radial mode and G±, G⁰ are the only Goldstones, all eaten. A larger coset needs new fields or new strong dynamics. QCD gives 0⁻ Goldstones and a broad 0⁺, and t̄t condensation would need m_t ≈ 235-246 GeV (LW2 §3).
- **Scale invariance plus Gildener-Weinberg** (Gildener & Weinberg, PRD 13, 3333 (1976)). With tree μ² = 0, dimensional transmutation fixes the scalon mass m² = 8Bv² by a relation among fourth powers of masses (STr M⁴), not C. With SM content B = (6M_W⁴ + 3M_Z⁴ − 12m_t⁴)/(64π²v⁴) = −4.39×10⁻³ < 0, so the GW vacuum does not exist; the measured μ² ≠ 0 anyway (S6).
- **Twin Z₂.** A discrete, linear, spin-preserving exchange between the SM and an independent copy. It never ties y_t to λ: it ties y_t^A to y_t^B and makes the Λ² term U(4) invariant. Unavailable because A1 forbids mirror sectors and because SM antimatter cannot be the copy (§4d).

**4d. Same-spin protection: twin Higgs, and why SM antimatter cannot be the twin (c9; `calc/c9_twin_antimatter_out.txt`) [computed; twin mechanism established, Chacko, Goh, Harnik, PRL 96, 231802 (2006), hep-ph/0506256].**

*The twin mechanism.* A Z₂ maps every SM field to an independent mirror copy (H_A ↔ H_B, t_A ↔ t_B, gauge fields likewise). With y_t^A = y_t^B the two top loops give a Λ² term κ(|H_A|² + |H_B|²), invariant under U(4) acting on the 8 real components. With ⟨H_B⟩ = f/√2, U(4) → U(3) gives 7 Goldstones (script: mass eigenvalues {0: 7, 2λf²: 1}); 3 are eaten by the twin W, Z, and the SM doublet sits in the remaining 4. The Λ² term sets only the radial mode. A Z₂-symmetric U(4)-breaking quartic δ(|H_A|⁴ + |H_B|⁴), generated at the log level, gives the light h its curvature d²V/dθ² = δf⁴(−8 sin⁴θ + 8 sin²θ − 1), independent of κ. So the top's Λ² term cancels between our top and the twin top, with partners of the same spin. Related routes: little Higgs collective breaking (Arkani-Hamed, Cohen, Georgi, PLB 513, 232 (2001), hep-ph/0105239) and folded SUSY (Burdman, Chacko, Goh, Harnik, JHEP 0702, 009 (2007), hep-ph/0609152; spin-changing, uncoloured partners). All need new fields.

*Why SM antimatter cannot be the twin* (the strongest form of the D2 hypothesis: a particle ↔ antiparticle exchange acting like the twin Z₂):
1. **H^c is not an independent field.** H^c = iσ₂H*. The 8 real components of (H, H^c) have Jacobian rank 4 with respect to H's 4 real fields. |H^c|² = |H|², H^c†H ≡ 0, and (UH)^c = U H^c for U ∈ SU(2). The space of gauge-invariant Higgs bilinears is 1-dimensional (|H|²), against 4 for an independent pair (|H_A|², |H_B|², H_A†H_B, h.c.). A twin Z₂ relates the coefficients of two different invariants; C, CP and CPT map |H|² to itself and relate nothing.
2. **The counterfactual.** Setting H_B := H^c in the twin potential gives κ(|H|² + |H^c|²) + λ(…)² = κh² + λh⁴ on H = (h, 0)/√2. The 4×4 mass matrix has eigenvalues {0, 0, 0, −4κ}: the three SM Goldstones (eaten) and h as the radial mode with m_h² = −4κ ∝ Λ². There is no spare angular direction to host a pNGB. The "doubling" 2κ|H|² also double-counts a single loop.
3. **H ↔ H^c is custodial, not a twin exchange.** In the bidoublet Φ = (H^c, H), the swap (H^c, H) → (H, −H^c) is Φ → ΦR† with R = iσ₂, det R = 1, R ∈ SU(2)_R. (−H^c)^c = H, so the result is again a bidoublet. Tr Φ†Φ = 2|H|² is invariant for any coefficient: the swap is a continuous, internal, spin-preserving rotation already listed in §4c, and imposes no condition on C. SU(2)_R rotates (t_R, b_R); it is not chirality L ↔ R.
4. **The antitop is the same Dirac field as the top.** C_top = (1/2)∂²_h[−4N_c m_t²(h)] = −6y_t², where 4 = 2 spin × (t, t̄) per colour. The antitop states are already 2 of the 4. C, CP and CPT map the top loop into itself, relating y_t to y_t: an identity. A twin top needs its own field t_B with its own coupling to H_B.

*Conclusion for D2 [computed + established].* The twin mechanism shows that spin preservation alone is not the obstruction: a spin-preserving exchange symmetry can cancel the top's Λ² term. What it needs is a second, independent copy of the fields. Antimatter is not one. The antiparticle of each SM field is a component of the same field (H^c from H, t̄ from t), so particle ↔ antiparticle maps are automorphisms of the existing field space and cannot enlarge it. The hypothesis fails against twin Higgs for this reason, and against SUSY because antimatter operations preserve spin.

## 5. Running, μ₀, and the M_t check

### 5a. R(μ) [computed; matching_running.py, c4_rxi_split.py]

| log₁₀ μ | Z+h sector | W sector | fermions | R |
|---|---|---|---|---|
| 2.24 (M_t) | 0.916 | 0.882 | 5.223 | 0.344 |
| 10 | 0.375 | 0.492 | 1.706 | 0.508 |
| 16 | 0.315 | 0.393 | 1.061 | 0.667 |
| 19.09 (M_Pl) | 0.321 | 0.363 | 0.866 | 0.790 |
| 22.83 | 0.352 | 0.337 | 0.689 | 1.000 |

- μ₀ = 10^22.83 at 3 loops, 10^22.98 at 2 loops and 10^26.79 at 1 loop.
- Input shifts: M_t ± 0.29 GeV moves μ₀ by ±0.35 decades, α_s ± 0.0009 by ∓0.52, M_h ± 0.11 by ∓0.04.
- Consistent with HKO (10^23 GeV at M_t = 173 GeV) and with Masina-Quiros ("slightly trans-Planckian").
- λ < 0 above 10^10.7 GeV, so the 4λ and 2λ pieces turn negative there. The near-equality of the two sectors at μ₀ (0.352 vs 0.337) has no mechanism behind it (H1).

### 5b. M_t* for C(M_Pl) = 0 and its significance [computed; c5_mt_budget.py]

C(M_Pl) = 0 needs M_t* = 169.54 GeV. The measured value is 172.57 GeV, 3.03 GeV above (3.035). Equivalent shifts in M_t:

| source | ΔM_t (GeV) |
|---|---|
| α_s(M_Z) ± 0.0009 (PDG 2024) [computed] | 0.42 |
| MC mass vs pole mass interpretation [Hoang, arXiv:2004.12915, Ann. Rev. Nucl. Part. Sci. 70 (2020): MC-mass measurements carry ~0.5 GeV and the relation to field-theory masses is unresolved] | 0.50 |
| experimental direct M_t (PDG 2024) | 0.29 |
| RGE order, 2-loop vs 3-loop [computed] | 0.13 |
| pole-mass renormalon ambiguity [Beneke, Marquard, Nason, Steinhauser, arXiv:1605.03609, PLB 775 (2017) 63: ~110 MeV] | 0.11 |
| y_t matching theory ± 0.0005 [Buttazzo et al. 1307.3536; value as transcribed, uncertain] | 0.09 |
| Λ² coefficient, 1-loop vs 2-loop: C1 → C2 moves μ₀ by 0.10 decades (Jegerlehner 1304.7813), at 1.22 dec/GeV [lit + computed] | 0.09 |
| M_h ± 0.11 [computed] | 0.04 |
| curvature of the linear Buttazzo y_t fit 3 GeV from its centre [computed, crude] | < 0.001 |
| **quadrature total** | **0.74** |

- **3.3-4.1σ** within Buttazzo-type matching. 4.1σ is with Buttazzo's ±0.0005 y_t matching error; an intermediate spread of 0.003 gives 3.3σ (`calc/c7_mt_significance_out.txt`, Referee A c6 finding 5). The cycle-4 "10.5σ" (experimental error only) stays withdrawn.
- **The range rests on two judgement calls** (Referee D c8 finding 5): the Δy_t range and the 0.5 GeV MC term. No published two-loop matching spread of 0.003 was read; it is not justified independently, so the range is widened instead (`calc/c9_symmetry_group_out.txt` (6)): the significance falls to 3σ at Δy_t = 0.0038, 2σ at 0.0074, 1σ at 0.0164, and 0.4σ at the Buttazzo-Jegerlehner spread 0.038. F-b is no longer the gate-7 item (CLAIM, G7), so nothing in the CLAIM depends on where in this range the truth lies.
- This restates the HKO and Masina-Quiros result that the SM does not meet the Veltman condition at M_Pl. Here it is updated to PDG 2024 inputs with an error budget. It is not a test of any mechanism proposed by this line (finding 3a, accepted).
- Not in the budget: the Jegerlehner matching spread (Section 5c), equivalent to about 6.8 GeV. If that matching is admitted, C(M_Pl) = 0 is not excluded. The dominant uncertainty is the on-shell → MS-bar y_t conversion.
- C(M_Pl) is a cutoff/PV-scheme coefficient evaluated at a non-SM (gravitational) scale (Referee B c6 finding 8).
- Further scheme caveat [established]: beyond one loop the Λ² coefficient is scheme dependent. Einhorn & Jones, PRD 46, 5206 (1992); Al-sarhi, Jack, Jones, Z. Phys. C 55, 283 (1992) and Nucl. Phys. B 345, 431 (1990); Kleppe, hep-th/9209124 (regularization dependence, disputes an Al-sarhi-Jack-Jones result); D.R.T. Jones, PRD 88, 098301 (2013), arXiv:1309.7335, who disputes HKO's two-loop coefficient. The C1 → C2 row above is one estimate of that spread, not a bound.

### 5c. Jegerlehner's μ₀ ≈ 10^16-17 GeV vs 10^22.83 GeV [computed; c5_jegerlehner.py]

**Sources.**
- Jegerlehner, Acta Phys. Polon. B 45, 1167 (2014), arXiv:1304.7813, Table 1 and text: μ₀ ≈ 1.4×10^16 GeV for C1 and 1.1×10^16 GeV for C2. Inputs: M_t = 173.5 GeV, M_H = 126 GeV, α_s = 0.1184. MS-bar couplings come from his on-shell → MS-bar matching with tadpoles included.
- Jegerlehner, arXiv:1305.6652 (preprint): ≈7×10^16 GeV in the text, ~10^17 in the abstract.
- Note (Referee D c8 finding 4): the arXiv/DESY abstract of 1304.7813 itself also quotes μ₀ ~ 7×10^16 GeV, while its Table 1 gives 1.1-1.4×10^16 GeV. So 7×10^16 is not specific to 1305.6652; the abstract and the table of 1304.7813 differ (or the versions do; not resolved here). Conclusions are unaffected: 10^16-10^17 GeV either way.
- His normalization: V ∋ λ_J φ⁴/24 with φ = √2|H|, so λ = λ_J/6 and C1 = 2C. The script checks this on his M_Z row, which gives 2C = −6.775 against his −6.768. His M_t row is internally off by 0.06, so the M_Z row is used as the reference.

| input set | log₁₀ μ₀ (3-loop RGE) |
|---|---|
| (A) Buttazzo matching, PDG 2024 | 22.83 |
| (B) Buttazzo matching, Jegerlehner's physical inputs (173.5, 126, 0.1184) | 23.46 |
| (J) Jegerlehner Table 1 couplings at M_Z, our RGEs | **16.11** (his 16.15) |
| (J) from his M_t row | 17.07 |
| (B) with only y_t(M_t) replaced by his 0.9002 | 15.68 |
| (B) with only λ replaced | 24.18 |
| (B) with only g' replaced | 24.29 |
| (B) with all five couplings replaced | 17.06 |

Starting from his M_Z row, our runner also reproduces his M_Pl couplings: y_t 0.3500 vs his 0.3510, λ_J 0.1426 vs 0.1405, g₂ 0.5063 vs 0.5068, g' 0.4597 vs 0.4589.

**Resolution of each candidate cause:**
- **y_t matching: this is the cause.** At equal physical inputs, his y_t(M_t) = 0.900 against Buttazzo's 0.938 (Δy_t = −0.038, about −6.8 GeV equivalent in M_t). This alone moves μ₀ by 7.8 decades. His λ and g' differences push the other way, by less than a decade.
  - On the PDG 2024 baseline, y_t(M_t) = 0.9005 puts μ₀ at 1.4×10^16 GeV, 0.9042 at 7×10^16 GeV (reproducing L01), and 0.9153 at M_Pl.
  - Jegerlehner states this cause himself: the difference with HKO "originates from a different estimate of the MS top quark Yukawa coupling" (1304.7813, Introduction).
- **MS-bar vs on-shell: not a separate cause.** Both analyses run MS-bar couplings. The difference is entirely in how on-shell inputs are converted to the MS-bar y_t (his tadpole-inclusive one-loop matching against Buttazzo's NNLO fits).
- **Loop order: not the cause here.** Both use 3-loop running. On his couplings, 2-loop running gives 16.29. With 1-loop running his couplings would give 10^21.1 instead, a 5-decade shift, so the RGE loop order matters a lot in general.
- **Λ² coefficient order:** C1 vs C2 is 0.1 decades.
- **Physical inputs** (M_t, α_s, M_H): 0.6 decades (A → B).

**Which matching is right** is a precision-EW question outside this line. Bednyakov, Kniehl, Pikelner, Veretin, PRL 115, 201802 (2015), arXiv:1507.08833, do a gauge-independent two-loop matching. Their abstract frames absolute vacuum stability as an upper bound on M_t; the numerical value was not checked here. Jegerlehner's matching gives λ > 0 up to M_Pl automatically.

**Consequence for this line:** μ₀ is conditional on the matching. CLAIM items 1-5 and 7 do not depend on it. Item 6 and the R illustration are quoted for Buttazzo matching, with the Jegerlehner crossing (10^16.15 GeV, slope +0.024) given alongside; G7 holds under either (C(M_t) = −3.43 or −3.07). With Jegerlehner's couplings R(M_t) ≈ 0.37, so the qualitative statement "the bosons cancel about a third at M_t" is unchanged.

### 5d. Log-level analogue R4 [computed in c4; interpretation H1]
- R4 is the gauge-invariant λ⁰ and λ² part of the STr M⁴ φ⁴ coefficient.
- R4 = 0.138 at M_t and 1.113 at M_Pl, crossing 1 at 10^18.19 GeV. This is the known near-criticality of λ, i.e. β_λ ≈ 0 (Buttazzo et al.), not a new matching.

## 6. Verdict

**Holds** [established theorems plus computed checks; regulator independent]:
- Every SM antimatter operation preserves spin and statistics (S1). Every element of the SM Lagrangian's symmetry group acts diagonally on (λ, g, g', y_t, y_b), so none relates y_t to λ or g (§4c); gauge invariance, pNGB, Gildener-Weinberg and twin-Z₂ routes need non-SM content (§4c). The only spin-changing symmetry algebra is SUSY, which SM content cannot realize (S3-S4). SM antimatter cannot be a twin: H^c is not an independent field, H ↔ H^c is SU(2)_R, the antitop is in the top loop (§4d). The measured C(μ) is non-zero at M_t (≥ 69σ) and crosses zero only transversally (S5, G7). Scale invariance acts on μ², not C, and is broken in the measured SM (S6). [Strong argument over the known mechanism classes, not a formal proof.]
- SUSY #4: no radiative EWSB in the SM. The only SM antimatter-condensate EWSB (⟨q̄q⟩) gives M_W ≈ 30 MeV (one doublet) to 52 MeV [approx] (three).

**Illustration** [computed, cutoff/PV only, no observable]: R = 0.344 at M_t and 0.790 at M_Pl, R = 1 at 10^22.83 GeV (Buttazzo) or about 10^16 GeV (Jegerlehner). DREG d = 2 pole: R(M_t) = 0.211.

**Not claimed:** any physical reading of μ₀ [speculation, outside SM scope]; that R measures sensitivity to heavy thresholds; that the scan of §4b proves anything by itself.

**Open:**
- LITCHECK of novelty items 1-2 (the assembled no-go; "antiparticles cannot be the twin because H^c is not independent").
- Whether a reformulation (A3) could tie λ, g, g' to y_t without its extra high-scale relations (A3.2). It would need a map between distinct operators (S ↔ F, S ↔ V, or an independent partner copy), i.e. SUSY, gauge-Higgs or twin content, so none is expected [conjecture].

## 7. Merged from L01-weisskopf-hierarchy (by reference)

L01 is support for this line, and L01b is the single line for SUSY #1 and #4. Calculations reused, all under `lines/L01-weisskopf-hierarchy/calc/` (rerun in a scratch copy, cycle 5):
- `weisskopf_ofpt.py`: hole-theory electron self-energy. The linear divergence cancels between particle-only and sea terms, leaving the covariant log 3α/2π. Chiral symmetry is the covariant reason.
- `higgs_top_ofpt.py`: top-loop time orderings (forward h → t t̄ and backward Z-graph), both negative. They agree with the covariant integrand to 8 digits. Also checked: Im Σ = m_h Γ(h → f f̄) and the light-fermion threshold structure.
- `veltman_running.py`: normalization δm_h² = CΛ²/8π² with the tadpole included, and the basis-independence of the trace (charged pair = rotated real fields).
- `cw_radiative_ewsb.py`: **SUSY #4.**
  - Coleman-Weinberg: with the tree mass term set to zero, B = −4.3×10⁻³ < 0, so the stationary point is a maximum and there is no radiative EWSB. The top threshold is 78.6 GeV, and W, Z alone give m_h = 9.8 GeV.
  - In MS-bar β(m²) ∝ m² at all orders, so the sign of m² is RG invariant and there is no RG-driven sign flip of the kind stop soft masses produce in the MSSM.
  - [established classics: Coleman-Weinberg PRD 7, 1888 (1973); Weinberg PRL 36, 294 (1976); Linde JETP Lett. 23, 64 (1976); reproduced in L01]
- **QCD-condensate EWSB (cycle 7, Referee B c6 finding 6)** [established, Quigg & Shrock, PRD 79, 096002 (2009), arXiv:0901.3958; computed `calc/c7_qcd_ewsb_out.txt`]. ⟨q̄_L q_R⟩ ≠ 0 has I = 1/2 and breaks SU(2)_L × U(1)_Y → U(1)_em; the pions are partly eaten. M_W = g√n_d f_π/2 = 30.1 MeV (n_d = 1) or 52.1 MeV (Higgs off, three massless doublets, f_π held at 92.1 MeV [approx]), M_Z = M_W/cos θ_W. In the real SM it adds f_π²/v² = 1.4×10⁻⁷ to v² (5.6 keV on M_W). This is an SM EWSB mechanism built from quark-antiquark pairs, and it is too small in scale by v/f_π ≈ 2700 (n_d = 1) or v/(√3 f_π) ≈ 1540 (n_d = 3) (`calc/c9_symmetry_group_out.txt` (5)). The CW and RG statements above use no antimatter structure, and β(m²) ∝ m² holds in a mass-independent scheme with no heavy thresholds.
- L01's open issue m(M_Pl) = 139.4 vs 129.4 GeV in `tools/rg_sm.py` affects only the dimensionful m², which this line does not use.

## 8. Citations
- Weisskopf, Phys. Rev. 56, 72 (1939)
- Veltman, Acta Phys. Polon. B 12, 437 (1981)
- 't Hooft, NATO Sci. Ser. B 59, 135 (1980)
- Coleman & Weinberg, PRD 7, 1888 (1973); Weinberg, PRL 36, 294 (1976); Linde, JETP Lett. 23, 64 (1976) [via L01 LITCHECK]
- Einhorn & Jones, PRD 46, 5206 (1992)
- Al-sarhi, Jack, Jones, "Quadratic divergences in gauge theories", Z. Phys. C 55, 283 (1992); "Quadratic divergences and dimensional regularization in two-dimensions and four-dimensions", Nucl. Phys. B 345, 431 (1990) [both verified on INSPIRE c7; no arXiv number; content not read]
- G. Kleppe, "Regularization dependence of quadratic divergence cancellations", arXiv:hep-th/9209124 [abstract read c7; previously mis-attributed to Al-sarhi-Jack-Jones]
- W. A. Bardeen, "On naturalness in the standard model", FERMILAB-CONF-95-391-T (1995) [title and report number verified on INSPIRE c7; text not read]
- S. Coleman & J. Mandula, Phys. Rev. 159, 1251 (1967); R. Haag, J. Łopuszański, M. Sohnius, Nucl. Phys. B 88, 257 (1975) [standard; not re-read]
- C. Quigg & R. Shrock, PRD 79, 096002 (2009), arXiv:0901.3958 [abstract verified c7]
- Line LW2-chiral-partner-protection, WORK.md §3 (pNGB/composite Higgs needs BSM dynamics)
- D.R.T. Jones, PRD 88, 098301 (2013), arXiv:1309.7335 [via L01 LITCHECK]
- Martin, "A Supersymmetry Primer", arXiv:hep-ph/9709356, eq. (1.13) [verified in v7, 27 Jan 2016], §7.4
- Hamada, Kawai, Oda, PRD 87, 053009 (2013), arXiv:1210.2538; erratum PRD 89, 059901 (2014)
- Masina & Quiros, PRD 88, 093003 (2013), arXiv:1308.1242
- Jegerlehner, Acta Phys. Polon. B 45, 1167 (2014), arXiv:1304.7813 [Table 1 and text read this cycle]
- Jegerlehner, arXiv:1305.6652 (preprint) [abstract checked]
- Buttazzo et al., JHEP 1312, 089 (2013), arXiv:1307.3536
- Bednyakov, Kniehl, Pikelner, Veretin, PRL 115, 201802 (2015), arXiv:1507.08833 [abstract only]
- Hoang, "What is the top quark mass?", Ann. Rev. Nucl. Part. Sci. 70 (2020), arXiv:2004.12915 [abstract]
- Beneke, Marquard, Nason, Steinhauser, PLB 775 (2017) 63, arXiv:1605.03609 [abstract; journal from DOI 10.1016/j.physletb.2017.10.054]
- Nielsen, NPB 101, 173 (1975); Caswell & Wilczek, PLB 49, 291 (1974) [used in c4 calculator section]
- Kolda & Murayama, hep-ph/0003170 [via CONSTRAINTS G]
- Added c9 (standard references, cited from memory, not re-read this cycle; LITCHECK should confirm):
  - Z. Chacko, H.-S. Goh, R. Harnik, "The Twin Higgs: Natural Electroweak Breaking from Mirror Symmetry", PRL 96, 231802 (2006), hep-ph/0506256
  - N. Arkani-Hamed, A. G. Cohen, H. Georgi, "Electroweak symmetry breaking from dimensional deconstruction", PLB 513, 232 (2001), hep-ph/0105239
  - G. Burdman, Z. Chacko, H.-S. Goh, R. Harnik, "Folded supersymmetry and the LEP paradox", JHEP 0702, 009 (2007), hep-ph/0609152
  - E. Gildener & S. Weinberg, "Symmetry breaking and scalar bosons", PRD 13, 3333 (1976)
  - W. Zimmermann, "Reduction in the number of coupling parameters", Commun. Math. Phys. 97, 211 (1985); J. Kubo, K. Sibold, W. Zimmermann, Nucl. Phys. B 259, 331 (1985)
  - D. V. Volkov & V. P. Akulov, PLB 46, 109 (1973)
  - B. de Wit & D. Z. Freedman, "Phenomenology of Goldstone neutrinos", PRL 35, 827 (1975)

## 9. Response to referee 1 (cycle 4)

| # | finding | response |
|---|---|---|
| 1 | MSSM sector-by-sector cancellation fails with sfermion D-terms; trivial where true | **Accepted.** Sfermion D-terms added to pair_matching.py Part 4: Q = 0 sector per generation (g²+g'²)(v_d²−v_u²)/4 ≠ 0. Claim restricted to the gauge+Higgs subsector and attributed to [Q_em, SUSY] = 0 (Martin §7.4). The self-conjugacy reading is dropped, §1b retagged [computed], and Verdict Holds-2 deleted. |
| 2 | "self-conjugacy blocks protection" is a non sequitur | **Accepted.** §4 rewritten: φ*φ is invariant for complex scalars too, so the obstruction is the spin-0 bilinear structure, (c) alone. [Superseded c7: see §11, A1.] symmetry_scan.py (2) now prints the complex-scalar, real-scalar, Weyl and Dirac cases. |
| 3a | M_t check is not a test of the line | **Accepted.** Reframed as a consistency statement credited to HKO and Masina-Quiros (F-b). The line-specific check is now F-a (sector ξ-independence). |
| 3b | significance overstated | **Accepted.** Full budget in c5_mt_budget.py: 0.74 GeV, 4.1σ. Close to the referee's 3.5-4σ. |
| 3c | scheme ambiguity | **Partly accepted.** RGE order (0.13 GeV) and C1→C2 (0.09 GeV) are included. The larger scheme issue turns out to be the y_t matching (Jegerlehner, ~6.8 GeV equivalent), now stated explicitly. A full two-loop Λ² treatment is not done; Jones 1309.7335 disputes the HKO coefficient, so no single two-loop number is authoritative. |
| 4 | "Holds" relabels the Veltman coefficient (H3) | **Accepted.** §1 opens with an explicit re-expression disclaimer. The CLAIM rests on the gauge-invariant split, the (c) obstruction and the crossing analysis. |
| 5 | top-higgsino removes the p² log: false | **Accepted.** Deleted from WORK and the script. The p² log is the Higgs anomalous dimension and is present in the MSSM. |
| 6 | gauge dependence | **Accepted.** The ξ-independence of the sector totals is proven in c4_rxi_split.py. The dof counts and per-dof averages are labelled Landau-gauge in the WORK and the script. |
| 7 | loose statements | **Accepted.** Script string fixed ("stop sign for k ≳ m_t only"); 3× → 2× at 10^10; (b)-in-SUSY replaced by F-term holomorphy; C/P/CP marked as by definition, with non-gauge-invariant operators dropped for conjugating maps; [computed] tag introduced. |
| 8 | citations | **Accepted.** MQ journal ref, HKO erratum, Jones 1309.7335 and Al-sarhi-Jack-Jones added. |
| A2 | Dirac y_ν assumption | **Accepted.** Rephrased as mechanism-insensitive (m_ν²/v² ~ 10⁻²⁵). |

**Disagreements and refinements:**
- 3c: the referee names the Λ² loop order and RGE order as the main fragility. Within Buttazzo matching these are sub-0.15 GeV effects. The 1-loop vs 3-loop RGE spread of μ₀ (26.8 vs 22.8) reflects 1-loop running being inadequate, not a scheme ambiguity of the 3-loop result. The dominant real ambiguity is the y_t matching (Section 5c).
- Finding 4 / gate item 6: the referee concludes that after the fixes the line is "largely a restatement". Agreed for the Veltman numerics. The line's claim to novelty is limited to the three "What is new" items, and it is offered as a negative result.

## LITCHECK (cycle 4) items addressed
- Martin primer: the stop-specific log is now cited as "standard", with eq. (1.13) as the generic form.
- HKO erratum and MQ journal ref added.
- Jegerlehner spread resolved quantitatively (§5c).
- Masina-Quiros Fig. 1 credited for the per-piece decomposition (§CLAIM "What is new" 3).
- Martin §7.4 credited for charge-block sum rules (§1b).
- Novelty claims limited to LITCHECK 2c (framing) plus the Jegerlehner reconciliation and the ξ-independence check.

## 10. CONSTRAINTS checklist (revised cycle 9; every entry addressed)
- **A1:** Pass. SM fields only in every mechanism. Stops, superpotential and supermultiplets appear only as the comparison target (pair_matching.py Parts 3-4, c7_same_spin S3-S4). Composite/pNGB Higgs, gauge-Higgs unification, superfields, twin/mirror sectors (H_B, t_B), little Higgs and folded SUSY are named only as routes that would need BSM content (route table, §4c-4d); the independent H_B in c9_twin_antimatter.py is a counterfactual computed to show what antimatter lacks, and none is used.
- **A2:** Pass. Neutrino masses are not used. Any mechanism contributes at most m_ν²/v² ~ 10⁻²⁵ to C.
- **A3:** Pass. No reformulation is used. Hole theory and time orderings are bookkeeping, checked against covariant integrands. In step 1 the Dirac-sea and Feynman-Stueckelberg pictures enter only as members of the set of antimatter operations tested, and are shown to preserve spin.
- **B1-B8:** Pass. CPT is used as an exact symmetry (step 1). Particle and antiparticle enter every C_i identically. No particle/antiparticle asymmetry is used.
- **B9, B10:** Pass. CP violation is not used.
- **C1, C2:** Pass. PDG 2024 inputs via tools/sm_inputs.py. PDG 2026 (m_t 172.60(27), M_W 80.3625(77), m_H 125.13(11)) gives C(M_t) = −4.071 ± 0.039 (pole) and −3.429 ± 0.049 (MS-bar), against −4.068 and −3.426 with PDG 2024 (c9_C_measured); M_t − M_t* moves by a few 0.01 GeV (Referee D c8), well inside the budget. F-b is quoted with its widened y_t-spread dependence and as not excluded under Jegerlehner matching. G7 uses C1/C2 inputs with their full errors.
- **C3:** Pass. Step 3 explains the absence of superpartner signatures trivially: the line uses none. It also explains why the SM cannot reproduce SUSY's cancellation without them.
- **C4:** Pass. No g−2 claim.
- **D:** Pass. Couplings from tools/, 3-loop running (2-loop for y_b, y_τ), stated.
- **E1, E5:** Not applicable. No dark-matter claim (SUSY #3 removed from the experiment by D1).
- **E2-E4, E6-E10:** Not applicable. No cosmology or baryogenesis claims. The QCD condensate (item 6) is a T = 0 statement; E10's crossover fact is not touched.
- **F1-F3:** Pass. No baryon-number violation.
- **G:** Pass. Normalization as in CONSTRAINTS G. The absence of Λ² in d = 4 DR is stated in the CLAIM, together with "R is not an observable".
- **H1:** Pass. Flagged as having no mechanism: the near-equality of the sectors at μ₀, the R4 crossing and the Landau-gauge dof counts.
- **H2:** Pass for the claim; fails for R by design. The no-go (items 1-5) is regulator independent: it concerns symmetries of the Lagrangian. R agrees in hard cutoff and PV (and DRED) only. The DREG d = 2 pole with d − 1 vector counting gives 0.211 at M_t (c7_regulators), so R is labelled scheme dependent. A 4D hard cutoff on gauge loops is not gauge invariant; its agreement with PV holds for the effective-potential momentum routing.
- **H3:** Pass. Antimatter structure enters as the set of operations tested in step 1, and the result (they preserve spin) is a covariant statement. Hole-theory forms are re-expressions.
- **H4:** Pass. 14 line scripts in calc/ (11 earlier plus c9_symmetry_group, c9_twin_antimatter, c9_C_measured), all rerun in cycle 9 from inside calc/ with saved outputs; the 11 earlier outputs reproduce byte for byte except the intentional changes to symmetry_scan_out.txt (custodial limit) and c7_same_spin_out.txt (S2 narrowing note). Referee scripts refA-refD are left as committed. L01 scripts are referenced by path.

## 11. Response to referees A and B (cycle 6)

| ref | # | finding | response |
|---|---|---|---|
| A | 1 | "fails at (c) alone" is a non sequitur; MSSM scalars have no chirality either | **Accepted.** The CLAIM now rests on spin preservation of SM antimatter operations (steps 1-3). (c) is restated as 't Hooft's internal-symmetry no-go, which SUSY evades with a spin-changing operator. |
| A | 2 | d = 2 pole agreement false (d − 1 counting gives R = 0.211) | **Accepted and verified.** c7_regulators: R(M_t) = 0.211, no R = 1 crossing below 10^29.9 GeV with d − 1 counting. The claim is restricted to cutoff and PV (n_V = 3, also DRED). The cutoff gauge-invariance caveat is added (H2). c4_regulator_running text corrected. Al-sarhi-Jack-Jones checked (see citations): the title of their NPB 345 (1990) paper indicates it treats the d = 2-pole definition (not read). |
| A | 3 | invariance of C proves nothing for field-relating symmetries; Bardeen; shift symmetry | **Accepted.** The scan is demoted to 4b. The general argument is S2 (type classes) plus S5 (RG). Bardeen is S6 and the route table; the shift symmetry is in the table and S2. |
| A | 4 | F-a is an identity, not a prediction | **Accepted.** F-a is relabelled a verification identity, and the "any linear gauge" generalization is dropped. Gate 7 is met weakly via F-b, and the CLAIM says so. |
| A | 5 | 4.1σ too high with y_t spread | **Accepted.** c7_mt_significance: 4.1σ at Δy_t = 0.0005, 3.7σ at 0.002, 3.3σ at 0.003 (2.9σ at 0.004 and with the σ(tt̄) pole mass). Quoted as 3.3-4.1σ. Why Jegerlehner's y_t is disfavoured [inference from abstracts, not a read of the numbers]: his matching gives absolute stability up to M_Pl, while the gauge-independent two-loop matching of Bednyakov et al. (1507.08833) yields an upper bound on M_t for stability that the measured mass exceeds (compatible with the MC mass at 1.3σ). That fits Buttazzo-type y_t and not y_t = 0.900. |
| A | 6 | verify Al-sarhi-Jack-Jones arXiv; Martin eq. (1.13) | **Done.** hep-th/9209124 is **not** Al-sarhi-Jack-Jones. It is G. Kleppe, "Regularization dependence of quadratic divergence cancellations" (VPI-IHEP-92/10), which argues that an Al-sarhi-Jack-Jones result fails with a nonlocal regulator. Al-sarhi, Jack, Jones: "Quadratic divergences in gauge theories", Z. Phys. C 55, 283 (1992), no arXiv number on INSPIRE; and "Quadratic divergences and dimensional regularization in two-dimensions and four-dimensions", Nucl. Phys. B 345, 431 (1990). Both verified on INSPIRE c7, contents not read. Martin eq. (1.13) checked in arXiv v7 (27 Jan 2016): it is Δm_H² = m_soft²[λ/16π² ln(Λ_UV/m_soft) + …], as cited. |
| B | 1 | classical scale invariance not addressed | **Accepted, option (i) plus a concession.** S6: μ² = 0 is RG invariant (β_{μ²} ∝ μ²). That is the SM's protection of μ² against SM-internal corrections, and it holds with no antimatter input. It is not a boson-fermion relation, it is anomalous, the measured μ² ≠ 0, and μ² = 0 gives no EWSB (B < 0). Whether μ² is protected from heavy thresholds cannot be posed within the SM spectrum. This is stated in the CLAIM ("What physical statement R supports"). |
| B | 2 | R has no observable | **Accepted.** CLAIM: "R is not an observable", with what it does mean (the Lagrangian lacks the coupling relation; δm² ∝ CM² only for a uniform PV-like completion; a real portal state gives κM²/16π² independent of C). R is demoted to "illustration, not claim". |
| B | 3 | scalars can be protected (shift, gauge-Higgs, SUSY, scale) | **Accepted.** Route table in CLAIM item 5, with SM status for each. The Goldstones G±, G⁰ are noted as the SM's protected scalars, and h is the radial mode. LW2 §3 is cited for pNGB/compositeness needing BSM. |
| B | 4 | not a rigorous no-go | **Accepted.** Rigorous chain S1-S6 (unitary/antiunitary maps commute with J²; type-class grading; Coleman-Mandula/HLS; supermultiplet scan; RG non-invariance; scale invariance). |
| B | 5 | exact Z₂ is SU(2) centre × (−1)^F | **Accepted.** Labelled trivial in §4b and in symmetry_scan.py. (b) is hermiticity, and m_t is protected by the chiral U(1) of t_R. |
| B | 6 | QCD-condensate EWSB omitted | **Accepted.** CLAIM item 6 and §7: M_W = g f_π/2 = 30 MeV (one doublet), 52 MeV (three massless doublets); f_π²/v² = 1.4×10⁻⁷. Quigg & Shrock, PRD 79, 096002 (2009), arXiv:0901.3958, verified (abstract). The CW/RG part of #4 is noted as using no antimatter structure. β(m²) ∝ m² is stated as holding in a mass-independent scheme with no heavy thresholds. |
| B | 7 | antimatter framing not load-bearing | **Accepted in part.** "What is new" 1 (old framing) is demoted. The antimatter content is now load-bearing in exactly one place, step 1: the operations C, CP, CPT and the sea/F-S pictures are the objects whose spin preservation decides the question. That is the only sense in which "antimatter" can answer D2. |
| B | 8 | 4.1σ headline selective | **Accepted.** See A5. F-b is labelled a cutoff-scheme coefficient at a non-SM scale, conditional on matching. |
| B | 9 | CLAIM 2 by numerical near-equality | **Accepted.** "Equally" is dropped. Self-conjugacy is dismissed by basis independence of the trace (L01 §4.4) and by complex stops. |

**Disagreements:**
- B3 cites the SM's protected vector masses (photon, gluon; W, Z ∝ gv) as evidence that "bosons carry no chirality" cannot be the obstruction. Agreed. Note that this also follows from step 1: gauge symmetry, the protector there, is internal and spin-preserving, and it protects vector masses because a vector mass term breaks it. No boson-fermion relation is involved.
- B1 suggests that under d = 4 DR "the SM and SUSY look alike for result #1". Only partly agreed. In DR both have m² multiplicatively renormalized by SM-internal loops. But SUSY's statement is the boson-fermion relation (step 2), which still distinguishes them in DR: with a heavy field coupled to H, SUSY gives δm_h² ∝ m_soft² ln, and the SM gives ∝ M². The line's negative result is about that relation, which is regulator independent.
- A2's suggestion that Al-sarhi-Jack-Jones is "likely about exactly this" is consistent with the NPB 345 title. The line cites it without reading it and does not rely on its content.

---


## 12. Response to referees C, D, E (cycle 8)

Files: REVIEWS_C.md (cycle 7 report, logic), REVIEWS_D.md (numbers), REVIEWS_E.md (cycle 8, adversarial). New scripts: `calc/c9_symmetry_group.py`, `calc/c9_twin_antimatter.py`, `calc/c9_C_measured.py`; `calc/symmetry_scan.py` corrected.

| ref | # | finding | response |
|---|---|---|---|
| C | 1 | S2 lemma false beyond global linear maps (gauge, pNGB, scale + GW, twin Z₂, 5D) | **Accepted.** S2 narrowed to global, homogeneous, linear 4D maps. Replaced as the load-bearing step by the enumeration of the SM Lagrangian's symmetry group (§4c, CLAIM item 2): every element maps each Higgs-sector operator to itself, checked numerically. One paragraph per counterexample class (§4c; CLAIM item 3). Empirical closure: C(M_t) ≠ 0 at ≥ 69σ and transverse crossing (G7, S5). |
| C | 2 | twin Higgs / folded SUSY missing | **Accepted.** Route-table row and §4d. Folded SUSY: spin-changing, new fields. |
| C | 3 | CM/HLS scope | **Accepted.** S3 and CLAIM item 4 now state the S-matrix assumptions, use only the algebra classification, and note that broken SUSY still needs new states (superpartners or a goldstino); neutrino-as-goldstino excluded (de Wit-Freedman). |
| C | 4 | β_C polynomial alone does not exclude reduction of couplings | **Accepted.** S5 rewritten: the exclusion comes from the measured transverse crossing; scheme status of each part stated; SUSY relation preserved in DR-bar. |
| C | 5 | tag inflation | **Accepted.** S1 boson part and S2 retagged [argument]. |
| C | 6 | Weyl vs Dirac in S1 | **Accepted.** One sentence added to S1 and CLAIM item 1. |
| C | 7 | "strong argument, not proof"; novelty explanatory | **Accepted.** CLAIM statement and Verdict say "strong argument"; What-is-new item 1 says "explanatory assembly". |
| C | 8 | F-b not a prediction of the line | **Accepted.** F-b demoted to context; gate 7 is G7. |
| C | 9 | factor 2700 vs 1540 | **Accepted.** See D1. |
| D | 1 | 2700 is one doublet; 52 MeV [approx] | **Accepted.** "≈ 2700 (one doublet) or ≈ 1540 (three)" in CLAIM item 7 and §7, computed in c9_symmetry_group (5): 2673 and 1543. [approx] carried to the CLAIM. |
| D | 2 | E1, E5 missing from checklist | **Accepted.** Added to §10 as not applicable (D1). |
| D | 3 | PDG 2026 note | **Accepted.** §10 C1/C2: C(M_t) recomputed with PDG 2026 inputs (−4.071 ± 0.039 pole, −3.429 ± 0.049 MS-bar); M_t − M_t* shifts by a few 0.01 GeV. |
| D | 4 | 1304.7813 abstract also quotes 7×10^16 | **Accepted.** Note added in §5c. |
| D | 5 | 3.3σ lower end arbitrary | **Accepted, widened rather than justified.** No published 0.003 spread was read, so §5b now states both judgement calls and gives the significance as a function of Δy_t (3σ at 0.0038, 2σ at 0.0074, 1σ at 0.0164, 0.4σ at 0.038). F-b is no longer the gate item. |
| D | 6 | rounding | **Accepted.** 3.04 → 3.03 (3.035). The §5a W-sector 0.393 at 10^16 is kept (0.3925 rounds to 0.393 or 0.392; left as committed). |
| D | 7 | S1 deviation quoted inconsistently | **Accepted.** 2.5×10⁻¹⁶ throughout. |
| E | 1 | twin / little Higgs omitted; "spin preservation is the departure" overclaimed | **Accepted.** §4d computes the twin protection (7 Goldstones, κ-independent pNGB curvature) and the antimatter counterfactual (H_B := H^c: eigenvalues {0,0,0,−4κ}, no protection). The D2 answer now names two departures: no spin-changing operator (vs SUSY), no independent partner field (vs twin). |
| E | 2 | custodial limit dropped y_b; H ↔ H^c is iσ₂ ∈ SU(2)_R; custodial L↔R ≠ chirality | **Accepted.** symmetry_scan.py corrected (C → 9/4 g² + 6λ − 12y²); iσ₂ check in c9_twin_antimatter (C); all three statements in §4d item 3 and D2 (b). |
| E | 3 | h self-loop uncredited | **Accepted.** 3λ = 0.378, 7.2% of the top term; all scalars 14.5% (§2, D2 (a)); pure-scalar term ∝ (m_h²/2v²)Λ², no Weisskopf softening (§3 table). |
| E | 4 | (b) is not "hermiticity" | **Accepted.** D2 (b) reworded: automatic for any Dirac mass; Λ² ∝ \|y_t\|²; P broken by SU(2)_L. |
| E | 5 | gate 7 not met for the CLAIM | **Accepted, option (iii) made quantitative plus option (i).** G7: the no-go's observable consequence is C not symmetry-enforced to vanish, so C(M_t) ≠ 0 and any zero is a transverse crossing. C(M_t) = −3.426 ± 0.050 (MS-bar, conservative) and −4.068 ± 0.040 (pole form), ≥ 69σ from zero with PDG 2024 errors propagated; falsifiers stated. Option (i), the counterfactual twin computation, is in §4d. Both are consistency checks of a no-go, not novel predictions; the overseer should rule whether that meets gate 7. |

**Disagreements and limits:**
- E5: G7 is a retrodiction. Its outcome was known before the line existed. It is offered because it is the only empirical content a symmetry no-go has (a symmetry that forced C = 0 would show up as C = 0 along the measured trajectory), and because it could have come out otherwise. It does not test anything about antimatter specifically.
- C1: the enumeration covers the known symmetry group of the renormalizable SM Lagrangian and the known classes of protection mechanisms. It does not exclude an unknown mechanism; hence "strong argument".
- The 5D-Lorentz case (Referee C) is folded into gauge-Higgs unification: it is 4D spin-changing (S ↔ V) and needs extra dimensions.

---

## Appendix: Cycle 4 calculator results (retained)

Scripts: `calc/c4_rxi_split.py` → `c4_rxi_split_out.txt`, `calc/c4_regulator_running.py` → `c4_regulator_running_out.txt`. Normalization: C_i = (1/2)∂²_φ STr M_i²(φ) at φ = v.

**C4.1 Gauge dependence [computed, symbolic].**
- The Λ² coefficient of Σ_hh(0) is read off from the large-k expansion of ln det of the fluctuation operator, sector by sector, with the longitudinal-A/Goldstone mixing block written out.
- Diagram identities: tr D_ξ = 3/(k²+M²) + ξ/(k²+ξM²) and k·D_ξ·k = ξk²/(k²+ξM²).
- Per diagram class C is ξ-dependent:
  - R_ξ charged sector: W seagull (3+ξ)g²/2, W–G bubble −ξg²/2, G seagull 2λ, ghosts 0.
  - Background R_ξ: ghosts −ξg², G seagull 2λ + ξg²/2.
  - Fermi gauge: the longitudinal seagull +ξg²/2 cancels the bubble.
- Per sector, STr M²(φ) is ξ-independent for all φ in all three families. The charged sector gives 3/2 g² + 2λ, and the neutral sector plus h gives 3/4(g²+g'²) + 4λ.
- Valid in any U(1)_em-preserving linear gauge.
- The MS-bar β functions are gauge independent (Caswell & Wilczek 1974), so R(μ) and μ₀ are too.

**C4.2 Regulator dependence [computed].**
- R2 (quadratic level) is the same in hard cutoff and PV (and DRED). **Corrected c7:** the dim-reg d = 2 pole with d − 1 vector polarizations gives R2(M_t) = 0.211, not 0.344 (`calc/c7_regulators_out.txt`).
- In d = 4 DR there is no such term (no observable).
- R4 (log level, gauge-invariant λ⁰ and λ² parts of STr M⁴): 0.138 at M_t, 0.345 at 10^10, 0.767 at 10^16, 1.113 at M_Pl; R4 = 1 at 10^18.19 (λ near-criticality, H1).

**C4.3** Per-diagram claims are gauge dependent and are not made. The symmetry no-go is gauge and regulator independent.
