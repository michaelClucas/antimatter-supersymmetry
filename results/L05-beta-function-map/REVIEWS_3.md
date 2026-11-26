# L05 Referee 3 (independent; gate compliance and framing)

Read: OVERSEER_PROMPT.md (Research question, Scope, Verification gate), CONSTRAINTS.md, STATE.md directives (D4), PROPOSAL.md, WORK.md, calc/. REVIEWS.md and LITCHECK.md were not read before forming the verdict.

## Verdict: MAJOR ISSUES (fixable)

No fatal error. No BSM content enters a mechanism: H^c-as-independent-field, T_dbl, Φ*, the MSSM and the toy parents are all flagged as comparison targets and A1-forbidden as mechanisms. All six scripts reproduce their committed outputs byte for byte. The algebra spot-checks (SM/MSSM b_ij, B = 115/218 and 5/7, r = −1/11 and −2/3, the counterexample ratios) hold. The problems are in how precisely the D4 negative is stated, and in one overstated attribution.

## Gate item 3: scripts rerun

Run from `calc/` with a 550 s timeout each: `beta_map.py`, `running.py`, `c4_doubling.py`, `c4_threeloop.py`, `c6_scope.py`, `referee1_check.py`. All exit 0, and every assert passes. stdout is identical to the committed `.txt` files, ignoring a BOM and CRLF line endings. The WORK.md numbers I checked match the outputs: running table (3.20 / 0.0738, 0.40 / 0.1289, 0.09 / 0.1202, 0.05 / 0.1168), partial-map B and α_s, Yukawa c_i, counterexamples 1, 3/2, 199/104, 8/7, 26/25, 389/199, and the three-loop 8/13 and 2/7. Pass.

## Findings

### 1. [MAJOR] The D4 negative has no stated class of excluded maps, and in its broad wording it is false for the Yukawa part of the gauge beta function
Location: CLAIM (b); C4.2 "Role of H^c"; C4.6 item 2 ("The beta function cannot tell H^c from any other copy").

Problem: "No structure-preserving map from SM beta functions to SUSY beta functions is specific to antimatter" never says which maps are excluded. The proof holds only for maps whose output depends on gauge-only data (S_i, C_j, spin): b_i and the gauge part of b_ij. These are invariant under R → R̄, so they cannot see conjugation. The full two-loop gauge beta function also contains Yukawa terms c_i^f y_f², and those can see conjugation through gauge invariance. With H_d = H^c (Y = −1/2), the superpotential terms Q H_d d^c and L H_d e^c are allowed. With a second Y = +1/2 doublet in its place, they are not (hypercharge sum 1 ≠ 0), so y_b = y_τ = 0 and the c_i differ. Anomaly coefficients A(R̄) = −A(R) also distinguish the two choices. So "a second Y = +1/2 doublet is indistinguishable" holds only for b_ij, not for the beta function. The line itself notes that the SM Yukawas already use H^c (§1.2), so this is exactly where the conjugate carries structure.

The phrase "structure-preserving" also has no definition. §2.6 tests the rep-space Killing metric, b-space and coupling space, but CLAIM (b) does not say that the negative is limited to those.

Fix: restate (b) as a statement about a defined class. Suggested form: "For any map Ψ on field content, the gauge-only coefficients b_i and b_ij of Ψ(T) are unchanged when any field in the image is replaced by its conjugate. So gauge-coefficient data cannot certify an antimatter reading of Ψ." Then state separately that the Yukawa terms and anomaly constraints do see R vs R̄. Say whether that counts as antimatter-specific: it is hypercharge bookkeeping already present in the SM's single H, and it does not touch one-loop B. Then explain why this does not rescue a unification mechanism.

### 2. [MODERATE] "Any equivalent formulation" is covered only implicitly; Prop. 1 covers relabellings only
Location: §1.1 Prop. 1, §1.3, Open question (c), Conclusion item 6.

Problem: gate item 1 asks for a negative about SUSY result #2 that holds in any equivalent formulation. Prop. 1 covers CPT-invariant relabellings of the SM state set. Furey is used only in the SU(3)×U(1)_em sector, Dixon is not examined, and Open question (c) leaves the full division-algebra structure open. The actual proof for all reformulations is one line: A3.4 requires an equivalent formulation to reproduce SM physics, so its gauge beta functions are the SM ones up to scheme redefinitions, which the line already shows leave b_i and b_ij unchanged. With that line, a division-algebra map restricted to the SM sector cannot change B, and Open question (c) does not bear on the negative. Without it, a reader can object that the excluded class omits the reformulations the prompt explicitly allows.

Fix: add this argument to CLAIM (b) or Conclusion item 6. Say plainly that the #2 negative ("SM antimatter, in any equivalent formulation, gives SM running, which does not unify") is standard. The new content is the accounting and the identity.

### 3. [MODERATE] The "15% of the B shift" attribution depends on the order of the steps, so it is not an exact decomposition
Location: §2.2 table and text; Conclusion item 5; cycle-3 H1 entry ("The 15% / factor-2 attribution is an exact decomposition, not a fit").

Problem: B = (c − nh/2)/(2c + nh/5) is nonlinear in r, so the B increment from promoting H^c depends on which steps came first. Applied first, it gives 0.5275 → 0.5556 (ΔB = 0.028, 15% of 0.187). Applied after H → chiral (r = −3/11 → −6/11, B = 0.5841 → 0.6731), the same doubling gives ΔB = 0.089, about 48%. Only the multiplicative statement in r, a factor 2 out of 22/3, is independent of order.

Fix: drop the 15% figure or label it "first step in this ordering". Keep the factor-2-in-r statement. Correct the H1 checklist wording.

### 4. [MODERATE] Gate item 7 is satisfied only in a weak sense
Location: CLAIM (c).

Problem: the theorem is proved from the Machacek-Vaughn and SUSY general formulas, and the published SM and MSSM tables were computed from the same formulas. The "check" can therefore only catch transcription or computation errors in the tables. A correct table cannot falsify it. The line says this honestly ("this check is mathematical"), and the overseer has accepted it. Still, it is a weaker reading of "could be tested or falsified" than the gate wording suggests. C4.6 4(b) already names a better candidate with an outcome not known in advance: compute the fully mixed three-loop scalar weight w_S from the general product-group three-loop formula (arXiv:1208.3357) and test whether Φ* gives a uniform 2³ (w_S = −4).

Fix: either do C4.6 4(b) and make it the gate-7 item, or have the overseer record that gate 7 is met as a mathematical consistency check only, with no physical falsifiability.

### 5. [MINOR] The coupling-space statement is overstated
Location: §2.6 "RG flow"; Conclusion item 4.

Problem: "there is no nontrivial map on coupling space intertwining the two flows other than the trivial affine ones" is wrong as written. At one loop both flows are constant-vector translations in α⁻¹ space, so any invertible linear A with A·b_SM ∝ b_MSSM conjugates them, up to rescaling t. There are infinitely many such maps. The correct point is that these maps exist without constraint and carry no information, and that requiring A to fix the unification locus (the (1,1,1) line) together with the measured boundary data rules them out.

Fix: reword to that statement.

### 6. [MINOR] The CONSTRAINTS checklist omits E1 and E5
Location: cycle-6 checklist.

Problem: E1 (Ω_c h²) and E5 (dark matter properties) are not listed. D1 puts dark matter out of scope, but gate item 4 requires every entry to be addressed in writing. Separately, the C1 entry says "m_H = 125.1 GeV", but `tools/sm_inputs.py` uses 125.20 (PDG), so only the label is wrong.

Fix: add "E1, E5: not used (dark matter is out of scope per D1)" and change the C1 label to 125.20.

### 7. [MINOR] Labels
- CLAIM (b) is tagged [established]. Downgrade it to the scoped statement of finding 1, or tag the broad wording as interpretation.
- §1.3: the Furey ideal assignments are "[unverified], from memory". They are used for no number, so this is harmless, but it reinforces finding 2: the negative should not lean on Furey at all.

## Gate item 6: novelty
A quick web search (MSSM vs SM two-loop b_ij, factor 2 on mixed terms, chiral-multiplet weights) found no source that states the off-diagonal doubling identity or its scope. The MSSM and SM matrices are printed side by side in many unification papers (e.g. arXiv:1907.10238), so the factor 2 is visible to anyone who compares them. The novelty claim is credible as "not found as a stated, scoped identity". It is not credible as a discovery. CLAIM (d) is already worded about right ("not proof of absence", "elementary").

## Gate items 1, 2, 4: summary
- Item 1: the line makes a specific negative claim about #2 and answers D4, but finding 1 (class of maps) and finding 2 (all formulations) must be fixed for it to count as a proof rather than an argument.
- Item 2: pass. No SM-external content in any mechanism.
- Item 4: pass apart from finding 6.
