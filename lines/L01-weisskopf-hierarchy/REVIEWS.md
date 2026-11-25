# L01 Reviews

## Referee 1 (cycle 2)

**Verdict: MAJOR ISSUES (fixable)**

All five calc scripts were rerun from `calc/` (`weisskopf_ofpt.py`, `higgs_top_ofpt.py`, `veltman_running.py`, `cw_radiative_ewsb.py`, `rg_sm.py`). Every output file reproduces exactly. I rederived independently: the hole-theory spin sums, the scalar pair spin sum Tr[Lam+ beta Lam- beta] = 2p^2/E^2, the F/B energy denominators, the 3D-vs-4D cutoff factor 2, the STr M^2 coefficient C, and the Gildener-Weinberg m_h^2 = 8Bv^2 (W,Z only gives 9.78 GeV = sqrt2 times the Linde-Weinberg bound, which is consistent). The central negative result holds: no SM antiparticle structure cancels the Lambda^2 term. The problems are a wrong normalization claim, an overextended sign claim, an unstated definition of "antimatter", and a "prediction" section that predicts nothing.

### Findings

1. **major. WORK.md section 2c (lines 76-80), `calc/veltman_running.py:4-6, 42-44`; also leaked into CONSTRAINTS.md G "Convention note".**
   The claim "delta m_h^2 = C Lambda^2/(16 pi^2) ... The prefactor is 3/(16 pi^2 v^2), not the 3/(8 pi^2 v^2) that is often quoted" is wrong in the line's own convention.
   - The script takes d^2/dphi^2 of (Lambda^2/32pi^2) STr M^2. That is the shift of the phi curvature, which equals -delta(mu2) for V = -(mu2/2)phi^2 + ... (mass list at `veltman_running.py:27-33`).
   - In the stated Buttazzo convention V = -(m^2/2)|H|^2, mu2 = m^2/2 and m_h^2 = m^2 at tree level. So delta m^2 = 2 C Lambda^2/(16 pi^2) = C Lambda^2/(8 pi^2) = (3 Lambda^2/(8 pi^2 v^2)) x bracket. That is exactly the commonly quoted form.
   - The physical broken-phase mass with tadpoles included gives the same factor: the 1PI shift +C Lambda^2/16pi^2 plus the v-shift term -3 C Lambda^2/16pi^2 gives -C Lambda^2/(8 pi^2).
   - C Lambda^2/(16 pi^2) is the shift of the |H|^2 coefficient mu^2, equivalently the 1PI h self-energy at fixed v. That is why it matches the top-loop -3 y^2 Lambda^2/(8 pi^2) in `higgs_top_ofpt.py`. It is not delta m_h^2.

   Fix: relabel C Lambda^2/(16 pi^2) as delta mu^2 (the |H|^2 coefficient) and state delta m_h^2 = C Lambda^2/(8 pi^2). Delete the "not the 3/(8pi^2 v^2)" sentence and the NOTE printed by the script. The overseer should correct the CONSTRAINTS G convention note. Nothing downstream changes, because only the zero of C is used.

2. **major. WORK.md section 4 item 3 (line 116).**
   "Every SM fermion contributes through its sea (pair) states only, and each such contribution is negative-definite pointwise in loop momentum (section 2b, item 3)" is false for every fermion except the top. Section 2b item 3 depends explicitly on m_h < 2 m_f. For b, c, tau, mu and every other light fermion, 2 m_f < m_h. So the forward ordering F ~ 1/(m_h - 2E) is positive for p < sqrt(m_h^2/4 - m_f^2) and has a pole at threshold: the on-shell h -> f fbar cut, i.e. the imaginary part of the self-energy.

   Fix: restrict the statement to the UV. For example: "for p > sqrt(m_h^2/4 - m_f^2), and in particular in the coefficient of the Lambda^2 term, every fermion ordering is negative." The conclusion that adding fermion seas makes the divergence worse survives in that form.

3. **major. Claim (line 30) and section 4 item 4 (line 117): "The only SM cancellation is the Veltman condition ... that involves no antimatter."**
   Under the project's own scope (A1: "SM fields and their antiparticles"), W- is the antiparticle of W+ and G- is the antiparticle of G+. The positive (cancelling) side of C contains W+W- and G+G- loops, which are particle-antiparticle pairs. The line silently defines "antimatter" as fermionic Dirac-sea antimatter.

   The argument is easy to repair, and the repair should be stated: Z and h are their own antiparticles and contribute with the same + sign per degree of freedom as W+-. So the sign follows spin-statistics, not charge conjugation.

   Fix: add one paragraph making this argument, plus a two-line check in `veltman_running.py` that prints the per-species signs grouped by self-conjugate vs not. Without this, the headline "involves no antimatter" is an unproven definitional claim.

4. **minor. WORK.md section 8 (lines 146-148): no genuine falsifiable prediction.**
   A negative result predicts nothing by itself. "M_t near 169.4 GeV would put C = 0 at M_Pl" tests a coincidence that the line explicitly gives no mechanism for (H1). The zero location also mixes MS-bar running couplings with a one-loop cutoff coefficient that is gauge- and regulator-dependent, as section 6 admits, and HKO's 2-loop quadratic terms shift it. So mu0 = 10^22.8 is scheme-dependent (H2) and should not be offered as a testable number.

   Fix: rename the section "Consistency checks" and list the real ones:
   - 8-digit agreement between the covariant integrand and the time-ordered sum
   - the 3 alpha/2pi log coefficient, which matches standard covariant QED
   - the chiral zero at m = 0
   - agreement with HKO (10^23.5 at M_t = 173.34 here vs their ~10^23 at 173)

   Tag mu0 as scheme-dependent.

5. **minor. WORK.md line 101: "M_t ≈ 169.4 GeV, which is 11 sigma below PDG."**
   This uses only the 0.29 GeV experimental error on the direct top mass. It ignores the ambiguity between the MC mass and the pole mass (~0.5 GeV) and the theory error in the y_t(M_t) matching. HKO themselves call 170 GeV "1.3 sigma" lower, with 2012 errors.

   Fix: quote the shift in GeV (3.2 GeV) and drop "11 sigma", or include the theory error.

6. **minor. WORK.md line 50: history mislabelled [established].**
   The no-sea quadratic divergence (Tneg: one-electron Dirac theory with negative-energy intermediate states) is the Waller / Oppenheimer 1930 result. Weisskopf 1934 was a hole-theory calculation with an algebraic error, which Furry pointed out. The 1934 erratum already gives the log. Attributing Tneg to "the 1934 Weisskopf result before Furry's correction" conflates the two.

   Fix: attribute Tneg to Waller/Oppenheimer 1930, and describe Weisskopf 1934 plus erratum as the first hole-theory log result.

7. **minor. WORK.md line 106: Jegerlehner citation.**
   arXiv:1305.6652 has no journal reference on arXiv, and I found none elsewhere. Acta Phys. Polon. B 45, 1167 (2014) appears to belong to his companion paper arXiv:1304.7813, "The Standard model as a low-energy effective theory: what is triggering the Higgs mechanism?". I did not confirm this. Separately, the 1305.6652 abstract gives "about 10^17 GeV", not 7x10^16.

   Fix: cite 1305.6652 as a preprint and check the APPB ref on INSPIRE. Give the section or equation number where the 7x10^16 figure appears.

8. **minor. WORK.md section 5(A) (line 124), `calc/cw_radiative_ewsb.py:34, 40`.**
   In a classically scale-invariant theory m_h is an output, but the "m_t > 87.5 GeV" threshold uses m_h = 125.2 GeV as an input to B. That is circular. The effect is small (the h^4 term is about 3% of the sum).

   Fix: quote the threshold from W and Z only, or solve it self-consistently with m_h^2 = 8 B v^2. Either way it comes out near 87 GeV.

9. **minor. WORK.md section 4 item 5 and section 7 "G": "the negative result holds ... in dim reg".**
   Dim reg has no Lambda^2 term to cancel, so there the antimatter question does not arise. It is not answered negatively.

   Fix: say "the question does not arise in dim reg; in the heavy-threshold version there are no SM heavy states", which is what item 5 already argues.

10. **minor. Bookkeeping.**
    - (a) Section 7 G (line 143) says CONSTRAINTS G uses "(3/2)(...)/v^2". It does not: it uses 3/(8pi^2 v^2). This text is stale.
    - (b) The checklist covers B1-B8 and F1-F2 but omits B9, B10 and F3. Each needs one word ("not relevant"), but CONSTRAINTS requires every item to be addressed explicitly.
    - (c) C(M_t) MS-bar is -3.43 in section 2c and -3.42 in the table. These are the script's -3.426 at mu = M_t and -3.4226 at log10 mu = 2.24. Use one value.
    - (d) Section 6 says the m^2 runner discrepancy (139.4 vs 129.4 GeV at M_Pl) is "not used in any conclusion", but section 5(B) quotes m(mu) values from that runner. The sign-invariance conclusion is unaffected, because beta(m^2) is proportional to m^2 at every loop order whatever the coefficients. Say that explicitly, and stop presenting the GeV values as checked until the discrepancy is resolved.

### Checked, nothing found
- No BSM content. SUSY appears only as a comparison target.
- No extra states from a reformulation. Hole theory and time ordering are cross-checked against the covariant integrand, so A3 and H3 are satisfied.
- No numerology is claimed.
- These citations are correct:
  - Hamada-Kawai-Oda, PRD 87, 053009 (abstract: zero at ~10^23 GeV for M_t = 173, at Planck for ~170)
  - Masina-Quiros, PRD 88, 093003 (the line marks this journal ref "unverified"; it is correct)
  - Weisskopf, Phys. Rev. 56, 72
  - Coleman-Weinberg, PRD 7, 1888
  - Weinberg, PRL 36, 294
  - Linde, JETP Lett. 23, 64

### Is the central claim supported?
The narrow claim is supported once findings 2 and 3 are fixed:
- The time-ordered top loop has no ordering of opposite sign.
- The decomposition is exact, with 8-digit agreement against the covariant integrand.
- The Weisskopf mechanism is reproduced with the correct 3 alpha/2pi log and the chiral zero at m = 0.

The broader framing "involves no antimatter" needs the self-conjugacy argument from finding 3. The line has solid consistency checks but no falsifiable prediction (finding 4).
