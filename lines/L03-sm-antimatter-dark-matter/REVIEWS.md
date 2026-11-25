# L03 Reviews

## Referee 1 (cycle 2)

**Verdict: MAJOR ISSUES (fixable)**

What I checked. I reran both scripts from inside `calc/` (`python freezeout.py`, `python stable_states.py`) and got output identical to the committed `*_output.txt`. I rederived the Boltzmann prefactor lambda = sqrt(pi/45) M_Pl m g_*^{1/2}/x^2, the ln-Y forms of both the symmetric and asymmetric equations (freezeout.py:119-136), the Omega h^2 conversion (s0 = 2891 cm^-3, rho_c/h^2 = 1.05368e-5 GeV cm^-3), the required yield 4.66e-10 = 5.38 Y_B, R(z*) = 0.622 and 3.958, all five rows of the anomaly table (B, L, B-L for SU(2)^2, SU(3)^2, Y^2, grav^2, cubic), the R-parity exponents, 1/m_pi^2 = 19.99 mb, the sexaquark thresholds (m_d + m_e = 1876.12 MeV, m_p + m_e + m_Lambda = 2054.47 MeV, which is the correct Delta S = 1 semileptonic S -> Lambda p e- nubar threshold), and exp(-4pi/alpha_W) ~ 1e-162 to 1e-165. All correct. The mean relative velocity at T_f = 21 MeV is v ~ 0.34, p_lab ~ 340 MeV/c, consistent with the "~300 MeV/c" in WORK:29. The asymmetric-case result is correctly identified as chemical-equilibrium tracking: by the script's own Gamma/H ~ 4.9e7 at x = 900 and Gamma/H ∝ 1/x, antinucleons would only freeze out near x ~ 4e10 (T ~ 0.02 eV).

Citations spot-checked by web search, all correct: Gross, Polosa, Strumia, Urbano, Xue, arXiv:1803.10242, PRD 98 063005 (it covers both the hexaquark and the Higgs-instability PBHs, so the double use at WORK:71 and WORK:88 is legitimate); Carbonell, Protasov, Zenoni, PLB 397 345 (1997) = nucl-th/9806032 (posted a year after publication, which is fine); arXiv:1801.10059 does quote n_N/n_gamma ~ 4.6e-19; Farrar & Wang arXiv:2306.03123 exists ("Constraints on long-lived di-baryons and di-baryonic dark matter"). arXiv:2404.12094 could not be resolved by search, and WORK already flags it as unread.

The central negative claim, that SM antimatter cannot be CDM, is supported by the calculations. The findings below are about the completeness argument and some bookkeeping, not about the conclusion of sections 1-2.

### Findings

1. **[major] The stability "theorem" is false as stated, and the completeness claim rests on it.** Location: stable_states.py:87-89, WORK.md §4.2 (line 115), §4.3 (line 130). The script says "the only absolutely stable single-particle states are the lightest state in each charge sector". For DM the relevant criterion is tau > t_U, not absolute stability, and the two give different lists. Counterexamples:
   - The heavier neutrino mass eigenstates nu_2 and nu_3 are not the lightest in their sector, but radiative decay nu_i -> nu_j gamma has a lifetime far above t_U. WORK itself uses all three, since Omega_nu = sum m_nu/93.14 eV.
   - Many stable or effectively stable nuclei and atoms are not the lightest state with their (B, Q). Examples are the double-beta isobar pairs and Bi-209.
   - The line itself uses a cosmological-stability window for the sexaquark, m_S < 2054 MeV, which contradicts the "lightest state" criterion of §4.2.

   Fix: restate the criterion as "lightest state in its sector, or decays only through processes with tau > t_U". Then add a sentence, with a scripted check if possible, that the extra metastable SM states this admits (heavy neutrino eigenstates, long-lived nuclei and atoms) are either already in the neutrino budget or baryonic.

2. **[major] The enumeration misses pion stars and lepton-asymmetry-driven pion condensation, which are SM-only compact dark objects tied directly to antimatter.** Location: WORK §3(e) (lines 99-103), §4.3 item 2 (line 134), PROPOSAL item 3.
   - Brandt, Endrodi, Fraga, Hippert, Schaffner-Bielich, Schmalzbauer, "New class of compact stars: Pion stars", PRD 98, 094510 (2018), arXiv:1802.06685, describes Bose-Einstein-condensed pi+ (or pi-) objects. Weak decay is stabilised by a lepton/neutrino Fermi sea, and the authors state no BSM constituents are needed.
   - Follow-ups find the cosmic trajectory passes through the pion-condensed phase at T ~ 100 MeV if the lepton-flavour asymmetry is large. See Wygas, Oldengott, Bodeker, Schwarz, PRL 121, 201302 (2018), and Vovchenko et al., and Stashko et al., arXiv:2303.06190.

   Such an object is neutral overall, compact, formed before BBN, and has B ~ 0, so it passes the operational "non-baryonic" test of §2. That is exactly the escape route WORK:63 and WORK:134 say does not exist in the SM. The required input is a lepton asymmetry |l| >> eta. Like eta, that is an initial condition rather than new physics, so A1 does not obviously exclude it. Fix: add a §3(f) on pion stars and condensates, bound the lepton asymmetry with BBN/CMB (E6 plus BBN flavour-equilibrated bounds on xi_nu), and show either that the allowed asymmetry is below the condensation threshold or that no SM mechanism fragments a condensate into stable compact objects with Omega h^2 ~ 0.12. Until then the §4.3 "only relic neutrinos" claim is incomplete.

3. **[minor] The "antineutrino" label is not mechanism-independent (A2).** Location: WORK:100 ("the only SM antimatter that is genuinely dark"), WORK:146, PROPOSAL item 3. Relic neutrinos are non-relativistic today. Whether a relic "antineutrino" is a distinct antiparticle, or just a helicity state of a Majorana field, depends on the unobserved mass mechanism. Omega_nu is insensitive to this, as WORK:156 correctly says, but calling it "antimatter" is not. Fix: say "relic neutrinos (whose particle/antiparticle distinction today depends on the unobserved Dirac/Majorana nature, A2)".

4. **[minor] The Thomson cross section scaling is misstated.** Location: WORK:59, stable_states.py:117. sigma_T = (8 pi/3) q^4 alpha^2/m^2 (charge to the fourth power), not "charge squared". The conclusion is unchanged. Also, B2 (pbar q/m) and B6 (g-factor, tagged [uncertain]) do not test e+ versus e- charge and mass. Cite the PDG positron limits (|m_e+ - m_e-|/m and |q_e+ + q_e-|/e) instead.

5. **[minor] PROPOSAL and WORK disagree on the neutrino fraction.** Location: PROPOSAL:11 says "100x too little", while WORK:130 and stable_states output give 1% at 0.12 eV and 12% (8x too little) at the KATRIN-saturating 1.35 eV. Make them consistent, and say the 1.35 eV case is already excluded by E7.

6. **[minor] Several CONSTRAINTS items are not addressed explicitly, which CONSTRAINTS.md requires before promotion.** Location: WORK §6 (lines 158, 171).
   - B9 and B10 are not listed. B10 (theta-bar < 1e-10) is actually used at WORK:95 without citation.
   - F3 (n-nbar, tau > 4.7e8 s) is omitted. It is the one direct Delta B = 2 matter-antimatter test and is relevant to the S/Sbar and nucleon discussion.
   - In E9, the 511 keV line and the BBN photodisintegration bound are not discussed.

   Fix: add one line each.

7. **[minor] The defect argument covers only the electroweak vacuum manifold.** Location: stable_states.py:92-93, WORK:76, WORK:102.
   - The QCD chiral manifold SU(3)_L x SU(3)_R / SU(3)_V has pi_3 = Z, and its solitons are the baryons themselves, so they are already counted.
   - Embedded (non-topological) Z-strings and W-strings exist in the EW sector. They are unstable at physical sin^2 theta_W and m_H (James, Perivolaropoulos, Vachaspati 1992), but should be named.

   Fix: one sentence covering both points.

8. **[minor] The falsifiable content is weak and partly mislabelled.** Location: WORK:149, PROPOSAL:17.
   - Item (iii) calls Omega_nu h^2 = sum m_nu/93.14 eV "predicted here". It is the standard relic relation and not an output of this line. Relabel it as a consistency check.
   - The genuine falsifier is (i), sexaquark discovery.
   - Finding 2 supplies a second one: an observational bound on pion-star-like compact objects, or a lepton-asymmetry measurement.

   No novel prediction is claimed or needed for a negative result, but the wording should not imply one.

9. **[minor] Some quantitative statements have no script, contrary to H4.** Location: WORK:46 (positron freeze-out at T ~ 20 keV), WORK:29 (p_lab ~ 300 MeV/c at T_f), WORK:127 (lifetimes "far faster than 13.8 Gyr"). Fix: add a few lines to freezeout.py or stable_states.py, or tag the statements [established] with a citation.

10. **[minor] Rhetoric and tag hygiene.**
    - WORK:49 "fails ... infinitely (asymmetric)" should be replaced by the computed bound (Y_Nbar < 10^-765 at T = 1 MeV, still falling).
    - WORK:83 tags the sexaquark block "[established, citations verified]" but WORK:86 quotes the lattice m_pi "from memory". The m_pi ~ 420 MeV figure needs checking against arXiv:2103.01054 before the [established] tag stands.

11. **[note, not an error] The Farrar-Zaharijas assessment (WORK:95) holds.** C invariance of QCD with theta-bar < 1e-10 maps Xbar N -> f onto X Nbar -> fbar, so the required ~10% difference can only come from CKM-suppressed weak amplitudes (order J times G_F-suppressed interference), many orders too small. I agree with the conclusion. Promote it from [conjecture] to [derived], cite B10/B8, and still check the full paper for whatever CP-violation source the authors invoke.

No BSM content is used in any mechanism. Axion nuggets, Higgs-instability PBHs, Majorana masses and BSM baryogenesis are correctly named and excluded. No numerology: the 5.38 ratio is presented as a target, not a fit.
