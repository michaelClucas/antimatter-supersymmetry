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
**Cycle 6 complete (2026-11-25).** No verified results yet. Dark matter removed from scope by the experimenter.

- **L01b (Higgs mass, main thread):** SM boson pair loops cancel 34% of the top/antitop loop at the weak scale, 79% at the Planck scale (cutoff/Pauli-Villars). Referees agree no SM symmetry enforces full cancellation; the precise obstruction is that every SM antimatter operation (C, CP, CPT) maps a particle to an antiparticle of the same spin, so nothing ties boson couplings to the top Yukawa the way SUSY does. Fix round 3.
- **LW2 (new, positive match):** the SM does contain an antimatter-built protection of a scalar mass. The charged pion's electromagnetic mass divergence is cancelled by quark-antiquark partner states (ρ, a₁) through the Weinberg sum rules, removing both the quadratic and log divergence, and the partners sit where naturalness says (851 MeV estimate vs 775/1230 MeV). It works for composite scalars; extending it to the elementary Higgs needs new physics.
- **L05 (beta functions, in verification, 1/3 referees clean):** two-loop mixed gauge coefficients double under SUSY completion of a one-doublet theory; checked against four published table pairings. No antimatter-specific map exists.
- **LW1 (hadronic SUSY, in verification):** QCD's antiquark↔diquark supercharge does not commute with the Hamiltonian, so it protects no mass. Predicts Ξ_cc*−Ξ_cc = 107 ± 32 MeV.
<!-- STATUS:END -->

Every file distinguishes established physics, conjecture and speculation. Subagent output is a claim until a referee and a calculation back it.
