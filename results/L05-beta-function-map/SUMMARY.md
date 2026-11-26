# L05 SUMMARY: beta-function map between SM and SUSY (verified, cycle 10)

**SUSY result addressed:** #2 gauge coupling unification. Experimenter question D4: is there an isometry or other structure-preserving map between "antimatter" beta functions and SUSY beta functions?

## Finding

1. **Doubling theorem** [established, new per LITCHECK.md]. For a gauge theory T with at most one U(1), let Φ*(T) be the SUSY completion with one vector multiplet per gauge factor, one chiral multiplet per Weyl fermion and per real scalar, and two chiral multiplets per complex scalar. Then every off-diagonal two-loop gauge coefficient and the abelian diagonal one double exactly: b_ij[Φ*(T)] = 2 b_ij[T]. Mechanism: per field, a Weyl fermion contributes 2·S·C, a complex scalar 4·S·C, a chiral multiplet 4·S·C.
   - SM corollary: with one Higgs doublet, Φ*(SM) is the MSSM, so b_ij^MSSM = 2 b_ij^SM on i ≠ j and (1,1).
   - Scope: it needs minimal SUSY completion = Φ*. Counterexamples: 2HDM parent (3/2, 199/104), vector-like scalar pair (1), SM + complex (8,3,0) (18/17), and others in `calc/c6_scope.py`, `calc/c8_scope.py`.
2. **Negative for D4** [established]. Gauge coefficients b_i, b_ij depend on fields only through spin, S(R) and C(R), and S(R̄) = S(R), C(R̄) = C(R). So adding conjugate fields is indistinguishable from adding duplicate fields. No map judged by these coefficients can be an antimatter map. At three loops the same holds only in the two exact cases (conjugating a complex scalar, conjugating everything); the proper-subset case is a conjecture.
3. **Where the conjugate does matter** [established]. The SM writes the up Yukawa with H and the down/lepton Yukawas with H^c = iσ₂H*, which is the MSSM H_u/H_d pattern. Holomorphy and anomaly cancellation make "conjugate vs duplicate" a real distinction in SUSY. In the Yukawa beta functions there is no exact identity: fermion-leg terms double, the Higgs-leg sum splits exactly into γ(H_u) + γ(H_d), and the SM vertex term (−2y_b² in β_yt) tracks one doublet in both Yukawas (also in type-I 2HDM). Two-loop g⁴ ratios are non-uniform.

**Answer to D4:** yes, there is an exact structure-preserving relation (the factor-2 doubling of b_ij), but it is a property of how SUSY multiplets are built from SM fields. Antimatter is not load-bearing in it.

## Gate

| Item | Status |
|---|---|
| 1 specific claim | pass (CLAIM in WORK.md) |
| 2 SM-only | pass; the MSSM appears only as the comparison target, never as a mechanism |
| 3 runnable scripts | pass; all `calc/*.py` exit 0 (cycle 10 rerun; `referee2_check.py` excluded, >300 s) |
| 4 CONSTRAINTS | pass (checklist in WORK.md) |
| 5 three referees | pass; REVIEWS.md, REVIEWS_2.md, REVIEWS_3.md, REVIEWS_4.md: no fatal error, no BSM |
| 6 novelty | pass; LITCHECK.md: doubling theorem not found in print |
| 7 falsifiable check | **met by a mathematical consistency check only**: SM diagrammatic two-loop tables (Machacek-Vaughn) vs SUSY NSVZ-derived MSSM tables reproduce the doubling. Referee 4 notes only an arithmetic slip could fail it. Accepted under experimenter ruling D6 (cycle 10). No physical prediction. |

Files: `WORK.md` (full derivation, referee responses), `calc/` (all numbers), `REVIEWS*.md`, `LITCHECK.md`.
