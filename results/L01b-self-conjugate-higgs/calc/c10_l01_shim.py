"""L01b cycle 10 (Referee F F5, CONSTRAINTS H4): run the merged L01 #4 / Weisskopf scripts from this line's calc/.

The L01 scripts stay the single source (lines/L01-weisskopf-hierarchy/calc/). Each is executed here with
__file__ set to calc/l01_<name>.py, so its tools/ import path resolves the same way and its output is written
to calc/l01_<name>_out.txt in this line. L01's own committed outputs are not touched. The shim then compares
each new output with L01's committed one.
Run from this directory: python c10_l01_shim.py
"""
import io
import os
import sys
import contextlib

HERE = os.path.dirname(os.path.abspath(__file__))
L01 = os.path.abspath(os.path.join(HERE, '..', '..', 'L01-weisskopf-hierarchy', 'calc'))
SCRIPTS = ['weisskopf_ofpt.py', 'higgs_top_ofpt.py', 'veltman_running.py', 'cw_radiative_ewsb.py']

summary = []
ok = True
for name in SCRIPTS:
    src_path = os.path.join(L01, name)
    with open(src_path, encoding='utf-8') as fh:
        src = fh.read()
    fake = os.path.join(HERE, 'l01_' + name)
    g = {'__name__': '__main__', '__file__': fake}
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(src, src_path, 'exec'), g)
    new_out = fake.replace('.py', '_out.txt')
    ref_out = src_path.replace('.py', '_out.txt')
    with open(new_out, encoding='utf-8') as a, open(ref_out, encoding='utf-8') as b:
        same = a.read() == b.read()
    ok &= same
    summary.append(f"{name:24s} -> {os.path.basename(new_out):30s} identical to L01 committed output: {same}")

summary.append("all identical" if ok else "DIFFERENCES FOUND (inspect the l01_*_out.txt files)")
print("\n".join(summary))
with open(os.path.join(HERE, 'c10_l01_shim_out.txt'), 'w', encoding='utf-8') as fh:
    fh.write("\n".join(summary) + "\n")
sys.exit(0 if ok else 1)
