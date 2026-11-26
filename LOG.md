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

## Cycle 5, 2026-11-25 (attempt 1 failed)
- Spawns: fixer L01b, referee 1 L05, referee 1 LW1. All three stalled (stream watchdog, no progress 600s), no files written. Re-spawned.

## Cycle 5, 2026-11-25 (attempt 2)
- Spawns (3, re-run after stall): fixer L01b round 2; referee 1 L05; referee 1 LW1.
- L01b: all c4 referee + lit items fixed; Jegerlehner discrepancy resolved (y_t matching). → verification, fresh referees.
- L05: referee 1 MINOR ONLY (first clean referee in the experiment). Theorem scope narrower (needs one-doublet parent). → fixer, then referees 2-3.
- LW1: referee 1 MAJOR fixable (wrong reason for no protection; census 30/40; missing control). → fixer.
- Also: an unrelated local file (MUON_G2_PROMPT.md) was committed by mistake in cycle 4 and untracked in cycle 5 (still in history).
- Status: no verified result. L05 1/3 referees clean.

## Cycle 6, 2026-11-25
- Spawns (5): referees A, B for L01b; fixer L05; fixer LW1; wildcard (→ LW2-chiral-partner-protection).
- L01b: both referees MAJOR (no fatal). Key correction: obstruction is absence of a boson↔fermion symmetry (antimatter operations preserve spin), not "no scalar chirality". → fix round 3.
- L05: fixed; consistency check against 4 published table pairings passes. → referees 2, 3.
- LW1: fixed ([H,Q]≠0 quantified; control shows SU(3) cancellation is not superflavor evidence). → referee 2.
- LW2 (new): first positive SM-antimatter match — pion EM mass protected by q̄q partners (ρ, a1) via Weinberg sum rules, more completely than soft SUSY; Higgs μ² not protected without BSM compositeness. → lit check.
- Status: no verified result. L05 1/3 clean referees.

## Cycle 7, 2026-11-25
- Spawns (5): fixer L01b round 3; referees 2, 3 for L05; referee 2 for LW1; lit check LW2.
- L01b: reframed around same-spin antimatter operations + CM/HLS; all c6 items addressed. → 3 fresh referees.
- L05: R2 minor, R3 major (claim (b) only proven for gauge coefficients; Yukawa/anomaly distinguish H^c; gate-7 near-circular). Gate item 5 passes by letter (no fatal, no BSM across 3 referees) but promotion held for narrowing fix.
- LW1: referee 2 major fixable. LW2: nothing new → support only.
- Status: no verified result.
