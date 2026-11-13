# Tapşırıqlar və gediş (Claude-un yaddaşı)

> Claude: sessiyanın əvvəlində bunu oxu, "Növbəti addım"dan davam et.
> Hər tapşırıqdan sonra bu faylı yenilə, commit et və push et.

## Növbəti addım
- **5:17-lik video → v4 (4:15) göndərildi (2026-11-13 22:20) — RƏY GÖZLƏNİLİR.** `video/output/caspian-teqdimat-v4.mp4` (52 MB).
  İstifadəçi recent.design skrinşotları (kitab rəfi, əyri 3D qalereya, üzən kartlar + axtarış zolağı, pazl, node-ağac, səhifə qatlanması,
  "Scout" kartı) və Soft Bridge reklam videosunu (tünd göy fon, yazılan mətn, qurulan UI pəncərələri) göndərdi: "bu dizaynları videoya əlavə et".
  - Yeni səhnələr (`scripts/trailer/`, `render_html.py --fps 25`): `books.html` (Mündəricat kitab rəfi, 18 san; orijinalda 44.6–75.6) ·
    `gallery.html` (Dörd əsas istiqamət, silindr içində dönən kartlar, 14 san; orijinalda 100.0–105.6) · `cloud.html` (müştəri loqoları
    dərinlikdə üzür + sektorları yazan axtarış zolağı, 14 san; `cust.mp4`-ün yerinə). Karusel və pazl qalır.
  - Yığma: `python3 scripts/trailer/assemble.py /mnt/user-data/uploads/1000140435.mp4` (SEGS yenilənib, çıxış v4).
  - Səs orijinaldandır, kəsilən/uzanan yerlərdə uyğun gəlmir (qalereya 14 san, orijinal 5.6 san → səs təkrarlanır).
  - Hələ istifadə edilməyən referanslar: node-ağac ("Yeddi ölkədən" üçün uyğundur), səhifə qatlanması, Scout kartı, Soft Bridge üslublu yazılan mətn.
- **YENİ BRİF: "Bir detaldan böyük nəticəyə" — 3:55, 9:16 (2026-11-13 20:41) — CARİ İŞ.** İstifadəçi 11 səhnəli hazır ssenari göndərdi
  (zaman kodları, ekran yazıları, səsləndirmə mətni; rənglər: ağ, tünd göy, mavi, gümüşü — narıncı YOX).
  - Kod: `scripts/trailer/film2.html` (1080×1920, 235 san, `window.seek`), musiqi `scripts/trailer/film2_music.py` → `video/src/music2.wav`.
  - Render: `render_html.py film2.html --w 1080 --h 1920 --fps 30 --frm 0 --to 3525 --out video/output/_f2a.mp4` və `--frm 3525 … _f2b.mp4`
    (paralel, ~20–30 dəq), sonra ffmpeg concat + music2.wav → `video/output/caspian-film-235.mp4`.
  - Səsləndirmə YOXDUR (edge-tts quraşdırılmır, ElevenLabs kredit istəyir) → mətn subtitr kimi gedir; səs faylı gəlsə səhnə vaxtlarına qoyulur.
  - Maskot istifadə edilməyib (brif icazə verir). Komanda fotosu (uşaq görünən) istifadə edilməyib; iş prosesi fotoları var.
  - **Göndərildi 21:40 (40 MB, −15 LUFS) — RƏY GÖZLƏNİLİR.** Yalnız 1-ci səhnəni yenidən render etmək: `--frm 0 --to 600`, sonra concat-da `_f2a.mp4`-ə `inpoint 20`.
- **DAYAN (2026-11-13 20:15).** İstifadəçi 66 saniyəlik filmi (v1 və v2) bəyənmədi: "bərbad, heç nə eləmə; 5 dəqiqəlik video bundan min dəfə
  yaxşı idi". **Yeni video işinə özbaşına başlama** — istifadəçi nə istədiyini desin. Kodla çəkilmiş yazı/qrafika filmi onun gözləntisini
  ödəmir: o, öz 5:17-lik videosundakı kimi kinematik kadrlar və "üstündə işlənmiş" hərəkət gözləyir. Ən yaxşı əsas onun öz videosudur.
- **Film v2 + səsli rəy (2026-11-13 18:10).** `video/output/caspian-film-v2.mp4` (66 san) render olunub, hələ GÖNDƏRİLMƏYİB — yoxla və göndər.
  İstifadəçinin səsli rəyi (film "qəşəngdir, amma çox sadə, kiçik şirkət kimi görünür"):
  - Giriş və əsas istiqamətlər: **Təchizat, Texniki xidmət, İcarə** (ən çox vurğu İcarədə). Logistika və Katalizatorlar kiçik, diqqət çəkməyən.
  - "29 müştəri" yazma — bunlar **seçilmiş** müştərilərdir (v2-də "Seçilmiş müştərilərimiz."). Şirkətin miqyasını kiçiltmə.
  - 1 dəqiqə azdır; daha geniş film istəyir (5:17-lik video, kataloq, fotolar, caspianindustry.com-dakı məlumatla).
  - **Qeyri-adi hərəkətlər** istəyir: asılqan kimi sağa-sola dönən cərgə, amma sənaye üslubunda; yuxarıdan enib fırlanan obyekt;
    kitab rəfləri kimi açılıb-bağlanan panellər. Referanslar qısa: hər iş bir sətirdə, hamısı bir səhifədə.
  - Təklif etdim (cavab gözlənilir): əvvəl "kran relsində dönən məhsul cərgəsi" 10–15 saniyəlik sınaq, bəyənsə 2–3 dəqiqəlik film.
  - v2-də edilənlər: `film.html`-də giriş sözləri, 3 əsas istiqamət + "Logistika · Katalizatorlar" kadrı, düz rəngli fonların arxasında fotolar.
- **SIFIRDAN FİLM (Claude-un öz zövqü) göndərildi (2026-11-13 14:30) — RƏY GÖZLƏNİLİR.** `video/output/caspian-film.mp4`
  (66 san, 1080p, 11 MB, −14 LUFS). İstifadəçi dedi: "özün sıfırdan hazırlasaydın necə hazırlayardın, öz zövqünlə hazırla".
  - Bir fayl: `scripts/trailer/film.html` (9 səhnə, `window.seek(t)`), musiqi `music.py`-dən (`video/src/music.wav`, 120 BPM, zərbələr 8/16/24/40/56 san).
  - Yığma: `python3 scripts/trailer/render_html.py scripts/trailer/film.html --fps 25 --out video/output/_film-sessiz.mp4` (~7 dəq),
    sonra `ffmpeg -i _film-sessiz.mp4 -i video/src/music.wav -c:v libx264 -crf 21 -c:a aac -shortest caspian-film.mp4`.
  - Quruluş: 0–8 tünd giriş (Boru. Avadanlıq. Xidmət.) · 8–16 loqo + 2019 / 40+ / 1000+ ton · 16–24 dörd istiqamət (foto + iri başlıq;
    Katalizatorlar fotosuz, narıncı fon) · 24–28 axan məhsul cərgələri · 28–31 altı sürətli məhsul kadrı · 32–40 referans layihələr (pazl + 6 sətir)
    · 40–48 29 müştəri loqosu · 48–52 7 ölkə · 52–56 "Sənayeniz üçün etibarlı tərəfdaş." · 56–66 loqo + əlaqə.
  - Üslub: iri Inter Display tipoqrafiyası, 4 düz rəng (krem, navy, göy `#12327d`, narıncı `#ff6a3d`), mono etiketlər, zərbələrdə ağ parıltı.
  - Yoxlanmayıb / istifadəçi təsdiq etməlidir: musiqini Claude eşitmir (yalnız ölçü); "40+ əməkdaş", "29 müştəri", müqavilə illəri təqdimatdan götürülüb;
    Katalizatorlar üçün foto yoxdur; diktor səsi və EN versiya yoxdur.
- **5:17-lik video → v3 (4:20) göndərildi (2026-11-13 13:30) — RƏY GÖZLƏNİLİR.** `video/output/caspian-teqdimat-v3.mp4`.
  İstifadəçi dörd təklifin hamısını təsdiqlədi və dedi: **"səsə görə dizayn etmə, möhtəşəm dizaynlar et, internetdəki ən yaxşı dizaynları referans götür."**
  - Yığma: `python3 scripts/trailer/assemble.py <orijinal.mp4>` (parçalar və kəsim nöqtələri `SEGS`-dədir, keçidlər 0.4 san).
  - Yeni səhnələr (hamısı `render_html.py --fps 25` ilə): `carousel.html` (Təchizat, 34.3 san) · `references.html` (6 layihə, foto pazl kimi
    yığılır, 46 san; orijinalda 75 san idi) · `customers.html` (29 loqo üç axan lentdə, 14 san).
  - Kəsildi: təkrarlanan Mündəricat (orijinalda 89–95, 178–184, 264–270, 284–290 san). 44–75 san-dəki ilk Mündəricat turu saxlanıldı.
  - Mənbələr repoda yoxdur: `video/src/ref/` (kataloq səhifələrindən kəsilmiş fotolar), `video/src/logo/` (orijinal videonun 275 və 282-ci
    saniyə kadrlarından kəsilmiş loqolar), `video/src/prod/`.
  - **Səs:** orijinalda diktor səsi var kimi görünür (spektroqrama görə, əmin deyiləm). Kəsilən yerlərdə səs də kəsilib; Referans bölməsi
    29 san qısaldığı üçün orada səs yarıda kəsilir. İstifadəçi səsi sonra həll edəcək / ayrıca səs faylı istənildi.
  - Qalan təkliflər: nasosun açılma animasiyası, maskot videosu (4K) ilə final, komanda fotoları (təsdiq gözlənilir), 2 təhrif olunmuş loqo
    (Neftqazkimya tresti, baec alt yazısı — orijinal videoda da belədir).
- **5:17-lik video, v2 göndərildi (2026-11-13 12:45) — RƏY GÖZLƏNİLİR.** `video/output/caspian-teqdimat-v2.mp4`:
  orijinalın 105.6–139.9 san hissəsi ("2.2 Təchizat portfeli", 5 kateqoriya) yeni karusellə əvəz edildi; qalan hər şey və **səs
  olduğu kimidir** (səs axını bayt-bayt eynidir). İstifadəçi karusel sınağına "oradan davam elə" dedi → üslub təsdiqlənib.
  - Karusel: `scripts/trailer/carousel.html` (36 məhsul, 5 kateqoriya, kateqoriya vaxtları orijinaldakı ilə eyni: 1.9/8.4/15.1/21.7/28.3 san),
    render: `python3 scripts/trailer/render_html.py --fps 25 --out video/output/karusel-34.mp4`, sonra ffmpeg `overlay` ilə
    orijinalın üstünə (0.4 san keçidlə). Orijinal: `/mnt/user-data/uploads/1000140435.mp4` (sessiya bitəndə itir — istifadəçidən yenidən istə).
  - Məhsul şəkilləri (36 PNG, şəffaf/tünd fon) `video/src/prod/`-da, repoda yoxdur. Fayl adı → məhsul adı `carousel.html`-dəki `CATS`-dadır.
  - **12:40-da gələn yeni material (hələ istifadə edilməyib):** maskot videosu (4K, 8.9 san, əl yelləyir və "əla" göstərir, küncdə "Ai" nişanı),
    2 komanda fotosu (ofis və sahə; üzlər və bir uşaq görünür — istifadədən əvvəl soruş), loqo işarəsi, nasosun yığılmış və açılmış şəkli,
    şaquli kataloq səhifələri (Mündəricat, Şirkət haqqında, Referans layihələr 1–6, Müştərilər, Əlaqə).
  - Növbəti təkliflər: Referans layihələr və Müştərilər hissələrini eyni üslubda yenilə; nasosun "açılma" animasiyası; Mündəricat təkrarlarını qısalt.
- **ƏSAS VİDEO = 5:17-lik təqdimat filmi (2026-11-13 09:00) — CARİ İŞ BUDUR.** İstifadəçi öz hazır videosunu göndərdi
  (`1000140435.mp4`, 1920×1080, 25 fps, 317 san: dəniz/loqo girişi → Mündəricat → 5 bölmə → "Təşəkkür edirik" maskotu; krem fon,
  göy bölmə kartları, narıncı nöqtə, mono etiketlər). İstəyi: **onu vizual olaraq daha "super" etmək; səsə toxunma, yalnız görüntü.**
  - Referanslar (recent.design və TikTok skrinşotları): dərinlikdə axan kartlar + ön planda bulanıqlıq (Deimos "Design Zeitgeist"),
    asılqanda sürüşən məhsul cərgəsi (wearebrand.io), toxunula bilən 3D düymələr, pazl kimi yığılan şəkil.
  - İstifadəçi 7 təmiz məhsul şəkli verdi (şəffaf fonlu PNG): mobil/vintli/porşenli kompressor (Chicago Pneumatic), paslanmayan boru,
    mikroskop, sürgülü klapan, avtomat açar → `video/src/prod/` (repoda yoxdur).
  - **Sınaq səhnəsi göndərildi:** `video/output/karusel-sinaq.mp4` (11 san, səssiz) — `scripts/trailer/carousel.html` +
    `render_html.py` (Playwright ilə kadr-kadr). **Rəy gözlənilir.** Bəyənsə: bu üslubda səhnələri 5:17-lik videoya yerləşdir.
  - **Məhdudiyyət:** videonun mənbə layihəsi məndə yoxdur, yalnız MP4 var → mövcud səhnələrin içini dəyişə bilmirəm, yalnız
    səhnə əvəz edə/əlavə edə və kəsə bilirəm. İstifadəçidən mənbəni soruşdum (hansı proqram/kim hazırlayıb).
  - Treyler v3 (aşağıda) haqqında rəy gəlmədi; istifadəçi diqqəti bu videoya keçirdi.
- **TREYLER v3 (2026-11-13) — CARİ İŞ BUDUR.** İstifadəçi film v2-ni bəyənmədi ("tünd və boğuq, yavaş, səssiz, təqdimat kimidir") və
  **real videolardan sürətli treyler** seçdi; musiqini Claude kodla yaratdı. Nəticə: `video/output/caspian-treyler-az.mp4`
  (66 san, 1080p, 31 MB, −14 LUFS), istifadəçiyə göndərildi, **rəyi gözlənilir**. EN versiya hələ render edilməyib (`--lang en` hazırdır).
  - Kod: `scripts/trailer/timeline.py` (kadrlar, yazılar AZ/EN, zərbə anları, 120 BPM), `music.py` (musiqi, numpy/scipy),
    `render.py` (montaj: PIL + ffmpeg; `--shots 3,9,17` yoxlama kadrları verir).
  - Mənbələr repoda YOXDUR: `video/src/vid/WAxxxx.mp4` (18 video) və `video/src/img/WAxxxx.jpg` (13 foto) — Drive qovluğundan
    `download_file_content` ilə endir, fayl adındakı `WA` nömrəsi ilə adlandır. 10 MB-dan böyük 3 video (WA0699, 0703, 0704) endirilmir.
  - Yenidən yığmaq: `python3 scripts/trailer/music.py && python3 scripts/trailer/render.py --lang az`, sonra crf 24 ilə sıx.
  - Üslub: parlaq rəng, iri ağ yazı + narıncı nöqtə, kino zolaqları, zərbələrdə ağ parıltı, final açıq fonda loqo.
  - Köhnə `preview.html` filmi (v2) saxlanılır, amma istifadəçi onu bəyənmədi — ona qayıtma.
  - Yeni connector-lar göründü (ElevenLabs creative, Canva, Adobe). ElevenLabs səsi kredit xərcləyir — yalnız istifadəçi istəsə.
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
