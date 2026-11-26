# Referee D (cycle 7) - numbers, reproducibility, constraint checklist

Formed without reading REVIEWS*.md or LITCHECK.md.

## Verdict: MINOR ISSUES ONLY

No fatal error, no BSM content found in my scope (gate items 3 and 4). Every script reruns and reproduces its committed output byte for byte (whitespace-normalized). Every headline number was recomputed independently in `calc/refD_check.py` (output `calc/refD_check_out.txt`) and agrees.

## Reproducibility (gate 3)

- All 13 scripts in `calc/` were run from inside a scratch copy of `calc/` (so committed outputs were not overwritten), with a 600 s timeout. All exit 0. `diff -w` against each `*_out.txt`: 0 differing lines for all 13.
- L01 scripts used by reference (`cw_radiative_ewsb.py`, `higgs_top_ofpt.py`, `veltman_running.py`, `weisskopf_ofpt.py`, `rg_sm.py` validation): all rerun, 0 differing lines.
- Numbers quoted in WORK.md were grepped against the outputs. All were found, to rounding, including 22.83, 22.98, 26.79, 0.0203, 0.344, 0.790, 0.211, 29.9, 169.535, 0.74, the 4.1/3.7/3.3/2.9σ table, 30.1, 52.1, 1.40e-7, 5.6 keV, 2674, B = -4.39e-3, 88.5, the §5a table, the §5c table (16.11, 15.68, 24.18, 24.29, 17.06, 17.07, 23.46, 0.9005, 0.9042, 0.9153, 16.29, 21.06), R4 0.138/0.3447/0.7665/1.113/18.19, R(M_t) ≈ 0.37 with Jegerlehner couplings (0.366/0.368), and 2.5e-16.

## Independent recomputation (`calc/refD_check.py`)

Inputs come only from `tools/sm_inputs.py` and `tools/rg_sm.py` (`couplings_at_mt`, `run`). Sector formulas, R, crossings, M_t*, the budget, d = 2 counting, CW, QCD and β_C were written from scratch, plus a separate 1-loop RGE integrator.

| quantity | WORK | mine |
|---|---|---|
| W sector 3/2 g² + 2λ at M_t | 0.882 | 0.8815 |
| Z+h 3/4(g²+g'²) + 4λ at M_t | 0.916 | 0.9156 |
| fermions 6y_t² + 6y_b² + 2y_τ² | 5.223 | 5.2231 |
| R(M_t), R(10^10), R(10^16), R(M_Pl) | 0.344, 0.508, 0.667, 0.790 | 0.3441, 0.5079, 0.6667, 0.7898 |
| μ₀ (C = 0), 3/2/1-loop | 22.83 / 22.98 / 26.79 | 22.832 / 22.98 / 26.79 |
| μ₀ 1-loop, my own β functions | 26.79 | 26.79 |
| dC/dlnμ at μ₀ | +0.0203 | +0.0203 |
| d = 2 pole (n_V = 1) R(M_t) | 0.211 | 0.2113 |
| n_V = 1 crossing | none below 10^29.9 | none up to 10^31.9 (max C = -0.079) |
| M_t* for C(M_Pl) = 0 | 169.54 | 169.535 |
| α_s ± 0.0009, M_h + 0.11, 2- vs 3-loop shifts of M_t* | 0.42, 0.04, 0.13 | ±0.418, +0.037, -0.125 |
| significance at Δy_t = 0.0005 / 0.003 / 0.004 | 4.1 / 3.3 / 2.9σ | 4.07 / 3.31 / 2.94σ |
| σ(tt̄) pole mass 172.4 ± 0.7, Δy_t = 0.003 | 2.9σ | 2.87σ |
| one-loop 16π²β_C on C = 0 (S5) | polynomial in S5 | identical (sympy difference 0) |
| CW B (μ² = 0, W, Z, t) | -4.4e-3 | -4.387e-3 |
| top threshold, W,Z-only m_h (L01) | 78.6, 9.8 GeV | 78.6, 9.78 GeV |
| tree μ | 88.5 GeV | 88.53 GeV |
| QCD M_W, n_d = 1 / 3 | 30.1 / 52.1 MeV | 30.06 / 52.07 MeV |
| f_π²/v², ΔM_W, v/f_π | 1.4e-7, 5.6 keV, ~2700 | 1.399e-7, 5.62 keV, 2673 |

The normalization identity C = 6λ + 9/4 g² + 3/4 g'² − 6y_t² = (3/v²)(m_h² + 2M_W² + M_Z² − 4m_t²) holds algebraically at tree level. Numerically, the pole-mass form gives −4.07 against −3.43 from MS-bar couplings at M_t. The line uses MS-bar throughout, which is correct.

## Constraint checklist (gate 4)

CONSTRAINTS IDs: A1-A3, B1-B10, C1-C4, D, E1-E10, F1-F3, G, H1-H4. All are addressed in WORK §10 except E1 and E5 (finding 2). The statements I checked are correct. A1: superpartners appear only as a comparison target. A2: the m_ν²/v² bound is mechanism independent. B: no particle/antiparticle asymmetry is used. C3: the absence of superpartners is stated explicitly. D: loop orders are stated. E10: untouched. H2: R is honestly labelled scheme dependent. H4: 13 scripts, all reproduce.

## Findings

1. **Minor - CLAIM item 6 and §7, QCD-condensate EWSB.**
   - "A factor of about 2700 too low in the condensate scale" is v/f_π for n_d = 1. For the n_d = 3 variant quoted in the same sentence it is about 1540.
   - The 52 MeV figure holds f_π at its physical 92.1 MeV in a world with six massless flavours. The chiral-limit f is about 86-87 MeV for two flavours and differs again for N_f = 6. It is tagged [approx] in §7 but not in the CLAIM.
   - Quigg-Shrock (PRD 79, 096002; arXiv:0901.3958) is confirmed as a real paper on exactly this mechanism, but only the abstract was verified. The numbers are the line's own.
   - Fix: say "2700 (n_d = 1), 1500 (n_d = 3)", and carry [approx] for 52 MeV into the CLAIM.
2. **Minor - §10 checklist omits E1 and E5.**
   - The header says "dropped per D1". STATE.md D1 removes SUSY #3 (dark matter) as a target. It does not remove CONSTRAINTS entries, and gate 4 requires every entry to be addressed in writing.
   - Fix: add "E1, E5: not applicable; no dark-matter claim (D1)".
3. **Minor - C2, PDG 2026 inputs not mentioned.**
   - CONSTRAINTS C2 lists PDG 2026 values: m_t = 172.60(27), M_W = 80.3625(77), m_H = 125.13(11). At 1.2 dec/GeV and 0.42 GeV per 0.0009 in α_s these shift M_t − M_t* by about +0.03 GeV and +0.02 GeV (from m_H), well inside the budget.
   - Fix: one sentence in the C1/C2 checklist entry.
4. **Minor - Jegerlehner attribution, §5c and §8.**
   - WORK attributes μ₀ ≈ 1.4×10^16 to 1304.7813 (Table 1) and ≈ 7×10^16 to 1305.6652.
   - The DESY/arXiv abstract of 1304.7813 itself quotes μ₀ ∼ 7×10^16 GeV.
   - Either the abstract and Table 1 of 1304.7813 differ, or versions differ. WORK should say so, so a reader does not take 7×10^16 to be specific to 1305.6652. Conclusions are unaffected: 10^16-10^17 either way.
5. **Minor - F-b significance is partly a choice.**
   - The 3.3σ lower end rests on an ad hoc Δy_t = 0.003, and the 0.5 GeV MC-mass row is an estimate.
   - The arithmetic is right (reproduced). The text already says Jegerlehner's matching (Δy_t = −0.038) is excluded from the budget, and that C(M_Pl) = 0 is not excluded there.
   - Fix: none strictly needed. Optionally state that "3.3-4.1σ" is conditional on two judgement calls (the Δy_t range and the MC term).
6. **Trivial - rounding.**
   - "3.04 GeV above" (§5b): the script prints 3.03; the exact value is 3.035.
   - §5a W sector at 10^16 is 0.3925 (WORK 0.393; refA output 0.392). Harmless.
7. **Note - the S1 deviation is quoted inconsistently**: "2×10⁻¹⁶" in the CLAIM, "2.5×10⁻¹⁶" in §4a and the output. Use one value.

## Citation spot-checks (web search)

- Quigg & Shrock PRD 79, 096002 (2009), arXiv:0901.3958: correct.
- Jegerlehner Acta Phys. Polon. B 45, 1167 (2014), arXiv:1304.7813: correct (see finding 4).
- Kleppe hep-th/9209124, "Regularization dependence of quadratic divergence cancellations", VPI-IHEP-92/10: correct, including its dispute with Al-sarhi-Jack-Jones.
- Al-sarhi, Jack, Jones, Z. Phys. C 55, 283 (1992) and NPB 345, 431 (1990): confirmed as cited by later papers.
- Bardeen FERMILAB-CONF-95-391-T: exists (cited in arXiv:1307.7879). Content not verified, as WORK says.
- Coleman-Mandula, HLS, HKO, Masina-Quiros, Buttazzo, Bednyakov et al., Beneke et al. and Hoang have standard references matching my knowledge. Buttazzo's y_t fit coefficients and ±0.00050 theory error in `tools/rg_sm.py` match my recollection of eq. (60).
