# L01b WORK - Self-conjugate Higgs vs SUSY's Higgs-mass protection

Single line for SUSY #1 (Higgs-mass protection) and #4 (radiative EWSB). L01-weisskopf-hierarchy is merged in by reference (Section 7).

Tags (CONSTRAINTS convention, refined per Referee 1 c4 finding 7):
- **[established]**: published or textbook result, citation given.
- **[computed]**: derived or computed in this line, with a committed script and saved output.
- **[conjecture]**: argued but not proven. **[speculation]**: outside what the line can test.

---

## CLAIM

**Statement.** Using only SM fields, the one-loop quadratic (Λ²) coefficient of the Higgs mass, C = (1/2)∂²_φ STr M²(φ), splits into three groups by physical particle:

| sector | contribution to C |
|---|---|
| W sector (W±, with the eaten G± and the ghosts) | 3/2 g² + 2λ |
| Z sector (Z with G⁰ and ghosts) plus h | 3/4 (g² + g'²) + 4λ |
| fermions | −6y_t² − 6y_b² − 2y_τ² |

1. Each sector total is independent of the gauge parameter at every φ. This holds in R_ξ, Fermi and background-field R_ξ gauges, with ξ_W and ξ_Z independent. The totals are the same with a hard cutoff, Pauli-Villars and the d = 2 pole of dim reg. [computed: `calc/c4_rxi_split_out.txt`, `calc/c4_regulator_running_out.txt`]
2. Both boson sectors enter with the sign the stops have in SUSY. The charged W± sector and the self-conjugate Z + h sector do so equally, so self-conjugacy makes no difference.
3. The bosons cancel only a fraction R = C_bos/|C_ferm| of the fermion term: R = 0.344 at M_t (0.169 charged + 0.175 self-conjugate), 0.790 at M_Pl, and R = 1 at μ₀ = 10^22.83 GeV. This uses 3-loop MS-bar running with Buttazzo et al. matching. With Jegerlehner's y_t matching, μ₀ = 10^16.1 GeV and R(M_t) ≈ 0.37 (Section 5c). [computed]
4. No SM symmetry enforces R = 1. C is invariant under every candidate symmetry, and C = 0 is not an RG-invariant surface. [computed]
5. The experimenter's analogue (STATE D2: (a) h is self-conjugate, (b) the Yukawa is L↔R symmetric, (c) bosons carry no chirality) fails at (c) alone:
   - A spin-0 mass bilinear contains the conjugate field (φ*φ), or is the square of a real field (h²). Either way it is neutral under every linear internal symmetry, for real and complex scalars alike.
   - A Weyl mass ψψ has no conjugate, so a phase rotation can forbid it, whether the fermion is Majorana or Dirac.
   - Self-conjugacy (a) is irrelevant: stops are complex and equally unprotected. (b) protects fermion masses, not h². [computed: `calc/symmetry_scan_out.txt` (2); the underlying fact is established, 't Hooft 1980]
6. SUSY #4: the SM has no radiative EWSB, either Coleman-Weinberg or RG-driven. See L01, merged in Section 7. [computed in L01]

This is a **negative result** for SUSY #1 and #4. SM antimatter, in any of the three forms (a)-(c), does not reproduce SUSY's protection of m_h². What survives is a gauge-invariant, quantitative statement of how far the SM boson sectors fall short.

**Status:** CONTINUE (fix round cycle 5). Candidate for the verification gate as a negative result. Referees so far: 0/3 clean.

**Falsifiable checks** (none is a test of new physics, and the line claims none):
- **F-a (sector gauge invariance).** In any linear gauge that preserves U(1)_em, the W-sector and Z+h-sector totals must equal 3/2 g² + 2λ and 3/4(g²+g'²) + 4λ exactly. Any ξ-dependence in either sector falsifies item 1. This item is specific to this line.
- **F-b (Veltman condition at M_Pl).** This repeats Hamada-Kawai-Oda and Masina-Quiros with updated inputs. It is not a new test.
  - C(M_Pl) = 0 needs M_t* = 169.54 GeV.
  - Full error budget: α_s, MC-vs-pole and renormalon ambiguities of the top mass, y_t matching, RGE order, and the 1- vs 2-loop Λ² coefficient. These total 0.74 GeV, so the measured 172.57 GeV is **4.1σ** from M_t* within Buttazzo-type matching. With the experimental error alone it would be 10.5σ.
  - Under Jegerlehner's matching the condition at M_Pl is not excluded (Section 5c).
  - [computed: `calc/c5_mt_budget_out.txt`]
- **F-c (where μ₀ sits).** μ₀ is set almost entirely by y_t(M_t): 10^16.1 GeV for y_t(M_t) = 0.900, 10^22.8 GeV for 0.933. A settled two-loop on-shell → MS-bar top-Yukawa matching decides between the two (`calc/c5_jegerlehner_out.txt`).

**What is new** (LITCHECK c4 §2-3):
1. The framing of Higgs self-conjugacy as an antimatter analogue of SUSY protection is not in print. Its precise failure point is new as a statement, though it is a negative result built from known pieces: the obstruction is (c), the Lorentz structure of spin-0 mass bilinears, and not (a).
2. The quantitative reconciliation of Jegerlehner's μ₀ ≈ 1.4×10^16 GeV with HKO/Masina-Quiros/this line's ≈10^23 GeV.
   - Starting from his Table 1 couplings, this line's 3-loop runner reproduces his zero (10^16.11 vs 10^16.15) and his M_Pl couplings.
   - Swapping one coupling at a time shows y_t(M_t) alone accounts for the 7.8-decade shift.
   - Jegerlehner himself names y_t as the cause (1304.7813, Introduction). New here are the numerical reproduction and the coupling-by-coupling attribution.
3. The explicit check that the charged/self-conjugate sector split is ξ-independent in three gauge families and the same in three regulators. This is known in substance: the Veltman coefficient is gauge independent, and Masina-Quiros Fig. 1 plots the pieces.

Everything else is known: the Veltman condition and its running zero (Veltman 1981; HKO 2013; Masina-Quiros 2013; Jegerlehner 2013), the per-charge-block SUSY sum rules (Martin §7.4), the symmetry arguments ('t Hooft 1980), and the hole-theory bookkeeping.

---

Scripts and outputs (all rerun cycle 5 from inside `calc/` and reproduced):
- `calc/pair_matching.py` → `pair_matching_out.txt` (species table, mode-by-mode, time orderings, SUSY comparison incl. sfermion D-terms)
- `calc/symmetry_scan.py` → `symmetry_scan_out.txt` (symmetry scan, bilinear structure, RG test)
- `calc/matching_running.py` → `matching_running_out.txt` (R(μ), μ₀)
- `calc/c4_rxi_split.py`, `calc/c4_regulator_running.py` (gauge and regulator independence; log-level R4)
- `calc/c5_jegerlehner.py` → `c5_jegerlehner_out.txt` (Jegerlehner vs HKO crossing)
- `calc/c5_mt_budget.py` → `c5_mt_budget_out.txt` (M_t* error budget)

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
  - The soft-mass log is −(3y_t²/8π²)(m_Q² + m_U² + A_t²) ln Λ [established, standard; Martin hep-ph/9709356 eq. (1.13) gives the generic form m_soft² (λ/16π²) ln(Λ/m_soft); the stop-specific coefficient is verified symbolically in Part 4].
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
- **Magnitude** [computed]: R = 0.344 at M_t, so the total |C| drops from 5.22 to 3.43. At 10^10 GeV R = 0.508, i.e. the bosons fall short by a factor of 2 there. The cycle-4 text said "3× for μ ≲ 10^10", which was wrong at 10^10 (finding 7).
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

## 4. Symmetries acting on h (symmetry_scan.py)

**Operator and spurion scan [computed]:**
- C, P and CP map each Higgs-sector operator to its hermitian conjugate. They only require real couplings, and μ²|H|² is allowed.
  - This holds by the definition of the map, not by computation (finding 7). The non-gauge-invariant comparison operators are no longer printed for these maps.
- h → −h alone forbids the Yukawa unless y_t → −y_t. It allows μ²|H|².
- h → −h with t_R → −t_R is an exact SM symmetry: the SU(2) centre element times a (3B+L) rotation by π. It forbids a bare Dirac mass and allows μ²|H|².
- U(1)_H, chiral U(1)_A and the combined PQ-like U(1) each allow μ²|H|².
- Custodial symmetry allows |H|², which is the O(4) norm.
- C = 6λ + 9/4 g² + 3/4 g'² − 6|y_t|² depends only on invariant combinations, so no candidate can force C = 0. This is true but trivial (finding 7).

**Why there is no protection: observation (c), not (a)** [computed illustration of an established fact; 't Hooft, NATO Sci. Ser. B 59, 135 (1980)]
- A scalar mass bilinear is φ*φ (complex) or h² (real). Under any unitary or orthogonal linear symmetry it is invariant. This holds equally for the self-conjugate h and for complex scalars such as stops, which are not protected either.
- A Weyl fermion mass ψψ is holomorphic in ψ, with no ψ* in it. Under ψ → e^{iα}ψ it picks up e^{2iα}. This applies to a Majorana gaugino (U(1)_R) and to a Dirac fermion, whose axial rotation acts on its two Weyl components.
- So the parallel between h and a gaugino breaks at the Lorentz structure of the mass term, which is observation (c). **Self-conjugacy (a) plays no role** (finding 2, accepted; the cycle-4 sentence "(a) and (c) together" is withdrawn). The 4×4 group-average matrix in the output only illustrates the standard fact that compact groups act orthogonally on real representations.
- (b), the L↔R-symmetric Yukawa, together with the exact Z₂ (h → −h, t_R → −t_R), protects the **fermion** mass (m_t ∝ y_t⟨h⟩). It does nothing for h².

**RG test [computed]:**
- On the surface C = 0, the one-loop β_C is 33g⁴ + 63/2 g²g'² − 162g²y² + 96g₃²y² + 17g'⁴ − 46g'²y² + 126y⁴ (per 16π² dlnμ), which is not identically zero.
- At the 3-loop crossing μ₀, dC/dlnμ = +0.0203.
- So C = 0 is a point the flow passes through, not a symmetry relation. In SUSY, λ_{h t̃ t̃} = y_t² is an F-term identity that running preserves [established].

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

- **4.1σ** within Buttazzo-type matching. The cycle-4 figure of "10.5σ" used only the experimental error and is withdrawn (finding 3b).
- This restates the HKO and Masina-Quiros result that the SM does not meet the Veltman condition at M_Pl. Here it is updated to PDG 2024 inputs with an error budget. It is not a test of any mechanism proposed by this line (finding 3a, accepted).
- Not in the budget: the Jegerlehner matching spread (Section 5c), equivalent to about 6.8 GeV. If that matching is admitted, C(M_Pl) = 0 is not excluded.
- Further scheme caveat [established]: beyond one loop the Λ² coefficient is scheme dependent. Einhorn & Jones, PRD 46, 5206 (1992); Al-sarhi, Jack, Jones, hep-th/9209124 (regularization dependence); D.R.T. Jones, PRD 88, 098301 (2013), arXiv:1309.7335, who disputes HKO's two-loop coefficient. The C1 → C2 row above is one estimate of that spread, not a bound.

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

**Holds** [computed, gauge and one-loop-regulator independent]:
- The sector split and signs of the CLAIM.
- R = 0.344 at M_t and 0.790 at M_Pl, with R = 1 at 10^22.83 GeV (Buttazzo matching) or about 10^16 GeV (Jegerlehner matching).

**Fails** [computed]:
- Magnitude: the bosons fall short by 2-3× below 10^10 GeV.
- No symmetry: C is invariant under every candidate and C = 0 is not RG invariant.
- Wrong sector pairing compared with SUSY.
- Self-conjugacy is irrelevant to scalar mass protection. The obstruction is (c).

**Not claimed:** any physical reading of μ₀, e.g. "SUSY restored at μ₀" (HKO) or "EW phase transition at μ₀" (Jegerlehner) [speculation, outside SM scope]. A d = 4 dim-reg observable for R: in DR the Λ² term is absent and the SM has no heavy thresholds (CONSTRAINTS G).

**Open:**
- Whether a reformulation (A3) could tie λ, g, g' to y_t at μ₀ without using its extra high-scale relations (A3.2). No candidate is known.

## 7. Merged from L01-weisskopf-hierarchy (by reference)

L01 is support for this line, and L01b is the single line for SUSY #1 and #4. Calculations reused, all under `lines/L01-weisskopf-hierarchy/calc/` (rerun in a scratch copy, cycle 5):
- `weisskopf_ofpt.py`: hole-theory electron self-energy. The linear divergence cancels between particle-only and sea terms, leaving the covariant log 3α/2π. Chiral symmetry is the covariant reason.
- `higgs_top_ofpt.py`: top-loop time orderings (forward h → t t̄ and backward Z-graph), both negative. They agree with the covariant integrand to 8 digits. Also checked: Im Σ = m_h Γ(h → f f̄) and the light-fermion threshold structure.
- `veltman_running.py`: normalization δm_h² = CΛ²/8π² with the tadpole included, and the basis-independence of the trace (charged pair = rotated real fields).
- `cw_radiative_ewsb.py`: **SUSY #4.**
  - Coleman-Weinberg: with the tree mass term set to zero, B = −4.3×10⁻³ < 0, so the stationary point is a maximum and there is no radiative EWSB. The top threshold is 78.6 GeV, and W, Z alone give m_h = 9.8 GeV.
  - In MS-bar β(m²) ∝ m² at all orders, so the sign of m² is RG invariant and there is no RG-driven sign flip of the kind stop soft masses produce in the MSSM.
  - [established classics: Coleman-Weinberg PRD 7, 1888 (1973); Weinberg PRL 36, 294 (1976); Linde JETP Lett. 23, 64 (1976); reproduced in L01]
- L01's open issue m(M_Pl) = 139.4 vs 129.4 GeV in `tools/rg_sm.py` affects only the dimensionful m², which this line does not use.

## 8. Citations
- Weisskopf, Phys. Rev. 56, 72 (1939)
- Veltman, Acta Phys. Polon. B 12, 437 (1981)
- 't Hooft, NATO Sci. Ser. B 59, 135 (1980)
- Coleman & Weinberg, PRD 7, 1888 (1973); Weinberg, PRL 36, 294 (1976); Linde, JETP Lett. 23, 64 (1976) [via L01 LITCHECK]
- Einhorn & Jones, PRD 46, 5206 (1992)
- Al-sarhi, Jack, Jones, hep-th/9209124 [cited per Referee 1; content not read]
- D.R.T. Jones, PRD 88, 098301 (2013), arXiv:1309.7335 [via L01 LITCHECK]
- Martin, "A Supersymmetry Primer", arXiv:hep-ph/9709356, eq. (1.13), §7.4
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
| 2 | "self-conjugacy blocks protection" is a non sequitur | **Accepted.** §4 rewritten: φ*φ is invariant for complex scalars too, so the obstruction is the spin-0 bilinear structure, (c) alone. symmetry_scan.py (2) now prints the complex-scalar, real-scalar, Weyl and Dirac cases. |
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

## 10. CONSTRAINTS checklist (E1, E5 dropped per D1)
- **A1:** Pass. SM fields only in every mechanism. Stops, electroweakinos, sfermion D-terms and the MSSM Higgs potential appear only in pair_matching.py Part 3-4 as the SUSY comparison target.
- **A2:** Pass. Neutrino masses are not used. Any mechanism contributes at most m_ν²/v² ~ 10⁻²⁵ to C, so the result is mechanism-insensitive.
- **A3:** Pass. No reformulation is used. Hole theory and time orderings are bookkeeping only, checked against covariant integrands (7-8 digits). The open item about reformulations makes no claim.
- **B1-B8:** Pass. CPT: particle and antiparticle enter every C_i identically, and the basis-independence of the trace is shown in L01. No particle/antiparticle asymmetry is used.
- **B9, B10:** Pass. CP violation is not used. The CP scan only requires real couplings.
- **C1, C2:** Pass. PDG 2024 inputs (m_h 125.20, M_t 172.57 ± 0.29, M_W, M_Z) via tools/sm_inputs.py. M_t* is quoted with its full error budget.
- **C3:** Pass. Nothing BSM is introduced, so no superpartner signatures arise. The line claims no reproduction of the SUSY cancellation at accessible scales, consistent with the LHC null results.
- **C4:** Pass. No g−2 claim.
- **D:** Pass. Couplings from tools/, 3-loop running (2-loop for y_b, y_τ), stated. CPT-equal counting is used.
- **E2-E4, E6-E10:** Not applicable. No cosmology, baryogenesis, N_eff or neutrino-mass claims. Jegerlehner's inflation and phase-transition reading of μ₀ is not adopted.
- **F1-F3:** Pass. No baryon-number violation. The (3B+L) rotation by π is a global phase identity, not a process.
- **G:** Pass. Normalization as in CONSTRAINTS G (δμ² = CΛ²/16π², δm_h² = CΛ²/8π²). Only ratios, signs and zeros are used. The absence of Λ² in dim reg is stated (§6).
- **H1:** Pass. Flagged as having no mechanism: the near-equality of the sectors at μ₀, the R4 crossing (= λ near-criticality) and the Landau-gauge dof counts. No claim rests on them.
- **H2:** Pass (one loop). The sector split and R hold in cutoff, PV and d = 2-pole schemes. The scheme dependence beyond one loop is cited (Einhorn-Jones, Al-sarhi-Jack-Jones, Jones) and partly estimated (C1 vs C2). μ₀ is stated as scheme- and matching-dependent.
- **H3:** Pass. The antimatter vocabulary is explicitly a re-expression (§1). The claims are covariant statements (STr by sector, ξ-independence, symmetry no-go, RG flow).
- **H4:** Pass. Eight scripts with saved outputs in calc/, all rerun in cycle 5 and reproducing. L01 scripts are referenced by path.

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
- R2 (quadratic level) is the same in hard cutoff, PV and the dim-reg d = 2 pole.
- In d = 4 DR there is no such term (no observable).
- R4 (log level, gauge-invariant λ⁰ and λ² parts of STr M⁴): 0.138 at M_t, 0.345 at 10^10, 0.767 at 10^16, 1.113 at M_Pl; R4 = 1 at 10^18.19 (λ near-criticality, H1).

**C4.3** Per-diagram claims are gauge dependent and are not made. The symmetry no-go is gauge and regulator independent.
