# Referee C (cycle 7) - logical rigour of the no-go

Read: OVERSEER_PROMPT.md (question, scope, gate), CONSTRAINTS.md, PROPOSAL.md, WORK.md (CLAIM, sections 1-4), calc/c7_same_spin.py + output. Did not read REVIEWS*.md or LITCHECK.md before writing this.
Own check: `calc/refC_check.py` -> `calc/refC_check_out.txt`.

## Verdict: MAJOR ISSUES (fixable)

No fatal error. No BSM content in any mechanism (SUSY, twin/extra-dim only as excluded comparisons). The conclusion (SM antimatter cannot reproduce SUSY's coupling-relation protection) is correct, but step 2 is stated as a general lemma that is false, and the route table misses the one mechanism that directly tests the "spin-preserving discrete symmetry" loophole.

## Verified

- S1 C/P/T spinor checks are correct (C L* C^-1 = L in Dirac rep; P J P^-1 = J; T J* T^-1 = -J). All maps preserve J^2 and (-1)^F. Dirac sea / Feynman-Stueckelberg are not Hilbert-space operators, so "they preserve spin" is right in the only sense it can mean.
- S5 one-loop polynomial: re-derived independently with standard SM one-loop betas; difference from WORK.md S5 is exactly 0.
- Tree C from pole masses = -4.07 (refC_check), consistent in sign/size with the MS-bar -3.43 (WORK.md sec 2 sums to C(M_t) = -3.43).
- S6: B = -4.39e-3, mu^2 = (88.5 GeV)^2 reproduced.
- QCD-condensate M_W = g f_pi/2 = 30 MeV, x sqrt(3) = 52 MeV, share 1.4e-7: correct.

## Findings

**1. MAJOR. Step 2 / S2 lemma is false as stated.** (CLAIM item 2; WORK.md sec 4a S2; c7_same_spin.py S2.)
Claim: a spin- and statistics-preserving map sends each Lagrangian monomial into its own field-type class, "so invariance of L gives conditions within each class only" and "no such symmetry can force C = 0".
This holds only for global, homogeneous, linear internal maps. Spin-preserving symmetries that do tie couplings across classes:
- Local gauge invariance (inhomogeneous, A -> A + d alpha): ties V S S, V V S S, V F F, V^3, V^4. The text calls this "gauge universality" but that contradicts "conditions within each class only".
- Non-linearly realized symmetries: in a coset (e.g. SO(5)/SO(4)) h-VV and hh-VV couplings, and h-tt and hh-tt, are fixed together. Twin Higgs (finding 2) is a spin-preserving discrete Z2 that removes the top Lambda^2 term from the pNGB mass.
- Scale invariance plus dimensional transmutation (Gildener-Weinberg): m_h^2 = 8 B v^2 with B built from g^4 and y_t^4, i.e. a spin-preserving symmetry fixes the scalar self-coupling in terms of g and y_t. It is a STr M^4 relation, not STr M^2, and it fails in the SM (B < 0), but it refutes the lemma in its general form.
- 5D Lorentz (spin-preserving in 5D) relates a 4D scalar to a 4D vector; the line already lists this as S <-> V, so "spin-preserving" is not the right criterion there either, "4D spin-preserving" is.
Fix: restate S2 as "homogeneous linear global maps (including C, P, T, CPT, flavour and custodial rotations) preserve field-type class". Then cover the exceptions explicitly: (a) gauge: the SM gauge group is fixed and y_t|Q H t^c| and lambda|H|^4 are separately gauge invariant, so gauge invariance cannot relate them; (b) nonlinear/shift: needs h to be a Goldstone, BSM; (c) scale: S6, constrains STr M^4/mu^2 not C, and GW fails (B < 0); (d) higher-dim: BSM. Better still, base the step on the known complete symmetry group of the SM Lagrangian (gauge x U(1)_B x U(1)_Le,mu,tau x CPT, approximate custodial/flavour) and show none fixes C. The empirical closure is already in the line and should be cited here: C(M_t) != 0 and the measured flow crosses C = 0 transversally, so no exact SM-internal relation (symmetry or otherwise) enforces C = 0.

**2. MAJOR. Route table omits neutral naturalness (twin Higgs; folded SUSY).** (CLAIM item 5.)
Twin Higgs is exactly the scenario the brief asks about: a spin-preserving discrete symmetry plus a field-content doubling cancels the top's Lambda^2 contribution to the light Higgs (y_t^A = y_t^B forces the quadratic piece into the accidental-SU(4) form |H_A|^2 + |H_B|^2). It is also the closest thing to an "antimatter partner" mechanism, since the partner has the same spin. Leaving it out makes step 3 ("the only spin-changing symmetry is SUSY") look like it covers all protection, which it does not.
Fix: add a row. Needs a mirror copy of the top sector with its own Higgs H_B (A1 forbids mirror/twin sectors). State why antimatter cannot be the twin: the antitop is in the same field as the top, C/CP/CPT map the top loop into itself, and the antitop dof are already in the -12 (Dirac, 4 x Nc) of the top term. There is no second H. Folded SUSY: spin-changing, needs new fields. One or two lines each.

**3. MINOR. CM/HLS step overstated in scope.** (CLAIM item 3; S3.)
CM and HLS classify symmetries of the S-matrix: unbroken, linearly realized on asymptotic one-particle states, finitely many particles below any mass, non-trivial analytic scattering. SUSY's protection works when SUSY is broken, and a relation among Lagrangian couplings can come from a symmetry that never shows up as an S-matrix symmetry. Also, gluons are not asymptotic states, so CM applies to the hadron/photon S-matrix. The fix is in the wording. (i) The usable output of HLS is the algebra classification: any spin-changing symmetry algebra of a 4D relativistic QFT is super-Poincare/superconformal. (ii) Every realization needs new states: linear means superpartners, nonlinear (Volkov-Akulov, constrained superfields) means at least a goldstino. Neutrino-as-goldstino is an old proposal that low-energy theorems exclude; mention it, because it is the one way SM content might look like it fills the role. (iii) Under A1 the decisive argument is the enumeration in finding 1. CM/HLS only explains why there is nothing else to look for.

**4. MINOR. S5 logic: "nonzero polynomial on C = 0" alone does not exclude an RG-invariant sub-variety inside C = 0.** Reduction of couplings (Zimmermann; Kubo-Sibold-Zimmermann) gives RG-invariant relations without any symmetry. The polynomial has real zeros (33g^4 - 162g^2y^2 + 126y^4 changes sign). What excludes it for the SM is the measured trajectory crossing transversally (3-loop dC/dln mu = +0.020). Say so. Also note that the one-loop statement is scheme-independent, while the 3-loop crossing scale is not, since C is a cutoff coefficient evaluated with MS-bar couplings. The SUSY relation "preserved by running" holds in DR-bar, not MS-bar.

**5. MINOR. Tag inflation.** "[computed check S2]" and the boson parts of S1 are printed prose in c7_same_spin.py, not computations. Retag them [argument]. S1 (spinor), S3 (F-term), S4 (scan) and S5 are genuine computations.

**6. MINOR. Weyl vs Dirac in S1.** For the SM's Weyl fields, C maps (1/2,0) to (0,1/2). Spin is preserved but the Lorentz representation is not the same, so "psi^c transforms with the same Lorentz matrix as psi" holds only for the Dirac 4-spinor. One sentence fixes it. It does not affect the conclusion, which needs only J^2 and (-1)^F.

**7. MINOR. Strength and novelty framing.** The empirical half of the no-go (nothing in the SM sets C = 0) follows from measured masses alone. Steps 1-3 explain why, but "no mechanism within SM field content" is not a formal class, so per the gate this is a strong argument, not a proof. Label it that way in the CLAIM. Novelty item 1 should say the assembly is explanatory.

**8. MINOR. Gate 7.** F-b tests C(M_Pl) = 0, a hypothesis the line itself says has no SM meaning. It is falsifiable as a check of HKO/Masina-Quiros, but it is not a prediction of this line. The text already says gate 7 is met "only weakly"; keep that wording.

**9. MINOR. "factor of about 2700"** (CLAIM item 6): 246/0.0924 = 2660 for one doublet, and about 1540 with three massless doublets (sqrt(3) f_pi). Say which.

## BSM / numerology / H3
- BSM: none used. Extra dimensions, twin and SUSY appear only as excluded routes or as the comparison target. Pass.
- Numerology: the mu_0 and M_t* items are labelled scheme-dependent and non-observable. Pass, with finding 8.
- H3: the line correctly concedes that the hole-theory and time-ordered pictures add no content. The antimatter content is only the set of operations tested in step 1, and that is honest.
