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
**Cycle 3 complete (2026-11-25).** No verified results yet. Dark matter removed from scope by the experimenter.

Main thread (L01b): SUSY's Higgs-mass protection is a cancellation of the top/antitop pair loop against stop/antistop pairs, sector by sector (self-conjugate bosons against Majorana neutralinos, charged pairs against charginos). The SM's own boson pairs (W⁺W⁻, Goldstones, Z, h) have the right sign and structure and cancel 34% of the top loop at the weak scale, 79% at the Planck scale, but couple ~3x too weakly, and no SM symmetry enforces the match. Exact match at the Planck scale would need m_t ≈ 169.5 GeV (measured 172.57).

Beta functions (L05): writing the SM in the antimatter (conjugate-field) basis and mapping fields to supermultiplets gives the MSSM; every off-diagonal two-loop gauge beta coefficient exactly doubles. Being checked for novelty.

LW1: QCD's antiquark-diquark supersymmetry; predicts Ξ_bb* − Ξ_bb = 30 ± 4 MeV (unmeasured).
<!-- STATUS:END -->

Every file distinguishes established physics, conjecture and speculation. Subagent output is a claim until a referee and a calculation back it.
