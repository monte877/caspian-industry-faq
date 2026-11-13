#!/usr/bin/env python3
"""5:17-lik təqdimat videosunu yenidən yığır: təkrarlanan Mündəricat hissələri kəsilir, üç bölmə yeni səhnələrlə əvəz olunur.

İstifadə: python3 scripts/trailer/assemble.py /yol/orijinal.mp4 [--out video/output/caspian-teqdimat-v3.mp4]
Əvvəlcə render et (25 fps): carousel.html → video/output/karusel-34.mp4, references.html → ref.mp4, customers.html → cust.mp4.
Hər parça orijinalın öz səsini daşıyır; yeni səhnələr orijinaldakı uyğun bölmənin səsi ilə başlayır.
"""
import argparse
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
O = ROOT / 'video' / 'output'
X = 0.4  # keçid (san)
# (video mənbəyi | None = orijinal, orijinalda başlanğıc, uzunluq)
SEGS = [
    (None, 0.0, 44.6),            # giriş, Şirkət haqqında girişi, Yeddi ölkədən
    ('books.mp4', 44.6, 18.0),    # Mündəricat — kitab rəfi (orijinalda 44.6–75.6)
    (None, 75.6, 13.4),           # 01 Şirkət haqqında
    (None, 95.4, 4.6),            # 02 Fəaliyyət sahələri başlığı                (Mündəricat 89–95 kəsildi)
    ('gallery.mp4', 100.0, 14.0), # Dörd əsas istiqamət — əyri qalereya (orijinalda 100.0–105.6)
    ('karusel-34.mp4', 105.6, 34.3),   # Təchizat portfeli — karusel
    (None, 140.4, 38.2),          # Yeddi ölkədən, inspeksiya, icarə, katalizatorlar
    (None, 184.3, 4.0),           # 03 Referans layihələr başlığı               (Mündəricat 178–184 kəsildi)
    ('ref.mp4', 188.3, 46.0),     # Referans layihələr — pazl
    ('cloud.mp4', 270.5, 14.0),   # Müştərilər — üzən loqolar                    (Mündəricat 264–270 kəsildi)
    (None, 290.0, 27.6),          # Əlaqə, Təşəkkür edirik                       (Mündəricat 284–290 kəsildi)
]

ap = argparse.ArgumentParser()
ap.add_argument('orig')
ap.add_argument('--out', default=str(O / 'caspian-teqdimat-v4.mp4'))
a = ap.parse_args()

# 1) Hər parça ayrıca fayla (yaddaşı doldurmamaq üçün), 2) sonra keçidlərlə birləşdirilir.
TMP = O / '_seg'
TMP.mkdir(parents=True, exist_ok=True)
inputs, fc = [], []
for i, (src, t0, d) in enumerate(SEGS):
    f = TMP / f's{i}.mkv'
    vin = ['-ss', f'{t0}', '-t', f'{d}', '-i', a.orig] if src is None else ['-t', f'{d}', '-i', str(O / src)]
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *vin, '-ss', f'{t0}', '-t', f'{d}', '-i', a.orig, '-map', '0:v', '-map', '1:a',
                    '-vf', 'fps=25,format=yuv420p', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-c:a', 'pcm_s16le',
                    '-ar', '48000', '-t', f'{d}', str(f)], check=True)
    inputs += ['-i', str(f)]
    fc.append(f'[{i}:v]settb=AVTB,setpts=PTS-STARTPTS[v{i}]')
    fc.append(f'[{i}:a]asetpts=PTS-STARTPTS[a{i}]')
v, au, off = 'v0', 'a0', 0.0
for i in range(1, len(SEGS)):
    off += SEGS[i - 1][2] - X
    fc.append(f'[{v}][v{i}]xfade=transition=fade:duration={X}:offset={off:.3f}[xv{i}]')
    fc.append(f'[{au}][a{i}]acrossfade=d={X}:c1=tri:c2=tri[xa{i}]')
    v, au = f'xv{i}', f'xa{i}'
subprocess.run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', ';'.join(fc), '-map', f'[{v}]', '-map', f'[{au}]',
                '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '23', '-maxrate', '5M', '-bufsize', '10M', '-pix_fmt', 'yuv420p',
                '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', a.out], check=True)
print('hazırdır:', a.out, f'~{off + SEGS[-1][2]:.1f} san')
