# Investigation Prompt: Where the Muon g-2 Standard Model Prediction Went Wrong

You are a research agent investigating the history of the muon anomalous magnetic moment, a_mu = (g-2)/2. Your job is forensic: determine where the original Standard Model prediction diverged from experiment, and specifically what about the way hadronic (quark and gluon) contributions were brought in from experimental data produced the gap that the lattice QCD approach later closed.

You may spawn subagents for parallel literature reading, calculation, and adversarial review. You own the conclusions.

## Background to verify, not assume

The figures below are approximate starting points. Confirm every one against the primary source before relying on it, and correct this prompt in your report if any are wrong.

- Experiment: BNL E821 (2006), then Fermilab E989 (Run 1 in 2021, Runs 2-3 in 2023, final result in 2025 at ~127 ppb).
- 2020 Muon g-2 Theory Initiative White Paper (Aoyama et al., Phys. Rept. 887 (2020) 1, arXiv:2006.04822). Its SM prediction used the data-driven (dispersive) hadronic vacuum polarization (HVP), a_mu^HVP,LO ≈ 6931(40) x 10^-11, and disagreed with the experimental average by roughly 4 to 5 sigma, a gap of roughly 2.5 x 10^-9.
- BMW lattice collaboration (Borsanyi et al., Nature 593 (2021) 51, arXiv:2002.12347) computed a_mu^HVP,LO ≈ 7075(55) x 10^-11, much closer to what experiment needed.
- CMD-3 (2023) measured e+e- -> pi+pi- cross sections above previous experiments, consistent with lattice and in tension with KLOE, BaBar, and earlier CMD-2/SND data.
- 2025 White Paper update (arXiv:2505.21476) adopted lattice HVP and found the SM prediction consistent with experiment.

## What you are investigating

The SM prediction is a sum: QED + electroweak + hadronic (HVP leading order, HVP higher order, hadronic light-by-light, HLbL). Work through it in this order:

### 1. Rule out the non-hadronic parts

- QED through 5 loops (Aoyama, Kinoshita, Nio and others). Confirm it is computed to far better precision than the gap and has been cross-checked independently.
- Electroweak through 2 loops. Same check.
- Hadronic light-by-light: compare the 2020 data-driven/dispersive value with lattice values (RBC/UKQCD, Mainz). Determine whether HLbL could account for any meaningful part of the gap.

Show numerically that the gap lives in leading-order HVP. If it does not, say so and follow the evidence.

### 2. Reconstruct the data-driven HVP calculation

The dispersive approach computes HVP from the measured cross section sigma(e+e- -> hadrons) through the dispersion integral

a_mu^HVP,LO = (alpha^2 / 3 pi^2) ∫ ds K(s) R(s) / s

where K(s) is a known QED kernel that heavily weights low energies. Reconstruct this:

- Write and commit a script that evaluates the kernel K(s) and shows which energy ranges dominate the integral. Confirm that the pi+pi- channel in the rho region (roughly 0.6 to 0.9 GeV) is the largest single contribution.
- Identify the datasets that fed the 2020 combination for each channel, especially pi+pi-: KLOE (multiple analyses), BaBar, CMD-2, SND, BESIII, CLEO-c, and others.
- Identify the combination methods (DHMZ, KNT, and the 2020 merging procedure) and how they handled the known KLOE vs BaBar tension.
- Where public data allows (HEPData, published tables), recompute the pi+pi- contribution from individual experiments and show how much each one moves the total.

### 3. Locate the failure

Determine, with evidence, which of these (or what else) caused the data-driven HVP to come out low. Do not pick one in advance.

- **Experimental normalization or systematics** in specific pi+pi- measurements, particularly KLOE and the pre-CMD-3 Novosibirsk data.
- **Radiative corrections**: initial-state radiation (ISR) handling in the radiative-return method, final-state radiation (FSR) from pions modeled in scalar QED, vacuum polarization corrections to the measured cross sections, and the Monte Carlo generators used (PHOKHARA and others). Check whether any of these were known to be incomplete at the time.
- **The combination procedure**: how inconsistent datasets were merged, how error inflation was handled, and whether the quoted uncertainty underestimated the real spread.
- **Tau-decay data**: the alternative route using tau -> pi pi nu with isospin-breaking corrections. What it gave and why it was excluded from the 2020 average.
- **Lattice side**: whether the lattice result could instead be the one in error. Check BMW against independent lattice groups (RBC/UKQCD, Mainz, ETMC, Fermilab/HPQCD/MILC), especially the "intermediate window" quantity that several groups computed independently. A forensic answer has to check both sides.

### 4. Compare at the level of windows and energy regions

Use the Euclidean time window decomposition (short, intermediate, long distance) introduced by RBC/UKQCD to compare lattice and data-driven results piece by piece. Determine which window, and which corresponding energy range of R(s), holds the discrepancy. Commit the comparison as a script with its inputs and outputs.

### 5. Answer the question in plain terms

State:

1. Where the original prediction went wrong, as specifically as the evidence allows: which experiment(s), which energy range, which correction or procedure.
2. How much of the gap each identified cause accounts for, with uncertainties.
3. What remains unexplained. As of the latest literature, the CMD-3 vs KLOE/BaBar tension may still be unresolved. If so, say so. Do not invent a resolution.
4. Whether "the original deduction of the muon's magnetism" (QED, Schwinger term, the theory framework itself) was ever wrong, or whether the problem was confined to the hadronic data input.

## Deliverables

Before starting the investigation, create the repo with the `gh` CLI, authenticated as GitHub user `michaelClucas`:

```
gh repo create michaelClucas/muon-g2-forensics --public --clone
```

Write everything into that clone. Commit and push after each completed section (1 through 5), after review, and at the end, with messages like `section 2: dispersive HVP reconstruction`. Nothing should live only locally. Add a `README.md` with a short description, current status, and the headline finding once there is one.

Layout:

```
README.md          # what this repo is, status, headline finding
REPORT.md          # the answer, sections 1 to 5 above, with citations
TIMELINE.md        # dated sequence of experimental results, theory predictions, and the shifts between them
calc/              # every script used, with its inputs and outputs, runnable as-is
data/              # downloaded public datasets, with source URL and retrieval date for each
SOURCES.md         # every paper cited, with arXiv ID or DOI, and what was taken from it
REVIEW.md          # adversarial review notes (see below)
```

## Review

Before finalizing, spawn at least two independent reviewer subagents. Give them only `REPORT.md`, `calc/`, and `SOURCES.md`, not your reasoning. Ask each to find errors in the numbers, misattributed causes, and claims not supported by a cited source. Record their findings and your responses in `REVIEW.md`, and fix what they find.

## Rules

- No fabricated numbers, citations, or quotes. If you cannot verify something, label it unverified.
- Separate clearly what the literature has established, what is still disputed, and what is your own inference.
- Prefer primary sources (collaboration papers, the White Papers) over reviews and news coverage.
- Every number in `REPORT.md` either traces to a source in `SOURCES.md` or to a script in `calc/`.
- If the evidence shows the premise of this prompt is wrong somewhere, report that instead of forcing an answer.
- Only commit public datasets whose terms allow redistribution. For anything else, commit the source URL and a download script instead of the data.
