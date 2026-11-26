# LW1 reviews

## Referee 1 (cycle 5)

**Verdict: MAJOR ISSUES (fixable).** No fatal error. Input masses are right (about 70 values spot-checked against PDG 2024 from memory; both 2026 LHCb masses verified on arXiv this cycle). The weak points are the #1 argument (what the Fock-space code can and cannot show), one R1 breach in the #6 census, and a "protection" claim that a plain additive quark model also reproduces.

### Inputs checked and OK
- T_cc+: 3874.7 MeV, 0.36 MeV below D*+D0 (unitarised pole, LHCb Nat. Commun. 13, 3351 (2022), arXiv:2109.01056). Threshold 2010.26 + 1864.84 = 3875.10. OK. The "[keV digits from memory]" tag can go: delta m_pole = -360 +- 40 keV.
- Xi_cc++ 3621.55 +- 0.23 +- 0.30 (LHCb arXiv:1911.08594). OK.
- Xi_cc+ 3619.97 +- 0.83 +- 0.26 +1.90/-1.30 (lifetime), PRL 137, 021902 (2026), arXiv:2603.28456. Verified on arXiv.
- Omega_cc+ 3725.9 +- 1.0 +- 0.2 +- 0.4 +- 0.6, 8.7 sigma, arXiv:2609.21921. Verified on arXiv. Still a preprint.
- c5d supermultiplet table: every meson, baryon and tetraquark mass I checked (light, charm, bottom and double-heavy rows) matches PDG 2024 to the quoted digits. The isospin and charge averages (Xi(1530), Sigma_b, Xi_b, Xi_c(2470), charged K2*(1430)) are reasonable choices.
- LO numbers: (3/4)(142.0) = 106.5, (3/4)(143.8) = 107.9, (3/4)(45.2) = 34.0, (3/4)(48.5) = 36.4. Reproduced. T_cc at LO: 2286.46 + 3691.4 - 1973.2 = 4004.7. Reproduced (isospin-averaged D, D*, Xi_cc).
- Metz et al. quartet (194Pt, 195Pt, 195Au, 196Au): correct to my knowledge. Drop "[unverified]" after a one-line check of the abstract.

### Findings

1. **MAJOR. WORK sec. 12 and 17, c5_supercharge_algebra.py. The code does not test the "no P_mu" result, and "no P_mu => cannot protect masses" does not follow as stated.**
   Problem:
   (a) Both Fock spaces have one spatial mode per colour, spin and flavour. Momentum does not exist in them, so the code cannot detect a P_mu term even in principle. "Numerically checked: no P_mu" is vacuous. The only support is the one-line field-theory remark.
   (b) The QCD-level toy gives the antiquark no spin (`abar_a`, 3 modes). The resulting Q is fermionic with spin 0. That is not the operator in the text (Q_s, spin 1/2), and it is not consistent with spin-statistics.
   (c) Q_s carries spin 1/2, so it does not commute with rotations. It is not "internal" in the Coleman-Mandula/HLS sense. The right label is "non-relativistic spectrum-generating superalgebra whose anticommutator is not proportional to P".
   (d) What blocks mass protection is that Q is not a symmetry. c5a itself gives [H,Q] = (m_D - m_dbar) Q != 0, and the hadron spectrum is visibly non-degenerate. The missing P_mu follows from Q being a non-relativistic ladder operator. It is not an independent reason. A hypothetical exact Bose-Fermi symmetry with equal couplings would cancel the loops however its algebra was written. HLS then says such a symmetry must be Poincare SUSY, and QCD has none.
   Fix: restate the #1 negative as three points. (i) Q is not conserved ([H,Q] != 0, non-degenerate partners). (ii) By HLS, QCD cannot have an exact fermionic symmetry with {Q,Q-bar} not proportional to P. (iii) The bosons are composite above ~1 GeV. Label the "no P_mu" statement [argument], not numerically checked. Either add antiquark spin to the QCD-level toy (6 abar modes) or state that the toy antiquark is spinless. Replace "internal" with the label in (c). The sec. 17 headline "wrong algebra, so no loop-momentum cancellation even in principle" is overstated. Change it to "not a symmetry, and HLS forbids an exact version".

2. **MAJOR. WORK sec. 15, c5_hadronic_supermultiplets.py row `chi_c2(3556) / "Xi_cc(3621) as 3/2+"`. An unobserved state is counted as observed (ruling R1).**
   Problem: the J=3/2 Xi_cc* is unobserved, as the line itself says in sec. 9. The row puts the J=1/2 Xi_cc(3621) in the 3/2+ slot and flags it OBS. The "31/40 both observed" count and the double-heavy statistics both include it. The EXO tally also counts Zc(3900) from a row whose baryon (Xi_cc(~3900)) is unobserved.
   Fix: mark that baryon PRED. The census becomes 30/40 and double-heavy becomes n=1. Counting EXO only in rows with an observed baryon leaves 1 (pi1(1600)).

3. **MAJOR (interpretive). WORK sec. 14, c5_superflavor_protection. The "96% partner cancellation" is not specific to superflavor.**
   Problem: any additive constituent model, with M = sum of constituent masses + spectator-independent binding, gives D_s - D ~ Omega_cc - Xi_cc ~ m_s - m_u. Calling this a "partner cancellation" analogous to SUSY protection needs a control. A non-superflavor control gives a larger residual: Xi_c' - Sigma_c = 125 MeV against D_s - D = 101 MeV, a residual of about 24 MeV. So superflavor may do better than the generic case, but the line has not shown it.
   Fix: add control pairs (Xi_c' - Sigma_c, Omega_c - Xi_c', B_s - B, Xi_b - Lambda_b) and quote the superflavor residual relative to the generic one. Keep "protects differences, not masses". Drop the SUSY "protection" wording unless the control supports it.

4. **MINOR. c5_superflavor_protection.py line 26. Xi_cc+ error.**
   The script uses 1.6 MeV, which is only the symmetrised lifetime term. It drops the 0.83 stat and 0.26 syst. The total is about 1.8 MeV (about 2.1 upward). The Omega_cc+ "ext" error (0.6) is partly correlated with the Xi_cc++ mass, and the lifetime biases of Xi_cc+ and Omega_cc+ are correlated in sign. The residual 4.0 +- 1.5 becomes roughly 4.0 +- 1.7. The conclusion is unchanged, but fix the number.

5. **MINOR. WORK sec. 14 isospin decomposition: numerology.**
   Xi_cc+ - Xi_cc++ = -1.58 +- 1.8 is 1 sigma from zero, so "explains why the splittings have opposite sign" rests on a 1 sigma sign. The comparison delta = 2.7 MeV ~ m_d - m_u (MS-bar, 2 GeV) mixes two different quantities. delta is a hadronic effective parameter that also absorbs the light-quark EM self-energy and the isospin dependence of the hyperfine term. m_d - m_u is a scheme-dependent current-mass difference. The fit is already labelled zero-d.o.f. Remove the m_d - m_u match or label it [speculation], and state that the sign is a 1 sigma result.

6. **MINOR. WORK sec. 12, HLS argument labelled [conjecture].**
   "Q is not an exact symmetry of QCD" is stronger than a conjecture and needs no HLS: the meson and baryon partners are non-degenerate, and [H,Q] != 0 in the line's own model. HLS adds that no deformation can make Q exact. Two caveats to state: HLS assumes a Lorentz-invariant S-matrix of asymptotic (hadron) states, and Q acts on confined constituents, so HLS applies to any hadron-level image of Q. The heavy-quark escape clause is fine. Relabel "not exact" as [established]. Keep [conjecture] only for "no QCD-level improvement changes the classification".

7. **MINOR. WORK sec. 9 / c4. Error budgets on the two predictions.**
   - Xi_cc* - Xi_cc = 107 +- 32: the LO central value with a 30% power-counting error is defensible. The 2 sigma kill band [43, 170], however, treats a power-counting estimate as Gaussian. Call it naive. The 1 sigma upper edge (139 MeV) is above the Xi_cc pi0 threshold (135 MeV) and the Xi_cc+ pi+ threshold (~138 MeV). So "Delta < m_pi0" holds only for the central values, and the M1-only decay statement needs that caveat.
   - Xi_bb* - Xi_bb = 30 +- 4: kappa is calibrated on the Brown+ charm lattice ratio and then "tested" on the same collaboration's bottom number (34.6 +- 7.8, a 23% error). The test is correlated and weak. The +-4 (13%) is no tighter than BVR's own LO +-4. The prediction is within 1 sigma of both LO and lattice, so it does not discriminate. Xi_bb itself is unobserved, so a test needs two unobserved states plus a ~30 MeV M1 photon. Call it a "refinement", not "the line's real prediction". Add the spread over lattice charm inputs to the budget, for example Mathur-Padmanath Omega_cc 76(6)(6), which gives a different kappa.

8. **MINOR. c5d bookkeeping.**
   - WORK sec. 15 gives max |dM| = 254 MeV as h1/N. That value is K2(1770)/Lambda(1520) (1773 - 1519). h1/N is 227 MeV.
   - The script prints QQB = 13 in the counts and n = 11 in the stats line, because chi_b0 and chi_b1 sit in rows with unobserved Xi_bb. Say which number is meant.
   - Some J^P assignments are reconstructed and conflict with data, yet the slots are counted as filled. D(2600) is "assumed 2-", but PDG lists D1*(2600) as 1-. D0(2550) is "assumed 1+", but LHCb gives 0-. Flag both as assignment conflicts.
   - Selection bias: the Nielsen-Brodsky tables were built from known states, so a high observed fraction is expected by construction. 31/40 (30/40 after finding 2) carries no evidential weight for #6 beyond what the line already concedes ("trivial sense"). Say so explicitly.

9. **MINOR. Framing "built on antimatter" (PROPOSAL, sec. 1).**
   Superflavor maps Q <-> Qbar Qbar just as well as Qbar <-> QQ, and the line uses the first map for T_cc. Which member counts as "the antiquark" depends on the C convention. The convention-independent statement: every supermultiplet pairs a matter object with an antimatter object in the same colour representation, so a world without antiquarks has none. Use that wording.

10. **MINOR. T_cc (sec. 14).**
   The line's LO value of 4005 MeV differs from Eichten-Quigg's 3978 MeV by 27 MeV with no explanation. EQ include a hyperfine term between the cc diquark and the light antidiquark. Reconcile the two or note the difference. The "flips bound/unbound" conclusion is unaffected.

### Not found
- No BSM input. Nuclear SUSY is excluded from the mechanism for a correct reason: nuclear holes are not antinucleons.
- No other R1 breach. Xi_bb, T_bb, B_s0(5800) and similar states are flagged and not used as evidence.
- The SUSY-QM protection test (c5b) is standard and correctly labelled. The pion/GMOR identification is properly [conjecture].
