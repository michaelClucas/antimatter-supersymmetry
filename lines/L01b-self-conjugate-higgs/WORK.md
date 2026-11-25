# L01b WORK - Self-conjugate Higgs vs SUSY's Higgs-mass protection

Scripts and outputs:
- `calc/pair_matching.py` → `calc/pair_matching_out.txt` (tasks 1, 3)
- `calc/symmetry_scan.py` → `calc/symmetry_scan_out.txt` (task 2)
- `calc/matching_running.py` → `calc/matching_running_out.txt` (task 4)

Shared inputs come from `tools/sm_inputs.py` (PDG 2024). Running uses `tools/rg_sm.py`: 3-loop for gauge, y_t and λ; 2-loop for y_b and y_τ; Buttazzo et al. arXiv:1307.3536 matching.

Normalization follows L01 and CONSTRAINTS G. Each species i has field-dependent mass M_i²(φ) = a_i φ² + const and n_i real degrees of freedom, and contributes C_i = ±n_i a_i. The SM total is C = 6λ + 9/4 g² + 3/4 g'² − 6y_t² = (3/v²)(m_h² + 2M_W² + M_Z² − 4m_t²). The Λ² term is proportional to C. Prefactors are regulator dependent (H2), so only ratios and zeros are used for conclusions. Gauge bosons are counted in Landau gauge, so the split of the total among W, Z and Goldstones is gauge dependent. The total and its zero are the standard one-loop result.

---

## 1. The SUSY cancellation written in antimatter language

### 1a. Which states enter [established; computed in pair_matching.py Parts 1-4]

In hole language, the Higgs mass shift at zero momentum equals d²E₀/dφ² of the φ-dependent vacuum energy:

E₀(φ) = Σ_bosons n ∫ω/2 − Σ_fermions n ∫ω/2,  with ω = √(k² + M²(φ)).

The fermion term is the energy of the filled Dirac sea. The boson terms are zero-point energies, i.e. virtual pair fluctuations. Every term that contributes to Λ² is a pair term: no Λ² piece comes from a state containing only particles.

| SUSY ingredient | states (n real dof) | C_i | antimatter reading |
|---|---|---|---|
| top | t_L, t̄ (from t_L field) ×3 col (6) and t_R, t̄ ×3 (6) | −3y² and −3y² | top Dirac sea: sea states deepen as φ grows |
| stops | t̃_L, t̃_L* ×3 (6) and t̃_R, t̃_R* ×3 (6) | +3y² and +3y² | stop-antistop zero-point pairs |
| quartic λ_{h t̃ t̃} = y_t² for both t̃_L and t̃_R | | | equal coupling for each chirality's partner |
| trilinear (y_t² v, A_t) | h → t̃ t̃* | log only | stop-antistop pair states, forward and backward orderings |

- **Particle-by-particle match:** each top chirality state and its antiparticle (t_L, t̄; t_R, t̄) has a complex scalar partner (t̃_L, t̃_L*; t̃_R, t̃_R*) with the same multiplicity (2 real dof per colour) and the same a = y²/2.
- **Observation (b) is realized in SUSY:** because the Yukawa couples L and R symmetrically, the F-terms give the same y_t² quartic to the L partner and to the R partner. Cancellation needs one bosonic pair per fermion chirality.
- **Mode by mode** (Part 2): with m_t̃ = m_t, the stop/antistop zero-point integrand cancels the top-sea integrand at every loop momentum k to machine precision, not only in the K² term.
- **On-shell Higgs, time ordered** (Part 3):
  - Top: forward h → t t̄ and backward vacuum Z-graph each contribute −3y²/(4π²)·k.
  - Stop seagull: this is an equal-time stop-antistop pair at one vertex, i.e. the vacuum contraction ⟨0|t̃ t̃†|0⟩. It contributes +3y²/(2π²)·k and exactly cancels the two top orderings.
  - Stop bubbles (h → t̃ t̃*, forward and backward): ~1/k, log only. Checked against the covariant Wick-rotated integrand; agreement is 7 digits.
  - The residual is a log. Numerically p·Σ' → −7.5243×10⁴ GeV² for m_soft = 1 TeV, which matches −(3y²/4π²)m_s² − (3y²/8π²)m_h² exactly. The first term is the soft-mass log, the standard −(3y_t²/8π²)(m_Q² + m_U² + A_t²) ln Λ (Part 4, symbolic; Martin, arXiv:hep-ph/9709356). The second is a p² (wave-function) log that the MSSM top-higgsino loop removes.
- **Feynman-Stueckelberg:** each closed stop loop reads as t̃ forward plus t̃* backward in time. Each closed top loop reads as t forward plus t̄ backward. So in this language SUSY's cancellation is **pair against pair**: top/antitop sea fluctuations against stop/antistop fluctuations. Weisskopf's electron cancellation was different, **particle-only against pair**.

### 1b. A new structural fact: SUSY respects self-conjugacy sector by sector [established within MSSM, computed here]

Part 4 computes the electroweak supertrace of the MSSM (gauge bosons, 8 Higgs scalars with D-term quartics, neutralinos, charginos) and resolves it by electric charge:

- **Neutral (self-conjugate) sector:** Z plus neutral Higgs scalars give (g² + g'²)(v_u² + v_d²). Majorana neutralinos give (g² + g'²)(v_u² + v_d²). Difference 0.
- **Charged-pair sector:** W± plus H± give 2g²(v_u² + v_d²). Dirac charginos give 2g²(v_u² + v_d²). Difference 0.

So SUSY cancels self-conjugate bosons with self-conjugate (Majorana) fermions, charged boson pairs with charged fermion pairs, and top/antitop with stop/antistop. **Observation (a) does have a SUSY counterpart:** the gauginos' self-conjugacy matches the self-conjugacy of the bosons they cancel (Z, γ, h). In SUSY, though, the SM's self-conjugate bosons are the loops that *need* cancelling. They are not the ones doing the cancelling.

## 2. The SM analogue: do the boson pairs play the stop role? (pair_matching.py Part 1, 2)

Per-species C_i, MS-bar at μ = M_t (pole-mass tree values in brackets):

| group | states | real dof | C |
|---|---|---|---|
| charged boson pairs | W⁺, W⁻ (3 pol. each), G⁺, G⁻ | 8 | +0.882 (+0.898) |
| self-conjugate bosons | Z (3 pol.), G⁰, h (photon a = 0) | 5 | +0.916 (+0.929) |
| top sea pairs | t, t̄, both chiralities, 3 colours | 12 | −5.221 (−5.895) |
| [SUSY] stop/antistop | t̃_L, t̃_L*, t̃_R, t̃_R* | 12 | +5.221 |

**What matches [established, computed]:**
- **Sign:** every SM boson pair (charged or self-conjugate) enters with the stop sign. In Part 2 this holds at every loop momentum above ~m_t. Below that, the h and G modes are negative because of their −a²v²/ω³ term (an infrared effect).
- **Pair structure:** as with stops, all SM boson Λ² pieces are pair terms (seagull, equal-time pair, zero-point). In Landau gauge the cubic hVV, hhh and hGG bubbles are only log divergent.
- **Counting:** 13 real massive boson dof couple to h. The top sea has 12 dof, and SUSY uses 12 stop dof. The SM has as many pair states as SUSY needs. [This is a count, not a mechanism. No claim is built on it (H1).]

**What fails [established, computed]:**
- **Coupling strength:** the mean coupling per boson dof is a = 0.138, against y_t²/2 = 0.435 for stops (ratio 0.32). The SM bosons amount to 4.1 "stop-equivalent" dof out of the 12 needed.
- **Matching ratio:** R = C_bos/|C_top| = **0.344** at μ = M_t (0.310 with pole masses). The boson pairs remove 34% of the top sea's Λ² coefficient, which drops from |C| = 5.22 to 3.42.
- **No pair-by-pair or sector-by-sector cancellation:** SUSY cancels within the colour-triplet sector and within the neutral and charged EW sectors separately. The SM would need a cross-sector cancellation: colourless W/Z/h pairs against the coloured top sea. The SM has no Yukawa-coupled self-conjugate fermion (neutrino masses are not used, A2), so its self-conjugate sector (+0.916) has nothing of its own to cancel against.

## 3. Weisskopf decomposition for the full one-loop Higgs self-energy [established; Parts 2-3]

| piece | Weisskopf (electron) | Higgs (SM) |
|---|---|---|
| particle-only states | C1 + Ta, linear divergence | **none** with Λ². Even the h-loop (hh) consists of pairs of a self-conjugate particle, i.e. particle plus its own antiparticle |
| pair / sea states | Cs + Tb, cancel the particle-only divergence | top sea: forward t t̄ and backward Z-graph, both −; boson pairs: W⁺W⁻, G⁺G⁻, ZZ, G⁰G⁰, hh seagulls, all + |
| result | linear → log; δm ∝ m (chiral symmetry) | Λ² survives with coefficient C = −3.42 at M_t |

- **Do the pair pieces reduce the divergence?**
  - Bosonic pairs (self-conjugate + charged) reduce the top sea's Λ² by 34% at M_t.
  - The top sea alone over-cancels the bosonic pairs by a factor 2.9: |C| goes from 1.80 for bosons alone to 3.42 for the total, so adding the top makes the total larger.
- **Exact cancellation needs the Veltman condition.** In this language:

> **Σ over boson pair channels n_i ∂²M_i²/∂h² = Σ over fermion sea channels n_f ∂²M_f²/∂h²**, i.e. 3/2 g² + 2λ (charged pairs) + 3/4(g² + g'²) + 4λ (self-conjugate) = 6y_t² + 6y_b² + 2y_τ² (seas).

SUSY satisfies this channel by channel. In the SM it holds, at best, as one total.

## 4. Symmetries acting on the self-conjugate h (symmetry_scan.py)

**Operator and spurion scan [established; computed]:**
- C, P (L↔R exchange; this is observation (b): it maps each Yukawa term to its h.c.), CP: every Higgs-sector operator maps to its hermitian conjugate. They only require real couplings. μ²|H|² is allowed.
- h → −h alone: forbids the Yukawa unless y_t → −y_t. μ²|H|² and λ are allowed.
- h → −h with t_R → −t_R: this is the "h → −h with L↔R sign" transformation. It is an exact SM symmetry: on all fields it equals the SU(2) centre element times a (3B+L) rotation by π. It forbids a bare Dirac mass m ψ̄_Lψ_R, which is why m_t ∝ y_t⟨h⟩. It allows μ²|H|².
- U(1) on H alone, chiral U(1)_A on the top, and the combined PQ-like U(1): each allows μ²|H|².
- Custodial SU(2)_L×SU(2)_R: |H|² is the O(4) bidoublet norm, so the mass term is allowed. g' and y_t − y_b break custodial symmetry, but setting g' → 0 only removes the 3/4 g'² term.

**Action on the couplings:**
- λ, g, g' are invariant under every candidate.
- y_t goes to ±y_t, e^{iα}y_t or y_t*.
- C depends on |y_t|², g², g'² and λ. It is **invariant under all candidates** (checked symbolically), so no candidate can force C = 0.

**Why self-conjugacy blocks protection [established; numerically illustrated]:**
- For a real field, averaging over the group gives an invariant positive quadratic form. For the 4 real Higgs components under SU(2)×U(1), h → −h and CP, the group average is the identity matrix to 10⁻¹⁷. A linear symmetry can never forbid h².
- A Weyl fermion carries a phase, and its mass term ψψ has charge 2α. This holds even for a **self-conjugate** Majorana gaugino, whose mass is protected by U(1)_R.
- **The parallel between h and the gauginos breaks exactly at (c):** both are self-conjugate, but only the fermion has a chiral phase to rotate. The experimenter's (a) and (c) together are the precise reason the SM gives no symmetry protection.

**RG test [established; computed]:**
- A relation imposed by a symmetry is RG invariant in a mass-independent scheme.
- At one loop, 16π² dC/dlnμ restricted to the surface C = 0 is 33g⁴ + 63/2 g²g'² − 162g²y² + 96g₃²y² + 17g'⁴ − 46g'²y² + 126y⁴. This is not identically zero.
- At the 3-loop crossing μ₀, dC/dlnμ = +0.0203. The one-loop formula gives +0.0202 there.
- So C = 0 is a crossing point that the flow passes through, not a fixed relation. SUSY's λ_{h t̃ t̃} = y_t² is an F-term identity that running preserves [established, standard non-renormalization].

## 5. Running and the falsifiable condition (matching_running.py)

| log₁₀ μ | self-conj. | charged | fermion seas | R |
|---|---|---|---|---|
| 2.24 (M_t) | 0.916 | 0.882 | 5.223 | 0.344 |
| 10 | 0.375 | 0.492 | 1.706 | 0.508 |
| 16 | 0.315 | 0.393 | 1.061 | 0.667 |
| 19.09 (M_Pl) | 0.321 | 0.363 | 0.866 | 0.790 |
| 22.83 | 0.352 | 0.337 | 0.689 | **1.000** |

**Crossing scale:**
- R = 1 (C = 0) at **log₁₀(μ₀/GeV) = 22.83** at 3 loops. At 2 loops it is 22.98, at 1 loop 26.79.
- Input dependence: M_t ± 0.29 GeV moves it by ±0.35 decades, α_s ± 0.0009 by ∓0.52, M_h ± 0.11 GeV by ∓0.04.
- This agrees with Hamada-Kawai-Oda, PRD 87, 053009 (2013), arXiv:1210.2538 (zero near 10²³ GeV for M_t = 173 GeV), and with Masina-Quiros arXiv:1308.1242 ("slightly trans-Planckian"). It reproduces L01's number independently.

**Falsifiable M_t values (pole, other inputs central)** at which boson pairs exactly match the fermion seas:
- at M_Pl: **M_t = 169.53 GeV**, −10.5σ from 172.57 ± 0.29
- at reduced M_Pl: 168.96 GeV
- at 10¹⁶ GeV: 166.83 GeV
- at the EW scale (tree): m_t = 96.1 GeV, or m_h = 312.9 GeV at the measured m_t
- Caveat: the M_t-dependence of the Buttazzo matching fit is linear around 173.34 GeV. 4 GeV away it is an extrapolation [uncertain at the 0.1 GeV level].

**What this means:**
- Above μ₀ the SM's boson pair fluctuations dominate the fermion sea [established, given the one-loop Landau-gauge coefficient].
- Below μ₀ there is no scale at which the SM reproduces SUSY's cancellation.
- Reading μ₀ as a physical boundary condition (e.g. "SUSY restored at μ₀", as HKO speculate) is outside SM scope [speculation].
- Above ~10¹⁰·⁷ GeV λ < 0 (metastability), so the h and G "pair" contributions turn negative there. The near-equality of the self-conjugate and charged pieces at μ₀ (0.352 vs 0.337) is a coincidence with no mechanism behind it (H1).
- Beyond one loop the Λ² coefficient is scheme dependent: Einhorn-Jones, PRD 46, 5206 (1992). HKO's 2-loop treatment gives the same ~10²³ GeV.

## 6. Verdict

**Holds [established, with calc]:**
1. The SUSY cancellation is entirely a cancellation between antimatter-containing pair states: top/antitop sea against stop/antistop zero-point pairs. Each top chirality state and its antiparticle has a partner, with the L↔R-symmetric coupling y_t² (observation (b)). In exact SUSY the cancellation is exact at every k.
2. SUSY carries self-conjugacy across multiplets: self-conjugate bosons (Z, γ, neutral Higgs) are cancelled by self-conjugate Majorana neutralinos, and charged pairs by charged pairs. The neutral and charged sectors each cancel exactly (symbolic).
3. In the SM, every boson pair (charged W⁺W⁻, G⁺G⁻ and self-conjugate ZZ, hh, G⁰G⁰) enters with the stop sign, uses the same pair (seagull) structure, and comes in a matching count (13 vs 12 dof). These pairs cancel 34% of the top sea at M_t, 67% at 10¹⁶ GeV and 79% at M_Pl, and 100% at 10^22.83 GeV.

**Fails [established, with calc]:**
1. **Magnitude:** the SM boson pairs couple about 3× too weakly (mean a = 0.138 against y_t²/2 = 0.435) for μ ≲ 10¹⁰ GeV. R = 1 only at 10^22.8 GeV.
2. **No symmetry:**
   - Self-conjugacy (a) guarantees that h² is invariant under every linear symmetry.
   - The L↔R-symmetric Yukawa (b) and the h → −h-with-chiral-sign Z₂ protect the *fermion* mass, not h².
   - Bosons have no chiral phase (c).
   - C is invariant under every SM candidate symmetry, and C = 0 is not RG invariant, so nothing in the SM enforces the match.
3. **Wrong sector pairing:** SUSY never uses the self-conjugate bosons to cancel the top. The SM version needs a cross-sector cancellation that SUSY does not use.

**Open:**
- Whether a non-linear or spectral (reformulation, A3) structure could tie λ, g, g' to y_t at μ₀. Any such tie must not use the NCG high-scale relations (A3.2).
- A gauge-independent OFPT treatment of the W/Z pieces. This line used Landau gauge for the Λ² split.
- The physical (dim-reg) restatement: there are no SM heavy thresholds, so the question reduces to gravity, which is out of scope.

**Falsifiable check:**
- Exact matching at M_Pl needs M_t = 169.5 GeV. At M_t = 172.57 ± 0.29 that is excluded at about 10σ.
- The crossing moves by 1.2 decades per GeV of M_t and by ~0.6 decades per 0.001 of α_s. Future M_t (threshold scan) and α_s measurements pin μ₀.

## 7. Citations
- Weisskopf, Phys. Rev. 56, 72 (1939) [from CONSTRAINTS G]
- Veltman, Acta Phys. Polon. B 12, 437 (1981) [from CONSTRAINTS G]
- Einhorn & Jones, PRD 46, 5206 (1992) [verified via INSPIRE record; full text not read]
- Martin, "A Supersymmetry Primer", arXiv:hep-ph/9709356 [verified; supertrace sum rule needs Tr Y = 0]
- Hamada, Kawai, Oda, PRD 87, 053009 (2013), arXiv:1210.2538 [verified abstract]
- Masina & Quiros, arXiv:1308.1242 [verified title; journal ref unverified]
- Buttazzo et al., JHEP 1312, 089 (2013), arXiv:1307.3536 [RGEs and matching, via tools/rg_sm.py]
- 't Hooft naturalness, NATO Sci. Ser. B 59, 135 (1980) [unverified details]

## 8. CONSTRAINTS checklist (E1, E5 dropped per D1)
- **A1:** SM fields only in every mechanism. Stops, electroweakinos and the 2HDM D-term potential appear only in pair_matching.py Part 3-4 as the SUSY comparison target. Pass.
- **A2:** neutrino masses are not used. The "no SM self-conjugate fermion coupling to h" statement does not assume Majorana neutrinos, and Dirac y_ν < 10⁻¹² changes C by < 10⁻²³. Pass.
- **A3:** no reformulation is used. Hole theory and time orderings are checked against covariant integrands (7-digit agreement) and the effective potential. Pass.
- **B1-B8:** particle and antiparticle enter identically in every C_i (CPT). No asymmetry is introduced. Pass.
- **B9, B10:** CP violation (baryon, neutron EDM, θ̄) is not used. The CP scan only needs real couplings. Pass.
- **C1, C2:** PDG 2024 inputs from tools/sm_inputs.py. The m_t, m_h needed for matching are falsifiable outputs. Pass.
- **C3:** nothing BSM is introduced, so no superpartner signatures arise. The line does not claim to reproduce the SUSY cancellation below 10²² GeV, so this is consistent with the LHC null results. Pass.
- **C4:** no g−2 claim. Pass.
- **D:** couplings from tools; running at 3 loops (2 loops for y_b, y_τ), stated. CPT-equal counting is used. Pass.
- **E2-E4, E6-E10:** no cosmological, baryogenesis, N_eff or neutrino-mass claims. Not applicable. Pass.
- **F1-F3:** no baryon-number violation used. The (3B+L) rotation by π in Section 4 is a global phase identity, not a process. Pass.
- **G:** Veltman normalization as in CONSTRAINTS G and L01. Only ratios and zeros are used. Dim reg has no Λ², which is stated in Section 6 "Open". Pass.
- **H1:** the 13-vs-12 dof count and the near-equality of the sectors at μ₀ are flagged as having no mechanism. No claim rests on them. Pass.
- **H2:** K² vs Λ² prefactors differ by 2. Only ratios, signs and zeros are used. The higher-loop scheme dependence of C is noted (Einhorn-Jones). The symmetry and RG-invariance arguments are regulator independent. Pass.
- **H3:** all OFPT/hole statements reproduce the covariant results, and the conclusions are stated covariantly (STr, symmetry, RG). Pass.
- **H4:** three scripts with saved outputs. Every number above appears in an `_out.txt`. Pass.

## Cycle 4 calculator results

Scripts: `calc/c4_rxi_split.py` → `calc/c4_rxi_split_out.txt` (task 1), `calc/c4_regulator_running.py` → `calc/c4_regulator_running_out.txt` (task 2). Running: `tools/rg_sm.py`, 3-loop. Normalization as above: C_i = (1/2) ∂²_φ STr M_i²(φ) at φ = v, C_top = −6y_t².

### C4.1 Gauge dependence (R_ξ, Fermi, background-field R_ξ) [established; symbolic, c4_rxi_split.py]

Method: Λ² coefficient of Σ_hh(0) = coefficient of 1/k² in the large-k expansion of ln det of the fluctuation operator, sector by sector, with the longitudinal-A/Goldstone mixing block written out for each gauge family.

- Diagram identities: tr D_ξ = 3/(k²+M²) + ξ/(k²+ξM²) and k·D_ξ·k = ξk²/(k²+ξM²). So the vector seagull has Λ² weight (3+ξ) and the h–V–G bubble has Λ² weight ∝ ξ (zero only in Landau gauge).
- Per diagram class, C is ξ-dependent. Ordinary R_ξ, charged sector: W seagull (3+ξ)g²/2, W–G bubble −ξg²/2, G seagull 2λ, ghosts 0 (ghost mass ξM_vM(φ) is linear in φ). Background R_ξ: W seagull (3+ξ)g²/2, G seagull 2λ + ξg²/2, ghosts −ξg². Fermi: longitudinal seagull +ξg²/2 cancels the bubble −ξg²/2. At M_t the "W seagull alone" is 0.629 (ξ=0), 0.839 (ξ=1), 1.258 (ξ=3).
- Per sector, STr M²(φ) is ξ-independent **for all φ** in all three families (d/dξ = 0 symbolically), with ξ_W, ξ_Z independent:
  - charged sector (W±, G±, ghosts): C_ch = 3/2 g² + 2λ
  - neutral sector (Z, G⁰, ghosts) + h: C_sc = 3/4(g²+g'²) + λ + 3λ; photon 0
- So the line's "charged pairs vs self-conjugate" split is gauge invariant, because it coincides with grouping by physical particle with Goldstones absorbed (W incl. eaten G±; Z incl. eaten G⁰; h). Landau gauge is the one gauge in each family where each diagram class already equals this grouping. Statements about "W pairs" or "Goldstone pairs" separately are gauge dependent and should not be made.
- Validity: any U(1)_em-preserving linear gauge. In a gauge that mixes charged and neutral fields the field-by-field split is undefined, but the grouping by charge eigenstates (W1,W2 / G1,G2 vs W3,B / G3) is fixed by group theory and the total is invariant.
- Running: MS-bar β functions of g, g', y, λ are gauge independent (Caswell & Wilczek, Phys. Lett. B 49, 291 (1974)), so R(μ) and μ₀ are gauge independent.

**Corrected numbers: none.** Gauge-invariant R (bosons/top) = 0.344 at M_t, 0.508 at 10¹⁰, 0.667 at 10¹⁶, 0.790 at M_Pl; charged 0.169 + self-conjugate 0.175 at M_t. These equal the line's Landau values.

### C4.2 Regulator dependence and the dim-reg version [c4_regulator_running.py]

**(a) Quadratic level, R2 = C_bos/|C_top|** [established at one loop]
- Per-species weight is n_i ∂²M_i²/∂φ² × a universal constant in hard cutoff (1/16π² × Λ²), Pauli-Villars (Λ² × const, M-independent) and dim reg via the residue of the pole at d = 2 (−1/2π, M-independent; Veltman 1981 identified quadratic divergences with these poles). So R2 = 0.344 (M_t) / 0.790 (M_Pl), μ₀ = 10^22.83 holds in three schemes (satisfies H2 at one loop).
- It is a property of the tree spectrum, C = (1/2)∂²STr M²(φ). In DR at d = 4 there is no such term and the SM has no heavy threshold to supply one. So R2 has no d = 4 physical observable attached. Beyond one loop the Λ² coefficient is scheme dependent (Einhorn-Jones, PRD 46, 5206 (1992)).

**(b) Log level, R4: the regulator-independent and gauge-invariant analogue** [established as a computation; interpretation conjecture]
- The universal one-loop log is the φ⁴ coefficient of STr M⁴(φ), i.e. the non-wave-function part of 16π²β_λ^(1). In exact SUSY (m_t̃ = m_t) STr M⁴ = 0, so the stops also cancel the top here.
- Gauge check: in Fermi gauge the mixed block gives Σm⁴ = m_G⁴ − 2ξM²m_G². So ∂²_φ STr M⁴ at v is ξ-dependent (Nielsen identity, Nielsen NPB 101, 173 (1975)), but the λ⁰ and λ² terms are not. Keep those:
  R4 = [24λ² + (3/8)(2g⁴ + (g²+g'²)²)] / [6y_t⁴ (+6y_b⁴+2y_τ⁴)]; charged W(+G±) = (3/4)g⁴ + 4λ², self-conjugate Z(+G⁰)+h = (3/8)(g²+g'²)² + 20λ².

| log₁₀ μ | R2 (quadratic) | R4 (log) | R4 charged | R4 self-conj |
|---|---|---|---|---|
| 2.24 (M_t) | 0.344 | **0.138** | 0.043 | 0.095 |
| 10 | 0.508 | 0.345 | 0.163 | 0.182 |
| 16 | 0.667 | 0.767 | 0.305 | 0.461 |
| 19.09 (M_Pl) | 0.790 | **1.113** | 0.396 | 0.718 |

- R4 = 1 at log₁₀ μ = 18.19 (3-loop; 18.24 at 2-loop, 19.15 at 1-loop). Input shifts: M_t ± 0.29 → ±0.07, α_s ± 0.0009 → ∓0.16, M_h ± 0.11 → ±0.01. This is close to the reduced Planck mass (10^18.39).
- This is not new physics and not a new coincidence. With λ ≈ 0 at high scale, R4 = 1 is essentially β_λ ≈ 0, i.e. the known near-criticality of the SM: λ has its minimum at 10^17.56 GeV here (Buttazzo et al., arXiv:1307.3536). Treat it under H1: no mechanism. [established that it is near-criticality; any "matching" reading is speculation]
- At M_t the log-level boson fraction (14%) is smaller than the quadratic one (34%), because couplings enter squared (g⁴ vs y_t⁴).

### C4.3 What survives

1. **Survives, gauge independent and (one-loop) regulator independent** [established]:
   - All SM boson pair sectors enter with the stop sign.
   - The quadratic-level fraction is R2 = 0.344 at M_t and 0.790 at M_Pl, with R2 = 1 at 10^22.83, and this is gauge invariant.
   - The charged/self-conjugate split, 0.169 / 0.175 at M_t, is gauge invariant when Goldstones are counted with their W/Z.
2. **Must be reworded:**
   - Any per-diagram claim (W⁺W⁻ seagull, G⁺G⁻ loop, "Landau-gauge W piece") is gauge dependent.
   - "Cancels 34% of the Λ² divergence" is a one-loop, regulator-class statement (cutoff/PV/d=2 pole), and it has no d = 4 DR content.
   - The regulator-independent physical analogue is R4: 14% at M_t, 111% at M_Pl, crossing 1 at 10^18.2 GeV. That crossing is the known near-criticality of λ, not a new matching. [established computation; interpretation H1-flagged]
3. **Unchanged:** the symmetry no-go (C invariant under all candidates, C = 0 not RG invariant) is gauge and regulator independent. The falsifiable M_t = 169.5 GeV refers to R2 (one-loop Λ² coefficient), so it inherits the scheme caveat above.
