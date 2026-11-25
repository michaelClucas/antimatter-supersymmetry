# L01 WORK - Weisskopf mechanism vs the Higgs hierarchy

All numbers below come from scripts in `calc/` (outputs in the matching `*_out.txt`). Units: natural, Heaviside-Lorentz, e^2 = 4 pi alpha.

## Claim

**The Weisskopf mechanism does not extend to the Higgs. No SM antiparticle structure cancels or softens the quadratic divergence of m_h^2.** In the top loop every time ordering contributes with the same sign at every loop momentum. The Weisskopf cancellation needs two things: the protected particle must be a fermion from the same field as the Dirac sea, so Pauli blocking applies, and its mass must break a chiral symmetry. The Higgs meets neither condition. The only SM cancellation is the Veltman condition, a sum over W, Z, h and top loops that involves no antimatter. With measured inputs and 3-loop running it is not satisfied below about 10^22.8 GeV. SM radiative EWSB also fails. [established for each component. The overall framing as a negative result for this project is the line's conclusion.]

---

## 1. Weisskopf cancellation reproduced (`calc/weisskopf_ofpt.py`)

Setup: electron at rest, spin-averaged, Coulomb gauge, sharp cutoff K on the photon 3-momentum, time-ordered perturbation theory, Dirac Hamiltonian H(p) = alpha.p + beta m, projectors Lam_pm(p) = (1 pm H(p)/E)/2. Integrands are d(delta m)/dk.

| piece | meaning | integrand | k -> inf |
|---|---|---|---|
| C1 | Coulomb self-energy, one-electron theory | alpha/pi | **+alpha/pi** (linear) |
| Cs | Coulomb exchange with the filled sea | alpha m/(pi E) - alpha/pi | **-alpha/pi** |
| Ta | transverse, intermediate state e(-k)+gamma (electron only) | see output | **-alpha/(2pi)** |
| Tb | transverse, vacuum pair e(0,s) ebar(-k) gamma, Pauli-blocked by the electron that is present, so removed from the vacuum energy | see output | **+alpha/(2pi)** |
| Tneg | (comparison) one-electron Dirac theory with no sea: electron jumps into negative-energy states | grows like alpha k/(pi m) | quadratic divergence |

Results [established, reproduced]:
- One-electron (no-pair) theory: C1 + Ta = alpha K/(2 pi). Linear divergence.
- Hole theory: C1 + Cs has linear coefficient 0, and Ta + Tb has linear coefficient 0. Each sector cancels separately.
- Total hole-theory integrand = alpha m (2k + E)/(pi (k^2 + kE + m^2)) -> (3 alpha m/2pi)/k. So delta m = (3 alpha/2 pi) m [ln(K/m) + c]. Numerically c = 0.5265 = ln 2 - 1/6 to the printed precision. That gives delta m = (3 alpha/2pi) m [ln(2K/m) - 1/6] for this cutoff [the closed form is a numerical identification. Weisskopf's own constant is not checked here, and the constant is cutoff-scheme dependent anyway].
- No-sea Dirac theory with negative-energy intermediate states (Tneg) diverges quadratically. This is the 1934 Weisskopf result before Furry's correction [established historically. Citation: Weisskopf, Z. Phys. 89, 27 (1934) and erratum Z. Phys. 90, 817 (1934), unverified citation details].
- **Chiral-symmetry check:** at m = 0 the hole-theory integrand vanishes identically, in both the Coulomb and the transverse sector. The one-electron theory integrand (C1+Ta) does not (alpha/2pi at m=0). So delta m is proportional to m only once the sea is included.

What does the cancelling: the Pauli-blocked vacuum-pair term (Tb) and the sea-exchange Coulomb term (Cs). Both exist only because the external electron and the sea electrons are the same fermion field and obey exclusion.

## 2. Modern reading, and the Higgs top loop in the same decomposition

### 2a. Electron [established]
In covariant QFT the two time orderings Ta and Tb are the two pieces of the single Feynman diagram after the k0 integral. The pair term is the Z-graph. The log, rather than linear, divergence is guaranteed by chiral symmetry. At m = 0 the QED Lagrangian is invariant under psi -> exp(i theta gamma5) psi, so delta m must be proportional to m, and by dimensional analysis it can then only be m ln(K/m). 't Hooft's technical-naturalness criterion makes this precise: 't Hooft, NATO Sci. Ser. B 59, 135 (1980) [unverified citation details]. In covariant language nothing antiparticle-specific remains. The hole-theory split into "electron" and "pair" pieces is noncovariant bookkeeping, and the sum is fixed by the symmetry.

### 2b. Higgs self-energy from the top loop (`calc/higgs_top_ofpt.py`)
H_int = (y/sqrt2) h tbar t, N_c = 3, Higgs at rest, cutoff K on the top 3-momentum.

Time-ordered pieces of d(delta m_h^2)/dp:
- F (forward, h -> t tbar -> h): 3 y^2 p^4 / [2 pi^2 (p^2+m^2)(m_h - 2E)]
- B (backward, Z-graph: vacuum -> h' t tbar, then t tbar h -> 0): -3 y^2 p^4 / [2 pi^2 (p^2+m^2)(m_h + 2E)]

Facts [established, reproduced]:
1. There is **no top-free intermediate state**. Both orderings contain a t tbar pair. In hole language both are excitations of the filled top Dirac sea: a sea top is lifted to positive energy. The quadratic divergence is therefore produced entirely by the top sea (vacuum polarization). For the Higgs, antimatter is the source of the divergence and cancels nothing.
2. There is **no Pauli blocking**: no top is present in the external state.
3. Since m_h < 2 m_t, **F < 0 and B < 0 at every p**. Both are negative-definite pointwise, so no cancellation among top-loop orderings is possible. Large p: each contributes -3y^2 p/(4pi^2), and they add.
4. F + B was checked against the covariant Feynman integrand with k0 integrated numerically (Wick rotation) at p = 0.1 ... 10 m_t. They agree to 8 digits, so the decomposition is exact and complete.
5. At m_t = 0 the quadratic piece persists. No symmetry of the SM forces delta m_h^2 proportional to m_h^2. A scalar mass term |H|^2 is invariant under every SM symmetry, so there is no chiral-symmetry analogue.
6. With a 3-momentum cutoff, delta m_h^2 = -(3 y^2/4pi^2) K^2 + (3 y^2/8pi^2)(6 m_t^2 - m_h^2) ln K + ... . With a 4D Euclidean cutoff, -(3y^2/8pi^2) Lambda^2. The factor 2 shows that quadratic-divergence coefficients are regulator dependent (CONSTRAINTS H2).

### 2c. Veltman coefficient: normalization fixed (`calc/veltman_running.py`)
Convention: V = -(m^2/2)|H|^2 + lambda|H|^4, m_h^2 = 2 lambda v^2 (the Buttazzo et al. convention), 4D Euclidean cutoff Lambda, Landau gauge. The Lambda^2 term of the one-loop effective potential is (Lambda^2/32pi^2) STr M^2(phi). sympy gives:

  **delta m_h^2 = C Lambda^2/(16 pi^2),  C = 6 lambda + (9/4) g^2 + (3/4) g'^2 - 6 y_t^2 [- 6 y_b^2 - 2 y_tau^2] = (3/v^2)(m_h^2 + 2 M_W^2 + M_Z^2 - 4 m_t^2)**

The prefactor is 3/(16 pi^2 v^2), not the 3/(8 pi^2 v^2) that is often quoted. Only the zero of C is convention independent [established; this matches Masina-Quiros eq. 12 and Jegerlehner's C1 = 2C with his lambda normalization].

Measured pole masses (PDG 2024, `tools/sm_inputs.py`): bracket = -82213 GeV^2, **C = -4.07**. MS-bar at mu = M_t: C = -3.43. Top dominance: C = 0 at these masses would need m_t = 96.1 GeV, or m_h = 312.9 GeV.

## 3. Running the Veltman coefficient (`calc/rg_sm.py`, copy in `tools/rg_sm.py`; `calc/veltman_running.py`)

RG runner: MS-bar beta functions transcribed from Buttazzo, Degrassi, Giardino, Giudice, Sala, Salvio, Strumia, JHEP 1312, 089 (2013), arXiv:1307.3536, Appendix B, eqs. (96)-(103). Loop orders: **3 loops for g1, g2, g3, y_t, lambda, m^2** (plus the 4-loop pure-QCD term in g3, used only when nloops=4); 2 loops for y_b, y_tau. Initial conditions are their NNLO matching fits, eqs. (55)-(60), at mu = M_t with PDG 2024 inputs. The source PDF was read directly to transcribe the formulas.

Validation against their eq. (61) at M_Pl (their inputs): 3-loop gives g1 = 0.6154, g2 = 0.5055, g3 = 0.4873, y_t = 0.3825, lambda = -0.0144. Their values are 0.6154, 0.5055, 0.4873, 0.3825, -0.0143. [established: runner validated]. One open discrepancy: their m(M_Pl) = 129.4 GeV, while this runner gives 139.4 GeV. It does not affect anything here, but it should be resolved before anyone uses m^2 from this runner.

Results with PDG 2024 central inputs (M_t = 172.57, M_h = 125.20, alpha_s = 0.1180):

| mu (GeV) | C |
|---|---|
| M_t | -3.42 |
| 10^10 | -0.84 |
| 10^16 | -0.35 |
| M_Pl = 1.22e19 | -0.18 |
| 10^22 | -0.04 |
| 10^25 | +0.10 |

Zero of C: **log10(mu0/GeV) = 22.83 (3-loop)**, 22.98 (2-loop), 26.8 (1-loop). Parametric dependence (3-loop): M_t +/- 0.29 GeV moves it by +/-0.35 decades, alpha_s +/- 0.0009 by -/+0.5, M_h +/- 0.33 by about 0.1. Putting the zero at M_Pl needs y_t(M_t) lower by 0.0175, about M_t ≈ 169.4 GeV, which is 11 sigma below PDG. For reference, lambda = 0 at 10^10.66 GeV.

Literature check:
- Hamada, Kawai, Oda, PRD 87, 053009 (2013), arXiv:1210.2538: the bare Higgs mass (1+2-loop quadratic divergences) vanishes at about 10^23 GeV for M_t = 173 GeV, and near M_Pl only for M_t ≈ 170 GeV. **Agrees with this line**: 10^23.5 at M_t = 173.34. [established, abstract verified]
- Masina, Quiros, arXiv:1308.1242: the Veltman condition is met "around Planckian scales", "slightly trans-Planckian" for central values [established, text verified; journal ref PRD 88, 093003 (2013) unverified].
- Jegerlehner, arXiv:1305.6652: zero at mu0 ≈ 7×10^16 GeV, with y_t(M_Pl) ≈ 0.355. **Reproduced and explained:** lowering y_t(M_t) by 0.0286 (to 0.904, roughly a 5 GeV lower M_t) gives the zero at 7e16 and y_t(M_Pl) = 0.356. The early zero comes from his lower top-Yukawa matching. Current NNLO matching (y_t(M_Pl) = 0.3825) does not support it. [established numerically here; Jegerlehner's journal ref (Acta Phys. Polon. B 45, 1167 (2014)) unverified]

Verdict on item 3: "C ≈ 0 near M_Pl" holds only approximately. With 3-loop running and current inputs C(M_Pl) = -0.18, about 5% of its EW value, and the zero is 3.7 decades above M_Pl. Calling that "satisfied at the Planck scale" requires m_t about 3 GeV low or a tolerance for |C| of about 0.2. [established numbers; any interpretation as a UV boundary condition is speculation and outside SM scope].

## 4. Is anything here antimatter? (rigorous negative)

**No.** [conjecture-level as a general claim, but each step below is established]

1. In the electron case the cancellation is Lorentz covariance plus chiral symmetry. The hole-theory split is a noncovariant bookkeeping of one Feynman diagram. The antiparticle is required by the Dirac field, but the output (delta m proportional to m) is fixed by the chiral symmetry. In Feynman-Stueckelberg language Tb is just the backward time ordering. CONSTRAINTS H3 applies: the interpretation adds no physics.
2. The specific cancelling term (Pauli-blocked pair) requires the protected particle to be a fermion of the same field as the sea. That is a statistics fact, not a property of antimatter as such. A scalar has no Fermi sea and no exclusion. Weisskopf 1939 also noted that charged Bose (scalar) particles keep a quadratically divergent self-energy [established in secondary literature; not checked against the original text here, so treat as unverified].
3. For the Higgs, every SM fermion contributes through its sea (pair) states only, and each such contribution is negative-definite pointwise in loop momentum (section 2b, item 3). Adding all SM fermion seas makes the divergence worse. CPT forces particle and antiparticle to enter identically (CONSTRAINTS D), so no particle/antiparticle imbalance can be used to arrange a cancellation.
4. The only SM-internal cancellation of the Lambda^2 term (Veltman) is between gauge/Higgs boson loops (+) and fermion loops (-). That is boson-fermion statistics, the same sign structure SUSY exploits, but in the SM the coefficients are unrelated by any symmetry and do not cancel at accessible scales (section 3).
5. In dimensional regularization the Lambda^2 term is absent. The physical hierarchy problem is then sensitivity to heavy thresholds, delta m_h^2 ~ (coupling) M_heavy^2/16pi^2. The SM-only content has no heavy thresholds below M_Pl. Bardeen's argument that the SM alone is natural in this sense (W. A. Bardeen, FERMILAB-CONF-95-391-T (1995) [unverified citation]) is a statement about the absence of heavy particles, not about antimatter. Whether gravity reintroduces the problem is outside SM scope.

So the analogy "antimatter protected the electron mass, maybe it protects the Higgs" fails, for a precise reason: what protected the electron was a chiral symmetry acting on a fermion, with the sea providing the Pauli-blocked counter-term. The Higgs is a scalar with no such symmetry, and the SM fermion seas are the source of its quadratic sensitivity.

## 5. Radiative EWSB (#4) (`calc/cw_radiative_ewsb.py`)

(A) Coleman-Weinberg, PRD 7, 1888 (1973), DOI 10.1103/PhysRevD.7.1888, with the tree mass term set to zero: V = A phi^4 + B phi^4 ln(phi^2/mu^2) has a minimum only for B > 0, with m_h^2 = 8 B v^2. With measured masses, sum n_i (-1)^F m_i^4 = -1.0e10 GeV^4 and B = -4.3e-3 < 0, so the stationary point is a maximum. **No radiative EWSB.** The top kills it for any m_t > 87.5 GeV. Even without the top, W and Z alone give m_h = 9.8 GeV, not 125 [established; the classic result, cf. Weinberg PRL 36, 294 (1976) and Linde JETP Lett. 23, 64 (1976), unverified citation details].

(B) SUSY's radiative EWSB is the RG-driven sign flip of m_Hu^2, driven by additive stop soft masses in its beta function. In the SM MS-bar scheme, beta(m^2) is proportional to m^2 at all orders (mass-independent scheme, m^2 the only dimensionful parameter), so the sign of m^2 is RG-invariant. Checked numerically: m(mu) stays between 131 and 144 GeV with m^2 > 0 from M_t to 10^20 GeV. The SM has no counterpart [established].

(C) Cutoff-language variant (Jegerlehner): C < 0 means top loops push the bare m^2 toward the broken phase below mu0. This depends on the regulator (Lambda^2 terms are absent in dim reg, CONSTRAINTS G and H2). It is also not an antimatter effect: it is the fermion-sea contribution of section 2b. It does not produce m_h or v, which remain inputs. [established that it is regulator dependent; any physical "triggering" reading is speculation]

## 6. Dead ends / open issues
- m(M_Pl) from the runner (139.4 GeV) disagrees with Buttazzo eq. (61f) (129.4 GeV). The gauge, Yukawa and lambda couplings match to 1e-4. Possibly a transcription error in eq. (100) or a different definition. Not used in any conclusion.
- The gauge-boson coefficient of Lambda^2 is gauge- and regulator-dependent in some treatments. The zero of C is quoted for the standard one-loop Landau-gauge form only. HKO include 2-loop quadratic terms and get the same scale (about 10^23 GeV).
- Weisskopf's own finite constant was not compared with c = ln 2 - 1/6.

## 7. CONSTRAINTS checklist
- **A1 (SM only):** only SM fields are used. SUSY appears only as a comparison target. Superpartners are mentioned only to state why the SM lacks the MSSM sign-flip mechanism. Pass.
- **A2 (neutrino mass):** not used. Neutrino Yukawas are omitted, and any Dirac-type y_nu < 1e-12 would change C by < 1e-23, so the result is insensitive to the mass mechanism. Pass.
- **A3 / H3 (reformulations, interpretations):** hole theory and time ordering are used only as bookkeeping. Every result is checked against the covariant formulation (section 2b, item 4) or stated covariantly (chiral symmetry). Pass.
- **B1-B8 (CPT, antimatter tests):** no particle/antiparticle asymmetry is introduced. Pass trivially.
- **C1-C2:** inputs from PDG 2024 via `tools/sm_inputs.py`. **C3:** no superpartner signatures arise because nothing BSM is introduced. The line does not claim to reproduce the SUSY cancellation, so the absence of superpartners is consistent with it. **C4:** not addressed, no claim made.
- **D:** CPT equal counting of particle and antiparticle in beta functions is respected (standard RGEs). It is used in section 4, item 3 as part of the argument. Running is 3-loop, stated. Couplings are taken from the shared tools.
- **E1-E10, F1-F2:** not relevant; no cosmological or baryon-number claims.
- **G:** the Veltman normalization is now fixed (section 2c). CONSTRAINTS G's "(3/2)(...)/v^2" corresponds to a different normalization; the zero is the same. No claim rests on the regulator: the negative result holds in cutoff (sections 1-2) and in dim reg (section 4, item 5). Weisskopf is reproduced.
- **H1:** no numerology. The near-zero of C at high scale is reported as a coincidence of running couplings, with no mechanism claimed. **H2:** the K^2 vs Lambda^2 factor 2 is explicitly shown as scheme dependent. Only scheme-independent statements are used as conclusions (sign-definiteness of the top-sea contribution, chiral symmetry, sign invariance of m^2). **H4:** every number has a script in `calc/`.

## 8. Testable / falsifiable content
- Prediction of this negative result: no SM-internal cancellation of the Higgs quadratic sensitivity at accessible scales. A Veltman-condition zero at mu0 ≈ 10^22.8 GeV is tied to M_t. A top pole mass measured near 169.4 GeV (versus 172.57 ± 0.29) would put C = 0 at M_Pl. Improved M_t and alpha_s measurements test the "Veltman at Planck" coincidence directly (dlog10 mu0/dM_t ≈ 1.2 per GeV).
