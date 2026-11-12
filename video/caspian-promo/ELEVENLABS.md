# ElevenLabs ilə səsləndirmə — korporativ film

## Əvvəlcə bilin
- **Model:** ElevenLabs-in dil siyahısına görə azərbaycancanı **Eleven v3** dəstəkləyir. Multilingual v2 və Flash v2.5 dəstəkləmir.
  Yeni model çıxıbsa, onun dil siyahısında azərbaycanca olub-olmadığını yoxlayın.
- **Lisenziya:** pulsuz planda yaradılan səs şirkət videosunda istifadə edilə **bilməz**, çünki pulsuz planda kommersiya lisenziyası yoxdur.
  Yekun səs üçün ödənişli plan lazımdır, bütün ödənişli planlarda kommersiya lisenziyası var. Pulsuz planla yalnız səs seçmək və sınamaq olar.
- **Səs seçimi:** kitabxanadan 2–3 sakit, inamlı səsi 01-ci sətirlə sınayın. Azərbaycancanı ən təbii deyəni seçin.
  Bütün sətirləri **eyni səslə** yaradın.
- **Hər sətri ayrıca yaradın** (10 fayl). Adları belə olsun: `01.mp3` … `10.mp3`.
- Claude-da ElevenLabs connector qoşulubsa, Claude sətirləri özü yarada bilər.

## Mətn — ElevenLabs-ə köçürün
| Fayl | Yer | ElevenLabs mətni |
|---|---|---|
| 01 | 5.7 san | Caspian Industry. Sənaye üçün etibarlı təchizat və texniki xidmət. |
| 02 | 8.6 san | İki min on doqquzuncu ildə Bakıda təsis edilən şirkətimiz sənaye müəssisələrinə məhsul, avadanlıq və xidmət həlləri təqdim edir. |
| 03 | 10.6 san | Dörd əsas istiqamətdə işləyirik: məhsul təchizatı, boru inspeksiyası, avadanlıq icarəsi və Washpipe xidmətləri. |
| 04 | 14.6 san | Mexaniki, enerji, elektrik və laboratoriya avadanlıqlarından borulara və metal məhsullarına qədər, texniki tələblərinizə uyğun təchizat həyata keçiririk. |
| 05 | 12.6 san | Boru inspeksiyasında borunun vəziyyəti, ölçüləri və mümkün qüsurlar tələb olunan NDT metodları ilə yoxlanılır. |
| 06 | 10.6 san | Sənaye avadanlıqlarının icarəsi: günlük və ya aylıq, operatorla icarə imkanı ilə. Şərtlər avadanlığa görə dəqiqləşdirilir. |
| 07 | 10.6 san | Washpipe istiqamətində boruların kirayəsi və texniki xidməti həyata keçirilir. Spesifikasiya tətbiqə uyğun seçilir. |
| 08 | 10.6 san | Neft-qaz, energetika, istehsalat, tikinti, sement və metal sənayesi: müxtəlif sahələrə xidmət göstəririk. |
| 09 | 8.6 san | Texniki tapşırığınızı göndərin: qiymətləndirmə, təklif və çatdırılma, hamısı bir ünvanda. |
| 10 | 4.8 san | Caspian Industry. Sənayeniz üçün etibarlı tərəfdaş. |

Mənası `VOICEOVER.md` ilə eynidir. Yalnız "2019-cu" sözlə yazılıb ki, düzgün oxunsun.
Səs yerindən bir az uzun çıxsa, problem deyil: montajda 12%-ə qədər sürətləndirilir. Daha uzundursa, sürəti artırıb yenidən yaradın.

## Tələffüz səhv çıxsa
| Söz | Bunu sınayın |
|---|---|
| Caspian Industry | Kaspian İndastri |
| Washpipe | Uoşpayp |
| NDT | en-di-ti |

## Sonra
1. 10 faylı söhbətə göndərin və ya `video/audio/vo/` qovluğuna qoyun.
2. `python3 scripts/build-voiceover.py` sətirləri vaxtlara yerləşdirir və `video/audio/voiceover.wav` faylını yaradır.
3. `node scripts/render-promo.js` filmi render edir.
4. Səsi `earshot critique video/output/caspian-promo.mp4` ilə yoxlayın: səviyyə və kadrla sinxron.
