# STATE (overseer working memory)

**Current cycle:** 2 (cycle 1 complete and committed)
**Next wildcard due:** cycle 6

## How to resume (for a fresh overseer)
1. Read `OVERSEER_PROMPT.md` (the rules), this file, the tail of `LOG.md`, `scrap/INDEX.md`. Check for `STOP` at repo root.
2. Pick 3-6 spawns from the queue below. Explorers get `CONSTRAINTS.md` + `scrap/INDEX.md` + research question. Referees get ONLY the line folder path + `CONSTRAINTS.md` + `OVERSEER_PROMPT.md` scope section, never the explorer's summary or the overseer's opinion. Subagents write files but do not commit; the overseer commits.
3. Triage by reading the line files, not the summaries. Rerun calc scripts (`for f in lines/*/calc/*.py` from each calc dir) before promoting. Update this file, append `LOG.md`, update README status block, commit `cycle <n>: ...`, push.

## Overseer rulings
- R1 (cycle 1): Sexaquark / any hypothesized-but-unobserved SM bound state = "unobserved phenomenon" under CONSTRAINTS A1. Cannot be used in a mechanism. A line may discuss it only as a conditional appendix ("even if it existed, ...").
- R2 (cycle 1): Shared inputs now PDG 2024 throughout (`tools/sm_inputs.py`, α_em⁻¹ = 127.930). L02's unification.py prints its own PDG line with 59.014/29.594 (old α_em); shift is 0.01 in α⁻¹, immaterial, but calculators should make L02 import from tools/ before final verification.
- R3 (cycle 1): Veltman normalization convention documented in CONSTRAINTS G.

## Lines

| Line | SUSY # | Status | Gate progress |
|---|---|---|---|
| L01-weisskopf-hierarchy | 1, 4 | VERIFICATION (negative result) | calcs run (cycle 1); referees 0/3; lit check pending; constraints section written by explorer, needs overseer check |
| L02-unification-virtual-pairs | 2 | VERIFICATION (negative result) | calcs run; referees 0/3; lit check pending |
| L03-sm-antimatter-dark-matter | 3 | VERIFICATION (negative result) | calcs run; referees 0/3; lit check pending |
| L04-dirac-sea-vacuum-energy | 5 | VERIFICATION (negative result) | calcs run; referees 0/3; lit check pending. Known prior: Alberghi et al. arXiv:0804.4782; must show what is new |
| LW1-antiquark-diquark-susy | 6 (and neg. #1) | CONTINUE, low priority | needs lit check + 1/m_c correction calc; likely ends as context, not a result |

Uncovered: SUSY #6 (null results) has no dedicated line; every negative-result line must state explicitly how it squares with C3. Consider a synthesis line once ≥2 negative results pass.

Gate item 7 (falsifiable prediction / consistency check) candidates already in the lines:
- L01: Veltman zero at 10^22.8 GeV; zero at M_Pl requires M_t ≈ 169.4 GeV (testable via m_t precision).
- L02: needed α_s(MZ)=0.074 vs measured 0.118; R-ratio and Δα_lep checks of antiparticle counting.
- L03: CMB baryon-loading R if DM were antibaryonic (3.96 vs 0.62).
- L04: Str m⁴ = 0 would require m_t = 87.5 GeV.

## Queue (cycle 2)
1. Referee #1 for each of L01, L02, L03, L04 (4 spawns)
2. Literature checker A: L01 + L04; Literature checker B: L02 + L03 (2 spawns)
Cycle 3: referees #2 (and any fixes); cycle 4: referees #3. Then gate decision per line.
Later: LW1 lit check + calculator.

## Open issues carried from explorers
- L01: runner gives m(M_Pl)=139.4 GeV vs Buttazzo 129.4 (not load-bearing); Weisskopf 1939 detail unverified.
- L02: Weisskopf 1936 and Pati-Salam citations unverified.
- L03: Farrar-Zaharijas C/CP argument is from abstract only; 2404.12094, 2603.16686 unread.
- L04: running is 1-loop only; CCM coefficients not checked against primary text.
