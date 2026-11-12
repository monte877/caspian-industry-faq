---
name: seslendirme
description: Mətni azərbaycanca danışığa çevirir (TTS) — diktor səsi (MP3) və altyazı (SRT) yaradır. Video üçün qaralama səsləndirmə, VOICEOVER.md-ni səsə çevirmək, səs nümunəsi və ya "Claude danışsın" istənəndə istifadə et.
---

# Səsləndirmə — Claude-un "ağzı"

Mətni MP3 səsə və SRT altyazıya çevirir. Pulsuz `edge-tts` alətini işlədir. Bu alət Microsoft-un onlayn neyron səslərinə qoşulur.

## Quraşdırma (hər yeni sessiyada bir dəfə)
```bash
python3 -m pip install -q --break-system-packages edge-tts
edge-tts --list-voices | grep -i '^az-AZ'   # azərbaycanca səslər
```
Şəbəkə lazımdır, çünki Microsoft-un səs xidmətinə qoşulur. Qoşulmasa, bunu istifadəçiyə açıq de və səs uydurma.

## İstifadə
- Səslər: `az-AZ-BanuNeural` (qadın), `az-AZ-BabekNeural` (kişi). Əvvəlcə siyahı ilə yoxla.
- Mətni fayla yaz, sonra çevir:
```bash
edge-tts --voice az-AZ-BabekNeural --text "$(cat video/audio/metn.txt)" \
  --write-media video/audio/voiceover.mp3 --write-subtitles video/audio/voiceover.srt
```
- Sürət, ton və səs: `--rate=-10%`, `--pitch=-5Hz`, `--volume=+0%`. Mənfi dəyərdə `=` işarəsi yaz.
- Uzun mətni səhnələrə böl (`VOICEOVER.md`-dəki vaxtlara görə). Hər səhnəni ayrıca yarat, sonra FFmpeg ilə birləşdir.
- Hər faylı yoxla:
  - `earshot measure` ilə səviyyəni (LUFS) ölç.
  - `faster-whisper` ilə səsi geri mətnə çevir və orijinal mətnlə müqayisə et. Belə səhv tələffüz tapılır.

## Qaydalar
- Rəqəmləri və işarələri sözlə yaz ki, düzgün oxunsun. Məsələn: "1000+ ton" → "min tondan çox".
- **Bu, qaralama üçündür.** edge-tts Microsoft Edge-in "ucadan oxu" xidmətindən rəsmi olmayan yolla istifadə edir.
  Şirkətin yekun videosu üçün istifadəçiyə iki yol təklif et:
  - rəsmi Azure Speech (eyni səslər, açar lazımdır);
  - peşəkar diktor.
- Səs fayllarını `video/audio/` qovluğuna qoy. Hansı səslə və nə vaxt yaradıldığını yanında qeyd et.
