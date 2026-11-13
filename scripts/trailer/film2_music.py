#!/usr/bin/env python3
""""Bir detaldan böyük nəticəyə" filmi üçün 235 saniyəlik sakit musiqi (kodla, numpy). Çıxış: video/src/music2.wav
Quruluş: 0–20 yalnız pad · 20–126 yumşaq nəbz · 126–193 ritm yüksəlir · 214–227 zirvə · 227–235 sakit final (D major)."""
import pathlib
import wave

import numpy as np

SR, DUR, BEAT = 44100, 235.0, 0.75
N = int(SR * DUR)
out = np.zeros((N, 2))
f = lambda m: 440 * 2 ** ((m - 69) / 12)
CH = [[50, 57, 62, 65, 69], [46, 53, 58, 62, 65], [41, 53, 57, 60, 65], [48, 55, 60, 64, 67]]  # Dm Bb F C
BAR = BEAT * 4


def add(t0, sig, pan=0.0, g=1.0):
    i = int(t0 * SR)
    if i >= N:
        return
    sig = sig[: N - i] * g
    out[i:i + len(sig), 0] += sig * (1 - max(0, pan))
    out[i:i + len(sig), 1] += sig * (1 + min(0, pan))


def lvl(t, pts):
    return float(np.interp(t, [p[0] for p in pts], [p[1] for p in pts]))


PAD = [(0, .5), (20, .7), (126, .8), (193, .7), (214, 1), (227, .9), (235, .0)]
PULSE = [(0, 0), (18, 0), (24, .5), (126, .6), (150, 1), (193, .6), (214, 1), (226, .7), (229, 0)]
BEATS = [(0, 0), (120, 0), (130, .7), (190, .8), (196, .2), (212, .3), (216, 1), (225, .8), (227.5, 0)]
bar = 0
t = 0.0
while t < DUR:
    ch = CH[bar % 4] if t < 227 else [50, 57, 62, 66, 69]
    L = BAR + 1.5
    x = np.arange(int(L * SR)) / SR
    env = np.minimum(1, x / 1.2) * np.minimum(1, (L - x) / 1.5)
    for k, m in enumerate(ch):
        s = sum(np.sin(2 * np.pi * f(m) * h * x + k) / h ** 1.6 for h in (1, 2, 3)) * (1 + .15 * np.sin(2 * np.pi * .2 * x + k))
        add(t, s * env, pan=(k - 2) * .25, g=.035 * lvl(t, PAD) * (1.5 if k == 0 else 1))
    if lvl(t, PAD) > .95:  # zirvədə yuxarı oktava
        for k, m in enumerate(ch[2:]):
            add(t, np.sin(2 * np.pi * f(m + 12) * x) * env, pan=.3 - k * .3, g=.02)
    for e in range(8):  # səkkizlik nəbz
        te = t + e * BEAT / 2
        g = lvl(te, PULSE)
        if g > 0:
            m = ch[[2, 4, 3, 4, 2, 3, 4, 3][e]] + 12
            xx = np.arange(int(.5 * SR)) / SR
            add(te, (np.sin(2 * np.pi * f(m) * xx) + .3 * np.sin(4 * np.pi * f(m) * xx)) * np.exp(-xx * 9), pan=.4 if e % 2 else -.4, g=.05 * g)
    for b in range(4):  # yumşaq zərbə
        tb = t + b * BEAT
        g = lvl(tb, BEATS)
        if g > 0 and b in (0, 2):
            xx = np.arange(int(.35 * SR)) / SR
            add(tb, np.sin(2 * np.pi * (48 * xx + 40 * (1 - np.exp(-xx * 30)) / 30 * 3)) * np.exp(-xx * 12), g=.22 * g)
    t += BAR
    bar += 1
out /= max(1e-9, np.abs(out).max()) / .7
p = pathlib.Path(__file__).resolve().parents[2] / 'video' / 'src' / 'music2.wav'
with wave.open(str(p), 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((out * 32767).astype('<i2').tobytes())
print('hazırdır:', p)
