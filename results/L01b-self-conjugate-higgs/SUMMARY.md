# L01b SUMMARY: SM antimatter cannot reproduce SUSY's Higgs-mass protection (verified, cycle 10)

**SUSY results addressed:** #1 hierarchy (Higgs mass protection), #4 radiative EWSB. Tests the experimenter's hypothesis (D2): the Higgs is its own antiparticle, its Yukawa coupling acts symmetrically on L and R fermions, and bosons have no chirality, so an antimatter analogue of Weisskopf's protection might hold. L01-weisskopf-hierarchy (in `results/`) is merged in by reference.

## Finding (negative; a strong argument over the known mechanism classes, not a formal proof)

1. **Structure matches, magnitude does not** [computed]. SM boson pair loops (W, Z, h) cancel part of the top/antitop Λ² term with the SUSY-like sign: 34% at M_t, 79% at M_Pl. The sector fractions are gauge- and regulator-independent.
2. **No SM symmetry enforces the cancellation.** Every SM antimatter operation (C, P, T, CP, CPT, Dirac-sea and Feynman-Stueckelberg readings) preserves spin, so none can tie y_t to λ, g as SUSY's λ_{Ht̃t̃} = y_t² does. The only spin-changing symmetry algebra is SUSY (Coleman-Mandula, HLS), which needs new states. Every element of the SM Lagrangian's symmetry group acts diagonally on the couplings in the Veltman coefficient C (complete for continuous linear internal symmetries); gauge invariance, pNGB, Gildener-Weinberg, BRST, worldline SUSY and scale invariance are each checked and excluded or outside the claim.
3. **Antimatter cannot be the twin partner** [computed; new per LITCHECK_2.md]. Same-spin (twin-Higgs) protection needs an independent partner doublet. The SM's conjugate doublet H^c = iσ₂H* is a function of H: gauge-invariant Higgs bilinears span 1 dimension (|H|² + |H^c|² = 2|H|², H^c†H ≡ 0) against 4 for an independent pair. H ↔ H^c is C composed with an SU(2) element (custodial SU(2)_R), already a symmetry of the SM, and it cancels nothing.
4. **On the hypothesis's three points:** self-conjugacy of h gives no extra protection (|φ|² is invariant for complex scalars too); the L↔R-symmetric coupling does not relate y_t to boson couplings; bosons lacking chirality is why no chiral symmetry protects their mass.
5. **#4 radiative EWSB:** β(m²) ∝ m² at every loop order in the SM, so m² cannot change sign under running; Coleman-Weinberg breaking would need m_t < 79 GeV and gives m_h ≈ 10 GeV; QCD-condensate EWSB gives m_W ≈ 30 MeV.

## Numbers
- C(M_t) = −3.43 ± 0.43 (MS-bar, 8.0σ) and −4.07 ± 0.47 (pole form, 8.7σ) with the conservative y_t matching spread; 4.4σ / 5.1σ with the scheme difference added as a systematic. d = 2 regulator: −4.12.
- C(μ) < 0 on [M_t, M_Pl]; single zero at 10^22.83 GeV (slope +0.0203, Buttazzo matching) or 10^16.15 GeV (slope +0.0240, Jegerlehner matching).

## Gate

| Item | Status |
|---|---|
| 1 specific claim | pass |
| 2 SM-only | pass; SUSY and twin Higgs appear only as targets |
| 3 runnable scripts | pass; all `calc/*.py` exit 0 from `results/` (cycle 10) |
| 4 CONSTRAINTS | pass (§10 checklist; DM items N/A by D1) |
| 5 three referees | pass; referees F, G, H (cycle 10) plus 1, A-E: none fatal, no BSM |
| 6 novelty | pass for the H^c non-independence argument (LITCHECK_2.md); the rest assembles known results. Citations verified (LITCHECK_3.md) |
| 7 falsifiable check | **met by a weak retrodiction only**: an exact enforcing symmetry would give C ≡ 0 at all scales; the measured C runs with one transverse zero. Cannot distinguish no symmetry from an approximate symmetry broken hard. Accepted under experimenter ruling D6 (cycle 10). |

Files: `WORK.md` (CLAIM at top, all referee responses), `calc/`, `REVIEWS*.md`, `LITCHECK*.md`.
