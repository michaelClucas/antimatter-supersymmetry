# REVIEWS - L01b

## Referee 1 (cycle 4)

**Verdict: MAJOR ISSUES (fixable)**

No BSM content enters a mechanism (SUSY appears only in pair_matching.py Part 3-4 as a comparison target), and the scripts run and reproduce every number quoted in WORK.md. I reran all three scripts from `calc/`; outputs match the committed `_out.txt` files. The one-loop algebra checks out: per-species C_i, the channel form of the Veltman condition in Section 3 (both sides are 2C, so the factor of 2 is harmless), the 1-loop SM beta functions in symmetry_scan.py (16π²β_λ = 24λ² + 12λy² − 6y⁴ − 3λ(3g²+g'²) + 3/8(2g⁴+(g²+g'²)²), β_y, b_2 = −19/6, b_Y = 41/6), the g' normalization (`gY` from tools/rg_sm.py is the SM g', not GUT g1), the crossing slopes (0.35 dec / 0.29 GeV gives 1.2 dec/GeV; 0.52 dec / 0.0009 gives about 0.6 dec per 0.001), and the MSSM electroweak supertrace. The problems are in what the line concludes from these numbers.

### 1. MAJOR: the "self-conjugacy carried sector by sector" result (Sec. 1b, Verdict Holds #2) is wrong as stated for the MSSM, and trivial where it holds
**Location:** WORK.md §1b and §6 Holds-2; pair_matching.py Part 4 (charge-resolved block).
**What is wrong:**
- (a) Part 4 includes only gauge bosons, the two Higgs doublets and the electroweakinos. In the full MSSM the sfermion D-terms contribute field-dependent masses Δ_f = (T3 − Q s_W²) cos2β M_Z², i.e. (g²T3 − g'²Y... ) × (v_u² − v_d²) pieces. In the Q = 0 sector this includes the three sneutrinos (T3 = +1/2, Y = −1/2) and nothing else among sfermions, so Tr_{Q=0}(T3) and Tr_{Q=0}(Y) over sfermions are nonzero. The neutral-sector supertrace then has an uncancelled field-dependent piece ∝ (v_u² − v_d²) whose second derivative with respect to h_u or h_d is nonzero. The total cancels only after summing over the whole generation (Tr Y = 0, Tr T3 = 0), which mixes charge sectors. The script's own comment ("sfermion D-terms cancel separately since Tr Y = 0 per generation") is exactly this cross-sector cancellation. So "SUSY cancels within the neutral and charged EW sectors separately" holds only for the gauge+Higgs subsector, not for the MSSM.
- (b) "Neutral" is not "self-conjugate". Sneutrinos are neutral complex scalars carrying lepton number, so they are not self-conjugate. Neutralinos are Majorana because the neutral gaugino/higgsino mass matrix is symmetric and no conserved charge forbids Majorana masses, not because of any link to the self-conjugacy of Z or h. A neutral Dirac partner would cancel the same supertrace.
- (c) Where the Higgs/gauge-subsector cancellation does hold, it follows directly from [Q_em, SUSY generators] = 0: superpartners have the same electric charge, and the sum rule holds within each charge block of the block-diagonal mass matrices. Calling it "a new structural fact [established]" overclaims. It is also a contradiction in terms, since [established] means measured or proven with a citation (CONSTRAINTS tag definition), and here the line computed it itself.
**Fix:** Add the sfermion D-term contributions by charge sector to Part 4 and report the result. Restate the claim as "within the gauge+Higgs subsector, charge sectors cancel separately, a consequence of [Q, SUSY] = 0". Drop the self-conjugacy reading, or support it with something beyond charge conservation. Retag as [computed].

### 2. MAJOR: "self-conjugacy blocks protection" (Sec. 4, Verdict Fails-2) is a non sequitur
**Location:** WORK.md §4 "Why self-conjugacy blocks protection"; symmetry_scan.py (2).
**What is wrong:** The group-averaging argument applies to any scalar, real or complex. For a complex scalar under any unitary linear symmetry, φ†φ is invariant. Stops are complex, not self-conjugate, and their mass is not symmetry-protected either. Observation (a) therefore plays no role. The real distinction is Lorentz structure: a fermion mass is a holomorphic bilinear ψψ (with no conjugate), which carries charge 2α, while a scalar mass is φ*φ (or φ² for a real field), which is always neutral. That is observation (c) alone. The sentence "(a) and (c) together are the precise reason" is wrong about (a). The 4×4 group-average numerics illustrate a standard fact (compact groups act orthogonally on real reps) and add nothing beyond it.
**Fix:** Attribute the absence of protection to the bilinear structure of spin-0 mass terms, which applies to every scalar, and state explicitly that self-conjugacy is irrelevant. Correct Verdict Fails-2 to match.

### 3. MAJOR: the falsifiable check (M_t = 169.5 GeV, "−10.5σ") is not a test of anything the line proposes, and its significance is overstated
**Location:** WORK.md §5, §6 "Falsifiable check"; matching_running.py `Mt_for_zero_at`.
**What is wrong:**
- (a) The line proposes no mechanism under which R = 1 at M_Pl should hold. "C = 0 at M_Pl needs M_t = 169.5" is the Veltman-condition-at-high-scale statement already in Hamada-Kawai-Oda (1210.2538), Masina-Quiros (1308.1242) and Jones (arXiv:1309.7335). Excluding a hypothesis nobody makes does not satisfy gate item 7 as a check on this line's claims.
- (b) The σ uses only the experimental ±0.29 GeV on the direct M_t. Omitted:
  - α_s: by the line's own slopes, ±0.0009 is equivalent to about ±0.43 GeV of M_t.
  - The relation between the MC mass and the pole mass, ~0.3 to 0.5 GeV or more (the cross-section pole mass in PDG has about ±0.7 GeV).
  - Theory error in the Buttazzo y_t matching.
  - The linear Buttazzo fit extrapolated 3 GeV from 173.34, which the line itself flags.
  
  Added in quadrature these give ~0.8 GeV and about 3.5-4σ, not 10.5σ.
- (c) The scheme ambiguity is the bigger problem. A one-loop Λ² coefficient is evaluated with 3-loop MS-bar couplings. At two loops the coefficient is scheme dependent (Einhorn-Jones; Al-sarhi-Jones-Jack hep-th/9209124; Jones 1309.7335). The 1-loop versus 3-loop RGE shift of μ₀ (26.8 to 22.8 decades) shows how fragile the crossing scale is. The M_t that gives R = 1 at a fixed scale inherits this ambiguity, and the line does not estimate it.
**Fix:** Present the M_t numbers as a consistency statement ("the SM does not satisfy the Veltman condition at M_Pl"), credited to HKO/Masina-Quiros. Quote the significance with α_s, pole/MC and matching errors included, plus a scheme-variation estimate (for example adding HKO's 2-loop coefficient, or varying the K² versus Λ² definition). If the line wants a genuine falsifiable item, it needs one tied to its own claims.

### 4. MAJOR (gate items 1, 6; H3): the positive "Holds" items are a relabelling of the Veltman coefficient
**Location:** §1a, §2 "What matches", §3, §6 Holds-1 and Holds-3.
**What is wrong:** Calling every Λ² piece a "pair term", "Dirac sea" or "zero-point pair" is a vocabulary choice. For a one-loop vacuum-energy/effective-potential computation every term is a zero-point or sea term by construction. "Right sign, pair structure, 13 vs 12 dof" for the SM bosons restates C_bos > 0. The fractions R = 0.34/0.67/0.79/1.0 are just (6λ + 9/4 g² + 3/4 g'²)/(6y_t² + 6y_b² + 2y_τ²) along the standard running, which HKO already compute. Under H3 the antimatter language adds no derived content beyond the covariant Veltman coefficient. Mode-by-mode cancellation "to machine precision" (Part 2) holds trivially, because the stop and top integrands are coded as the same function with opposite sign.
**Fix:** State plainly that §§1-3 are a re-expression of the known one-loop result, and that the line's actual output is the no-go in §4 (once corrected per finding 2) plus the comparison table. The literature checker should assess novelty against HKO, Masina-Quiros, Jones 2013 and Kolda-Murayama.

### 5. MEDIUM: wrong MSSM claim about the residual p² log
**Location:** WORK.md §1a bullet "The second is a p² (wave-function) log that the MSSM top-higgsino loop removes"; pair_matching.py Part 3 print.
**What is wrong:** No one-loop Higgs-boson self-energy diagram contains a top and a higgsino. The superpotential y H Q U gives h-t-t and h̃-t-t̃ vertices, but no h-t-h̃ vertex. The top-higgsino-stop loop belongs to the higgsino and stop self-energies. The Higgs wave-function log −(3y_t²/8π²)p² ln Λ is physical in SUSY too: it is the Kähler (wave-function) renormalization γ_{H_u} = 3y_t²/16π², which non-renormalization does not forbid.
**Fix:** Delete the claim. State that the p² log is the Higgs anomalous dimension and is present in the MSSM.

### 6. MINOR: gauge dependence is partly stated, partly not
**Location:** §2 table, "Counting" and "Coupling strength" bullets.
**What is wrong:**
- R, C_bos and the charged versus neutral sector totals are ξ-independent at the Λ² level. In R_ξ the Goldstone (+ξa_V), the extra vector mode (+ξa_V) and the two ghosts (−2ξa_V) cancel within each charge sector. The line should say so, because it makes the 34%/79% numbers gauge-invariant.
- The "13 real massive boson dof" count, the "mean a per dof = 0.138", and the "4.1 stop-equivalent dof" are Landau-gauge artefacts: in unitary gauge the count is 10, and in R_ξ ghosts enter with negative weight. Massless Landau Goldstones are also counted as "massive".
- The Part 2 IR negativity of the h/G modes is partly a Landau-gauge artefact (massless G).
**Fix:** Add the ξ-independence argument for the sector totals. Label the dof count and per-dof averages as Landau-gauge specific.

### 7. MINOR: inconsistent or loose statements
- pair_matching.py Part 2 prints "SM boson pairs have the right sign at every k". Its own table has negative h+G entries at k = 10 and 50 GeV (ratio −26306 at k = 10). WORK.md has the caveat right, so fix the script string.
- §6 Fails-1 says "about 3× too weakly for μ ≲ 10¹⁰ GeV". At 10¹⁰, R = 0.51, i.e. 2×.
- "Observation (b) is realized in SUSY" (§1a): the equal y_t² quartics for t̃_L and t̃_R come from the F-terms |∂W/∂U|² and |∂W/∂Q|² of the one superpotential term (holomorphy). They do not come from an L↔R symmetry of the Yukawa. A Dirac mass always involves both chiralities equally.
- symmetry_scan.py (1): for C, P and CP the output is a hard-coded string, not a computation, and it is applied to non-gauge-invariant comparison operators where it is meaningless ("odd power of H … allowed iff coupling real"). "Checked symbolically" for C's invariance is true but trivial, since C depends only on |y_t|², λ, g², g'².
- The [established] tag is used throughout for the line's own computations (§§1b, 2, 3, 4, 5). Per the CONSTRAINTS tag definitions use [computed] or [derived here].

### 8. MINOR: citations
- Einhorn & Jones, PRD 46, 5206 (1992), "The effective potential and quadratic divergences": verified (INSPIRE 32379).
- HKO PRD 87, 053009, arXiv:1210.2538: correct.
- Masina & Quiros, arXiv:1308.1242: published as PRD 88, 093003 (2013) (from memory, not re-verified). Add the journal ref after checking.
- Missing and directly relevant: D.R.T. Jones, "The quadratic divergence in the Higgs mass revisited", arXiv:1309.7335 (PRD 88, 098301), which discusses the two-loop and scheme issues of the Veltman coefficient and HKO's result. Also Al-sarhi, Jack, Jones, hep-th/9209124, on regularization dependence of quadratic-divergence cancellations (H2).

### Constraint checklist audit
- A1 passes. SUSY is used only as a comparison target.
- A2 passes, but the "Dirac y_ν < 10⁻¹²" sentence assumes a Dirac mechanism. Rephrase it as "any neutrino-mass mechanism contributes < m_ν²/v² ~ 10⁻²⁵ to C", which makes it mechanism-insensitive as A2 requires.
- H1 passes: the dof count and the sector near-equality are flagged.
- H2 needs the scheme-dependence estimate from finding 3c.
- H3 is only weakly satisfied (finding 4).
- No constraint is violated outright.

### Summary for triage
Nothing fatal, and no BSM leakage. The SM numerics are right. Four of the interpretive headline claims need correcting or downgrading:
- the MSSM self-conjugate sector cancellation (fails once sfermions are included, and is trivially charge conservation otherwise)
- "self-conjugacy blocks protection" (self-conjugacy is irrelevant)
- the 10.5σ falsifiable check (overstated significance, scheme dependent, and not a test of the line)
- the top-higgsino p² claim (false)

After the fixes the line is a correct but largely known restatement of the Veltman-condition literature. Its scope for passing gate items 6 and 7 is limited.
