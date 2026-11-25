"""Feynman-Stueckelberg vs time-ordered (hole-theory-like) bookkeeping of a one-loop bubble.

The energy integral of a loop with two Feynman propagators is done by residues. Each Feynman propagator
  i/(k0^2 - E^2 + i eps) = (i/2E) [ 1/(k0 - E + i eps) - 1/(k0 + E - i eps) ]
has exactly two poles: positive frequency (particle, forward in time) and negative frequency (antiparticle =
particle backward in time). Closing the contour gives exactly two time-ordered terms:
  (a) pair (particle+antiparticle) created by the external field and later absorbed  -> 1/(q0 - E1 - E2)
  (b) 'Z-graph': pair created from the vacuum before the external quantum arrives    -> 1/(q0 + E1 + E2)
There is no third term in which 'the antiparticle loop' is added separately. Check: symbolic residue sum and direct
numerical integration at finite eps.
Also: the absorptive part (pair-production threshold) fixes the normalisation via unitarity; doubling the antiparticle
contribution would double the pair-production rate (checked against data in WORK.md via R-ratio).
"""
import sympy as sp
import numpy as np
from scipy.integrate import quad

k0, q0, E1, E2 = sp.symbols("k0 q0 E1 E2", positive=True)
# integrand of  int dk0/(2 pi) [i/(k0^2-E1^2+i0)] [i/((k0-q0)^2-E2^2+i0)]
f = sp.I / (k0 ** 2 - E1 ** 2) * sp.I / ((k0 - q0) ** 2 - E2 ** 2)
# close in the lower half plane: poles with -i eps: k0 = +E1 and k0 = q0 + E2 (clockwise -> -2 pi i)
res = sp.residue(f, k0, E1) + sp.residue(f, k0, q0 + E2)
I_res = sp.simplify(-2 * sp.pi * sp.I * res / (2 * sp.pi))
topt = sp.I / (4 * E1 * E2) * (1 / (q0 - E1 - E2) - 1 / (q0 + E1 + E2))
print("residue result      :", sp.simplify(I_res))
print("two time orderings  :", sp.simplify(topt))
print("difference          :", sp.simplify(I_res - topt))

# numerical check at finite eps, q0 below threshold
def num(q0v, e1, e2, eps=1e-3):
    def g(k):
        return (1j / (k * k - e1 * e1 + 1j * eps)) * (1j / ((k - q0v) ** 2 - e2 * e2 + 1j * eps))
    re = quad(lambda k: g(k).real, -200, 200, points=[-e1, e1, q0v - e2, q0v + e2], limit=2000)[0]
    im = quad(lambda k: g(k).imag, -200, 200, points=[-e1, e1, q0v - e2, q0v + e2], limit=2000)[0]
    return (re + 1j * im) / (2 * np.pi)

for (qv, a, b) in ((0.7, 1.0, 1.3), (1.5, 1.0, 1.0)):
    exact = complex(topt.subs({q0: qv, E1: a, E2: b}))
    print(f"q0={qv}, E1={a}, E2={b}: numeric {num(qv, a, b):.5f}   two-ordering formula {exact:.5f}   "
          f"(counting the Z-graph ordering twice would give {2*exact - complex((sp.I/(4*E1*E2)*(1/(q0-E1-E2))).subs({q0:qv,E1:a,E2:b})):.5f})")
