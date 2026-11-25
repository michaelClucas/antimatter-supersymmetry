"""L04 step 3: does SM representation content / anomaly cancellation constrain the Pauli supertraces?
Run: python sm_structure_check.py"""
from fractions import Fraction as Fr
import os
out = []; P = lambda *a: out.append(" ".join(str(x) for x in a))
# one generation of left-handed Weyl fermions: (name, SU3 dim, SU2 dim, Y) with Q = T3 + Y
gen = [("Q", 3, 2, Fr(1, 6)), ("u^c", 3, 1, Fr(-2, 3)), ("d^c", 3, 1, Fr(1, 3)), ("L", 1, 2, Fr(-1, 2)), ("e^c", 1, 1, Fr(1))]
n_weyl = sum(a*b for _, a, b, _ in gen)
P(f"Weyl fermions per generation (no nu_R): {n_weyl}  -> real fermionic d.o.f. {2*n_weyl}")
anoms = {
 "SU3^2 U1": sum(b*y for _, a, b, y in gen if a == 3),
 "SU2^2 U1": sum(a*y for _, a, b, y in gen if b == 2),
 "U1^3":     sum(a*b*y**3 for _, a, b, y in gen),
 "grav^2 U1": sum(a*b*y for _, a, b, y in gen),
 "SU3^3 (L - R count)": sum(1 for _, a, b, y in gen if a == 3 and b == 2)*2 - sum(1 for _, a, b, y in gen if a == 3 and b == 1),
}
for k_, v in anoms.items(): P(f"  anomaly {k_:20s} = {v}")
P("  number of SU(2) doublets per generation (Witten anomaly needs even):", sum(a for _, a, b, y in gen if b == 2))
dimG = 8 + 3 + 1
P(f"\nbosonic d.o.f.: 2*dim G + 4 (Higgs doublet real components) = {2*dimG + 4}")
for Ng in range(0, 5):
    P(f"  N_g={Ng}: Str 1 = {2*dimG + 4} - {2*n_weyl}*N_g = {2*dimG + 4 - 2*n_weyl*Ng}")
P("Str 1 = 0 needs N_g = 28/30, not an integer. Anomaly conditions are linear/cubic in Y and independent of")
P("Yukawa couplings, so they cannot constrain Str m^2 or Str m^4 (masses are free parameters y_f v/sqrt2).")
txt = "\n".join(out); print(txt)
open(os.path.join(os.path.dirname(__file__), 'sm_structure_check_out.txt'), 'w').write(txt + "\n")
