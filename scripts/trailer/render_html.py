#!/usr/bin/env python3
"""window.seek(t) olan HTML səhnəsini kadr-kadr MP4-ə çevirir (Playwright + ffmpeg).

İstifadə: python3 scripts/trailer/render_html.py [scripts/trailer/carousel.html] [--out video/output/karusel-sinaq.mp4]
          --shots 1.0,3.2  → yalnız JPG yoxlama kadrları
"""
import argparse
import pathlib
import subprocess

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[2]
ap = argparse.ArgumentParser()
ap.add_argument('html', nargs='?', default='scripts/trailer/carousel.html')
ap.add_argument('--out', default='video/output/karusel-sinaq.mp4')
ap.add_argument('--fps', type=int, default=30)
ap.add_argument('--shots')
ap.add_argument('--query', default='', help="məs. 'dur=34.3&stops=7'")
a = ap.parse_args()
out = ROOT / a.out
out.parent.mkdir(parents=True, exist_ok=True)
with sync_playwright() as pw:
    b = pw.chromium.launch()
    p = b.new_page(viewport={'width': 1920, 'height': 1080})
    p.goto((ROOT / a.html).as_uri() + ('?' + a.query if a.query else ''))
    p.evaluate('Promise.all([...document.images].map(i => i.decode().catch(() => {}))).then(() => document.fonts.ready)')
    dur = p.evaluate('window.DURATION')
    if a.shots:
        for s in a.shots.split(','):
            p.evaluate('t => window.seek(t)', float(s))
            p.screenshot(path=str(out.parent / f'karusel-{s}.jpg'), type='jpeg', quality=85)
        print('kadrlar hazır')
    else:
        n = int(dur * a.fps)
        enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', str(a.fps), '-c:v', 'mjpeg', '-i', '-',
                                '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
                                str(out)], stdin=subprocess.PIPE)
        for i in range(n):
            p.evaluate('t => window.seek(t)', i / a.fps)
            enc.stdin.write(p.screenshot(type='jpeg', quality=95))
        enc.stdin.close()
        enc.wait()
        print('hazırdır:', out, f'{dur:.1f} san')
    b.close()
