# L01b WORK - Self-conjugate Higgs vs SUSY's Higgs-mass protection

Single line for SUSY #1 (Higgs-mass protection) and #4 (radiative EWSB). L01-weisskopf-hierarchy is merged in by reference (Section 7).

Tags (CONSTRAINTS convention, refined per Referee 1 c4 finding 7):
- **[established]**: published or textbook result, citation given.
- **[computed]**: derived or computed in this line, with a committed script and saved output.
- **[conjecture]**: argued but not proven. **[speculation]**: outside what the line can test.

---

## CLAIM

**Target.** SUSY result #1 in its symmetry form: SUSY makes m_h² insensitive to the UV because an operator Q that commutes with the Hamiltonian and changes spin by 1/2 ties every boson coupling of H to a fermion coupling, e.g. λ_{H t̃ t̃} = y_t² (F-term of W = y_t H Q U). That relation is what cancels the top's Λ² term against the stops'. Result #4 (radiative EWSB) is treated in item 6.

**Statement (negative result).** No operation of SM antimatter physics can enforce the boson-fermion coupling relation that SUSY's protection rests on, and within SM field content no other mechanism can either. The argument is a chain, each step checked in `calc/c7_same_spin_out.txt`:

1. **Every SM antimatter operation preserves spin.** C, P and CP are unitary and T and CPT antiunitary operators; all commute with J² (C, P commute with J; T, CPT send J → −J). They map a spin-j particle to a spin-j antiparticle with the same statistics. Checked explicitly for the Dirac field: ψ^c = iγ²ψ* transforms with the same spinor Lorentz matrix as ψ (deviation 2×10⁻¹⁶). The Dirac-sea and Feynman-Stueckelberg pictures are relabelings of the same Fock space (H3): the hole in a spin-1/2 level is a spin-1/2 positron. [established; computed check S1]
2. **A spin- and statistics-preserving map cannot relate y_t to λ or g.** Such a map sends scalars to scalars, Weyl fermions to Weyl fermions and vectors to vectors, so it maps each Lagrangian monomial into monomials of the same field-type class. y_t lives in class (scalar, fermion, fermion), λ in (scalar)⁴, and g is fixed by gauge universality. The Veltman combination C = 6λ + 9/4 g² + 3/4 g'² − 6y_t² cuts across classes, so no such symmetry can force C = 0. [established; computed check S2]
3. **The only spin-changing symmetry is SUSY, and it needs new fields.** By Coleman-Mandula, every bosonic symmetry of a nontrivial S-matrix is Poincaré × internal, and internal generators commute with J. By Haag-Łopuszański-Sohnius, the only extension is a graded one whose odd generators transform as spin 1/2: SUSY (plus conformal symmetry for massless theories, item 5). SUSY multiplets pair states of equal gauge charge with spin differing by 1/2. The SM has no colour-triplet scalar for the top, no octet fermion for the gluon, and 28 bosonic vs 90 fermionic dof. Its only quantum-number match is H ~ L*, which does not touch the top loop. Supersymmetrizing the SM needs superpartners, which A1 and C3 forbid. [established theorems; computed scan S3-S4]
4. **The relation cannot hold accidentally at all scales.** Without a symmetry, C = 0 could at best hold at one scale. On the surface C = 0 the one-loop β_C is a nonzero polynomial, and the 3-loop flow crosses C = 0 transversally at μ₀ = 10^22.83 GeV with dC/dlnμ = +0.020. [computed S5]
5. **Other routes to scalar protection are not available with SM content.**

   | mechanism | what it needs | SM status |
   |---|---|---|
   | SUSY (spin-1/2 generator, holomorphy plus non-renormalization) | superpartners | absent (step 3) |
   | shift symmetry / pNGB Higgs | h a Goldstone of a larger spontaneously broken group | h is the radial mode of H; G±, G⁰ are the SM's only Goldstones and are exactly protected. A pNGB or composite h needs new strong dynamics (LW2 §3: QCD gives 0⁻ Goldstones and a heavy, broad 0⁺; t̄t compositeness needs m_t ≈ 235-246 GeV). BSM. |
   | gauge-Higgs unification (H = A₅) | extra dimensions, enlarged gauge group | BSM |
   | holomorphy | superfields, which means SUSY | absent |
   | classical scale invariance (Bardeen 1995) | μ² = 0 at tree level | m² = 0 is RG invariant in a mass-independent scheme. But dilatations preserve spin, so they act on μ² and leave C alone. The symmetry is anomalous. The measured spectrum needs a tree μ² = (88.5 GeV)², and with μ² = 0 the SM has no radiative EWSB (B = −4.4×10⁻³ < 0). It is not an antimatter operation. |

6. **SUSY #4.** The SM has no Coleman-Weinberg or RG-driven radiative EWSB (L01, §7). It does have one dynamical EWSB mechanism built from antimatter: the QCD quark-antiquark condensate ⟨q̄_L q_R⟩ carries weak isospin and breaks SU(2)×U(1). It gives M_W = g f_π/2 = 30 MeV for one light doublet and 52 MeV with all three quark doublets massless, compared with the observed 80.4 GeV. Its share of v² in the real SM is 1.4×10⁻⁷. So antimatter-condensate EWSB exists in the SM, but at the QCD scale, a factor of about 2700 too low in the condensate scale. [established, Quigg-Shrock 2009; computed `calc/c7_qcd_ewsb_out.txt`]

**Answer to D2.** (a) Self-conjugacy of h is irrelevant: complex stops are protected in SUSY, and the trace is basis independent (W± = rotated real fields). (b) The L↔R symmetry of y h ψ̄ψ is hermiticity of a real Yukawa. What protects m_t is the chiral U(1) of t_R, broken only by y_t, and that does nothing for h². (c) "Bosons carry no chirality" is true of MSSM scalars too, so it is not where the SM departs from SUSY. What it does show ('t Hooft) is that no internal linear symmetry protects a scalar bilinear. The precise departure is items 1-3: SUSY evades (c) with a spin-changing operator, and every SM antimatter operation is spin-preserving. [established ingredients; assembled here]

**Illustration, not claim: how far short the SM falls.** The one-loop Λ² coefficient splits into gauge-independent sector totals (ξ-independent in R_ξ, background R_ξ and Fermi gauges): W sector 3/2 g² + 2λ, Z sector + h 3/4(g²+g'²) + 4λ, fermions −6y_t² − 6y_b² − 2y_τ². Both boson sectors carry the stop sign (spin-statistics, (−1)^{2J}). Their ratio to the fermion term is R = 0.344 at M_t and 0.790 at M_Pl, with R = 1 at 10^22.83 GeV (3-loop, Buttazzo matching; about 10^16 GeV with Jegerlehner's y_t, §5c). [computed]
- **R is not an observable.** It is the ratio of one-loop supertrace coefficients of the Lagrangian. Hard cutoff and Pauli-Villars agree on it (n_V = 3, also dimensional reduction). The d = 2 pole of dimensional regularization, with d − 1 vector polarizations, gives R(M_t) = 0.211 and no crossing below 10^29.9 GeV. In d = 4 MS-bar the term is absent. [computed `calc/c7_regulators_out.txt`; the cycle-5 claim of d = 2 agreement was false and is withdrawn]
- **What physical statement R supports.** If a UV completion regulated every SM loop uniformly (heavy copies of all SM fields with SM couplings, PV-style), then δm_h² ∝ C M². A real heavy state with a portal κ|H|²|S|² instead shifts m_h² by about κM_S²/16π², independent of C. So C ≠ 0 is a statement that the SM Lagrangian lacks the coupling relation of step 2. It does not measure any SM sensitivity to heavy thresholds, and the SM spectrum contains no heavy threshold to test. [established reasoning]

**Falsifiable or checkable items** (gate 7 is met only weakly, through F-b):
- **F-a (verification identity, not a prediction).** The sector totals are ξ-independent in the three gauge families computed. This follows from the Nielsen identity with independent ξ_W, ξ_Z. Only a calculational error could falsify it. It is not claimed for arbitrary gauges.
- **F-b (consistency check, HKO/Masina-Quiros, conditional on matching).** C(M_Pl) = 0 needs M_t* = 169.54 GeV. The measured 172.57 GeV lies **3.3-4.1σ** from it within Buttazzo-type matching, for a y_t matching spread of 0.0005-0.003 (`calc/c7_mt_significance_out.txt`; 2.9σ using the cross-section pole mass 172.4 ± 0.7). It is not excluded under Jegerlehner's matching. The dominant uncertainty is the on-shell → MS-bar y_t conversion. C(M_Pl) is a cutoff-scheme coefficient evaluated at a non-SM scale.
- **F-c.** μ₀ is set by y_t(M_t). A settled two-loop matching decides between 10^16 and 10^23 GeV (cutoff/PV scheme only).
- **F-d (structural; a theorem within the SM, not a prediction).** Steps 1-3 imply that no SM-only mechanism yields λ_{H X X} = y_t² for any colour-triplet boson X. Finding a colour-triplet scalar at the LHC would be BSM and outside this line.

**What is new** (LITCHECK c4 §2-3, revised c7):
1. The spin-preservation argument assembled into a no-go for an antimatter analogue of SUSY's protection: steps 1-4 plus the route table. Each ingredient is textbook (Coleman-Mandula, HLS, 't Hooft naturalness, the Veltman RG flow). The assembly, aimed at C/CP/CPT and the hole-theory pictures, was not found in print [conjecture about novelty; LITCHECK should confirm].
2. The quantitative reconciliation of Jegerlehner's μ₀ ≈ 10^16 GeV with the ≈10^23 GeV of HKO/MQ: y_t(M_t) alone accounts for the shift (§5c). Jegerlehner names the cause; new here are the numerical reproduction and the coupling-by-coupling attribution.
3. The explicit ξ-independence of the sector split in three gauge families, and the correction that the d = 2 pole with d − 1 counting gives a different R.

**No step uses antimatter structure as a mechanism.** The antimatter content of the line is the input to step 1: the set of operations to be tested. Hole-theory and time-ordered forms (§1-3) reproduce covariant results and add nothing (H3).

**Status:** CONTINUE (fix round 3, cycle 7). Negative result for #1 and #4. Referees so far: 0/3 clean (A and B c6: MAJOR, no fatal).

---

Scripts and outputs (all rerun cycle 7 from inside `calc/` and reproduced):
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
- `calc/refA_check.py`, `calc/refB_check.py` (referee checks, rerun)

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
- **Landau-gauge artefacts, not used in any claim** (finding 6): the "13 boson dof vs 12 stop dof" count, the "mean a per dof = 0.138" and the "4.1 stop-equivalent dof". In unitary gauge the count is 10, and in R_ξ the ghosts enter with negative weight. The small-k negativity of the h + G modes in Part 2 is partly an artefact of the massless Landau-gauge Goldstones.
- **Statements about W⁺W⁻ or G⁺G⁻ separately are gauge dependent** (per-diagram weights (3+ξ)g²/2, −ξg²/2, …; c4_rxi_split). They are not made.
- **The SUSY comparison is about sectors, and they do not match.** In SUSY the colour-triplet top is cancelled within its own sector (stops). The SM version would need a cross-sector cancellation of colourless W/Z/h against the coloured top. The SM has no Yukawa-coupled self-conjugate fermion. Whatever the neutrino-mass mechanism, it contributes to C at order m_ν²/v² ~ 10⁻²⁵, so the conclusion does not depend on it (A2).

## 3. Weisskopf comparison (L01 merged)

| | electron (Weisskopf 1939) | Higgs (SM) |
|---|---|---|
| particle-only states | linear divergence | none with Λ² |
| pair/sea states | cancel the linear piece → log | top sea adds (both orderings −); boson sectors subtract |
| reason | chiral symmetry: δm ∝ m | no symmetry; C ≠ 0 except at μ₀ |

- The Weisskopf hole-theory reproduction (linear → log, coefficient 3α/2π) is in L01 `calc/weisskopf_ofpt.py`.
- The two top-loop time orderings, both negative and agreeing with the covariant integrand to 8 digits, are in L01 `calc/higgs_top_ofpt.py`. [computed in L01]
- **Channel form of the Veltman condition** (both sides are 2C): Σ_boson sectors n_i ∂²M_i²/∂h² = Σ_fermions n_f ∂²M_f²/∂h², i.e. 3/2 g² + 2λ + 3/4(g² + g'²) + 4λ = 6y_t² + 6y_b² + 2y_τ². In the SM it holds, if at all, only for the total, and only at μ₀.

## 4. The same-spin obstruction (c7_same_spin.py; scan retained from symmetry_scan.py)

**4a. The chain [established theorems; computed checks].** This section carries the CLAIM. Details for each step:
- **S1. Antimatter operations preserve spin.** In the Dirac representation, the script checks that iγ² L* (iγ²)⁻¹ = L for random spinor Lorentz transformations L (max deviation 2.5×10⁻¹⁶). So ψ^c is a (1/2,0)⊕(0,1/2) field like ψ. γ⁰ J γ⁰ = J (parity) and T J* T⁻¹ = −J with T = iγ¹γ³ (time reversal, antiunitary). All of these preserve J² = 3/4. On bosons, φ → φ* and W⁺_μ ↔ −W⁻_μ keep scalars scalar and vectors vector. None changes (−1)^F = (−1)^{2j}. The Dirac sea and Feynman-Stueckelberg readings are not operators on the Hilbert space. They redescribe the same states (H3), and the hole of a spin-1/2 level is spin 1/2.
- **S2. Field-type classes.** A spin- and statistics-preserving linear field map preserves the multiset of field types in each monomial. So invariance of L gives conditions within each class only: y_t (S F F), λ (S⁴), g (V S S, V F F, V³, V⁴, tied by gauge universality). Relating y_t to λ or g needs S ↔ F (SUSY) or S ↔ V (gauge-Higgs unification, H = A₅ in extra dimensions). A non-linear shift symmetry mixes classes of different degree, but h would have to be a Goldstone of a larger broken group.
- **S3. Coleman-Mandula and HLS.** Coleman & Mandula, Phys. Rev. 159, 1251 (1967), restricts the bosonic symmetry algebra of a nontrivial S-matrix with a mass gap to Poincaré ⊕ internal, with internal generators commuting with J. Haag, Łopuszański & Sohnius, Nucl. Phys. B 88, 257 (1975), show that the only graded extension has spin-1/2 odd generators (SUSY), plus conformal symmetry when all particles are massless. C, P and T are discrete and not covered by CM, but S1 checks them directly. Caveat: the SM has massless photons and gluons, so CM's mass-gap assumption does not hold literally. The extra generators HLS allow in the massless case are conformal ones, which also preserve spin, so the conclusion stands [established; the massless extension is not re-derived here]. The script verifies that [J_z, Q_α] = ∓Q_α/2 shifts J_z by 1/2, and that the F-term of W = yHQU gives λ_{H t̃ t̃} = |y|² with m_t = y⟨H⟩, cancelling the top-sector ∂²STr M² (+6y² − 6y² = 0).
- **S4. SM content cannot fill supermultiplets.** Quantum-number scan: Q, u^c, d^c, e^c have no SM boson partner. Gluon, W and B have no SM fermion partner. Only H ~ L* matches. dof are 28 vs 90. [computed]
- **S5. No accidental relation.** One-loop 16π²β_C on C = 0: 33g⁴ + 63/2 g²g'² − 162g²y² + 96g₃²y² + 17g'⁴ − 46g'²y² + 126y⁴. 3-loop dC/dlnμ = +0.0203 at μ₀ = 10^22.83 GeV. In SUSY, λ_{H t̃ t̃} = y_t² is preserved by running because it is an F-term identity [established].
- **S6. Classical scale invariance (Bardeen, "On naturalness in the standard model", FERMILAB-CONF-95-391-T, 1995 Ontake Summer Institute; report number and title verified on INSPIRE c7, text not read).** In a mass-independent scheme β_{μ²} ∝ μ², so μ² = 0 is RG invariant. This is the SM's own protection of μ² against SM-internal corrections [established]. It is not a SUSY analogue in the sense of the CLAIM. Dilatations commute with J², so they constrain the dimensionful μ² and leave C alone. They are anomalous. The measured spectrum has tree μ² = m_h²/2 ≠ 0. With μ² = 0, the SM CW potential has B = (6M_W⁴ + 3M_Z⁴ − 12m_t⁴)/(64π²v⁴) = −4.4×10⁻³ < 0 and no radiative EWSB (L01: −4.3×10⁻³ with m_h included). Whether μ² is "protected" against heavy thresholds cannot be posed inside the SM, which has none (Referee B c6 finding 1, option (i)) [established reasoning].

**4b. Retained operator scan (symmetry_scan.py) [computed, demoted to illustration].**
- C, P and CP map each Higgs-sector operator to its hermitian conjugate, by definition. h → −h alone forbids the Yukawa unless y_t → −y_t. U(1)_H, chiral U(1)_A, the PQ-like U(1) and custodial O(4) all allow μ²|H|².
- The Z₂ (h → −h, t_R → −t_R) is the SU(2)_L centre element times (−1)^F (refB_check). It is trivial, a gauge transformation times a 2π rotation, and is no longer cited as protecting anything. m_t is protected by the chiral U(1) of t_R, broken only by y_t.
- "C is invariant under every candidate" does not by itself prove anything for symmetries relating different fields: SUSY leaves the singlet C invariant and still forces λ_{Ht̃t̃} = y_t² (Referee A c6 finding 3). The general arguments are S2-S5.
- 't Hooft (NATO Sci. Ser. B 59, 135 (1980)): spin-0 bilinears φ*φ and h² are invariant under every linear internal symmetry, for real and complex scalars alike. A Weyl mass ψψ is not. This is observation (c), and it holds in the MSSM too. It rules out internal-symmetry protection of h²; it is not the point where the SM departs from SUSY.

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

C(M_Pl) = 0 needs M_t* = 169.54 GeV. The measured value is 172.57 GeV, 3.04 GeV above. Equivalent shifts in M_t:

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
- This restates the HKO and Masina-Quiros result that the SM does not meet the Veltman condition at M_Pl. Here it is updated to PDG 2024 inputs with an error budget. It is not a test of any mechanism proposed by this line (finding 3a, accepted).
- Not in the budget: the Jegerlehner matching spread (Section 5c), equivalent to about 6.8 GeV. If that matching is admitted, C(M_Pl) = 0 is not excluded. The dominant uncertainty is the on-shell → MS-bar y_t conversion.
- C(M_Pl) is a cutoff/PV-scheme coefficient evaluated at a non-SM (gravitational) scale (Referee B c6 finding 8).
- Further scheme caveat [established]: beyond one loop the Λ² coefficient is scheme dependent. Einhorn & Jones, PRD 46, 5206 (1992); Al-sarhi, Jack, Jones, Z. Phys. C 55, 283 (1992) and Nucl. Phys. B 345, 431 (1990); Kleppe, hep-th/9209124 (regularization dependence, disputes an Al-sarhi-Jack-Jones result); D.R.T. Jones, PRD 88, 098301 (2013), arXiv:1309.7335, who disputes HKO's two-loop coefficient. The C1 → C2 row above is one estimate of that spread, not a bound.

### 5c. Jegerlehner's μ₀ ≈ 10^16-17 GeV vs 10^22.83 GeV [computed; c5_jegerlehner.py]

**Sources.**
- Jegerlehner, Acta Phys. Polon. B 45, 1167 (2014), arXiv:1304.7813, Table 1 and text: μ₀ ≈ 1.4×10^16 GeV for C1 and 1.1×10^16 GeV for C2. Inputs: M_t = 173.5 GeV, M_H = 126 GeV, α_s = 0.1184. MS-bar couplings come from his on-shell → MS-bar matching with tadpoles included.
- Jegerlehner, arXiv:1305.6652 (preprint): ≈7×10^16 GeV in the text, ~10^17 in the abstract.
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

**Consequence for this line:** μ₀ is conditional on the matching. CLAIM items 1, 2, 4 and 5 do not depend on it. Item 3 is quoted for Buttazzo matching. With Jegerlehner's couplings R(M_t) ≈ 0.37, so the qualitative statement "the bosons cancel about a third at M_t" is unchanged.

### 5d. Log-level analogue R4 [computed in c4; interpretation H1]
- R4 is the gauge-invariant λ⁰ and λ² part of the STr M⁴ φ⁴ coefficient.
- R4 = 0.138 at M_t and 1.113 at M_Pl, crossing 1 at 10^18.19 GeV. This is the known near-criticality of λ, i.e. β_λ ≈ 0 (Buttazzo et al.), not a new matching.

## 6. Verdict

**Holds** [established theorems plus computed checks; regulator independent]:
- Every SM antimatter operation preserves spin and statistics (S1). No spin-preserving map can tie y_t to λ or g (S2). The only spin-changing symmetry is SUSY, which SM content cannot carry (S3-S4). C = 0 is not RG invariant (S5). Scale invariance acts on μ², not C, and is broken in the measured SM (S6).
- SUSY #4: no radiative EWSB in the SM. The only SM antimatter-condensate EWSB (⟨q̄q⟩) gives M_W ≈ 30-52 MeV.

**Illustration** [computed, cutoff/PV only, no observable]: R = 0.344 at M_t and 0.790 at M_Pl, R = 1 at 10^22.83 GeV (Buttazzo) or about 10^16 GeV (Jegerlehner). DREG d = 2 pole: R(M_t) = 0.211.

**Not claimed:** any physical reading of μ₀ [speculation, outside SM scope]; that R measures sensitivity to heavy thresholds; that the scan of §4b proves anything by itself.

**Open:**
- LITCHECK of novelty item 1 (the assembled same-spin no-go).
- Whether a reformulation (A3) could tie λ, g, g' to y_t without its extra high-scale relations (A3.2). By S2 it would need an S ↔ F or S ↔ V map, i.e. SUSY or gauge-Higgs content, so none is expected [conjecture].

## 7. Merged from L01-weisskopf-hierarchy (by reference)

L01 is support for this line, and L01b is the single line for SUSY #1 and #4. Calculations reused, all under `lines/L01-weisskopf-hierarchy/calc/` (rerun in a scratch copy, cycle 5):
- `weisskopf_ofpt.py`: hole-theory electron self-energy. The linear divergence cancels between particle-only and sea terms, leaving the covariant log 3α/2π. Chiral symmetry is the covariant reason.
- `higgs_top_ofpt.py`: top-loop time orderings (forward h → t t̄ and backward Z-graph), both negative. They agree with the covariant integrand to 8 digits. Also checked: Im Σ = m_h Γ(h → f f̄) and the light-fermion threshold structure.
- `veltman_running.py`: normalization δm_h² = CΛ²/8π² with the tadpole included, and the basis-independence of the trace (charged pair = rotated real fields).
- `cw_radiative_ewsb.py`: **SUSY #4.**
  - Coleman-Weinberg: with the tree mass term set to zero, B = −4.3×10⁻³ < 0, so the stationary point is a maximum and there is no radiative EWSB. The top threshold is 78.6 GeV, and W, Z alone give m_h = 9.8 GeV.
  - In MS-bar β(m²) ∝ m² at all orders, so the sign of m² is RG invariant and there is no RG-driven sign flip of the kind stop soft masses produce in the MSSM.
  - [established classics: Coleman-Weinberg PRD 7, 1888 (1973); Weinberg PRL 36, 294 (1976); Linde JETP Lett. 23, 64 (1976); reproduced in L01]
- **QCD-condensate EWSB (cycle 7, Referee B c6 finding 6)** [established, Quigg & Shrock, PRD 79, 096002 (2009), arXiv:0901.3958; computed `calc/c7_qcd_ewsb_out.txt`]. ⟨q̄_L q_R⟩ ≠ 0 has I = 1/2 and breaks SU(2)_L × U(1)_Y → U(1)_em; the pions are partly eaten. M_W = g√n_d f_π/2 = 30.1 MeV (n_d = 1) or 52.1 MeV (Higgs off, three massless doublets, f_π held at 92.1 MeV [approx]), M_Z = M_W/cos θ_W. In the real SM it adds f_π²/v² = 1.4×10⁻⁷ to v² (5.6 keV on M_W). This is an SM EWSB mechanism built from quark-antiquark pairs, and it is too small by a factor of about 2700 in scale. The CW and RG statements above use no antimatter structure, and β(m²) ∝ m² holds in a mass-independent scheme with no heavy thresholds.
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

## 10. CONSTRAINTS checklist (E1, E5 dropped per D1; revised cycle 7)
- **A1:** Pass. SM fields only in every mechanism. Stops, superpotential and supermultiplets appear only as the comparison target (pair_matching.py Parts 3-4, c7_same_spin S3-S4). Composite/pNGB Higgs, gauge-Higgs unification and superfields are named only as routes that would need BSM content (CLAIM item 5), and none is used.
- **A2:** Pass. Neutrino masses are not used. Any mechanism contributes at most m_ν²/v² ~ 10⁻²⁵ to C.
- **A3:** Pass. No reformulation is used. Hole theory and time orderings are bookkeeping, checked against covariant integrands. In step 1 the Dirac-sea and Feynman-Stueckelberg pictures enter only as members of the set of antimatter operations tested, and are shown to preserve spin.
- **B1-B8:** Pass. CPT is used as an exact symmetry (step 1). Particle and antiparticle enter every C_i identically. No particle/antiparticle asymmetry is used.
- **B9, B10:** Pass. CP violation is not used.
- **C1, C2:** Pass. PDG 2024 inputs via tools/sm_inputs.py. F-b is quoted as 3.3-4.1σ with the y_t-matching spread, and as not excluded under Jegerlehner matching.
- **C3:** Pass. Step 3 explains the absence of superpartner signatures trivially: the line uses none. It also explains why the SM cannot reproduce SUSY's cancellation without them.
- **C4:** Pass. No g−2 claim.
- **D:** Pass. Couplings from tools/, 3-loop running (2-loop for y_b, y_τ), stated.
- **E2-E4, E6-E10:** Not applicable. No cosmology or baryogenesis claims. The QCD condensate (item 6) is a T = 0 statement; E10's crossover fact is not touched.
- **F1-F3:** Pass. No baryon-number violation.
- **G:** Pass. Normalization as in CONSTRAINTS G. The absence of Λ² in d = 4 DR is stated in the CLAIM, together with "R is not an observable".
- **H1:** Pass. Flagged as having no mechanism: the near-equality of the sectors at μ₀, the R4 crossing and the Landau-gauge dof counts.
- **H2:** Pass for the claim; fails for R by design. The no-go (steps 1-5) is regulator independent: it concerns symmetries of the Lagrangian. R agrees in hard cutoff and PV (and DRED) only. The DREG d = 2 pole with d − 1 vector counting gives 0.211 at M_t (c7_regulators), so R is labelled scheme dependent. A 4D hard cutoff on gauge loops is not gauge invariant; its agreement with PV holds for the effective-potential momentum routing.
- **H3:** Pass. Antimatter structure enters as the set of operations tested in step 1, and the result (they preserve spin) is a covariant statement. Hole-theory forms are re-expressions.
- **H4:** Pass. 13 scripts in calc/, all rerun in cycle 7 from inside calc/ with saved outputs. L01 scripts are referenced by path.

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
