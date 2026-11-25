# L03 WORK: SM antimatter and dark matter

Status: negative result, draft for review. Scripts: `calc/freezeout.py` (-> `calc/freezeout_output.txt`), `calc/stable_states.py` (-> `calc/stable_states_output.txt`). Run from any directory with `python <script>`; both import `tools/sm_inputs.py`.

Tags: [established] = measured/proven with citation; [derived] = follows from committed script plus established inputs; [conjecture]; [speculation].

---

## 0. What "dark matter" has to be (E1, E5)

The target is Omega_c h^2 = 0.1200 +- 0.0012 of matter that (i) is not coupled to the photon-baryon plasma before recombination, (ii) is cold, (iii) is electrically neutral, (iv) is stable over 13.8 Gyr, (v) has sigma/m <~ 1 cm^2/g. [established, CONSTRAINTS E1/E5]

"Non-baryonic" in the CMB/BBN sense is an operational statement: the matter does not take part in acoustic oscillations and does not enter BBN reaction rates. Section 2 shows antibaryonic matter fails this exactly as baryonic matter does.

Required yield: Y = n/s = 4.66e-10 for m = m_N, 2.33e-10 for m = 1.88 GeV. [derived, stable_states.py sec. 7] For nucleon-mass relics this is 5.38 Y_B, i.e. the familiar Omega_c/Omega_b ratio.

---

## 1. Relic antibaryons/antileptons from thermal freeze-out (task a, task 2)

### 1.1 Set-up [established physics, derived numbers]

Below the QCD crossover (T_c ~ 155 MeV, E10) nucleons N = (p, n) and antinucleons are in equilibrium through N Nbar <-> pions/photons. Boltzmann equation for the antinucleon yield Ybar = n_Nbar/s, with Y_N = Ybar + Y_B:

    dYbar/dx = -lambda(x) [ Y_N Ybar - Yeq^2 ],   lambda(x) = sqrt(pi/45) M_Pl m_N g_*^{1/2}(T) <sigma v> / x^2,   x = m_N/T

g_*^{1/2} = (g_*s/sqrt(g_*))(1 + (1/3) dln g_*s/dln T) (Gondolo-Gelmini form), with g_*(T), g_*s(T) computed by numerical integration over an ideal gas of photons, 3 nu + 3 nubar, e+-, mu+-, pi, K, eta, rho, omega. Check: g_* = 10.75 at 5 MeV, 14.6 at 50 MeV, 20.1 at 150 MeV. Yeq uses the full Bessel K_2 form with g = 4 per species. Solver: scipy Radau in ln Ybar, x from 8 (T = 117 MeV) to 900 (T = 1.04 MeV).

Cross section. OBELIX (LEAR) measured beta*sigma_ann(pbar p) = 40.4-48 mb (c = 1) for p_lab = 46-175 MeV/c, roughly constant (1/v law with Coulomb enhancement at the lowest momenta); fitted Im a_sc = -0.69 fm. Carbonell, Protasov, Zenoni, Phys. Lett. B 397, 345 (1997), arXiv:nucl-th/9806032. [established] At T_f ~ 21 MeV the typical relative momentum is larger (p_lab ~ 300 MeV/c) where P-waves add, and pbar n, nbar n channels are not measured with the same precision, so I take <sigma v> = const and scan 20-120 mb. Also run sigma v = 1/m_pi^2 (= 19.9 mb), the Kolb & Turner estimate. Plasma (Debye) screening of the Coulomb enhancement is ignored; it only lowers sigma v at the smallest momenta and the result scales as 1/sigma v anyway.

### 1.2 Symmetric universe (no asymmetry) [derived]

| <sigma v> | x_f | T_f (MeV) | Y_N = Y_Nbar | n_N/n_gamma | Omega h^2 (N + Nbar) | / 0.12 |
|---|---|---|---|---|---|---|
| 1/m_pi^2 = 19.9 mb | 44.5 | 21.1 | 8.6e-20 | 6.1e-19 | 4.4e-11 | 3.7e-10 |
| 40 mb (OBELIX-like) | 45.1 | 20.8 | 4.4e-20 | 3.1e-19 | 2.3e-11 | 1.9e-10 |
| 60 mb | 45.5 | 20.6 | 3.0e-20 | 2.1e-19 | 1.5e-11 | 1.3e-10 |
| 120 mb | 46.2 | 20.3 | 1.5e-20 | 1.1e-19 | 7.7e-12 | 6.5e-11 |

Comparison: Kolb & Turner, *The Early Universe* (Addison-Wesley 1990), quote n_b/s ~ 7e-20 for the symmetric case with T_f ~ 22 MeV [unverified citation: page and exact number not checked against the book this session; a secondary source, arXiv:1801.10059, quotes n_N/n_gamma ~ 4.6e-19, consistent with the table]. My numbers agree to within the sigma v uncertainty.

Result: a matter-antimatter symmetric SM universe leaves Omega_(N+Nbar) h^2 ~ 1e-11, about 10^10 times too small for DM, and 10^9 times too small for the observed baryons. [derived] This is the "annihilation catastrophe", the standard argument that the asymmetry is an initial condition (or BSM output), restated with a committed solver.

### 1.3 Observed asymmetry Y_B = 8.67e-11 [derived]

With Y_N >= Y_B, the antinucleon annihilation rate per antinucleon is Gamma = n_N <sigma v> >= Y_B s <sigma v>. The script finds Gamma/H ~ 5e7-1e8 still at T = 1 MeV, so antinucleons never freeze out in the relevant window: they track chemical equilibrium Ybar = Yeq^2/Y_B ~ exp(-2 m_N/T). At T = 1.04 MeV this is ln Ybar = -1762 (Ybar ~ 10^-765), independent of sigma v, and it keeps falling. The relic antinucleon density is zero for every practical purpose. Antileptons: positrons annihilate on the electron excess (Y_e = Y_p by neutrality) at T ~ 20 keV and end in the same exponential suppression; antineutrinos are treated in section 4.

### 1.4 Constraint checks for (a)
- E1: fails by 10 orders of magnitude (symmetric) or infinitely (asymmetric).
- E5: even if the abundance were right, Nbar/pbar are charged or ionised at recombination: baryonic in the CMB sense (section 2).
- E9: a symmetric universe at the 1e-19 level would also be visible only through annihilation; domain-based escapes are the excluded symmetric cosmologies (A1).

**Status (a): dead.** [derived]

---

## 2. Antibaryonic matter counts as baryonic for CMB and BBN (task 3) [established physics, derived numbers]

CMB. The acoustic peaks depend on the baryon loading R = 3 rho_b/(4 rho_gamma) of the fluid tightly coupled to photons. Coupling is Thomson scattering, sigma_T = (8 pi/3) alpha^2/m_e^2, which depends on the charge squared and the mass of the scatterer, so e+ and e- scatter identically (CPT; B6 tests the g-factor, B2 the pbar q/m to 16 ppt). Antiprotons are tied to positrons by the same Coulomb coupling. So an ionised antimatter plasma contributes to R exactly as ordinary plasma does. Planck measures Omega_b h^2 = 0.02237; if 0.12 were antibaryonic plasma, R(z* = 1090) would be 3.96 instead of 0.62 (`stable_states.py` sec. 5), a factor 6.4, which the odd/even peak height ratio excludes. The measured Omega_b is therefore a bound on baryons plus antibaryons.

BBN. The strong and electromagnetic interactions are C-invariant and the weak n <-> p rates map under CP to the nbar <-> pbar rates; the antineutron and neutron lifetimes are equal by CPT. In an antimatter region, anti-BBN produces the same anti-element yields as a function of |eta|. BBN therefore treats antibaryons as baryons too. Mixing matter and antimatter regions before or during BBN causes annihilation and photodisintegration, constrained by E9. [established physics; the CP mapping of n<->p rates holds exactly only for zero lepton asymmetry, which E6 bounds]

Consequence: any antimatter that was ever ionised and spatially mixed with photons at recombination is inside Omega_b. Only antimatter already locked in compact, photon-decoupled objects before ~z = 1100 (and before BBN to avoid the BBN eta budget) could escape. That restricts (b) and (c) to objects formed in the first ~seconds.

---

## 3. Candidates by category (task 1)

### (b) Antimatter in compact objects
- Antistars, anti-white-dwarfs, anti-neutron-stars [established that they can't be DM]: they form from gas after recombination, so their mass is inside Omega_b (sec. 2), at most 0.0224, not 0.12. In addition, any antistar population in our Galaxy is bounded by Fermi-LAT to <~1 per 4e5 stars [CONSTRAINTS E9, Dupourque, Tibaldo, von Ballmoos, PRD 103, 083016 (2021), arXiv:2103.10073, figure uncertain], and Gpc-scale antimatter domains would be needed to avoid boundary annihilation (Cohen, De Rujula, Glashow, arXiv:astro-ph/9707087). They also need a mechanism for local antimatter excesses, which the SM lacks (E10). **Dead.**
- "Antimatter primordial black holes". A black hole has no baryon number: the no-hair theorems leave mass, charge and spin, and Hawking emission is C-symmetric. A PBH formed from antimatter is indistinguishable from one formed from matter, so "antimatter PBH" has no physical content. [established] Separately, PBH formation needs O(1) curvature perturbations at the horizon scale; the QCD crossover softens the equation of state and enhances formation near a solar mass by a factor ~5 for a given perturbation spectrum (Byrnes, Hindmarsh, Young, Hawkins, JCAP 08 (2018) 041, arXiv:1801.06138), but it does not produce the perturbations. The primordial spectrum is measured only on large scales (amplitude ~2e-9) and is not SM physics. Gross et al. (arXiv:1803.10242) examined PBHs from the SM Higgs-potential instability during inflation, which needs inflation plus a fixed non-minimal coupling: not SM-only. **Out of scope and not antimatter.**

### (c) Antiquark / strange-antimatter nuggets
- Witten's quark nuggets (E. Witten, "Cosmic separation of phases", Phys. Rev. D 30, 272 (1984), DOI 10.1103/PhysRevD.30.272; viable only if quark matter has energy per baryon < 938 MeV) need (1) a first-order QCD transition to concentrate baryon number, and (2) the Bodmer-Witten hypothesis that strange quark matter is absolutely stable. (1) is false: the transition is a crossover at physical quark masses (Aoki et al., Nature 443, 675 (2006), E10). (2) is an unobserved phenomenon (A1). Small nuggets also evaporate/boil at T ~ tens of MeV (Alcock & Farhi, Phys. Rev. D 32, 1273 (1985), DOI 10.1103/PhysRevD.32.1273: only lumps above a threshold baryon number survive to T ~ 1 MeV). Recent reappraisals exist (arXiv:2404.12094; arXiv:2603.16686) which I have not read; a literature checker should confirm none of them gives a crossover-compatible SM formation route. Witten's original scenario was also for matter nuggets, which would be baryonic in B but decoupled from photons; an antimatter version additionally needs a CP-odd separation mechanism.
- Zhitnitsky's (anti)quark nuggets: compressed by axion domain walls (A. Zhitnitsky, JCAP 10 (2003) 010, arXiv:hep-ph/0202161). Requires the axion. **Out of scope (A1).**
- SM-only route? I find none. With a crossover there is no bubble wall and no latent heat, so nothing concentrates baryon or antibaryon number on macroscopic scales; the SM has no stable domain walls either (vacuum manifold S^3, pi_0 = 0; sec. 4 of the script). With CKM CP violation (J ~ 3e-5) and no first-order transition, there is no SM process that separates B from Bbar into different nuggets. [derived for the topological statement; conjecture-level for "no other SM concentration mechanism", but every published nugget mechanism I know uses a first-order transition or a new field]. **Dead in scope.**

### (d) Sexaquark S (uuddss, B = 2, Q = 0, strangeness -2) and anti-sexaquark Sbar
Scope classification for the overseer:
- It is built only from SM quarks and its existence is a question of SM QCD dynamics, so it is **SM field content**.
- It has never been observed; deep binding is not established by lattice QCD at physical masses. Under A1 ("any unobserved phenomenon, however well-motivated") it is an **unobserved phenomenon**. My recommendation: treat it as out of scope as a mechanism input; a line may discuss it conditionally ("if QCD binds S deeply, then ...") only if the conclusion is flagged conditional. Final call is the overseer's.

Experimental and theoretical status [established, citations verified by web search this session]:
- Proposal: G. Farrar, arXiv:1708.08951 (stable S with m_S <~ 2 GeV as DM); follow-ups arXiv:1805.03723, 2007.10378, 2201.01334 (m_S < 2054 MeV gives lifetime > age of Universe), Farrar & Wang arXiv:2306.03123.
- BaBar, PRL 122, 072002 (2019), arXiv:1810.04724: no Upsilon(2S,3S) -> S Lbar Lbar signal; B < (1.2-1.4)e-7 at 90% CL for m_S < 2.05 GeV.
- Lattice: Green, Hanlon, Junnarkar, Wittig, PRL 127, 242003 (2021), arXiv:2103.01054: H dibaryon bound by only 4.56 +- 1.13 +- 0.63 MeV at the SU(3)-flavour-symmetric point (heavier-than-physical light quarks, m_pi ~ 420 MeV [approx, from memory]). Not a deeply bound state; physical-point binding unsettled.
- Abundance: Kolb & Turner, PRD 99, 063519 (2019), arXiv:1809.06003: under generous assumptions S carries at most ~1e-11 of the baryon number, so it cannot be the DM. Farrar disputes applicability to her scenario (arXiv:1805.03723 v-later, 2306.03123).
- Gross, Polosa, Strumia, Urbano, Xue, PRD 98, 063005 (2018), arXiv:1803.10242: thermal abundance would require m_S ~ 1.2 GeV, which is excluded by 16O stability.
- McDermott, Reddy, Sen, PRD 99, 035013 (2019), arXiv:1809.06765: S with 1860 < m_S < 2054 MeV is in serious tension with neutron stars and supernovae unless production is strongly suppressed.

Mass windows from my script: absolutely stable if m_S < m(2H atom) = 1876.12 MeV; cosmologically stable (doubly weak decay) if m_S < m_p + m_e + m_Lambda = 2054.47 MeV.

Is S "baryonic" for CMB purposes? No: it is neutral and compact, so it would not couple to photons. It is the one SM-content object that carries B and still behaves as CMB dark matter. That is why it is the only real loophole in this line.

Antimatter angle: Farrar & Zaharijas, PRL 96, 041302 (2006), arXiv:hep-ph/0510079, proposed that the DM is an antibaryonic H-dibaryon-like state whose antibaryon number compensates the visible baryon excess (total B = 0), which needs particle and antiparticle annihilation cross sections on ordinary matter to differ by >~10%. My assessment [conjecture, not in the paper as far as I verified; I read only the abstract]: within the SM, a 10% difference between sigma(Xbar N) and sigma(X Nbar) for strong-interaction processes is impossible, because QCD with |theta| < ~1e-10 conserves C and CP exactly, so those cross sections are equal up to CKM-suppressed weak corrections. The SM version of this antimatter-DM idea fails at the CP-violation step even before S existence is considered. This needs a referee check.

**Status (d): out of scope (unobserved) by A1, and disfavoured on the merits even if granted.**

### (e) Anything else
- Relic antineutrinos (with neutrinos): SM, stable, neutral, non-baryonic, they exist. Omega_nu h^2 = sum m_nu/93.14 eV = 6.3e-4 (minimal 0.059 eV) to 1.3e-3 (0.12 eV bound); even 3 x 0.45 eV (KATRIN) gives 0.0145. They are hot. A large lepton asymmetry (antineutrino excess) increases their number density only through a chemical potential bounded by N_eff (E6) and does not make them cold. [derived numbers, established physics] **Dead as CDM; it is the only SM antimatter that is genuinely dark.**
- Positronium, protonium, antihydrogen in neutral form: positronium and protonium are unstable (ns-us). Neutral antihydrogen gas is ionised before recombination and counts as baryons (sec. 2). **Dead.**
- SM topological or non-topological solitons: no stable defects (S^3 homotopy). Non-topological "Higgs-top bags" involve unstable tops. **Dead.**
- Dirac sea / hole theory as "hidden mass": the filled sea is the vacuum, renormalised to zero charge and its energy is part of the cosmological-constant problem (G), not a clustering matter component. H3 applies: it is an interpretation with identical S-matrix, so it cannot produce a new matter density. **Dead.**

---

## 4. Is there an SM analogue of R-parity? (task 4)

### 4.1 R-parity restricted to SM states is trivial [derived, stable_states.py sec. 1]
For every SM field, 3(B-L) + 2s is even: quarks 3(1/3) + 1 = 2, leptons 3(-1) + 1 = -2, gauge bosons 2, Higgs 0; antiparticles flip B, L, leaving the parity unchanged. Hence R = +1 on every SM state, elementary or composite. Equivalently (-1)^{2s} = (-1)^{3B+L} on the SM spectrum. The SUSY mechanism works because superpartners carry R = -1; the SM has no R = -1 states, so the operation has nothing to protect.

### 4.2 Stability classification [derived + established]
The exact or effectively exact SM charges at T = 0 are Q (exact, gauge), B and L (accidental; violated only non-perturbatively by B+L sphalerons/instantons, rate ~ exp(-4pi/alpha_W) ~ 1e-165 at T = 0, F2), (-1)^F (exact, Lorentz), and energy-momentum. B-L: gauge anomalies cancel (script sec. 2: B and L each have SU(2)^2 coefficient 1/2 per generation, which cancels in B-L), so SM gauge dynamics conserve it. Two caveats: without nu_R, B-L has a mixed gravitational anomaly of -1 per generation; and if neutrino masses are Majorana, B-L is broken by 2 units. So "exact B-L" is exact with respect to SM gauge interactions only.

A state is absolutely stable only if it is the lightest state with its set of conserved charges. The lightest states per sector (script sec. 3):

| sector | lightest state | DM-relevant property |
|---|---|---|
| Q != 0 | e-/e+ | charged |
| Q = 0, B = 0, F odd (or L != 0) | lightest nu/nubar | neutral, non-baryonic, hot, Omega h^2 <~ 1.3e-3 |
| B = +-1 | p/pbar | charged |
| B = +-1, Q = 0 | H / anti-H atom | ionised before recombination: baryonic |
| B = +-2, Q = 0 | 2H / anti-2H atom (or S/Sbar if it exists with m_S < 1876.12 MeV) | baryonic, unless S exists |
| B = +-A | nuclei/antinuclei and atoms | baryonic |
| all zero | photon | radiation |

Every unstable SM state (mu, tau, pi, K, n, W, Z, H, t, positronium, protonium, sphalerons) decays far faster than 13.8 Gyr.

### 4.3 Statement of the negative result
**Claim [derived, conditional on the stable-state list being complete]:** Within the SM with observed parameters, the set of stable, electrically neutral states that are not coupled to the photon-baryon plasma before recombination consists of the relic neutrinos and antineutrinos only. They are hot and supply at most ~1% of Omega_c (0.12 eV bound) or ~12% at the KATRIN-saturating mass. Therefore no SM conserved quantity, including those involving antimatter (B, L, B-L, CPT, C, CP), stabilises a neutral, non-baryonic, cold relic. The single loophole within SM field content is a deeply bound uuddss state, whose existence is unobserved (A1).

Where the proof is not airtight:
1. Completeness of the bound-state list rests on QCD dynamics that is not solved at the physical point for B = 2, S = -2 (the sexaquark). This is the loophole above.
2. "Non-baryonic" is used operationally (not coupled to photons before recombination). A neutral compact B != 0 object formed before BBN would pass the CMB test; within the SM I find no formation mechanism (section 3c), but that sub-claim is a conjecture supported by the absence of a first-order transition, not a theorem.

### 4.4 Structural analogy, stated plainly
R-parity = (-1)^{3(B-L)} x (-1)^{2s}. In the SM the two factors are equal on every state, so their product is trivial. The SM's (B-L)-type conservation does stabilise something, the proton (via B, effectively) and the lightest neutrino (via (-1)^F and Lorentz invariance), but both fail as CDM: one is charged/baryonic, the other hot. Antimatter adds no new conserved charge: CPT maps each stable particle to a stable antiparticle with identical mass and lifetime (B1-B4), so antiparticles inherit exactly the particle stability list.

---

## 5. Result

SM antimatter cannot reproduce SUSY result #3. [derived/established; conditional only on the sexaquark loophole being closed or ruled out of scope]
- Freeze-out: Omega_(N+Nbar) h^2 = (0.8-4.4) x 1e-11 symmetric; antinucleons exponentially gone with the observed asymmetry.
- Antibaryons ionised at recombination are part of Omega_b (CMB R factor 6.4 too large otherwise).
- The only neutral non-baryonic stable SM relic is the (anti)neutrino: hot, Omega h^2 <~ 1.3e-3.
- SM R-parity is identically +1.

Testable/falsifiable consistency checks: (i) a sexaquark with m_S < 2.05 GeV found below the BaBar limit or a deeply bound H on the lattice at the physical point would reopen (d); (ii) direct detection of a cosmic antinucleus flux would bound antimatter far below Omega_b and leave this conclusion intact; (iii) Omega_nu from DESI/Euclid-type sum m_nu measurement fixes the antineutrino contribution, predicted here as Omega_nu h^2 = sum m_nu/93.14 eV.

---

## 6. CONSTRAINTS checklist

- **A1 (scope):** only SM fields used. Axion nuggets, PBH perturbation spectra, Majorana masses, BSM baryogenesis are named and excluded. Sexaquark flagged as unobserved; used only conditionally.
- **A2:** neutrino masses enter only via Omega_nu = sum m/93.14 eV, which is insensitive to the mass mechanism (it uses only the measured/bounded masses and SM decoupling). B-L caveat for Majorana noted, not used.
- **A3:** no reformulation used.
- **B1-B8:** CPT used to give antiparticles identical masses, lifetimes, Thomson cross sections (B2, B4, B6). No particle/antiparticle asymmetry assumed. CKM size (B8) used to argue against SM separation of B and Bbar (sec. 3c/3d).
- **C1-C2:** not used numerically except masses in thresholds.
- **C3:** a negative result for #3 says nothing about superpartners; the absence of SUSY signals is consistent with an SM-only world, and nothing here predicts superpartner-like signatures.
- **C4:** not used.
- **D:** not used.
- **E1:** compared in every candidate.
- **E2/E3:** Omega_b and eta used (sec. 1.3, 2).
- **E4:** not relevant.
- **E5:** used as the definition of the target; charged/ionised candidates fail it.
- **E6:** bounds the lepton-asymmetry escape for relic antineutrinos.
- **E7/E8:** used for Omega_nu.
- **E9:** antistars, domains, antinuclei: all bound antimatter far below Omega_b.
- **E10:** crossover kills nugget formation; asymmetry taken as input, not produced.
- **F1/F2:** used for B and B+L stability statements.
- **G:** Dirac sea energy is a vacuum-energy question, not matter (sec. 3e).
- **H1:** no numerology; the 5.38 Y_B ratio is shown as the target, not fitted.
- **H2:** no loop calculations; regulator independence not applicable.
- **H3:** Dirac sea interpretation explicitly gives nothing new.
- **H4:** both scripts committed with outputs.

## 7. Open issues
1. Kolb & Turner book number (7e-20) not checked against the book. Secondary source agrees.
2. sigma v at T ~ 20 MeV is extrapolated from OBELIX data at lower momenta; the result scales as 1/<sigma v> and is 10 orders away from the target, so the uncertainty is irrelevant to the conclusion.
3. Farrar & Zaharijas 2006 only read at abstract level. The claim that QCD C/CP conservation forbids their required 10% cross-section difference needs a referee or literature check against the full paper.
4. Lattice pion mass for 2103.01054 quoted from memory.
5. Strange-nugget reappraisals arXiv:2404.12094 and arXiv:2603.16686 not read; check whether either proposes nugget formation compatible with a QCD crossover.
