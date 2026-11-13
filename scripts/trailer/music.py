#!/usr/bin/env python3
"""Caspian Industry treyler musiqisi, tam kodla (numpy/scipy). 120 BPM, Re minor, final Re major.

İstifadə: python3 scripts/trailer/music.py [--out video/src/music.wav]
Alətlər: sub bum, kik, taiko, snare, polad boru zərbəsi (modal sintez), saat tıqqıltısı,
pad akkordları, 16-lıq ostinato, bas, "braam", riser. Zaman şkalası: timeline.py.
"""
import argparse
import pathlib
import sys

import numpy as np
from scipy.signal import butter, fftconvolve, sosfilt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from timeline import BAR, BEAT, CHORDS, DUR, PROG, ROOTS  # noqa: E402

SR = 48000
TAIL = 4.0
N = int((DUR + TAIL) * SR)
rng = np.random.default_rng(2019)
dry = np.zeros((2, N), np.float64)
send = np.zeros((2, N), np.float64)
S16 = BEAT / 4


def mtof(m):
    return 440.0 * 2 ** ((np.asarray(m, float) - 69) / 12)


def tt(n):
    return np.arange(n) / SR


def lp(x, fc, order=2):
    return sosfilt(butter(order, min(fc, SR * 0.45), 'low', fs=SR, output='sos'), x)


def hp(x, fc, order=2):
    return sosfilt(butter(order, fc, 'high', fs=SR, output='sos'), x)


def bp(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo, min(hi, SR * 0.45)], 'band', fs=SR, output='sos'), x)


def noise(n):
    return rng.standard_normal(n)


def place(sig, t, gain=1.0, pan=0.0, rev=0.0):
    """mono və ya stereo siqnalı t saniyəsinə qoyur (bərabər güc panı)"""
    if sig.ndim == 1:
        sig = np.vstack([sig * np.sqrt(0.5 * (1 - pan)), sig * np.sqrt(0.5 * (1 + pan))])
    i = int(round(t * SR))
    if i < 0:
        sig, i = sig[:, -i:], 0
    n = min(sig.shape[1], N - i)
    if n <= 0:
        return
    dry[:, i:i + n] += gain * sig[:, :n]
    if rev:
        send[:, i:i + n] += gain * rev * sig[:, :n]


def saw(freq, n, phase0=None):
    """polyBLEP mişar dalğa (aliasingsiz)"""
    dt = np.broadcast_to(np.asarray(freq, float) / SR, (n,))
    ph = ((rng.random() if phase0 is None else phase0) + np.cumsum(dt)) % 1.0
    y = 2 * ph - 1
    m = ph < dt
    x = ph[m] / dt[m]
    y[m] -= x + x - x * x - 1
    m = ph > 1 - dt
    x = (ph[m] - 1) / dt[m]
    y[m] -= x * x + x + x + 1
    return y


def adsr(n, a=0.005, r=0.02):
    e = np.ones(n)
    na, nr = max(1, int(a * SR)), max(1, int(r * SR))
    e[:na] = np.linspace(0, 1, na)
    e[-nr:] *= np.linspace(1, 0, nr)
    return e


# ---------- zərb alətləri ----------
def boom(f0=120, f1=34, dur=3.2, decay=0.9):
    n = int(dur * SR)
    t = tt(n)
    f = f1 + (f0 - f1) * np.exp(-t / 0.05)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / decay) * np.minimum(1, t / 0.002)
    click = lp(noise(n), 2500) * np.exp(-t / 0.006) * 0.5
    thump = lp(noise(n), 180) * np.exp(-t / 0.08) * 1.2
    return np.tanh(1.6 * (body + click + thump)) * 0.9


def kick(dur=0.55):
    n = int(dur * SR)
    t = tt(n)
    f = 48 + 125 * np.exp(-t / 0.035)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.2)
    click = lp(noise(n), 7000) * np.exp(-t / 0.004) * 0.55
    return np.tanh(1.4 * (body + click)) * 0.9


def taiko(f=92, dur=1.1):
    n = int(dur * SR)
    t = tt(n)
    ff = f + 0.6 * f * np.exp(-t / 0.04)
    body = np.sin(2 * np.pi * np.cumsum(ff) / SR) * np.exp(-t / 0.33)
    skin = bp(noise(n), 200, 2800) * np.exp(-t / 0.05) * 1.0
    return np.tanh(1.5 * (body + skin)) * 0.8


def snare(dur=0.6, tone=185):
    n = int(dur * SR)
    t = tt(n)
    wires = bp(noise(n), 1500, 7500) * np.exp(-t / 0.15)
    body = np.sin(2 * np.pi * tone * t) * np.exp(-t / 0.06) * 0.7
    crack = bp(noise(n), 400, 1400) * np.exp(-t / 0.03) * 0.5
    return np.tanh(1.3 * (wires + body + crack)) * 0.7


def hat(open_=False):
    n = int((0.25 if open_ else 0.06) * SR)
    t = tt(n)
    return bp(noise(n), 6500, 13000) * np.exp(-t / (0.08 if open_ else 0.014))


def hats(t0, t1, step, gain, accent=1.6):
    k = 0
    t = t0
    while t < t1 - 1e-6:
        place(hat(), t, gain * (accent if k % 2 == 0 else 1.0), pan=0.35 if k % 2 else 0.2)
        t += step
        k += 1


def crash(dur=2.5):
    n = int(dur * SR)
    t = tt(n)
    sL, sR = hp(noise(n), 3500), hp(noise(n), 3500)
    env = np.exp(-t / 0.7) * np.minimum(1, t / 0.003)
    return np.vstack([sL, sR]) * env * 0.35


def clang(f=146.83, dur=4.0, bright=1.0, short=1.0):
    """polad borunun zərbəsi: sərbəst millin inharmonik modları"""
    ratios = [1.0, 2.756, 5.404, 8.933, 13.344, 18.64]
    amps = [1.0, 0.75, 0.55 * bright, 0.40 * bright, 0.25 * bright, 0.15 * bright]
    taus = [2.2, 1.4, 0.9, 0.55, 0.30, 0.18]
    n = int(dur * SR)
    t = tt(n)
    out = np.zeros((2, n))
    for r, a, tau in zip(ratios, amps, taus):
        fr = f * r
        if fr > SR * 0.45:
            continue
        for ch, det in ((0, 1.0), (1, 1.0025)):
            env = np.exp(-t / (tau * short))
            out[ch] += a * env * (np.sin(2 * np.pi * fr * det * t + rng.random() * 6.28)
                                  + 0.5 * np.sin(2 * np.pi * fr * (det + 0.0031) * t + rng.random() * 6.28))
    hit = bp(noise(n), 2000, 9000) * np.exp(-t / 0.008) * 1.2
    out += hit
    out *= np.minimum(1, t / 0.0015)
    return out / np.max(np.abs(out)) * 0.85


def tick(accent=False):
    s = clang(2349.0, dur=0.12, bright=0.6, short=0.012 if not accent else 0.02)
    s += hp(noise(s.shape[1]), 6000) * np.exp(-tt(s.shape[1]) / 0.003) * 0.4
    return s


# ---------- tonal alətlər ----------
def pad(chord, dur, cutoff=1200, attack=1.2, release=1.2, detune=0.09):
    n = int(dur * SR)
    out = np.zeros((2, n))
    for m in chord:
        for ch in (0, 1):
            for d in (-detune, 0.0, detune):
                out[ch] += saw(mtof(m + d + (0.03 if ch else -0.03)), n)
    out /= 3 * len(chord)
    out = np.vstack([hp(lp(out[0], cutoff, 2), 120), hp(lp(out[1], cutoff, 2), 120)])
    t = tt(n)
    env = np.minimum(1, t / max(attack, 1e-3)) * np.minimum(1, (dur - t) / max(release, 1e-3))
    env = np.clip(env, 0, 1) ** 1.5
    return out * env * (1 + 0.04 * np.sin(2 * np.pi * 0.25 * t))


def osti_note(m, dur, cutoff, vel=1.0):
    n = int(dur * SR)
    s = saw(mtof(m), n) + 0.6 * saw(mtof(m + 0.08), n) + 0.35 * saw(mtof(m + 12), n)
    s = hp(lp(s, cutoff, 2), 140)
    t = tt(n)
    env = (0.35 + 0.65 * np.exp(-t / 0.045)) * adsr(n, 0.002, 0.012)
    return s * env * vel * 0.4


OSTI = [0, 0, 12, 0, 7, 0, 12, 0, 0, 0, 12, 0, 7, 0, 12, 7]
VEL = [1, .55, .8, .55, .9, .55, .8, .6, 1, .55, .8, .55, .9, .6, .85, .7]


def ostinato(t0, t1, cut0, cut1, gain=0.22, chord_at=None):
    """16-lıq ostinato; filtr cut0-dan cut1-ə açılır; kök notu akkorda uyğun"""
    k = 0
    t = t0
    while t < t1 - 1e-6:
        root = ROOTS[chord_at(t)]
        u = (t - t0) / max(t1 - t0, 1e-6)
        cut = cut0 * (cut1 / cut0) ** u
        note = osti_note(root + OSTI[k % 16], S16 * 0.95, cut, VEL[k % 16])
        place(note, t, gain, pan=0.25 if k % 2 else -0.25, rev=0.12)
        place(note, t + 3 * S16, gain * 0.28, pan=-0.6 if k % 2 else 0.6, rev=0.2)   # 3/16 əks-səda
        t += S16
        k += 1


def bass(t0, t1, gain=0.35, chord_at=None):
    t = t0
    while t < t1 - 1e-6:
        m = ROOTS[chord_at(t)] - 24
        n = int(BEAT / 2 * 0.92 * SR)
        tt_ = tt(n)
        s = np.sin(2 * np.pi * mtof(m) * tt_) + 0.45 * lp(saw(mtof(m), n), 220) + 0.3 * bp(saw(mtof(m + 12), n), 250, 1400)
        s *= adsr(n, 0.004, 0.03) * (0.6 + 0.4 * np.exp(-tt_ / 0.08))
        place(np.tanh(1.3 * s), t, gain)
        t += BEAT / 2


def braam(root=38, dur=3.5, peak=2600):
    n = int(dur * SR)
    t = tt(n)
    voices = [root - 12, root, root + 7, root + 12]
    out = np.zeros((2, n))
    for ch in (0, 1):
        x = np.zeros(n)
        for m in voices:
            for d in (-0.15, 0.0, 0.15):
                x += saw(mtof(m + d + (0.05 if ch else -0.05)), n)
        x /= 12
        cut = 160 + peak * np.minimum(1, t / 0.22) * np.exp(-t / 0.9)
        y = np.zeros(n)
        zi = None
        blk = 256
        for i in range(0, n, blk):
            sos = butter(2, max(80, cut[i]), 'low', fs=SR, output='sos')
            if zi is None:
                zi = np.zeros((sos.shape[0], 2))
            y[i:i + blk], zi = sosfilt(sos, x[i:i + blk], zi=zi)
        out[ch] = y
    env = np.minimum(1, t / 0.03) * np.exp(-t / 1.6) * np.minimum(1, (dur - t) / 0.3)
    return np.tanh(2.6 * out) * env * 0.7


def riser(dur, f_lo=300, f_hi=6000):
    n = int(dur * SR)
    t = tt(n)
    u = t / dur
    out = np.zeros((2, n))
    blk = 512
    for ch in (0, 1):
        x = noise(n)
        y = np.zeros(n)
        zi = None
        for i in range(0, n, blk):
            c = f_lo * (f_hi / f_lo) ** u[i]
            sos = butter(2, [c * 0.7, min(c * 1.4, SR * 0.45)], 'band', fs=SR, output='sos')
            if zi is None:
                zi = np.zeros((sos.shape[0], 2))
            y[i:i + blk], zi = sosfilt(sos, x[i:i + blk], zi=zi)
        out[ch] = y
    sweep = np.sin(2 * np.pi * np.cumsum(110 * 2 ** (3 * u)) / SR) * 0.25
    out += sweep
    return out * (u ** 2.2) * 0.5


def rev_swell(f=146.83, dur=1.5):
    s = clang(f, dur=3.0)
    tail = np.vstack([fftconvolve(s[c], IR[c])[:s.shape[1]] for c in (0, 1)])
    x = tail[:, ::-1][:, -int(dur * SR):]
    return x / (np.max(np.abs(x)) + 1e-9) * 0.7 * np.linspace(0, 1, x.shape[1]) ** 1.5


def snare_roll(t0, t1, g0=0.15, g1=0.8):
    t = t0
    while t < t1 - 1e-6:
        u = (t - t0) / (t1 - t0)
        step = BEAT / 2 if u < 0.4 else (BEAT / 4 if u < 0.75 else BEAT / 8)
        place(snare(0.4), t, g0 + (g1 - g0) * u ** 1.5, pan=0.1, rev=0.25)
        t += step


def make_ir(rt60=2.6, dur=3.2, predelay=0.022):
    n = int(dur * SR)
    t = tt(n)
    env = np.exp(-6.91 * t / rt60)
    ir = []
    for _ in (0, 1):
        x = noise(n) * env
        w = np.minimum(1, t / 0.9)
        x = x * (1 - w) + lp(x, 3200) * w
        x = hp(x, 160)
        x = np.concatenate([np.zeros(int(predelay * SR)), x])
        ir.append(x / np.sqrt(np.sum(x ** 2)))
    return np.vstack(ir)


IR = make_ir()


def chord_seq(start, chords, bars_each=2):
    """t → akkord adı (start-dan başlayaraq hər bars_each taktda bir)"""
    def at(t):
        i = int((t - start + 1e-6) // (bars_each * BAR))
        return chords[min(max(i, 0), len(chords) - 1)]
    return at


def build():
    D3, A2 = 146.83, 110.0
    # ---------- GİRİŞ 0-8 ----------
    place(pad([38, 45, 50], 8.6, cutoff=650, attack=3.0, release=0.8), 0.0, 0.42, rev=0.35)
    sub = np.sin(2 * np.pi * mtof(26) * tt(int(8.2 * SR))) * np.minimum(1, tt(int(8.2 * SR)) / 6.0) ** 2
    place(sub * adsr(sub.size, 0.01, 0.2), 0.0, 0.14)
    place(boom(dur=3.0), 0.0, 0.55, rev=0.25)
    for t, f, p in ((2.0, D3, -0.2), (4.0, A2, 0.2), (6.0, D3, 0.0)):
        place(clang(f), t, 0.5, pan=p, rev=0.45)
        place(boom(f0=90, f1=40, dur=1.5, decay=0.4), t, 0.2)
    k = 0
    t = 2.0
    while t < 7.9:
        place(tick(accent=k % 4 == 0), t, 0.11 if k % 4 == 0 else 0.06, pan=0.3 if k % 2 else -0.3, rev=0.1)
        t += S16
        k += 1
    place(riser(3.0), 5.0, 0.32, rev=0.2)
    place(rev_swell(D3, 1.6), 8.0 - 1.6, 0.35)

    # ---------- QURULMA 8-24 ----------
    big_hit(8.0, 38)
    at1 = chord_seq(8.0, PROG * 2)
    for i, c in enumerate(PROG * 2):
        place(pad(CHORDS[c], 4.15, cutoff=1500 + 200 * i, attack=0.4, release=0.5), 8.0 + i * 4, 0.24, rev=0.3)
    ostinato(8.0, 24.0, 900, 4200, gain=0.24, chord_at=at1)
    bass(16.0, 24.0, 0.26, chord_at=at1)
    hats(12.0, 16.0, BEAT / 2, 0.08)
    hats(16.0, 24.0, BEAT / 4, 0.07)
    for b in range(8):
        t0 = 8.0 + b * BAR
        place(kick(), t0, 0.6)
        place(kick(), t0 + 1.0, 0.48)
        for off, f, g, p in ((0.0, 88, 0.42, -0.3), (0.75, 120, 0.3, 0.3), (1.0, 88, 0.38, -0.3),
                             (1.5, 120, 0.3, 0.35), (1.75, 120, 0.26, 0.35)):
            place(taiko(f), t0 + off, g, pan=p, rev=0.22)
    for t, f in ((16.0, D3), (18.0, A2 * 1.5), (20.0, D3 * 0.84), (22.0, D3 * 1.122)):
        place(clang(f), t, 0.45, pan=0.15, rev=0.45)
        place(boom(f0=100, f1=42, dur=1.6, decay=0.45), t, 0.25)
    place(riser(2.0), 22.0, 0.25)

    # ---------- BÖLMƏ 2: 24-31 ----------
    big_hit(24.0, 38, small=True)
    at2 = chord_seq(24.0, ['Dm', 'Bb', 'F', 'C'])
    for i, c in enumerate(['Dm', 'Bb', 'F']):
        place(pad(CHORDS[c], 4.1 if i < 2 else 3.1, cutoff=2600, attack=0.2, release=0.4), 24.0 + i * 4, 0.24, rev=0.3)
    ostinato(24.0, 31.0, 3800, 4800, gain=0.24, chord_at=at2)
    bass(24.0, 31.0, 0.27, chord_at=at2)
    hats(24.0, 31.0, BEAT / 4, 0.09)
    for b in range(4):
        t0 = 24.0 + b * BAR
        if t0 >= 31.0:
            break
        place(kick(), t0, 0.62)
        place(kick(), t0 + 0.75, 0.4)
        place(snare(), t0 + 1.0, 0.5, rev=0.3)
        if t0 < 28.0:
            for off, f, g in ((0.5, 120, 0.28), (1.5, 120, 0.28), (1.75, 105, 0.3)):
                place(taiko(f), t0 + off, g, pan=0.3, rev=0.2)
    for i, t in enumerate((28.0, 28.5, 29.0, 29.5, 30.0, 30.5)):
        place(taiko(80), t, 0.5, pan=-0.2, rev=0.25)
        place(clang(D3 * (1.0, 1.189, 1.335, 1.498, 1.682, 2.0)[i], dur=1.5, short=0.5), t, 0.3, pan=0.25, rev=0.3)
    place(rev_swell(A2, 1.0), 32.0 - 1.0, 0.32)

    # ---------- SAKİTLƏŞMƏ 32-40 ----------
    place(boom(dur=3.0), 32.0, 0.45, rev=0.3)
    place(clang(73.42, dur=5.0), 32.0, 0.35, rev=0.55)
    for i, c in enumerate(['Dm', 'Bb', 'F', 'C']):
        place(pad(CHORDS[c], 2.15, cutoff=1300 + 400 * i, attack=0.6 if i == 0 else 0.25, release=0.3), 32.0 + i * 2, 0.3, rev=0.4)
    k = 0
    t = 32.0
    while t < 39.85:
        place(tick(accent=k % 4 == 0), t, 0.09 if k % 4 == 0 else 0.05, pan=0.3 if k % 2 else -0.3, rev=0.12)
        t += S16
        k += 1
    for b in range(3):
        place(kick(), 32.0 + b * BAR + 0.0, 0.4)
        place(kick(), 32.0 + b * BAR + 0.35, 0.25)
    at3 = chord_seq(36.0, ['F', 'C'], bars_each=1)
    ostinato(36.0, 39.85, 800, 4500, gain=0.22, chord_at=at3)
    place(riser(4.0), 35.85, 0.42, rev=0.2)
    snare_roll(38.0, 39.85)

    # ---------- KULMİNASİYA 40-56 ----------
    big_hit(40.0, 38)
    at4 = chord_seq(40.0, PROG * 2)
    for i, c in enumerate(PROG * 2):
        place(pad(CHORDS[c], 4.1, cutoff=3000, attack=0.15, release=0.4), 40.0 + i * 4, 0.26, rev=0.3)
        place(pad([m + 12 for m in CHORDS[c][2:]], 4.1, cutoff=4500, attack=0.3, release=0.4), 40.0 + i * 4, 0.1, rev=0.45)
    ostinato(40.0, 55.9, 4800, 6500, gain=0.25, chord_at=at4)
    bass(40.0, 55.9, 0.28, chord_at=at4)
    for b in range(8):
        t0 = 40.0 + b * BAR
        for j in range(4):
            place(kick(), t0 + j * BEAT, 0.6 if j % 2 == 0 else 0.46)
        place(snare(), t0 + 0.5, 0.48, rev=0.28)
        place(snare(), t0 + 1.5, 0.52, rev=0.28)
        hats(t0, t0 + BAR, BEAT / 4, 0.1)
        for j in range(4):
            place(hat(True), t0 + j * BEAT + BEAT / 2, 0.13, pan=-0.3)
        for off, f, g in ((1.5, 120, 0.28), (1.625, 110, 0.28), (1.75, 100, 0.32), (1.875, 92, 0.34)):
            place(taiko(f), t0 + off, g, pan=-0.3, rev=0.2)
        if b % 2 == 1:
            place(clang((D3, A2 * 1.5, D3 * 0.84, D3 * 1.122)[b // 2], dur=3.0), t0 + 1.0, 0.33, pan=-0.15, rev=0.4)
    for t, c in ((44.0, 'Bb'), (48.0, 'Dm'), (52.0, 'F')):
        place(braam(ROOTS[c] - 12, 3.4), t, 0.42, rev=0.3)
        place(boom(dur=2.0, decay=0.6), t, 0.32)
        place(crash(1.8), t, 0.6)
    place(riser(4.0), 52.0, 0.36)
    snare_roll(55.0, 55.95, 0.3, 0.9)

    # ---------- FİNAL 56 ----------
    place(boom(f0=140, f1=32, dur=5.0, decay=1.4), 56.0, 0.75, rev=0.4)
    place(braam(26, 6.0, peak=3000), 56.0, 0.55, rev=0.45)
    place(clang(73.42, dur=6.0), 56.0, 0.6, rev=0.6)
    place(clang(146.83, dur=6.0), 56.0, 0.45, rev=0.6)
    place(crash(3.5), 56.0, 0.8, rev=0.3)
    # Loqo: Re major, işıqlı son
    place(pad(CHORDS['D'], 8.6, cutoff=1900, attack=2.2, release=3.5), 57.0, 0.24, rev=0.5)
    for t, m, g in ((57.6, 86, 0.16), (57.75, 93, 0.12), (57.9, 90, 0.1), (58.4, 98, 0.07)):
        place(clang(float(mtof(m)), dur=4.0, bright=0.5), t, g, pan=(-0.3, 0.3, 0.0, 0.2)[[57.6, 57.75, 57.9, 58.4].index(t)], rev=0.7)


def big_hit(t, root, small=False):
    place(boom(dur=3.5), t, 0.62 if not small else 0.5, rev=0.3)
    place(braam(root - 12, 3.4), t, 0.5 if not small else 0.38, rev=0.3)
    place(clang(146.83, dur=4.0), t, 0.5 if not small else 0.35, pan=-0.1, rev=0.45)
    place(crash(2.5), t, 0.7 if not small else 0.5, rev=0.2)


def master(x):
    wet = np.vstack([fftconvolve(send[c], IR[c])[:N] for c in (0, 1)])
    y = x + 0.55 * wet
    y = np.vstack([hp(y[c], 28) for c in (0, 1)])
    y = np.vstack([y[c] - 0.5 * lp(y[c], 90) + 0.6 * bp(y[c], 1200, 5000) + 0.4 * hp(y[c], 7000) for c in (0, 1)])
    # yumşaq kompressor (RMS, 30 ms)
    lev = np.sqrt(lp(np.mean(y ** 2, axis=0), 15, 1).clip(1e-12))
    thr = 0.18
    g = np.where(lev > thr, (lev / thr) ** (1 / 2.5 - 1), 1.0)
    y *= g
    y /= np.max(np.abs(y)) + 1e-9
    y = np.tanh(1.25 * y) / np.tanh(1.25)
    fade = np.ones(N)
    i0, i1 = int((DUR - 1.2) * SR), int(DUR * SR)
    fade[i0:i1] = np.linspace(1, 0, i1 - i0) ** 2
    fade[i1:] = 0
    return (y * fade * 0.89)[:, :int(DUR * SR)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='video/src/music.wav')
    a = ap.parse_args()
    build()
    y = master(dry)
    out = pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    import wave
    pcm = (np.clip(y.T, -1, 1) * 32767).astype('<i2')
    with wave.open(str(out), 'wb') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    print('hazırdır:', out, f'{y.shape[1] / SR:.1f} san', 'pik', round(float(np.max(np.abs(y))), 3))


if __name__ == '__main__':
    main()
