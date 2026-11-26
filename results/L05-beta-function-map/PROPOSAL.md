# L05 - Beta-function map between "antimatter" and SUSY beta functions

Target: SUSY result #2 (gauge coupling unification). Experimenter directive D4 (is there an isometry or other structure-preserving map between antimatter beta functions and SUSY beta functions?), D3 (constructive matching, not "explained by statistics").

## Idea

1. Make "antimatter beta function" precise. Two definitions are computed:
   - (i) the contribution of antiparticle one-particle states to each SM beta coefficient (Nielsen-Hughes per-helicity-state form);
   - (ii) the SM written in the CP-conjugate (all left-handed Weyl) basis, Q, u^c, d^c, L, e^c, H, where right-handed particles enter as left-handed antiparticle fields. This is the basis in which the MSSM is written.
   - (iii) Furey's Cl(6)/C⊗O ideal basis is checked and gives nothing beyond (ii) for beta functions.
2. Define a map Phi on SM field content in basis (ii): each Weyl field (particle or antiparticle field) -> chiral multiplet; the complex Higgs doublet H and its conjugate H^c = iσ₂H* (both already used in SM Yukawas) -> two independent chiral multiplets; each self-conjugate gauge field -> vector multiplet with a self-conjugate (Majorana) gaugino. Phi(SM) is exactly the minimal MSSM content.
3. Ask what Phi preserves (Dynkin/Killing data, anomaly freedom, Yukawa structure, two-loop matrices, the unification ratio B), whether it commutes with RG flow, and which part of the SM -> MSSM change in B is attributable to the antimatter-interpretable step (treating H^c as independent).

SUSY is a comparison target only. Superpartners never enter a mechanism; the line is a structural map plus an accounting of what the map needs.

## Deliverables

- `calc/beta_map.py` (sympy, exact rationals): b_i, b_ij, Yukawa c_i^f for SM and Phi(SM); NH state decomposition; partial maps; identities, all asserted.
- `calc/running.py` (numpy/scipy): 2-loop gauge running from M_Z with `tools/sm_inputs.py`, SM vs Phi(SM) with M_S = M_Z, 1, 3, 10 TeV.
- `WORK.md`: derivations, results, literature, conclusion, CONSTRAINTS checklist.
