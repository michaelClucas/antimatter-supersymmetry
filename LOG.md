# LOG (append-only)

## Cycle 0, 2026-11-25
- Repository created, structure scaffolded, `CONSTRAINTS.md` written (items tagged [uncertain] await literature check).
- Shared tool `tools/sm_inputs.py` added.
- Status: ready for cycle 1.

## Cycle 1, 2026-11-25
- Spawns (6): explorer+calc L01-weisskopf-hierarchy, L02-unification-virtual-pairs, L03-sm-antimatter-dark-matter, L04-dirac-sea-vacuum-energy; wildcard LW1-antiquark-diquark-susy; literature checker on CONSTRAINTS.md.
- Lit check: 47 confirmed, 10 corrected, 3 unverified (CONSTRAINTS_LITCHECK.md). Corrections applied; added B9 (LHCb baryon CPV), B10 (nEDM), F3 (n-nbar). α_em⁻¹(MZ) corrected 127.951 → 127.930; all calc scripts rerun (all exit 0).
- Ruling R1: sexaquark = unobserved phenomenon, out of scope for mechanisms.
- Triage: L01, L02, L03, L04 → promote to verification (all negative results). LW1 → continue (low priority). Nothing scrapped.
- Status: four candidate negative results (SUSY #1/#4, #2, #3, #5) entering referee rounds.

## Cycle 2, 2026-11-25
- Spawns (6): referee #1 for L01, L02, L03, L04; literature checkers (L01+L04), (L02+L03).
- Referees: all four MAJOR ISSUES (fixable), no fatal errors, central negative claims hold, all scripts reproduce.
- Lit checks: all four lines restate known work (details in each LITCHECK.md); several citations corrected.
- Overseer: CONSTRAINTS G Veltman note corrected (δμ² vs δm_h²). Rulings R4 (lepton asymmetry as bounded input), R5 (gate item 6 requires "What is new").
- Triage: L01-L04 back to CONTINUE for fix round. LW1 continue. Planned synthesis line S1. Nothing scrapped.
- Status: no line has passed referee round 1 cleanly; fix round next.

## Cycle 3, 2026-11-25
- Experimenter directives D1-D5 received mid-cycle (dark matter out; focus L01; match antimatter to SUSY rather than statistics framing; pursue beta-function map; LW1 relevant). S1 and L03 fixer stopped.
- Spawns (8 total): fixers L01, L02, L04 (L03 fixer stopped); S1 explorer (stopped, nothing written); LW1 lit check + subleading calc; new explorers L01b-self-conjugate-higgs, L05-beta-function-map.
- All new calc scripts rerun by overseer (exit 0).
- Triage: L01b → continue (top priority). L01 → continue as support. L05 → continue (candidate novelty: two-loop off-diagonal b_ij doubling, checked by overseer against standard tables). LW1 → continue. L02, L03, L04 → scrap (restatement / out of scope).
- Status: no verified result. Main thread: does SM antimatter (self-conjugate h, charged pairs, top sea) reproduce SUSY's Higgs-mass cancellation? Structure yes, magnitude and symmetry no so far.

## Cycle 4, 2026-11-25
- Spawns (5): referee 1 L01b; calculator L01b (R_ξ + regulator); lit check L01b+L05; explorer/calc L05 (derive doubling); explorer LW1 (constructive extension).
- All c4/c5 scripts rerun by overseer (exit 0).
- Results: L01b fractions are gauge- and regulator-independent at sector level (0.344 at M_t, 0.790 at M_Pl); referee found MAJOR fixable issues. L05 doubling is a general theorem of minimal SUSY completion, new per lit check, but antimatter-blind. LW1: hadronic SUSY is internal (no P in {Q,Q†}), so cannot protect masses; protects mass differences.
- Triage: L05 → verification (negative result for D4 + new theorem). L01b → fix round. LW1 → continue (referee next).
- Status: no verified result.
