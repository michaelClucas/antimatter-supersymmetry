# L01 - Weisskopf mechanism and the Higgs hierarchy

Targets: SUSY result #1 (hierarchy problem / cancellation of the quadratic divergence in m_h^2), secondarily #4 (radiative EWSB).

## Idea

Weisskopf showed that in hole theory the Dirac-sea (positron) contributions turn the electron self-mass divergence from linear to logarithmic: one loop in Z. Phys. 89, 27 (1934) with the erratum Z. Phys. 90, 817 (1934) (sign error found by Furry), all orders and the charged-Bose case in Phys. Rev. 56, 72 (1939), DOI 10.1103/PhysRev.56.72 [established]. That is the historical case of antimatter protecting a mass. SUSY protects the Higgs mass the same way structurally: a partner loop cancels the leading divergence. Question: does SM antimatter (the Dirac seas of the SM fermions, Feynman-Stueckelberg Z-graphs) give the Higgs any analogous protection, and can the SM break EW symmetry radiatively?

## Plan

1. Reproduce the Weisskopf cancellation in old-fashioned (time-ordered) perturbation theory, separating electron-only from pair intermediate states. Committed sympy check.
2. Do the same decomposition for the top loop in the Higgs self-energy. Identify what, if anything, cancels the quadratic piece. Fix the normalization of the Veltman coefficient and evaluate it with measured masses.
3. Run SM couplings (3-loop RGEs, NNLO matching) and locate the zero of the Veltman coefficient. Compare with Hamada-Kawai-Oda (arXiv:1210.2538), Jegerlehner (arXiv:1305.6652, preprint), Masina-Quiros (arXiv:1308.1242). Veltman condition: Veltman, Acta Phys. Polon. B 12, 437 (1981).
4. Decide whether anything is antiparticle-specific or only chiral symmetry / statistics, including the charged (W+W-, G+G-) vs self-conjugate (Z, h, G0) boson loops.
5. Coleman-Weinberg check for radiative EWSB with measured m_h, m_t.

## Expected outcome

A rigorous negative result is acceptable and likely: the Weisskopf mechanism depends on fermion statistics and chiral symmetry, and neither is available to a scalar.

## Status

Cycle 3 fix round done, see WORK.md (sections 8-10: response to referee 1, what is new, CONSTRAINTS checklist). The result is negative for #1 and #4 as an SM-antimatter mechanism. Prior art for the framing: Murayama hep-ph/0002232 sec. 1.3; Craig et al. arXiv:2205.05708 sec. 2. Nothing physically new (WORK.md section 9); candidate input to the S1 synthesis.
