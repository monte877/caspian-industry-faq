#!/usr/bin/env python3
"""preview.html içindəki zaman şkalasından storyboard.md, altyazı (.srt) və səsyazma ssenarisini yaradır.
Zamanı/mətni dəyişmək üçün yalnız preview.html-dakı <script id="timeline"> blokunu redaktə et, sonra bunu işlət."""
import json, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
d = root / 'video/caspian-promo'
tl = json.loads(re.search(r'<script type="application/json" id="timeline">(.*?)</script>', (d/'preview.html').read_text('utf-8'), re.S).group(1))
ts = lambda x: f"{int(x//3600):02}:{int(x%3600//60):02}:{int(x%60):02},{int(round(x%1*1000)):03}"
mm = lambda x: f"{int(x//60)}:{x%60:04.1f}"
S = tl['scenes']

srt = '\n'.join(f"{i}\n{ts(s['vo'][0])} --> {ts(s['vo'][1])}\n{s['vo'][2]}\n" for i, s in enumerate(S, 1))
(d/'voiceover.srt').write_text(srt, 'utf-8')

vo = ["# Səsyazma ssenarisi — Caspian Industry", "",
      "Hər sətri göstərilən müddətə sığdırın (sakit korporativ temp: azərbaycanca təxminən 1.2–1.8 söz/saniyə). Bütöv faylı 0:00-dan başlayaraq,",
      "sətirlər arasında fasilə ilə yazın: hər sətir öz başlanğıc vaxtında başlamalıdır.",
      "Fayl: `video/audio/voiceover.wav` (48 kHz, mono və ya stereo). Sonra: `node scripts/render-promo.js`.", ""]
for s in S:
    a, b, t = s['vo']; w = len(t.split())
    vo.append(f"**{mm(a)} – {mm(b)}** ({b-a:.1f} san · {w} söz · {w/(b-a):.1f} söz/san) — _{s['title']}_  \n{t}\n")
(d/'VOICEOVER.md').write_text('\n'.join(vo), 'utf-8')

L = [f"# Storyboard — Caspian Industry korporativ filmi", "",
     f"**Format:** {tl['width']}×{tl['height']} · 16:9 · {tl['fps']} FPS · {mm(tl['duration'])} ({len(S)} səhnə)  ",
     "**Mənbə:** `preview.html` (bu fayl ondan avtomatik yaradılıb: `python3 scripts/build-storyboard.py`)", "",
     "| # | Vaxt | Səhnə | Vizual | Kamera | Keçid | Səs / musiqi |", "|---|---|---|---|---|---|---|"]
for i, s in enumerate(S, 1):
    L.append(f"| {i} | {mm(s['start'])}–{mm(s['end'])} | **{s['title']}** | {s['visual']} | {s['camera']} | {s['transition']} | {s['audio']} |")
L += ["", "## Səsləndirmə (sinxron)", ""]
for i, s in enumerate(S, 1):
    L.append(f"{i}. `{mm(s['vo'][0])}–{mm(s['vo'][1])}` {s['vo'][2]}")
L += ["", "## Brend qaydaları", "",
      "- Loqo və məhsul fotoları yalnız bərabər miqyasla (`object-fit: contain`) yerləşdirilir: dartılma, kəsilmə, rəng dəyişikliyi yoxdur.",
      "- Rənglər: `#0b2444`, `#12538a`, `#1266aa` (+ işıq `#6cb8ff`, qığılcım `#f0a92b` yalnız effektlərdə).",
      "- Şirkət haqqında bütün iddialar `index.html` FAQ bazasından götürülüb; qiymət, müddət, sertifikat iddiası yoxdur.",
      "", "## Təsdiq tələb edən məqamlar", "",
      "- Washpipe: FAQ-da 'BP layihəsi üzrə' qeyd olunub; videoda BP adı **istifadə edilməyib** (üçüncü tərəf brendi, icazə lazımdır).",
      "- NDT metodları (UT/PT/MT/VT) FAQ-da 'mümkünlüyü dəqiqləşdirilir' kimi verilib; ekranda bu qeyd var.",
      "- Operatorla icarə: 'imkanı' kimi təqdim olunur, zəmanət kimi yox.", ""]
(d/'storyboard.md').write_text('\n'.join(L), 'utf-8')
print('storyboard.md, voiceover.srt, VOICEOVER.md yaradıldı')
