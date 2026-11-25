# L02-unification-virtual-pairs: PROPOSAL

**Target SUSY result:** #2, gauge coupling unification (MSSM: alpha_1, alpha_2, alpha_3 meet near 2e16 GeV).

**Question.** Running of gauge couplings is, in hole-theory language, screening and antiscreening by virtual particle-antiparticle pairs. SUSY gets unification by adding superpartner pairs to the vacuum. Can SM antimatter, counted in any SM-equivalent way (Dirac sea, Feynman-Stueckelberg, NCG / division-algebra reformulations restricted to the SM sector), change the running enough to unify?

**Claim (result of this line).** No. [established, reproduced here]
1. In every formulation equivalent to the SM, the beta-function coefficients are functions of the gauge group, the representations and their multiplicities only. A Dirac (or Weyl) field already contains its antiparticle; the loop that "is" the antiparticle is the negative-frequency pole of the same propagator and is counted once. Any other weighting changes measured quantities (Delta alpha_lep, the R-ratio, alpha_s running) by factors of order 2 and is therefore not an equivalent formulation.
2. Structural point: at one loop the SM fermions (matter and antimatter) shift b_1, b_2, b_3 by the same amount, because each generation fills complete SU(5) multiplets. So fermion antimatter contributes exactly zero to the one-loop non-unification, under ANY weighting of antiparticle loops. The mismatch comes from the gauge-boson and Higgs loops. To unify at one loop one would need the scalar loops weighted ~7.4x (7-8 Higgs doublets) or the gauge loops weighted ~0.13x; neither is an SM counting.
3. Quantified non-unification (3-loop SM, PDG-2024 inputs): M12 = 10^13.05, M13 = 10^14.25, M23 = 10^16.47 GeV; minimal spread of alpha^-1 = 3.18 (7.7%) at 10^14.24 GeV; alpha_3^-1 misses the alpha_1 = alpha_2 point by 4.9; exact unification would need alpha_s(MZ) = 0.074 (measured 0.1180 +- 0.0009). MSSM reference (2-loop, M_SUSY = 2 TeV): spread 0.02, alpha_s predicted 0.118.
4. The spectral action's boundary condition g3 = g2 = sqrt(5/3) g1 at the cutoff is an extra high-scale relation (CONSTRAINTS A3.2) and is not satisfied by SM running anyway; its m_H ~ 170 GeV prediction (hep-th/0610241) was excluded in 2008 and the 2012 repair adds the sigma scalar (forbidden).
5. Proton decay: there is no X boson in the SM, so no physical scale emerges. If one were placed at the SM crossings, M12 and M13 give tau_p ~ 1e24 and 5e28 yr, excluded by Super-K; only M23 (~3e16 GeV) would be safe.

**Status:** negative result, ready for referee. Recommend scrapping the "antimatter fixes unification" idea with this file as the cause of death, salvage: the RG runner (validated against arXiv:1307.3536 to 4 digits) and the state-counting check.
