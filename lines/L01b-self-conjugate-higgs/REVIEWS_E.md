# L01b Referee E (cycle 8, independent, adversarial)

Read: OVERSEER_PROMPT.md, CONSTRAINTS.md (A, G), STATE.md directives D1-D5, PROPOSAL.md, WORK.md (all), calc/c7_same_spin_out.txt, calc/symmetry_scan.py/out (custodial part). Did not read other REVIEWS or LITCHECK.
Own check script (not committed, outside repo): refE.py in the referee scratchpad. Code and output are quoted below so they can be reproduced.

**Verdict: MAJOR ISSUES (fixable).** No fatal error, no BSM content in any mechanism. The negative conclusion for SUSY #1 is correct. The stated *reason* for it ("the precise departure is items 1-3", spin preservation) is incomplete, because spin-preserving protection mechanisms exist (twin Higgs, little Higgs) and the closest structural analogue of D2's idea, a discrete exchange symmetry, is one of them. The line never tests it. Gate 7 is not met for the CLAIM itself.

---

## Referee calculation (reproducible)

```python
# H=(p1+i p2, p3+i p4)/sqrt2, H^c = eps H*, Phi=(H^c, H)
Tr Phi^dag Phi            = 2 |H|^2
Tr Phi Phi^dag - Tr Phi^dag Phi = 0            # L<->R element Phi -> Phi^dag leaves the mass term alone
Phi R^dag, R = i sigma2:  (H^c, H) -> (H, -H^c)  det R = 1
   # the particle<->antiparticle swap of the doublet is an ordinary SU(2)_R element (continuous, internal, spin 0 -> spin 0)
C general        = 9/4 g^2 + 3/4 g'^2 + 6 lam - 6 y_t^2
C custodial limit (g'=0, y_t=y_b=y) = 9/4 g^2 + 6 lam - 12 y^2     # no relation imposed; further from 0
|H|^2 + |H^c|^2  = 2 |H|^2     # "antimatter twin": H_B := H^c gives no new field, no enlarged U(4), no pNGB
At M_t (Buttazzo-type MS-bar): h self-loop 3 lam = 0.378, all scalars 6 lam = 0.756, top 6 y_t^2 = 5.267
   h share = 0.072, scalar share = 0.144
Top Dirac mass with complex y = a+ib: m^2 propto a^2+b^2 (phase removable by t_R rephasing)
```

---

## Findings

### 1. MAJOR. Same-spin protection (twin Higgs, little Higgs) omitted; "spin preservation is the departure" is overclaimed
- **Location:** CLAIM Statement ("within SM field content no other mechanism can"), item 5 route table, "Answer to D2" last sentence, §4a S2.
- **Problem:** The CLAIM defines SUSY #1 as the boson-fermion relation λ_{Ht̃t̃} = y_t² and then shows spin-preserving maps cannot produce it. Correct, but the top Λ² can also be cancelled by a *same-spin* partner enforced by a *spin-preserving* symmetry: the twin Higgs (Chacko, Goh, Harnik, hep-ph/0506256; a discrete Z₂ exchanging the SM with a copy, linear, commutes with J²) and little Higgs collective breaking (Arkani-Hamed, Cohen, Georgi, hep-ph/0105239). S2 correctly says y_t cannot be tied to λ by such maps, but twin Z₂ never ties y_t to λ; it ties y_t to y_t^B and makes the Λ² term ∝ |H_A|² + |H_B|², which is U(4)-invariant, so h becomes a pNGB. So step 1 (spin preservation) is not by itself the obstruction, and the "Answer to D2" sentence "the precise departure is items 1-3" is false as stated. This matters most for D2: a discrete particle↔antiparticle exchange is the closest structural cousin of the twin Z₂, and a fair test of the hypothesis has to say why C/CP/CPT cannot play that role.
- **Why the conclusion still holds (referee calc):** C, CP, CPT act inside the SM's own field space. The antiparticle of H is H^c = εH*, which is not an independent field: |H|² + |H^c|² = 2|H|². The "doubled" Λ² term is just the Higgs mass term again. No enlarged accidental symmetry appears, so h does not become a pNGB. The same holds for the top: t̄ is the same Dirac field, so "y_t = y_t̄" is CPT plus hermiticity, an identity, and cannot cancel anything. The twin mechanism needs a second copy of the fields, which A1 forbids.
- **Fix:** Add a route-table row "discrete exchange / twin Z₂, little Higgs (same-spin partners)": needs a second field copy or an enlarged global group, BSM. Add a step 2′: antimatter operations are automorphisms of the SM field space and don't double it (show |H|²+|H^c|² = 2|H|²). Restate the D2 answer as two departures: (i) no spin-changing operator (vs SUSY), (ii) no independent partner field (vs twin/little Higgs). Cite both papers after a literature check.

### 2. MINOR (borderline MAJOR for D2 fairness). The H ↔ H^c / custodial reading is not stated in antimatter language, and the custodial limit in symmetry_scan is wrong
- **Location:** §4b; calc/symmetry_scan.py lines ~101-106, symmetry_scan_out.txt line 74.
- **Problem:** (i) The "custodial limit" sets only g' → 0 and keeps −6y_t². Custodial SU(2)_R also needs y_t = y_b, which gives −12y². The printed expression is not the custodial limit. (ii) The line never says what the experimenter's bidoublet reading means: the swap (H^c, H) → (H, −H^c) is the SU(2)_R element iσ₂ (det 1). So "treating particle and antiparticle symmetrically" is ordinary continuous custodial symmetry: internal, spin-preserving, covered by S2. It leaves Tr Φ†Φ = 2|H|² invariant and imposes no condition on the Λ² coefficient. (iii) The custodial "L↔R" is not chirality L↔R. SU(2)_R rotates (t_R, b_R), and literal parity is broken maximally by the SU(2)_L gauge coupling, which enters C as 9/4 g².
- **Fix:** Correct the custodial limit (y_t = y_b, C = 9/4 g² + 6λ − 12y²). Add the three statements above with the iσ₂ check to symmetry_scan.py.

### 3. MINOR. Observation (a) is dismissed without crediting or quantifying what it does contribute
- **Location:** "Answer to D2" (a); §2; §3 Weisskopf table.
- **Problem:** The real h loop is gauge independent (no ξ in m_h²(φ)), it has the stop sign, and it is 3λ = 0.378, 7.2% of the top term. All scalars together give 14.4%. Per real dof the complex G± give the same λ as h, and that is the quantitative reason self-conjugacy is irrelevant. The line argues this only by basis independence and complex stops. A "Weisskopf-style sea from the Higgs's own fluctuations" is also never computed: the pure-scalar term is δm_h² ∝ λΛ² = (m_h²/2v²)Λ². It is proportional to m_h², but multiplied by Λ²/v², not a log, so there is no Weisskopf softening. Weisskopf's softening came from δm ∝ m at m → 0, i.e. chiral symmetry, and m_h² → 0 enlarges no symmetry except scale (S6).
- **Fix:** Add these two numbers and one line to the D2 answer and §3.

### 4. MINOR. Observation (b) mis-described as "hermiticity"
- **Location:** "Answer to D2" (b); §4b.
- **Problem:** For complex y the two chirality terms differ by a phase, which t_R rephasing removes. More to the point, any Dirac mass term pairs L with R, so the L↔R form of y h ψ̄ψ is automatic. It is not a property that could have been different in the SM, and so it cannot carry any protection. Literal L↔R (P) is broken by the gauge sector.
- **Fix:** Reword: "(b) is automatic for any Dirac mass; the top's Λ² ∝ |y_t|² either way; P itself is broken by SU(2)_L."

### 5. MAJOR (fixable). Gate 7: no check that could falsify the CLAIM
- **Location:** CLAIM "Falsifiable or checkable items".
- **Problem:** F-b (C(M_Pl) = 0 at 3.3-4.1σ) cannot falsify the CLAIM. Step 4 explicitly allows an accidental single-scale zero, so either outcome is consistent with the no-go. It is also a restatement of HKO/Masina-Quiros. F-a is an identity, F-c is about matching, and F-d is a theorem. The line says gate 7 is met "weakly". For the CLAIM it is not met.
- **Fix:** Supply a consistency check whose result could have come out the other way and that bears on D2. Options: (i) the counterfactual computation in Finding 1 (an independent H_B gives a U(4)-invariant Λ² term and pNGB protection; H_B := H^c gives 2|H|² and none), which tests whether "antimatter partner" ≠ "independent partner" is the operative distinction; (ii) an independent cross-check of S5's one-loop β_C on C = 0 against a published one-loop β of the Veltman coefficient (HKO or Jegerlehner); (iii) state plainly that a no-go theorem's gate-7 item is internal consistency only, and let the overseer rule.

### 6. Scope (item 3 of the brief). No issue
- All-orders vs one-loop: S1-S3 are statements about symmetries, so all orders. S5 is one-loop analytic plus 3-loop numerics, labelled as such. Quadratic vs physical threshold sensitivity is handled correctly ("R is not an observable"; the portal gives κM²/16π² independent of C; DR caveat; H2 respected). The d = 2-pole correction is honest.

### 7. Other gate items, BSM, numerology, H3
- Gate 1: met (negative for #1; #4 handled with the QCD-condensate estimate, M_W ≈ 30 MeV, v/f_π ≈ 2670 checks).
- Gate 2: no BSM used. Stops and superfields appear only as the comparison target. Twin/little Higgs should be added only as excluded routes (Finding 1).
- Gate 3: scripts present with outputs. Spot-checked c7_same_spin_out. The custodial line is wrong (Finding 2).
- Gate 4: CONSTRAINTS checklist §10 is complete.
- Gate 6: not assessed (instructed not to read LITCHECK). Novelty item 1 is plausible only if Finding 1 is added, because the twin-Higgs comparison is the non-obvious part.
- Numerology: none. H1 flags (sector near-equality at μ₀, R4 crossing) are honest.
- H3: antimatter is load-bearing only as the set of operations tested. That is acceptable for a negative result, and Finding 1 gives it a second, sharper role (C does not double the field space).

---

## Was the experimenter's hypothesis tested fairly?
Mostly. Each of (a), (b), (c) is addressed and the negative is right. The test skips the strongest form of the idea, a particle↔antiparticle exchange acting like a twin-Higgs Z₂, and the custodial H↔H^c reading. Both fail for a reason the line does not state: antiparticles are not independent fields (|H|²+|H^c|² = 2|H|²; H↔H^c is just the SU(2)_R element iσ₂). The line needs to add that reason to be complete.
