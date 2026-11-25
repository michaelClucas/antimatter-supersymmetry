# L04 WORK: Dirac sea, zero-point energy, Pauli conditions in the SM

All numbers below come from scripts in `calc/` with saved outputs:

| script | output | content |
|---|---|---|
| `calc/zpe_derivation.py` | `calc/zpe_derivation_out.txt` | Dirac sea energy, cutoff and dim-reg ZPE, ρ+p |
| `calc/sm_pauli_sums.py` | `calc/sm_pauli_sums_out.txt` | four Pauli sums for the SM, comparison to ρ_Λ |
| `calc/sm_running_supertrace.py` | `calc/sm_running_supertrace_out.txt` | running-coupling supertraces, β_λ identity, Veltman |
| `calc/sm_structure_check.py` | `calc/sm_structure_check_out.txt` | rep content, anomalies, Str 1 vs N_g |

**Result in one line.** Negative. The SM violates every Pauli condition. With measured masses Str 1 = −62, Str m² = −2.78e5 GeV², Str m⁴ = −9.94e9 GeV⁴. Even in the most forgiving Lorentz-invariant dim-reg treatment the residual vacuum energy is |ρ| ~ 1e53 to 5e55 ρ_Λ depending on μ. No SM-only structure links the bosonic and fermionic sums. The sign of the fermion contribution comes from Fermi statistics, not from the existence of antiparticles.

---

## 1. Zero-point energy with the Dirac sea

### 1a. Hole theory equals second quantization for the vacuum energy [established]
The single-particle Dirac Hamiltonian h(k) = α·k + βm has eigenvalues ±ω_k, ω_k = √(k²+m²), each twice degenerate (sympy, `zpe_derivation_out.txt`). Filling the negative-energy states gives sea energy per momentum mode

E_sea(k) = −2ω_k.

The charge-conjugation-symmetric ordering of the second-quantized Hamiltonian, H = Σ ω (b†b − bb† + d†d − dd†)/2, gives the same −2ω_k per mode. A Dirac field has 4 real d.o.f. (2 spin × particle/antiparticle), so the sea energy is −ω_k/2 per d.o.f., exactly opposite to the +ω_k/2 per bosonic d.o.f. Normal ordering sets the constant to zero by subtracting a c-number, which in the presence of gravity is the same as choosing the bare cosmological constant. So hole theory adds no information beyond standard QFT here (CONSTRAINTS H3).

### 1b. The negative sign is from Fermi statistics, not from antiparticles [established]
- A complex scalar (e.g. the W± or a charged pion field) has an antiparticle and contributes **+**ω/2 per d.o.f.
- A two-component Weyl field (the SM ν_L) contributes −ω/2 per d.o.f. In the covariant language the sign is the inverse power of the fermion determinant from Grassmann integration.
- In hole theory the "sea" picture is available only for fermions because Pauli exclusion is what makes a filled sea stable. For bosons there is no sea.

So the antimatter picture is a description of the fermion sign, not its cause. This already removes the main hope of the line: nothing about antiparticles per se pairs them with bosons.

### 1c. Hard cutoff (per bosonic d.o.f.; multiply by (−1)^F g_i and sum) [established]
sympy, small-m/Λ expansion:

ρ = Λ⁴/(16π²) + m²Λ²/(16π²) − m⁴/(64π²)[ln(4Λ²/m²) − 1/2] + O(m⁶/Λ²)

p = Λ⁴/(48π²) − m²Λ²/(48π²) + m⁴/(64π²)[ln(4Λ²/m²) − 7/6] + ...

ρ + p = (8Λ⁴ + 4m²Λ² − m⁴)/(96π²) ≠ 0.

Summed over species, Λ⁴ ∝ Str 1, m²Λ² ∝ Str m², m⁴ ln Λ ∝ Str m⁴, and the finite part ∝ Str m⁴ ln m² (given the first three vanish). These are Pauli's four conditions. The 3-momentum cutoff breaks Lorentz invariance (w ≠ −1). Visser (arXiv:1610.07264, Particles 1 (2018) 10, verified) shows that summed over species ρ+p = 0 iff Str 1 = Str m² = Str m⁴ = 0, after which ρ = −p = Str[m⁴ ln(m²/μ²)]/(64π²) (his eq. 17). So the Lorentz-invariant finite answer needs the first three conditions, and vanishing needs the fourth.

### 1d. Dimensional regularization [established]
With n = 3 − 2ε spatial dimensions (sympy):

ρ = −m⁴/(64π² ε) + m⁴/(64π²)[ln(m²/μ̄²) − 3/2]   (MS-bar finite part checked symbolically)

and ρ + p = 0 exactly in ε (w = −1). Power divergences are absent, so the Str 1 and Str m² conditions disappear (Akhmedov hep-th/0204048 and Koksma & Prokopec arXiv:1105.6296, both verified on arXiv, reach the same conclusion: Lorentz-invariant regularization leaves only m⁴ terms, massless fields contribute nothing). What remains:
- The pole ∝ Str m⁴. If Str m⁴ ≠ 0 it is removed by a bare cosmological-constant counterterm, and the renormalized ρ runs: dρ/d ln μ = −Str m⁴/(32π²).
- The finite part ∝ Str m⁴ ln m² − (3/2) Str m⁴ (scalars, fermions). For massive vectors in Landau gauge the MS-bar constant per d.o.f. is 5/6 instead of 3/2 [established, standard Coleman-Weinberg result; scheme constant].

Status of each Pauli condition by scheme (CONSTRAINTS H2):

| condition | hard cutoff | dim-reg / Lorentz-invariant |
|---|---|---|
| Str 1 = 0 | needed (Λ⁴) | not needed |
| Str m² = 0 | needed (Λ²) | not needed |
| Str m⁴ = 0 | needed (ln Λ) | needed for μ-independence without a bare counterterm |
| Str m⁴ ln m² = 0 | needed for ρ = 0 | needed for ρ = 0 |

In both schemes Str m⁴ = 0 and Str m⁴ ln m² = 0 are required for a cancellation. These are the scheme-independent tests.

---

## 2. The SM sums with measured masses

### 2a. Counting [established]
Physical (unitary-gauge) d.o.f.: gluons 16, photon 2, W± 6, Z 3, h 1 → 28 bosonic. Quarks 6 × 3 colours × 4 = 72, charged leptons 12, ν_L 3 × 2 = 6 → 90 fermionic. Matches CONSTRAINTS G.

Goldstones: in R_ξ gauges a massive vector contributes 4 components, −2 ghosts, +1 Goldstone. In Landau gauge at the tree minimum the Goldstones and ghosts are massless and the vector gives 3 d.o.f. at mass M plus a massless remainder that cancels (4 − 1 − 2 + 1 = 3 massive, 0 net massless). So Str 1 and all Str m^{2k} are gauge-independent with weight 3 per massive vector, and only the finite constant (5/6) is scheme-specific.

Neutrinos (CONSTRAINTS A2): 2 d.o.f. each. Masses from oscillations, normal ordering, lightest = 0. The neutrino m⁴ terms are 1e-51 of the top term. The only mechanism-dependent quantity is Str 1: a Dirac mass with ν_R (excluded) would give 4 d.o.f. per neutrino and Str 1 = −68 instead of −62. Every conclusion below holds for either count.

### 2b. Numbers (`sm_pauli_sums_out.txt`) [established, given inputs]

| sum | SM value | bosons | fermions |
|---|---|---|---|
| Str 1 | −62 | +28 | −90 |
| Str m² | −2.782e5 GeV² | +7.94e4 | −3.58e5 (|F/B| = 4.5) |
| Str m⁴ | −9.939e9 GeV⁴ | +7.03e8 | −1.064e10 (|F/B| = 15.1) |
| Str m⁴ ln(m²/GeV²) | −1.03e11 GeV⁴ | | (unit-dependent since Str m⁴ ≠ 0) |

Str m⁴ is 107% top quark. With all other masses fixed, Str m⁴ = 0 would need m_t = 87.5 GeV and Str m² = 0 would need m_t = 81.2 GeV. Measured: 172.57 GeV.

### 2c. Comparison to ρ_Λ = 2.5e-47 GeV⁴ (CONSTRAINTS E4)

Hard cutoff, magnitude / ρ_Λ:

| Λ | quartic | quadratic | log |
|---|---|---|---|
| 1 TeV | 1.6e58 | 7.0e55 | 9.6e54 |
| M_Pl | 3.5e122 | 1.1e88 | 5.6e55 |

Dim-reg MS-bar, ρ(μ) / ρ_Λ: 1.1e53 (μ = M_Z), 9.1e53 (m_t), 3.1e54 (1 TeV), 2.3e55 (1e10 GeV), 5.0e55 (M_Pl).

ρ(μ) vanishes at μ* = 83.6 GeV. This is not a cancellation. The μ-dependence (dρ/d ln μ = 3.1e7 GeV⁴, i.e. 1.3e54 ρ_Λ per e-fold) is exactly what the bare counterterm absorbs, so μ* is only the renormalization scale at which the MS-bar one-loop term happens to be zero; the physical ρ is the sum of that term and the bare counterterm, which is a free parameter. A physical statement needs Str m⁴ = 0, which fails by 1e10 GeV⁴.

Neutrino sector alone (dim-reg): 6e3 to 4e4 ρ_Λ for μ from 1 eV to 1 GeV. The coincidence ρ_Λ^{1/4} = 2.24 meV ~ m_ν is not used (H1).

### 2d. Running masses (`sm_running_supertrace_out.txt`) [established method; one-loop numbers indicative]
Inputs at μ = M_t from Buttazzo et al. arXiv:1307.3536 (JHEP 12 (2013) 089, verified; fits eqs. 55-60 shifted to PDG 2024 m_t, m_H, α_s, M_W): λ = 0.12617, y_t = 0.93286, g₂ = 0.64764, g_Y = 0.35843, g₃ = 1.16516. One-loop RGEs, top Yukawa only. Convention V ⊃ λ|H|⁴, m_h² = 2λv².

Defined (couplings at μ):
- A_vac = Str M⁴/v⁴ at the EW vacuum = 4λ² + (3/16)(2g⁴ + (g²+g'²)²) − 3y_t⁴
- A_φ = Str M⁴(φ)/φ⁴ in a large Higgs background (h mass² 3λφ², 3 Goldstones λφ²) = 12λ² + (3/16)(...) − 3y_t⁴
- B_vac = Str M²/v² at vacuum (Pauli quadratic)
- B_φ = Str M²(φ)/φ² = (3/v²)(m_h² + 2M_W² + M_Z² − 4m_t²), the Veltman combination

| log10 μ/GeV | λ | A_vac | A_φ | B_vac | B_φ |
|---|---|---|---|---|---|
| 2.24 (M_t) | +0.126 | −2.09 | −1.96 | −3.93 | −3.42 |
| 10 | −0.012 | −0.20 | −0.20 | −1.03 | −1.08 |
| 16 | −0.029 | −0.042 | −0.036 | −0.47 | −0.59 |
| 19 | −0.029 | −0.008 | −0.001 | −0.29 | −0.41 |

A_vac(M_t) v⁴ = −7.7e9 GeV⁴ (MS-bar top mass, vs −9.9e9 with the pole mass). One-loop zero crossings: λ at 2.3e8 GeV (the 3-loop literature value is ~1e10 GeV, so one loop is off by ~1.6 decades), A_φ at 1.4e19, A_vac at 9e19, B_vac and B_φ none below 1e20.

**Identity (sympy, exact) [established, standard Coleman-Weinberg RG consistency]:**
16π² β_λ|_(without anomalous-dimension term λ(12y_t² − 9g² − 3g'²)) = 2 Str M⁴(φ)/φ⁴.

So the Pauli quartic condition evaluated in a Higgs background is the same statement as "the non-anomalous part of one-loop β_λ vanishes", and the Pauli quadratic condition in a background is the Veltman condition. Both have known high-scale behaviour in the SM: β_λ ≈ 0 near 1e17-1e18 GeV (Buttazzo et al.; λ(M_Pl) close to zero, Degrassi et al. arXiv:1205.6497, JHEP 08 (2012) 098, verified), and the Veltman / bare-mass coefficient vanishes only near 1e23 GeV for m_t = 173 GeV at two loops (Hamada, Kawai, Oda arXiv:1210.2538, PRD 87, 053009 (2013), verified; erratum PRD 89, 059901). My one-loop scan agrees qualitatively with both.

What these crossings mean for vacuum energy [conjecture → assessed negative]: A_vac(μ) at μ ≫ m_t is the MS-bar beta function of the cosmological-constant counterterm, which in a mass-independent scheme does not decouple heavy states and does not describe the physical low-energy vacuum energy (Koksma-Prokopec make the same point). The physical vacuum energy at our vacuum is fixed by the low-scale spectrum, where Str m⁴ = −1e10 GeV⁴. A zero of A_vac near M_Pl is a statement about coupling running, already known as Higgs near-criticality, and would at most say the high-scale cc counterterm stops running there. It does not cancel anything at our vacuum. Treating the coincidence of these crossings with M_Pl as meaningful would be the Shaposhnikov-Wetterich type argument (arXiv:0912.0208, PLB 683 (2010) 196, verified), which needs asymptotically safe gravity, outside scope.

---

## 3. SM-only structures that could relate the sums

### 3a. Rep content and anomalies (`sm_structure_check_out.txt`) [established]
Bosonic d.o.f. = 2 dim G + 4 = 28 (eaten Goldstones move between columns, the total is fixed). Fermionic d.o.f. = 30 N_g. Str 1 = 28 − 30 N_g; zero needs N_g = 14/15. No integer works.

All gauge and mixed gauge-gravitational anomalies cancel per generation (checked). These conditions are linear or cubic in hypercharges and contain no Yukawa couplings. The fermion masses are y_f v/√2 with free y_f, so anomaly cancellation cannot constrain Str m² or Str m⁴. The gravitational anomaly condition Σ Y = 0 is a trace over charges, not over d.o.f., and gives no relation to Str 1.

### 3b. Dirac sea counting conventions [established]
Section 1a shows hole theory and symmetric second quantization give the same −2ω per mode. Any other convention differs by a c-number subtraction. A mass-independent subtraction can only change the Λ⁴ term (Str 1); a mass-dependent one is the same as choosing the bare cc. Neither can produce a relation between boson and fermion masses. The "particle/antiparticle" split of a Dirac field's 4 d.o.f. is fixed by CPT (CONSTRAINTS D: particle and antiparticle count identically), so there is no freedom to reweight antiparticle contributions.

### 3c. NCG spectral action (A3) [established structure; assessed]
In the Chamseddine-Connes-Marcolli spectral action (arXiv:hep-th/0610241, Adv. Theor. Math. Phys. 11 (2007) 991, verified), the heat-kernel expansion of Tr f(D/Λ) gives a cosmological term with Λ⁴ ∝ Tr(1) over the fermion Hilbert space, Λ² ∝ Tr(D_F²) (fermion mass² sum) and Λ⁰ ∝ Tr(D_F⁴). This has supertrace-like structure but:
1. Only fermion traces appear, all with positive weight. There is no boson subtraction, so it is not a Pauli-type cancellation. The coefficients f₄, f₂, f₀ are free moments of the cutoff function, so no relation among the Λ⁴, Λ², Λ⁰ terms is predicted. [exact numerical coefficients in CCM: unverified here]
2. The finite space in CCM has 96 fermionic states (32 per generation) including ν_R, plus the σ scalar from the Majorana mass. Both are excluded (A1, A3.2). Restricting to the SM-equivalent sector removes the Majorana terms from Tr(D_F²) and Tr(D_F⁴).
3. The one mass relation CCM produce, Σ_generations Tr(m_ν² + m_e² + 3m_u² + 3m_d²) = 8 M_W² at the unification scale (form as given in van den Dungen & van Suijlekom, arXiv:1204.0328, verified via search summary; CCM primary text not read), is a high-scale boundary condition, explicitly excluded by A3.2. It is also not a supertrace: it equates a fermion mass sum to a single gauge mass, while Str m² at that order would need 6M_W² + 3M_Z² + m_H² on the boson side.

No SM-equivalent relation survives.

### 3d. Prior work [established]
Alberghi, Kamenshchik, Tronconi, Vacca, Venturi, arXiv:0804.4782 (journal ref not found; [unverified journal]) already concluded that one-loop SM vacuum-energy contributions cannot cancel without extra bosons and at least one extra massive fermion. Kamenshchik, Starobinsky, Tronconi, Vardanyan, Venturi, EPJC 78 (2018) 200, arXiv:1801.08434 (verified) extend Pauli-Zeldovich cancellation to interacting toy models. This line is therefore largely a restatement for the core negative result. What it adds: (i) explicit Dirac-sea derivation showing the fermion sign is from statistics, not antiparticles; (ii) scheme-by-scheme table of which Pauli conditions survive with SM numbers; (iii) μ* = 83.6 GeV as an explicit example of a regulator artifact (H2); (iv) the exact identity Str M⁴(φ)/φ⁴ = 8π² β_λ^(non-anom) tying Pauli's quartic condition to Higgs near-criticality, and the Pauli-quadratic vs Veltman distinction (Higgs weight 1 vs 3 from Goldstones).

Pauli's original statement: W. Pauli, lectures (ETH 1950-51), published as "Selected Topics in Field Quantization", Pauli Lectures on Physics vol. 6 (MIT Press, 1973) [unverified citation; cited via Visser].

---

## 4. Conclusion

**Negative result [established, with the numbers above].** SM antimatter, in hole-theory or any equivalent language, does not reproduce the SUSY boson/fermion vacuum-energy cancellation:
- All four Pauli conditions fail. The two scheme-independent ones fail by Str m⁴ = −9.9e9 GeV⁴ (1e54 ρ_Λ after the 1/64π²) and by a μ-dependent finite part that is 1e53-1e55 ρ_Λ.
- The fermion sign is a Fermi-statistics effect; antiparticles of bosons contribute with positive sign, so "antimatter" is not the paired object SUSY supplies.
- SM-only structures (anomaly cancellation, rep content, sea conventions) do not touch the mass sums. Str 1 = 28 − 30N_g has no integer zero.
- The only places SM supertraces vanish are at very high scales, as running-coupling statements (β_λ ≈ 0 near 1e17-1e18 GeV; Veltman zero near 1e23 GeV), which are known near-criticality facts and do not cancel the vacuum energy at our vacuum.

Since unbroken SUSY's cancellation is also lost once SUSY is broken at ≳ 1 TeV (soft breaking gives Str m⁴ of order M_SUSY⁴ or M_SUSY² m², with M_SUSY ≳ 1 TeV from CONSTRAINTS C3) [established, standard], SUSY does not solve the cc problem either. On this item the SM fails in the same way SUSY does, just by more orders of magnitude.

**Falsifiable consistency checks.** Any claimed SM-only cancellation must (a) produce m_t ≈ 87 GeV (Str m⁴) or 81 GeV (Str m²) with other masses fixed, both excluded by the measured 172.57 GeV, or (b) introduce a new contribution of size ≥ 1e10 GeV⁴/(64π²), which with SM fields only does not exist at one loop. The one-loop crossing scales above are checkable against higher-loop running (prediction: A_φ crosses zero within ~1-2 decades of the literature β_λ = 0 scale).

**Open issues.**
- One-loop running only; λ crossing is 1.6 decades low versus the 3-loop literature. Does not affect the conclusion.
- QCD condensate and Higgs potential depth (λv⁴/4 = 1.2e8 GeV⁴) are separate vacuum-energy contributions, not Pauli sums; they make the gap larger, not smaller.
- CCM spectral-action coefficients not checked against the primary text.

---

## CONSTRAINTS checklist

- **A1 (SM only):** only SM fields; SUSY used as comparison. No new particles. ✓
- **A2 (neutrino mass):** ν masses enter only via m⁴ (negligible vs top) and d.o.f. count in Str 1 (−62 with 2 d.o.f. each, −68 if Dirac). Conclusions insensitive to the mechanism. ✓
- **A3 (reformulations):** NCG spectral action used only to check for a relation; ν_R, σ, unification boundary condition all discarded; nothing derived from it. ✓
- **B1-B8 (CPT, antimatter tests):** particles and antiparticles treated identically (CPT); nothing distinguishes them. ✓ No conflict.
- **C1-C2:** PDG 2024 masses from `tools/sm_inputs.py`. ✓ **C3:** negative result, no superpartner signatures required; nothing predicted at LHC. ✓ **C4:** not used.
- **D:** couplings used only for running (`sm_running_supertrace.py`, one loop stated); CPT counting of antiparticles in loops respected.
- **E4:** all sums compared to ρ_Λ = 2.5e-47 GeV⁴. **E1-E3, E5-E10:** not used; no cosmological mechanism proposed. E7/E8: neutrino masses at oscillation minimum, within bounds.
- **F:** not relevant.
- **G:** reproduces the Pauli condition list and the 28/90 count; the Veltman combination computed separately and distinguished from Str m². The dim-reg version is stated and the result does not depend on choosing a regulator (H2). ✓
- **H1:** no numerology. The meV-scale neutrino coincidence and μ* = 83.6 GeV are flagged as non-results. ✓
- **H2:** results given in hard cutoff and dim-reg; the scheme-independent conditions (Str m⁴, Str m⁴ ln m²) fail in both. ✓
- **H3:** Dirac sea shown equivalent to standard quantization for vacuum energy; conclusion holds in standard formulation. ✓
- **H4:** all numbers from `calc/` scripts with saved outputs. ✓
