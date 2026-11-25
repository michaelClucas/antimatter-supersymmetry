# L01 - Weisskopf mechanism and the Higgs hierarchy

Targets: SUSY result #1 (hierarchy problem / cancellation of the quadratic divergence in m_h^2), secondarily #4 (radiative EWSB).

## Idea

Weisskopf, Phys. Rev. 56, 72 (1939), DOI 10.1103/PhysRev.56.72, showed that in hole theory the Dirac-sea (positron) contributions turn the electron self-mass divergence from linear to logarithmic [established]. That is the historical case of antimatter protecting a mass. SUSY protects the Higgs mass the same way structurally: a partner loop cancels the leading divergence. Question: does SM antimatter (the Dirac seas of the SM fermions, Feynman-Stueckelberg Z-graphs) give the Higgs any analogous protection, and can the SM break EW symmetry radiatively?

## Plan

1. Reproduce the Weisskopf cancellation in old-fashioned (time-ordered) perturbation theory, separating electron-only from pair intermediate states. Committed sympy check.
2. Do the same decomposition for the top loop in the Higgs self-energy. Identify what, if anything, cancels the quadratic piece. Fix the normalization of the Veltman coefficient and evaluate it with measured masses.
3. Run SM couplings (3-loop RGEs, NNLO matching) and locate the zero of the Veltman coefficient. Compare with Hamada-Kawai-Oda (arXiv:1210.2538), Jegerlehner (arXiv:1305.6652), Masina-Quiros (arXiv:1308.1242).
4. Decide whether anything is antiparticle-specific or only chiral symmetry / statistics.
5. Coleman-Weinberg check for radiative EWSB with measured m_h, m_t.

## Expected outcome

A rigorous negative result is acceptable and likely: the Weisskopf mechanism depends on fermion statistics and chiral symmetry, and neither is available to a scalar.

## Status

Done, see WORK.md. The result is negative for #1 and #4 (as an SM-antimatter mechanism).
