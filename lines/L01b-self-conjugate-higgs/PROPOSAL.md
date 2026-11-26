# L01b - Self-conjugate Higgs: an antimatter analogue of SUSY's Higgs-mass protection?

**Targets:** SUSY result #1 (Higgs-mass protection) and #4 (radiative EWSB, via L01 merged by reference in cycle 5), with a side check on #6 (absence of superpartners). The current claim is the CLAIM section at the top of WORK.md.

**Origin:** experimenter directive D2 (STATE.md). This line sits next to L01 and does not replace it. L01 asks whether the Weisskopf mechanism carries over. L01b tests the experimenter's three structural observations directly, and per D3 it looks for positive matches:

- (a) h is its own antiparticle (self-conjugate), as SUSY's Majorana gauginos are.
- (b) The Yukawa coupling y h ψ̄ψ = y h(ψ̄_Lψ_R + ψ̄_Rψ_L) is symmetric under L↔R.
- (c) Bosons carry no chirality.

**Question:** Can SM antimatter structure built from (a)-(c) reproduce the SUSY cancellation of the quadratic sensitivity of m_h²? SUSY cancels the top/antitop loop with stop/antistop loops. Exactly where does the SM match this, and exactly where does it fail?

**Method:**
1. Write the SUSY cancellation term by term in particle/antiparticle language. Use hole theory (Dirac sea plus boson zero-point pairs) and Feynman-Stueckelberg time orderings, and cross-check each piece against covariant integrands.
2. Rewrite the SM one-loop Higgs Λ² coefficient in the same language. Break it down by species: charged pairs, self-conjugate quanta, fermion seas.
3. Scan the candidate SM symmetries (C, P, CP, h→−h, h→−h with a chiral sign, custodial, chiral U(1)s) for their action on operators and couplings. Test whether the matching condition is RG invariant.
4. Run the matching ratio with 3-loop RGEs (tools/rg_sm.py). Find the falsifiable m_t values.

**Scope:** SM fields only. SUSY (stops, electroweakinos) appears only as a comparison target in calc/pair_matching.py Part 4.
