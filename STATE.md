# STATE (overseer working memory)

**Current cycle:** 1 (in progress: 6 subagents spawned 2026-11-25)
**Next wildcard due:** cycle 6

Cycle 1 spawns (if overseer context was lost mid-cycle, check which folders exist and re-spawn missing ones):
- Explorer+calc L01-weisskopf-hierarchy (SUSY #1, #4)
- Explorer+calc L02-unification-virtual-pairs (SUSY #2)
- Explorer+calc L03-sm-antimatter-dark-matter (SUSY #3)
- Explorer+calc L04-dirac-sea-vacuum-energy (SUSY #5)
- Wildcard LW1-* (own choice)
- Literature checker on CONSTRAINTS.md -> CONSTRAINTS_LITCHECK.md

## How to resume (for a fresh overseer)
1. Read `OVERSEER_PROMPT.md` (the rules), this file, the tail of `LOG.md`, `scrap/INDEX.md`. Check for `STOP` at repo root.
2. Pick 3-6 spawns from the queue below. Explorers get `CONSTRAINTS.md` + `scrap/INDEX.md` + research question. Referees get ONLY the line's files (path), never the explorer's framing. Subagents write files but do not commit; the overseer commits.
3. Triage by reading the line files, not the summaries. Update this file, append `LOG.md`, update README status block, commit `cycle <n>: ...`, push.

## Active lines
(none yet)

## Queue
- Verify every [uncertain] citation in CONSTRAINTS.md (literature checker)
- Open lines for: hierarchy problem, gauge unification, dark matter, vacuum energy (all SUSY results 1-6 need at least one line)

## Verification progress
(none)
