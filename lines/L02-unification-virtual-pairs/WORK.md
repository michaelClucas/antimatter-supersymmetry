# L02-unification-virtual-pairs: WORK

Target: SUSY result #2 (gauge coupling unification). All numbers below come from scripts in `calc/` with saved outputs (`*.txt`). Run any of them with `python <script>.py` from inside `calc/`. Every script takes its SM inputs from `tools/sm_inputs.py` (PDG 2024, alpha_em^-1(MZ) = 127.930) via `calc/sm_path.py`. Exceptions, by design: `validate_rg.py` uses the 1307.3536 central inputs (that is what it validates against), `fs_residues.py` has no physical inputs, and `empirical_counting.py` uses alpha(0) = 1/137.035999 (CODATA), which `tools/sm_inputs.py` does not carry.

Tags: [established] = textbook or cited and checked; [derived here] = computed in this line, reproducible from `calc/`; [conjecture] = argued but not computed; [speculation] = not argued in detail.

| Script | Output | What it does |
|---|---|---|
| `rg_sm3.py` | (module) | SM RGEs at 1/2/3 loops (g1,g2,g3,yt,lambda), MSSM 1/2-loop gauge for comparison |
| `validate_rg.py` | `validate_rg.txt` | reproduces arXiv:1307.3536 eq. (61) Planck-scale couplings |
| `crosscheck_tools.py` | `crosscheck_tools.txt` | `rg_sm3.py` vs the shared `tools/rg_sm.py`, 1/2/3 loops |
| `unification.py` | `unification.txt`, `sm_3loop_alpha_inv.txt` | crossing scales, spread, thresholds, required alpha_s; MSSM reference |
| `counting.py` | `counting.txt` | state bookkeeping for b_i; uniform weight scan; antiquark/antilepton splits; 2-loop weighted runs |
| `reweighting.py` | `reweighting.txt` | every single-sector reweighting that could unify, with its empirical kill |
| `fs_residues.py` | `fs_residues.txt` | Feynman-Stueckelberg pole bookkeeping of a one-loop bubble, eps -> 0 convergence |
| `empirical_counting.py` | `empirical_counting.txt` | Delta alpha_lep and R-ratio with single vs double counting |
| `proton_decay.py` | `proton_decay.txt` | d=6 lifetime estimate at each crossing scale (scales computed live from `unification.py`) |
| `hypercharge_norm.py` | `hypercharge_norm.txt` | U(1) normalisation that would make alpha_1 hit M23 (convention check) |

---

## 1. Antiparticle counting in beta functions

### 1.1 The coefficients depend only on group, representations and multiplicities [established]

One-loop, for gauge group factor G_i (background-field method, any gauge, MS-bar or momentum subtraction):

b_i = -(11/3) C2(G_i) + (2/3) sum_{Weyl fermions} T_i(R) + (1/3) sum_{complex scalars} T_i(R)

(Gross-Wilczek PRL 30, 1343 (1973), DOI 10.1103/PhysRevLett.30.1343; Politzer PRL 30, 1346 (1973), DOI 10.1103/PhysRevLett.30.1346; two loops: Machacek-Vaughn NPB 222, 83 (1983), DOI 10.1016/0550-3213(83)90610-7.) Every input on the right is a group-theory datum of the field content. Two formulations with the same group, representations and multiplicities have identical b_i, identical two-loop coefficients, and identical higher-loop coefficients, since those are also built from Casimirs, Dynkin indices and Yukawa/quartic traces. So any reformulation equivalent to the SM (CONSTRAINTS A3.1) has the SM beta functions. [established]

### 1.2 Particle and antiparticle are already counted, once [established; reproduced]

A left-handed Weyl field psi in representation R creates a particle in R with helicity -1/2 and its antiparticle in R-bar with helicity +1/2. T(R-bar) = T(R), and Y flips sign, so Y^2 is unchanged. The 2/3 per Weyl field in b_i can be written as 1/3 per on-shell helicity state, particle and antiparticle each.

`counting.py` part 1 is **bookkeeping, not a verification**: it lists all 45 Weyl fields x {particle, antiparticle} plus H and H-bar, and applies 1/3 T(R) per fermionic state and 1/6 T(R) per scalar state. That rule is chosen so the sum gives b = (41/10, -19/6, -7), so the `assert` only checks the bookkeeping is internally consistent. What it does show: the antiparticle states are already half of every fermion and scalar contribution, so there is nothing missing to "add". The non-trivial facts printed are the particle-only sums over the 15 Weyl fields of a generation: Tr Y = 0 and Tr Y^3 = 0 (`counting.txt`). [established]

Feynman-Stueckelberg reading. The Feynman propagator has two poles, positive frequency (particle) and negative frequency (particle backward in time = antiparticle). `fs_residues.py` does the energy integral of a one-loop bubble by residues and gets exactly two time-ordered terms, 1/(q0 - E1 - E2) (pair produced by the external field) and -1/(q0 + E1 + E2) (Z-graph: pair from the vacuum first). The symbolic residue sum minus the two-ordering formula is exactly 0. Direct numerical integration at finite eps agrees with it up to a residual proportional to eps: 2.3e-3, 2.3e-4, 2.3e-5 at eps = 1e-2, 1e-3, 1e-4 for (q0, E1, E2) = (0.7, 1, 1.3), and 1.6e-2, 1.6e-3, 1.6e-4 for (1.5, 1, 1) (`fs_residues.txt`). So the agreement at eps = 1e-3 is ~1e-3, and it goes to 0 as eps -> 0. The two poles of one propagator exhaust the loop. Both time orderings contain one particle line and one antiparticle line, so neither ordering is "the antiparticle loop", and there is no separate antiparticle contribution that could be added. [established; check reproduced]

Wick-contraction reading. <T j^mu(x) j^nu(y)> with j = psi-bar gamma psi has exactly one connected contraction. For the two-point function the two orientations of the fermion loop are the same diagram. (For three-point loops the two orientations are distinct and both are summed.) [established]

Dirac-sea (hole theory) reading. Vacuum polarisation was first computed in hole theory with a filled sea and gave the same charge renormalisation and the same Uehling potential as later covariant QED (Heisenberg, Z. Phys. 90, 209 (1934), DOI 10.1007/BF01333516; Uehling, Phys. Rev. 48, 55 (1935), DOI 10.1103/PhysRev.48.55; Weisskopf, Kgl. Danske Vid. Selsk. Mat.-fys. Medd. 14, no. 6 (1936), no DOI, verified in LITCHECK). The sea's response to an external field is the pair-creation amplitude above; the hole is the antiparticle. Hole theory needs Heisenberg's charge-symmetrised current to remove the infinite sea charge; that subtraction is a constant and does not touch the q^2 dependence that drives running. [established] Hole theory has no version for bosons (no Pauli blocking), so W, gluon and Higgs loops have no sea reading (Weinberg, QFT Vol. I, ch. 1, DOI 10.1017/CBO9781139644167). [established]

### 1.3 Lorentz structure and CPT forbid an asymmetric contribution [established]

(Corrected: the earlier heading invoked C. C is maximally violated in the chiral SM and cannot be used to forbid anything in the electroweak sector. It holds only in the vector-like QCD x QED sector.)

The running of g_i comes from the gauge two-point function Pi^{mu nu}_{ab}(q). Lorentz covariance allows (q^2 g^{mu nu} - q^mu q^nu) Pi(q^2) and epsilon^{mu nu rho sigma} q_rho q_sigma; the latter vanishes identically by antisymmetry. CPT (exact; CONSTRAINTS A1, B1-B6) maps each particle state to an antiparticle state with the same mass and conjugate representation, with the same T(R) and Y^2, so the two halves of each loop are equal term by term at every order. The only place a particle-antiparticle asymmetry enters is a background with net charge density (chemical potential mu, or the cosmological baryon asymmetry eta ~ 6e-10). That changes in-medium polarisation at momenta q <~ mu, T and decouples from the UV running relevant here. [established]

### 1.4 Uniform reweightings (corrected statement) [established for the algebra; the weights are not SM]

Write b_i = w_V b_i^V + w_F b_i^F + w_S b_i^S, with b^V = (0, -22/3, -11) (gauge+ghost), b^F = (4, 4, 4) (three generations), b^S = (1/10, 1/6, 0) (Higgs). `counting.py` part 2 (sympy):

- One-loop unification condition (B-test, the ratio used by Giveon, Hall, Sarid, PLB 271, 138 (1991)): (b2 - b3)/(b1 - b2) must equal (A2 - A3)/(A1 - A2) at MZ = 0.7178. The ratio is 5(-w_S - 22 w_V)/(2(w_S - 110 w_V)), independent of w_F.
- **Correction (referee 1, finding 1).** The earlier text said fermion antimatter contributes zero to one-loop non-unification "under ANY weighting of antiparticle loops". That is false. It holds only for weights that are **uniform within each complete SU(5) multiplet** (5-bar = d^c + L, and 10 = Q + u^c + e^c) of each generation; the weights may differ between the 5-bar and the 10 and between generations. Counterexample printed in `counting.txt`: antiquark states only give Delta b = (11/30, 1/2, 2/3) per generation, antilepton states only give (3/10, 1/6, 0), neither proportional to (1,1,1). Non-uniform weights do move the B-ratio and are treated in 1.6. [established; Georgi-Quinn-Weinberg PRL 33, 451 (1974), DOI 10.1103/PhysRevLett.33.451, for the complete-multiplet fact]
- SM value 0.5275, MSSM value 0.7143, measured 0.7178.
- Needed: w_S = 7.45 (7-8 Higgs doublets; unification at 10^13.7 GeV, alpha^-1 = 38.6) or w_V = 0.134. The w_V solution satisfies the B-ratio only formally: with b = (4.10, 3.18, 2.52) the alpha_1 = alpha_2 meeting point sits at 10^89 GeV with negative alpha^-1, so it is not a unification at all (`reweighting.txt`). It also gives b_3 = +2.52 (6 flavours), +1.86 (5 flavours): QCD loses asymptotic freedom, alpha_s would fall toward low energy, alpha_s(m_tau) = 0.104 < alpha_s(MZ), against the measured alpha_s(m_tau) ~ 0.3. (`counting.txt`, `reweighting.txt`) [derived here]
- Two-loop gauge-only runs with uniform weights (`counting.txt` part 3), best-point spread in alpha^-1: SM 3.20; antifermion states twice (w_F = 3/2) 3.28; every fermion field twice (w_F = 2) 3.44; particles only (w_F = w_S = 1/2) 3.45; antifermion + anti-Higgs states twice 2.97. Only w_S = 7.45 gets down to 0.54. [derived here]

Empirical exclusion of double counting (`empirical_counting.py`) [established]:
- Leptonic running of alpha_em from 0 to MZ at one loop with each lepton counted once: 0.03142 (3-loop literature value 0.031498, Steinhauser PLB 429, 158 (1998), hep-ph/9803313). Counting antileptons again: 0.06284, which would put alpha^-1(MZ) near 124.6 instead of ~129 (on-shell).
- The hadronic running is extracted from data through the dispersion relation from sigma(e+e- -> hadrons) (Davier, Hoecker, Malaescu, Zhang, EPJC 80, 241 (2020), arXiv:1908.00921; Keshavarzi, Nomura, Teubner, PRD 101, 014029 (2020), arXiv:1911.00367). Unitarity ties the imaginary part of the bubble to the pair-production rate. R = N_c sum Q^2 (1 + alpha_s/pi) = 3.82 for five flavours, consistent with data in the 10-40 GeV region; double counting would predict 7.6. The final state q q-bar contains one particle and one antiparticle; the counting is measured, not interpreted.
- QCD with every quark field counted twice: b_3 = -11 + 8 = -3. With the unprojected NCG fourfold count (1.5): b_3 = -11 + 16 = +5, no asymptotic freedom. The +5 is this line's own extrapolation (4x the quark contribution), not a number from the NCG papers. [derived here, heuristic]

### 1.5 Reformulations

- **Connes-Chamseddine NCG / spectral action.** The almost-commutative spectral triple has fermion Hilbert space H_F containing f and f^c for each SM fermion. Taken naively in Euclidean signature the fermions are counted more than once (fermion doubling / quadrupling), identified by Lizzi, Mangano, Miele, Sparano, PRD 55, 6357 (1997), hep-th/9610035, who did not find an acceptable projection. The resolution is the KO-dimension-6 real structure with the physical-subspace / Pfaffian projection (Connes, JHEP 0611:081 (2006), hep-th/0608226; Barrett, J. Math. Phys. 48, 012303 (2007), hep-th/0608221). After that projection the fermion content is one copy of the SM (plus nu_R, which A1/A2 remove), and the beta functions are the SM ones. [established] Before the projection the theory is not equivalent to the SM; the b_3 = +5 above is a heuristic estimate of what an unprojected count would give, not computed in those papers [derived here, heuristic]. The doubling is uniform across complete generations and drops out of the one-loop B-test (1.4). [established]
- **Division algebras (Dixon; Furey).** Corrected citation (LITCHECK #15). Furey, "Charge quantization from a number operator", PLB 742, 195 (2015), DOI 10.1016/j.physletb.2015.01.023, arXiv:1603.04078 (verified this session): one generation of quarks and leptons built from a minimal left ideal of C (x) O via ladder operators, with electric charge given by a number operator divided by 3. Separately, Furey, EPJC 78, 375 (2018), arXiv:1806.00612: Cl(10) ladder operators from R (x) C (x) H (x) O give G_SM = SU(3)xSU(2)xU(1)/Z6 by not fully realising SU(5), with a possible extra U(1)_X. Restricted to the SM sector (no nu_R, no U(1)_X; A3.2), the representations and multiplicities are the SM's, so the b_i are the SM's. The ideal and its conjugate carry particle and antiparticle, the same two charge states as 1.2. [established that the reps match; equivalence of the full dynamics is not claimed in those papers, A3.3 caveat]
- **Hypercharge normalisation.** "Unification" of alpha_1 requires choosing alpha_1 = k alpha_Y. The SM does not fix k; k = 5/3 comes from SU(5)/SO(10) embedding (Baez-Huerta, Bull. AMS 47, 483 (2010), arXiv:0904.1556). `hypercharge_norm.py`: making alpha_1 pass through the alpha_2 = alpha_3 point at 10^16.47 GeV would need k = 1.339. Choosing k to force unification is a high-scale relation (A3.2) and numerology (H1). Not used. [derived here]

### 1.6 Classification of every reweighting that could unify, with its kill (`reweighting.py`)

**Reduction to species weights.** A vacuum-polarisation bubble always contains one particle and one antiparticle line (1.2). A weight x on "the antiparticle states" of species X can only mean the X loop counts (1+x)/2 times. So every antiparticle reweighting is a species reweighting with w = (1+x)/2. [derived here]

**Linearity.** The B-test condition L(w) = (b2 - b3) - R(b1 - b2) = 0 is linear in the weights, L(w) = sum_s w_s l_s. SM: L(1) = -1.383. The unifying weights form a hyperplane in weight space. The 5-bar and the 10 each have l = 0 exactly, so they never help. Every other direction does. [derived here]

**What a loop weight could mean physically.** The one-loop coefficient of species X is the asymptotic coefficient of the absorptive part of Pi_VV, which by the optical theorem is the pair-production rate V* -> X X-bar (the dispersion relation is how alpha_em running is actually measured). A weight w != 1 can be realised in three ways only:
1. as a multiplicity (extra copies of X): BSM, excluded by A1;
2. by rescaling X's gauge couplings: breaks charge universality and changes the measured rate;
3. as a bare weight on the loop with unchanged vertices: violates unitarity (Im Pi no longer equals the sum over final states), so it is not a QFT, let alone one equivalent to the SM.
In cases 2 and 3 the rate that unitarity ties to the loop is a measured quantity. That is the empirical kill below. [established for the optical theorem and dispersion relation; the case split is derived here]

**Single-sector results** (each sector reweighted alone, others = 1; all numbers from `reweighting.txt`):

| Sector | w needed | x (antiparticle-only form) | M_U (1-loop) | Kill |
|---|---|---|---|---|
| all fermions, uniform | none | none | - | l = 0 (GQW) |
| 5-bar or 10, uniform | none | none | - | l = 0 |
| **all antiquarks** (Q, u^c, d^c) | -2.25 | -5.49 | 10^10.1 | negative weight = negative rate; Gamma_had x(-2.25), R x(-2.25); alpha_s(MZ) from alpha_s(m_tau) -> 0.066 |
| **all antileptons** (L, e^c) | 4.25 | 7.49 | 10^10.1 | Gamma_ll x4.25, Gamma_inv x4.25 (N_nu = 12.7 vs 2.984 +- 0.008) |
| Q only | 1.46 | 1.92 | 10^15.4 | Gamma_had x1.42 (~370 sigma), R x1.23; alpha_s(MZ) -> 0.125 |
| Q, 3rd generation only | 2.38 | 3.76 | 10^15.4 | Gamma_had x1.29 (via b_L), ~260 sigma |
| u^c only | 0.36 | -0.29 | 10^14.8 | Gamma_had x0.96 (~30 sigma), R x0.77 |
| d^c only | -0.07 | -1.15 | 10^13.7 | negative weight; Gamma_had x0.98 (~20 sigma) |
| L only | 2.07 | 3.15 | 10^13.7 | N_nu = 6.2 vs 2.984 +- 0.008 (~600 sigma) |
| e^c only | -0.61 | -2.21 | 10^17.0 | negative weight; Gamma_ll x0.32 (~670 sigma) |
| gluon loops | 1.126 | 1.25 | 10^13.0 | alpha_s(MZ) evolved from fixed alpha_s(m_tau) -> 0.107 vs 0.1180 |
| all gauge loops (w_V) | 0.134 | - | 10^89, alpha^-1 < 0 | not a unification; b_3 = +1.86 (5 fl.): asymptotic freedom lost, alpha_s(m_tau) = 0.104 |
| W loops | 0.890 | 0.78 | 10^14.4 | no clean empirical kill; equivalence (below) |
| Higgs loops (w_S) | 7.45 | 13.9 | 10^13.7 | kappa_V = 2.73 if via couplings; VH rate x7.4 if via unitarity; multiplicity = BSM |

Z widths: ALEPH, DELPHI, L3, OPAL, SLD et al., Phys. Rept. 427, 257 (2006), hep-ex/0509008 (verified): Gamma_had = 1744.4 +- 2.0 MeV, Gamma_ll = 83.984 +- 0.086 MeV, Gamma_inv = 499.0 +- 1.5 MeV, N_nu = 2.9840 +- 0.0082, all in agreement with the SM counting. The script computes LO ratios to the SM, Gamma ~ N_c (w_L gL^2 + w_R gR^2); sigma counts use the experimental relative errors only, so they are order-of-magnitude [derived here]. The alpha_s shifts are one-loop with 5 active flavours, holding alpha_s(m_tau) fixed: Delta alpha_s^-1(MZ) = -Delta b3/(2 pi) ln(MZ/m_tau) [derived here, 1-loop estimate].

Notes on individual rows:
- **Antiquark-only weighting** (the referee's counterexample) needs x = -5.5: a negative loop weight. Through the optical theorem this is a negative e+e- -> hadrons cross section. Dead on unitarity alone, and on Gamma_had, R and alpha_s running. [derived here]
- **L and Higgs give the same b**, (4.74, -2.09, -7.00), because L and H have the same SU(2)xU(1) quantum numbers up to the sign of Y (2/3 per Weyl doublet vs 1/3 per complex-scalar doublet). This is the reason extra doublets (Higgs or lepton-like) are the standard non-SUSY unification fix (Willenbrock, hep-ph/0302168, PLB 561, 130 (2003)). [established]
- **Gluon loops.** Only a 12.6% overweight is needed. The kill is quantitative but modest: with alpha_s(m_tau) fixed, alpha_s(MZ) moves from 0.118 to 0.107. The PDG QCD review lists the tau-decay extraction of alpha_s(MZ) as consistent with the world average 0.1180 +- 0.0009 with an uncertainty of order 0.002 [uncertain on the exact figure, PDG 2024 QCD review], so this is a ~5 sigma exclusion at one loop. The scale 10^13.0 GeV would also be excluded by F1 if an X boson existed there (conditional, 5e23 yr). [derived here; the experimental error is [uncertain]]
- **w_V = 0.134**: see 1.4. It does not unify at a physical scale, and it kills asymptotic freedom. [derived here]
- **W loops (w_W = 0.89)**. Delta b2 = +0.80; from MZ to 1 TeV this shifts alpha_2^-1 by 0.31 (1.0%). I do not know of a measurement of SU(2) running above MZ at that precision and do not claim one. **No clean empirical kill.** The kill is equivalence: the gauge+ghost loop weight is fixed by BRST invariance (Slavnov-Taylor identities tie the gauge and ghost loops to the same vertices), and the vertices are the triple gauge couplings tested at LEP2 in e+e- -> W+W- (ALEPH, DELPHI, L3, OPAL and LEP EW WG, Phys. Rept. 532, 119 (2013), DOI 10.1016/j.physrep.2013.07.004, arXiv:1302.3415; arXiv ID and DOI verified this session, volume/page from memory). A weight on the loop with these vertices fixed is not a QFT. The scale 10^14.4 GeV would also be excluded by F1 (conditional). [conjecture for the precision statement; established for BRST]
- **Higgs loops (w_S = 7.45).** Direct effect on running from MZ to 1 TeV: Delta alpha_1^-1 = 0.25, Delta alpha_2^-1 = 0.41 (1.4%). No measurement used here tests that, so **there is no clean kill from running itself.** The kills come from what the weight would have to be: (i) a multiplicity of ~7 doublets is BSM (A1) and is exactly the known extra-doublet unification (Willenbrock 2003; arXiv:1709.02366); (ii) a rescaling of the doublet's gauge coupling by sqrt(7.45) = 2.73 would multiply the hWW and hZZ couplings (both ~ g^2 v) by the same factor, against kappa_W, kappa_Z = 1 at the 5-10% level (ATLAS, Nature 607, 52 (2022); CMS, Nature 607, 60 (2022); CONSTRAINTS C1); (iii) a bare loop weight violates unitarity, and by the Goldstone equivalence theorem (Cornwall, Levin, Tiktopoulos, PRD 10, 1145 (1974); Lee, Quigg, Thacker, PRD 16, 1519 (1977)) the absorptive part it would need is a 7.4x larger V* -> (W_L W_L, Z_L h, W_L h) rate at high energy, whereas the measured VH rates agree with the SM within their errors (same ATLAS/CMS papers). (iii) is an equivalence argument with data pinning the tree-level rate, not a direct measurement of the loop. [established for (i), (ii); (iii) conjecture-level as a quantitative statement, established as a unitarity argument]
- **Colour- or isospin-component-dependent weights** (weight red quarks only, or the upper component of a doublet only) break SU(3) or SU(2) invariance: different components of the gauge field would run differently, and there is no single g_3 or g_2 to unify. alpha_s measured in processes with different colour structure agrees (PDG QCD review). [established]
- **Scale-dependent weights** (a weight that switches on above some scale) are thresholds, i.e. new states. BSM by A1. [established]

**Bottom line of 1.6.** Every reweighting that changes the one-loop unification test is either (a) a negative weight, which violates unitarity outright, (b) a fermion-species weight, excluded by the Z-pole widths at 20-3000 sigma and in several cases by N_nu, (c) a gluon weight, excluded by alpha_s running (~5 sigma, 1-loop estimate), (d) w_V, which does not unify and kills asymptotic freedom, or (e) a W or Higgs weight, which has no clean kill from measured running and is excluded by equivalence (BRST, unitarity) with kappa_V and VH data pinning the couplings and rates. [derived here]

**Conclusion of section 1:** in any SM-equivalent bookkeeping, antimatter is already in the beta functions with weight fixed by the field content and by unitarity. Uniform antiparticle weights within complete SU(5) multiplets cannot touch one-loop unification; non-uniform ones can, and each such choice is excluded as listed above. [established / derived here as tagged]

---

## 2. Numerical running

### 2.1 Implementation and validation

`rg_sm3.py`: x = (g1^2, g2^2, g3^2, yt^2, lambda) vs ln mu^2, g1 GUT-normalised, V = lambda |H|^4. Gauge at 1/2/3 loops including yt and lambda at 3 loops; yt and lambda at the same loop order (3-loop terms numeric). Transcribed from Buttazzo et al., JHEP 1312, 089 (2013), arXiv:1307.3536, App. B eqs. (96)-(101). Cross-checked by hand against Mihaila-Salomon-Steinhauser, PRL 108, 151602 (2012), arXiv:1201.5868 eq. (5): b_i/4, B_ij/16, the yt^4 g1^4 3-loop coefficient 189/16, the lambda g1^6 coefficient 27/50, the g2^6 coefficient 324953/1728 and the g3^6 coefficient 65/2 all agree. b, tau and light Yukawas set to zero.

Validation (`validate_rg.txt`): with the 1307.3536 central inputs, 3-loop running to M_Pl = 1.2209e19 GeV gives g1 = 0.6154, g2 = 0.5055, g3 = 0.4873, yt = 0.3824, lambda = -0.0143 vs published 0.6154, 0.5055, 0.4873, 0.3825, -0.0143. [established: runner correct to 4 digits]

Cross-check against the shared runner (referee 1, finding 4; CONSTRAINTS D): `crosscheck_tools.py` runs `rg_sm3.py` and `tools/rg_sm.py` from the same PDG-2024 inputs. At 1, 2 and 3 loops, at mu = 1e10, 10^13.05, 10^14.25, 10^16.47 GeV and M_Pl, alpha_i^-1 agree to |Delta| <= 8.7e-6 (`crosscheck_tools.txt`). The b/tau Yukawas that `tools/rg_sm.py` keeps have no visible effect. So every number below would be the same with the `tools/` runner. [derived here]

Inputs:
- Set A: NNLO-matched MS-bar couplings at mu = Mt from 1307.3536 eqs. (55), (57)-(60) with PDG-2024 Mt = 172.57, Mh = 125.20, alpha_s = 0.1180, MW = 80.369 (`tools/sm_inputs.py`). alpha^-1(Mt) = 58.689, 29.960, 9.256; yt = 0.9329; lambda = 0.1262. Set A does not use alpha_em(MZ), so it is unchanged by the 127.951 -> 127.930 update.
- Set B: PDG MS-bar alpha_s = 0.1180, alpha_em^-1 = 127.930 (corrected from 127.951), sin^2 theta_W = 0.23129 at MZ, run directly in the 6-flavour SM. alpha^-1(MZ) = 59.005, 29.589, 8.475. Caveat: these are 5-flavour quantities; running them in the full SM from MZ is a scheme mismatch. The A vs B difference measures it.

### 2.2 SM results (`unification.txt`, regenerated with tools/sm_inputs.py) [derived here; matches standard literature]

| | M12 (GeV) | a^-1 | M13 | a^-1 | M23 | a^-1 | best spread (at) | a3^-1 - a12^-1 at M12 |
|---|---|---|---|---|---|---|---|---|
| A 1-loop | 10^13.03 | 42.48 | 10^14.39 | 40.43 | 10^16.97 | 47.06 | 3.63 (10^14.39) | -5.55 |
| A 2-loop | 10^13.05 | 42.28 | 10^14.25 | 40.46 | 10^16.47 | 46.21 | 3.19 (10^14.25) | -4.91 |
| A 3-loop | 10^13.05 | 42.27 | 10^14.25 | 40.46 | 10^16.47 | 46.19 | 3.18 (10^14.24) | -4.90 |
| B 1-loop | 10^13.01 | 42.41 | 10^14.38 | 40.34 | 10^16.99 | 47.03 | 3.67 | -5.60 |
| B 2-loop | 10^13.03 | 42.19 | 10^14.23 | 40.38 | 10^16.46 | 46.14 | 3.20 | -4.92 |
| B 3-loop | 10^13.03 | 42.19 | 10^14.23 | 40.37 | 10^16.46 | 46.12 | 3.19 | -4.90 |

- Best spread = min over mu > 1e10 GeV of max_i alpha_i^-1 - min_i alpha_i^-1. It sits at M13. Relative spread 7.7% at 2-3 loops.
- Minimal threshold correction: alpha_3^-1 must be shifted by +4.9 (11.6% of alpha_12^-1) at M12. Any such threshold needs heavy states, not in the SM.
- alpha_s(MZ) that would give exact unification (set B): 0.0711 (1-loop), 0.0739 (2-loop), 0.0739 (3-loop), versus 0.1180 +- 0.0009 measured: about 49 sigma. This is how Amaldi et al. and Langacker-Luo (1991) phrased the SM failure.
- alpha_s +- 1 sigma (A, 3-loop): spread 3.14 to 3.22, M23 10^16.42 to 10^16.51.
- 3-loop vs 2-loop: shifts <= 0.03 in alpha^-1 and <= 0.01 decades. A vs B: <= 0.09 in alpha^-1, <= 0.02 decades. Both negligible against the 3.2 gap.

### 2.3 MSSM reference (comparison only; superpartners are not in any mechanism here)

SM below a common M_SUSY, MSSM above (b = (33/5, 1, -3), B_ij standard, tan beta = 10, MS-bar to DR-bar conversion at M_SUSY at 2 loops). Single common threshold is a simplification.

| M_SUSY | loops | set | best spread | at | a^-1 | alpha_s needed (set B) |
|---|---|---|---|---|---|---|
| 1 TeV | 1 | A | 0.33 | 10^16.17 | 25.80 | 0.1100 |
| 1 TeV | 2 | A | 0.12 | 10^16.15 | 25.21 | 0.1206 |
| 2 TeV | 1 | A | 0.42 | 10^16.12 | 26.22 | 0.1082 |
| 2 TeV | 2 | A | 0.02 | 10^16.10 | 25.66 | 0.1183 |
| 3 TeV | 1 | A | 0.47 | 10^16.10 | 26.46 | 0.1072 |
| 3 TeV | 2 | A | 0.03 | 10^16.07 | 25.92 | 0.1170 |

(Set B spreads, for reference: 1 TeV 0.36 / 0.10, 2 TeV 0.45 / 0.01, 3 TeV 0.50 / 0.04 at 1 / 2 loops.) A common M_SUSY = 1 TeV is already excluded for coloured sparticles by CONSTRAINTS C3 (gluino ~2.2-2.4 TeV, first/second-generation squarks ~1.8-1.9 TeV). The 2-3 TeV rows are the relevant reference; the 1 TeV row is kept only to show the trend. Consistent with CONSTRAINTS D (~2e16 GeV, alpha_GUT^-1 ~ 24-26). The SM gap (3.2) is 30-150 times the MSSM 2-loop gap. [derived here; established reference]

---

## 3. Spectral action boundary condition

- The Chamseddine-Connes-Marcolli spectral action gives g3^2 = g2^2 = (5/3) g1^2 at the cutoff Lambda (Chamseddine, Connes, Marcolli, Adv. Theor. Math. Phys. 11, 991 (2007), hep-th/0610241). [established]
- Not allowed here: it is an extra high-scale relation the SM does not contain (CONSTRAINTS A3.2). The CCM model also includes right-handed neutrinos with Majorana masses (A1, A2). [established]
- Even if allowed as an input, it is a condition, not a mechanism. Section 2 shows there is no Lambda where it holds: the best is the 10^14.24 GeV point with a 3.18 spread, or two of three equalities at M23 = 10^16.47 GeV with alpha_1^-1 = 37.10 vs 46.19. [derived here] CCM themselves state the couplings "do not meet exactly" (hep-th/0610241 Sec. 5.1, checked in LITCHECK) and use Lambda ~ 1e17 GeV, treating the mismatch as an uncertainty. [established]
- Prediction failures: CCM predicted m_H ~ 170 GeV (hep-th/0610241), excluded at 95% CL by the 2008 Tevatron combination (CDF and D0, arXiv:0808.0534) and in conflict with m_H = 125.20 GeV. The repair (Chamseddine-Connes, JHEP 1209, 104 (2012), arXiv:1208.1030) adds a real scalar sigma, forbidden by A3.2. Pati-Salam spectral models (Chamseddine, Connes, van Suijlekom, JHEP 1311, 132 (2013), arXiv:1304.8050) add new fields. [established]

---

## 4. Proton decay (CONSTRAINTS F1)

In the SM-only setting no scale "emerges". There is no X boson, and B is violated only by sphalerons/instantons (F2), with zero-temperature rate ~1e-165. The crossing points are just where curves cross. [established]

If a gauge-mediated d=6 operator were placed at a crossing scale (`proton_decay.txt`, scales now computed live from `unification.py`; estimate tau ~ M^4/(alpha^2 m_p^5), uncertain by O(1-10)):
- M12 = 1.1e13 GeV: tau ~ 8e23 yr, excluded (bound 2.4e34 yr)
- M13 = 1.8e14 GeV (best point): tau ~ 5e28 yr, excluded
- M23 = 2.9e16 GeV: tau ~ 5e37 yr, allowed
- minimal M_X for the bound with alpha^-1 = 42: ~4.7e15 GeV
- MSSM reference 1.25e16 GeV, alpha^-1 = 25.7: ~5e35 yr (d=6 only; d=5 is model dependent)

The single-sector reweightings of 1.6 unify at 10^10.1-10^15.4 GeV in every row except e^c-only (10^17.0, but negative weight); all of those would be excluded by F1 if an X boson existed (`reweighting.txt`). This kill is conditional and secondary. [derived here, estimate]

---

## 5. Dead ends and open issues

- Dead: "antiparticle loops counted again / differently weighted" (1.2-1.6). Not equivalent to the SM; uniform weights are irrelevant to one-loop unification; non-uniform weights excluded as listed in 1.6.
- Dead: spectral-action boundary condition (section 3).
- Not done: 4-loop gauge terms beyond the pure-QCD term; b/tau Yukawas in `rg_sm3.py` (shown irrelevant by `crosscheck_tools.py`); full electroweak 2-loop threshold at MZ for set B beyond the A vs B comparison. All far below the gap. [established by the size of the 2-to-3-loop shift]
- Not done: a two-loop version of the 1.6 table, and a proper fit (instead of the one-loop m_tau -> MZ estimate) for the gluon-weight kill. The gluon row is the only kill that depends on a rough one-loop estimate. [open]
- Not done: non-perturbative SM contributions to running scale as exp(-2 pi alpha^-1) ~ 1e-109 at alpha^-1 ~ 40, negligible. [established, standard estimate]
- Out of scope: gravitational corrections to gauge running near M_Pl.

---

## 6. Response to referee 1

1. **"ANY weighting" false (major).** Agreed. Corrected in PROPOSAL item 2 and WORK 1.4 to "uniform within each complete SU(5) multiplet (5-bar, 10) of each generation". `counting.py` now prints the antiquark-only Delta b = (11/30, 1/2, 2/3) and antilepton-only (3/10, 1/6, 0) per generation. New `reweighting.py` and WORK 1.6 classify every single-sector reweighting and give the kill for each. I extended the referee's point slightly: uniformity within the 5-bar and within the 10 separately is enough (each has l = 0), so the 5-bar and 10 weights may differ.
2. **w_V, w_S not empirically killed.** Agreed. w_V: b_3 = +2.52 (6 fl.), +1.86 (5 fl.), asymptotic freedom lost, alpha_s(m_tau) = 0.104 < alpha_s(MZ) (`counting.txt`, `reweighting.txt`). New finding while doing this: the w_V solution only satisfies the B-ratio formally, its meeting point is at 10^89 GeV with negative alpha^-1, so the earlier claim that w_V = 0.134 "would unify" was itself wrong. w_S: no clean kill from measured running (the 1.4% shift in alpha_2^-1 up to 1 TeV is not tested by anything used here). Kills: multiplicity is BSM; coupling rescaling gives kappa_V = 2.73 vs 1; a bare weight violates unitarity and would need a 7.4x VH/longitudinal-VV rate. The Slavnov-Taylor sentence was replaced by this argument.
3. **Stale unification.txt.** Agreed. Regenerated from `tools/sm_inputs.py`. First line now `59.005 29.589 8.475`. Set-B rows, the MSSM set-B spreads, and required alpha_s 0.0739 updated in 2.1-2.3. No conclusion changed.
4. **tools/ runner.** Agreed. `crosscheck_tools.py` compares with `tools/rg_sm.py` at 1/2/3 loops: max |Delta alpha^-1| = 8.7e-6. The "own copy as instructed" sentence is removed.
5. **fs_residues: 1e-5 claim and Z-graph framing.** Agreed on both. The script now runs eps = 1e-2, 1e-3, 1e-4 and shows the residual scales with eps (2.3e-4 and 1.6e-3 at eps = 1e-3). The "Z-graph twice = adding the antiparticle loop" line is removed; the text says both orderings contain one particle and one antiparticle.
6. **Tautological assert.** Agreed. Part 1 relabelled as bookkeeping; the script prints the particle-only Tr Y = 0 and Tr Y^3 = 0 over the 15 Weyl fields.
7. **C in the chiral SM.** Agreed. 1.3 now uses Lorentz structure plus CPT; C restricted to the vector-like sector.
8. **Furey citation.** Agreed. Fixed per LITCHECK #15 and verified 1603.04078 = PLB 742, 195 (2015) this session.
9. **b_3 = +5 tag.** Agreed. Retagged [derived here, heuristic]; NCG papers cited only for the doubling and its resolution (Lizzi et al. not cited as a resolution).
10. **M_SUSY = 1 TeV.** Agreed. 2.3 states 1 TeV is excluded for coloured states by C3; 2-3 TeV is the reference.
11. **H2 contradiction.** Agreed. Rewritten in the checklist.
12. **Missing checklist items.** Agreed. Section 8 covers every item ID.

Disagreements: none on substance. One partial: on finding 2 the referee suggests the w_S kill could be stated as "excluded only by definition". I give more than that (kappa_V and the unitarity link to VH rates), but I agree that no measured running excludes w_S directly, and say so in 1.6.

LITCHECK items: Furey fixed (#15); [unverified] removed from Weisskopf and 1304.8050 (#6, #22); Barrett "four times" quote removed and replaced by a paraphrase (#12); Lizzi et al. cited only for identifying the doubling (#13); CCM Sec. 5.1 treatment now stated as checked (#19); Amaldi et al., Langacker-Luo, Giveon-Hall-Sarid and Willenbrock now cited where the corresponding facts are used.

---

## 7. What is new (ruling R5)

Comparison with the literature, item by item:
- **SM non-unification and the required alpha_s ~ 0.07.** Amaldi, de Boer, Fuerstenau, PLB 260, 447 (1991); Langacker, Luo, PRD 44, 817 (1991). My 3-loop numbers with PDG-2024 inputs are an update of their inputs, not of their conclusion. The 3-loop SM running itself is in Buttazzo et al. 1307.3536, which my runner reproduces. **Not new.**
- **Complete multiplets drop out of the one-loop test.** Georgi, Quinn, Weinberg, PRL 33, 451 (1974); B-test form in Giveon, Hall, Sarid (1991). **Not new.**
- **Extra Higgs doublets (~6-7) unify the SM couplings, at a scale with fast proton decay.** Willenbrock, hep-ph/0302168; arXiv:1709.02366. My w_S = 7.45 at 10^13.7 GeV is the one-loop version. **Not new.**
- **One field = particle + antiparticle; hole theory = covariant QED; NCG doubling and its projection.** Textbook and Heisenberg/Weisskopf/Uehling; Lizzi et al. 1997, Connes 2006, Barrett 2007. **Not new.**
- **The classification of antiparticle reweightings (1.6).** No paper proposes that antiparticle loops change SM running (LITCHECK found none), so there is nothing in print to compare against. The pieces I use are standard: the reduction of antiparticle weights to species weights is the optical theorem; the kills are the LEP Z-pole widths, N_nu, alpha_s running and kappa_V. What is new is only the assembly for this question: (a) the observation that the unifying weights form a hyperplane and which single-sector directions reach it (e.g. a 12.6% gluon-loop overweight, a 46% Q-loop overweight, an x = -5.5 antiquark weight); (b) the explicit kill for each, including that the w_V direction does not unify at all; (c) the honest statement that for W-loop and Higgs-loop weights no measured running excludes them and the kill is equivalence plus coupling/rate data.

**Verdict.** The classification-with-kills in 1.6 is the only piece not found in the literature, and it is new only in the weak sense that nobody needed to write it down: every ingredient is standard and the conclusion (SM-equivalent counting fixes the weights) was never in doubt. It is a consistency check that answers this project's question, not a publishable result. Under R5 I recommend this line be folded into the planned synthesis S1 as its gauge-unification chapter (or scrapped as a negative result with `reweighting.py`, the validated runner and `crosscheck_tools.py` marked salvageable), rather than taken through the verification gate on its own.

---

## 8. CONSTRAINTS checklist (every item)

- **A1 (SM only):** No new fields in any mechanism. MSSM only as a numerical comparison (2.3). Extra doublets appear only as the thing a w_S weight would have to be, and are rejected for that reason. nu_R in NCG/Furey constructions excluded. Pass.
- **A2 (neutrino mass):** Not used. Neutrino Yukawas < 1e-12 do not affect gauge running at any shown digit; result insensitive to the mass mechanism. N_nu = 2.984 is used only as a count of light Z decay channels, independent of the mass mechanism. Pass.
- **A3 (reformulations):** Map stated (1.5): NCG after the KO-dim-6 projection, and division-algebra models restricted to the SM sector, reproduce SM reps, hence SM beta functions. Extra relations (spectral-action boundary condition, U(1) normalisation choice, sigma, U(1)_X) named and not used. Every result also holds in the standard formulation. Pass.
- **B1 (K0 mass difference):** CPT input to 1.3; any particle/antiparticle-dependent weight that showed up as a mass or self-energy difference is excluded at 6e-19. Pass.
- **B2 (pbar q/m):** Used only through CPT (1.3). Pass.
- **B3 (pbar magnetic moment):** As B2. Pass.
- **B4 (antihydrogen 1S-2S):** Antihydrogen spectroscopy includes the Uehling (vacuum polarisation) shift; agreement with hydrogen at 2e-12 is consistent with identical loop counting for matter and antimatter. Pass.
- **B5 (ALPHA-g):** Not relevant to gauge running. Pass.
- **B6 (e+/e- g-factor):** The anomalous moment includes vacuum polarisation; equality supports CPT-symmetric counting. Pass.
- **B7 (electron EDM):** Not relevant; no CP-violating mechanism proposed. Pass.
- **B8 (Jarlskog):** CKM CP violation enters gauge beta functions only through Yukawa traces at 2+ loops, and those traces are CP-even. No effect. Pass.
- **B9 (baryon CP violation, LHCb 2025):** Same as B8: CKM-sized CP violation, not in the CP-even beta-function traces. Not relevant. Pass.
- **B10 (neutron EDM, theta-bar):** The theta term is a total derivative and does not enter perturbative running; instanton effects are ~1e-109 (section 5). Not relevant. Pass.
- **C1 (Higgs):** m_H = 125.20 used via `tools/sm_inputs.py`; kappa_V at 5-10% used as a kill for w_S (1.6). Pass.
- **C2 (EW and top inputs):** m_t = 172.57, MW = 80.369, MZ = 91.1876 via `tools/sm_inputs.py`. Pass.
- **C3 (LHC SUSY limits):** No superpartners in any mechanism; the line reproduces nothing SUSY-specific, so absence of SUSY signals is automatically consistent. The MSSM comparison notes that M_SUSY = 1 TeV is excluded for coloured states; 2-3 TeV used as reference. Pass.
- **C4 (muon g-2):** Not used; no claim to explain it. Pass.
- **D (couplings at MZ):** PDG 2024 values from `tools/sm_inputs.py` (alpha_em^-1 = 127.930). Runner cross-checked against `tools/rg_sm.py` to 8.7e-6 in alpha^-1. Loop order stated everywhere. The CPT reference fact in D is the starting point of 1.2-1.3. Pass.
- **E1 (Omega_c h^2):** Not relevant (no dark matter claim). Pass.
- **E2 (Omega_b h^2):** Not relevant. Pass.
- **E3 (eta):** Only as an in-medium effect decoupled from UV running (1.3). Pass.
- **E4 (rho_Lambda):** Not relevant. Pass.
- **E5 (DM properties):** Not relevant. Pass.
- **E6 (N_eff):** Not relevant (N_nu from the Z width is used instead, 1.6). Pass.
- **E7 (sum m_nu, cosmology):** Not relevant. Pass.
- **E8 (KATRIN):** Not relevant. Pass.
- **E9 (symmetric cosmologies, annihilation limits):** No antimatter domains or symmetric cosmology used. Pass.
- **E10 (SM baryogenesis):** No baryogenesis claim. Pass.
- **F1 (p -> e+ pi0):** Section 4 and the conditional column in `reweighting.txt`. Pass.
- **F2 (SM B+L violation):** Section 4: only sphalerons/instantons, no X boson. Pass.
- **F3 (n-nbar):** Delta B = 2 needs a d=9 operator; nothing here generates one, and the SM has none at the perturbative level. Not relevant. Pass.
- **G (hierarchy, vacuum energy facts):** Not used; this line is about gauge running only. Pass.
- **H1 (no numerology):** k = 1.339, w_S = 7.45 and all 1.6 weights are reported as what would be needed, then excluded. None is proposed as a mechanism. Pass.
- **H2 (regulator independence):** b_i and the two-loop gauge coefficients are universal in mass-independent schemes; three-loop coefficients are scheme dependent. The conclusion (gap 3.2 vs 3-loop shift 0.03) holds in any mass-independent scheme; MS-bar vs DR-bar conversion shifts alpha^-1 by C2/(12 pi) <= 0.08. The 1.6 argument uses one-loop coefficients and the optical theorem, both scheme independent. Pass.
- **H3 (interpretations not mechanisms):** 1.2 shows Dirac-sea and Feynman-Stueckelberg give the identical bubble; nothing derived from them differs from standard QFT. Pass.
- **H4 (runnable scripts):** All numbers have scripts and saved outputs in `calc/`, all rerun from inside `calc/` in this round. Pass.
