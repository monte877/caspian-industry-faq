# Tapşırıqlar və gediş (Claude-un yaddaşı)

> Claude: sessiyanın əvvəlində bunu oxu, "Növbəti addım"dan davam et.
> Hər tapşırıqdan sonra bu faylı yenilə, commit et və push et.

## Növbəti addım
- Ekran şəklində 7-ci skill-in adı kəsik idi; 8-ci və sonrakı skill-lər varsa, istifadəçidən soruş.
- Sonra: Caspian Industry üçün dizayn/animasiya/video işinə başla (Blender, Inkscape, FFmpeg, Reveal.js).

## Aktiv tapşırıqlar
- [x] "Modellər" = ChatGPT-nin təklif etdiyi 7 skill → `.claude/skills/`-ə yükləndi
- [ ] Dizayn / animasiya / video (pulsuz alətlərlə)

## Bitmiş işlər
- 2026-11-12 — GitHub bağlantısı yoxlandı; yazma icazəsi istifadəçi tərəfindən verildi, push işləyir.
- 2026-11-12 — FAQ saytı (`index.html`) təkmilləşdirildi (sayt istifadəçi üçün əsas məqsəd DEYİL).
- 2026-11-12 — Blender 4.0, Inkscape 1.2, FFmpeg 6.1, Reveal.js 5.1 quraşdırıldı və yoxlandı.
  Yeni sessiyada yoxdursa: `bash scripts/setup-tools.sh`.
- 2026-11-12 — `CLAUDE.md`, qovluqlar, bu yaddaş sistemi quruldu. PR #1 açıldı.
- 2026-11-12 — PR #1 istifadəçi tərəfindən `main`-ə birləşdirildi. Yaddaş artıq yeni sessiyalarda yüklənir.

- 2026-11-12 — 7 skill yaradıldı: vision-ai-director, video-production-studio, motion-graphics-master,
  audio-voice-director, interactive-animation-developer, ai-video-tools-orchestrator, video-editor-export.

## İstifadəçi haqqında qeydlər
- Azərbaycan dilində yazır, telefondan istifadə edir. Qısa, sadə izah sevir.
- Əsas istəyi: Claude tapşırıqları **yadda saxlasın və qaldığı yerdən davam etsin**.
- Pulsuz alətlərə üstünlük verir (pullu video saytları yox).
- Seçimi bəzən Claude-a həvalə edir ("ən idealı hansıdı, onu seç").

## Qərarlar
- Yaddaş = bu fayl + `CLAUDE.md`. Əsas branch-da (`main`) olmalıdır ki, yeni sessiyalar görsün.
