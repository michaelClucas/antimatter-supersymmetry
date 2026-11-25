# L01 WORK - Weisskopf mechanism vs the Higgs hierarchy

All numbers below come from scripts in `calc/` (outputs in the matching `*_out.txt`; rerun from inside `calc/` in cycle 3). Units: natural, Heaviside-Lorentz, e^2 = 4 pi alpha. Shared code: `tools/sm_inputs.py` (PDG 2024) and `tools/rg_sm.py`. `calc/rg_sm.py` is now a shim that re-exports `tools/rg_sm.py` (see Response to referee 1, item R).

## Claim

**The Weisskopf mechanism does not extend to the Higgs. No SM antiparticle structure cancels or softens the quadratic (Lambda^2) sensitivity of the Higgs mass parameter.** [established for each component; the overall framing is this line's conclusion]

- The Weisskopf cancellation needs a fermion whose mass breaks a chiral symmetry, with the sea of the same field providing a Pauli-blocked counter-term. The Higgs has neither.
- In the top loop, both time orderings are negative at every loop momentum. For lighter fermions (2 m_f < m_h) the forward ordering is positive below the h -> f fbar threshold, but every ordering is negative above it, and every fermion's Lambda^2 coefficient is negative.
- The only SM cancellation of the Lambda^2 term is the Veltman condition. Its positive side contains both charged particle-antiparticle pairs (W+W-, G+G-) and self-conjugate fields (Z, h, G0). Every boson enters with + and every fermion with -, whether or not the field is self-conjugate. The coefficient is a trace over the mass-squared matrix, so it cannot depend on whether a degenerate pair is written as particle + antiparticle or as two real fields. The sign comes from spin-statistics, and "antimatter" is not a variable it can depend on (section 4).
- With measured inputs and 3-loop running the Veltman coefficient has no zero below about 10^22.8 GeV (a scheme-dependent number, section 3).
- SM radiative EWSB also fails (section 5).

Normalization used throughout (CONSTRAINTS G, ruling R3): V = -mu^2|H|^2 + lambda|H|^4, m_h^2 = 2 mu^2 = 2 lambda v^2,
C = 6 lambda + (9/4) g^2 + (3/4) g'^2 - 6 y_t^2 = (3/v^2)(m_h^2 + 2 M_W^2 + M_Z^2 - 4 m_t^2),
**|delta mu^2| = |C| Lambda^2/(16 pi^2), |delta m_h^2| = |C| Lambda^2/(8 pi^2) = (3 Lambda^2/(8 pi^2 v^2)) |bracket|.**
The overall sign of "delta" depends on whether one quotes the correction or the counterterm, and on what is held fixed. The zero of C does not.

---

## 1. Weisskopf cancellation reproduced (`calc/weisskopf_ofpt.py`)

Setup: electron at rest, spin-averaged, Coulomb gauge, sharp cutoff K on the photon 3-momentum, time-ordered perturbation theory, Dirac Hamiltonian H(p) = alpha.p + beta m, projectors Lam_pm(p) = (1 pm H(p)/E)/2. Integrands are d(delta m)/dk.

| piece | meaning | k -> inf |
|---|---|---|
| C1 | Coulomb self-energy, one-electron theory | **+alpha/pi** (linear) |
| Cs | Coulomb exchange with the filled sea | **-alpha/pi** |
| Ta | transverse, intermediate state e(-k)+gamma (electron only) | **-alpha/(2pi)** |
| Tb | transverse, vacuum pair e(0,s) ebar(-k) gamma, Pauli-blocked by the electron present, so removed from the vacuum energy | **+alpha/(2pi)** |
| Tneg | (comparison) one-electron Dirac theory with no sea: electron jumps into negative-energy states | quadratic divergence, coefficient alpha/(pi m) of K^2/2 |

Results [established, reproduced]:
- One-electron (no-pair, positive-energy only) theory: C1 + Ta = alpha K/(2 pi). Linear divergence.
- Hole theory: C1 + Cs has linear coefficient 0, and Ta + Tb has linear coefficient 0. Each sector cancels separately.
- Total hole-theory integrand = alpha m (2k + E)/(pi (k^2 + kE + m^2)) -> (3 alpha m/2pi)/k. So delta m = (3 alpha/2 pi) m [ln(K/m) + c], c = 0.5265, numerically equal to ln 2 - 1/6 to the printed precision [numerical identification; cutoff-scheme dependent; Weisskopf's own constant not compared].
- The log coefficient 3 alpha/(2 pi) is the standard covariant QED one-loop mass-shift coefficient [established].
- Tneg (no sea, negative-energy intermediate states allowed) diverges quadratically. Historically this is the one-electron Dirac-theory result of 1930: Oppenheimer, Phys. Rev. 35, 461 (1930), and Waller, Z. Phys. 62, 673 (1930) [both bibliographic details not re-verified this cycle; LITCHECK could not verify Waller]. Weisskopf's 1934 paper, Z. Phys. 89, 27 (1934), was already a hole-theory calculation; a sign error, pointed out by Furry, made it come out as divergent as the one-electron theory, and the erratum, Z. Phys. 90, 817 (1934), gives the logarithm [established, LITCHECK item 2]. Weisskopf, Phys. Rev. 56, 72 (1939), extended the analysis to all orders and showed charged Bose particles keep a quadratic divergence [established, LITCHECK item 1].
- **Chiral-symmetry check:** at m = 0 the hole-theory integrand vanishes identically, in both the Coulomb and the transverse sector. The one-electron theory integrand (C1+Ta) does not (alpha/2pi at m=0). So delta m is proportional to m only once the sea is included.

What does the cancelling: the Pauli-blocked vacuum-pair term (Tb) and the sea-exchange Coulomb term (Cs). Both exist only because the external electron and the sea electrons are the same fermion field and obey exclusion.

## 2. Modern reading, and the Higgs fermion loops in the same decomposition

### 2a. Electron [established]
In covariant QFT the two time orderings Ta and Tb are the two pieces of one Feynman diagram after the k0 integral. The pair term is the Z-graph. The log, rather than linear, divergence is guaranteed by chiral symmetry: at m = 0 the QED Lagrangian is invariant under psi -> exp(i theta gamma5) psi, so delta m must be proportional to m and can only be m ln(K/m). 't Hooft's technical-naturalness criterion: 't Hooft, "Naturalness, chiral symmetry, and spontaneous chiral symmetry breaking", NATO Sci. Ser. B 59, 135 (1980) [CONFIRMED by LITCHECK]. In covariant language nothing antiparticle-specific remains. The hole-theory split is noncovariant bookkeeping, and the sum is fixed by the symmetry. This is the standard pedagogical account, e.g. Murayama, hep-ph/0002232, sec. 1.3 "Positron analogue".

### 2b. Higgs self-energy from a fermion loop (`calc/higgs_top_ofpt.py`)
H_int = (y/sqrt2) h fbar f, N_c = 3 (N_c = 1 for leptons), Higgs at rest, cutoff K on the fermion 3-momentum. The quantity computed is the 1PI self-energy Sigma_hh at fixed v. For the Lambda^2 term this is the shift of the |H|^2 coefficient (the delta mu^2 normalization), not the physical delta m_h^2, which is twice as large (section 2c). The script labels were changed from "delta m_h^2" to "Sigma" in cycle 3.

Time-ordered pieces of dSigma/dp:
- F (forward, h -> f fbar -> h): 3 y^2 p^4 / [2 pi^2 (p^2+m^2)(m_h - 2E)]
- B (backward, Z-graph: vacuum -> h' f fbar, then f fbar h -> 0): -3 y^2 p^4 / [2 pi^2 (p^2+m^2)(m_h + 2E)]

Facts [established, reproduced]:
1. There is **no fermion-free intermediate state**. Both orderings contain an f fbar pair. In hole language both are excitations of the filled Dirac sea (a sea fermion lifted to positive energy). The Lambda^2 sensitivity from fermions comes entirely from the seas, i.e. vacuum polarization. For the Higgs, the fermion seas are a source of the divergence and cancel nothing.
2. There is **no Pauli blocking**: no fermion is present in the external state.
3. **Top (2 m_t > m_h):** F < 0 and B < 0 at every p. No cancellation among top-loop orderings is possible. Large p: each contributes -3y^2 p/(4pi^2), and they add.
4. **Light fermions (2 m_f < m_h: b, c, tau, and lighter):** B < 0 at every p. F > 0 for p < p* = sqrt(m_h^2/4 - m_f^2), has a pole at p* and is negative for p > p*. Numerically for the b (m_h/m_b = 29.95, p* = 14.94 m_b): F = +0.56 at p = 0.5 p*, -13.7 at 1.1 p*. So pointwise sign-definiteness at all p holds only for the top. What holds for every fermion: every ordering is negative for p > p*, and the coefficient of the K^2 (Lambda^2) term is -3y^2/(4pi^2) per ordering (times N_c/3), independent of m_f and m_h. Adding fermion seas makes the Lambda^2 term more negative in every case.
5. The pole of F at p* is the on-shell decay. sympy: |Im Sigma| from the F pole = 3 y^2 (m_h^2 - 4 m_f^2)^{3/2}/(16 pi m_h), identical to m_h Gamma_LO(h -> f fbar) with y = sqrt2 m_f/v. Difference 0. This is a consistency check of the decomposition, not new physics.
6. F + B (top) was checked against the covariant Feynman integrand with k0 integrated numerically (Wick rotation) at p = 0.1 ... 10 m_t. They agree to 8 digits, so the decomposition is exact and complete. (The Wick rotation used there is valid only for m_h < 2 m_f, so this check is for the top case.)
7. At m_f = 0 the quadratic piece persists. No SM symmetry forces Sigma proportional to m_h^2: |H|^2 is invariant under every SM symmetry, so there is no chiral-symmetry analogue.
8. With a 3-momentum cutoff, Sigma ~ -(3 y^2/4pi^2) K^2; with a 4D Euclidean cutoff, -(3y^2/8pi^2) Lambda^2. The factor 2 shows that quadratic-divergence coefficients are regulator dependent (CONSTRAINTS H2). Only their sign is used as a conclusion.

### 2c. Veltman coefficient: normalization (`calc/veltman_running.py`)
Convention as in CONSTRAINTS G: V = -mu^2|H|^2 + lambda|H|^4 (Buttazzo et al. write m^2 = 2 mu^2), 4D Euclidean cutoff Lambda, Landau gauge. The Lambda^2 term of the one-loop effective potential is (Lambda^2/32pi^2) STr M^2(phi) = (C Lambda^2/32pi^2) phi^2 + const. sympy gives

  C = 6 lambda + (9/4) g^2 + (3/4) g'^2 - 6 y_t^2 [- 6 y_b^2 - 2 y_tau^2] = (3/v^2)(m_h^2 + 2 M_W^2 + M_Z^2 - 4 m_t^2).

- Shift of the |H|^2 coefficient: delta mu^2 = C Lambda^2/(16 pi^2) in magnitude. This equals the 1PI h self-energy at fixed v, which is why it matches the top-loop -3y^2 Lambda^2/(8 pi^2) of section 2b.
- Physical mass: holding bare mu^2 and lambda fixed and including the tadpole (shift of v), sympy gives m_h^2 = 2 mu^2 - C Lambda^2/(8 pi^2), so **|delta m_h^2| = |C| Lambda^2/(8 pi^2) = (3 Lambda^2/(8 pi^2 v^2)) |m_h^2 + 2 M_W^2 + M_Z^2 - 4 m_t^2|**, the standard form (Veltman, Acta Phys. Polon. B 12, 437 (1981); Kolda-Murayama hep-ph/0003170).
- Cycle-2 text claimed "delta m_h^2 = C Lambda^2/(16 pi^2) ... not the 3/(8 pi^2 v^2) often quoted". That was wrong (Referee 1, finding 1) and is withdrawn. The script's NOTE is deleted.
- C matches Masina-Quiros, PRD 88, 093003 (2013), arXiv:1308.1242, eq. 12, and Jegerlehner's C1 = 2C (his lambda normalization) [CONFIRMED by LITCHECK].

Measured pole masses (PDG 2024): bracket = -82213 GeV^2, **C = -4.07**. MS-bar at mu = M_t: **C = -3.43**. C = 0 at these masses would need m_t = 96.1 GeV, or m_h = 312.9 GeV.

## 3. Running the Veltman coefficient (`tools/rg_sm.py`, `calc/veltman_running.py`)

RG runner: the shared `tools/rg_sm.py`. MS-bar beta functions from Buttazzo, Degrassi, Giardino, Giudice, Sala, Salvio, Strumia, JHEP 1312, 089 (2013), arXiv:1307.3536, Appendix B. Loop orders: 3 loops for g1, g2, g3, y_t, lambda, m^2; 2 loops for y_b, y_tau. Initial conditions are their NNLO matching fits, eqs. (55)-(60), at mu = M_t, with PDG 2024 inputs.

Validation against their eq. (61) at M_Pl (their inputs), `calc/rg_sm_validation_out.txt`: 3-loop gives g1 = 0.6154, g2 = 0.5055, g3 = 0.4873, y_t = 0.3825, lambda = -0.0144, against their 0.6154, 0.5055, 0.4873, 0.3825, -0.0143 [established: runner validated for the dimensionless couplings]. Open: m(M_Pl) = 139.4 GeV vs their 129.4 GeV. Not used anywhere below (see section 5B).

Results with PDG 2024 central inputs (M_t = 172.57, M_h = 125.20, alpha_s = 0.1180), 3-loop:

| mu (GeV) | C |
|---|---|
| M_t | -3.43 |
| 10^10 | -0.84 |
| 10^16 | -0.35 |
| M_Pl = 1.22e19 | -0.18 |
| 10^22 | -0.04 |
| 10^25 | +0.10 |

Zero of C: log10(mu0/GeV) = 22.83 (3-loop), 22.98 (2-loop), 26.8 (1-loop). Parametric dependence (3-loop): M_t +/- 0.29 GeV moves it by +/-0.35 decades, alpha_s +/- 0.0009 by -/+0.5, M_h +/- 0.33 by about 0.1. Putting the zero at M_Pl needs y_t(M_t) lower by 0.0175, i.e. M_t lower by about 3.2 GeV. No significance is quoted: the MC-vs-pole top-mass ambiguity and the y_t matching theory error are not included. For reference, lambda = 0 at 10^10.66 GeV.

**mu0 is scheme dependent [established].** It combines MS-bar running couplings with a one-loop cutoff coefficient. The gauge-boson part of the Lambda^2 coefficient is gauge- and regulator-dependent in some treatments, and two-loop quadratic terms shift it: Hamada-Kawai-Oda include them; D.R.T. Jones, PRD 88, 098301 (2013), arXiv:1309.7335, disputes their two-loop coefficient. So 10^22.8 GeV is a number in one stated scheme, not a physical prediction.

Literature comparison:
- Hamada, Kawai, Oda, PRD 87, 053009 (2013), arXiv:1210.2538 (erratum PRD 89, 059901 (2014)): bare Higgs mass vanishes at about 10^23 GeV for M_t = 173 GeV, at the Planck scale for M_t ≈ 170 GeV. This line gives 10^23.5 at M_t = 173.34 (Buttazzo inputs). Consistent [CONFIRMED].
- Masina, Quiros, PRD 88, 093003 (2013), arXiv:1308.1242: Veltman condition met "around Planckian scales", "slightly trans-Planckian" for central values [CONFIRMED].
- Jegerlehner, "The hierarchy problem of the electroweak Standard Model revisited", arXiv:1305.6652 (preprint; no journal publication on INSPIRE per LITCHECK). The text gives mu0 ≈ 7×10^16 GeV and y_t(M_Pl) ≈ 0.355; the abstract rounds to about 10^17 GeV. Both numbers were confirmed in the text by LITCHECK; I did not pin the section or equation number. Lowering y_t(M_t) by 0.0286 (to 0.904, about 5 GeV in M_t) reproduces the zero at 7e16 GeV and gives y_t(M_Pl) = 0.356. The cause, his lower top-Yukawa matching, is stated by Jegerlehner himself (1305.6652, introduction; see also Jegerlehner, Kalmykov, Kniehl, PLB 722, 123 (2013), arXiv:1212.4319). This line only reproduces it numerically. The cycle-2 journal reference "Acta Phys. Polon. B 45, 1167 (2014)" belongs to a different paper, arXiv:1304.7813, and is removed.

Verdict on running: C(M_Pl) = -0.18 with current inputs, and the zero is 3.7 decades above M_Pl in this scheme. Any reading as a UV boundary condition is speculation and outside SM scope.

## 4. Is anything here antimatter? (negative)

**No.** [each step established; the general statement is a conjecture-level summary for the S1 synthesis]

1. **Electron.** The cancellation is Lorentz covariance plus chiral symmetry. The hole-theory split is a noncovariant bookkeeping of one Feynman diagram. The antiparticle is required by the Dirac field, but the output (delta m proportional to m) is fixed by chiral symmetry. In Feynman-Stueckelberg language Tb is the backward time ordering. CONSTRAINTS H3: the interpretation adds no physics.
2. **Statistics, not charge conjugation, supplies the cancelling term.** The Pauli-blocked pair requires the protected particle to be a fermion of the same field as the sea. A scalar has no Fermi sea and no exclusion. Weisskopf 1939 states that charged Bose particles keep a quadratically divergent self-energy [CONFIRMED by LITCHECK from the abstract].
3. **Fermion seas only add to the Higgs divergence.** For every SM fermion the Lambda^2 coefficient of each time ordering is negative (section 2b items 3-4; pointwise at all p only for the top, above threshold for the rest). CPT forces particle and antiparticle to enter identically (CONSTRAINTS D), so no particle/antiparticle imbalance can be used to arrange a cancellation.
4. **The bosonic side: charged pairs vs self-conjugate fields** (`calc/veltman_running.py`, section 1b). Per-species contributions to C at mu = M_t (MS-bar):

   | species | self-conjugate? | C_i | value |
   |---|---|---|---|
   | W+, W- | no (each other's antiparticle) | 3g^2/4 each | +0.315 each |
   | G+, G- | no | lambda each | +0.126 each |
   | Z | yes | 3(g^2+g'^2)/4 | +0.411 |
   | h | yes | 3 lambda | +0.379 |
   | G0 | yes | lambda | +0.126 |
   | photon | yes | 0 (massless) | 0 |
   | t, tbar | no | -3 y_t^2 each | -2.611 each |

   Self-conjugate bosons alone give +0.916; charged boson pairs alone give +0.882. Both groups are positive, with the same sign per degree of freedom. So the positive (cancelling) side of the Veltman condition is not "the antiparticle half" of anything: removing every charged pair leaves a positive self-conjugate contribution of the same size.

   The structural reason: the Lambda^2 coefficient is STr M^2 = Sum (-1)^{2J}(2J+1) Tr M^2, a trace over the mass-squared matrix. A charged pair W+-, G+- is a unitary change of basis of two degenerate real (self-conjugate) fields, W+- = (W1 -+ i W2)/sqrt2, and the trace is invariant: sympy shows Tr = 2 M_W^2 in both bases. Likewise a Dirac top is two degenerate Majorana components with the same trace (4 real-component degrees of freedom per colour either way). So "which states are antiparticles" is a choice of basis that C cannot depend on. The sign is (-1)^{2J}, spin-statistics [established].

   The SM has no self-conjugate fermion (Majorana neutrinos are excluded by A1/A2), so on the fermion side the basis argument is the only control. It is sufficient: it shows the coefficient is the same whether the top is described as t + tbar or as two Majorana components.
5. **Veltman cancellation is boson-fermion statistics.** The same sign structure SUSY exploits, but in the SM the coefficients are unrelated by any symmetry and do not cancel at accessible scales (section 3). Murayama hep-ph/0002232 sec. 1.3 and the Snowmass naturalness report (Craig et al., arXiv:2205.05708, sec. 2) state the same contrast.
6. **Dim reg.** In dimensional regularization the Lambda^2 term is absent, so the antimatter question does not arise there; it is not answered negatively. The physical hierarchy problem is then sensitivity to heavy thresholds, delta m_h^2 ~ (coupling) M_heavy^2/16pi^2. The SM has no heavy states below M_Pl, so there is nothing for antimatter (or anything else) to cancel within SM scope. Bardeen's argument that the SM alone is natural in this sense (W. A. Bardeen, "On naturalness in the standard model", FERMILAB-CONF-95-391-T (1995) [bibliographic CONFIRMED; content not checked]) is about the absence of heavy particles, not antimatter. Whether gravity reintroduces the problem is outside SM scope.

So the analogy "antimatter protected the electron mass, maybe it protects the Higgs" fails for a precise reason: what protected the electron was a chiral symmetry acting on a fermion, with the same field's sea providing the Pauli-blocked counter-term. The Higgs is a scalar with no such symmetry, the SM fermion seas are a source of its Lambda^2 sensitivity, and the bosonic cancelling terms carry their sign from statistics, identically for charged pairs and self-conjugate fields.

## 5. Radiative EWSB (#4) (`calc/cw_radiative_ewsb.py`)

(A) Coleman-Weinberg, PRD 7, 1888 (1973), with the tree mass term set to zero: V = A phi^4 + B phi^4 ln(phi^2/mu^2) has a minimum only for B > 0, with m_h^2 = 8 B v^2. With measured masses, Sum n_i (-1)^F m_i^4 = -1.0e10 GeV^4 and B = -4.3e-3 < 0, so the stationary point is a maximum. **No radiative EWSB.**
- Top-mass threshold, self-consistent (m_h is an output, m_h^2 = 8Bv^2, so B -> 0 forces m_h -> 0): B < 0 for m_t > (Sum_{W,Z} n m^4/12)^{1/4} = **78.6 GeV**. The cycle-2 value 87.5 GeV fed the measured m_h into B, which is circular in a scale-invariant theory (Referee 1, finding 8); it is printed only for comparison.
- Without the top, W and Z alone give m_h = 9.8 GeV, not 125.
[established; classic result: Weinberg, PRL 36, 294 (1976); Linde, JETP Lett. 23, 64 (1976), both CONFIRMED]

(B) SUSY's radiative EWSB is the RG-driven sign flip of m_Hu^2, driven by additive stop soft masses in its beta function. In the SM MS-bar scheme, beta(m^2) is proportional to m^2 at all orders (mass-independent scheme, m^2 the only dimensionful parameter), so the sign of m^2 is RG-invariant [established]. This conclusion depends only on that proportionality, not on the coefficients, so it is unaffected by the unresolved 139.4 vs 129.4 GeV discrepancy in m(M_Pl). The m(mu) values the script prints (131-144 GeV, m^2 > 0 from M_t to 10^20 GeV) are illustrative only until that discrepancy is resolved.

(C) Cutoff-language variant (Jegerlehner): C < 0 means top loops push the bare mu^2 toward the broken phase below mu0. This depends on the regulator (Lambda^2 terms are absent in dim reg, CONSTRAINTS G and H2). It is the fermion-sea contribution of section 2b, not an antimatter effect, and it does not produce m_h or v, which remain inputs. [established that it is regulator dependent; any physical "triggering" reading is speculation]

## 6. Dead ends / open issues
- m(M_Pl) from the shared runner (139.4 GeV) disagrees with Buttazzo eq. (61f) (129.4 GeV); the dimensionless couplings match to 1e-4. The 1-loop m^2 beta in `tools/rg_sm.py` matches the standard form (m^2 (6 lambda + 3 y_t^2 - 9g_2^2/4 - 9g_1^2/20) per ln mu^2); the discrepancy is likely in the initial value or higher-loop terms. Not resolved; not used in any conclusion. Flagged for whoever owns `tools/rg_sm.py`.
- mu0 is quoted for the one-loop Landau-gauge Lambda^2 coefficient only; scheme dependent (section 3).
- Weisskopf's own finite constant was not compared with c = ln 2 - 1/6.
- Jegerlehner's 7×10^16 figure: section/equation number not pinned.

## 7. Consistency checks (replaces cycle-2 "Testable / falsifiable content")

This is a negative result. **It makes no falsifiable prediction of its own.** The only number that could be tested against data is the top mass at which C would vanish at M_Pl (about 3.2 GeV below the PDG pole mass in this scheme, about 1.2 decades of mu0 per GeV of M_t). That tests a coincidence for which the line offers no mechanism (H1), and mu0 is scheme dependent (H2), so it is not offered as a prediction. Gate item 7 is met, if at all, only by the consistency checks below, each of which could have failed:

1. Time-ordered F + B equals the covariant Feynman integrand (k0 integrated numerically) to 8 digits at p = 0.1 ... 10 m_t (`higgs_top_ofpt_out.txt`).
2. The hole-theory electron self-energy reproduces the covariant QED log coefficient 3 alpha/(2 pi), and the linear divergence cancels sector by sector (`weisskopf_ofpt_out.txt`).
3. Chiral zero: the hole-theory integrand vanishes identically at m = 0; the one-electron theory does not.
4. The threshold pole of the forward Higgs ordering reproduces m_h Gamma_LO(h -> f fbar) exactly (sympy difference 0). The h -> b bbar rate is measured (CONSTRAINTS C1), so this ties the decomposition to data, though it is standard SM physics, not a test of anything specific to this line.
5. Per-species contributions sum to C, and the charge-basis and real-basis traces agree (`veltman_running_out.txt`).
6. Runner reproduces Buttazzo eq. (61) couplings to 1e-4; the Veltman zero at Buttazzo inputs (10^23.5 GeV at M_t = 173.34) agrees with HKO's ~10^23 GeV at M_t = 173 GeV.
7. The self-consistent CW top-mass threshold (78.6 GeV) and the W,Z-only m_h = 9.8 GeV agree with the Linde-Weinberg-type bound up to the sqrt2 factor noted by Referee 1.

## 8. Response to referee 1

| # | Finding | Change |
|---|---|---|
| 1 | delta mu^2 vs delta m_h^2 factor 2 | Accepted. Section 2c rewritten: C Lambda^2/16pi^2 = delta mu^2 (= 1PI self-energy at fixed v); delta m_h^2 = C Lambda^2/8pi^2 in magnitude, derived in `veltman_running.py` with the tadpole included (sympy: m_h^2 = 2 mu^2 - C Lambda^2/8pi^2). Wrong sentence and script NOTE deleted. `higgs_top_ofpt.py` labels changed to Sigma. Sign of "delta" stated as convention dependent. |
| 2 | "negative pointwise" only true for top | Accepted. Section 2b item 4 and section 4 item 3 now restrict pointwise negativity to 2 m_f > m_h. For light fermions: F > 0 below p*, pole at p*, all orderings negative above p*, Lambda^2 coefficient negative and m_f-independent. Added numerical b-quark check and the Im Sigma = m_h Gamma check in `higgs_top_ofpt.py`. |
| 3 | W+W-, G+G- are particle-antiparticle pairs | Accepted. Section 4 item 4 added: per-species table grouped by self-conjugacy (all bosons +, all fermions -), each group positive on its own, and the trace/basis-invariance argument showing C cannot depend on the particle/antiparticle labelling. Printed by `veltman_running.py` section 1b. Headline now says the sign is from spin-statistics, with this argument behind it. |
| 4 | Section 8 predicts nothing | Accepted. Replaced by section 7 "Consistency checks", with an explicit statement that there is no falsifiable prediction beyond the scheme-dependent M_t coincidence. mu0 tagged scheme dependent (section 3), Jones 1309.7335 cited. Added check 4 (decay width). |
| 5 | "11 sigma" | Accepted. Now "about 3.2 GeV lower", no significance; script prints the caveat. |
| 6 | Tneg history | Accepted. Tneg attributed to Oppenheimer / Waller 1930; Weisskopf 1934 described as a hole-theory calculation with Furry's sign correction, log in the erratum. Also fixed in PROPOSAL.md and the `weisskopf_ofpt.py` docstring. |
| 7 | Jegerlehner citation | Accepted. Cited as arXiv preprint; APPB 45, 1167 reassigned to 1304.7813 and dropped. Partly unmet: I could not give a section/equation number for 7×10^16 (LITCHECK confirmed it is in the text; abstract says ~10^17). |
| 8 | CW threshold circular | Accepted. Self-consistent threshold = W,Z-only threshold = 78.6 GeV (B -> 0 forces m_h -> 0). The referee's "near 87 GeV" for the W,Z-only version is not what the script gives; W,Z only gives 78.6 GeV. Conclusion unchanged. |
| 9 | Dim reg wording | Accepted. Section 4 item 6: the question does not arise in dim reg; no SM heavy thresholds. Checklist G updated. |
| 10a | Stale "(3/2)" text about CONSTRAINTS G | Accepted, removed. Line now uses the CONSTRAINTS G convention explicitly. |
| 10b | B9, B10, F3 missing | Accepted. Full checklist in section 10. |
| 10c | -3.43 vs -3.42 | Accepted. Script table now starts at exactly mu = M_t (-3.426); both places say -3.43. |
| 10d | m^2 runner values used in 5(B) | Accepted. 5(B) now says the sign result depends only on beta(m^2) ∝ m^2; GeV values marked illustrative; script prints the caveat. |
| R | Use shared tools | `calc/rg_sm.py` was byte-identical to `tools/rg_sm.py` (diff, cycle 3). Replaced by a shim that re-exports the shared module; scripts now put `tools/` first on the path and import `rg_sm`/`sm_inputs` from there. Outputs unchanged except for the edits above. |

LITCHECK corrections: Jegerlehner journal ref (fixed), Weisskopf 1934 attribution (fixed), Masina-Quiros journal ref and Weisskopf 1939 Bose claim marked CONFIRMED, Veltman APPB 12, 437 (1981), Murayama hep-ph/0002232 and Jones 1309.7335 added, Jegerlehner's own statement of the y_t cause credited.

Disagreement: none of substance. One numerical correction to finding 8 (78.6 GeV, not ~87 GeV, for the self-consistent threshold).

## 9. What is new (ruling R5)

Honest verdict: **nothing physically new.** The central conclusion, that the positron protects the electron mass through chiral symmetry and nothing in the SM does the same for the Higgs, is the framing of Murayama hep-ph/0002232 sec. 1.3 and the Snowmass naturalness report arXiv:2205.05708 sec. 2. The Veltman-zero running is HKO 1210.2538 and Masina-Quiros 1308.1242 with updated inputs. The CW failure is 1973/1976 textbook material.

What the line adds, all at the level of explicit checks rather than new results:
1. The self-conjugacy / basis-invariance argument (section 4 item 4) stated specifically against the "antimatter" reading of the Veltman condition: the Lambda^2 coefficient is a trace and cannot depend on the particle/antiparticle labelling; self-conjugate bosons alone carry the same sign and similar size as charged pairs. Elementary; I have not seen it written for this question, but I have not searched exhaustively [conjecture that it is unpublished in this form].
2. The time-ordered decomposition of the Higgs fermion-loop self-energy, checked to 8 digits against the covariant integrand, with the light-fermion threshold structure and the Im Sigma = m_h Gamma identity. Pedagogical (LITCHECK section 3).
3. A numerical update of the Veltman zero with PDG 2024 inputs and 3-loop running (10^22.8 GeV, scheme dependent) and a numerical reproduction of Jegerlehner's 7×10^16 GeV from his lower y_t matching (cause already stated by Jegerlehner).

Recommendation: L01 does not pass gate item 6 on its own. Its items 1-2 above are suitable input for the planned S1 synthesis line (antiparticle contributions fixed by CPT + spin-statistics).

## 10. CONSTRAINTS checklist

- **A1 (SM only):** only SM fields used. SUSY appears only as a comparison target (MSSM m_Hu^2 sign flip). Pass.
- **A2 (neutrino mass):** not used. Neutrino Yukawas omitted; any Dirac-type y_nu < 1e-12 would change C by < 1e-23, so the result is insensitive to the mass mechanism. Majorana neutrinos are not used in the self-conjugacy argument. Pass.
- **A3 (reformulations):** hole theory and time ordering are used only as bookkeeping, and every result is checked against or restated in the covariant formulation (section 2b item 6, section 2a). No extra states. Pass.
- **B1 (K0 mass difference):** no particle/antiparticle mass difference introduced; CPT respected. Pass.
- **B2 (pbar/p q/m):** no particle/antiparticle charge or mass asymmetry. Pass.
- **B3 (pbar magnetic moment):** none introduced. Pass.
- **B4 (antihydrogen 1S-2S):** none introduced. Pass.
- **B5 (ALPHA-g):** gravity not used. Not applicable.
- **B6 (e-/e+ g-factor):** none introduced; the Weisskopf calculation is CPT symmetric. Pass.
- **B7 (electron EDM):** no CP violation used. Not applicable.
- **B8 (CKM J):** CKM phase not used. Not applicable.
- **B9 (baryon CPV, LHCb):** not used. Not applicable.
- **B10 (neutron EDM):** theta-bar not used. Not applicable.
- **C1 (Higgs):** m_H = 125.20 GeV (PDG 2024) via `tools/sm_inputs.py`; SM Higgs couplings assumed, consistent with C1. Pass.
- **C2 (EW, top):** PDG 2024 M_Z, M_W, m_t, G_F via `tools/sm_inputs.py`. Pass.
- **C3 (SUSY limits):** the line introduces no new states, so no superpartner signatures arise; it does not claim to reproduce the SUSY cancellation, so the null LHC results are consistent with it. Pass.
- **C4 (muon g-2):** no claim made. Not applicable.
- **D (gauge couplings, CPT in beta functions):** alpha_s, alpha_em, sin^2 theta_W at M_Z via shared tools; running 3-loop (gauge, y_t, lambda, m^2), 2-loop (y_b, y_tau), stated. CPT equal counting of particle and antiparticle used in section 4 item 3. Pass.
- **E1 (Omega_c h^2):** not used. Not applicable.
- **E2 (Omega_b h^2):** not used. Not applicable.
- **E3 (eta):** not used. Not applicable.
- **E4 (rho_Lambda):** vacuum energy not addressed (that is L04). Not applicable.
- **E5 (DM properties):** not used. Not applicable.
- **E6 (N_eff):** not used. Not applicable.
- **E7 (Sum m_nu):** not used. Not applicable.
- **E8 (KATRIN):** not used. Not applicable.
- **E9 (symmetric cosmologies):** none assumed. Not applicable.
- **E10 (SM baryogenesis):** no baryogenesis claim. Not applicable.
- **F1 (p -> e+ pi0):** no baryon-number violation. Not applicable.
- **F2 (sphalerons):** not used. Not applicable.
- **F3 (n -> nbar):** no Delta B = 2. Not applicable.
- **G (hierarchy facts):** Veltman normalization now matches CONSTRAINTS G (delta mu^2 = C Lambda^2/16pi^2, delta m_h^2 = C Lambda^2/8pi^2, stated in the Claim section). Nothing is "solved" by regulator choice; in dim reg the question does not arise (section 4 item 6). Weisskopf reproduced. Pauli conditions and vacuum energy not used. Pass.
- **H1 (no numerology):** the near-zero of C at high scale is reported as a coincidence of running couplings with no mechanism claimed and no prediction built on it. Pass.
- **H2 (regulator independence):** conclusions use only scheme-independent facts: sign of every fermion's Lambda^2 coefficient, spin-statistics signs, trace invariance, chiral symmetry, sign invariance of m^2 under MS-bar running. The K^2 vs Lambda^2 factor 2 and mu0 are labelled scheme dependent. Pass.
- **H3 (interpretations):** the Dirac-sea / time-ordered split is shown equal to the covariant integrand, and every conclusion is restated covariantly. Pass.
- **H4 (committed scripts):** every number has a script in `calc/` (shared runner in `tools/`), all rerun from inside `calc/` in cycle 3 with outputs saved. Pass.
