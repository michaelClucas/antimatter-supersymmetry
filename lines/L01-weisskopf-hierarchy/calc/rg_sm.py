"""Shim: L01 uses the shared runner tools/rg_sm.py (no private copy).

Cycle 3: the private copy that lived here was byte-identical to tools/rg_sm.py (checked with diff),
so it was replaced by this re-export. Running this file runs the shared runner's validation against
Buttazzo et al. (arXiv:1307.3536) eq. (61) and saves it to rg_sm_validation_out.txt.
"""
import os
import runpy
import sys

_tools = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools'))
sys.path.insert(0, _tools)

if __name__ == '__main__':
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        runpy.run_path(os.path.join(_tools, 'rg_sm.py'), run_name='__main__')
    txt = buf.getvalue()
    print(txt, end='')
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rg_sm_validation_out.txt'), 'w') as fh:
        fh.write(txt)
else:
    del sys.modules[__name__]
    import rg_sm as _shared  # noqa: E402  (resolves to tools/rg_sm.py now that this module is unregistered)
    sys.modules[__name__] = _shared
