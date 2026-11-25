"""Quantify SM non-unification at 1, 2, 3 loops and compare with MSSM (1, 2 loops, M_SUSY = 1-3 TeV).
Two input sets:
  A = NNLO-matched MS-bar couplings at mu=Mt (Buttazzo et al. 1307.3536 fit formulas) with PDG-2024 Mt, Mh, alpha_s, MW
  B = PDG MS-bar alpha_s, alpha_em, sin^2thetaW at MZ (tools/sm_inputs.py), run directly in 6-flavour SM
Outputs crossing scales M12, M13, M23, best-point spread, threshold needed, alpha_s predicted by exact unification.
"""
import math
import numpy as np
from scipy.optimize import brentq
import sm_path  # noqa: F401
import sm_inputs as smi
from rg_sm3 import inputs_buttazzo_at_mt, inputs_pdg_at_mz, run, alpha_inv

MU_MAX = 1e20


def curves(model, loops, inp="A", msusy=None, as_mz=smi.ALPHA_S_MZ):
    if inp == "A":
        mu0, x0 = inputs_buttazzo_at_mt(as_mz=as_mz)
    else:
        mu0, x0 = inputs_pdg_at_mz(as_mz=as_mz)
    mu, y = run(x0, mu0, MU_MAX, loops=loops, model=model, msusy=msusy, npts=4000)
    return np.log10(mu), alpha_inv(y)


def crossing(lmu, a, i, j):
    d = a[i] - a[j]
    idx = np.where(np.sign(d[:-1]) != np.sign(d[1:]))[0]
    if len(idx) == 0:
        return None, None
    k = idx[0]
    f = d[k] / (d[k] - d[k + 1])
    l = lmu[k] + f * (lmu[k + 1] - lmu[k])
    return l, a[i][k] + f * (a[i][k + 1] - a[i][k])


def analyse(model, loops, inp="A", msusy=None, as_mz=smi.ALPHA_S_MZ):
    lmu, a = curves(model, loops, inp, msusy, as_mz)
    out = {}
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        out[f"M{i+1}{j+1}"] = crossing(lmu, a, i, j)
    spread = a.max(axis=0) - a.min(axis=0)
    sel = lmu > 10
    k = np.argmin(np.where(sel, spread, np.inf))
    out["best"] = (lmu[k], spread[k], a[:, k].mean())
    l12, a12 = out["M12"]
    if l12 is not None:
        a3 = np.interp(l12, lmu, a[2])
        out["dA3_at_M12"] = a3 - a12
    return out


def predicted_alpha_s(model, loops, msusy=None):
    """alpha_s(MZ) for which alpha_3 passes exactly through the alpha_1=alpha_2 crossing.
    Uses input set B only (set A's fit formulas are linearised around alpha_s=0.1184 and are not valid far away)."""
    def f(asz):
        return analyse(model, loops, "B", msusy, asz)["dA3_at_M12"]
    lo, hi = (0.055, 0.15) if model == "SM" else (0.10, 0.145)
    return brentq(f, lo, hi, xtol=1e-6)


def fmt(o):
    s = []
    for key in ("M12", "M13", "M23"):
        l, av = o[key]
        s.append(f"{key}: 10^{l:.2f} GeV (a^-1={av:.2f})" if l is not None else f"{key}: none<1e20")
    l, sp, am = o["best"]
    s.append(f"best point 10^{l:.2f} GeV, spread max-min alpha^-1 = {sp:.2f} (mean {am:.2f}, rel {sp/am*100:.1f}%)")
    s.append(f"alpha3^-1 - alpha12^-1 at M12 = {o['dA3_at_M12']:.2f}")
    return "\n    ".join(s)


if __name__ == "__main__":
    a1, a2, a3 = smi.gauge_couplings_mz()
    print(f"PDG alpha^-1(MZ): {1/a1:.3f} {1/a2:.3f} {1/a3:.3f}")
    mu0, x0 = inputs_buttazzo_at_mt()
    print(f"Set A alpha^-1(Mt={mu0}): {', '.join(f'{v:.3f}' for v in 4*math.pi/x0[:3])}; yt={math.sqrt(x0[3]):.4f} lam={x0[4]:.4f}")
    print()
    for inp in ("A", "B"):
        for loops in (1, 2, 3):
            print(f"SM  inputs {inp}  {loops}-loop:\n    " + fmt(analyse("SM", loops, inp)))
            if inp == "B":
                print(f"    alpha_s(MZ) required for exact unification: {predicted_alpha_s('SM', loops):.4f}")
        print()
    # alpha_s uncertainty band at 3 loops
    for asz in (smi.ALPHA_S_MZ - 0.0009, smi.ALPHA_S_MZ + 0.0009):
        o = analyse("SM", 3, "A", as_mz=asz)
        print(f"SM A 3-loop alpha_s={asz:.4f}: best spread {o['best'][1]:.2f}, dA3(M12)={o['dA3_at_M12']:.2f}, "
              f"M23=10^{o['M23'][0]:.2f}")
    print()
    for inp in ("A", "B"):
        for ms in (1000.0, 2000.0, 3000.0):
            for loops in (1, 2):
                o = analyse("MSSM", loops, inp, msusy=ms)
                print(f"MSSM inputs {inp} Ms={ms/1000:.0f} TeV {loops}-loop:\n    " + fmt(o))
                if inp == "B":
                    print(f"    alpha_s(MZ) required for exact unification: {predicted_alpha_s('MSSM', loops, ms):.4f}")
    # save curves for plotting/other lines
    lmu, a = curves("SM", 3, "A")
    np.savetxt("sm_3loop_alpha_inv.txt", np.column_stack([lmu, a.T])[::40], header="log10(mu/GeV) a1^-1 a2^-1 a3^-1  (SM 3-loop, inputs A)", fmt="%.5f")
