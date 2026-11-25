# L05 WORK - beta-function map: SM in antiparticle labelling vs SUSY

All numbers below are printed by `calc/beta_map.py` (exact, all asserted; output `calc/beta_map.txt`) and `calc/running.py` (output `calc/running.txt`). Run from `calc/`: `python beta_map.py`, `python running.py`.

Conventions: dg_i/dlnμ = g_i³/(16π²) b_i + g_i³/(16π²)² [Σ_j b_ij g_j² − Σ_f c_i^f y_f²]. g₁ GUT-normalised (T₁ = (3/5)Y²·dim). S_i(field) = Dynkin index under G_i times dimension under the other factors; C_i(field) = quadratic Casimir (C₁ = (3/5)Y²).

---

## 1. What "antimatter beta function" can mean

### 1.1 Definition (i): antiparticle-state contribution [established mechanism, new bookkeeping]

The one-loop coefficient can be written as a sum over one-particle helicity states (Nielsen-Hughes form):

b_i = −(1/2) Σ_states (−1)^{2s} [(2s)² − 1/3] T_i(state)

Check: two vector states in the adjoint give −(11/3)C(G); a Weyl field (particle state in R, h=−1/2; antiparticle state in R̄, h=+1/2) gives (2/3)T(R); a complex scalar gives (1/3)T(R). `beta_map.py` §2 reproduces (41/10, −19/6, −7) this way. The (2s)² term is the spin (paramagnetic) piece, the −1/3 term the orbital (diamagnetic) piece.

Split by CPT class of the state:

| part | b | B |
|---|---|---|
| self-conjugate states (gauge bosons) | (0, −22/3, −11) | 1/2 |
| particle states | (41/20, 25/12, 2) | −5/2 |
| antiparticle states | (41/20, 25/12, 2) | −5/2 |

Particle and antiparticle parts are identical exactly: CPT maps (R, h) to (R̄, −h), T(R) = T(R̄), and the summand depends on s² only. This is the CONSTRAINTS D statement in per-state form. [established]

**Proposition 1** [established, elementary]. b_i is a sum over the SM state set, so it is invariant under any relabelling of which states are called "particle" and which "antiparticle" (including the conjugate-field relabelling of §1.2). Any "antimatter beta function" that is a CPT-invariant function of the SM states gives back the SM b_i and B = 115/218. Changing B requires changing the state set.

### 1.2 Definition (ii): CP-conjugate (all-LH) field basis [established]

Q(3,2,1/6), u^c(3̄,1,−2/3), d^c(3̄,1,1/3), L(1,2,−1/2), e^c(1,1,1), H(1,2,1/2); H^c ≡ iσ₂H* is (1,2,−1/2). The SM Yukawas in this basis (hypercharge sums zero) are y_t Q H u^c, y_b Q H^c d^c, y_τ L H^c e^c (SU(2) indices contracted with ε): the SM already uses both H and its conjugate.

| fields | b | B |
|---|---|---|
| antiparticle fields u^c, d^c, e^c | (16/5, 0, 2) | −5/8 |
| particle fields Q, L | (4/5, 4, 2) | −5/8 |
| one full generation (Weyl) | (4/3, 4/3, 4/3) | undefined (b ∝ (1,1,1)) |

Each generation is a complete SU(5) set (10 = Q + u^c + e^c, 5̄ = d^c + L), so matter shifts b along (1,1,1) and drops out of B. Note the 10 and 5̄ each mix particle and antiparticle fields; neither "antiparticle fields" nor "particle fields" alone is SU(5)-complete. [established]

### 1.3 Definition (iii): Furey ideal basis

Furey, "Charge quantization from a number operator", PLB 742 (2015) 195, arXiv:1603.04078, DOI 10.1016/j.physletb.2015.01.023 [abstract verified]: one generation from ladder operators of C⊗O, number operator/3 = electric charge, SU(3)_c × U(1)_em generators. The minimal left ideal organises states as 1 ⊕ 3 ⊕ 3̄ ⊕ 1 graded by charge, mixing particle and antiparticle states in one ideal (which states sit in which ideal: from memory of the full text, [unverified]). Scope A3: this sector is equivalent to the SM only for SU(3)_c × U(1)_em (below the EW scale); the unification test needs SU(2)_L × U(1)_Y. Beta coefficients depend only on representation content (A3.4), so (iii) gives the same b as (ii) in the equivalent sector and adds nothing here. Dixon's R⊗C⊗H⊗O was not used.

**Chosen definition**: (ii), with (i) as the per-state decomposition. (ii) is the only one in which a SUSY completion is even definable, since chiral superfields must be left-chiral.

---

## 2. The map Phi

On SM content in basis (ii):

- each LH Weyl field (Q, L and antiparticle fields u^c, d^c, e^c) -> chiral multiplet in the same rep;
- the complex scalar H and its conjugate H^c -> two independent chiral multiplets (H_u ≡ H in (1,2,+1/2), H_d ≡ H^c in (1,2,−1/2)); scalars carry no chirality, so the scalar sits in both chiral classes;
- each self-conjugate (real adjoint) gauge field -> vector multiplet with a self-conjugate (Majorana) gaugino;
- Yukawas: y_t Q H u^c -> y_t Q H_u u^c, y_b Q H^c d^c -> y_b Q H_d d^c, y_τ L H^c e^c -> y_τ L H_d e^c.

Phi(SM) = minimal MSSM content. [established: this is the standard construction, e.g. Martin, "A Supersymmetry Primer", hep-ph/9709356 (verified exists), §6.1. Standard justification of the second doublet is holomorphy plus higgsino anomaly cancellation; the reading "H^c promoted to an independent field" is the antimatter-labelled description of the same step.]

**Scope warning**: promoting H^c to an independent field IS a second Higgs doublet, which A1 forbids as a mechanism. In the SM, H^c is the same field as H; counting it twice is double counting.

### 2.1 One loop

| | b | B |
|---|---|---|
| SM | (41/10, −19/6, −7) | 115/218 = 0.5275 |
| Phi(SM), NSVZ −3C(G) + Σ_chiral S | (33/5, 1, −3) | 5/7 = 0.7143 |
| Phi(SM), components via NH | (33/5, 1, −3) | identical (asserted) |
| data (one loop, α_i⁻¹(M_Z)) | | 0.7178 |

**Spin/orbital structure** [established arithmetic; the presentation is ours]:

- b = −2 Str(s² T) + (1/6) Str(T), Str over helicity states with (−1)^{2s}.
- In every supermultiplet Str(T) = 0, so Phi(SM) has zero orbital part (asserted). SM orbital part = (−19/10, −7/6, −1).
- SM spin part = (6, −2, −6), B = 1/2 exactly.
- b[Phi(SM)] − b_spin[SM] = (3/5, 3, 3) = C(G) [Majorana gauginos] + 2 S(H) [higgsino pair] (asserted).

So: **MSSM b = (spin part of SM b) + (self-conjugate adjoint Weyl fermions) + (one Dirac fermion with the Higgs's charges)**. The higgsino pair H̃_u, H̃_d is a single Dirac fermion whose particle and antiparticle states carry the H and H^c quantum numbers. Adding the Majorana gaugino to the SM spin part leaves B = 1/2 (gauge weight −4 -> −3, no Higgs term). All of B − 1/2 in the MSSM comes from the Dirac higgsino. In the SM all of B − 1/2 comes from the Higgs orbital term (the two scalar charge states, particle and antiparticle, T/6 each).

### 2.2 Why only gauge and Higgs matter for B

Complete multiplets drop out, so with c = gauge weight, h = weight per Higgs doublet, n = number of doublets:

B = (c − nh/2)/(2c + nh/5),  depends only on r = nh/c.

Pure gauge + complete multiplets: B = 1/2 for any c. Data B = 0.718 needs r ≈ −0.68. SM r = −1/11, MSSM r = −2/3. r_MSSM/r_SM = 22/3 = 2 (H^c doubling) × 3 (scalar -> chiral) × 11/9 (vector -> vector multiplet).

Partial maps (`beta_map.py` §4, `running.py` one-loop α_s from exact unification, all thresholds at M_Z):

| map | r | B | α_s(M_Z) predicted |
|---|---|---|---|
| SM | −1/11 | 0.5275 | 0.0711 |
| gauge -> vector multiplet only | −1/9 | 0.5337 | 0.0720 |
| **H^c promoted only (the antimatter step)** | −2/11 | 0.5556 | 0.0755 |
| H -> chiral only | −3/11 | 0.5841 | 0.0806 |
| H, H^c chiral, no gaugino | −6/11 | 0.6731 | 0.1021 |
| full Phi(SM) | −2/3 | 0.7143 | 0.1166 |
| measured | | | 0.1180 ± 0.0009 |

The antimatter-interpretable step alone moves B by 0.028 of the 0.187 needed (15%); in r it supplies a factor 2 of 22/3. The rest needs spin-1/2 partners. [established arithmetic]

### 2.3 Two loop: an exact homothety

SM b_ij = [[199/50, 27/10, 44/5], [9/10, 35/6, 12], [11/10, 9/2, −26]] (Machacek-Vaughn component formula, asserted against the known matrix).
Phi(SM) b_ij = [[199/25, 27/5, 88/5], [9/5, 25, 24], [11/5, 9, 14]] (SUSY formula −6C²δ + Σ_chiral (4C_j + 2C_iδ)S_i; also obtained as components + gaugino-Yukawa term −2Σ[S_iC_j + δ_ij C_i S_i], asserted equal).

**Identity** [established arithmetic, asserted]: Phi(SM) b_ij = 2 · SM b_ij for every i ≠ j and for (1,1). The diagonal non-abelian remainder is C_i[(50/3)C_i − (14/3)W_i + (8/3)S_{H,i}] = (0, 40/3, 66).

Mechanism: off-diagonal weight per Weyl field is 2C_jS_i in the SM and 4C_jS_i per chiral multiplet (= Weyl 2 + sfermion 4 − gaugino Yukawa 2); a complex scalar has 4C_jS_i, and Phi gives the Higgs two chiral multiplets, 8C_jS_i. **The uniform factor 2 holds only if H^c is counted as an independent field**: without it the off-diagonal ratios are 5/3 or 2 (asserted). This is the one place where the conjugate-field step turns Phi into a scale map (homothety) on part of the beta-function data. Literature search did not find this identity stated (a search-engine comparison of the matrices noticed it; no source found) [novelty unverified].

### 2.4 Two-loop Yukawa coefficients

| | SM c_i | Phi(SM) c_i | Higgs-leg term |
|---|---|---|---|
| y_t | (17/10, 3/2, 2) | (26/5, 6, 4) | (9/5, 3, 0) |
| y_b | (1/2, 3/2, 2) | (14/5, 6, 4) | (9/5, 3, 0) |
| y_τ | (3/2, 1/2, 0) | (18/5, 2, 0) | (3/5, 1, 0) |

c^Phi = 2 c^SM + 2(N/d_i)C_i(Higgs leg). In the SM only the two fermion legs carry Casimirs; in SUSY all three legs do, with weight 2. So the Yukawa sector is also "doubled plus the Higgs leg" (asserted against the known values).

### 2.5 What the map does to the running (`running.py`)

Inputs: tools/sm_inputs.py (α⁻¹ = 59.005, 29.589, 8.475 at M_Z), Yukawas at M_Z from tools/rg_sm.py run down from M_t. 2-loop gauge, 1-loop Yukawa, tanβ = 10, no threshold corrections, no MS-bar -> DR-bar shift [approx, O(0.1) in α⁻¹].

| model | min spread of α_i⁻¹ (2-loop) | at | α_s(M_Z) for exact unification |
|---|---|---|---|
| SM | 3.20 | 10^14.23 | 0.0738 |
| Phi(SM) from M_Z | 0.40 | 10^16.30 | 0.1289 |
| Phi(SM) from 1 TeV | 0.09 | 10^16.11 | 0.1202 |
| Phi(SM) from 3 TeV | 0.05 | 10^16.03 | 0.1168 |
| Phi(SM) from 10 TeV | 0.21 | 10^15.93 | 0.1130 |

These reproduce the standard MSSM results (cf. L02 `unification.txt`: SM 2-loop spread 3.19-3.20, MSSM 1 TeV 0.12) and the known MSSM-at-M_Z overshoot α_s ≈ 0.13 (Langacker & Polonsky, PRD 47, 4028 (1993), hep-ph/9210235 [unverified for exact number]).

### 2.6 Isometry / RG commutation

- **Rep-space metric** (Dynkin index / Killing form tr_R(T^aT^b) = T(R)δ^ab): Phi is the identity on the rep data of every fermion and every gauge field, so it is an isometry on those sectors. On the scalar sector it sends H to H ⊕ H^c, doubling the norm; not an isometry. [established, trivial]
- **b-space**: any two vectors in R³ are related by many linear maps; that carries no information. The unification test sees b only through its class in P(R³/⟨(1,1,1)⟩) ≅ RP¹, coordinate B. Maps b -> λb + μ(1,1,1) (λ > 0) preserve the unification verdict; adding complete multiplets is such a map. Phi is not: it moves B from 115/218 to 5/7. Phi creates unification; it does not preserve it.
- **RG flow**: one-loop flow in α⁻¹ space is translation by −b t/2π. Phi acts on theory space (field content), not on coupling space. With identical data at M_S the trajectories split immediately; there is no nontrivial map on coupling space intertwining the two flows other than the trivial affine ones of the previous point. Phi does not commute with RG flow in any non-trivial sense.
- **Two loops**: the nearest thing to a structure-preserving property is §2.3, a homothety by 2 on the inter-group block of b_ij (and b₁₁), which requires H^c to be independent.

---

## 3. Literature

- Nielsen, "Asymptotic freedom as a spin effect", Am. J. Phys. 49, 1171 (1981) [citation verified via secondary sources]; Hughes, Phys. Lett. B 97, 246 (1980) and Nucl. Phys. B 186, 376 (1981) [unverified]. Source of the per-state formula used in §1.1.
- NSVZ: Novikov, Shifman, Vainshtein, Zakharov, Nucl. Phys. B 229, 381 (1983) [citation verified via secondary sources]. Gives −3C(G) + Σ T(1 − γ).
- Machacek & Vaughn, Nucl. Phys. B 222, 83 (1983) [unverified page]: general two-loop gauge betas (component formula used in §2.3).
- Jones, Phys. Rev. D 25, 581 (1982) [unverified]: two-loop SUSY gauge betas.
- Martin & Vaughn, PRD 50, 2282 (1994), hep-ph/9311340 [verified]: two-loop soft-term RGEs, MSSM specialisation.
- Martin, hep-ph/9709356 [verified]: MSSM written with u^c, d^c, e^c and H_u, H_d; holomorphy/anomaly reason for two doublets.
- Amaldi-de Boer-Fürstenau, Langacker-Luo, Ellis-Kelley-Nanopoulos (CONSTRAINTS D): MSSM unification. Georgi-Quinn-Weinberg PRL 33, 451 (1974): B test.
- Furey PLB 742, 195 (2015), arXiv:1603.04078 [abstract verified].
- Not found in a limited search: any paper presenting SM -> MSSM beta coefficients as a map in the conjugate basis, the spin-part decomposition b_MSSM = b_spin(SM) + gauginos + Dirac higgsino, or the two-loop off-diagonal doubling identity. All three are elementary consequences of known formulas; they are probably known to specialists but I could not cite them. [novelty unverified]

---

## 4. Conclusion

1. **Definition.** The natural "antimatter beta function" is the SM in CP-conjugate (all-LH Weyl) labelling, definition (ii). The per-state version (i) gives antiparticle contribution = particle contribution exactly (41/20, 25/12, 2), and Proposition 1: no CPT-invariant relabelling of SM states changes b or B. [established]
2. **The map.** Phi (Weyl field incl. u^c, d^c, e^c -> chiral; H and H^c -> two chiral; self-conjugate gauge field -> vector multiplet with self-conjugate gaugino) is natural, needs the conjugate basis to be defined, and sends SM content exactly to MSSM content. It is the standard MSSM construction in antimatter-labelled language. [established]
3. **What it preserves.** Rep/Dynkin data of fermions and gauge fields (isometry there), anomaly freedom, the Yukawa structure, SU(5) completeness of matter (so matter stays irrelevant to B). At two loops it acts as exact multiplication by 2 on all off-diagonal b_ij and b₁₁, and this uniformity holds iff H^c is an independent field. [established arithmetic; interpretation conjecture]
4. **What it does not preserve.** B: 115/218 -> 5/7. It does not commute with RG flow. It is not an isometry of b-space or coupling space under any natural metric found.
5. **Does it carry SM to MSSM unification?** Yes by construction (2-loop spread 3.20 -> 0.09 at M_S = 1 TeV). But the B shift is produced by new states. The only antimatter-interpretable step (H^c independent) supplies a factor 2 of the required 22/3 in r and 15% of the B shift, and it is itself a second Higgs doublet (A1-forbidden as a mechanism). The other 85% needs gaugino/higgsino spin-1/2 states. In the spin decomposition all of the MSSM's B − 1/2 comes from one Dirac fermion with the Higgs's charges, which the SM does not have (L has H^c's quantum numbers but is a single Weyl field). [established arithmetic]
6. **Net for D4.** A natural, antimatter-labelled, structure-preserving map exists (Phi), but it is SUSY completion; it does not turn SM antimatter into a mechanism for unification. It gives a precise accounting: SM-only content cannot reach B ≈ 0.72 under any CPT-respecting reinterpretation (Prop. 1), and the gap is exactly the Dirac-higgsino spin term plus the gaugino correction to the gauge term.
7. **Falsifiable consequence.** None for SM experiments: the line makes no new SM prediction. Checkable mathematical claims: Prop. 1; the homothety identity of §2.3; the decomposition of §2.1. A conditional consequence: if any future SM-only reformulation claims MSSM-like unification, it must change r by 22/3 without new states; Prop. 1 says a relabelling of particle/antiparticle states cannot do that, so such a claim would have to change the state set or the loop weights (L02's reweighting territory, already constrained there).

Open questions: (a) does the two-loop homothety extend to three loops (needs MSSM 3-loop gauge betas, Jack-Jones-Kord hep-ph/0308231 [unverified])? (b) is there an interpretation of the diagonal remainder C_i[(50/3)C_i − (14/3)W_i + (8/3)S_{H,i}]? (c) the Furey/Dixon ideal structure in the full SU(3)×SU(2)×U(1) sector was not examined.

---

## CONSTRAINTS checklist

- **A1** SM antimatter only: No mechanism uses non-SM content. MSSM / Phi(SM) is a comparison target only. The H^c-promotion step is identified explicitly as a second Higgs doublet, i.e. forbidden as a mechanism; it is used only to describe the map. Pass.
- **A2** Neutrino mass: no neutrino mass term used; no ν_R in either content. Insensitive. Pass.
- **A3** Reformulations: (ii) is a relabelling of the same fields (equivalent). (iii) Furey: restricted to SU(3)_c × U(1)_em where equivalence holds; not used for any number. Results hold in the standard formulation (A3.4). Pass.
- **B1-B4, B6** CPT/mass/charge/moment/spectroscopy tests: nothing treats antiparticles differently; Prop. 1 is a CPT identity. Pass.
- **B5** ALPHA-g: gravity not involved. Pass.
- **B7, B10** EDMs: no new CP violation. Pass.
- **B8, B9** CKM CP violation: not used; beta coefficients are CP-blind at this order. Pass.
- **C1** m_H: enters only through tools/rg_sm.py matching for Yukawas at M_Z. Pass.
- **C2** EW/top inputs: from tools/sm_inputs.py (PDG 2024). Pass.
- **C3** LHC SUSY limits: the line predicts no superpartners; the comparison target with M_S ≤ 1 TeV is excluded for coloured states (gluino 2.2-2.4 TeV), which is why M_S = 3, 10 TeV are also shown. No superpartner signatures expected because none exist in the mechanism. Pass.
- **C4** muon g-2: not addressed, not claimed. Pass.
- **D** Gauge couplings: PDG 2024 values via tools/; loop order stated (2-loop gauge, 1-loop Yukawa; one-loop B). CPT identity of D reproduced as §1.1. Pass.
- **E2, E3** baryon density / η: not used. Pass.
- **E4** dark energy: not used. Pass.
- **E6, E7, E8** N_eff, neutrino masses: no new light states. Pass.
- **E9** symmetric cosmologies: not used. Pass.
- **E10** baryogenesis: not used. Pass.
- **F1** proton decay: Phi(SM) unification scale 10^16.0-16.3 GeV is in the comparison target only; no GUT is proposed. Pass (n/a).
- **F2** sphalerons: not used. Pass.
- **F3** n-n̄: not used. Pass.
- **G** hierarchy / vacuum energy facts: not used. Note for L04: the orbital piece Str(T)/6 is a charge-weighted supertrace of the same type as the Pauli conditions; no claim made. Pass.
- **H1** No numerology: every number follows from field content via standard formulas; no fitting. The 15% / factor-2 attribution is an exact decomposition, not a fit. Pass.
- **H2** Regulator independence: one-loop b_i and two-loop b_ij for gauge couplings are scheme-independent in mass-independent schemes; the MS-bar vs DR-bar shift of the running is noted as [approx]. Pass.
- **H3** Interpretations not mechanisms: the conjugate basis and per-state split are relabellings; Prop. 1 states they cannot change b. Pass.
- **H4** Every quantitative claim is in calc/beta_map.py or calc/running.py with outputs committed alongside. Pass.

---

## Cycle 4: derivation of the doubling identity

Scripts: `calc/c4_doubling.py` (output `c4_doubling.txt`) and `calc/c4_threeloop.py` (output `c4_threeloop.txt`). Both use exact sympy rationals and assert every identity. Literature coefficients were copied from the arXiv TeX sources, not from memory.

### C4.1 Formulas used and how they were checked

- Non-SUSY two-loop gauge coefficient (Machacek-Vaughn, NPB 222 (1983) 83, product-group form), with Weyl fermions F, complex scalars S_c and real scalars S_r:
  b_ij = 2 Σ_F S_i C_j + 4 Σ_Sc S_i C_j + 2 Σ_Sr S_i C_j + δ_ij C(G_i) [−34/3 C(G_i) + 10/3 Σ_F S_i + 2/3 Σ_Sc S_i + 1/3 Σ_Sr S_i].
  Yukawa term: c_i = (1/d(G_i)) Σ_triples |Y|² × (C_i of the two fermion legs only).
  Checked [established]: it reproduces the full n_G-dependent SM two-loop matrix of Mihaila-Salomon-Steinhauser, PRL 108 (2012) 151602, arXiv:1201.5868, eq. (5), with b_ij = 16 × their coefficient. It also reproduces their y_t term (17/160 → c_1^t = 17/10).
- SUSY two-loop (Jones PRD 25 (1982) 581 [unverified page]; Martin-Vaughn hep-ph/9311340): b_ij = −6 C(G_i)² δ_ij + Σ_chiral S_i [4 C_j + 2 C(G_i) δ_ij]. Yukawa term: c_i = (1/d(G_i)) Y^{ijk}Y_{ijk} C(k), summed over all three legs.
  Checked [established]: it reproduces b_ij(n_g) and a_i = (26/5, 6, 4) tr T, (14/5, 6, 4) tr B, (18/5, 2, 0) tr E from Ferreira-Jack-Jones, PLB 387 (1996) 80, hep-ph/9605440. It was also re-derived from components, asserted equal for every model tested. The components are: Weyl fermion, complex scalar, Majorana gaugino, and the gaugino Yukawa −√2 g φ* T^a ψ λ^a entering through the MV Yukawa term.

### C4.2 Derivation [established]

Per-field weights in b_ij. Notation: S_i = index under G_i times the dimension under the other factors, C_j = Casimir under G_j, CG = C(G_i).

| field | off-diagonal part | δ_ij part |
|---|---|---|
| Weyl fermion | 2 S_i C_j | 10/3 CG S_i |
| complex scalar | 4 S_i C_j | 2/3 CG S_i |
| real scalar | 2 S_i C_j | 1/3 CG S_i |
| gaugino Yukawa (per chiral) | −2 S_i C_j | −2 CG S_i |
| **chiral multiplet (sum)** | **4 S_i C_j** | **2 CG S_i** |
| vector multiplet | 0 | −34/3 CG² + 16/3 CG² = −6 CG² |

Off-diagonal: a chiral multiplet carries weight 4, twice the Weyl weight of 2. A complex scalar carries 4, so doubling it needs 8, i.e. two chiral multiplets with the same (S_i, C_j). In Φ, H → chiral H_u and H^c → chiral H_d gives exactly 8. Hence

b_ij^MSSM = 4 Σ_Weyl S_iC_j + 4·[S_iC_j(H) + S_iC_j(H^c)] = 2·(2 Σ_Weyl S_iC_j + 4 S_iC_j(H)) = 2 b_ij^SM.

This holds term by term (matter and Higgs separately) and identically in n_G. `c4_doubling.py` §1 gives MSSM − 2·SM = diag(0, 208/3 − 56 n_G/3, 150 − 28 n_G).

- **Why b_11 doubles.** Every δ_ij term is proportional to C(G_i), and C(U(1)) = 0. So the abelian diagonal entry has the same form as an off-diagonal one: there is no gauge self-interaction and the U(1) gaugino is neutral.
- **Why b_22, b_33 do not double.** The δ_ij parts are not in ratio 2. These are the gauge loop (−34/3 C²), the gaugino (+16/3 C²), and the C(G)-weighted matter terms (10/3 and 2/3 in the SM vs 2 in SUSY). A non-abelian diagonal entry doubles iff 25 C(G) = 7 Σ_F S − 4 Σ_Sc S. In the SM this fails: SU(2) gives 50 vs 40, SU(3) gives 75 vs 42.
- **Role of H^c.** The identity needs the second Higgs chiral multiplet to have the same S_i, C_j as H. Conjugation guarantees this, since S and C are invariant under R → R̄. But b_ij cannot tell H^c from a second Y = +1/2 doublet: both give the same numbers (asserted). The conjugate is selected by higgsino anomaly cancellation and holomorphy, not by the beta function. Without H^c the off-diagonal ratios are 5/3 for (1,2) and (2,1), and 389/199 for (1,1).
- **Yukawa terms (full result).** c_i^MSSM = 2 c_i^SM + (Higgs-leg term). Example, y_t: (26/5, 6, 4) = 2·(17/10, 3/2, 2) + (9/5, 3, 0). The fermion legs double exactly. The scalar leg is absent from the non-SUSY two-loop Yukawa term, so in the MSSM it is an extra contribution. Only c_3 doubles, because the Higgs is colourless. So the gauge-only part of b_ij doubles (off-diagonal entries and (1,1)), but the full two-loop gauge beta function (gauge + Yukawa) does not. Numerically there is also y_f^MSSM = y_f^SM / sinβ or / cosβ on top.

### C4.3 Antimatter phrasing [established arithmetic; interpretation conjecture]

Test A: let T_dbl = SM plus an independent CP-conjugate copy of every Weyl field and of H, with the gauge fields counted once. Then b_ij(T_dbl) = b_ij(MSSM) for every off-diagonal entry and for (1,1) (asserted). The diagonal entries (2,2), (3,3) are 57, 50 vs 25, 14. The statement that survives:

> The off-diagonal (and abelian) two-loop MSSM coefficients equal the SM coefficients computed with every SM state and its CP conjugate counted as independent fields.

This is true but says nothing specific to antimatter. S_i and C_j are CPT-blind, so an independent conjugate copy and an independent identical copy give the same numbers. In per-state language, b_ij(off) = Σ_states w S_iC_j, with w = 1 per fermion state set (particle (R, −1/2), antiparticle (R̄, +1/2)) and w = 2 per scalar state set. A chiral multiplet then has 1 + 1 + 2 + 2 − 2 (gaugino Yukawa) = 4 = 2 × Weyl. T_dbl is a vector-like (mirror) doubling of the SM, which A1 forbids as a mechanism.

Side result: at one loop b(T_dbl) = (41/5, 1, −3) vs MSSM (33/5, 1, −3). The b_2 and b_3 entries coincide because 2C(G) = Σ_F S − 4 Σ_Sc S holds for SU(2) (4 = 4) and SU(3) (6 = 6), and that needs n_G = 3. [established arithmetic; coincidence of n_G = 3]

### C4.4 Generality: theorem [established, proof above]

**Theorem.** Let T be any gauge theory with group Π G_i, Weyl fermions F, complex scalars S_c and real scalars S_r. Let Φ*(T) be T supersymmetrized as follows:
- a vector multiplet for every G_i;
- one chiral multiplet for each Weyl fermion in F and each real scalar in S_r;
- two chiral multiplets s, s′ for each complex scalar s in S_c, where s′ has the same (S_i, C_j) as s. The anomaly-safe choice is s′ = s̄.

Then b_ij[Φ*(T)] = 2 b_ij[T] for all i ≠ j and for every abelian i = j. Proof: b_ij is linear in field content, and the weight table of C4.2 gives the factor 2 field by field.

Tests (`c4_doubling.py` §4):
- SM with n_H = 0, 1, 2 doublets: ratio 2 in every off-diagonal entry.
- Toy SU(2)×U(1) with vector-like leptons and complex scalars (2,1/2) and (3,1): ratio 2.
- SU(5) with 3(5̄+10) + 5_H + real 24_H: simple group, so there are no off-diagonal entries; the diagonal does not double.
- Counterexample to "minimal supersymmetrization doubles": SU(2)×SU(3) with a complex scalar in the real rep (3,8). Its minimal SUSY completion is one chiral (3,8), since nothing in anomalies or holomorphy forces a second one, and the off-diagonal ratio is then 26/25. With two chirals (Φ*) the ratio is 2. With a real (3,8) scalar and one chiral it is also 2.

So the identity is general, but it is a statement about Φ*, not about minimal SUSY. The two agree whenever each complex scalar's higgsino needs a partner, which is true for any U(1)-charged scalar and any scalar in a complex rep. The SM is such a case. The only SM-specific input is that the SM's one scalar carries U(1) charge.

### C4.5 Three loops [established numbers; scheme caveat]

Sources:
- SM in MS-bar: arXiv:1201.5868 eq. (5), with c = 64 × their coefficient and y_b = y_τ = 0.
- MSSM in DR-bar: hep-ph/9605440, whose gauge part comes from Jack-Jones-North hep-ph/9606323. Jack-Jones-Kord (hep-ph/0308231, PLB 579 (2004) 180, checked) covers soft-term running and points to hep-ph/9605440 for the gauge betas.

Three-loop coefficients depend on the scheme. The one-loop conversion g_DR = g_MS(1 + C(G)g²/96π²) (Martin-Vaughn PLB 318 (1993) 331, hep-ph/9308222; formula [unverified from full text]) changes only c_i(jj) with j ≠ i, by −2 k_j b_ij (derived symbolically in §0). Both the raw and the converted comparisons are printed.

Result: **no uniform ratio on the mixed block.** At n_G = 3 (MS-bar) the MSSM/SM ratios are −3.59, −1.54, −1.02, 0.29, 0.33, 0.62, 0.84, 5.21, 5.23, 5.29 and 8, including sign flips. The gauge × y_t terms are also non-uniform, with ratios from 0.64 to 4.6.

Two uniform sub-structures remain:
1. Fully mixed terms g_i³g_j²g_k² (i, j, k distinct) and the abelian single-matter-loop pieces have weight −2 S_iC_jC_k per Weyl fermion and −16 per chiral multiplet. The ratio is **8 = 2³**, and it does not change under any g_j → g_j(1 + k_j g_j²). Only Q contributes, so the scalar weight is not tested here (no SM scalar is coloured).
2. The two-matter-loop (n_G²) parts of all mixed entries equal κ b_ij^m b_j^m, with κ_SM = −11/12 and κ_MSSM = −3/2. The ratio is **54/11** = 2 (two-loop doubling) × 3/2 (one-loop matter, chiral/Weyl) × 18/11. It is unchanged under the MS↔DR conversion, but not under general matter-dependent redefinitions.

The pieces containing the Higgs (n_G⁰) break any uniform scaling, e.g. c_1(12) is 783/800 in the SM and −27/25 in the MSSM. Part of this is structural. The SM quartic λ appears as a separate term in the three-loop gauge betas, while the MSSM quartics are D-terms that already sit inside the gauge terms. A fair comparison of the Higgs sector would need the D-term substitution and tanβ, which was not done. [conjecture: it would not restore a uniform ratio]

### C4.6 Conclusion

1. **Theorem, not SM coincidence** [established]. The two-loop off-diagonal and abelian doubling holds for any gauge theory under Φ* (one chiral multiplet per Weyl fermion and per real scalar, two per complex scalar). It all follows from one fact: a chiral multiplet's mixed weight 4 S_iC_j is twice a Weyl fermion's and equal to a complex scalar's.
2. **For D4.** The structure-preserving map is Φ* acting on field content. What it preserves is the two-loop mixed-gauge block, up to a factor 2 (a homothety). The only antimatter input is that the second Higgs multiplet must have H's (S, C), and the conjugate H^c has them. The beta function cannot tell H^c from any other copy, so the identity does not single out antimatter. At three loops it is no longer a uniform scaling: the per-multiplet factor becomes 2³ for single-matter-loop mixed terms and 54/11 for two-matter-loop terms, and the Higgs and gaugino pieces are non-uniform. [established arithmetic; interpretation conjecture]
3. **Novelty.** Once the weight table is written down, the identity follows in two lines from standard formulas, so it is probably implicit in the literature. The literature check is running in parallel. [novelty unverified]
4. **Checkable consequences.**
   (a) Any model obtained from a non-SUSY parent by Φ* has b_ij^off = 2 b_ij^off(parent). This can be checked against published two-loop tables.
   (b) A general three-loop product-group formula (e.g. Mihaila-Salomon-Steinhauser PRD 86 (2012) 096008, arXiv:1208.3357 [unverified]) would give the fully-mixed weight w_S of a complex scalar. Under Φ*, two chiral multiplets give −32, so a 2³ scaling would need w_S = −4. If w_S ≠ −4, Φ* has no uniform three-loop version even for the fully-mixed term. Not done here.
   (c) There is no consequence for SM experiments, and nothing in this section is a mechanism.

CONSTRAINTS: no change from the checklist above. Φ*, T_dbl and the MSSM are comparison targets only (A1). T_dbl and treating H^c as an independent field are A1-forbidden as mechanisms. H1: no fitting, every identity is exact. H2: the three-loop scheme dependence is stated and the MS↔DR shift is computed.
