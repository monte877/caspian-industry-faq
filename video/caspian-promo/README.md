# Caspian Industry — korporativ film (1:54, Full HD, 30 FPS)

| Fayl | Nədir |
|---|---|
| `preview.html` | İnteraktiv preview **və** render mənbəyi (zaman şkalası `<script id="timeline">`-dadır) |
| `storyboard.md` | 10 səhnəlik storyboard (avtomatik yaradılır) |
| `VOICEOVER.md` | Diktor üçün vaxtlı səsyazma ssenarisi |
| `voiceover.srt` | Altyazı faylı (YouTube / montaj proqramları üçün) |
| `ai-prompts.md` | İstəyə görə AI fon görüntüləri üçün promptlar |
| `assets/` | **Orijinal** loqo və məhsul fotoları buraya |

## Assetləri qoşmaq
- `assets/logo.svg` (və ya `.png`, şəffaf fon) — giriş və finalda.
- `assets/product-1.png` … `product-6.png` — sıra: kompressor, generator, nasos, borular, klapan, elektrik.
- `../audio/voiceover.wav` — `VOICEOVER.md`-yə görə yazılmış səs (0:00-dan başlayan tək fayl).
- `../audio/music.mp3` — lisenziyalı fon musiqisi (səs olan yerlərdə avtomatik azalır).

Şəkillər yalnız bərabər miqyasla yerləşdirilir — heç vaxt dartılmır və ya kəsilmir.

## Render
```bash
bash scripts/setup-tools.sh                       # alətlər yoxdursa
python3 scripts/build-storyboard.py               # zaman şkalası dəyişibsə
node scripts/render-promo.js                      # → video/output/caspian-promo.mp4
node scripts/render-promo.js --from 30 --to 46    # yalnız bir səhnə (test)
node scripts/render-promo.js --no-subs            # altyazısız versiya
```
Çıxış: H.264, yuv420p, CRF 18, 1920×1080, 30 FPS, `+faststart`; səs varsa AAC 192k, −14 LUFS.
