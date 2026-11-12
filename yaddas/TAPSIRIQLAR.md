# Tapşırıqlar və gediş (Claude-un yaddaşı)

> Claude: sessiyanın əvvəlində bunu oxu, "Növbəti addım"dan davam et.
> Hər tapşırıqdan sonra bu faylı yenilə, commit et və push et.

## Növbəti addım
- **Mövcud təqdimatın dizayn sistemi** → `design/referans/DIZAYN-SISTEMI.md`. Yeni işlər BU üslubda olmalıdır
  (açıq fon, elektrik göy, narıncı vurğu, 3D loqo/ikonlar, mono etiketlər). İstifadəçidən 41 slaydlıq faylın tamamını və 3D loqo PNG-ni istə.
- **111 real şirkət fotosu alındı** (2 internet şəkli işarələnib) → `mehsullar/fotolar/FOTOLAR.md`. JPG-lər repoda YOXDUR (repo publikdir) —
  istifadəçidən soruş: repo private edilsin, yoxsa fotolar başqa yerdə saxlanılsın? Sessiya bitsə fotolar itir!
- **Kataloq alındı və köçürüldü** → `mehsullar/katalog/KATALOQ.md`. İstifadəçidən soruşulacaq:
  1) Hansı məhsul(lar) üçün ilk video? 2) Orijinal loqo faylı (SVG/PNG).
- İstifadəçi əlavə məhsul göndərsə: `mehsullar/<ad>/info.md` şablonu + orijinal fotolar.
- **Korporativ film** (`video/caspian-promo/`): istifadəçidən gözlənilir →
  1) orijinal loqo (`assets/logo.*`), 2) 6 məhsul fotosu, 3) səsləndirmə faylı (`VOICEOVER.md`-yə görə), 4) istəyə görə musiqi.
  Gələn kimi: fayllari yerləşdir → `node scripts/render-promo.js` → yoxla → istifadəçiyə göndər.
- İstifadəçi rəyinə görə səhnələri düzəlt (zaman şkalası `preview.html`-da, sonra `build-storyboard.py`).
- Artifact preview: https://claude.ai/artifact/BoALx2DRQVNebXck7viaXa (eyni fayl yolu ilə yenilə).

## Aktiv tapşırıqlar
- [x] "Modellər" = ChatGPT-nin təklif etdiyi 7 skill → `.claude/skills/`-ə yükləndi
- [~] Korporativ film 1:54 — storyboard ✓, preview ✓, qaralama MP4 ✓ (yer tutucularla); real assetlər gözlənilir

## Bitmiş işlər
- 2026-11-12 — GitHub bağlantısı yoxlandı; yazma icazəsi istifadəçi tərəfindən verildi, push işləyir.
- 2026-11-12 — FAQ saytı (`index.html`) təkmilləşdirildi (sayt istifadəçi üçün əsas məqsəd DEYİL).
- 2026-11-12 — Blender 4.0, Inkscape 1.2, FFmpeg 6.1, Reveal.js 5.1 quraşdırıldı və yoxlandı.
  Yeni sessiyada yoxdursa: `bash scripts/setup-tools.sh`.
- 2026-11-12 — `CLAUDE.md`, qovluqlar, bu yaddaş sistemi quruldu. PR #1 açıldı.
- 2026-11-12 — PR #1 istifadəçi tərəfindən `main`-ə birləşdirildi. Yaddaş artıq yeni sessiyalarda yüklənir.

- 2026-11-12 — 7 skill yaradıldı: vision-ai-director, video-production-studio, motion-graphics-master,
  audio-voice-director, interactive-animation-developer, ai-video-tools-orchestrator, video-editor-export.

- 2026-11-12 — Korporativ film: 10 səhnəli storyboard, interaktiv preview (artifact), render skripti, qaralama MP4.
  Videoda BP adı istifadə edilmədi (üçüncü tərəf brendi) — istifadəçi təsdiq etməlidir.

- 2026-11-12 — İngiliscə məhsul kataloqu (26 s.) alındı, bütün məhsullar `KATALOQ.md`-yə köçürüldü; loqo və telefon (+994 51 206 41 45) qeyd edildi.

- 2026-11-12 — 19 real foto (komanda, Washpipe, inspeksiya, CP CPS 900-175, logistika, Baku Energy Week 2026, 7 il yubiley).

## İstifadəçi haqqında qeydlər
- Azərbaycan dilində yazır, telefondan istifadə edir. Qısa, sadə izah sevir.
- Əsas istəyi: Claude tapşırıqları **yadda saxlasın və qaldığı yerdən davam etsin**.
- Pulsuz alətlərə üstünlük verir (pullu video saytları yox).
- Əsas işi: **məhsullar haqqında video təqdimatlar** hazırlamaq.
- Seçimi bəzən Claude-a həvalə edir ("ən idealı hansıdı, onu seç").

## Qərarlar
- 2026-11-12 — İstifadəçinin öz təqdimatında 'BP ilə əməkdaşlıq' açıq yazılıb → BP adı videolarda işlədilə bilər (layihə faktı kimi).
- Yeni fəaliyyət istiqaməti: **Katalizatorlar** (təqdimatdan).
- 2026-11-12 — Brendlər (Chicago Pneumatic, ADALIT və s.) və kataloq şəkilləri videolarda işlədilə bilər — şirkət təchizatçıdır.
  Yalnız 'rəsmi diler/partnyor' iddiası yazılmır.
- Yaddaş = bu fayl + `CLAUDE.md`. Əsas branch-da (`main`) olmalıdır ki, yeni sessiyalar görsün.
