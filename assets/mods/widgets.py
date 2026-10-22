"""widgets.py -- browser-side anywidgets for the marimo slide deck.

RotorScope      chain-of-rotors animation + oscilloscope of the output y.
                The "pluck" button replays a precomputed trajectory and plays
                the WAV entirely in the browser (no Python round-trip).
simulate_pluck  runs xy_sim.simulate for one torque pluck and returns a dict
                whose keys are RotorScope traits:  RotorScope(**sim)  or
                scope.load(sim).
wav_b64         16-bit mono WAV (base64) with a gentle limiter.

Rotor 0 of an open chain gets no coupling force in the kernel, so it acts as a
fixed wall/anchor; the widget shows rotors 1..N-1 (display index = rotor - 1).
"""
from __future__ import annotations

import base64
import io
import wave

import anywidget
import numpy as np
import traitlets

import xy_sim

FS = 44100
RED = "#d1495b"    # output / needles
BLUE = "#6f42c1"   # input (purple: blue is reserved for learned models)


# --------------------------------------------------------------------------- audio
def wav_b64(y, fs: int = FS, ceiling: float = 0.3, ref: float = 0.25, fade_ms: float = 5.0) -> str:
    """16-bit mono WAV as base64, with a limiter.

    DC removed, `fade_ms` fade-in/out, then  g = y / max(peak, ref)  (loud
    signals are normalised, quiet decays are NOT boosted above y/ref), then a
    tanh soft clip scaled so |out| <= ceiling (0.3 ~ -10 dBFS).
    """
    y = np.nan_to_num(np.asarray(y, float).ravel())
    if y.size == 0:
        y = np.zeros(1)
    y = y - y.mean()
    nf = min(int(fs * fade_ms / 1000), y.size // 2)
    if nf > 0:
        ramp = 0.5 - 0.5 * np.cos(np.linspace(0, np.pi, nf))
        y[:nf] *= ramp
        y[-nf:] *= ramp[::-1]
    g = y / max(float(np.abs(y).max()), ref)          # |g| <= 1
    k = 1.5                                            # soft-clip knee
    out = ceiling * np.tanh(k * g) / np.tanh(k)        # |out| <= ceiling
    pcm = np.clip(out, -1, 1) * 32767
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(int(fs))
        w.writeframes(pcm.astype("<i2").tobytes())
    return base64.b64encode(buf.getvalue()).decode()


# --------------------------------------------------------------------------- physics
def simulate_pluck(N: int = 21, J: float = 1.0, alpha: float = 0.1, B: float = 0.2,
                   inertia: float = 1.0, amp: float = 0.6, seconds: float = 1.0,
                   record_every: int = 2, input_site: int | None = None, tap: int = 1,
                   torque_scale: float = 0.5, width: int = 20, max_frames: int = 3600,
                   min_frames: int = 1800, tail_tol: float = 2e-4, volume: float = 0.3,
                   dt: float = xy_sim.DT_APP, integrator: str = "euler") -> dict:
    """One torque pluck (rect pulse `amp` x `width` samples) on the rightmost
    rotor, read out at `tap` (next to the wall).  gain = 0 (no feedback).

    The chain starts exactly at rest (all rotors along the field, B_dir = 180 deg).
    The trajectory is cut once max|omega| < tail_tol (but kept >= min_frames and
    <= max_frames frames).  Returns RotorScope traits:
      traj  (frames x N-1 angles, rotors 1..N-1), eq, y, u (rate: y_per_frame
      samples per frame, aligned with traj), y_per_frame, fs, audio_b64
      (`seconds` of real-time audio limited to `volume`), labels.
    """
    N = int(N)
    input_site = N - 1 if input_site is None else int(input_site)
    record_every = max(1, int(record_every))
    n = max(int(seconds * FS), max_frames * record_every)
    rest = np.full(N, np.pi)                       # field direction 180 deg
    r = xy_sim.simulate(N=N, k0=float(J), alpha=float(alpha), B=float(B), inertia=float(inertia),
                        gain=0.0, n_steps=n, dt=float(dt), u_ext=xy_sim.pluck(n, float(amp), int(width)),
                        theta0=rest, settle_steps=0, input_site=input_site, tap=int(tap),
                        input_mode="torque", torque_scale=float(torque_scale), B_dir_deg=180.0,
                        integrator=integrator, record_every=record_every)
    th, om, y, u = r["theta"][:, 1:], r["omega"][:, 1:], r["y"], r["u"]
    if not np.all(np.isfinite(th)):
        raise FloatingPointError("simulation blew up (NaN/inf) -- reduce dt or the parameters")
    active = np.nonzero(np.abs(om).max(1) > tail_tol)[0]
    nfr = int(np.clip((active[-1] + 1) if active.size else 0, min_frames, max_frames))
    nfr = min(nfr, len(th))
    ns = nfr * record_every
    yr = y[:int(seconds * FS)] if seconds > 0 else y
    return dict(
        traj=np.round(th[:nfr], 5).tolist(),
        eq=rest[1:].tolist(),
        y=np.round(y[:ns], 6).tolist(),
        u=np.round(u[:ns], 4).tolist(),
        y_per_frame=record_every,
        fs=FS,
        audio_b64=wav_b64(yr, ceiling=volume),
        labels=[[int(tap) - 1, "output y", RED], [input_site - 1, "input u", BLUE]],
    )


# --------------------------------------------------------------------------- widget
class RotorScope(anywidget.AnyWidget):
    """Rotor chain + oscilloscope, animated in the browser.

    traits: traj [[th_1..th_{N-1}] per frame], eq [rest angles], y / u (samples,
    y_per_frame per traj frame), zoom (needle exaggeration of th-eq, soft-limited
    to +-150 deg), speed (traj frames per 1/60 s, wall-clock based, fractional = interpolated),
    labels [[display_idx, text, color]], audio_b64 (WAV played on pluck if audio_on),
    scope_window (samples shown), scope_min (smallest y half-range, so tiny
    outputs look tiny), fs (for the real-time readout), height_chain, vh (>0: fill vh%
    of the window height; chain/scope split + text scale follow), audio_on (sound toggle).
    New traj from Python -> playback resets to rest; the view is not recreated.
    """

    _css = r"""
    .rs-root { background:#fff; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
    .rs-root canvas { display:block; width:100%; }
    .rs-bar { display:flex; align-items:center; gap:14px; margin-top:10px; }
    .rs-pluck { font-size:26px; font-weight:700; letter-spacing:.02em; padding:12px 38px; border-radius:12px;
                border:none; background:#d1495b; color:#fff; cursor:pointer;
                box-shadow:0 2px 0 #a8313f, 0 4px 14px rgba(209,73,91,.25); transition:transform .06s, filter .15s; }
    .rs-pluck:hover { filter:brightness(1.06); }
    .rs-pluck:active { transform:translateY(2px); box-shadow:0 0 0 #a8313f, 0 2px 8px rgba(209,73,91,.25); }
    .rs-reset, .rs-sound { font-size:19px; font-weight:600; padding:10px 18px; border-radius:10px; border:1px solid #d0d7de;
                background:#fff; color:#57606a; cursor:pointer; }
    .rs-reset:hover, .rs-sound:hover { background:#f6f8fa; color:#1f2328; }
    .rs-sound.off { color:#8b949e; background:#f6f8fa; border-style:dashed; }
    """

    _esm = r"""
    if (!window.__xyBlurInstalled) {
      window.__xyBlurInstalled = true;
      document.addEventListener('pointerup', () => setTimeout(() => {
        let a = document.activeElement;
        while (a && a.shadowRoot && a.shadowRoot.activeElement) a = a.shadowRoot.activeElement;
        if (a && a.tagName !== 'INPUT' && a.tagName !== 'TEXTAREA' && a.blur) a.blur();
      }, 0), true);
    }
    const RED = '#d1495b', INK = '#1f2328', MUTED = '#57606a', LINE = '#d0d7de', GRID = '#eef1f4';
    const FONT = '-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif';
    const MAXDEF = 2.6;   // soft limit of displayed deflection (rad, ~150 deg)
    const wrap = a => { a = (a + Math.PI) % (2 * Math.PI); if (a < 0) a += 2 * Math.PI; return a - Math.PI; };

    function render({ model, el }) {
      const root = document.createElement('div'); root.className = 'rs-root'; el.appendChild(root);
      const c = document.createElement('canvas'); root.appendChild(c);
      const ctx = c.getContext('2d');
      const bar = document.createElement('div'); bar.className = 'rs-bar';
      const btn = document.createElement('button'); btn.className = 'rs-pluck'; btn.textContent = '⚡ pluck';
      const rst = document.createElement('button'); rst.className = 'rs-reset'; rst.textContent = '↺ reset';
      const sndBtn = document.createElement('button'); sndBtn.className = 'rs-sound';
      bar.append(btn, rst, sndBtn); root.appendChild(bar);
      const snd = new Audio();
      let f = 0, playing = false, started = false, raf, W = 0, H = 0, dpr = 1, dirty = true, ymax = 1, umax = 1, srcB64 = '';

      function scan() {
        const y = model.get('y') || [], u = model.get('u') || [];
        let m = 0; for (const v of y) m = Math.max(m, Math.abs(v)); ymax = Math.max(m * 1.18, model.get('scope_min') || 1e-9);
        m = 0; for (const v of u) m = Math.max(m, Math.abs(v)); umax = m > 0 ? m : 1;
      }
      function stopAudio() { try { snd.pause(); snd.currentTime = 0; } catch (e) {} }
      function reset() { f = 0; playing = false; started = false; stopAudio(); dirty = true; }
      function syncSound() {
        const on = !!model.get('audio_on');
        sndBtn.textContent = on ? '🔊 sound on' : '🔇 sound off';
        sndBtn.classList.toggle('off', !on);
        if (!on) stopAudio();
      }
      sndBtn.onclick = () => { model.set('audio_on', !model.get('audio_on')); model.save_changes(); syncSound(); };
      model.on('change:audio_on', syncSound);
      syncSound();
      btn.onclick = () => {
        f = 0; playing = true; started = true; dirty = true;
        const a = model.get('audio_b64');
        if (a && model.get('audio_on')) {
          if (a !== srcB64) { snd.src = 'data:audio/wav;base64,' + a; srcB64 = a; }
          try { snd.currentTime = 0; } catch (e) {}
          snd.play().catch(() => {});
        }
      };
      rst.onclick = reset;
      model.on('change:traj', () => { scan(); reset(); });
      model.on('change:y', () => { scan(); dirty = true; });
      model.on('change:u', () => { scan(); dirty = true; });
      model.on('change:scope_min', () => { scan(); dirty = true; });
      for (const k of ['eq', 'zoom', 'labels', 'scope_window', 'height_chain', 'vh']) model.on('change:' + k, () => { dirty = true; });

      // layout: vh > 0 -> total height = vh% of the window, chain gets what its rotors need
      // (R capped by the width gap AND ~half the height), the scope takes the rest.
      function geom(N) {
        const vh = model.get('vh') || 0, gapEst = (W - 70) / Math.max(1, N);
        let R, chainH, scopeH, sc = 1;
        if (vh > 0) {
          const Ht = Math.max(320, Math.round(vh / 100 * (window.innerHeight || 800)));
          sc = Math.max(1, Math.min(1.4, Ht / 520));
          const pad = Math.round(84 * sc);
          R = Math.max(9, Math.min(0.44 * gapEst, (0.5 * Ht - pad) / 2, 90));
          chainH = model.get('height_chain') || Math.round(2 * R + pad);
          scopeH = Math.max(150, Ht - chainH - 12);
        } else {
          R = Math.max(9, Math.min(48, 0.44 * gapEst));
          chainH = model.get('height_chain') || Math.round(2 * R + 84);
          scopeH = Math.round(Math.max(170, Math.min(230, 0.17 * W)));
        }
        const x0 = 46 + R, x1 = W - 14 - R;
        const gap = N > 1 ? (x1 - x0) / (N - 1) : 0;
        return { R, x0, gap, chainH, scopeH, sc };
      }

      function drawChain(g, d, eq) {
        const { R, x0, gap } = g, N = eq.length, yc = 18 + R, labels = model.get('labels') || [];
        // wall (rotor 0 = fixed anchor)
        const wx = 16, wh = Math.max(R, 18);
        ctx.strokeStyle = '#8b949e'; ctx.lineWidth = 3; ctx.lineCap = 'butt';
        ctx.beginPath(); ctx.moveTo(wx, yc - wh); ctx.lineTo(wx, yc + wh); ctx.stroke();
        ctx.lineWidth = 1.4;
        for (let k = -wh; k < wh; k += 8) { ctx.beginPath(); ctx.moveTo(wx, yc + k); ctx.lineTo(wx - 9, yc + k + 8); ctx.stroke(); }
        // bonds
        ctx.strokeStyle = LINE; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(wx, yc); ctx.lineTo(x0 - R, yc);
        for (let i = 0; i < N - 1; i++) { const x = x0 + i * gap; ctx.moveTo(x + R, yc); ctx.lineTo(x + gap - R, yc); }
        ctx.stroke(); ctx.setLineDash([]);
        const z = model.get('zoom'), lw = Math.max(2.5, Math.min(6, 0.15 * R));
        for (let i = 0; i < N; i++) {
          const x = x0 + i * gap, lab = labels.find(l => l[0] === i);
          const def = MAXDEF * Math.tanh(z * d[i] / MAXDEF);
          // circle, tinted by |deflection| so the travelling wave reads from afar
          ctx.beginPath(); ctx.arc(x, yc, R, 0, 2 * Math.PI);
          ctx.fillStyle = `rgba(209,73,91,${Math.min(0.32, 0.4 * Math.abs(def)).toFixed(3)})`; ctx.fill();
          ctx.strokeStyle = lab ? lab[2] : '#b6bec8'; ctx.lineWidth = lab ? Math.max(2.5, 0.08 * R) : 1.5; ctx.stroke();
          const a = eq[i] + def;
          ctx.beginPath(); ctx.moveTo(x, yc); ctx.lineTo(x + 0.88 * R * Math.cos(a), yc - 0.88 * R * Math.sin(a));
          ctx.strokeStyle = RED; ctx.lineWidth = lw; ctx.lineCap = 'round'; ctx.stroke();
          ctx.beginPath(); ctx.arc(x, yc, Math.max(2.5, 0.09 * R), 0, 2 * Math.PI); ctx.fillStyle = INK; ctx.fill();
          if (lab) {
            ctx.font = `700 ${Math.round(g.sc * Math.max(18, Math.min(22, 0.5 * R + 10)))}px ${FONT}`;
            const tw = ctx.measureText(lab[1]).width, tx = Math.min(Math.max(x, tw / 2 + 2), W - tw / 2 - 2);
            ctx.fillStyle = lab[2]; ctx.textAlign = 'center'; ctx.textBaseline = 'alphabetic';
            ctx.fillText(lab[1], tx, yc + R + Math.round(30 * g.sc)); ctx.textAlign = 'left';
          }
        }
      }

      function drawScope(top, h, s, sc) {
        const F = Math.round(20 * sc), Fs = Math.round(16 * sc);
        const L = 8, Rr = W - 8, w = Rr - L, mid = top + h / 2 + 0.4 * F, half = h / 2 - 1.1 * F;
        const win = Math.max(10, model.get('scope_window')), y = model.get('y') || [], u = model.get('u') || [];
        ctx.fillStyle = '#fbfcfd'; ctx.fillRect(L, top, w, h);
        ctx.strokeStyle = GRID; ctx.lineWidth = 1; ctx.beginPath();
        for (let k = 1; k < 10; k++) { const x = L + k * w / 10; ctx.moveTo(x, top); ctx.lineTo(x, top + h); }
        for (let k = 1; k < 4; k++) { const yy = top + k * h / 4; ctx.moveTo(L, yy); ctx.lineTo(Rr, yy); }
        ctx.stroke();
        ctx.strokeStyle = LINE; ctx.lineWidth = 1; ctx.strokeRect(L + .5, top + .5, w - 1, h - 1);
        ctx.strokeStyle = '#8b949e'; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.moveTo(L, mid); ctx.lineTo(Rr, mid); ctx.stroke();
        const X = k => Rr - (s - k) / win * w;
        const k0 = Math.max(0, Math.ceil(s - win)), k1 = Math.min(Math.floor(s), y.length - 1);
        if (started && k1 >= k0) {
          // input u (thin blue)
          ctx.beginPath(); for (let k = k0; k <= k1; k++) { const yy = mid - 0.45 * half * (u[k] || 0) / umax; k === k0 ? ctx.moveTo(X(k), yy) : ctx.lineTo(X(k), yy); }
          ctx.strokeStyle = 'rgba(46,111,216,.75)'; ctx.lineWidth = 1.6; ctx.lineJoin = 'round'; ctx.stroke();
          // output y (red)
          ctx.beginPath(); for (let k = k0; k <= k1; k++) { const yy = mid - half * y[k] / ymax; k === k0 ? ctx.moveTo(X(k), yy) : ctx.lineTo(X(k), yy); }
          ctx.strokeStyle = RED; ctx.lineWidth = 2.6; ctx.stroke();
          ctx.beginPath(); ctx.arc(X(k1), mid - half * y[k1] / ymax, 4.5, 0, 2 * Math.PI); ctx.fillStyle = RED; ctx.fill();
        }
        ctx.font = `600 ${F}px ${FONT}`; ctx.textBaseline = 'top';
        ctx.fillStyle = MUTED; ctx.textAlign = 'left'; ctx.fillText('output y (oscilloscope)', L + 10, top + 8);
        const lw0 = ctx.measureText('output y (oscilloscope)').width;
        ctx.fillStyle = 'rgba(111,66,193,.9)'; ctx.font = `600 ${F}px ${FONT}`; ctx.fillText('·  input u', L + 18 + lw0, top + 8);
        const fs = model.get('fs') || 44100, ype = model.get('y_per_frame') || 1, sp = model.get('speed') || 1;
        const slow = Math.round(fs / (60 * sp * ype * boost(s)));
        ctx.font = `600 ${F}px ${FONT}`; ctx.fillStyle = MUTED; ctx.textAlign = 'right';
        const t = started ? `t = ${(1000 * s / fs).toFixed(1)} ms   ·   ` : 'press ⚡ pluck   ·   ';
        ctx.fillText(`${t}${slow}× slow motion`, Rr - 10, top + 8);
        ctx.font = `500 ${Fs}px ${FONT}`; ctx.fillStyle = '#8b949e'; ctx.textBaseline = 'bottom';
        ctx.fillText(`window ${(1000 * win / fs).toFixed(1)} ms`, Rr - 10, top + h - 6);
        ctx.textAlign = 'left';
      }

      // slow motion for the first wave transits, then speed up so the long ring-down doesn't drag
      function boost(s) { return Math.min(2, 1 + Math.max(0, s - 1300) / 1300); }

      function draw() {
        const T = model.get('traj') || [], eq = model.get('eq') || [];
        const N = eq.length || (T[0] || []).length;
        const g = geom(N), scopeH = g.scopeH;
        const newH = g.chainH + 12 + scopeH;
        if (newH !== H) { H = newH; c.style.height = H + 'px'; c.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); }
        ctx.clearRect(0, 0, W, H); ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, W, H);
        let s = 0;
        if (N) {
          const d = new Array(N).fill(0);
          if (started && T.length) {
            const i0 = Math.min(Math.floor(f), T.length - 1), i1 = Math.min(i0 + 1, T.length - 1), fr = Math.min(1, f - i0);
            const A = T[i0], Bf = T[i1];
            for (let i = 0; i < N; i++) { const a = wrap(A[i] - eq[i]), b = wrap(Bf[i] - eq[i]); d[i] = a + (b - a) * fr; }
            s = Math.min(f, T.length - 1) * (model.get('y_per_frame') || 1);
          }
          drawChain(g, d, eq);
        }
        drawScope(g.chainH + 12, scopeH, s, g.sc);
      }

      let last = 0, ih = 0;
      function tick(now) {
        const dtick = last ? Math.min(0.1, (now - last) / 1000) : 1 / 60; last = now;
        const cw = el.clientWidth || root.clientWidth || 0;
        if (cw > 0 && cw !== W) { W = cw; dpr = window.devicePixelRatio || 1; c.width = W * dpr; H = -1; dirty = true; }
        if (window.innerHeight !== ih) { ih = window.innerHeight; dirty = true; }
        if (W > 0 && (dirty || playing)) { draw(); dirty = false; }
        if (playing) {
          const n = (model.get('traj') || []).length;
          if (f < n - 1) f = Math.min(n - 1, f + 60 * dtick * model.get('speed') * boost(f * (model.get('y_per_frame') || 1))); else playing = false;   // speed = frames per 1/60 s, display-rate independent
        }
        raf = requestAnimationFrame(tick);
      }
      scan(); raf = requestAnimationFrame(tick);
      return () => { cancelAnimationFrame(raf); stopAudio(); };
    }
    export default { render };
    """

    traj = traitlets.List([]).tag(sync=True)
    eq = traitlets.List([]).tag(sync=True)
    y = traitlets.List([]).tag(sync=True)
    u = traitlets.List([]).tag(sync=True)
    y_per_frame = traitlets.Int(1).tag(sync=True)
    fs = traitlets.Int(FS).tag(sync=True)
    zoom = traitlets.Float(6.0).tag(sync=True)
    speed = traitlets.Float(4.5).tag(sync=True)      # traj frames per display frame (x y_per_frame=2 -> 9 samples)
    labels = traitlets.List([]).tag(sync=True)
    audio_b64 = traitlets.Unicode("").tag(sync=True)
    scope_window = traitlets.Int(1500).tag(sync=True)  # ~34 ms
    audio_on = traitlets.Bool(True).tag(sync=True)    # sound toggle; persists across re-renders
    scope_min = traitlets.Float(0.01).tag(sync=True)  # min half-range of the y axis
    height_chain = traitlets.Int(0).tag(sync=True)   # 0 = auto from rotor size
    vh = traitlets.Float(0.0).tag(sync=True)          # >0: total height = vh% of window height (0 = auto)

    def load(self, sim: dict) -> None:
        """Push a simulate_pluck() result; traj is set last (it resets playback)."""
        with self.hold_sync():
            for k, v in sim.items():
                if k != "traj" and self.has_trait(k):
                    setattr(self, k, v)
            if "traj" in sim:
                self.traj = sim["traj"]
