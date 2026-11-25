# Antimatter x Supersymmetry: a free-range agent experiment

**Question.** Can antimatter physics, restricted strictly to Standard Model content, explain the results attributed to supersymmetry (SUSY), either replacing SUSY or reproducing its successes through a different mechanism?

The SUSY "results" under test:
1. Higgs mass stability against quadratic divergences (hierarchy problem)
2. Gauge coupling unification near 10¹⁶ GeV
3. A stable dark matter candidate
4. Radiative electroweak symmetry breaking
5. Boson/fermion vacuum-energy cancellation (and SUSY's failure on the cosmological constant)
6. The LHC null results for superpartners

A rigorous negative result (SM antimatter provably cannot reproduce a given SUSY result) counts as a finding.

## How it runs

An overseer agent runs cycles. Each cycle it spawns 3-6 subagents (explorers, calculators, adversarial referees, literature checkers, an occasional unsteered wildcard), reads what they commit, and triages every line: continue, promote to verification, or scrap. Nothing is deleted; dead ideas go to `scrap/` with a cause of death.

## How to read the repo

| Path | What it is |
|---|---|
| `CONSTRAINTS.md` | Scope rules (SM-only) and the experimental/theoretical constraints every idea must survive |
| `STATE.md` | Overseer's working memory: active lines, queue, cycle count |
| `LOG.md` | Append-only, one entry per cycle |
| `lines/<id>/` | Active lines: `PROPOSAL.md`, `WORK.md`, `calc/`, `REVIEWS.md` |
| `results/` | Lines that passed the verification gate |
| `scrap/` | Everything that died, with `CAUSE_OF_DEATH.md`; `scrap/INDEX.md` lists them |
| `tools/` | Shared scripts (SM inputs, RG running) |
| `OVERSEER_PROMPT.md` | The full instructions the overseer runs under |

## Verification gate (summary)

A line becomes a result only if: it makes a specific claim about a SUSY result; uses only SM content; every number has a committed runnable script; it addresses every item in `CONSTRAINTS.md`; three fresh referees fail to break it; a literature check finds it new or adds something new; it makes a falsifiable prediction or consistency check.

## Status

<!-- STATUS:BEGIN -->
**Cycle 2 complete (2026-11-25).** No verified results yet.

Four candidate **negative** results (L01 hierarchy/EWSB, L02 unification, L03 dark matter, L04 vacuum energy) each survived their first adversarial referee without a fatal error, but each had fixable major issues and each largely restates known literature. They are in a fix round. A synthesis line (S1) will test whether the antimatter-specific pieces add something new: whether any SM-equivalent treatment can reweight antiparticle contributions, and whether the boson/fermion sign SUSY relies on comes from spin-statistics rather than charge conjugation.
<!-- STATUS:END -->

Every file distinguishes established physics, conjecture and speculation. Subagent output is a claim until a referee and a calculation back it.
