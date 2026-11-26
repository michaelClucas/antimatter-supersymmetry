# Referee G (theory, adversarial) - L01b, cycle 9 text

Read: OVERSEER_PROMPT.md (scope, verification gate), CONSTRAINTS.md, PROPOSAL.md, WORK.md (all), calc/c9_twin_antimatter.py + out, calc/c9_symmetry_group.py (header and part 1). Other REVIEWS_* and LITCHECK files not read.
Independent script: `calc/refG_check.py` -> `calc/refG_check_out.txt` (numpy + sympy only, imports nothing from tools/ or other calc scripts).

**Verdict: MINOR.** No fatal error, no BSM content used as a mechanism. I tried to build a counterexample to the CLAIM from every class in the brief and did not find one. The H^c argument is correct and correctly stated. Two classes of SM-internal structure are missing from or mis-argued in the enumeration (scale invariance reasoning, BRST / worldline SUSY); neither breaks the claim, both should be fixed in the text.

---

## 1. Independent checks (`calc/refG_check_out.txt`)

| # | statement in WORK | result |
|---|---|---|
| 1 | \|H\|² + \|H^c\|² = 2\|H\|², H^c†H ≡ 0, real Jacobian of (H, H^c) w.r.t. H has rank 4 | confirmed (1000 random H, max deviation 0; finite-difference rank 4) |
| 2 | H ↔ H^c is a symmetry only as the custodial element | confirmed: H → H^c with fermions untouched maps (Q†H^c)t_R to −(Q†H)t_R, a different operator with mismatched hypercharge; needs t_R ↔ b_R, y_t = y_b, g' = 0 |
| 3 | iγ² S* (iγ²)⁻¹ = S (C commutes with Lorentz on Dirac spinors) | confirmed, max deviation 1.4×10⁻¹⁴ over 200 random Lorentz elements |
| 4 | sector totals W 3/2 g² + 2λ, Z+h 3/4(g²+g'²) + 4λ, fermions −6y_t² − 6y_b² − 2y_τ²; C = (3/v²)(m_h² + 2M_W² + M_Z² − 4m_t²) | confirmed symbolically from field-dependent masses; pole form C = −4.068 with PDG 2024 centrals, matches WORK |
| 5 | counterfactual H_B := H^c: Hessian eigenvalues {0, 0, 0, −4κ} | confirmed by a separate derivation |
| 6 | (new) second-order rewriting of a fermion loop as a bosonic determinant | for any D with γ5 D γ5 = −D: 2 ln det(D+m) = ln det(m² − D²) to 10 digits. The fermion loop equals a boson-operator determinant with the opposite power. SM content does map fermion loops onto boson-type loops, but the (−1)^F sign survives the map, so no cancellation follows |

## 2. Counterexample attempts

| candidate | outcome |
|---|---|
| Custodial SU(2)_L×SU(2)_R | Fails as counterexample. Acts as identity on (λ, g, y); custodial limit C = 9/4 g² + 6λ − 12y² is further from zero. WORK §4b/§4d correct. |
| H → H^c as an antimatter "twin" Z₂ | Fails. Space of Higgs bilinears is 1-dimensional; the swap is iσ₂ ∈ SU(2)_R (check 2 adds that alone it is not even a symmetry of the Yukawas). Argument correct and correctly stated (see §3). |
| Antitop as top partner | Fails. Same Dirac field, already 2 of the 4 states per colour in −6y_t². |
| Nonlinear realization / HEFT form of the SM | Fails. Writing H = (v+h)U/√2 is a field redefinition; h stays an O(4) singlet radial mode with no shift symmetry. WORK item 3 correct. |
| Reduction of couplings (Zimmermann) giving an RG-invariant Veltman relation | Fails on the measured trajectory (transverse crossing, slope/σ ≈ 90). WORK S5 correct, and correctly concedes the polynomial alone does not exclude it. Note the Λ² coefficient beyond one loop is scheme dependent, so "RG-invariant C = 0" is not even a scheme-independent notion; this strengthens the line's position and could be said. |
| Discrete symmetries combined with field redefinitions (generalized CP, h → −h with t_R → −t_R, Z₂ centre) | Fail. Linear redefinitions preserving renormalizability act diagonally on (λ, \|y\|) up to phases (c9_symmetry_group). Nonlinear redefinitions are not symmetries of the renormalizable Lagrangian; "symmetry up to redefinition" is an S-matrix symmetry and falls under CM/HLS for continuous groups. |
| Classical scale invariance (Bardeen) | Not a counterexample to the CLAIM as worded (it imposes no relation among couplings), but the line's stated reasons are partly wrong. See finding G1. |
| BRST / anti-BRST of the gauge-fixed SM | Not a counterexample (physical operators are BRST-closed, not exact; no relation among λ, y_t), but omitted. See finding G2. |
| Worldline supersymmetry of the spinning-particle (Feynman-Stueckelberg) form of the top loop | Not a counterexample (1D symmetry, broken by antiperiodic boundary conditions in the effective action; check 6 shows the sign survives), but it is the most natural "antimatter-language SUSY inside the SM" and is not addressed. See G2. |
| Asymptotic / large gauge symmetries (infinite-dimensional, evade CM via massless gauge bosons) | Spin-preserving, act on soft charges, impose no relation on λ, y_t. Omitted; one sentence would close it. |

## 3. Is "H^c is not an independent field, so it cannot be a twin partner" correct and correctly stated?

Yes. The load-bearing content is the dimension count of gauge-invariant Higgs bilinears (1 for {H}, 4 for an independent pair), which WORK gives explicitly; a Z₂ forces equal coefficients only between distinct invariants. The "rank-4 Jacobian" is true but nearly tautological (any function of H has rank ≤ 4); the operator count is the real argument and should be stated as the primary one. Precision point: WORK calls H^c "the antiparticle doublet" and lists C, CP, CPT as the operations; strictly, H → H^c is C composed with the global SU(2)_L element iσ₂ (equivalently SU(2)_R in bidoublet form). WORK §4d item 3 already says this in bidoublet form; the CLAIM statement could say it in one clause.

## 4. Findings

**G1 (MINOR, wording/logic). Scale invariance: the objections given do not do the work.** Route table and S6 dismiss classical scale invariance because it is "anomalous" and "broken by μ²". Neither restores a Λ² term: the trace anomaly is ∝ β-functions (logs), and a soft μ² regenerates only μ²-proportional corrections. Bardeen's point is that with SM content and a scale-respecting regulator the top Λ² term is absent, not cancelled. That is the strongest SM-internal objection to the informal reading of the CLAIM ("nothing in the SM protects m_h from the top's Λ²"). The CLAIM survives because (i) it is about a symmetry-enforced coupling relation, which dilatations do not impose, and (ii) the question scale invariance would answer (sensitivity to heavy thresholds) cannot be posed with SM content, which WORK already says. Fix: drop "anomalous" and "broken by μ²" as reasons in the route table; state that scale invariance removes rather than cancels the Λ² term, that this is a regulator statement (CONSTRAINTS G: not a result), and that the CLAIM is restricted to coupling relations.

**G2 (MINOR, completeness). Fermionic and non-spacetime symmetries missing from the enumeration.**
- BRST (and anti-BRST) is a nilpotent Grassmann-odd symmetry of the gauge-fixed SM Lagrangian. Its ghost loops cancel the unphysical gauge-boson modes: it is the one SM symmetry that does cancel boson loops against Grassmann loops. It evades CM/HLS through the indefinite metric. It cannot tie λ to y_t because |H|⁴ and (Q†H^c)t_R are BRST-closed and not exact, and its ghost contributions are already inside the ξ-independent sector totals. CLAIM item 2 (the group) and item 4 ("the only spin-changing algebra is SUSY") should mention it and say this.
- Worldline SUSY: in the first-quantized (Feynman-Stueckelberg) representation of the top loop, x^μ and ψ^μ are related by an N = 1 worldline supersymmetry. That is a boson-fermion symmetry that lives inside the antimatter picture the line tests. It is a 1D gauge symmetry fixing spin 1/2, the antiperiodic ψ boundary condition of the effective action breaks its global part (the periodic case gives the index / chiral anomaly instead), and the spacetime (−1)^F sign is unchanged (check 6). Item 1's "the sea and F-S pictures relabel the same Fock space" is true but does not address it. Add one paragraph.
- Asymptotic symmetries: one sentence.

**G3 (MINOR, claim scope).** The "strong argument, not a formal proof" label is present in the CLAIM, Verdict and §12, and is appropriate. Two places still read stronger than shown: (a) the CLAIM's first sentence "No symmetry of the SM Lagrangian ... enforces" is unqualified until two sentences later; move the qualifier into that sentence. (b) For continuous, linear, internal symmetries of the renormalizable SM the enumeration is actually complete (the global symmetry group with generic Yukawas is computable), so the line undersells that part and oversells the remainder. Split the statement: proven for linear internal symmetries; argued, over known mechanism classes, for inhomogeneous / nonlinear / spacetime ones.

**G4 (MINOR, gate 7).** G7 (C(M_t) ≠ 0 at ≥ 69σ, transverse crossing) is a retrodiction, and the line says so. It also cannot distinguish "no symmetry" from "an approximate symmetry broken hard" (custodial-type), so it tests the CLAIM only against exact or softly broken symmetries (soft breaking keeps C = 0). Say that explicitly. Whether a retrodiction meets gate item 7 is an overseer ruling.

**G5 (note).** WORK §6 "Open" still lists the novelty items as pending LITCHECK while LITCHECK_2.md exists in the folder. I did not read it (outside brief); the overseer should reconcile.

## 5. BSM content

None used as a mechanism. Stops, superpotential, H_B, t_B, twin/little-Higgs/folded-SUSY, pNGB cosets and extra dimensions appear only as comparison targets or computed counterfactuals, labelled as such (§10 A1). Neutrino mass enters only as a bound (A2). No reformulation used (A3).

## 6. Gate table

| gate item | status | note |
|---|---|---|
| 1. Specific claim about a SUSY result | Pass | negative result for #1 (and #4) |
| 2. SM content only | Pass | §5 above |
| 3. Runnable calculations for every quantitative step | Pass (spot-checked) | refG_check reproduces H^c identities, sector totals, C(M_t) pole form, twin eigenvalues; not every script rerun by me |
| 4. Every CONSTRAINTS entry addressed | Pass | §10 checklist complete, including E1/E5 n/a |
| 5. No fatal error / BSM (this referee) | Pass | MINOR only: G1-G4 |
| 6. Literature check | Not assessed | G5: WORK still says pending |
| 7. Falsifiable prediction or consistency check | Weak pass | retrodiction; overseer ruling (G4) |
