# LW2 WORK: chiral-partner protection, pion vs Higgs

## CLAIM

1. [established, re-derived] The SM realises the SUSY #1 cancellation for one scalar: the charged pion. Its photon-loop mass shift is a sum over quark-antiquark states (π, ρ-like vector, a1-like axial) with weights obeying the two Weinberg sum rules. WSR1 removes Λ², WSR2 removes ln Λ. The result is finite (DGMLY). Softly broken SUSY (top/stop) removes Λ² but leaves −(3y_t²/8π²) m̃² ln(Λ²/m̃²). So for this observable QCD's matter-antimatter partner structure cancels more than soft SUSY does.
2. [established structure, explicit check here] The SM Higgs sector has the same chiral-partner structure: h (0+, t̄t scalar channel) and G0 (0−, t̄iγ5t channel) are partners under SO(4) ≅ SU(2)L×SU(2)R. The t̄t loop gives them identical Λ² terms; S − P is log-only and ∝ m_t². So λ = m_h²/2v² is protected in the same way as the pion splitting. The Λ² sits only in the SO(4)-invariant operator H†H.
3. [conjecture, argued] Obstruction: the pion mechanism protects a scalar mass only when the scalar is a Goldstone of a symmetry whose constituents have no symmetric relevant operator. QCD has none (q̄q mass terms break chiral symmetry; Λ_QCD comes from dimensional transmutation). The SM has H†H, allowed by every SM symmetry including C, P, CP, CPT and custodial SO(4). Removing it requires h to be a composite of an SM fermion-antifermion pair. Both SM options fail: QCD gives 0− Goldstones and a heavy, broad 0+ σ, and h is 0+ and light. t̄t compositeness needs m_t ≈ 235-246 GeV (1-loop). **Protecting μ² this way needs BSM strong dynamics, so the line stops there.**

Status: partial positive match (pion) plus a negative result for the Higgs μ². SUSY #4 and #6 are not reproduced (see §5).

## 1. Pion EM mass as the SM's finite scalar self-energy (calc/c1_pion_wsr.py)

- [established] Δm_π² ≡ m(π+)² − m(π0)² = −(3α/4πf_π²) ∫₀^∞ dQ² Q² [Π_V − Π_A](Q²), in the chiral limit and at O(α). Das, Guralnik, Mathur, Low, Young, PRL 18, 759 (1967), doi:10.1103/PhysRevLett.18.759 [unverified, from memory]. Weinberg sum rules: Weinberg, PRL 18, 507 (1967), doi:10.1103/PhysRevLett.18.507 [unverified, from memory].
- Narrow states: Π_V = F_V²/(m_V²+Q²), Π_A = f_π²/Q² + F_A²/(m_A²+Q²). The weights are c_V = F_V², c_A = −F_A², c_π = −f_π² (m_π = 0).
- [derived, c1(a)] Σ c_i J(m_i) with J = ∫₀^Λ² dQ² Q²/(Q²+m²) has coefficient Σc_i of Λ², −Σc_i m_i² of ln Λ², and constant Σc_i m_i² ln m_i². WSR1 is F_V² − F_A² = f_π², i.e. Σc = 0. WSR2 is F_V²m_V² = F_A²m_A², i.e. Σc m² = 0. These are the same conditions as Pauli's Σ(−1)^F m^{2k} = 0 for k = 0, 1 (CONSTRAINTS G) with weights F² in place of degree-of-freedom counts.
- [derived, c1(b)] Solving both WSRs gives Δm_π² = (3α/4π) m_V²m_A²/(m_A²−m_V²) ln(m_A²/m_V²), the DGMLY formula (sympy reproduces it). A point-like pion (c_π only) gives +(3α/4π)Λ².
- [established inputs, computed] Measured Δm_π² = 1261.2 MeV² (Δm = 4.5936 MeV). DGMLY with m_ρ = 775.26, m_a1 = 1230 ± 40 MeV gives 1604 MeV² (5.82 MeV, 1.27× measured); with KSRF m_a1 = √2 m_ρ it gives 1452 MeV² (5.27 MeV). The ~20-30% excess is the usual size of lowest-resonance saturation error [established order of magnitude; not a precision test]. The m_u − m_d contribution is O((m_u−m_d)²), about 0.1 MeV [established, Gasser & Leutwyler, Ann. Phys. 158, 142 (1984), unverified page].
- [established inputs, computed] The naive cutoff estimate (3α/4π)Λ² = Δm_π² gives Λ_nat = 851 MeV. The partners sit at 775 and 1230 MeV. Here naturalness predicted the partners' location and they are there (the same logic as Gaillard & Lee's charm estimate, PRD 10, 897 (1974) [unverified, from memory]).
- [derived, c1(d)] Top/stop with cutoff CW potential: the Λ² coefficient of ∂²V/∂φ² is 0 (Str M² is φ-independent), and the remainder is −(3y²/8π²) m̃² ln(Λ²/m̃²) (log survives).

Dictionary [this line's framing; each entry is literal, not an analogy]:

| SUSY (softly broken) | QCD charged pion |
|---|---|
| superpartner: same gauge charges, spin differs by ½ | chiral partner: ρ (1−) vs a1 (1+), both q̄q |
| Str 1 = 0 (dof matching) | WSR1: Σ F_V² − Σ F_A² − f_π² = 0 |
| ∂_φ² Str M² = 0 → no Λ² | WSR1 → no Λ² |
| ∂_φ² Str M⁴ ≠ 0 → ln Λ remains | WSR2: Σ F_V²m_V² − Σ F_A²m_A² = 0 → no ln Λ |
| soft mass m̃² | splitting m_a1² − m_ρ², set by ⟨q̄q⟩ (OPE of Π_V − Π_A starts at α_s⟨q̄q⟩²/Q⁶ [established]) |

Limits of the map [established]: WSR2 holds only in the chiral limit and is exact because Π_V − Π_A falls as 1/Q⁶. The partners are bound states, not elementary. The map applies only to the photon-loop part of the π± mass.

## 2. The Higgs sector's own chiral partners (calc/c2(a))

- Couplings −(y/√2) h t̄t and −(y/√2) G0 t̄ iγ5 t (SM, unitary normalisation of the doublet). Euclidean cutoff, p² = 0, broken phase with m = m_t.
- [derived] Λ² coefficient: −N_c y²/8π² for h and for G0. The two are equal.
- [derived] S − P = N_c y² m²/(4π²)·[ln((Λ²+m²)/m²) − Λ²/(Λ²+m²) + …], with leading term (N_c y² m_t²/4π²) ln Λ. It vanishes as m_t → 0. With m_t² = y²v²/2 this is the y⁴v² ln Λ term, i.e. the −6y_t⁴ in β_λ (sign checked against the CW potential, c2 printout).
- [established] The G0 mass is fixed at zero (Goldstone, then eaten) by the tadpole condition, which absorbs the common Λ² piece. So the physical m_h² gets from t̄t only the S − P part, which is log-only. Equivalently m_h² = 2λv² with λ running logarithmically.
- Consequence [established in content, framed here]: the SM already protects the ratio m_h/v by the same partner mechanism that makes the pion splitting finite. The hierarchy problem is entirely the question of why v² (μ²) is small. That parameter multiplies H†H, which is invariant under SO(4), C, P, CP and CPT, so no symmetry of the SM, antimatter-related or otherwise, forbids its Λ² shift. This agrees with L01b's finding that no SM symmetry enforces its boson/top cancellation.
- Experimenter hypothesis D2 [comparison]: π0 is self-conjugate and gets no O(α) EM shift, while π± (each the other's antiparticle) get the finite shift. In the pion case the protection comes from the Goldstone nature, not from C-self-conjugacy. The same holds for h vs G0, where both are self-conjugate and only the 0− one is protected. This is consistent with L01b ("self-conjugacy irrelevant").

## 3. Why the pion mechanism cannot protect μ² inside the SM (calc/c2(c), calc/c3)

For μ² to be protected the way m_π is, h would have to be a fermion-antifermion composite whose constituents admit no symmetric relevant operator. SM candidates:

(a) QCD q̄q. [established] The chiral-symmetry Goldstones are 0− (pions). h is 0+: spin-parity measurements favour 0+ over 0−, CMS arXiv:1411.3441, ATLAS arXiv:1506.05669 [unverified refs, from memory]. QCD's 0+ radial mode, the analogue of h, is the f0(500): pole ≈ 441 − i272 MeV (Caprini, Colangelo, Leutwyler, PRL 96, 132001 (2006), hep-ph/0512364 [unverified, from memory]). With f_π = 92.1 MeV:

| | radial mode / condensate | effective quartic m²/2f² | Γ/m |
|---|---|---|---|
| QCD σ | 4.79 (4.34-5.97 over PDG 400-550 MeV) | 11.5 (9.4-17.8) | 0.62 (pole Im/Re) |
| SM h | 0.508 | 0.129 | 3.3×10⁻⁵ |

The one SM example of a q̄q condensate puts its 0+ mode at the compositeness scale, strongly coupled. h is lighter by a factor of about 10 relative to its condensate and weakly coupled. [established numbers; the inference "h is not QCD-like" is standard, cf. Contino arXiv:1005.4269]
The QCD condensate does break EW symmetry in the real SM [established, Quigg & Shrock PRD 79, 096002 (2009), arXiv:0901.3958]: M_W(QCD alone) = g f_π/2 = 30 MeV, and its share of v² is f_π²/v² = 1.4×10⁻⁷ (one light doublet; heavier flavours do not change the order). This is the only SM instance of EWSB by quark-antiquark pairs, and it is 7 orders too small.

(b) t̄t (Bardeen-Hill-Lindner compositeness, PRD 41, 1647 (1990), doi:10.1103/PhysRevD.41.1647 [unverified, from memory]). Compositeness at Λ requires a y_t Landau pole at Λ.
- [computed, 1/2/3-loop, tools/rg_sm.py] SM y_t(μ) decreases monotonically: 0.933 (M_t), 0.436 (10¹⁵), 0.380 (M_Pl) at 3 loops. There is no pole, and λ(M_Pl) = −0.010.
- [computed, 1-loop] A pole at Λ = 10¹⁵ (10¹⁹) GeV needs y_t(M_t) = 1.331 (1.272), i.e. m_t ≈ 246 (235) GeV [approx: pole/MS-bar ratio held fixed]. BHL's figure is ~218 GeV at 10¹⁹ [from memory, unverified]. The measured 172.57 ± 0.29 GeV excludes it. The 2-loop search finds no pole below y_t(M_t) = 3. [conjecture: an artefact of the truncated 2-loop β; not checked]
- So the SM is not a t̄t-composite Higgs theory. Making it one needs new four-fermion or topcolor dynamics at Λ (BSM, A1). **Stop here per rules.**

## 4. What is new (R5)

- The quantitative statement that, for the observable where the SM does cancel a scalar's Λ² by partner states (π± EM mass), the cancellation is stronger than in soft SUSY (Λ² and ln Λ against Λ² only), with the sum-rule ↔ supertrace correspondence written as literal equalities (c1). [framing new as far as I know; DGMLY, WSR and soft-SUSY formulas are textbook; literature check needed]
- The explicit cutoff check that h/G0 form a chiral-partner pair with Λ²-free S − P (c2a), which localises the SM hierarchy problem exactly in the symmetric operator H†H. [content known; explicit side-by-side new to this repo]
- A uniform naturalness comparison (c2b): pion Λ_nat = 851 MeV with partners found at 775/1230 MeV. Higgs Λ_nat = 458 GeV (t̄t only) or 552 GeV (full Veltman bracket −8.22×10⁴ GeV²). The nearest partner-like bounds are 1.2-1.3 TeV (stop), so the ratio is ≈ 2.7 and a naive tuning of about 7. [approx: stop corrections are log, so this ratio is indicative only]
- Not new: BHL failure, Higgs not a QCD pGB, Quigg-Shrock. These are reproduced with repo tools.

## 5. SUSY results targeted

- #1: reproduced for π± (constructive, SM-only). Not reproduced for h's μ². Obstruction in §3, and lifting it needs BSM.
- #4: MSSM radiative EWSB is driven by y_t. The SM analogue (t̄t condensation) fails (§3b). The real SM q̄q-driven EWSB is a 1.4×10⁻⁷ effect (§3a). Not reproduced.
- #6: in the pion case partners were found where naturalness put them. For h, the SM has no partners beyond W/Z/h (L01b's partial cancellation), and LHC null results are consistent with the SM because the SM predicts no superpartners (C3 satisfied trivially). The pion mechanism does not explain the null results. It shows the contrast.

## 6. Open issues

- Literature check of the "stronger than soft SUSY" framing (likely discussed in composite-Higgs reviews, e.g. Contino 1005.4269; Panico & Wulzer arXiv:1506.01961 [unverified]).
- Verify all [unverified] references (DGMLY, Weinberg, BHL, CCL, Gaillard-Lee, CMS/ATLAS spin-parity).
- Beyond narrow resonances: test the WSRs with τ-decay spectral functions (ALEPH/OPAL). Not done here.
- The 2-loop y_t pole search is inconclusive (§3b).
- c2(a) uses a hard cutoff. In dim reg the common Λ² is absent and S − P is the same log (H2: the S − P statement is scheme-independent in content; the Λ² equality is a cutoff statement only).

## CONSTRAINTS checklist

- A1: pass. Uses only SM fields and QCD hadrons (π, ρ, a1, f0(500), all observed). Top condensation, topcolor and composite-Higgs sectors are named only as what would be needed (BSM) and are not used.
- A2: pass. No neutrino masses used.
- A3: pass. No reformulation used. The narrow-resonance saturation is an approximation to SM QCD spectral functions, labelled as such.
- B1-B10: pass. Particle and antiparticle masses are treated as equal (CPT). No CP violation used. No EDM or baryon-number effect enters.
- C1: m_h = 125.20 GeV used. C2: PDG 2024 via tools/sm_inputs.py. C3: addressed in §5 #6 and c2(b). C4: no g-2 claim.
- D: gauge inputs via tools; RG loop order stated (1/2/3 loop in c3; 1-loop pole search).
- E2-E4, E6-E10: not used, no cosmological claim. E10: §3a QCD EWSB is a T = 0 statement, not baryogenesis.
- F1-F3: not used. No B violation.
- G: Veltman bracket reproduced (−8.221×10⁴ GeV²). Dim-reg caveat in §6. Pauli-type sum rules (k = 0, 1) are the WSRs (§1).
- H1: no numerology. All numbers come from formulas derived in c1-c3. The 1.27 DGMLY ratio is reported as a model error, not tuned.
- H2: Λ² statements are cutoff statements. The finite DGMLY result and the log S − P are regulator-independent in content (dim reg gives the same finite and log parts) [conjecture for c2 beyond leading log; not computed in dim reg].
- H3: no interpretation (Dirac sea / FS) used.
- H4: calc/c1_pion_wsr.py, calc/c2_higgs_chiral_partners.py, calc/c3_top_compositeness.py, each with a committed _out.txt.
