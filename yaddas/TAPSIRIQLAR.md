# Tapşırıqlar və gediş (Claude-un yaddaşı)

> Claude: sessiyanın əvvəlində bunu oxu, "Növbəti addım"dan davam et.
> Hər tapşırıqdan sonra bu faylı yenilə, commit et və push et.

## Növbəti addım
- **Film v2 (2026-11-12 23:30) — real foto fonları ilə:** `preview.html`-a `setBg(səhnə, url)` əlavə edildi (Ken Burns hərəkəti + göy ton).
  `render-promo.js` fotoları `mehsullar/fotolar/film-bg-<səhnə>.jpg` və `film-product-N.jpg`-dən götürür (repoya yazılmır, hər sessiyada Drive-dan endir).
  Seçim (Drive fayl adı → səhnə): WA0047 → directions, products · WA0415 → inspection · WA0404 → rental · WA0588 → washpipe ·
  WA0553 → sectors · WA0609 → process · WA0630 → product-4 (borular). Yoxlama kadrları: `node scripts/render-promo.js --shot 52,78`.
  Drive qovluğundakı fotolar əsasən logistika/boru çatdırılmasıdır; komanda, Washpipe aləti, kompressor fotoları orada görünmədi (yalnız 13-ü baxıldı).
  **Hələ yoxdur:** səs (bu sessiyada paket yükləmək bağlı idi → edge-tts işləmədi), musiqi, EN versiya. İstifadəçi v2-yə baxıb rəy verəcək.
- **FOTOLAR GOOGLE DRIVE-DADIR (2026-11-12 23:20):** qovluq `Caspian fotolar`, ID `1K4xn1pxikaPxtFEKLAO03C8ajrpUnfB9`, 100+ JPG (WhatsApp adları `IMG-…-WA….jpg`).
  Siyahı: `mcp__Google_Drive__search_files` (`parentId = '<ID>'`); fayl: `mcp__Google_Drive__download_file_content` (şəkli göstərir və diskə yazır).
  İstifadəçidən fotoları bir daha İSTƏMƏ. Repo publik qalır, fotolar repoya yazılmır.
  **Higgsfield sınağı açılmadı → film Higgsfield-siz qurulur:** real fotolar (kinematik hərəkət) + hərəkətli qrafika + qaralama səs.
  Növbəti iş: ən yaxşı 15–20 fotonu seç (`mehsullar/fotolar/FOTOLAR.md` təsvirləri ilə tutuşdur) → `preview.html`-a qoş → render → istifadəçiyə göstər.
- **Higgsfield vəziyyəti (2026-11-12 22:55):** connector qoşulub və alətlər işləyir (`mcp__Higgsfield__*`), AMMA hesab
  **free plandadır, 0 kredit, limitsiz sınaq aktiv deyil** → hələ heç bir kadr yaradılmayıb. Alət yalnız ödənişli planlar təklif etdi.
  İstifadəçi sınağı higgsfield.ai/mcp-də eyni hesabla başlatmalıdır. Sessiya əvvəlində `balance` və
  `models_explore(action:list, type:video, unlim:true)` ilə yoxla; aktivdirsə 2, 5, 7-ci səhnələri `generate_video_batch` ilə yarat
  (`use_unlim: true`, 16:9). İstifadəçi razılıq vermədən kredit/pul xərcləmə.
- **Film brifi (istifadəçi 2026-11-12 22:45-də təsdiqlədi) — BUNA GÖRƏ İŞLƏ:**
  - Yalnız **korporativ film** (16:9, ~1:54). Reels yox.
  - Səs: **pulsuz qaralama** (`seslendirme` skill-i, edge-tts: AZ — Babek/Banu; EN — siyahıdan sakit kişi səsi). ElevenLabs hələlik yox.
  - Dil: **azərbaycanca + ingiliscə** (iki ayrı MP4). EN mətn: `video/caspian-promo/VOICEOVER-EN.md`; EN altyazı və ekran yazıları da lazımdır.
  - **AI fonlarla başla** (Higgsfield, `ai-prompts.md`); real məhsul fotoları sonra əlavə olunacaq (istifadəçi yenidən göndərməlidir).
  - Gözlənti: "nəfəs kəsici, baxanın ağzı açıq qalsın" — kinematik kadrlar, güclü musiqi, dəqiq sinxron.
  - İlk addım: Higgsfield qoşulubmu yoxla → 2, 5, 7-ci səhnələrin sınaq kadrları → istifadəçiyə göstər.
- **3 günlük "möhtəşəm video" planı** (istifadəçi 2026-11-12 22:24-də istədi; Higgsfield 72 saatlıq sınaq, ElevenLabs səs):
  1. **1-ci gün:** istifadəçi Higgsfield sınağını başladıb Claude-a qoşur (`video/caspian-promo/ai-prompts.md`).
     Claude `seslendirme` ilə AZ və EN qaralama səsi yaradır (ElevenLabs — yalnız istifadəçi sonra istəsə). Claude 2, 5, 7-ci səhnələr üçün sınaq kadrları yaradır.
  2. **2-ci gün:** qalan AI fonları (hər səhnəyə 2 variant), ən yaxşısını seçmək.
     Səs: `python3 scripts/build-voiceover.py` → `video/audio/voiceover.wav`.
  3. **3-cü gün:** fonları `preview.html`-a qoşmaq → `node scripts/render-promo.js` → `earshot critique` → yekun MP4.
     Ödəniş istəmirsə, istifadəçiyə **Higgsfield sınağını ləğv etməyi** xatırlat.
  - Sınağın başlama vaxtını soruş və ləğv üçün xatırlatma təklif et. Auto-renew: Higgsfield Ultra.
  - Kampaniya **Claude Fable 5.2** çıxışı ilə bağlıdır: bələdçilər yeni söhbətdə Fable 5.2 seçməyi deyir
    (Claude planında olmalıdır). Pulsuz olan Higgsfield sınağıdır, Claude-un özü yox.
- **Mövcud təqdimatın dizayn sistemi** → `design/referans/DIZAYN-SISTEMI.md`. Yeni işlər BU üslubda olmalıdır
  (açıq fon, elektrik göy, narıncı vurğu, 3D loqo/ikonlar, mono etiketlər). İstifadəçidən 41 slaydlıq faylın tamamını istə.
- ✅ Rəsmi loqo alındı → `design/logo/` (şəffaf PNG), korporativ filmə qoşuldu (`video/caspian-promo/assets/logo.png`).
- **111 real şirkət fotosu alındı** (2 internet şəkli işarələnib) → `mehsullar/fotolar/FOTOLAR.md`. JPG-lər repoda YOXDUR (repo publikdir) —
  istifadəçidən soruş: repo private edilsin, yoxsa fotolar başqa yerdə saxlanılsın? Sessiya bitsə fotolar itir!
- **Kataloq alındı və köçürüldü** → `mehsullar/katalog/KATALOQ.md`. İstifadəçidən soruşulacaq:
  1) Hansı məhsul(lar) üçün ilk video? (loqo alındı ✓)
- İstifadəçi əlavə məhsul göndərsə: `mehsullar/<ad>/info.md` şablonu + orijinal fotolar.
- **Korporativ film** (`video/caspian-promo/`): istifadəçidən gözlənilir →
  1) orijinal loqo (`assets/logo.*`), 2) 6 məhsul fotosu, 3) səsləndirmə faylı (`VOICEOVER.md`-yə görə), 4) istəyə görə musiqi.
  Gələn kimi: fayllari yerləşdir → `node scripts/render-promo.js` → yoxla (səsi `earshot critique` ilə) → istifadəçiyə göndər.
  Səsləndirmə faylı gəlməsə: `seslendirme` skill-i ilə qaralama səs yarat (Babek və ya Banu), istifadəçiyə göndər, təsdiq al.
- İstifadəçi rəyinə görə səhnələri düzəlt (zaman şkalası `preview.html`-da, sonra `build-storyboard.py`).
- Artifact preview: https://claude.ai/artifact/BoALx2DRQVNebXck7viaXa (eyni fayl yolu ilə yenilə).

## Aktiv tapşırıqlar
- [x] "Modellər" = ChatGPT-nin təklif etdiyi 7 skill → `.claude/skills/`-ə yükləndi
- [~] Korporativ film 1:54 — storyboard ✓, preview ✓, qaralama MP4 ✓ (yer tutucularla); real assetlər gözlənilir
- [ ] AZ interaktiv kataloq PDF-i (62 s.) — düzəlişlər: `mehsullar/katalog/AZ-KATALOQ-DUZELISLER.md` (istifadəçi dizaynerə ötürə bilər)

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

- 2026-11-12 — AZ interaktiv kataloq PDF-i (62 s., istifadəçinin göndərdiyi) yoxlanıldı: keçidlər düzgündür (62-ci s. "Geri" istisna),
  ~25 hərf/məntiq səhvi tapıldı → `mehsullar/katalog/AZ-KATALOQ-DUZELISLER.md`.

- 2026-11-12 — **earshot v0.4.1** (səs təhlili, MIT) iş sahəsinə əlavə edildi: skill `.claude/skills/earshot`,
  quraşdırma `scripts/setup-tools.sh`-da, `CLAUDE.md` alətlər siyahısında. Modellər ilk istifadədə ~1,1 GB yüklənir.

- 2026-11-12 — Instagram-da göstərilən 5 skill reposu yoxlanıldı (karpathy-skills, superpowers, mattpocock/skills,
  everything-claude-code, ui-ux-pro-max). 18 faydalı skill `.claude/skills/`-ə əlavə edildi (hamısı MIT, `LICENSE` ilə).
  Mənbələr, commit-lər və əlavə edilməyənlər: `yaddas/SKILL-KATALOQ.md`.

- 2026-11-12 — Claude-a "hisslər" əlavə edildi (istifadəçi: "gözün, qulağın, ağzın, əlin, ayağın olsun"):
  göz — watch, qulaq — faster-whisper (+ earshot), ağız — seslendirme (öz skill, edge-tts),
  əl — webapp-testing və canvas-design. Cəmi 31 skill. Paketlər ilk istifadədə quraşdırılır (şəbəkə lazımdır).

- 2026-11-12 — Film üçün səs və AI kadr hazırlığı:
  - `video/caspian-promo/ELEVENLABS.md`: 10 sətirlik ElevenLabs mətni, model, lisenziya və tələffüz qeydləri.
  - `scripts/build-voiceover.py`: sətirləri vaxtlara yerləşdirir (sınaq səslərlə yoxlanıldı: 48 kHz mono, 112.5 san).
  - `ai-prompts.md`: 10 səhnə üçün prompt və Higgsfield qoşulma addımları.
  - ElevenLabs connector-u istifadəçiyə təklif edildi. Higgsfield və Sora üçün kataloqda connector yoxdur;
    Higgsfield xüsusi connector kimi qoşulur (`https://mcp.higgsfield.ai/mcp`).

## İstifadəçi haqqında qeydlər
- Azərbaycan dilində yazır, telefondan istifadə edir. Qısa, sadə izah sevir.
- Əsas istəyi: Claude tapşırıqları **yadda saxlasın və qaldığı yerdən davam etsin**.
- Pulsuz alətlərə üstünlük verir (pullu video saytları yox).
- Əsas işi: **məhsullar haqqında video təqdimatlar** hazırlamaq.
- Seçimi bəzən Claude-a həvalə edir ("ən idealı hansıdı, onu seç").
- **"Claude işçi stolu" = bu GitHub repo.** "Bunu da əlavə et" deyəndə alət/skill buraya əlavə olunur
  (`.claude/skills/`, `scripts/setup-tools.sh`, `CLAUDE.md`), istifadəçinin öz kompüterinə yox.
- Instagram/Reels-də gördüyü alət və skill repolarını göndərir ki, Claude "daha çox özəllik" qazansın.
- AI video (Higgsfield, Sora) və AI səs (ElevenLabs) ilə "möhtəşəm video" etmək istəyir; pulsuz sınaqları sevir.

## Qərarlar
- 2026-11-12 — İstifadəçinin öz təqdimatında 'BP ilə əməkdaşlıq' açıq yazılıb → BP adı videolarda işlədilə bilər (layihə faktı kimi).
- Yeni fəaliyyət istiqaməti: **Katalizatorlar** (təqdimatdan).
- 2026-11-12 — Brendlər (Chicago Pneumatic, ADALIT və s.) və kataloq şəkilləri videolarda işlədilə bilər — şirkət təchizatçıdır.
  Yalnız 'rəsmi diler/partnyor' iddiası yazılmır.
- Yaddaş = bu fayl + `CLAUDE.md`. Əsas branch-da (`main`) olmalıdır ki, yeni sessiyalar görsün.
- 2026-11-12 — Xarici skill-lər **seçilərək** əlavə olunur: lisenziya və təhlükəsizlik yoxlanır, hook-lar əlavə edilmir,
  yüzlərlə skill kütləvi gətirilmir (Claude-u yavaşladır). Səbəblər və sonra əlavə ediləcəklər: `yaddas/SKILL-KATALOQ.md`.
- 2026-11-12 — Pulsuz plan və lisenziya qaydası:
  - ElevenLabs-in pulsuz planı kommersiya lisenziyası vermir. Şirkət filminin yekun səsi üçün ödənişli plan, edge-tts qaralaması və ya diktor lazımdır.
  - Higgsfield sınağı 72 saatdan sonra avtomatik ödənişli Ultra planına keçir, ləğv xatırlatması vacibdir.
  - AI kadrlar yalnız fon üçündür; məhsullar real fotolarla, loqo/yazı montajda üstə qoyulur.
