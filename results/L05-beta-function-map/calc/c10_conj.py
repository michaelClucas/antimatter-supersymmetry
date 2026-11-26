"""
L05 cycle 10 (referee 4, F1): which "conjugate vs duplicate" pairs used in CLAIM (b) are anomaly-free, and which
differ in a conjugation-odd non-anomaly trace. Supports restricting the three-loop part of CLAIM (b).

For each fermion content (LH Weyl fields, n_G = 3) print:
  Tr Y^3, Tr Y, SU(2)^2 U(1), SU(3)^2 U(1), SU(3)^3, number of SU(2) doublets (Witten parity),
  and the conjugation-odd trace O = sum_f Y_f C2(f) C3(f) d(f)  (plain Y, not GUT-normalised).
Contents: SM; SMbar (every SM Weyl field conjugated); T_dbl = SM + SMbar; DUP = SM + SM;
MSSM fermions (SM + H~u + H~d; gauginos carry Y = 0 and real reps, no contribution); MSSM with H~d replaced by
a duplicate H~u.
Exact rationals, all statements asserted. Run from calc/: python c10_conj.py  (output c10_conj.txt)
"""
from fractions import Fraction as F

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

# (SU(3) rep, SU(2) dim, Y); SU(3) rep in {"1", "3", "3b"}
GEN = [("3", 2, F(1, 6)), ("3b", 1, F(-2, 3)), ("3b", 1, F(1, 3)), ("1", 2, F(-1, 2)), ("1", 1, F(1))]
NG = 3
def conj(f):
    r3, d2, Y = f
    return ({"1": "1", "3": "3b", "3b": "3"}[r3], d2, -Y)   # SU(2) doublet is pseudoreal: 2bar ~ 2
D3 = {"1": 1, "3": 3, "3b": 3}
T3 = {"1": 0, "3": F(1, 2), "3b": F(1, 2)}
A3 = {"1": 0, "3": 1, "3b": -1}
C3 = {"1": 0, "3": F(4, 3), "3b": F(4, 3)}
T2 = {1: 0, 2: F(1, 2)}
C2 = {1: 0, 2: F(3, 4)}

def data(content):
    tY3 = sum(D3[r]*d*Y**3 for r, d, Y in content)
    tY = sum(D3[r]*d*Y for r, d, Y in content)
    a22 = sum(D3[r]*T2[d]*Y for r, d, Y in content)
    a33 = sum(d*T3[r]*Y for r, d, Y in content)
    a333 = sum(d*A3[r] for r, d, Y in content)
    ndbl = sum(D3[r] for r, d, Y in content if d == 2)
    odd = sum(Y*C2[d]*C3[r]*D3[r]*d for r, d, Y in content)
    return (tY3, tY, a22, a33, a333, ndbl, odd)

SM = GEN*NG
SMbar = [conj(f) for f in SM]
Hu, Hd = ("1", 2, F(1, 2)), ("1", 2, F(-1, 2))
contents = {"SM": SM, "SMbar": SMbar, "T_dbl = SM+SMbar": SM + SMbar, "DUP = SM+SM": SM + SM,
            "MSSM (H~u+H~d)": SM + [Hu, Hd], "MSSM with duplicate H~u": SM + [Hu, Hu]}
P("content: (Tr Y^3, Tr Y, SU2^2 Y, SU3^2 Y, SU3^3, #doublets, O = sum Y C2 C3 d)")
D = {}
for k, c in contents.items():
    D[k] = data(c)
    P(f"  {k:26s}", tuple(str(x) for x in D[k]))
af = lambda v: v[:5] == (0, 0, 0, 0, 0) and v[5] % 2 == 0

assert af(D["SM"]) and af(D["SMbar"]) and af(D["T_dbl = SM+SMbar"]) and af(D["DUP = SM+SM"]) and af(D["MSSM (H~u+H~d)"])
assert not af(D["MSSM with duplicate H~u"])
assert D["SM"][6] == NG and D["SMbar"][6] == -NG
assert D["T_dbl = SM+SMbar"][6] == 0 and D["DUP = SM+SM"][6] == 2*NG
P("\nResults (asserted):")
P("  SM, SMbar, T_dbl and DUP are anomaly-free (all five anomaly coefficients 0, even doublet count).")
P("  The MSSM fermion content is anomaly-free; replacing H~d by a duplicate H~u makes it anomalous.")
P(f"  O = {NG} (SM), {-NG} (SMbar), 0 (T_dbl), {2*NG} (DUP): T_dbl and DUP are both anomaly-free but differ in this")
P("  conjugation-odd non-anomaly trace (1 per generation in the SM). Anomaly freedom alone therefore does not make")
P("  the pair (T_dbl, DUP) indistinguishable at three loops unless such traces are absent from the three-loop")
P("  gauge-only entries; that was not checked (no general three-loop formula in this line).")
P("  SMbar vs SM: every field conjugated at once is the same theory after the gauge-field relabelling")
P("  A^a T^a -> A^a (-T^a*) (an automorphism of the Lie algebra; g1 -> -g1 for U(1)); O flips sign, consistent with")
P("  O entering gauge-only coefficients, if at all, only at even powers or multiplied by another odd trace.")

open(__file__.replace(".py", ".txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
