#!/usr/bin/env python3
"""Səsləndirmə sətirlərini (01..10) VOICEOVER.md vaxtlarına yerləşdirib video/audio/voiceover.wav yaradır.

İstifadə:  python3 scripts/build-voiceover.py [--dir video/audio/vo] [--out video/audio/voiceover.wav]
Fayllar:   01.mp3 … 10.mp3 (wav, m4a, flac, ogg da olar) — VOICEOVER.md-dəki sıra ilə, hər sətir ayrıca fayl.
Sətir öz yerinə sığmasa, 12%-ə qədər sürətləndirilir; daha çox lazımdırsa xəbərdarlıq verir.
Sonra: node scripts/render-promo.js
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TIME = re.compile(r'\*\*(\d+):(\d+(?:\.\d+)?)\s*[–-]\s*(\d+):(\d+(?:\.\d+)?)\*\*')
AUDIO = ('.mp3', '.wav', '.m4a', '.flac', '.ogg')


def slots(md):
    """VOICEOVER.md-dən (başlanğıc, son) saniyələri"""
    out = []
    for m in TIME.finditer(md.read_text(encoding='utf-8')):
        out.append((int(m.group(1)) * 60 + float(m.group(2)), int(m.group(3)) * 60 + float(m.group(4))))
    return out


def duration(path):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'json', str(path)],
                       capture_output=True, text=True, check=True)
    return float(json.loads(r.stdout)['format']['duration'])


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument('--dir', default='video/audio/vo', help='sətir faylları (01.mp3 …)')
    p.add_argument('--out', default='video/audio/voiceover.wav')
    p.add_argument('--script', default='video/caspian-promo/VOICEOVER.md')
    p.add_argument('--max-speedup', type=float, default=1.12, help='ən çox sürətləndirmə (1.12 = 12%%)')
    a = p.parse_args()

    sl = slots(ROOT / a.script)
    if not sl:
        sys.exit(f'build-voiceover: error: {a.script}-də vaxt tapılmadı')
    d = ROOT / a.dir
    files = []
    for i in range(1, len(sl) + 1):
        c = sorted(f for f in d.glob(f'{i:02d}.*') if f.suffix.lower() in AUDIO)
        if not c:
            sys.exit(f'build-voiceover: error: {i:02d}.* tapılmadı ({d})')
        files.append(c[0])

    inputs, chains, labels, warnings = [], [], [], []
    for i, ((start, end), f) in enumerate(zip(sl, files)):
        dur, room = duration(f), end - start
        tempo = 1.0
        if dur > room:
            tempo = dur / room
            if tempo > a.max_speedup:
                warnings.append(f'{i + 1:02d}: səs {dur:.1f} san, yer {room:.1f} san (×{tempo:.2f} lazım idi) — '
                                f'mətni qısaldın və ya sürəti artırıb yenidən yaradın')
                tempo = a.max_speedup
        chain = f'[{i}:a]aresample=48000,aformat=channel_layouts=mono'
        if tempo > 1.0:
            chain += f',atempo={tempo:.4f}'
        chain += f',adelay={int(round(start * 1000))}:all=1[a{i}]'
        inputs += ['-i', str(f)]
        chains.append(chain)
        labels.append(f'[a{i}]')
        print(f'{i + 1:02d}  {start:6.1f} san  yer {room:4.1f}  səs {dur:4.1f}' + (f'  sürət ×{tempo:.2f}' if tempo > 1 else ''))

    total = sl[-1][1] + 1.0
    chains.append(''.join(labels) + f'amix=inputs={len(labels)}:normalize=0,apad,atrim=0:{total:.2f}[out]')
    out = ROOT / a.out
    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', ';'.join(chains),
                    '-map', '[out]', '-ar', '48000', '-c:a', 'pcm_s16le', str(out)], check=True)
    print(f'hazırdır: {out} ({total:.1f} san)')
    for w in warnings:
        print('XƏBƏRDARLIQ:', w, file=sys.stderr)


if __name__ == '__main__':
    main()
