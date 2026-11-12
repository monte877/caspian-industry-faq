# Claude üçün əsas qayda — YADDAŞ

**Hər sessiyanın əvvəlində:** aşağıdakı tapşırıq faylını oxu və "Növbəti addım"dan davam et.
İstifadəçiyə qısaca de: "Qaldığımız yer: ...".

**Hər tapşırıqdan sonra:** `yaddas/TAPSIRIQLAR.md` faylını yenilə (bitən işi "Bitmiş işlər"ə köçür,
yeni "Növbəti addım" yaz, istifadəçi haqqında yeni öyrəndiyini qeyd et), sonra commit və push et.
Yazılmayan şey növbəti sessiyada unudulur.

@yaddas/TAPSIRIQLAR.md

---

# Caspian Industry — layihə məlumatı

## Layihə
- Şirkət: **Caspian Industry MMC** (Bakı, 2019). Sənaye avadanlıqlarının təchizatı, boru inspeksiyası, icarə, Washpipe xidmətləri.
- Əlaqə: info@caspianindustry.com • caspianindustry.com • WhatsApp +994 51 206 41 45
- Kataloq və bütün məhsullar: `mehsullar/katalog/KATALOQ.md` (5 bölmə A–E). Məhsul videosundan əvvəl onu oxu.
- Dil: istifadəçi ilə **Azərbaycan dilində** danış. Sayt mətnləri azərbaycanca.
- Sayt rəngləri: `#0b2444`, `#12538a`, `#1266aa`.
- **Loqo faylları (rəsmi, istifadəçi göndərib):** `design/logo/caspian-loqo-yazili.png`, `caspian-loqo-isare.png` (şəffaf fon, 3× böyüdülmüş),
  `caspian-icon-512/192.png`; orijinallar `design/logo/orijinal/`. Rənglər: navy `#011c3d`, orta göy `#025da5`, açıq göy `#51a4eb`.
- **Vizual üslub:** `design/referans/DIZAYN-SISTEMI.md` (şirkətin mövcud təqdimatı) — bütün yeni işlər buna uyğun.

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
- **earshot** (v0.4.1) — Claude üçün "qulaq": hazır videonun səsini yoxlayır (səs–kadr sinxronu, LUFS, diktor/musiqi balansı),
  kodla yaradılmış səs effektləri verir (`earshot sfx`, `earshot kit`). Əsas əmr: `earshot critique video/output/caspian-promo.mp4`.
  Skill: `.claude/skills/earshot`.
- Sessiya konteyneri müvəqqətidir: alətlər yoxdursa `bash scripts/setup-tools.sh` işlət.

## Qaydalar
- FAQ-da sual dəyişəndə: `data` massivi + JSON-LD bloku + `sw.js` `VERSION` birlikdə yenilənir.
- Qiymət, mövcudluq, müddət haqqında konkret rəqəm uydurma — "təsdiq tələb edir" yaz.
- Böyük render faylları (>50 MB) repoya commit edilmir.
- Yaddaş faylları `main`-də olmalıdır: işdən sonra PR aç və istifadəçidən birləşdirməyi istə.
