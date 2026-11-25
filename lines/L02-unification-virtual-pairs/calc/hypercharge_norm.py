"""What U(1)_Y normalisation k (alpha_1 = k alpha_Y) would make alpha_1 pass through the alpha_2 = alpha_3 crossing?
In the SM alone k is a convention (only SU(5)/SO(10)-type embeddings fix k=5/3). Shown only to document that
'unification' of alpha_1 is a statement about an embedding, not about SM dynamics (A3.2: such relations not allowed)."""
import numpy as np
d = np.loadtxt("sm_3loop_alpha_inv.txt")
l, a1, a2, a3 = d.T
diff = a2 - a3
k = np.where(np.sign(diff[:-1]) != np.sign(diff[1:]))[0][0]
f = diff[k] / (diff[k] - diff[k + 1])
l23 = l[k] + f * (l[k + 1] - l[k]); a23 = a2[k] + f * (a2[k + 1] - a2[k]); a1_23 = a1[k] + f * (a1[k + 1] - a1[k])
aY = 5 / 3 * a1_23
print(f"M23 = 10^{l23:.2f} GeV, alpha_2^-1 = alpha_3^-1 = {a23:.2f}, alpha_Y^-1 = {aY:.2f}")
print(f"k needed = alpha_Y^-1/alpha_23^-1 = {aY/a23:.3f}   (SU(5) value 5/3 = 1.667)")
