#!/usr/bin/env python3
"""Caspian Industry treylerini yığır: real video/foto + iri yazılar + musiqi → MP4.

İstifadə:
  python3 scripts/trailer/render.py --lang az            # video/output/caspian-treyler-az.mp4
  python3 scripts/trailer/render.py --lang en
  python3 scripts/trailer/render.py --lang az --shots 3,9,17,29,34,53,58   # yalnız yoxlama kadrları (JPG)
Mənbələr: video/src/vid/*.mp4, video/src/img/*.jpg, video/src/music.wav (bax timeline.py, music.py).
"""
import argparse
import pathlib
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import timeline as TL  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / 'video' / 'src'
W, H, FPS = TL.W, TL.H, TL.FPS
NF = int(round(TL.DUR * FPS))
FD = '/usr/share/fonts/opentype/inter/'
F_BLACK, F_XBOLD, F_SEMI, F_MED = (FD + f for f in ('InterDisplay-Black.otf', 'InterDisplay-ExtraBold.otf',
                                                     'Inter-SemiBold.otf', 'Inter-Medium.otf'))
ORANGE, WHITE, NAVY, BLUE, PAPER = (255, 106, 61), (255, 255, 255), (1, 28, 61), (2, 93, 165), (232, 236, 251)
GRADE = 'eq=contrast=1.14:saturation=1.28:brightness=0.025:gamma={g:.3f},unsharp=5:5:0.9:5:5:0.0'


def vf_cover(w, h, fx=0.5, fy=0.5):
    return (f'scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,'
            f'crop={w}:{h}:(iw-{w})*{fx}:(ih-{h})*{fy}')


class Clip:
    """ffmpeg-dən ardıcıl RGB kadrlar (video) və ya tək kadr (foto)"""

    def __init__(self, path, n, w=W, h=H, inp=0.0, speed=1.0, focus=(0.5, 0.5), exp=1.0, still=False):
        self.w, self.h, self.last, self.still = w, h, None, still
        vf = []
        if not still and speed != 1.0:
            vf.append(f'setpts=PTS/{speed}')
        if not still:
            vf.append(f'fps={FPS}')
        vf += [vf_cover(w, h, *focus), GRADE.format(g=1.04 * exp)]
        cmd = ['ffmpeg', '-v', 'error']
        if not still:
            cmd += ['-ss', f'{inp:.3f}']
        cmd += ['-i', str(path), '-vf', ','.join(vf), '-frames:v', '1' if still else str(n),
                '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
        self.p = subprocess.Popen(cmd, stdout=subprocess.PIPE)

    def read(self):
        if self.still and self.last is not None:
            return self.last
        buf = self.p.stdout.read(self.w * self.h * 3)
        if len(buf) == self.w * self.h * 3:
            self.last = Image.frombytes('RGB', (self.w, self.h), buf)
        if self.last is None:
            raise RuntimeError('kadr oxunmadı')
        return self.last

    def close(self):
        self.p.stdout.close()
        self.p.wait()


def zoomed(im, z, w=W, h=H):
    if abs(z - 1) < 1e-4:
        return im
    cw, ch = im.width / z, im.height / z
    x0, y0 = (im.width - cw) / 2, (im.height - ch) / 2
    return im.resize((w, h), Image.BILINEAR, box=(x0, y0, x0 + cw, y0 + ch))


class Shot:
    def __init__(self, t0, t1, kind, o):
        self.t0, self.t1, self.kind, self.o = t0, t1, kind, o
        self.n = int(round((t1 - t0) * FPS))
        self.clips = []
        if kind == 'vid':
            self.clips = [Clip(SRC / 'vid' / f"{o['src']}.mp4", self.n, inp=o.get('inp', 0), speed=o.get('speed', 1.0),
                               focus=o.get('focus', (0.5, 0.5)), exp=o.get('exp', 1.0))]
        elif kind == 'img':
            self.clips = [Clip(SRC / 'img' / f"{o['src']}.jpg", 1, focus=o.get('focus', (0.5, 0.5)), still=True)]
        elif kind == 'tri':
            pw = (W - 2 * 10) // 3
            self.pw = pw
            self.clips = [Clip(SRC / 'vid' / f'{s}.mp4', self.n, w=pw, h=H, inp=inp) for s, inp in o['srcs']]

    def frame(self, t):
        u = min(1.0, max(0.0, (t - self.t0) / (self.t1 - self.t0)))
        if self.kind == 'black':
            return Image.new('RGB', (W, H), (0, 0, 0))
        if self.kind == 'tri':
            out = Image.new('RGB', (W, H), (0, 0, 0))
            for i, c in enumerate(self.clips):
                # panellər ardıcıl açılır (hər biri 4 kadr gecikmə ilə)
                a = min(1.0, max(0.0, (t - self.t0 - i * 0.13) / 0.2))
                if a <= 0:
                    c.read()
                    continue
                p = zoomed(c.read(), 1.0 + 0.05 * u, self.pw, H)
                dy = int((1 - a) ** 2 * 90)
                out.paste(p, (i * (self.pw + 10), dy))
            return out
        z0, z1 = self.o.get('zoom', (1.0, 1.0))
        im = zoomed(self.clips[0].read(), z0 + (z1 - z0) * u)
        fi = self.o.get('fade_in')
        if fi and t - self.t0 < fi:
            im = Image.blend(Image.new('RGB', (W, H), (0, 0, 0)), im, ((t - self.t0) / fi) ** 1.5)
        return im

    def close(self):
        for c in self.clips:
            c.close()


# ---------- yazılar ----------
def fit_font(path, text, size, max_w):
    f = ImageFont.truetype(path, size)
    while f.getlength(text) > max_w and size > 40:
        size -= 6
        f = ImageFont.truetype(path, size)
    return f


def spaced(d, xy, text, font, fill, tracking):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += font.getlength(ch) + tracking
    return x


def spaced_w(text, font, tracking):
    return sum(font.getlength(ch) + tracking for ch in text) - tracking


def title_layer(T):
    """yazının RGBA qatı (kölgə ilə) və ekranda yeri"""
    st = T['style']
    size = {'statement': 190 if T.get('big') else 150, 'service': 190, 'flash': 230, 'brand': 170}[st]
    max_w = 1640 if st != 'service' else 1500
    fonts = [fit_font(F_BLACK, s, size, max_w) for s, _ in T['lines']]
    fs = min(f.size for f in fonts)
    font = ImageFont.truetype(F_BLACK, fs)
    lh = int(fs * 0.98)
    widths = [font.getlength(s) for s, _ in T['lines']]
    dot = int(fs * 0.17) if T.get('dot') else 0
    eb = T.get('eyebrow')
    ef = ImageFont.truetype(F_SEMI, 34 if st == 'brand' else 44)
    eb_h = 78 if eb else 0
    pad = 90
    tw = int(max(widths + [spaced_w(eb, ef, 10) if eb else 0]) + dot * 1.6) + 2 * pad
    th = eb_h + lh * len(T['lines']) + 2 * pad
    txt = Image.new('RGBA', (tw, th), (0, 0, 0, 0))
    d = ImageDraw.Draw(txt)
    left = st == 'service'
    y = pad
    if eb:
        ew = spaced_w(eb, ef, 10)
        ex = pad if left else (tw - ew) / 2
        if left:
            d.rectangle([ex, y + 20, ex + 70, y + 26], fill=ORANGE)
            spaced(d, (ex + 92, y), eb, ef, ORANGE, 10)
        else:
            spaced(d, (ex, y), eb, ef, WHITE, 10)
        y += eb_h
    for i, ((s, orange), wd) in enumerate(zip(T['lines'], widths)):
        x = pad if left else (tw - wd - (dot * 1.6 if i == len(widths) - 1 else 0)) / 2
        d.text((x, y - fs * 0.12), s, font=font, fill=ORANGE if orange else WHITE)
        if dot and i == len(widths) - 1:
            bx, by = x + wd + dot * 0.35, y + lh - dot * 1.62
            d.rectangle([bx, by, bx + dot, by + dot], fill=ORANGE)
        y += lh
    a = txt.getchannel('A')
    sh = Image.new('RGBA', (tw, th), (0, 0, 0, 0))
    sh.putalpha(Image.eval(Image.blend(a.filter(ImageFilter.GaussianBlur(34)), a.filter(ImageFilter.GaussianBlur(9)), 0.5),
                           lambda v: min(255, int(v * 0.95))))
    layer = Image.alpha_composite(sh, txt)
    if left:
        pos = (140 - pad, H - TL.BARS_Y - 70 - th + pad)
    else:
        pos = ((W - tw) // 2, (H - th) // 2 + (10 if st != 'brand' else 0))
    return layer, pos


def put(frame, layer, pos, alpha=1.0, dy=0, scale=1.0):
    if alpha <= 0.003:
        return
    L = layer
    x, y = pos
    if abs(scale - 1) > 1e-3:
        nw, nh = int(L.width * scale), int(L.height * scale)
        x -= (nw - L.width) // 2
        y -= (nh - L.height) // 2
        L = L.resize((nw, nh), Image.BILINEAR)
    m = L.getchannel('A')
    if alpha < 0.997:
        m = m.point(lambda v: int(v * alpha))
    frame.paste(L, (int(x), int(y + dy)), m)


def ease(u):
    u = min(1.0, max(0.0, u))
    return 1 - (1 - u) ** 3


def draw_titles(frame, t, titles):
    for T, (layer, pos) in titles:
        if not (T['t0'] <= t < T['t1']):
            continue
        st = T['style']
        tin, tout = (0.10, 0.07) if st == 'flash' else (0.30, 0.18)
        a_in, a_out = ease((t - T['t0']) / tin), min(1.0, (T['t1'] - t) / tout)
        if st == 'flash':
            put(frame, layer, pos, min(a_in, a_out), scale=1.18 - 0.18 * a_in)
        elif st == 'service':
            put(frame, layer, (pos[0] - (1 - a_in) * 70, pos[1]), min(a_in, a_out))
        else:
            put(frame, layer, pos, min(a_in, a_out), dy=(1 - a_in) * 46, scale=1.0 + 0.025 * (t - T['t0']) / (T['t1'] - T['t0']))


# ---------- final kartı ----------
def end_assets(lang):
    bg = Image.new('RGB', (W, H), PAPER)
    d = ImageDraw.Draw(bg)
    for x in range(0, W, 48):
        d.line([(x, 0), (x, H)], fill=(220, 226, 246), width=1)
    for y in range(0, H, 48):
        d.line([(0, y), (W, y)], fill=(220, 226, 246), width=1)
    logo = Image.open(ROOT / 'design' / 'logo' / 'caspian-loqo-yazili.png').convert('RGBA')
    lw = 1080
    logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
    url, contact = TL.END_TEXT[lang]
    f1, f2 = ImageFont.truetype(F_XBOLD, 62), ImageFont.truetype(F_MED, 33)
    t1 = Image.new('RGBA', (W, 90), (0, 0, 0, 0))
    ImageDraw.Draw(t1).text(((W - f1.getlength(url)) / 2, 6), url, font=f1, fill=NAVY)
    t2 = Image.new('RGBA', (W, 60), (0, 0, 0, 0))
    ImageDraw.Draw(t2).text(((W - f2.getlength(contact)) / 2, 6), contact, font=f2, fill=BLUE)
    return bg, logo, t1, t2


def end_frame(t, A):
    bg, logo, t1, t2 = A
    f = bg.copy()
    e = t - TL.END_CARD
    a = ease(e / 0.7)
    put(f, logo, ((W - logo.width) // 2, 250), a, scale=0.93 + 0.07 * a + 0.012 * min(e, 9) / 9)
    b = ease((e - 1.3) / 0.6)
    if b > 0:
        lw = int(120 * b)
        ImageDraw.Draw(f).rectangle([W // 2 - lw // 2, 690, W // 2 + lw // 2, 696], fill=ORANGE)
    put(f, t1, (0, 730), ease((e - 1.5) / 0.6), dy=(1 - ease((e - 1.5) / 0.6)) * 24)
    put(f, t2, (0, 830), ease((e - 2.1) / 0.6), dy=(1 - ease((e - 2.1) / 0.6)) * 24)
    return f


# ---------- effektlər ----------
def hit_amount(t):
    """(parıltı, kadr zərbəsi) — musiqidəki zərbələrə bağlı"""
    fl = pu = 0.0
    for ts, f0, p0 in ((TL.HITS_BIG, 0.85, 0.07), (TL.HITS_MED, 0.42, 0.04), (TL.HITS_SMALL, 0.28, 0.03)):
        for h in ts:
            dt = t - h
            if 0 <= dt < 0.5:
                fl = max(fl, f0 * (1 - dt / 0.22) ** 2 if dt < 0.22 else 0)
                pu = max(pu, p0 * (1 - dt / 0.5) ** 3)
    return fl, pu


def vignette():
    m = Image.radial_gradient('L').resize((W, H))            # mərkəz 0, kənar 255
    return m.point(lambda v: int(max(0, v - 120) * 0.42))


def render(lang, out, shots_at=None):
    titles = [(T, title_layer(T)) for T in TL.TITLES[lang]]
    endA = end_assets(lang)
    vig, black, white = vignette(), Image.new('RGB', (W, H), (0, 0, 0)), Image.new('RGB', (W, H), WHITE)
    want = None if shots_at is None else {int(round(s * FPS)): s for s in shots_at}
    enc = None
    if want is None:
        out.parent.mkdir(parents=True, exist_ok=True)
        enc = subprocess.Popen(
            ['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
             '-i', str(SRC / 'music.wav'), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-pix_fmt', 'yuv420p',
             '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', '-shortest', str(out)], stdin=subprocess.PIPE)
    si, shot = -1, None
    for i in range(NF):
        t = i / FPS
        while si + 1 < len(TL.SHOTS) and t >= TL.SHOTS[si + 1][0] - 1e-6:
            if shot:
                shot.close()
            si += 1
            shot = Shot(*TL.SHOTS[si])
        need = want is None or i in want
        if shot.kind == 'end':
            f = end_frame(t, endA) if need else None
        else:
            f = shot.frame(t)                                  # həmişə oxu (ardıcıllıq pozulmasın)
            if need:
                f = f.copy()
                fl, pu = hit_amount(t)
                if pu > 0.002:
                    f = zoomed(f, 1 + pu)
                f.paste(black, (0, 0), vig)
                draw_titles(f, t, titles)
                d = ImageDraw.Draw(f)
                d.rectangle([0, 0, W, TL.BARS_Y], fill=(0, 0, 0))
                d.rectangle([0, H - TL.BARS_Y, W, H], fill=(0, 0, 0))
                if fl > 0.01:
                    f = Image.blend(f, white, min(0.9, fl))
        if need and shot.kind == 'end':
            e = t - TL.END_CARD
            if e < 0.3:
                f = Image.blend(f, white, 0.9 * (1 - e / 0.3))
            if t > TL.DUR - 0.7:
                f = Image.blend(f, black, min(1.0, (t - (TL.DUR - 0.7)) / 0.6))
        if want is None:
            enc.stdin.write(f.tobytes())
            if i % 300 == 0:
                print(f'kadr {i}/{NF}', flush=True)
        elif i in want:
            p = out.parent / f'treyler-{lang}-{want[i]:05.1f}.jpg'
            p.parent.mkdir(parents=True, exist_ok=True)
            f.save(p, quality=86)
            print('kadr', p.name, flush=True)
            if i == max(want):
                break
    if shot:
        shot.close()
    if enc:
        enc.stdin.close()
        enc.wait()
        print('hazırdır:', out)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', default='az', choices=['az', 'en'])
    ap.add_argument('--out')
    ap.add_argument('--shots', help='yalnız bu saniyələrin kadrları, məs. 3,9,17')
    a = ap.parse_args()
    out = pathlib.Path(a.out) if a.out else ROOT / 'video' / 'output' / f'caspian-treyler-{a.lang}.mp4'
    render(a.lang, out, [float(s) for s in a.shots.split(',')] if a.shots else None)
