"""Referee B check: the 'exact Z2' (h -> -h, t_R -> -t_R) of WORK.md Sec. 4 equals
(SU(2)_L centre, a gauge transformation) x (-1)^F (a 2*pi rotation).  Prints the sign each
map gives on each SM field and compares."""
fields = {  # name: (SU(2) doublet?, B, L, is_fermion)
    "H":   (True, 0, 0, False), "Q_L": (True, 1/3, 0, True), "u_R": (False, 1/3, 0, True),
    "d_R": (False, 1/3, 0, True), "L_L": (True, 0, 1, True), "e_R": (False, 0, 1, True)}
import cmath
def sgn(z): return int(round(z.real))
ok = True
for n, (dbl, B, L, F) in fields.items():
    centre = -1 if dbl else 1
    rot = sgn(cmath.exp(1j * cmath.pi * (3 * B + L)))
    z2 = centre * rot
    fF = centre * (-1 if F else 1)
    ok &= (z2 == fF)
    print(f"{n:4s} centre={centre:+d} (3B+L)pi={rot:+d} -> Z2={z2:+d} | centre*(-1)^F={fF:+d}")
print("Z2 == SU(2) centre x (-1)^F on all fields:", ok)
