# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.25.1",
#     "numpy",
#     "numba",
#     "matplotlib",
#     "altair",
#     "pandas",
#     "schemdraw",
#     "wigglystuff",
#     "anywidget",
#     "traitlets",
# ]
# ///

import marimo

__generated_with = "0.25.1"
app = marimo.App(
    width="full",
    layout_file="data:application/json;base64,eyJ0eXBlIjogInNsaWRlcyIsICJkYXRhIjogeyJjZWxscyI6IFt7InR5cGUiOiAic2tpcCJ9LCB7InR5cGUiOiAic2tpcCJ9LCB7InR5cGUiOiAic2xpZGUiLCAic3BlYWtlck5vdGVzIjogIldoeSBjYXJlOiBzZWxmLW9zY2lsbGF0aW9uIHNob3dzIHVwIGluIG1hbnkgcGh5c2ljYWwgc3lzdGVtczsgcHJlZGljdGluZyB3aGVyZSBpdCBzdGFydHMgZnJvbSBkYXRhIHRoYXQgbmV2ZXIgb3NjaWxsYXRlZCBpcyBnZW51aW5lIGV4dHJhcG9sYXRpb24uIFN0YXRlIHRoZSByZXNlYXJjaCBxdWVzdGlvbi4ifSwgeyJ0eXBlIjogInNraXAifSwgeyJ0eXBlIjogInNsaWRlIiwgInNwZWFrZXJOb3RlcyI6ICJUaGUgbW9kZWw6IHJvdG9ycyB3aXRoIGluZXJ0aWEgSSwgY291cGxlZCB0byBuZWlnaGJvdXJzIChKKSwgcHVsbGVkIHRvd2FyZHMgYSBmaWVsZCBkaXJlY3Rpb24gKEIpLCBkYW1wZWQgKGFscGhhKS4gVG9ycXVlIHUgZW50ZXJzIGF0IHRoZSByaWdodCByb3RvciwgdGhlIG91dHB1dCB5IGlzIHJlYWQgYXQgdGhlIGxlZnQgcm90b3IgbmV4dCB0byB0aGUgd2FsbC4gTm8gZmVlZGJhY2sgeWV0LiBGaXJzdCBsaW5lOiBIYW1pbHRvbmlhbi4gU2Vjb25kIGxpbmU6IEVPTSA9IC1kSC9kdGhldGFfaSArIGRhbXBpbmcgKyB0b3JxdWUgKyBMYW5nZXZpbiB0aGVybWFsIHRlcm0gc3FydCgyIGFscGhhIGtfQiBUKSB4aV9pKHQpOyB0aGUgc3R1ZHkgcnVucyBhdCBUID0gMC4ifSwgeyJ0eXBlIjogInNsaWRlIiwgInNwZWFrZXJOb3RlcyI6ICJMaXZlOiBwcmVzcyBwbHVjay4gVGhlIHdhdmUgdHJhdmVscyBmcm9tIHRoZSBpbnB1dCAocHVycGxlLCByaWdodCkgdG8gdGhlIHdhbGwgYW5kIGVjaG9lcyBiYWNrOyB0aGUgb3NjaWxsb3Njb3BlIHNob3dzIHkuIFJhaXNlIEogLT4gZmFzdGVyIHdhdmUsIGVhcmxpZXIgZWNobzsgcmFpc2UgYWxwaGEgLT4gZmFzdGVyIGRlY2F5LiBTb3VuZCBvbi9vZmYgbmV4dCB0byByZXNldC4gVGhlIGRlbW8gc3RhcnRzIGF0IGFscGhhID0gMC4wMyBzbyB0aGUgcmluZy1kb3duIGxhc3RzIH41MC04MCBtcyAodGhlIHN0dWR5IHVzZXMgMC4xKS4gRGVtbyB1c2VzIDIwIHJvdG9ycywgdGhlIHN0dWR5IHVzZXMgOC4ifSwgeyJ0eXBlIjogInNraXAifSwgeyJ0eXBlIjogInNraXAifSwgeyJ0eXBlIjogInNraXAifSwgeyJ0eXBlIjogInNraXAifSwgeyJ0eXBlIjogInNsaWRlIiwgInNwZWFrZXJOb3RlcyI6ICJDbG9zZSB0aGUgbG9vcDogb3V0cHV0IC0+IERDIGJsb2NrZXIgLT4gZ2FpbiBnIC0+IChvcHRpb25hbCBkZWxheSBkKSAtPiBiYWNrIGluIGFzIHRvcnF1ZSwgY2xpcHBlZC4gSW4gdGhlIHN0dWR5IGQgPSAwLiBUaGUgY2xpcCBib3VuZHMgdGhlIGFtcGxpdHVkZS4ifSwgeyJ0eXBlIjogInNraXAifSwgeyJ0eXBlIjogInNsaWRlIiwgInNwZWFrZXJOb3RlcyI6ICJCZWxvdyBnX2MgdGhlIHBsdWNrIGRpZXMgb3V0OyBhYm92ZSBpdCB0aGUgbG9vcCBmZWVkcyBtb3JlIGVuZXJneSBwZXIgY3ljbGUgdGhhbiBkYW1waW5nIHJlbW92ZXMgLT4gc3VzdGFpbmVkLCBib3VuZGVkIG9zY2lsbGF0aW9uLiBUaGUgb25zZXQgaXMgdmVyeSBzaGFycCAoMy4xMiBzdGlsbCBkZWNheXMsIDMuMTQgc2F0dXJhdGVzKS4gV2hldGhlciB0aGlzIGlzIGEgSG9wZiBiaWZ1cmNhdGlvbiBpcyBzdGlsbCB0byBiZSBjaGFyYWN0ZXJpc2VkLiJ9LCB7InR5cGUiOiAic2xpZGUiLCAic3BlYWtlck5vdGVzIjogIkxpdmU6IHN0YXJ0cyBhdCBnID0gMi4zNSwgdGhlIHBsdWNrIGRpZXMgb3V0LiBUdXJuIHBhc3QgZ19jICh+My4xIGF0IHRoZSBzdHVkeSBzZXR0aW5ncykgYW5kIHBsYXk6IGEgc3VzdGFpbmVkIH44ODAgSHogdG9uZS4gVGhlIHNsaWRlcnMgY2hhbmdlIEosIGFscGhhIGFuZCB0aGUgZGVsYXkgZCBsaXZlOyBnX2MgbW92ZXMgd2l0aCB0aGVtIGFuZCB0aGUgZ3JlZW4gbm90Y2ggb24gdGhlIGtub2IgaXMgcmVjb21wdXRlZCBmb3IgdGhlIGN1cnJlbnQgc2V0dGluZ3MgKHRha2VzIGFib3V0IGEgc2Vjb25kKS4gUHJlc2V0czogJ2xvbmcgdGFpbCcgKEogMi44LCBhbHBoYSAwLjA0LCBkIDEyMCwga25vYiBhdCBnX2M6IGNyaXRpY2FsIHNsb3dpbmcgZG93biwgdGhlIHRhaWwgZGVjYXlzIHZlcnkgc2xvd2x5KTsgJ2NsZWFuIG9zY2lsbGF0aW9uJyAoSiAwLjksIGFscGhhIDAuMjIsIGQgMTIwLCBrbm9iIGp1c3QgcGFzdCBnX2M6IGdyb3dzIGludG8gYSBjbGVhbiB0b25lKTsgJ2NoYW90aWMgb3NjaWxsYXRpb24nIChhcyBsb25nIHRhaWwgYnV0IGFscGhhIDAuMDMsIHNvIHRoZSBzYW1lIGtub2IgaXMgbm93IHdlbGwgYWJvdmUgb25zZXQ6IGlycmVndWxhciwgYnVyc3Rpbmcgb3NjaWxsYXRpb24pLiJ9LCB7InR5cGUiOiAic2tpcCJ9LCB7InR5cGUiOiAic2xpZGUiLCAic3BlYWtlck5vdGVzIjogIkZvdXIgbW9kZWwgZmFtaWxpZXMgd2l0aCB0aGUgc2FtZSBrbm93biB0b3JxdWUgaW5wdXQgcG9ydCBHLiBQSE5OOiBlbmVyZ3kgSCwgZGFtcGluZyBSID49IDAgLT4gcGFzc2l2ZSBwbGFudCwgZW5lcmd5IG9ubHkgdmlhIHUuIERITk46IGRpc3NpcGF0aW9uIHNpZ24gbm90IGVuZm9yY2VkLiBOT0RFOiBubyBlbmVyZ3kgc3RydWN0dXJlLiBMaW5lYXI6IHRoZSBzYW5pdHkgYmFzZWxpbmUuIn0sIHsidHlwZSI6ICJzbGlkZSIsICJzcGVha2VyTm90ZXMiOiAiV2UgbGVhcm4gb25seSB0aGUgcGxhbnQ7IHRoZSBjb250cm9sbGVyIGlzIGEga25vd24gYWxnb3JpdGhtLiBGZWVkYmFjayBjb21lcyBmcm9tIHRoZSBtb2RlbCdzIG93biBvdXRwdXQsIG5ldmVyIHRoZSB0cnVlIHRvcnF1ZS4gRmluYWwgc3R1ZHk6IGlucHV0L291dHB1dCBkYXRhLCBzbyBQSE5OL0RITk4gbmVlZCBhIHN0YXRlIGVzdGltYXRlOyB0aGUgcGlsb3QgdXNlZCB0aGUgZnVsbCBzdGF0ZS4ifSwgeyJ0eXBlIjogInNraXAifSwgeyJ0eXBlIjogInNsaWRlIiwgInNwZWFrZXJOb3RlcyI6ICJQaWxvdCAoZnVsbCBzdGF0ZSwgdGlueSBtb2RlbHMsIDMgZGF0YXNldHMgeCAyIHNlZWRzLCB0cnVlIGdfYyA9IDMuMTIpLiBPbnNldCBnYWluOiBOT0RFIH4wLjIlLCBsaW5lYXIgfjAuNiUsIFBITk4gLTMuLis0JSwgREhOTiAtMTEuLis0JSAoc2VlZC1kZXBlbmRlbnQpLiBTbyBmYXIgdGhlIG5ldHdvcmtzIGRvbid0IGJlYXQgbGluZWFyIG9uIHRoZSBvbnNldCBpdHNlbGYuIn0sIHsidHlwZSI6ICJzbGlkZSIsICJzcGVha2VyTm90ZXMiOiAiU2FtZSBwaWxvdCwgb25lIHJ1biwgY2xvc2VkIGxvb3AgYWJvdmUgb25zZXQuIFRoZSBvbnNldCB3YXMgZmluZSwgYnV0IHRoZSBuZXR3b3JrcyBvc2NpbGxhdGUgYXQgdGhlIHdyb25nIGZyZXF1ZW5jeSAoNjAtMTEwICUgdG9vIGhpZ2gpOyBsaW5lYXIgaXMgd2l0aGluIH40ICUuIEFtcGxpdHVkZSBlcnJvcnMgMy0zMCAlLiBUaGlzIGlzIHRoZSAnaG93IHRoZXkgZmFpbCcgcGFydDogcmlnaHQgb25zZXQsIHdyb25nIHNvdW5kLiBTd2l0Y2ggcmVnaW1lcyBhbmQgbW9kZWxzIGxpdmUuIn0sIHsidHlwZSI6ICJzbGlkZSIsICJzcGVha2VyTm90ZXMiOiAiQURFTVAgKE1vcnJpcyBldCBhbC4gMjAxOSk6IGZpdmUgcXVlc3Rpb25zIGFuc3dlcmVkIGJlZm9yZSBydW5uaW5nIGFueXRoaW5nLiBBaW1zLCBkYXRhLWdlbmVyYXRpbmcgbWVjaGFuaXNtcywgZXN0aW1hbmRzICh0cnVlIGdfYywgZnJlcXVlbmN5LCBhbXBsaXR1ZGUpLCBtZXRob2RzLCBwZXJmb3JtYW5jZSBtZWFzdXJlcy4gU2FtZSBkYXRhc2V0cyBmb3IgZXZlcnkgbW9kZWwgKHBhaXJlZCksIGRhdGFzZXRzIGFuZCBzZWVkcyBib3RoIG1vZGVsbGVkLCBmYWlsdXJlcyBrZXB0LiJ9LCB7InR5cGUiOiAic2tpcCJ9LCB7InR5cGUiOiAic2tpcCJ9LCB7InR5cGUiOiAic2xpZGUiLCAic3BlYWtlck5vdGVzIjogIkZlZWRiYWNrIG1hdHJpeCAoWFludGggbWFudXNjcmlwdCwgZXEuIDc7IFhZTlRIIEZlZWRiYWNrTWF0cml4QmxvY2spOiB3aXRoIHNldmVyYWwgdGFwcyBhbmQgaW5wdXQgcm90b3JzIHRoZSBzY2FsYXIgZ2FpbiBiZWNvbWVzIGEgbWF0cml4IEY7IHVbbl0gPSB1X2V4Y1tuXSArIGcgRiB5W24tZF0uIEhlcmUgMyB0b3JxdWUgaW5wdXRzIChyb3RvcnMgMiwgNSwgOCkgYW5kIDMgdGFwcyAocm90b3JzIDEsIDQsIDcpOyBGIGlzIHJhbmRvbSBhbmQgc2NhbGVkIHRvIHx8Rnx8XzIgPSAxLCBzbyBnIGlzIHRoZSBvdmVyYWxsIGZlZWRiYWNrIGFtb3VudC4gTGl2ZTogcmFuZG9taXNlIEYsIHRoZSBvbnNldCBnX2MgbW92ZXMgKHJvdWdobHkgMi44IHRvIDQuNyBmb3IgZGVuc2UgRikuIExpbmVhciBndWlkZTogb3NjaWxsYXRpb24gc3RhcnRzIHdoZW4gdGhlIHNwZWN0cmFsIHJhZGl1cyBvZiBnIEYgSChlXmp3KSByZWFjaGVzIDEgYXQgc29tZSBmcmVxdWVuY3kgKHNtYWxsLWdhaW4gLyBnZW5lcmFsaXNlZCBOeXF1aXN0KS4gU3BhcnNlIEYgKDEtMiBwYXRocykgdGVuZHMgdG8gZ2l2ZSBwdXJlciB0b25lcywgZGVuc2UgRiBtb3JlIGNvbXBsZXggb25lcy4gRXh0ZW5zaW9uOiB0aGUgb25zZXQgaXMgbm93IGEgcHJvcGVydHkgb2YgdGhlIG1hdHJpeCwgbm90IG9uZSBudW1iZXIuIn0sIHsidHlwZSI6ICJzbGlkZSIsICJzcGVha2VyTm90ZXMiOiAiT3V0bG9vayBvbmx5OiByZWFsIHNlbGYtb3NjaWxsYXRpbmcgc3lzdGVtcyAoTGluYXJlcyBldCBhbC4pLiBPcHRpb25hbCBleHRlbnNpb24gaW4gdGhlIHByb3Bvc2FsLiJ9LCB7InR5cGUiOiAic2xpZGUiLCAic3BlYWtlck5vdGVzIjogIlBsYW4gaW4gZml2ZSBzdGVwczsgb3BlbiBxdWVzdGlvbnMgaW5jbC4gc3RhdGUgZXN0aW1hdGlvbiBmb3IgaW5wdXQvb3V0cHV0IHRyYWluaW5nLiBUaW1lbGluZTogZmlsbCBpbiB5b3VyIGRhdGVzLiBOZWltYXJrXHUyMDEzU2Fja2VyIGlzIHRoZSBkaXNjcmV0ZS10aW1lIChtYXApIHZlcnNpb24gb2YgSG9wZjsgdGhlIG9wZW4gcXVlc3Rpb24gaXMgd2hldGhlciB0aGUgb25zZXQgaXMgc3VwZXItIG9yIHN1YmNyaXRpY2FsIChpdCBsb29rcyBhYnJ1cHQpIGFuZCBob3cgdGhlIGNsaXAgc2hhcGVzIGl0LiJ9LCB7InR5cGUiOiAic2xpZGUiLCAic3BlYWtlck5vdGVzIjogIlJlZmVyZW5jZXMgKGJhY2t1cCkuIn0sIHsidHlwZSI6ICJza2lwIn1dLCAiZGVjayI6IHsidHJhbnNpdGlvbiI6ICJmYWRlIiwgInZlcnRpY2FsQWxpZ24iOiAidG9wIn19fQ==",
    app_title="Predicting oscillation onset in the XY model",
)


@app.cell(hide_code=True)
def _(ASSET_DIR):
    import base64
    import io
    import json
    import wave
    from pathlib import Path

    import altair as alt
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import wigglystuff as ws

    import importlib
    import sys

    sys.path.insert(0, str(ASSET_DIR / "mods"))
    figures = importlib.import_module("figures")
    xy_sim = importlib.import_module("xy_sim")
    DECK_CSS = "<style>" + (ASSET_DIR / "deck.css").read_text() + "</style>"

    figures.style()
    DATA = ASSET_DIR / "data"
    return DATA, DECK_CSS, alt, base64, figures, importlib, io, json, mo, np, pd, plt, wave, ws, xy_sim


@app.cell(hide_code=True)
def _(DATA, DECK_CSS, base64, io, json, mo, np, wave, xy_sim):
    # Simulator settings = the ones used to train the models (data/sim_params.json).
    # Rotor 0 is a fixed anchor (wall); rotors 1..N-1 are the visible chain.
    _fallback = dict(N=9, k0=1.0, alpha=0.1, B=0.2, B_dir_deg=180.0, torque_scale=0.5, delay=256,
                     tap=1, input_site=8, input_mode="torque", integrator="euler")
    _path = DATA / "sim_params.json"
    P = {**_fallback, **json.loads(_path.read_text())} if _path.exists() else _fallback
    P.setdefault("input_mode", "torque")
    FS = 44100
    _keys = ("N", "k0", "alpha", "B", "B_dir_deg", "delay", "tap", "input_site", "input_mode",
             "integrator", "torque_scale", "dc_r", "dt", "inertia")
    SIM_KW = {k: P[k] for k in _keys if k in P}
    # no feedback delay: y_hist[s-1] is the readout of the current state, so delay=1 in the
    # kernel means u[n] = g*h(x[n])  (delay=0 there would switch feedback off)
    SIM_KW["delay"] = 1

    @mo.cache
    def run(gain: float, seconds: float = 1.0, amp: float = 0.2, record_every: int = 1,
            J: float | None = None, alpha: float | None = None, d: int = 0):
        """Closed loop with the study settings; J, alpha and the extra delay d (samples) can be overridden."""
        n = int(seconds * FS)
        kw = dict(SIM_KW, delay=1 + int(d))
        if J is not None:
            kw["k0"] = float(J)
        if alpha is not None:
            kw["alpha"] = float(alpha)
        return xy_sim.simulate(gain=float(gain), n_steps=n, u_ext=xy_sim.pluck(n, amp, 20),
                               record_every=record_every, **kw)

    def wav_b64(y):
        """16-bit WAV as base64. Quiet signals stay quiet (no normalisation of a decaying pluck)."""
        y = np.asarray(y, float)
        y = y - y.mean()
        # limiter: peak never above CEIL (~ -10 dBFS), quiet decays are not boosted, tanh as safety
        CEIL = 0.3
        y = CEIL * y / max(np.abs(y).max(), 0.25)
        y = CEIL * np.tanh(y / CEIL)
        n = min(len(y) // 4, int(0.005 * FS))
        if n > 0:
            ramp = np.linspace(0, 1, n)
            y[:n] *= ramp
            y[-n:] *= ramp[::-1]
        buf = io.BytesIO()
        with wave.open(buf, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(FS)
            w.writeframes((y * 32767).astype("<i2").tobytes())
        return base64.b64encode(buf.getvalue()).decode()

    def audio(y, autoplay=False):
        b64 = wav_b64(y)
        auto = " autoplay" if autoplay else ""
        return mo.Html(f'<audio controls{auto} src="data:audio/wav;base64,{b64}" style="height:36px"></audio>')

    def cite(*refs):
        """Small reference line at the bottom of a slide."""
        return mo.md('<p class="cite">' + " · ".join(refs) + "</p>")

    def _h(x):
        return x if isinstance(x, str) else mo.as_html(x).text

    def page(*items):
        """Full-height slide. items: obj or (obj, 'grow'); grow items share the leftover height."""
        parts = []
        for it in items:
            obj, cls = (it if isinstance(it, tuple) else (it, "n"))
            parts.append(f'<div class="{cls}">{_h(obj)}</div>')
        return mo.Html(DECK_CSS + '<div class="page">' + "".join(parts) + "</div>")

    def row(*items, cols=None, cls=""):
        """Grid row that fills its parent's height."""
        cols = cols or " ".join(["1fr"] * len(items))
        cells = "".join(f'<div class="cell">{_h(x)}</div>' for x in items)
        return f'<div class="row {cls}" style="grid-template-columns:{cols}">{cells}</div>'

    def fig(svg):
        return f'<div class="fig">{svg}</div>'

    run(0.0, 0.05)  # warm up numba
    return FS, P, SIM_KW, audio, cite, fig, page, row, run, wav_b64


@app.cell(hide_code=True)
def _(DECK_CSS, mo):
    mo.Html(DECK_CSS + """
    <div class="title-slide">
      <h1>Can a neural network predict when a system starts to oscillate?</h1>
      <p class="rq">Trained only <span class="hl">below</span> the onset of self-oscillation,<br>can a neural model predict what happens <span class="hl">above</span> it?</p>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(importlib, mo):
    _w = importlib.import_module("widgets")
    RotorScope, simulate_pluck = _w.RotorScope, _w.simulate_pluck

    scope = RotorScope(**simulate_pluck(alpha=0.03), vh=66)
    s_J = mo.ui.slider(0.2, 3.0, step=0.1, value=1.0, label="$J$", show_value=True)
    s_alpha = mo.ui.slider(0.01, 0.5, step=0.01, value=0.03, label="$\\alpha$", show_value=True)
    s_B = mo.ui.slider(0.0, 1.0, step=0.05, value=0.2, label="$B$", show_value=True)
    s_I = mo.ui.slider(0.3, 3.0, step=0.1, value=1.0, label="$I$", show_value=True)
    s_amp = mo.ui.slider(0.1, 1.0, step=0.05, value=0.6, label="pluck", show_value=True)
    return s_B, s_I, s_J, s_alpha, s_amp, scope, simulate_pluck


@app.cell(hide_code=True)
def _(fig, figures, mo, page):
    page(
        mo.md("## The XY model: a chain of coupled rotors"),
        (mo.md(r"""
        $$
        \begin{aligned}
        H &= \sum_i \frac{p_i^2}{2I} \;-\; J\sum_i \cos(\theta_{i+1}-\theta_i) \;-\; B\sum_i \cos(\theta_i-\theta_B) \\[0.4em]
        I\,\ddot\theta_i &= J\,\big[\sin(\theta_{i+1}-\theta_i) + \sin(\theta_{i-1}-\theta_i)\big] \;-\; B\sin(\theta_i-\theta_B) \;-\; \alpha\,\dot\theta_i \;+\; u_i \;+\; \sqrt{2\alpha k_B T}\,\xi_i(t)
        \end{aligned}
        $$
        """), "eqbox xy xy2"),
        mo.md(r"""<p class="center legend"><b>J</b> coupling &nbsp;·&nbsp; <b>B</b> field &nbsp;·&nbsp; <b>α</b> damping &nbsp;·&nbsp; <b>I</b> inertia &nbsp;·&nbsp; <b>T</b> temperature &nbsp;·&nbsp; <span style="color:#6f42c1"><b>u</b> torque in, right end</span> &nbsp;·&nbsp; <span style="color:#d1495b"><b>y</b> output, left end</span></p>"""),
        (fig(figures.loop_diagram(feedback=False)), "grow"),
    )
    return


@app.cell(hide_code=True)
def _(mo, page, row, s_B, s_I, s_J, s_alpha, s_amp, scope):
    # display only (never reads slider values, so the widget view persists)
    page(
        mo.md("## Pluck it and watch the wave travel"),
        (row(
            mo.vstack([s_J, s_alpha, s_B, s_I, s_amp], gap=1.2, justify="center").style({"zoom": "1.6", "height": "100%"}),
            scope, cols="1fr 5fr"), "grow"),
    )
    return


@app.cell(hide_code=True)
def _(s_B, s_I, s_J, s_alpha, s_amp, scope, simulate_pluck):
    # slider changes -> new simulation pushed into the existing widget
    scope.load(simulate_pluck(J=s_J.value, alpha=s_alpha.value, B=s_B.value, inertia=s_I.value, amp=s_amp.value))
    return


@app.cell(hide_code=True)
def _(P, figures, mo, ws):
    class GKnob(ws.Knob):
        # every tick is drawn as the g_c notch: green and thick
        _css = str(ws.Knob._css) + """
        .knob-tick { stroke: #1a7f37 !important; stroke-width: 6px !important; stroke-linecap: round; }
        .knob-tick-label { fill: #1a7f37 !important; font-weight: 800; font-size: 15px !important; }
        """

    _gmax = max(round(2 * float(P.get("gc_true", 1.0)), 1), 3.0)
    knob = mo.ui.anywidget(GKnob(value=2.35, min_value=0.0, max_value=_gmax, step=0.01,
                                 label="feedback gain g", size=200, ticks=[], color=figures.ACCENT))
    # presets: (J, alpha, d, where the knob goes); "gc" = at the onset of these settings,
    # "past" = just above it, ("gc_of", J, alpha, d) = at the onset of other settings
    PRESETS = {
        "long tail": (2.8, 0.04, 120, "gc"),
        "clean oscillation": (0.9, 0.22, 120, "past"),
        "chaotic oscillation": (2.8, 0.03, 120, ("gc_of", 2.8, 0.04, 120)),
    }
    get_preset, set_preset = mo.state(None)
    preset_applied = {"t": None}
    return PRESETS, get_preset, knob, preset_applied, set_preset


@app.cell(hide_code=True)
def _(PRESETS, mo, set_preset):
    import time as _time
    preset_btns = mo.hstack(
        [mo.ui.button(label=_name, on_click=lambda _, n=_name: set_preset({"name": n, "t": _time.monotonic()}))
         for _name in PRESETS], justify="center", gap=0.4, wrap=True)
    return (preset_btns,)


@app.cell(hide_code=True)
def _(P, PRESETS, get_preset, mo):
    _p = get_preset()
    _J, _a, _d = PRESETS[_p["name"]][:3] if _p else (float(P.get("k0", 1.0)), float(P.get("alpha", 0.1)), 0)
    f_J = mo.ui.slider(0.5, 3.0, step=0.1, value=_J, label="coupling $J$", show_value=True, full_width=True)
    f_alpha = mo.ui.slider(0.02, 0.5, step=0.01, value=_a, label="damping $\\alpha$", show_value=True, full_width=True)
    f_d = mo.ui.slider(0, 300, step=10, value=_d, label="delay $d$", show_value=True, full_width=True)
    return f_J, f_alpha, f_d


@app.cell(hide_code=True)
def _(fig, figures, mo, page):
    page(
        mo.md("## Add feedback"),
        (mo.md(r"$$u[n] = u_\text{exc}[n] + g\,y[n-d]$$"), "eqbox"),
        (fig(figures.loop_diagram(learned=False, delay=True)), "grow"),
    )
    return


@app.cell(hide_code=True)
def _(DATA, mo, np, pd, run, xy_sim):
    def find_gc(lo: float, hi: float, it: int = 18) -> float:
        for _ in range(it):
            mid = 0.5 * (lo + hi)
            if xy_sim.growth_ratio(run(mid, seconds=1.5)["y"]) > 1.0:
                hi = mid
            else:
                lo = mid
        return 0.5 * (lo + hi)

    _roll = DATA / "rollouts.npz"
    GC = float(np.load(_roll)["gc_true"]) if _roll.exists() else find_gc(0.0, 3.0)

    def _amp_ratio(g):
        y = run(g, seconds=1.5)["y"]
        first = np.sqrt(np.mean(y[20:2000] ** 2)) + 1e-30
        last = np.sqrt(np.mean(y[-8000:] ** 2))
        return np.log10(max(last / first, 1e-8))  # below 1e-8: decayed to numerical noise

    _g = np.linspace(0, 2.2 * GC, 45)
    SWEEPS = pd.DataFrame({"model": "True", "gain": _g, "growth": [_amp_ratio(g) for g in _g]})
    return GC, SWEEPS


@app.cell(hide_code=True)
def _(FS, GC, SWEEPS, fig, figures, mo, np, page, plt, run):
    _sw = SWEEPS[SWEEPS.model == "True"]
    _fig = plt.figure(figsize=(13, 5.6))
    _gs = _fig.add_gridspec(2, 2, width_ratios=[1.15, 1], hspace=0.75, wspace=0.12)
    _ax = _fig.add_subplot(_gs[:, 0])
    _ax.plot(_sw.gain, _sw.growth, "o-", ms=5, color=figures.INK, lw=1.8)
    _ax.axhline(0, color=figures.MUTED, lw=0.8, ls=":")
    _ax.axvline(GC, color=figures.ACCENT, lw=2.5, ls="--")
    _ax.axvspan(0, GC, color="#f0f3f6", zorder=-1)
    _ax.text(GC * 0.5, -4, "decays", ha="center", color=figures.MUTED, fontsize=22)
    _ax.text(GC * 1.55, -4, "self-oscillates", ha="center", color=figures.ACCENT, fontsize=22, fontweight="bold")
    _ax.set_xlabel("feedback gain g", fontsize=19)
    _ax.set_ylabel("final / initial amplitude", fontsize=19)
    _ax.set_yticks([-8, -4, 0])
    _ax.set_yticklabels(["$\\leq 10^{-8}$", "$10^{-4}$", "1"])
    _ax.tick_params(labelsize=16)
    _ax.set_title(f"onset at $g_c \\approx {GC:.2f}$", loc="left", fontsize=21)
    _lo, _hi = run(0.7 * GC, 1.5)["y"], run(1.15 * GC, 1.5)["y"]
    _t = np.arange(len(_lo)) / FS
    for _row, (_y, _c, _lab, _t0, _w) in enumerate([
            (_lo, figures.INK, f"rings down at g = {0.7 * GC:.2f}", 0.0, 0.03),
            (_hi, figures.ACCENT, f"sustained tone at g = {1.15 * GC:.2f}", 1.0, 0.01)]):
        _a = _fig.add_subplot(_gs[_row, 1])
        _m = (_t >= _t0) & (_t < _t0 + _w)
        _a.plot(1e3 * (_t[_m] - _t0), _y[_m], lw=2, color=_c)
        _a.set_title(_lab, loc="left", fontsize=19, color=_c)
        _a.set_yticks([])
        _a.tick_params(labelsize=15)
        _a.set_xlabel("ms", fontsize=16)
    page(
        mo.md("## Above a critical gain $g_c$ it starts to self-oscillate"),
        (fig(figures.to_svg(_fig)), "grow"),
    )
    return


@app.cell(hide_code=True)
def _(FS, audio, f_J, f_alpha, f_d, fig, figures, knob, mo, np, page, plt, preset_btns, preset_g, row, run):
    _g = float(knob.value.get("value", 2.35) or 0.0)
    if preset_g.get("g") is not None and _g == preset_g["stale"]:
        _g = preset_g["g"]
    _y = run(_g, seconds=1.5, J=f_J.value, alpha=f_alpha.value, d=f_d.value)["y"]
    _t = np.arange(len(_y)) / FS
    _fig, (_ax, _az) = plt.subplots(1, 2, figsize=(12, 5.4), gridspec_kw={"width_ratios": [2, 1], "wspace": 0.08})
    _ax.plot(_t, _y, lw=0.7, color=figures.ACCENT)
    _ax.set_xlabel("time [s]", fontsize=17)
    _ax.set_title(f"output y(t),  g = {_g:.2f}", loc="left", fontsize=19)
    _sus = np.abs(_y[-4000:]).max() > 0.05 * max(np.abs(_y).max(), 1e-12)   # still oscillating at the end?
    _z0, _zl = (1.47, "zoom: last 30 ms") if _sus else (0.0, "zoom: first 30 ms")
    _ax.axvspan(_z0, _z0 + 0.03, color="#fde2e5", zorder=-1)
    _m = (_t >= _z0) & (_t < _z0 + 0.03)
    _az.plot(1e3 * (_t[_m] - _z0), _y[_m], lw=2, color=figures.ACCENT)
    _az.set_xlabel("ms", fontsize=17)
    _az.set_title(_zl, loc="left", fontsize=19)
    _az.set_facecolor("#fff7f8")
    for _a in (_ax, _az):
        _a.set_yticks([])
        _a.tick_params(labelsize=15)
    _lim = max(np.abs(_y[_m]).max(), 1e-9) * 1.1
    _az.set_ylim(-_lim, _lim)
    page(
        mo.md("## Turn up the gain"),
        (row(mo.vstack([preset_btns, knob, audio(_y),
                        mo.vstack([f_J, f_alpha, f_d], gap=0.3).style({"width": "100%"}),
                        mo.md('<p class="knob-key"><span style="color:#1a7f37">▮</span> g<sub>c</sub> for these settings</p>')],
                       align="center", justify="center", gap=0.3).style({"height": "100%", "zoom": "1.2"}),
             fig(figures.to_svg(_fig)), cols="1.4fr 3fr"), "grow"),
    )
    return


@app.cell(hide_code=True)
def _(PRESETS, SIM_KW, f_J, f_alpha, f_d, get_preset, knob, mo, np, preset_applied, xy_sim):
    # critical gain for the current J, alpha, d (bisection, ~0.5 s); drawn as the green notch
    @mo.cache
    def _onset(J: float, alpha: float, d: int):
        def _ratio(g, n=44100):
            kw = dict(SIM_KW, k0=J, alpha=alpha, delay=1 + int(d))
            y = xy_sim.simulate(gain=g, n_steps=n, u_ext=xy_sim.pluck(n, 0.2, 20), **kw)["y"]
            return np.sqrt(np.mean(y[-8000:] ** 2)) / (np.sqrt(np.mean(y[20:276] ** 2)) + 1e-30)

        lo, hi = 0.0, 3.0
        while _ratio(hi) <= 1 and hi < 40:
            lo, hi = hi, 1.5 * hi
        if _ratio(hi) <= 1:
            return None
        for _ in range(16):
            mid = 0.5 * (lo + hi)
            lo, hi = (lo, mid) if _ratio(mid) > 1 else (mid, hi)
        return 0.5 * (lo + hi)

    _gc = _onset(float(f_J.value), float(f_alpha.value), int(f_d.value))
    knob.widget.ticks = [{"value": round(_gc, 2), "label": "g꜀"}] if _gc is not None else []
    # a preset button was pressed: move the knob once
    _p = get_preset()
    if _p and _p["t"] != preset_applied["t"]:
        preset_applied["t"] = _p["t"]
        _where = PRESETS[_p["name"]][3]
        if _where == "gc":
            _g = _gc
        elif _where == "past":
            _g = None if _gc is None else 1.03 * _gc
        else:
            _g = _onset(*_where[1:])
        if _g is not None:
            _g = min(round(_g, 2), knob.widget.max_value)
            # the kernel does not see a value set from Python, so remember it until the knob is turned
            preset_applied.update(g=_g, stale=float(knob.value.get("value", 0.0) or 0.0))
            knob.widget.value = _g
    preset_g = dict(preset_applied)
    return (preset_g,)


@app.cell(hide_code=True)
def _(mo, page):
    _top = {"node": "#e69f00", "phnn": "#2e6fd8", "dhnn": "#009e73", "lin": "#8b949e"}

    def _card(title, eq, txt, ref, cls):
        return (f'<div class="mcard" style="border-left-color:{_top[cls]}">'
                f'<div class="card-title" style="color:{_top[cls]}">{title}</div>'
                f'{mo.md(eq).text}<div class="card-txt">{txt}</div><div class="card-ref">{ref}</div></div>')

    _cards = [
        _card("Neural ODE", r"$$\dot x = f_\vartheta(x) + G u$$", "free-form network, <b>no physics built in</b>", "Chen et al. 2018", "node"),
        _card("Port-Hamiltonian NN", r"$$\dot x = (\mathcal{J} - \mathcal{R})\,\nabla H_\vartheta(x) + G u$$",
              "learned <b>energy</b>, <b>dissipative</b> by construction", "Desai et al. 2021 · Linares et al. 2026", "phnn"),
        _card("Dissipative HNN", r"$$\dot x = \mathcal{J}\,\nabla H_\vartheta + \nabla D_\vartheta + G u$$",
              "learned energy <b>+</b> dissipation, sign not enforced", "Sosanya & Greydanus 2022", "dhnn"),
        _card("Linear baseline", r"$$\dot x = A x + G u$$", "baseline: <b>does a network add anything?</b>", "least squares", "lin"),
    ]
    page(
        mo.md(r"## Learning the dynamics from data: $\;\dot x = f(x) + G\,u$"),
        ('<div class="grid2">' + "".join(_cards) + "</div>", "grow"),
    )
    return


@app.cell(hide_code=True)
def _(fig, figures, mo, page):
    page(
        mo.md("## Replace the plant, keep the loop"),
        (fig(figures.loop_diagram(learned=True, delay=True)), "grow"),
    )
    return


@app.cell(hide_code=True)
def _(DATA, mo):
    model_pick = mo.ui.multiselect(["NODE", "PHNN", "DHNN", "Linear"], value=["PHNN", "NODE"], label="models")
    gain_pick = mo.ui.radio(["in training range", "just above onset", "far above onset"],
                            value="just above onset", inline=True)
    HAVE_ROLLOUTS = (DATA / "rollouts.npz").exists()
    return HAVE_ROLLOUTS, gain_pick, model_pick


@app.cell(hide_code=True)
def _(DATA, GC, fig, figures, json, mo, np, page, pd, plt):
    _gt = float(json.loads((DATA / "sim_params.json").read_text())["train_gain_max"])
    _p = pd.read_csv(DATA / "gc_pred.csv")
    _fig, _ax = plt.subplots(figsize=(13, 5.6))
    _ax.axvspan(0, _gt, color="#eef1f4")
    _ax.text(_gt / 2, 4.55, f"training data\n$g \\leq {_gt:.2f}$", ha="center", va="top", fontsize=19, color=figures.INK)
    _ax.axvline(GC, color=figures.ACCENT, ls="--", lw=3)
    _ax.text(GC, 4.55, f"  true $g_c$ = {GC:.2f}", va="top", color=figures.ACCENT, fontsize=20)
    for _j, _m in enumerate(["Linear", "NODE", "DHNN", "PHNN"]):
        _v = _p[(_p.model == _m) & (_p.status == "success")].gc_pred
        _ax.plot(_v, np.full(len(_v), _j), "o", ms=17, alpha=0.7, color=figures.MODEL_COLORS[_m])
        _ax.text(-0.06 * GC, _j, _m, ha="right", va="center", fontsize=21, fontweight="bold", color=figures.MODEL_COLORS[_m])
    _ax.set_xlim(0, 1.6 * GC)
    _ax.set_ylim(-0.6, 4.7)
    _ax.set_yticks([])
    _ax.tick_params(labelsize=17)
    _ax.set_xlabel("predicted onset gain $g_c$   (3 datasets × 2 seeds)", fontsize=19)
    _ax.spines[["top", "right", "left"]].set_visible(False)
    page(
        mo.md(r"## Pilot 1 · where does it start? <span class='mock-badge'>pilot · tiny models</span>"),
        (fig(figures.to_svg(_fig)), "grow"),
    )
    return


@app.cell(hide_code=True)
def _(DATA, GC, HAVE_ROLLOUTS, fig, figures, gain_pick, mo, model_pick, np, page, plt):
    _title = mo.md(r"## Pilot 2 · does it oscillate the right way? <span class='mock-badge'>pilot · one run</span>")
    _ok = HAVE_ROLLOUTS and {"y_True", "gains_show", "t"} <= set(np.load(DATA / "rollouts.npz").files)
    if not _ok:
        _body = mo.callout(mo.md("Precomputed rollouts are missing. Run `uv run python train_models.py`."), kind="warn")
    else:
        _d = np.load(DATA / "rollouts.npz")
        _k = ["in training range", "just above onset", "far above onset"].index(gain_pick.value)
        _g = float(_d["gains_show"][_k])
        _t = _d["t"]
        _fig = plt.figure(figsize=(14, 5.6))
        _gs = _fig.add_gridspec(2, 1, hspace=0.55)
        _ov, _zm = _fig.add_subplot(_gs[0]), _fig.add_subplot(_gs[1])
        # zoom window: early ring-down in the training range, later and later for the oscillating regimes
        _w = 50.0
        _z0 = [_t[0], 0.5 * (_t[0] + _t[-1]), _t[-1] - _w][_k]
        _sel = (_t >= _z0) & (_t <= _z0 + _w)
        _ov.axvspan(_z0, _z0 + _w, color="#f4a7b2", alpha=0.6, zorder=-1)
        _series = [("True", figures.INK, 2.6)] + [(_m, figures.MODEL_COLORS[_m], 2.0) for _m in model_pick.value]
        for _m, _c, _lw in _series:
            _yy = _d[f"y_{_m}"][_k]
            _ov.plot(_t, _yy, lw=0.8, color=_c, alpha=0.8, label="true XY" if _m == "True" else _m)
            _zm.plot(_t[_sel], _yy[_sel], lw=_lw, color=_c, alpha=0.9)
        _lim = 1.15 * max(np.abs(_d["y_True"][_k]).max(), 1e-9)   # common scale: tiny numerical noise stays flat
        for _a in (_ov, _zm):
            _a.set_yticks([])
            _a.set_ylim(-_lim, _lim)
            _a.tick_params(labelsize=15)
        _ov.set_title(f"closed loop, g = {_g:.2f}", loc="right", fontsize=19)
        _ov.legend(loc="lower left", bbox_to_anchor=(0, 1.02), ncols=5, fontsize=18, frameon=False, handlelength=1.2)
        _zm.set_title(["zoom: ring-down after the pluck", "zoom: mid-run", "zoom: last cycles"][_k], loc="left", fontsize=19)
        _zm.set_facecolor("#fff7f8")
        _zm.set_xlabel("time (simulation units)", fontsize=17)
        _body = fig(figures.to_svg(_fig))
    page(_title,
         mo.hstack([gain_pick, model_pick], justify="start", gap=3).style({"zoom": "1.6"}),
         (_body, "grow"))
    return


@app.cell(hide_code=True)
def _(mo, page, row):
    _tiles = [("A", "Aims", "What do we test?", "onset&nbsp;· frequency&nbsp;· amplitude&nbsp;· failures", "#2e6fd8"),
              ("D", "Data", "How do we make the data?", "simulated XY&nbsp;· noise&nbsp;· data size&nbsp;· gap", "#009e73"),
              ("E", "Estimands", "What is the truth?", "true g<sub>c</sub>&nbsp;· frequency&nbsp;· amplitude", "#e69f00"),
              ("M", "Methods", "Who competes?", "PHNN&nbsp;· DHNN&nbsp;· NODE&nbsp;· linear", "#d1495b"),
              ("P", "Performance", "How do we score?", "bias&nbsp;· spread&nbsp;· failure rate", "#57606a")]
    _html = "".join(f'<div class="tile" style="border-top-color:{c}"><div class="tile-letter" style="color:{c}">{L}</div>'
                    f'<div class="tile-name">{n}</div><div class="tile-q">{q}</div><div class="tile-txt">{t}</div></div>'
                    for L, n, q, t, c in _tiles)
    _tree = mo.md(r"""
```text
scenario (noise × size × gap)
 └─ dataset d = 1 … D
     ├─ PHNN   seeds 1 … S
     ├─ DHNN   seeds 1 … S
     ├─ NODE   seeds 1 … S
     └─ Linear
```
""").text
    page(
        mo.md("## From one pilot run to a simulation study"),
        f'<div class="tiles">{_html}</div>',
        (row(f'<div class="tree">{_tree}</div>',
             '<p class="ademp"><b>ADEMP</b> (Morris et al. 2019): five questions, answered <span class="hl">before</span> anything is run.</p>',
             cols="1.1fr 1fr"), "grow"),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    fm_btn = mo.ui.button(value=0, on_click=lambda v: v + 1, label="randomise F")
    fm_sparse = mo.ui.switch(value=False, label="sparse (2 paths)")
    fm_g = mo.ui.slider(0.0, 8.0, step=0.05, value=4.0, label="feedback amount $g$", show_value=True, full_width=True)
    return fm_btn, fm_g, fm_sparse


@app.cell(hide_code=True)
def _(SIM_KW, fm_btn, fm_sparse, mo, np, xy_sim):
    # random 3x3 feedback matrix (inputs at rotors 2, 5, 8; taps at 1, 4, 7), scaled to ||F||_2 = 1
    _rng = np.random.default_rng(fm_btn.value)
    Fm = _rng.normal(size=(3, 3))
    if fm_sparse.value:
        _keep = np.zeros(9, bool)
        _keep[_rng.choice(9, 2, replace=False)] = True
        Fm = Fm * _keep.reshape(3, 3)
    Fm = Fm / np.linalg.norm(Fm, 2)
    _kw = {k: v for k, v in SIM_KW.items() if k not in ("tap", "input_site", "input_mode", "integrator")}

    @mo.cache
    def run_mimo(g: float, seed: int, sparse: bool, n: int = 44100):
        u = np.zeros((n, 3))
        u[:20] = 0.2
        return xy_sim.simulate_mimo(Fm, g, n_steps=n, u_ext=u, **_kw)

    def _ratio(g):
        y = run_mimo(g, fm_btn.value, fm_sparse.value)
        return np.sqrt(np.mean(y[-8000:] ** 2)) / (np.sqrt(np.mean(y[20:276] ** 2)) + 1e-30)

    _lo, _hi = 0.0, 3.0
    while _ratio(_hi) <= 1 and _hi < 40:
        _lo, _hi = _hi, 1.5 * _hi
    if _ratio(_hi) > 1:
        for _ in range(12):
            _mid = 0.5 * (_lo + _hi)
            _lo, _hi = (_lo, _mid) if _ratio(_mid) > 1 else (_mid, _hi)
        gc_F = 0.5 * (_lo + _hi)
    else:
        gc_F = None
    return Fm, gc_F, run_mimo


@app.cell(hide_code=True)
def _(FS, Fm, audio, fig, figures, fm_btn, fm_g, fm_sparse, gc_F, mo, np, page, plt, row, run_mimo):
    _g = float(fm_g.value)
    _y = run_mimo(_g, fm_btn.value, fm_sparse.value, n=int(1.5 * FS))
    _t = np.arange(len(_y)) / FS
    _cols = ["#2e6fd8", "#d1495b", "#009e73"]
    _fig, _axs = plt.subplots(3, 2, figsize=(12, 5.0), sharex="col",
                              gridspec_kw={"width_ratios": [2, 1], "wspace": 0.06, "hspace": 0.15})
    _m = _t >= _t[-1] - 0.03
    for _k in range(3):
        _a, _z = _axs[_k]
        _a.plot(_t, _y[:, _k], lw=0.7, color=_cols[_k])
        _z.plot(1e3 * (_t[_m] - _t[_m][0]), _y[_m, _k], lw=2, color=_cols[_k])
        _z.set_facecolor("#fff7f8")
        _a.set_ylabel(f"$y_{_k + 1}$", fontsize=18, rotation=0, labelpad=18)
        for _ax in (_a, _z):
            _ax.set_yticks([])
            _ax.tick_params(labelsize=14)
        _lim = max(np.abs(_y[_m, _k]).max(), 1e-9) * 1.1
        _z.set_ylim(-_lim, _lim)
    _axs[2, 0].set_xlabel("time [s]", fontsize=16)
    _axs[2, 1].set_xlabel("last 30 ms", fontsize=16)

    def _cell(v):
        c = "209,73,91" if v > 0 else "46,111,216"
        return f'<div class="fm-c" style="background:rgba({c},{min(abs(v), 1):.2f})">{v:+.2f}</div>' if abs(v) > 1e-9 else '<div class="fm-c fm-0">0</div>'

    _hdr = '<div></div>' + "".join(f'<div class="fm-h">y<sub>{j + 1}</sub></div>' for j in range(3))
    _rows = "".join(f'<div class="fm-h">u<sub>{i + 1}</sub></div>' + "".join(_cell(Fm[i, j]) for j in range(3)) for i in range(3))
    _grid = f'<div class="fm-grid">{_hdr}{_rows}</div>'
    if gc_F is None:
        _status = "no onset below g = 40"
    else:
        _osc = _g > gc_F
        _status = (f'g<sub>c</sub> for this F = <b>{gc_F:.2f}</b> · '
                   + ('<span style="color:#d1495b"><b>oscillates</b></span>' if _osc else "<b>decays</b>"))
    _left = mo.vstack([mo.Html(_grid), mo.hstack([fm_btn, fm_sparse], justify="center", gap=1), fm_g,
                       mo.md(f'<p class="fm-status">{_status}</p>'), audio(_y.sum(axis=1))],
                      align="center", justify="center", gap=0.6).style({"height": "100%", "zoom": "1.15"})
    page(
        mo.md("## Three inputs, three outputs: a feedback matrix"),
        (mo.md(r"$$u[n] = u_\text{exc}[n] + g\,F\,y[n-d]$$"), "eqbox fm-eq"),
        (row(_left, fig(figures.to_svg(_fig)), cols="1.2fr 3fr"), "grow"),
    )
    return


@app.cell(hide_code=True)
def _(mo, page):
    _cards = [("Self-oscillators", "PHNNs learn self-sustained oscillators with control input", "Linares et al. 2026"),
              ("Nonlinear strings", "PHNNs identify nonlinear string dynamics", "Linares, Doras &amp; Hélie 2026 · Zheleznov et al. 2026"),
              ("Bowed strings", "robotic bowed cello string: bow, bridge &amp; nut forces", "Lampis 2025 · Zenodo 10.5281/zenodo.17795326")]
    _html = "".join(f'<div class="xcard"><div class="xcard-title">{t}</div><div class="xcard-txt">{x}</div>'
                    f'<div class="card-ref">{r}</div></div>' for t, x, r in _cards)
    page(
        mo.md("## Next: real instruments"),
        (f'<div class="xcards">{_html}</div>', "grow"),
        mo.md('<div class="changes"><b>What gets harder:</b> we only measure audio or forces, the physics is unknown, and the true onset has to be measured too.</div>'),
    )
    return


@app.cell(hide_code=True)
def _(mo, page):
    _steps = ["Characterise the onset", "Pilot all models", "Pre-specify the study", "Run &amp; analyse", "Write up"]
    _html = "".join(f'<div class="step"><div class="step-n">{i + 1}</div><div class="step-txt">{t}</div></div>'
                    for i, t in enumerate(_steps))
    _qs = ["<b>Super- or subcritical</b> Hopf? (onset looks abrupt)", "Continuous-time or per-sample reference?",
           "How far below g<sub>c</sub> can we train?", "Output only: how to <b>estimate the state</b>?"]
    page(
        mo.md("## Plan & open questions"),
        (f'<div class="steps">{_html}</div>', "grow"),
        ('<div class="qs">' + "".join(f'<div class="q">{q}</div>' for q in _qs) + "</div>", "grow"),
    )
    return


@app.cell(hide_code=True)
def _(mo, page):
    page(mo.md("## References"), (mo.md(r"""

- Agarwal, R. et al. (2021). Deep reinforcement learning at the edge of the statistical precipice. *NeurIPS 34*.
- Bates, D., Mächler, M., Bolker, B., Walker, S. (2015). Fitting linear mixed-effects models using lme4. *J. Stat. Softw.* 67(1).
- Bouthillier, X. et al. (2021). Accounting for variance in machine learning benchmarks. *MLSys 3*.
- Chen, R. T. Q., Rubanova, Y., Bettencourt, J., Duvenaud, D. (2018). Neural ordinary differential equations. *NeurIPS 31*.
- Desai, S. et al. (2021). Port-Hamiltonian neural networks for learning explicit time-dependent dynamical systems. *Phys. Rev. E* 104, 034312.
- Lampis, A. (2025). A collection of bowed responses of cello strings, parts 6 and 7. *Zenodo*, doi:10.5281/zenodo.17795326, 10.5281/zenodo.17822016.
- Linares, M., Doras, G., Hélie, T., Roebel, A. (2026). Controlled oscillation modeling using port-Hamiltonian neural networks. *Physica D* 497, 135341.
- Linares, M., Doras, G., Hélie, T. (2026). Identifying the nonlinear string dynamics with port-Hamiltonian neural networks. *arXiv:2605.12785*.
- Morris, T. P., White, I. R., Crowther, M. J. (2019). Using simulation studies to evaluate statistical methods. *Stat. Med.* 38(11).
- Patel, D., Ott, E. (2023). Using machine learning to anticipate tipping points and extrapolate to post-tipping dynamics. *Chaos* 33, 023143.
- Sosanya, A., Greydanus, S. (2022). Dissipative Hamiltonian neural networks. *arXiv:2201.10085*.
- van Tegelen, N. et al. (2025). Neural ODEs for learning and extrapolating system dynamics across bifurcations. *Chaos* 35(10), 101103.
- Wünsch, M. et al. (2025). Rethinking the handling of method failure in comparison studies. *Stat. Med.* 44.
- Zheleznov, V., Bilbao, S., Wright, A., King, S. (2026). Stable differentiable modal synthesis for learning nonlinear dynamics. *JAES* 74(7/8).
- XY rotor-chain synthesizer: *Phase Transitions in DSP: Physical Modeling via the Statistical XY Spin Hamiltonian* (manuscript, 2026).
""").style({"font-size": "0.78em", "line-height": "1.35", "columns": "2", "column-gap": "2.5em", "height": "100%"}), "grow"))
    return


@app.cell(hide_code=True)
def _():
    # helper modules, data and CSS, downloaded from the GitHub release "assets"
    import tempfile as _tempfile
    import urllib.request as _request
    from pathlib import Path as _Path

    _names = ['mods/figures.py', 'mods/xy_sim.py', 'mods/widgets.py', 'data/sim_params.json', 'data/gc_pred.csv', 'data/rollouts.npz', 'deck.css']
    ASSET_DIR = _Path(_tempfile.mkdtemp(prefix="deck_assets_"))
    for _n in _names:
        (ASSET_DIR / _n).parent.mkdir(parents=True, exist_ok=True)
        with _request.urlopen('https://github.com/Tuujj/thesis-slides/releases/download/assets/' + _n.split("/")[-1], timeout=60) as _r:
            (ASSET_DIR / _n).write_bytes(_r.read())
    return (ASSET_DIR,)


if __name__ == "__main__":
    app.run()
