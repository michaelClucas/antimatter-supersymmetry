# L04 WORK: Dirac sea, zero-point energy, Pauli conditions in the SM

Revised in cycle 3 (fix round) after Referee 1 (REVIEWS.md) and LITCHECK.md. Changes are listed in "Response to referee 1" at the end.

All numbers below come from scripts in `calc/`, rerun from inside `calc/` in cycle 3, with saved outputs:

| script | output | content |
|---|---|---|
| `calc/zpe_derivation.py` | `calc/zpe_derivation_out.txt` (written by `python zpe_derivation.py > zpe_derivation_out.txt`) | Dirac sea energy, one-mode (anti)commutator check, cutoff and dim-reg ZPE, ρ+p |
| `calc/sm_pauli_sums.py` | `calc/sm_pauli_sums_out.txt` | four Pauli sums for the SM, scheme dependence of the finite part, required counterterm, tuning measure |
| `calc/sm_running_supertrace.py` | `calc/sm_running_supertrace_out.txt` | running-coupling supertraces with `tools/rg_sm.py` (3-loop), β_λ identity (Landau gauge), Veltman zero vs m_t |
| `calc/sm_structure_check.py` | `calc/sm_structure_check_out.txt` | rep content, anomalies, Str 1 vs N_g |

Inputs: `tools/sm_inputs.py` (PDG 2024) for all masses; `tools/rg_sm.py` (`couplings_at_mt`, `run(nloops=3)`) for all running.

**Result in one line.** Negative [established]. The SM violates the Pauli conditions. With measured masses Str 1 = −62, Str m² = −2.78e5 GeV², Str m⁴ = −9.94e9 GeV⁴. The scheme-independent failure is Str m⁴ ≠ 0: the SM one-loop vacuum energy changes by |Str m⁴|/(64π²) = 1.57e7 GeV⁴ = 6.3e53 ρ_Λ per unit ln μ², so a bare cosmological-constant counterterm must cancel the SM contributions to roughly 1 part in 1e54 (in MS-bar, Landau gauge, at μ ~ M_Z to m_t the required counterterm is ~1e8 GeV⁴ ≈ 4e54 ρ_Λ). No SM-only structure links the bosonic and fermionic sums. The sign of the fermion contribution comes from Fermi statistics, not from the existence of antiparticles (textbook; stated explicitly in Martin, arXiv:1205.3365, secs. VII.A and VII.D).

---

## 1. Zero-point energy with the Dirac sea

### 1a. Hole theory equals second quantization for the vacuum energy [established]
The single-particle Dirac Hamiltonian h(k) = α·k + βm has eigenvalues ±ω_k, ω_k = √(k²+m²), each twice degenerate (sympy, `zpe_derivation_out.txt`). Filling the negative-energy states gives sea energy per momentum mode

E_sea(k) = −2ω_k.

The charge-conjugation-symmetric ordering of the second-quantized Hamiltonian, H = Σ ω (b†b − bb† + d†d − dd†)/2, gives the same −2ω_k per mode. (The script line that prints this restates the single-particle sum in symmetrized form; it is not a separate derivation.) A Dirac field has 4 real d.o.f. (2 spin × particle/antiparticle), so the sea energy is −ω_k/2 per d.o.f., opposite to +ω_k/2 per bosonic d.o.f. Normal ordering sets the constant to zero by subtracting a c-number, which in the presence of gravity is the same as choosing the bare cosmological constant. Hole theory adds no information beyond standard QFT here (CONSTRAINTS H3).

### 1b. The negative sign is from Fermi statistics, not from antiparticles [established, textbook]
`zpe_derivation.py` part (a2) checks this at the level of a single mode:
- One fermion mode with {b, b†} = 1: H = ω(b†b − bb†)/2 has eigenvalues ±ω/2, vacuum −ω/2.
- One boson mode with [a, a†] = 1: H = ω(a†a + aa†)/2 has vacuum +ω/2.
- A complex scalar field (for example the charged Goldstone component G± of the Higgs doublet, in R_ξ gauge) has a distinct antiparticle and contributes 2 boson modes per k: vacuum **+**ω.
- A two-component Weyl field (the SM ν_L) contributes 2 fermion modes per k: vacuum −ω. In the covariant language the sign is the inverse power of the fermion determinant from Grassmann integration.
- In hole theory the "sea" picture is available only for fermions because Pauli exclusion is what makes a filled sea stable. For bosons there is no sea.

The antimatter picture is a description of the fermion sign, not its cause. Nothing about antiparticles pairs them with bosons. This is not new: Martin (arXiv:1205.3365, sec. VII.A, around eqs. 357-358) traces the Dirac minus sign to the anticommutation of the creation and annihilation operators, and sec. VII.D (eqs. 415-425 and the Wess-Zumino discussion) computes a complex scalar (positive) and a Majorana spinor (negative, self-conjugate) and shows their cancellation. In the simplest SUSY cancellation the field with a distinct antiparticle is the boson, and the fermion is its own antiparticle.

### 1c. Hard cutoff (per bosonic d.o.f.; multiply by (−1)^F g_i and sum) [established]
sympy, small-m/Λ expansion:

ρ = Λ⁴/(16π²) + m²Λ²/(16π²) − m⁴/(64π²)[ln(4Λ²/m²) − 1/2] + O(m⁶/Λ²)

p = Λ⁴/(48π²) − m²Λ²/(48π²) + m⁴/(64π²)[ln(4Λ²/m²) − 7/6] + ...

ρ + p = (8Λ⁴ + 4m²Λ² − m⁴)/(96π²) ≠ 0.

Summed over species, Λ⁴ ∝ Str 1, m²Λ² ∝ Str m², m⁴ ln Λ ∝ Str m⁴. The 3-momentum cutoff breaks Lorentz invariance (w ≠ −1). Visser (M. Visser, "Lorentz invariance and the zero-point stress-energy tensor", Particles 1(1), 138-154 (2018), DOI 10.3390/particles1010010, arXiv:1610.07264) shows that summed over species ρ+p = 0 iff Str 1 = Str m² = Str m⁴ = 0, after which ρ = −p = Σ(−1)^{2S} g m⁴ ln(m²/μ²)/(64π²) (his eq. 17).

### 1d. Dimensional regularization [established]
With n = 3 − 2ε spatial dimensions (sympy):

ρ = −m⁴/(64π² ε) + m⁴/(64π²)[ln(m²/μ̄²) − 3/2]   (MS-bar finite part checked symbolically)

and ρ + p = 0 exactly in ε (w = −1). Power divergences are absent, so the Str 1 and Str m² conditions disappear. Koksma and Prokopec (arXiv:1105.6296) get only m⁴ ln m² terms in dim-reg; Akhmedov (hep-th/0204048) argues instead that zero-point energies diverge at most quadratically (he keeps an m²Λ² term and says dim-reg is not suited to power divergences), and Koksma-Prokopec say their results differ from his. Both find massless fields contribute zero.

What remains in dim-reg:
- The pole ∝ Str m⁴. If Str m⁴ ≠ 0 it is removed by a bare cosmological-constant counterterm, and the one-loop term at fixed masses runs: dρ₁/d ln μ = −Str m⁴/(32π²).
- The finite part Σ s_i m_i⁴[ln(m_i²/μ²) − c_i]/(64π²). The constant c_i depends on scheme and spin: MS-bar c = 3/2 for scalars and fermions and 5/6 for massive vectors (Landau gauge, standard Coleman-Weinberg); DR-bar c = 3/2 for all (S. P. Martin, PRD 65, 116003 (2002), hep-ph/0111209, discusses the MS-bar/DR-bar effective-potential relation); the 3-momentum cutoff gives a uniform constant again, with μ² → 4Λ².

**The fourth condition is scheme-dependent [established].** If Str m⁴ = 0, a species-independent constant drops out and ρ_fin = Str(m⁴ ln m²)/(64π²). A non-uniform constant leaves an extra term: in MS-bar, ρ_fin = [Str(m⁴ ln m²) + (2/3) Σ_V g_V m_V⁴]/(64π²). For the SM vectors the MS-bar minus DR-bar difference is (2/3)Σ_V g_V m_V⁴/(64π²) = 4.83e5 GeV⁴ (`sm_pauli_sums_out.txt`). So "Str m⁴ ln m² = 0" is the condition for ρ = 0 only in schemes with a species-independent constant. Only Str m⁴ = 0, equivalently μ-independence of the one-loop term, is scheme-independent.

Status of each Pauli condition by scheme (CONSTRAINTS H2):

| condition | hard 3-momentum cutoff | dim-reg MS-bar | dim-reg DR-bar |
|---|---|---|---|
| Str 1 = 0 | needed (Λ⁴) | not needed | not needed |
| Str m² = 0 | needed (Λ²) | not needed | not needed |
| Str m⁴ = 0 | needed (ln Λ) | needed for μ-independence without a counterterm | same |
| finite part = 0 | Str m⁴ ln m² = 0 | Str m⁴ ln m² + (2/3)Σ_V g_V m_V⁴ = 0 | Str m⁴ ln m² = 0 |

Str m⁴ = 0 is the only scheme-independent condition. The fourth condition is scheme-dependent. The negative result rests on Str m⁴ alone.

---

## 2. The SM sums with measured masses

### 2a. Counting [established]
Physical (unitary-gauge) d.o.f.: gluons 16, photon 2, W± 6, Z 3, h 1 → 28 bosonic. Quarks 6 × 3 colours × 4 = 72, charged leptons 12, ν_L 3 × 2 = 6 → 90 fermionic. Matches CONSTRAINTS G.

Goldstones: in R_ξ gauges a massive vector contributes 4 components, −2 ghosts, +1 Goldstone. At the tree minimum the unphysical modes (timelike vector component, Goldstone, two ghosts) all sit at ξM² with weights +1 +1 −2, so they cancel in every Str m^{2k}, and each massive vector counts with weight 3 at mass M. Str 1 and all Str m^{2k} at the vacuum are therefore gauge-independent. Only the finite constant (5/6 vs 3/2) is scheme-specific.

Neutrinos (CONSTRAINTS A2): 2 d.o.f. each. Masses from oscillations, normal ordering, lightest = 0. The neutrino m⁴ terms are 1e-51 of the top term. The only mechanism-dependent quantity is Str 1: a Dirac mass with ν_R (excluded) would give 4 d.o.f. per neutrino and Str 1 = −68 instead of −62. Every conclusion below holds for either count.

### 2b. Numbers (`sm_pauli_sums_out.txt`) [established, given inputs]

| sum | SM value | bosons | fermions |
|---|---|---|---|
| Str 1 | −62 | +28 | −90 |
| Str m² | −2.782e5 GeV² | +7.94e4 | −3.58e5 (\|F/B\| = 4.5) |
| Str m⁴ | −9.939e9 GeV⁴ | +7.03e8 | −1.064e10 (\|F/B\| = 15.1) |
| Str m⁴ ln(m²/GeV²) | −1.03e11 GeV⁴ | | (unit-dependent since Str m⁴ ≠ 0) |

Str m⁴ is 107% top quark. With all other masses fixed, Str m⁴ = 0 would need m_t = 87.5 GeV and Str m² = 0 would need m_t = 81.2 GeV. Measured: 172.57 GeV. (These are a re-expression of the sums; Alberghi et al. eqs. 4-6 give the equivalent top-vs-W/Z relations.)

### 2c. Comparison to ρ_Λ = 2.5e-47 GeV⁴ (CONSTRAINTS E4)

Hard cutoff, magnitude / ρ_Λ (scheme: 3-momentum cutoff, not Lorentz invariant, illustration only):

| Λ | quartic | quadratic | log |
|---|---|---|---|
| 1 TeV | 1.6e58 | 7.0e55 | 9.6e54 |
| M_Pl | 3.5e122 | 1.1e88 | 5.6e55 |

**Physical statement in dim-reg [established].** The physical vacuum energy is ρ_phys = Ω(μ) + V_tree(v; μ) + ρ₁(μ) + (higher loops, QCD condensate, ...), where Ω is the bare cosmological-constant counterterm, a free parameter. ρ₁(μ) alone is not physical. What the SM spectrum fixes is:

1. **Tuning measure (μ-independent, scheme-independent).** ρ₁ changes by |Str m⁴|/(64π²) = 1.57e7 GeV⁴ = 6.3e53 ρ_Λ per unit ln μ². Ω(μ) must run to compensate. No choice of μ makes the SM loop contribution naturally of size ρ_Λ. That would need Str m⁴ = 0.
2. **Size of the required counterterm (scheme stated: MS-bar, Landau gauge; mixed order: tree term with λ = m_h²/2v², one-loop term with pole masses).** V_tree = −λv⁴/4 = −1.19e8 GeV⁴. Ω_req = ρ_Λ − V_tree − ρ₁(μ) = +1.16e8 GeV⁴ (4.6e54 ρ_Λ) at μ = M_Z and +9.6e7 GeV⁴ (3.8e54 ρ_Λ) at μ = m_t. So Ω must cancel the SM electroweak contributions to about 1 part in 4e54. This is the standard statement of the cc problem at the electroweak scale (Koksma-Prokopec; Martin arXiv:1205.3365 sec. IX; Ossola-Sirlin hep-ph/0305050), updated with PDG 2024 masses.

The MS-bar one-loop term with Ω set to zero, ρ₁(μ)/ρ_Λ = 1.1e53 (M_Z), 9.1e53 (m_t), 3.1e54 (1 TeV), 2.3e55 (1e10 GeV), 5.0e55 (M_Pl), is printed only to show the μ-dependence. It vanishes at μ* = 83.6 GeV. That is the scale at which the MS-bar one-loop term happens to be zero, not a cancellation.

Neutrino sector alone (dim-reg, Ω = 0): 6e3 to 4e4 ρ_Λ for μ from 1 eV to 1 GeV. The coincidence ρ_Λ^{1/4} = 2.24 meV ~ m_ν is not used (H1).

### 2d. Running couplings (`sm_running_supertrace_out.txt`) [established method; 3-loop RGEs]
Runner: `tools/rg_sm.py`, `run(nloops=3)`, 3-loop MS-bar RGEs for gauge, y_t, λ, NNLO matching at μ = M_t from Buttazzo et al. (arXiv:1307.3536, JHEP 12 (2013) 089, eqs. 55-60) with PDG 2024 inputs. At M_t: λ = 0.12617, y_t = 0.93286, g₂ = 0.64764, g_Y = 0.35843, g₃ = 1.16516. Convention V ⊃ λ|H|⁴, m_h² = 2λv². A 1-loop run from the same runner is printed for comparison only.

Defined (couplings at μ, **Landau-gauge** field-dependent masses):
- A_vac = Str M⁴/v⁴ at the EW vacuum = 4λ² + (3/16)(2g⁴ + (g²+g'²)²) − 3y_t⁴
- A_φ = Str M⁴(φ)/φ⁴ in a large Higgs background (h mass² 3λφ², 3 Goldstones λφ²) = 12λ² + (3/16)(...) − 3y_t⁴
- B_vac = Str M²/v² at vacuum (Pauli quadratic)
- B_φ = Str M²(φ)/φ² = (3/v²)(m_h² + 2M_W² + M_Z² − 4m_t²), the Veltman combination

| log10 μ/GeV | λ | A_vac | A_φ | B_vac | B_φ | 16π² β_λ (3-loop) |
|---|---|---|---|---|---|---|
| 2.24 (M_t) | +0.126 | −2.09 | −1.96 | −3.93 | −3.42 | −3.13 |
| 10 | +0.003 | −0.159 | −0.159 | −0.85 | −0.84 | −0.32 |
| 16 | −0.010 | −0.023 | −0.022 | −0.31 | −0.35 | −0.034 |
| 19 | −0.010 | +0.006 | +0.006 | −0.14 | −0.19 | +0.025 |
| 23 | −0.007 | +0.031 | +0.031 | +0.038 | +0.008 | +0.072 |

A_vac(M_t) v⁴ = −7.7e9 GeV⁴ (MS-bar top mass, vs −9.9e9 with the pole mass).

Zero crossings, log10(μ/GeV), 3-loop (1-loop in brackets): λ 10.66 (8.36); β_λ full 17.56 (17.78); β_λ one-loop formula on 3-loop couplings 17.53; A_φ 18.19 (19.15); A_vac 18.30 (19.96); B_vac 22.13 (none below 1e25); B_φ 22.83 (none). The 3-loop λ crossing at 10^10.7 GeV and β_λ = 0 at 10^17.6 GeV agree with Buttazzo et al. (λ = 0 near 1e10-1e11 GeV; β_λ vanishes at about 1e17-1e18 GeV).

**Identity (sympy, exact, one loop, Landau gauge) [established, standard]:**
16π² β_λ − 4λ(16π² γ_H^Landau) = 2 Str M⁴(φ)/φ⁴, with 16π² γ_H^Landau = 3y_t² − (9/4)g² − (3/4)g'².

This holds in Landau gauge only. In R_ξ or Fermi gauges γ_H is ξ-dependent and the Goldstone field-dependent masses shift by ξ-dependent terms, so the split of β_λ into "non-anomalous" and "anomalous" parts, and with it the identity, is gauge-dependent. β_λ itself is not. (On gauge dependence of the SM effective potential: Di Luzio, Mihaila, JHEP 06 (2014) 079, arXiv:1404.7450; Andreassen, Frost, Schwartz, PRD 91, 016009 (2015), arXiv:1408.0287.) The identity is the standard one-loop RG-consistency condition of the Coleman-Weinberg potential (μ-independence of V_tree + V_1-loop at large φ; see e.g. Sher, Phys. Rep. 179 (1989) 273; Ford, Jack, Jones, Nucl. Phys. B 387 (1992) 373). Here it is only restated in Pauli language: the Pauli quartic sum in a Higgs background is the Landau-gauge non-anomalous part of β_λ, and the Pauli quadratic sum in a background is the Veltman combination (stated explicitly by Masina, Quiros, PRD 88, 093003 (2013), arXiv:1308.1242, eqs. 9-11, including the Goldstone weight 3).

Because 16π² β_λ − 2A_φ = −3λ(3g² + g'² − 4y_t²) vanishes with λ, A_φ and β_λ must cross zero near each other by construction (3-loop: 10^18.2 vs 10^17.6). This is not a prediction.

Veltman zero: B_φ = 0 at 10^22.83 GeV for m_t = 172.57 GeV, moving from 10^22.48 to 10^23.17 over m_t ± 0.29 GeV and to 10^23.34 at m_t = 173.0 GeV. Hamada, Kawai, Oda (arXiv:1210.2538, PRD 87, 053009 (2013); erratum PRD 89, 059901) find the bare-mass coefficient vanishing near 1e23 GeV at M_t = 173 GeV (two-loop), close to M_Pl for 170 GeV. Jegerlehner (arXiv:1304.7813) reports a much lower crossing with different matching. The crossing scale is [uncertain / scheme- and m_t-dependent].

**What these crossings mean for vacuum energy [conjecture → assessed negative].** A_vac(μ) is Str M⁴ at φ = v evaluated with couplings at μ. It is not the beta function of the cosmological-constant counterterm. In the standard MS-bar treatment with symmetric-phase parameters V = Ω − m²|H|²/2 + λ|H|⁴, the φ-independent term Ω runs only through the Lagrangian mass parameter (one-loop β_Ω ∝ m⁴ from the four real scalar components); gauge and fermion masses are proportional to φ and feed β_λ, β_{m²} and γ_H instead (RG-improved effective potential with the vacuum term: Bando, Kugo, Maekawa, Nakano, PLB 301 (1993) 83, hep-ph/9210228 [content cited from memory, not rechecked this cycle]). Str M⁴ at φ = v mixes all of these. So a zero of A_vac at high scale says nothing about the cc counterterm stopping to run, and β_Ω ≠ 0 whenever m² ≠ 0. A zero of A_vac or A_φ near M_Pl is a restatement of Higgs near-criticality (λ and β_λ small at high scale; Degrassi et al., arXiv:1205.6497, JHEP 08 (2012) 098) and cancels nothing at our vacuum, where Str m⁴ = −1e10 GeV⁴. Treating the coincidence with M_Pl as meaningful would be the Shaposhnikov-Wetterich type argument (arXiv:0912.0208, PLB 683 (2010) 196), which needs asymptotically safe gravity, outside scope.

---

## 3. SM-only structures that could relate the sums

### 3a. Rep content and anomalies (`sm_structure_check_out.txt`) [established]
Bosonic d.o.f. = 2 dim G + 4 = 28 (eaten Goldstones move between columns, the total is fixed). Fermionic d.o.f. = 30 N_g. Str 1 = 28 − 30 N_g; zero needs N_g = 14/15. No integer works.

All gauge and mixed gauge-gravitational anomalies cancel per generation (checked). These conditions are linear or cubic in hypercharges and contain no Yukawa couplings. Fermion masses are y_f v/√2 with free y_f, so anomaly cancellation cannot constrain Str m² or Str m⁴. The gravitational anomaly condition Σ Y = 0 is a trace over charges, not over d.o.f., and gives no relation to Str 1.

### 3b. Dirac sea counting conventions [established]
Section 1a shows hole theory and symmetric second quantization give the same −2ω per mode. Any other convention differs by a c-number subtraction. A mass-independent subtraction can only change the Λ⁴ term (Str 1); a mass-dependent one is the same as choosing the bare cc. Neither produces a relation between boson and fermion masses. The particle/antiparticle split of a Dirac field's 4 d.o.f. is fixed by CPT (CONSTRAINTS D: particle and antiparticle count identically), so there is no freedom to reweight antiparticle contributions.

### 3c. NCG spectral action (A3) [established structure, primary text per LITCHECK]
Map to the SM: Chamseddine, Connes, Marcolli (hep-th/0610241, Adv. Theor. Math. Phys. 11 (2007) 991-1089) derive the SM Lagrangian (plus ν_R and a Majorana sector) from the spectral action Tr f(D/Λ) on an almost-commutative geometry. In their Theorem 3.13, eq. (3.41), as checked in LITCHECK.md, the explicit cosmological (φ-independent) term is

(1/π²)(48 f₄ Λ⁴ − f₂ Λ² c + (f₀/4) d),  c = Tr(Y_R† Y_R), d = Tr((Y_R† Y_R)²),

with Y_R the Majorana (ν_R) Yukawa matrix. The Dirac Yukawa traces (a, b in CCM) multiply |H|² and |H|⁴, so Dirac masses reach the vacuum energy only through the Higgs potential at its minimum.

1. In the SM-equivalent sector (no ν_R, no Majorana mass, A3.2) c = d = 0, so the explicit cosmological term is 48 f₄ Λ⁴/π², a pure Tr(1) term. There is no mass-dependent cosmological term at all and no boson-fermion Pauli structure. f₄ is a free moment of the cutoff function.
2. The finite space in CCM has 96 fermionic states (32 per generation) including ν_R, plus the σ scalar from the Majorana mass. Both are excluded (A1, A3.2).
3. The mass relation CCM impose, Tr(m_ν†m_ν + m_e†m_e + 3m_u†m_u + 3m_d†m_d) = 8M_W² at the unification scale (trace over generations; verified in van den Dungen, van Suijlekom, Rev. Math. Phys. 24, 1230004 (2012), arXiv:1204.0328, sec. 8.1, and CCM sec. 1), is a high-scale boundary condition, excluded by A3.2. It is also not a supertrace: it equates a fermion mass sum to one gauge mass, while Str m² would need 6M_W² + 3M_Z² + m_H² on the boson side.

No SM-equivalent relation survives. Result holds in the standard formulation (A3.4) trivially, since nothing is derived from the reformulation.

### 3d. Prior work [established]
- Alberghi, Kamenshchik, Tronconi, Vacca, Venturi, "Vacuum energy, cosmological constant and standard model physics", JETP Lett. 88, 705-710 (2008), DOI 10.1134/S002136400823001X, arXiv:0804.4782: one-loop SM vacuum energy (divergent and finite parts) cannot cancel without several new bosons and at least one new massive fermion. Their count is N_F = 96, N_B = 27 (massive ν, no Higgs); same substance as 90/28 here.
- Kamenshchik, Starobinsky, Tronconi, Vacca, Venturi, arXiv:1604.02371: the same analysis repeated with a then-hypothetical 750 GeV resonance.
- Kamenshchik, Starobinsky, Tronconi, Vardanyan, Venturi, EPJC 78 (2018) 200, arXiv:1801.08434: Pauli-Zeldovich cancellation with interactions in toy models.
- Visser 2018 sec. 10.1 (eqs. 50-52): the SM alone cannot satisfy the Pauli rules; BSM states are required. Sec. 9 (eqs. 45-49): RG flow of the Pauli sums.
- Koksma, Prokopec, arXiv:1105.6296: Lorentz-invariant (dim-reg) SM vacuum energy from t, W, Z, h; discrepancy of ~56 orders.
- J. Martin, Comptes Rendus Physique 13, 566 (2012), arXiv:1205.3365: sec. IX SM vacuum energy vs μ (eqs. 515-516, Fig. 5, including the sign change); secs. VII.A, VII.D the fermion sign from anticommutation and the complex scalar / Majorana / Wess-Zumino cancellation.
- Ossola, Sirlin, EPJC 31, 165 (2003), hep-ph/0305050: SM vacuum energy at one loop.
- Masina, Quiros, PRD 88, 093003 (2013), arXiv:1308.1242, eqs. 9-11: Veltman coefficient = Str M²(φ)/φ² with Goldstone weight.
- Pauli's original statement: W. Pauli, ETH lectures 1950-51, "Selected Topics in Field Quantization", Pauli Lectures on Physics vol. 6, ed. C. P. Enz (MIT Press, 1973) [confirmed by LITCHECK via library records; sum rules p. 33 of the English translation per Visser].

---

## 4. Conclusion

**Negative result [established].** SM antimatter, in hole-theory or any equivalent language, does not reproduce the SUSY boson/fermion vacuum-energy cancellation:
- The scheme-independent Pauli condition Str m⁴ = 0 fails: Str m⁴ = −9.9e9 GeV⁴. The one-loop SM vacuum energy changes by 6.3e53 ρ_Λ per unit ln μ², and in MS-bar (Landau gauge) at the electroweak scale the bare counterterm must be ~1e8 GeV⁴ ≈ 4e54 ρ_Λ to leave ρ_Λ. Str 1 and Str m² also fail (relevant with a hard cutoff). The fourth condition is scheme-dependent and moot once Str m⁴ ≠ 0.
- The fermion sign is a Fermi-statistics effect; a complex boson with a distinct antiparticle contributes with positive sign, so "antimatter" is not the paired object SUSY supplies (textbook; Martin 2012).
- SM-only structures (anomaly cancellation, rep content, sea conventions, the SM-equivalent part of the NCG spectral action) do not touch the mass sums. Str 1 = 28 − 30N_g has no integer zero.
- The only places SM supertraces vanish are at very high scales, as running-coupling statements (Landau-gauge A_φ ≈ 0 near 10^18.2 GeV, tied by construction to β_λ ≈ 0 near 10^17.6 GeV; Veltman zero near 10^22.8 GeV at 3 loops, m_t-sensitive). These are known near-criticality facts and do not cancel the vacuum energy at our vacuum.

Comparison with SUSY [established qualitatively]: unbroken SUSY gives Str m^{2k} = 0 multiplet by multiplet. With soft breaking at the LHC-allowed scale (M_SUSY ≳ 1-2 TeV, CONSTRAINTS C3), the sfermion contribution alone is of order 90 M_SUSY⁴ ~ 1e14-1e15 GeV⁴ before partial cancellation against gauginos and higgsinos (arithmetic in `sm_pauli_sums_out.txt`, not a spectrum calculation), so broken SUSY at that scale leaves a residual Str m⁴ equal to or larger than the SM's 1e10 GeV⁴. Neither solves the cc problem.

**Internal consistency checks (no new falsifiable prediction).** This is a negative result and makes no new falsifiable prediction. The checks it offers:
(a) Any claimed SM-only cancellation of the one-loop vacuum-energy running must change measured masses: with other masses fixed it needs m_t = 87.5 GeV (Str m⁴) or 81.2 GeV (Str m²), excluded by m_t = 172.57 ± 0.29 GeV. This re-expresses the computed sums.
(b) No SM structure fixes the sum Ω + V_tree + ρ₁ (+ higher loops, QCD condensate) to zero. The tree term V_tree = −λv⁴/4 = −1.19e8 GeV⁴ is an SM contribution larger than the one-loop term at the electroweak scale, but it depends on μ through λ(μ), v(μ) and is absorbed into the same free counterterm, so it supplies no relation either.
(c) The 3-loop running reproduces the literature crossings (λ = 0 at 10^10.7 GeV, β_λ = 0 at 10^17.6 GeV vs Buttazzo et al.; Veltman zero at 10^23.3 GeV for m_t = 173 GeV vs Hamada-Kawai-Oda ~1e23). These are checks of the tooling, not predictions.

**Open issues.**
- Ω_req above mixes tree (λ from m_h) and one-loop (pole masses) terms; a consistent two-loop/threshold-corrected evaluation would move it by O(10%). Does not affect any conclusion.
- QCD condensate (~(0.2 GeV)⁴ scale, ~1e44 ρ_Λ) and higher-loop terms are separate vacuum-energy contributions, absorbed into the same counterterm. Not computed here.
- Bando et al. 1993 cited for the Ω running from memory; content not rechecked this cycle.

---

## Response to referee 1

1. **Headline 1e53-5e55 ρ_Λ (major).** Agreed. Dropped ρ(μ)/ρ_Λ as a "residual". The headline is now the μ-independent tuning measure |Str m⁴|/(64π²) = 6.3e53 ρ_Λ per unit ln μ², plus the size of the required counterterm in a stated scheme (MS-bar, Landau gauge, μ = M_Z or m_t: ~1e8 GeV⁴ ≈ 4e54 ρ_Λ, including the tree term). The μ table is kept in 2c only as an illustration of μ-dependence and is labeled unphysical in the script output too.
2. **Fourth condition scheme-dependent (major).** Agreed. 1d now states it as scheme-dependent, gives the MS-bar form Str m⁴ ln m² + (2/3)Σ_V g_V m_V⁴, and the SM size of the MS-bar/DR-bar difference (4.83e5 GeV⁴, computed in `sm_pauli_sums.py`). Table split into cutoff / MS-bar / DR-bar. H2 checklist fixed: only Str m⁴ is scheme-independent.
3. **Check (b) false (major).** Agreed. Old (b) and the "larger, not smaller" sentence removed. New (b) is the referee's restatement: no SM structure fixes Ω + V_tree + ρ₁ to zero; V_tree is μ-dependent and absorbed by the same counterterm. V_tree is now printed with its sign and included in Ω_req.
4. **Own 1-loop RGE vs tools/ (major).** Agreed. `sm_running_supertrace.py` now uses `rg_sm.couplings_at_mt()` and `rg_sm.run(nloops=3)` (and `sm_inputs`). Table and crossings updated; my numbers match the referee's (λ 10^10.66, A_φ 10^18.19, A_vac 10^18.30, β_λ one-loop form 10^17.53, B_φ 10^22.83). Added the full 3-loop β_λ (numerical derivative): 10^17.56. The "1.6 decade" open issue is gone.
5. **A_vac is not β of the cc counterterm (minor).** Agreed. Reasoning rewritten in 2d: Ω runs only through the Lagrangian m² in the symmetric-phase MS-bar treatment; Str M⁴ at φ = v mixes β_λ, β_{m²}, γ_H. The assessed-negative verdict is unchanged.
6. **Identity Landau gauge only; not novel (minor).** Agreed. The script now states and checks the identity with γ_H^Landau explicitly, the text says "Landau gauge only" with gauge-dependence references, cites Sher 1989 and Ford-Jack-Jones 1992 as the standard source, and it is removed from the novelty list.
7. **A_φ "prediction" (minor).** Agreed. The script prints 16π²β_λ − 2A_φ = −3λ(3g² + g'² − 4y_t²), which shows the close crossing is automatic. Relabeled "internal consistency checks" and stated plainly that the line makes no new falsifiable prediction.
8. **SUSY comparison reversed (minor).** Agreed. Now: broken SUSY at the LHC-allowed scale leaves a residual equal to or larger than the SM's, with the arithmetic 90 M_SUSY⁴ printed and labeled as not a spectrum calculation.
9. **Veltman scale "only near 1e23" (minor).** Agreed. "Only" dropped; tagged [uncertain / scheme- and m_t-dependent]; added an m_t scan of the crossing (10^22.5 to 10^23.2 over ±1σ, 10^23.3 at 173 GeV) and the Jegerlehner reference.
10. **CCM description (minor).** Agreed. Rewritten from CCM eq. (3.41) as checked by LITCHECK: cosmological Λ², Λ⁰ terms are Majorana-only and vanish in the SM sector; Dirac traces multiply |H|², |H|⁴; Λ² enters with a minus sign. "Σ_generations Tr" notation fixed.
11. **W± as complex scalar; zpe script (minor).** Agreed. Example changed to the charged Goldstone G± and "complex scalar field". The symmetrized-ordering line is now labeled in the script and text as a restatement, not a separate check. Added a one-mode (anti)commutator check (part a2) that does derive the sign from the operator algebra. Comment fixed to Γ(−(n+1)/2).
12. **Checklist incomplete (minor).** Agreed. Checklist below now lists every item ID.

No disagreements with the referee. One partial qualification: on finding 1 I report the required counterterm at a stated μ in addition to the referee's μ-independent measure, because CONSTRAINTS E4 asks for a comparison to ρ_Λ and the counterterm size is the standard physical way to state it. It is labeled scheme-dependent and mixed-order.

LITCHECK corrections: (1) Akhmedov characterization fixed in 1d. (2) CCM fixed in 3c. (3) Alberghi et al. journal ref added. (4) Visser reference format fixed. (5) "Koksma-Prokopec make the same point" about non-decoupling removed. (6) Martin 2012, Ossola-Sirlin 2003, Masina-Quiros 2013, Visser sec. 10.1, Kamenshchik et al. 1604.02371 added to 3d.

---

## What is new (ruling R5)

Honest verdict: **nothing new physically. The line is a restatement of known work with an updated numerical evaluation.** Recommend folding it into the S1 synthesis line rather than promoting it alone.

Comparison, item by item:

| piece of this line | where it already is | new here? |
|---|---|---|
| SM fails the Pauli conditions; cancellation needs new bosons and a massive fermion | Alberghi et al., JETP Lett. 88, 705 (2008) / 0804.4782; Visser sec. 10.1 | no |
| Lorentz invariance ⇔ first three conditions; dim-reg ρ = −p with m⁴ ln m² | Visser secs. 4-6, eq. 17; Koksma-Prokopec 1105.6296 | no |
| SM dim-reg vacuum energy vs μ, sign change, ~55-56 orders | Koksma-Prokopec; Martin 1205.3365 sec. IX, Fig. 5; Ossola-Sirlin | no (PDG 2024 update only) |
| Veltman coefficient = Str M²(φ)/φ², Goldstone weight | Masina-Quiros 1308.1242 eqs. 9-11 | no |
| Str M⁴(φ)/φ⁴ = Landau-gauge non-anomalous β_λ | standard CW RG consistency (Sher 1989; Ford-Jack-Jones 1992) | no; Pauli-language packaging only |
| fermion sign from Fermi statistics, not antiparticles; complex boson positive | Martin 1205.3365 sec. VII.A (anticommutation) and VII.D (complex scalar vs Majorana, Wess-Zumino) | no |
| fourth Pauli condition scheme-dependent through the vector constant (MS-bar 5/6 vs 3/2), with SM size 4.8e5 GeV⁴ | the constants are standard (e.g. S. P. Martin hep-ph/0111209); Visser eq. 17 uses a uniform constant; I did not find the consequence for Pauli's fourth condition stated, but did not search exhaustively | minor technical clarification at most; does not change any conclusion |

The candidate piece named by the overseer, "the negative sign is from Fermi statistics, not from antiparticles, shown by complex bosons", is already in the literature. Martin (arXiv:1205.3365) attributes the Dirac minus sign to the anticommuting operators (sec. VII.A) and explicitly computes a complex scalar (positive, two real fields) against a Majorana spinor (negative, its own antiparticle), which is the Wess-Zumino cancellation (sec. VII.D). The antimatter-specific phrasing ("antiparticles are not what SUSY pairs") is a one-line corollary of that, and of CPT counting (3b). I found no paper that uses exactly that phrasing as a thesis, but the content is there, so I do not claim it as new. Its value is as one input to S1 (antiparticle-reweighting no-go), where it supplies the vacuum-energy instance.

---

## CONSTRAINTS checklist

**Part A (scope)**
- **A1 (SM only):** only SM fields; SUSY used only as a comparison target (sec. 4). No new particles in any mechanism. The NCG ν_R, σ and Majorana sector are discarded. ✓
- **A2 (neutrino mass):** ν masses from oscillation data enter only via m⁴ (1e-51 of the top term) and the d.o.f. count in Str 1 (−62 with 2 d.o.f. each, −68 with the excluded Dirac ν_R). Every conclusion is insensitive to the mechanism. ✓
- **A3 (reformulations):** NCG spectral action used only to look for a relation. Map to SM cited (CCM 2007); in the SM-equivalent sector the cosmological term is a pure Λ⁴ Tr(1) term. Extra states and the unification boundary condition are not used (A3.2). Nothing is derived from the reformulation, so A3.4 holds trivially. ✓

**Part B (antimatter tests)**
- **B1-B6 (CPT tests: K0 mass difference, p̄ q/m and magnetic moment, H̄ 1S-2S, ALPHA-g, e± g-factor):** the line treats particles and antiparticles identically, as CPT requires (3b). No mechanism distinguishes them, so none of these limits is approached. ✓
- **B7 (electron EDM), B10 (neutron EDM, θ̄):** no CP-violating input is used; vacuum energy at one loop is CP-even. Not affected. ✓
- **B8 (CKM J), B9 (Λ_b baryon CP violation):** CP violation enters no Pauli sum (sums depend only on masses and d.o.f.). Consistent; not used. ✓

**Part C (collider)**
- **C1, C2:** m_H = 125.20, M_W, M_Z, m_t = 172.57, v from `tools/sm_inputs.py` (PDG 2024). ✓
- **C3:** negative result; no superpartner-like signature is predicted, so the null LHC results are automatically consistent. The SUSY comparison uses M_SUSY ≳ 1-2 TeV from C3. ✓
- **C4 (muon g-2):** not used, no claim made. ✓

**Part D (couplings, RG):** running uses `tools/rg_sm.py`, 3-loop RGEs (`run(nloops=3)`), NNLO matching at M_t; loop order stated in the script and in 2d. CPT counting of particles and antiparticles in loops respected (a Dirac fermion counts once as a field). ✓

**Part E (cosmology)**
- **E4:** all vacuum-energy quantities compared to ρ_Λ = 2.5e-47 GeV⁴ (from `sm_inputs`). ✓
- **E1, E2, E3, E5, E6:** no dark matter, baryon density, η, or N_eff claim; not used. ✓
- **E7, E8:** neutrino masses at the oscillation minimum (Σm_ν ≈ 0.059 eV, normal ordering, lightest 0), within Planck/DESI and KATRIN bounds. ✓
- **E9 (matter-antimatter symmetric cosmologies):** none proposed. ✓
- **E10 (baryogenesis in the SM):** not used; no claim. ✓

**Part F (B violation)**
- **F1 (proton decay), F2 (sphalerons), F3 (n-n̄):** no baryon-number-violating process is involved in the vacuum-energy sums. Not affected. ✓

**Part G (reference facts):** reproduces the Pauli condition list and the 28/90 count; the Veltman combination is computed separately (B_φ) and distinguished from the Pauli quadratic sum (B_vac). Veltman normalization: only the bracket and its zero are used, so the δμ² vs δm_h² factor (R3) does not enter. The dim-reg statement of the problem is given; nothing is "solved" by regulator choice. ✓

**Part H (method)**
- **H1:** no numerology. The meV neutrino coincidence, μ* = 83.6 GeV, and the A_φ / β_λ crossing proximity are explicitly flagged as non-results. ✓
- **H2:** results given for hard cutoff, MS-bar and DR-bar. Str m⁴ (scheme-independent) fails in all; the fourth condition is stated as scheme-dependent; the Str M⁴(φ)/β_λ identity is stated as Landau-gauge only. ✓
- **H3:** Dirac sea shown equivalent to standard quantization for vacuum energy; the sign is derived from the (anti)commutator in standard language; conclusion holds in the standard formulation. ✓
- **H4:** every number comes from a `calc/` script, rerun from `calc/` this cycle with saved outputs. ✓
