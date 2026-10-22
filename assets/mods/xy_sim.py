"""
xy_sim.py -- minimal deterministic (T=0) reference implementation of the
XY rotor-chain synthesizer with delayed output -> input feedback.

Mirrors the conventions of the XY V3 codebase (XY_CCP.pyx
`_step_block_ptrs_multi_out`, audio.py `_callback`, feedback_delay.py):

  * Force on rotor j (nearest neighbour, open chain):
        F_j = k0 * [ sin(th_{j+1}-th_j) + sin(th_{j-1}-th_j) ] + B * sin(phi_B - th_j)
    (open boundary: the missing neighbour term is 0; NOTE the codebase kernel
    computes d = diff[j]-diff[j-1] with diff[n-1]=0 and li=0 for j=0, which
    makes rotor 0's coupling force identically 0 -- harmless because rotor 0 is
    normally the clamped input.  Reproduced here.)
  * Damping is applied to omega directly (not divided by I):
        EULER : om += dt*(-alpha*om + F/I);  th += dt*om
        BAOAB : om += dt*F/I; th += dt/2*om; om *= exp(-alpha*dt); th += dt/2*om
  * dt per audio sample = slider_dt * physics_speed = (1/44100)*10000 ~= 0.2268
  * Audio input is NOT a torque in the codebase: the input rotor is clamped
        th_in = pi/2 + clip(drive,-1,1) * (interval_deg/2 in rad),  om_in = 0
    (input_mode='clamp', default).  input_mode='torque' instead adds
    torque_scale*drive to F_in (not what the app does; offered for comparison).
  * Output tap:  x = 0.8*sin(th_tap)  ->  DC blocker  y = x - x_prev + r*y_prev
    (r = 0.995 default).  readout='cos'/'omega' are extra (non-codebase) options.
  * Feedback: drive[n] = clip(u_ext[n] + gain*y[n-delay], -1, 1)
    gain = feedback_pct/100 * matrix[(out,in)]; in the app delay is
    (delay_frames+1)*blocksize samples (block delay line, min 1 block = 256).
"""
from __future__ import annotations

import math
import numpy as np

try:  # optional JIT
    from numba import njit
    HAVE_NUMBA = True
except Exception:  # pragma: no cover
    HAVE_NUMBA = False

    def njit(*a, **k):
        def deco(f):
            return f
        return deco(a[0]) if (a and callable(a[0])) else deco

DT_APP = (1.0 / 44100.0) * 10000.0   # slider dt * physics_speed


@njit(cache=True)
def _wrap(a):
    return (a + math.pi) % (2.0 * math.pi) - math.pi


@njit(cache=True)
def _run(th, om, n_steps, k0, alpha, B, phi_B, inertia, dt, half_int,
         input_site, tap, gain, delay, u_ext, dc_r, out_scale,
         readout_code, input_mode, torque_scale, integrator, periodic,
         theta_hist, omega_hist, u_hist, y_hist, x_prev, y_prev, record_every):
    n = th.shape[0]
    F = np.zeros(n)
    diff = np.zeros(n)
    inv_I = 1.0 / inertia
    half_dt = 0.5 * dt
    decay = math.exp(-alpha * dt)
    base = 0.5 * math.pi
    rec = 0
    for s in range(n_steps):
        # ---- drive = external + delayed feedback, clipped (audio.py L1022-1024)
        fb = 0.0
        if delay > 0 and s - delay >= 0:
            fb = gain * y_hist[s - delay]
        d_in = u_ext[s] + fb
        if d_in > 1.0:
            d_in = 1.0
        elif d_in < -1.0:
            d_in = -1.0
        u_hist[s] = d_in
        # ---- input injection
        if input_mode == 0:  # clamp (codebase)
            th[input_site] = base + d_in * half_int
            om[input_site] = 0.0
        # ---- forces (XY_CCP.pyx L686-760)
        for j in range(n):
            if j == n - 1:
                ri = 0 if periodic else n - 1
            else:
                ri = j + 1
            diff[j] = math.sin(th[ri] - th[j])
        for j in range(n):
            if j == 0:
                li = n - 1 if periodic else 0
            else:
                li = j - 1
            F[j] = k0 * (diff[j] - diff[li])
            if B != 0.0:
                F[j] += B * math.sin(phi_B - th[j])
        if input_mode == 1:
            F[input_site] += torque_scale * d_in
        # ---- integrator
        if integrator == 0:  # EULER (mode 1)
            for j in range(n):
                om[j] += dt * (-alpha * om[j] + F[j] * inv_I)
            if input_mode == 0:
                om[input_site] = 0.0
            for j in range(n):
                th[j] = _wrap(th[j] + dt * om[j])
        else:  # BAOAB at T=0 (mode 0)
            for j in range(n):
                om[j] += dt * F[j] * inv_I
            if input_mode == 0:
                om[input_site] = 0.0
            for j in range(n):
                th[j] = _wrap(th[j] + half_dt * om[j])
            for j in range(n):
                om[j] *= decay
            if input_mode == 0:
                om[input_site] = 0.0
            for j in range(n):
                th[j] = _wrap(th[j] + half_dt * om[j])
        # ---- output tap + DC blocker (XY_CCP.pyx L1021-1032)
        if readout_code == 0:
            x = out_scale * math.sin(th[tap])
        elif readout_code == 1:
            x = out_scale * math.cos(th[tap])
        else:
            x = om[tap]
        if dc_r > 0.0:
            y = x - x_prev + dc_r * y_prev
            x_prev = x
            y_prev = y
        else:
            y = x
        y_hist[s] = y
        if record_every > 0 and s % record_every == 0:
            for j in range(n):
                theta_hist[rec, j] = th[j]
                omega_hist[rec, j] = om[j]
            rec += 1
    return x_prev, y_prev


_READOUT = {"sin": 0, "cos": 1, "omega": 2}


def simulate(N=12, k0=1.0, alpha=0.3, B=0.5, gain=0.0, delay=256, tap=None,
             input_site=0, n_steps=20000, dt=DT_APP, u_ext=None, theta0=None,
             readout="sin", *, B_dir_deg=180.0, inertia=1.0, interval_deg=180.0,
             dc_r=0.995, out_scale=0.8, input_mode="clamp", torque_scale=1.0,
             integrator="euler", periodic=False, settle_steps=4000,
             record_every=1):
    """Run the chain sample-by-sample with delayed feedback.

    Returns dict(theta, omega, u, y, t):
      theta, omega : (n_steps//record_every, N) state history
      u            : (n_steps,) applied drive (clipped ext+feedback; in clamp mode
                     input angle = pi/2 + u*interval/2)
      y            : (n_steps,) DC-blocked output (the signal that is fed back)
    Before t=0 the chain is relaxed for `settle_steps` with zero drive/feedback
    and the DC blocker is pre-loaded so y starts at ~0.
    """
    if tap is None:
        tap = N - 1
    th = np.full(N, 0.5 * np.pi) if theta0 is None else np.asarray(theta0, float).copy()
    om = np.zeros(N)
    phi_B = np.deg2rad(B_dir_deg)
    half_int = 0.5 * np.deg2rad(interval_deg)
    rc = _READOUT[readout]
    im = 0 if input_mode == "clamp" else 1
    ig = 0 if integrator.lower() == "euler" else 1
    args = (k0, alpha, B, phi_B, inertia, dt, half_int, int(input_site), int(tap))
    # settle (no feedback, no input)
    if settle_steps > 0:
        dummy2 = np.zeros((1, N))
        yb = np.zeros(settle_steps)
        _run(th, om, settle_steps, *args, 0.0, 0, np.zeros(settle_steps), 0.0,
             out_scale, rc, im, torque_scale, ig, periodic,
             dummy2, dummy2, np.zeros(settle_steps), yb, 0.0, 0.0, 0)
    # preload DC blocker with steady-state input
    if rc == 0:
        x0 = out_scale * np.sin(th[tap])
    elif rc == 1:
        x0 = out_scale * np.cos(th[tap])
    else:
        x0 = om[tap]
    u_ext = np.zeros(n_steps) if u_ext is None else np.asarray(u_ext, float)
    nrec = (n_steps + record_every - 1) // record_every
    theta_hist = np.zeros((nrec, N))
    omega_hist = np.zeros((nrec, N))
    u_hist = np.zeros(n_steps)
    y_hist = np.zeros(n_steps)
    _run(th, om, n_steps, *args, float(gain), int(delay), u_ext, float(dc_r),
         out_scale, rc, im, torque_scale, ig, periodic,
         theta_hist, omega_hist, u_hist, y_hist, x0, 0.0, int(record_every))
    t = np.arange(n_steps) * dt
    return dict(theta=theta_hist, omega=omega_hist, u=u_hist, y=y_hist, t=t)


def pluck(n_steps, amp=0.5, width=20, start=0):
    """Short rectangular pulse on the drive (an 'impulse' through the clamp)."""
    u = np.zeros(n_steps)
    u[start:start + width] = amp
    return u


def growth_ratio(y, frac=0.2, skip=0):
    """RMS(last frac) / RMS(first frac after `skip`)."""
    n = len(y)
    w = int(frac * n)
    a = np.sqrt(np.mean(y[skip:skip + w] ** 2)) + 1e-30
    b = np.sqrt(np.mean(y[-w:] ** 2))
    return b / a


@njit(cache=True)
def _run_mimo(th, om, n_steps, k0, alpha, B, phi_B, inertia, dt, inputs, taps,
              K, delay, u_ext, dc_r, out_scale, torque_scale, clip, y_hist, x_prev, y_prev):
    """Torque inputs at `inputs`, sin readouts at `taps`, u = clip(u_ext + K y[n-delay]).
    Same force law / Euler step / DC blocker as `_run` (torque mode)."""
    n = th.shape[0]
    n_in = inputs.shape[0]
    n_out = taps.shape[0]
    F = np.zeros(n)
    diff = np.zeros(n)
    inv_I = 1.0 / inertia
    for s in range(n_steps):
        for j in range(n):
            ri = n - 1 if j == n - 1 else j + 1
            diff[j] = math.sin(th[ri] - th[j])
        for j in range(n):
            li = 0 if j == 0 else j - 1
            F[j] = k0 * (diff[j] - diff[li]) + B * math.sin(phi_B - th[j])
        for i in range(n_in):
            d_in = u_ext[s, i]
            if s - delay >= 0:
                for k in range(n_out):
                    d_in += K[i, k] * y_hist[s - delay, k]
            if d_in > clip:
                d_in = clip
            elif d_in < -clip:
                d_in = -clip
            F[inputs[i]] += torque_scale * d_in
        for j in range(n):
            om[j] += dt * (-alpha * om[j] + F[j] * inv_I)
        for j in range(n):
            th[j] = _wrap(th[j] + dt * om[j])
        for k in range(n_out):
            x = out_scale * math.sin(th[taps[k]])
            y = x - x_prev[k] + dc_r * y_prev[k]
            x_prev[k] = x
            y_prev[k] = y
            y_hist[s, k] = y


def simulate_mimo(Fmat, gain, inputs=(2, 5, 8), taps=(1, 4, 7), N=9, k0=1.0, alpha=0.1, B=0.2,
                  n_steps=44100, delay=1, u_ext=None, dt=DT_APP, *, B_dir_deg=180.0, inertia=1.0,
                  dc_r=0.995, out_scale=0.8, torque_scale=0.5, clip=1.0, settle_steps=4000, **_):
    """Multi-input multi-output loop: u[n] = clip(u_ext[n] + gain * F y[n-delay]).
    Fmat has shape (len(inputs), len(taps)). Returns y with shape (n_steps, len(taps))."""
    inputs = np.asarray(inputs, np.int64)
    taps = np.asarray(taps, np.int64)
    th = np.full(N, 0.5 * np.pi)
    om = np.zeros(N)
    args = (k0, alpha, B, np.deg2rad(B_dir_deg), inertia, dt, inputs, taps)
    tail = (float(dc_r), float(out_scale), float(torque_scale), float(clip))
    if settle_steps > 0:
        _run_mimo(th, om, settle_steps, *args, np.zeros((len(inputs), len(taps))), 1,
                  np.zeros((settle_steps, len(inputs))), *tail,
                  np.zeros((settle_steps, len(taps))), np.zeros(len(taps)), np.zeros(len(taps)))
    x0 = out_scale * np.sin(th[taps])
    u_ext = np.zeros((n_steps, len(inputs))) if u_ext is None else np.asarray(u_ext, float)
    y = np.zeros((n_steps, len(taps)))
    _run_mimo(th, om, n_steps, *args, float(gain) * np.asarray(Fmat, float), int(delay),
              u_ext, *tail, y, x0.copy(), np.zeros(len(taps)))
    return y
