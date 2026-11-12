# Caspian Industry — layihə yaddaşı (Claude üçün)

## Layihə
- Şirkət: **Caspian Industry MMC** (Bakı, 2019). Sənaye avadanlıqlarının təchizatı, boru inspeksiyası, icarə, Washpipe xidmətləri.
- Əlaqə: info@caspianindustry.com • caspianindustry.com
- Dil: istifadəçi ilə **Azərbaycan dilində** danış. Sayt mətnləri azərbaycanca.
- Rənglər: tünd göy `#0b2444`, `#071b35` → `#12538a` qradiyent, vurğu `#1266aa`, fon `#edf3f9`.

## Qovluqlar
| Qovluq | Nə üçün |
|---|---|
| `index.html`, `sw.js`, `manifest.webmanifest`, `icon.svg` | FAQ saytı (statik, GitHub Pages) |
| `design/logo/` | Loqo və vektor dizaynı (Inkscape, SVG/PNG) |
| `design/3d/` | 3D loqo, maskot, avadanlıq modelləri (Blender, `.blend`/`.glb`) |
| `design/slides/` | Toxunma ilə idarə olunan təqdimat (Reveal.js) |
| `video/scenes/` | Blender-dən çıxan səhnələr (PNG ardıcıllığı və ya MP4) |
| `video/audio/` | Musiqi və səs (yalnız lisenziyası aydın olan fayllar) |
| `video/output/` | Hazır MP4 (FFmpeg ilə birləşdirilmiş) |
| `scripts/` | Quraşdırma və render skriptləri |

## Alətlər (pulsuz)
- **Blender** — ekransız: `blender -b -P scripts/fayl.py`
- **Inkscape** — `inkscape fayl.svg -o fayl.png`
- **FFmpeg** — səhnə + səs → MP4
- **Reveal.js** — npm paketi `reveal.js@5.1.0`
- Sessiya konteyneri müvəqqətidir: alətlər yoxdursa `bash scripts/setup-tools.sh` işlət.

## Qaydalar
- FAQ-da sual dəyişəndə: `data` massivi + JSON-LD bloku + `sw.js` `VERSION` birlikdə yenilənir.
- Qiymət, mövcudluq, müddət haqqında konkret rəqəm uydurma — "təsdiq tələb edir" yaz.
- Böyük render faylları (>50 MB) repoya commit edilmir.
- İş branch-ı: `claude/github-baglandi-42axnt`.
