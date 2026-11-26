# Antimatter x Supersymmetry: a free-range agent experiment

> **Verified results (cycle 10, 2026-11-25).**
> 1. **Higgs mass (SUSY #1, #4), negative** ([results/L01b-self-conjugate-higgs](results/L01b-self-conjugate-higgs/SUMMARY.md)). SM antimatter reproduces the structure of SUSY's cancellation (boson pair loops cancel 34% of the top/antitop Λ² term at M_t, 79% at M_Pl) but nothing in the SM enforces it. Every antimatter operation preserves spin, so none can tie y_t to the boson couplings the way SUSY does. Antimatter also cannot act as a twin-Higgs partner: H^c = iσ₂H* is a function of H, so |H|² + |H^c|² = 2|H|² and nothing cancels. Strong argument, not a formal proof.
> 2. **Beta functions (SUSY #2, experimenter question D4), exact map but not an antimatter map** ([results/L05-beta-function-map](results/L05-beta-function-map/SUMMARY.md)). Two-loop off-diagonal gauge coefficients double exactly under SUSY completion of a one-doublet theory (b_ij^MSSM = 2 b_ij^SM). Gauge coefficients cannot tell a conjugate field from a duplicate, so antimatter is not load-bearing.
>
> Gate item 7 was met by a retrodiction (L01b) and a mathematical consistency check (L05), per experimenter ruling D6, not by a new prediction.

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
**Cycle 10 complete (2026-11-25). Gate passed by L01b and L05; experiment halted per the halt condition.** Dark matter removed from scope by the experimenter.

- **L01b + L01 (Higgs mass, #1 and #4):** verified negative result, see `results/`.
- **L05 (beta functions, #2):** verified doubling theorem, antimatter-blind, see `results/`.
- **LW1 (hadronic SUSY):** parked as context. QCD's antiquark↔diquark supercharge protects mass differences, not masses ([H,Q] ≠ 0). Predicts Ξ_cc*−Ξ_cc = 107 ± 32 MeV (unmeasured).
- **LW2 (pion EM mass):** support only. ρ, a₁ (q̄q states) cancel the pion's EM mass divergence via Weinberg sum rules; known result, needs compositeness.
- **Scrapped:** L02, L04 (restatements), L03 (out of scope), S1 (stopped). See `scrap/INDEX.md`.
- **Not addressed by any line:** #5 beyond the scrapped L04 restatement; #6 (an SM-only account trivially predicts no superpartners).
<!-- STATUS:END -->

Every file distinguishes established physics, conjecture and speculation. Subagent output is a claim until a referee and a calculation back it.
