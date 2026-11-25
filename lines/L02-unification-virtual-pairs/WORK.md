# L02-unification-virtual-pairs: WORK

Target: SUSY result #2 (gauge coupling unification). All numbers below come from scripts in `calc/` with saved outputs (`*.txt`). Run any of them with `python <script>.py` from `calc/`.

| Script | Output | What it does |
|---|---|---|
| `rg_sm3.py` | (module) | SM RGEs at 1/2/3 loops (g1,g2,g3,yt,lambda), MSSM 1/2-loop gauge for comparison |
| `validate_rg.py` | `validate_rg.txt` | reproduces arXiv:1307.3536 eq. (61) Planck-scale couplings |
| `unification.py` | `unification.txt`, `sm_3loop_alpha_inv.txt` | crossing scales, spread, thresholds, required alpha_s; MSSM reference |
| `counting.py` | `counting.txt` | particle/antiparticle state sum for b_i; weight scan; 2-loop weighted runs |
| `fs_residues.py` | `fs_residues.txt` | Feynman-Stueckelberg pole bookkeeping of a one-loop bubble |
| `empirical_counting.py` | `empirical_counting.txt` | Delta alpha_lep and R-ratio with single vs double antiparticle counting |
| `proton_decay.py` | `proton_decay.txt` | d=6 lifetime estimate at each crossing scale |
| `hypercharge_norm.py` | `hypercharge_norm.txt` | U(1) normalisation that would make alpha_1 hit M23 (convention check) |

---

## 1. Antiparticle counting in beta functions

### 1.1 The coefficients depend only on group, representations and multiplicities [established]

One-loop, for gauge group factor G_i (background-field method, any gauge, MS-bar or momentum subtraction):

b_i = -(11/3) C2(G_i) + (2/3) sum_{Weyl fermions} T_i(R) + (1/3) sum_{complex scalars} T_i(R)

(Gross-Wilczek PRL 30, 1343 (1973), DOI 10.1103/PhysRevLett.30.1343; Politzer PRL 30, 1346 (1973), DOI 10.1103/PhysRevLett.30.1346; two loops: Machacek-Vaughn NPB 222, 83 (1983), DOI 10.1016/0550-3213(83)90610-7.) Every input on the right is a group-theory datum of the field content. Two formulations with the same group, same representations and same multiplicities have identical b_i, B_ij, and identical higher-loop coefficients, since those are also built from Casimirs, Dynkin indices and Yukawa/quartic traces. Therefore any reformulation that is equivalent to the SM (CONSTRAINTS A3.1) has the SM beta functions. [established]

### 1.2 Particle and antiparticle are already counted, once [established; reproduced]

A left-handed Weyl field psi in representation R creates a particle in R with helicity -1/2 and its antiparticle in R-bar with helicity +1/2. T(R-bar) = T(R), and the U(1) charge flips sign, so its Y^2 is unchanged. The 2/3 per Weyl field in b_i is exactly (1/3) per on-shell helicity state, particle and antiparticle each. `counting.py` part 1 lists every SM state explicitly (45 Weyl fields x {particle, antiparticle} plus H and H-bar), applies 1/3 T(R) per fermionic state and 1/6 T(R) per scalar particle-or-antiparticle state, and gets b = (41/10, -19/6, -7) exactly (`counting.txt`). The antiparticle states supply exactly half of every fermion and scalar contribution; they are not missing and cannot be "added".

Feynman-Stueckelberg reading: the Feynman propagator has two poles, the positive-frequency (particle) one and the negative-frequency one (particle backward in time = antiparticle). `fs_residues.py` does the energy integral of a one-loop bubble by residues and gets exactly two time-ordered terms, 1/(q0 - E1 - E2) (pair produced by the external field) and -1/(q0 + E1 + E2) (Z-graph: pair from the vacuum first). Symbolic residue sum minus the two-ordering formula = 0, and direct numerical integration at finite epsilon agrees to 1e-5 (`fs_residues.txt`). There is no third term. Adding "the antiparticle loop" on top means counting one of these poles twice; at q0 = 0.7, E1 = 1, E2 = 1.3 that changes the bubble from -0.184i to -0.248i, i.e. it is a different theory. [established; check reproduced]

Wick-contraction reading: <T j^mu(x) j^nu(y)> with j = psi-bar gamma psi has exactly one connected contraction. For the two-point function the two orientations of the fermion loop are the same diagram. (For three-point loops the two orientations are distinct and both are summed; their C-odd combination is what Furry's theorem removes.) [established]

Dirac-sea (hole theory) reading: vacuum polarisation was first computed in hole theory with a filled sea and gave the same charge renormalisation and the same Uehling potential as later covariant QED (Heisenberg, Z. Phys. 90, 209 (1934), DOI 10.1007/BF01333516; Uehling, Phys. Rev. 48, 55 (1935), DOI 10.1103/PhysRev.48.55; Weisskopf, Kgl. Danske Vid. Selsk. Mat.-fys. Medd. 14, no. 6 (1936) [unverified citation, no DOI]). The sea's response to an external field is the pair-creation amplitude above; the hole is the antiparticle. Hole theory needs Heisenberg's charge-symmetrised current to remove the infinite sea charge; that subtraction is a constant and does not touch the q^2-dependence that drives running. [established] Hole theory has no version for bosons (no Pauli blocking), so the W, gluon and Higgs loops have no sea reading at all (Weinberg, QFT Vol. I, ch. 1, DOI 10.1017/CBO9781139644167). [established]

### 1.3 CPT / C forbid any asymmetric contribution [established]

The running of g_i comes from the gauge two-point function Pi^{mu nu}_{ab}(q). Lorentz covariance allows (q^2 g^{mu nu} - q^mu q^nu) Pi(q^2) and an epsilon^{mu nu rho sigma} q_rho q_sigma structure, which vanishes identically. A particle-antiparticle asymmetric (C-odd) piece would be proportional to an odd trace such as sum Y, sum Y^3 or d^{abc}; those cannot appear in a two-point function of a single gauge field. `counting.txt`: sum over fermion states of Y = 0, and the Y^2 sum is 10 for particles and 10 for antiparticles. CPT (exact; CONSTRAINTS A1, B1-B6) maps each particle state to an antiparticle state with the same mass and conjugate representation, so the two halves are equal term by term at every loop order. The only place a particle-antiparticle asymmetry enters is a background with net charge density (chemical potential mu or the cosmological baryon asymmetry eta ~ 6e-10). That changes in-medium polarisation at momenta q <~ mu, T and decouples from the UV running that matters for unification. [established]

### 1.4 What non-equivalent reweightings would do (and why they are dead) [established for the algebra; the reweightings themselves are not SM]

Write b_i = w_V b_i^V + w_F b_i^F + w_S b_i^S, with b^V = (0, -22/3, -11) (gauge+ghost), b^F = (4, 4, 4) (three generations), b^S = (1/10, 1/6, 0) (Higgs). `counting.py` part 2 (sympy):

- One-loop unification condition (B-test): (b2 - b3)/(b1 - b2) must equal (a2^-1 - a3^-1)/(a1^-1 - a2^-1) at MZ = 0.7178. The ratio is 5(-w_S - 22 w_V)/(2(w_S - 110 w_V)). **It is independent of w_F.** Because each generation fills complete SU(5) multiplets (5-bar + 10), fermions shift b_1, b_2, b_3 equally (Delta b = (2,2,2) if antifermion states are counted twice). So no reweighting of fermion antiparticle loops, equivalent or not, can affect one-loop unification. [established; Georgi-Quinn-Weinberg PRL 33, 451 (1974), DOI 10.1103/PhysRevLett.33.451, use the same fact]
- SM value 0.5275, MSSM value 0.7143, measured 0.7178.
- Needed: w_S = 7.45 (about 7-8 Higgs doublets; unification then at 10^13.7 GeV, alpha^-1 = 38.6, which is excluded by proton decay anyway, see section 4) or w_V = 0.134 (gauge self-interaction cut by 7x, which contradicts the measured alpha_s running and the Slavnov-Taylor identities that fix the -11/3 C2(G)).
- Two-loop gauge-only runs with weights (`counting.txt` part 3), best-point spread in alpha^-1: SM 3.20; antifermion states twice (w_F = 3/2) 3.28; every fermion field twice (w_F = 2) 3.44; particles only (w_F = w_S = 1/2) 3.45; antifermion + anti-Higgs states twice 2.97. None comes close. Only w_S = 7.45 gets down to 0.54.

Empirical exclusion of double counting (`empirical_counting.py`) [established]:
- Leptonic running of alpha_em from 0 to MZ at one loop with each lepton counted once: 0.03142 (3-loop literature value 0.031498, Steinhauser PLB 429, 158 (1998), hep-ph/9803313). Counting antileptons again: 0.06284, which would put alpha^-1(MZ) near 124 instead of the measured ~129 on-shell value.
- The hadronic running is extracted from data through the dispersion relation from sigma(e+e- -> hadrons) (e.g. Davier, Hoecker, Malaescu, Zhang, EPJC 80, 241 (2020), arXiv:1908.00921; Keshavarzi, Nomura, Teubner, PRD 101, 014029 (2020), arXiv:1911.00367). Unitarity ties the imaginary part of the bubble to the pair-production rate. R = N_c sum Q^2 (1 + alpha_s/pi) = 3.82 for five flavours, consistent with data in the 10-40 GeV region; double counting would predict 7.6. The final state q q-bar contains exactly one particle and one antiparticle; the counting is measured, not interpreted. [established]
- QCD with every quark field counted twice: b_3 = -11 + 8 = -3 (still asymptotically free but alpha_s would run visibly slower); with the NCG fourfold doubling (below) b_3 = -11 + 16 = +5 and QCD would lose asymptotic freedom, contradicting the measured alpha_s running. [established]

### 1.5 Reformulations [established unless tagged]

- **Connes-Chamseddine NCG / spectral action.** The almost-commutative spectral triple has fermion Hilbert space H_F containing f and f^c for each SM fermion. Taken naively in Euclidean signature, "each particle appears four times, not once" (Barrett, J. Math. Phys. 48, 012303 (2007), hep-th/0608221; Lizzi, Mangano, Miele, Sparano, PRD 55, 6357 (1997), hep-th/9610035). This is literally antiparticle (and mirror) over-counting. The SM-equivalent version removes it by the KO-dimension-6 real structure and the physical-subspace / Pfaffian projection J psi = psi, chi psi = psi (Connes, JHEP 0611:081 (2006), hep-th/0608226; Barrett 2007). After that projection the fermion content is one copy of the SM (plus nu_R, which A1/A2 removes), and the beta functions are the SM ones. Before the projection the theory is not equivalent to the SM (wrong particle counts, b_3 = +5). Either way the doubling is uniform across complete generations and drops out of the one-loop B-test (1.4). [established]
- **Division algebras (Dixon; Furey).** Furey, EPJC 78, 375 (2018), arXiv:1806.00612, obtains one generation (plus nu_R) and G_SM = SU(3)xSU(2)xU(1)/Z6 from minimal ideals of C (x) O, with a possible extra U(1)_X. Restricted to the SM sector (no nu_R, no U(1)_X; A3.2), the representations and multiplicities are the SM's, so the b_i are the SM's. The algebra encodes particle and antiparticle as the ideal and its conjugate, i.e. the same two charge states as 1.2. [established that the reps match; detailed equivalence of the dynamics is not claimed in those papers, A3.3 caveat]
- **Hypercharge normalisation.** "Unification" of alpha_1 requires choosing alpha_1 = k alpha_Y. The SM does not fix k; k = 5/3 comes from embedding in SU(5)/SO(10) (Baez-Huerta, Bull. AMS 47, 483 (2010), arXiv:0904.1556). `hypercharge_norm.py`: making alpha_1 pass through the alpha_2 = alpha_3 point at 10^16.47 GeV would need k = 1.339. Choosing k to force unification is a high-scale relation (A3.2) and numerology (H1). Not used. [established]

**Conclusion of section 1:** in any SM-equivalent bookkeeping, antimatter is already in the beta functions with weight fixed by the field content, verified by data, and at one loop fermion antimatter contributes nothing to the non-unification. [established]

---

## 2. Numerical running

### 2.1 Implementation and validation

`rg_sm3.py`: x = (g1^2, g2^2, g3^2, yt^2, lambda) vs ln mu^2, g1 GUT-normalised, V = lambda |H|^4. Gauge at 1/2/3 loops including yt and lambda at 3 loops; yt and lambda at the same loop order (3-loop terms numeric). Transcribed from Buttazzo et al., JHEP 1312, 089 (2013), arXiv:1307.3536, App. B eqs. (96)-(101). Cross-checked by hand against Mihaila-Salomon-Steinhauser, PRL 108, 151602 (2012), arXiv:1201.5868 eq. (5), using mu^2 d(alpha/pi)/dmu^2 = dg^2/dln mu^2 /(4 pi^2): b_i/4, B_ij/16, the yt^4 g1^4 3-loop coefficient 189/16, the lambda g1^6 coefficient 27/50, the g2^6 coefficient 324953/1728 and the g3^6 coefficient 65/2 all agree. b, tau and light Yukawas set to zero (enter gauge running at 2 loops with y_b^2 ~ 3e-4).

Validation (`validate_rg.txt`): with the 1307.3536 central inputs, 3-loop running to M_Pl = 1.2209e19 GeV gives g1 = 0.6154, g2 = 0.5055, g3 = 0.4873, yt = 0.3824, lambda = -0.0143 vs published 0.6154, 0.5055, 0.4873, 0.3825, -0.0143. [established: runner correct to 4 digits]

Inputs:
- Set A: NNLO-matched MS-bar couplings at mu = Mt from 1307.3536 eqs. (55), (57)-(60) with PDG-2024 Mt = 172.57, Mh = 125.20, alpha_s = 0.1180, MW = 80.369 (sm_inputs.py). alpha^-1(Mt) = 58.689, 29.960, 9.256; yt = 0.9329; lambda = 0.1262.
- Set B: PDG MS-bar alpha_s, alpha_em^-1 = 127.951, sin^2 theta_W = 0.23129 at MZ, run directly in the 6-flavour SM. alpha^-1(MZ) = 59.014, 29.594, 8.475. Caveat: these are 5-flavour quantities; running them in the full SM from MZ is a scheme mismatch. The A vs B difference measures it.

### 2.2 SM results (`unification.txt`) [established]

| | M12 (GeV) | a^-1 | M13 | a^-1 | M23 | a^-1 | best spread (at) | a3^-1 - a12^-1 at M12 |
|---|---|---|---|---|---|---|---|---|
| A 1-loop | 10^13.03 | 42.48 | 10^14.39 | 40.43 | 10^16.97 | 47.06 | 3.63 (10^14.39) | -5.55 |
| A 2-loop | 10^13.05 | 42.28 | 10^14.25 | 40.46 | 10^16.47 | 46.21 | 3.19 (10^14.25) | -4.91 |
| A 3-loop | 10^13.05 | 42.27 | 10^14.25 | 40.46 | 10^16.47 | 46.19 | 3.18 (10^14.24) | -4.90 |
| B 1-loop | 10^13.01 | 42.41 | 10^14.38 | 40.35 | 10^16.99 | 47.04 | 3.67 | -5.60 |
| B 2-loop | 10^13.03 | 42.20 | 10^14.23 | 40.38 | 10^16.47 | 46.15 | 3.20 | -4.92 |
| B 3-loop | 10^13.03 | 42.19 | 10^14.23 | 40.38 | 10^16.46 | 46.12 | 3.19 | -4.91 |

- Best spread = min over mu > 1e10 GeV of max_i alpha_i^-1 - min_i alpha_i^-1. It sits at M13 (the crossing of the two outer curves). Relative spread 7.7% at 2-3 loops.
- Minimal threshold correction: alpha_3^-1 must be shifted by +4.9 (11.6% of alpha_12^-1) at M12, or equivalently a spread of 3.2 in alpha^-1 absorbed by thresholds at the best point. Any such threshold needs heavy states, which are not in the SM.
- alpha_s(MZ) that would give exact unification (set B): 0.0711 (1-loop), 0.0738 (2-loop), 0.0739 (3-loop), versus 0.1180 +- 0.0009 measured: about 49 sigma.
- alpha_s +- 1 sigma (A, 3-loop): spread 3.14 to 3.22, M23 10^16.42 to 10^16.51.
- 3-loop vs 2-loop: shifts of <= 0.03 in alpha^-1 and <= 0.01 decades. Input-scheme (A vs B): <= 0.08 in alpha^-1, <= 0.02 decades. Both negligible against the 3.2 gap.

### 2.3 MSSM reference (comparison only; superpartners are not in any mechanism here)

SM below a common M_SUSY, MSSM above (b = (33/5, 1, -3), B_ij standard, tan beta = 10, MS-bar to DR-bar conversion at M_SUSY at 2 loops). Single common threshold is a simplification.

| M_SUSY | loops | set | best spread | at | a^-1 | alpha_s needed (set B) |
|---|---|---|---|---|---|---|
| 1 TeV | 1 | A | 0.33 | 10^16.17 | 25.80 | 0.110 |
| 1 TeV | 2 | A | 0.12 | 10^16.15 | 25.21 | 0.1206 |
| 2 TeV | 1 | A | 0.42 | 10^16.12 | 26.22 | 0.108 |
| 2 TeV | 2 | A | 0.02 | 10^16.10 | 25.66 | 0.1183 |
| 3 TeV | 1 | A | 0.47 | 10^16.10 | 26.46 | 0.107 |
| 3 TeV | 2 | A | 0.03 | 10^16.07 | 25.92 | 0.1170 |

Consistent with the CONSTRAINTS D reference (~2e16 GeV, alpha_GUT^-1 ~ 24-26). [established] The SM gap (3.2) is about 30-150 times the MSSM 2-loop gap.

---

## 3. Spectral action boundary condition

- The Chamseddine-Connes-Marcolli spectral action gives g3^2 = g2^2 = (5/3) g1^2 at the cutoff Lambda (Chamseddine, Connes, Marcolli, Adv. Theor. Math. Phys. 11, 991 (2007), hep-th/0610241). [established]
- Not allowed here: it is an extra high-scale relation that the SM does not contain (CONSTRAINTS A3.2, OVERSEER_PROMPT scope condition 2). The CCM model also includes right-handed neutrinos with Majorana masses (A1, A2). [established]
- Even if it were allowed as an input, it is a condition, not a mechanism: it does not change the running, and section 2 shows there is no Lambda where it holds. The best you can do is the 10^14.24 GeV point with a 3.18 spread, or impose two of the three equalities at M23 = 10^16.47 GeV with alpha_1^-1 off by 46.19 vs 37.10 (= (3/5) 61.83). [established, computed] CCM take Lambda ~ 1e17 GeV and treat the mismatch as an uncertainty [unverified detail of their treatment].
- Prediction failures: CCM predicted m_H ~ 170 GeV (hep-th/0610241 abstract), excluded at 95% CL by the 2008 Tevatron combination (CDF and D0, arXiv:0808.0534) and in conflict with m_H = 125.20 GeV. The repair (Chamseddine-Connes, JHEP 1209, 104 (2012), arXiv:1208.1030) adds a real scalar sigma, explicitly listed as forbidden in A3.2. Beyond that, extensions such as Pati-Salam spectral models (Chamseddine, Connes, van Suijlekom, JHEP 1311, 132 (2013), arXiv:1304.8050 [unverified citation]) add new fields. [established]

---

## 4. Proton decay (CONSTRAINTS F1)

In the SM-only setting no scale "emerges". There is no X boson, and B is violated only by sphalerons/instantons (F2), whose zero-temperature rate is ~1e-165. The crossing points are just where curves cross. [established]

If one placed a gauge-mediated d=6 operator at a crossing scale (`proton_decay.txt`; estimate tau ~ M^4/(alpha^2 m_p^5), uncertain by O(1-10)):
- M12 = 1.1e13 GeV: tau ~ 8e23 yr, excluded (bound 2.4e34 yr)
- M13 = 1.8e14 GeV (best point): tau ~ 5e28 yr, excluded
- M23 = 3.0e16 GeV: tau ~ 5e37 yr, allowed
- minimal M_X for the bound with alpha^-1 = 42: ~4.7e15 GeV
- MSSM reference 1.3e16 GeV, alpha^-1 = 25.7: ~5e35 yr (d=6 only; d=5 is model dependent)

So the scale where the SM couplings come closest is also the one a unified gauge theory could not use. The 7.4-Higgs-doublet reweighting from 1.4 would unify at 10^13.7 GeV, also excluded. [established for the estimate]

---

## 5. Dead ends and open issues

- Dead: "antiparticle loops counted again / differently weighted" (sections 1.2-1.4). Not equivalent to the SM, empirically excluded (Delta alpha_lep, R-ratio, alpha_s running), and for fermions irrelevant to one-loop unification anyway.
- Dead: spectral-action boundary condition (section 3).
- Not done: 4-loop gauge terms (only QCD 4-loop -2472.28 term available as an option, effect < 1e-4 in g at M_Pl); b/tau Yukawas; electroweak 2-loop threshold at MZ for set B beyond the A vs B comparison. All are orders of magnitude below the gap. [established by the size of the 2-to-3-loop shift]
- Not done: non-perturbative SM contributions to running (instantons) scale as exp(-8 pi^2/g^2) = exp(-2 pi alpha^-1) ~ 1e-109 at alpha^-1 ~ 40, negligible. [established, standard estimate]
- Open in principle: gravitational corrections to gauge running near M_Pl are scheme-dependent and not part of the SM. Out of scope.

---

## 6. CONSTRAINTS checklist

- **A1 (SM only):** No new fields anywhere in a mechanism. MSSM used only as a numerical comparison (section 2.3). nu_R appearing in NCG/Furey constructions is explicitly excluded. Pass.
- **A2 (neutrino mass):** Not used. Neutrino Yukawas are < 1e-12 and do not affect gauge running at any shown digit; result insensitive to the mass mechanism. Pass.
- **A3 (reformulations):** Map stated (section 1.5): NCG after the KO-dim-6 projection and division-algebra models restricted to the SM sector reproduce SM reps, hence SM beta functions. Extra relations (spectral action boundary condition, U(1) normalisation choice, sigma, U(1)_X) are named and not used. Any result also holds in standard formulation. Pass.
- **B1-B8 (CPT tests):** The argument uses exact CPT; any mechanism weighting antiparticles differently would be excluded by B1-B6 and by the counting data. Pass.
- **C1-C2:** PDG-2024 m_H = 125.20, m_t = 172.57, MW = 80.369 used via sm_inputs.py. Pass.
- **C3 (LHC SUSY limits):** No superpartners; nothing to explain. MSSM reference uses M_SUSY = 1-3 TeV, roughly the range at the edge of current limits. Pass.
- **C4 (g-2):** Not used.
- **D (couplings):** PDG values used; runner in calc/ (own copy as instructed, not tools/), loop order stated everywhere. Pass.
- **E:** Not relevant except E3 (eta) noted as an in-medium effect that does not affect UV running.
- **F1/F2:** Section 4.
- **G:** Not relevant.
- **H1 (no numerology):** The k = 1.339 and w_S = 7.45 numbers are reported only to show what would be needed; neither is proposed as a mechanism. Pass.
- **H2 (regulator independence):** b_i, B_ij are scheme independent; B_ij and higher-loop coefficients are scheme dependent at 3 loops, but the conclusion (gap 3.2 vs 3-loop shift 0.03) holds in any mass-independent scheme; MS-bar vs DR-bar conversion only shifts alpha^-1 by C2/(12 pi) <= 0.08. Pass.
- **H3 (interpretations not mechanisms):** Section 1.2 shows Dirac-sea and Feynman-Stueckelberg give the identical bubble; nothing derived from them differs from standard QFT. Pass.
- **H4 (runnable scripts):** All numbers have scripts and saved outputs in calc/. Pass.
