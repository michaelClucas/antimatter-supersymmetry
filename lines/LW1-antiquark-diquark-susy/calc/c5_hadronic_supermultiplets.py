"""LW1 cycle 4, c5d: what the hadronic (LFHQCD) supermultiplets predict, and how much of it is confirmed.

Source of the assignments: Nielsen & Brodsky, "Hadronic superpartners from superconformal and supersymmetric
algebra", arXiv:1802.09652, Tables 4 (light), 5 (charm), 6 (bottom), 7 (double heavy), n = 0 families (plus the
n = 1 double-heavy rows they include). Tetraquark rule (Brodsky et al. 1604.06746 sec. 2.3): T = R B-, L_T = L_B,
M_T = M_B up to quark-mass terms. Meson rule: L_M = L_B + 1, M_M = M_B.
Greek letters were lost in PDF text extraction; names were reconstructed from mass, J^P and quark content
[reconstruction: conjecture for a few rows, flagged '?n'].

Masses: PDG 2024 central values, transcribed (last digits [uncertain]; the % mismatches are robust).
Tetraquark status codes (as of PDG 2024 / LITCHECK, my classification):
  EXO  established state that cannot be q-qbar (exotic J^PC, or charged hidden-charm)
  DEB  established state, internal structure actively debated (4q / molecule / q-qbar)
  QQB  established state with a standard q-qbar quark-model assignment (PDG quark-model table)
  PRED predicted by the paper, not observed (cannot be evidence, ruling R1)
  NONE no tetraquark assigned
Hadron status codes for meson/baryon: OBS observed; PRED predicted ('?' in the paper); UNC unconfirmed.
"""
import numpy as np

# (sector, meson, M_meson, mstat, baryon, M_baryon, bstat, tetraquark, M_T, tstat, note)
R = [
 # light, Table 4
 ("light", "h1(1170)", 1166, "OBS", "N(939)", 938.9, "OBS", "f0(500)", 475, "DEB", "pole 400-550"),
 ("light", "eta2(1645)", 1617, "OBS", "N(1520)", 1515, "OBS", "-", None, "NONE", "I=0 1-+ slot empty"),
 ("light", "a2(1320)", 1318.2, "OBS", "Delta(1232)", 1232, "OBS", "a1(1260)", 1230, "QQB", ""),
 ("light", "rho3(1690)", 1688.8, "OBS", "Delta(1700)", 1710, "OBS", "pi1(1600)", 1661, "EXO", "1-+ exotic"),
 ("light", "a4(1970)", 1967, "OBS", "Delta(1950)", 1930, "OBS", "-", None, "NONE", ""),
 ("light", "K1(1270)", 1253, "OBS", "Lambda(1116)", 1115.7, "OBS", "K0*(1430)", 1425, "DEB", ""),
 ("light", "K2(1770)", 1773, "OBS", "Lambda(1520)", 1519, "OBS", "-", None, "NONE", ""),
 ("light", "K1(1270)", 1253, "OBS", "Sigma(1193)", 1193.2, "OBS", "a0(980)/f0(980)", 985, "DEB", "K1(1270) used twice"),
 ("light", "K2*(1430)", 1427.3, "OBS", "Sigma(1385)", 1385, "OBS", "K1(1400)", 1403, "QQB", ""),
 ("light", "K3*(1780)", 1779, "OBS", "Sigma(1670)?n", 1670, "OBS", "K2(1820)", 1819, "QQB", ""),
 ("light", "K4*(2045)", 2048, "OBS", "Sigma(2030)", 2030, "OBS", "-", None, "NONE", ""),
 ("light", "h1(1415)", 1416, "OBS", "Xi(1318)", 1318.3, "OBS", "f0(1370)/a0(1450)", 1395, "DEB", "f0(1370) 1200-1500"),
 ("light", "eta2(1870)", 1842, "OBS", "Xi(1620)?n", 1620, "OBS", "-", None, "NONE", "Xi(1620) J^P unmeasured"),
 ("light", "f2'(1525)", 1517.4, "OBS", "Xi(1530)", 1533.4, "OBS", "f1(1420)/a1(1420)", 1420, "DEB", ""),
 ("light", "phi3(1850)", 1854, "OBS", "Xi(1820)", 1823, "OBS", "-", None, "NONE", ""),
 ("light", "f2(1640)", 1639, "UNC", "Omega(1672)", 1672.45, "OBS", "K1(1650)", 1650, "QQB", "f2(1640) needs confirmation"),
 # charm, Table 5
 ("charm", "D1(2420)", 2422.1, "OBS", "Lambda_c(2286)", 2286.46, "OBS", "D0*(2300)", 2343, "DEB", "listed as D0*(2400)"),
 ("charm", "D(2600)?n", 2627, "OBS", "Lambda_c(2625)", 2628.0, "OBS", "-", None, "NONE", "J^P assumed 2-"),
 ("charm", "D1(2420)", 2422.1, "OBS", "Sigma_c(2455)", 2453.5, "OBS", "D0*(2300)", 2343, "DEB", "same state used twice"),
 ("charm", "D2*(2460)", 2461.1, "OBS", "Sigma_c(2520)", 2518.4, "OBS", "D0(2550)", 2549, "QQB", "J^P assumed 1+"),
 ("charm", "D3*(2750)", 2763.1, "OBS", "Sigma_c(2800)", 2800, "OBS", "-", None, "NONE", ""),
 ("charm", "Ds1(2460)", 2459.5, "OBS", "Xi_c(2470)", 2469.4, "OBS", "Ds0*(2317)", 2317.8, "DEB", ""),
 ("charm", "Ds2(2830)?", 2830, "PRED", "Xi_c(2815)", 2816.5, "OBS", "-", None, "NONE", ""),
 ("charm", "Ds2*(2573)", 2569.1, "OBS", "Xi_c(2645)", 2645.6, "OBS", "Ds1(2536)", 2535.1, "QQB", ""),
 ("charm", "Ds3*(2860)", 2860, "OBS", "Xi_c(2930)", 2940, "OBS", "-", None, "NONE", ""),
 ("charm", "Ds1(2700)?", 2700, "PRED", "Omega_c(2695)", 2695.2, "OBS", "??", None, "PRED", ""),
 ("charm", "Ds2(2750)?", 2750, "PRED", "Omega_c(2770)", 2765.9, "OBS", "??", None, "PRED", ""),
 # bottom, Table 6
 ("bottom", "B1(5721)", 5726.1, "OBS", "Lambda_b(5620)", 5619.6, "OBS", "B_J(5732)", 5698, "QQB", "J^P assumed 1+"),
 ("bottom", "B_J(5970)", 5971, "OBS", "Lambda_b(5920)", 5920.1, "OBS", "-", None, "NONE", "J^P assumed 2-"),
 ("bottom", "B1(5721)", 5726.1, "OBS", "Sigma_b(5815)", 5813.1, "OBS", "B_J(5732)", 5698, "QQB", "same state used twice"),
 ("bottom", "B2*(5747)", 5739.5, "OBS", "Sigma_b*(5835)", 5832.6, "OBS", "B_J(5840)", 5863, "QQB", "J^P assumed 0+"),
 ("bottom", "Bs1(5830)", 5828.7, "OBS", "Xi_b(5795)", 5794.5, "OBS", "Bs0(~5800)?", 5800, "PRED", "D0 X(5568) not confirmed by LHCb/CMS"),
 ("bottom", "Bs2*(5840)", 5839.9, "OBS", "Xi_b(5945)", 5952.3, "OBS", "Bs1(~5900)?", 5900, "PRED", ""),
 ("bottom", "Bs1(6000)?", 6000, "PRED", "Omega_b(6046)", 6045.8, "OBS", "??", None, "PRED", ""),
 # double heavy, Table 7
 ("2heavy", "h_c(3525)", 3525.37, "OBS", "Xi_cc(3621)", 3621.55, "OBS", "chi_c0(3415)", 3414.71, "QQB", "alt. SELEX Xi_cc(3520): unconfirmed"),
 ("2heavy", "chi_c2(3556)", 3556.17, "OBS", "Xi_cc(3621) as 3/2+", 3621.55, "OBS", "chi_c1(3510)", 3510.67, "QQB", "same baryon used twice"),
 ("2heavy", "chi_c2(3930)", 3922.5, "OBS", "Xi_cc(~3900)?", 3900, "PRED", "X(3872), Zc(3900)", 3879, "EXO", "n=1; Zc charged -> exotic"),
 ("2heavy", "h_b(9899)", 9899.3, "OBS", "Xi_bb(~9900)?", 9900, "PRED", "chi_b0(9859)", 9859.44, "QQB", ""),
 ("2heavy", "chi_b2(9912)", 9912.21, "OBS", "Xi_bb(~9900)?", 9900, "PRED", "chi_b1(9893)", 9892.78, "QQB", ""),
 ("2heavy", "chi_b2(10269)", 10268.65, "OBS", "Xi_bb(~10300)?", 10300, "PRED", "X_b(10250)?", 10250, "PRED", "n=1"),
]

print(f"{'sector':7s} {'meson':16s} {'baryon':20s} {'dM/M(m-b)':>9s}  {'tetraquark':18s} {'dM/M(t-b)':>9s} tstat")
mb, mev, tb, rows_obs = {}, {}, [], 0
for sec, m, Mm, ms, b, Mb, bs, t, Mt, ts, note in R:
    both = ms == "OBS" and bs == "OBS"
    d = (Mm - Mb) / (0.5 * (Mm + Mb))
    dt = None if Mt is None else (Mt - Mb) / (0.5 * (Mt + Mb))
    if both:
        mb.setdefault(sec, []).append(d)
        mev.setdefault(sec, []).append(Mm - Mb)
        rows_obs += 1
    if dt is not None and ts != "PRED" and bs == "OBS":
        tb.append((sec, t, dt, ts))
    flag = "" if both else "  (pair not both observed)"
    dts = "" if dt is None else f"{dt:+9.3f}"
    print(f"{sec:7s} {m:16s} {b:20s} {d:+9.3f}  {t:18s} {dts:>9s} {ts:4s} {note}{flag}")

print("\nMeson-baryon superpartner pairs")
print(f"  rows in tables: {len(R)}; both members observed: {rows_obs}; "
      f"meson predicted (unobserved): {sum(r[3]=='PRED' for r in R)}; baryon predicted (unobserved): {sum(r[6]=='PRED' for r in R)};"
      f" meson unconfirmed: {sum(r[3]=='UNC' for r in R)}")
for sec, v in mb.items():
    v = np.array(v)
    print(f"  {sec:7s} n={len(v):2d}  mean dM/M = {np.mean(v):+.3f}  mean |dM/M| = {np.mean(np.abs(v)):.3f}  max |dM/M| = {np.max(np.abs(v)):.3f}")
print("  in MeV (heavy sectors: the fractional number is diluted by the heavy-quark mass, so use MeV):")
for sec, v in mev.items():
    v = np.array(v)
    print(f"  {sec:7s} mean |dM| = {np.mean(np.abs(v)):5.0f} MeV  max |dM| = {np.max(np.abs(v)):4.0f} MeV")
allv = np.concatenate([np.array(v) for v in mb.values()])
print(f"  all     n={len(allv):2d}  mean |dM/M| = {np.mean(np.abs(allv)):.3f}  fraction within 5%: {np.mean(np.abs(allv)<0.05):.2f}")

print("\nTetraquark slots (the members with no conventional interpretation)")
from collections import Counter
c = Counter(r[9] for r in R)
print("  status counts over all rows:", dict(c))
for code in ["EXO", "DEB", "QQB"]:
    sel = [x for x in tb if x[3] == code]
    if sel:
        v = np.array([x[2] for x in sel])
        print(f"  {code}: n={len(sel)}  mean |dM/M(t-b)| = {np.mean(np.abs(v)):.3f}  states: {', '.join(x[1] for x in sel)}")
n_assigned = sum(r[9] in ("EXO", "DEB", "QQB") for r in R)
print(f"  observed tetraquark candidates assigned: {n_assigned}; of these, unambiguously non-q-qbar (EXO): {c['EXO']};"
      f" standard q-qbar states re-labelled as tetraquarks (QQB): {c['QQB']}")
print("\nDouble use of one observed state for two partner slots: D0*(2300), B_J(5732), K1(1270), Xi_cc(3621).")
print("Conflict with QCD-derived superflavor (c2/c4): superflavor partners Xi_cc with D (cbar -> cc, light q spectator);")
print(f"LFHQCD partners Xi_cc with h_c(3525) (cbar -> [cq]). Different maps. Mismatch: Xi_cc - h_c = {3621.55-3525.37:.0f} MeV"
      f" ({(3621.55-3525.37)/3573:.3f}); Xi_cc - D is ~1755 MeV by construction (heavy mass not degenerate).")
