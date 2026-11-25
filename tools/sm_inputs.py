"""Shared SM inputs (PDG 2024 unless noted). Import from here so every line uses the same numbers.

Values tagged uncertain in CONSTRAINTS.md are marked with a trailing comment.
"""
import math

# Masses in GeV
MZ = 91.1876
MW = 80.369          # uncertain last digit, see CONSTRAINTS C2
MH = 125.20
MT = 172.57          # top pole mass
MB = 4.18            # MS-bar mb(mb)
MC = 1.27            # MS-bar mc(mc)
MTAU = 1.77686
GF = 1.1663788e-5    # GeV^-2
V = (math.sqrt(2) * GF) ** -0.5  # 246.22 GeV

# Couplings at MZ, MS-bar
ALPHA_S_MZ = 0.1180
ALPHA_EM_INV_MZ = 127.930  # PDG 2024 (was 127.951, PDG 2022; corrected cycle 1)
SIN2W_MZ = 0.23129


def gauge_couplings_mz():
    """Return (alpha1_GUT, alpha2, alpha3) at MZ, alpha1 in SU(5) normalization (5/3 alpha_Y)."""
    a_em = 1.0 / ALPHA_EM_INV_MZ
    a2 = a_em / SIN2W_MZ
    aY = a_em / (1.0 - SIN2W_MZ)
    a1 = 5.0 / 3.0 * aY
    return a1, a2, ALPHA_S_MZ


# Cosmology (Planck 2018)
OMEGA_C_H2 = 0.1200
OMEGA_B_H2 = 0.02237
ETA_B = 6.1e-10
RHO_LAMBDA_GEV4 = 2.5e-47   # approx, (2.24 meV)^4
M_PLANCK = 1.220890e19      # GeV, non-reduced

if __name__ == "__main__":
    a1, a2, a3 = gauge_couplings_mz()
    print(f"v = {V:.3f} GeV")
    print(f"alpha^-1 at MZ: a1={1/a1:.3f}  a2={1/a2:.3f}  a3={1/a3:.3f}")
