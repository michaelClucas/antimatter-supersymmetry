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
**Cycle 4 complete (2026-11-25).** No verified results yet. Dark matter removed from scope by the experimenter.

- **L01b (Higgs mass, main thread):** The SM's boson pair loops (W sector, Z sector + Higgs) carry the stop-like sign and cancel a gauge- and regulator-independent fraction of the top/antitop loop: 34% at the weak scale, 79% at the Planck scale, 100% only at 10²²·⁸ GeV. No SM symmetry enforces the match; the obstruction is that scalars carry no chirality. In fix round.
- **L05 (beta functions, in verification):** Theorem: under minimal SUSY completion every mixed two-loop gauge beta coefficient (and the abelian diagonal) exactly doubles, in any gauge theory. Not found in the literature. It does not single out antimatter: counting each state's CP conjugate separately gives the same numbers as any duplicate copy. Answer to "is there an antimatter-SUSY beta-function isometry?": no antimatter-specific one.
- **LW1 (hadronic SUSY):** QCD's antiquark↔diquark symmetry is internal (its anticommutator has no momentum), so it cannot protect masses the way SUSY does; it does protect partner mass differences (96% cancellation of SU(3) breaking).
<!-- STATUS:END -->

Every file distinguishes established physics, conjecture and speculation. Subagent output is a claim until a referee and a calculation back it.
