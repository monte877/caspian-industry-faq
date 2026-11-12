# AI video promptları — Higgsfield (və ya Kling, Runway)

Film pulsuz qurulub, bütün kadrlar `preview.html`-dan render olunur. AI kadrları yalnız **fon** üçündür.
- **Loqo, yazı, məhsul fotoları və insan üzlərini AI-a verməyin.** AI bunları pozur. Onlar montajda üstə qoyulur.
- Şirkətin öz məhsulları yalnız real fotolarla göstərilir. AI kadrı real məhsul kimi təqdim edilmir.
- BP, SOCAR və başqa şirkətlərin loqolarını və adlarını promptlara yazmayın.

## Higgsfield-i Claude-a qoşmaq
1. higgsfield.ai/mcp səhifəsində 72 saatlıq sınağı başladın və Higgsfield hesabınıza daxil olun.
2. Claude-da **Ayarlar → Connectors** bölməsinə keçin və xüsusi connector əlavə edin:
   - ad: `Higgsfield`
   - URL: `https://mcp.higgsfield.ai/mcp`
3. **Connect** basın, Higgsfield hesabı ilə daxil olun və icazə verin.
4. Yoxlamaq üçün Claude-a yazın: "Higgsfield modellərimi və kreditimi göstər".

**Diqqət:** ləğv etməsəniz, sınaq 72 saatdan sonra avtomatik olaraq ödənişli **Higgsfield Ultra** planına keçir
(ilk ay endirimlə). Su nişanı və kommersiya hüququ şərtlərini Higgsfield-in qaydalarında yoxlayın.
Sora-nın Claude üçün connector-u yoxdur.

## Səhnə promptları
Format: 16:9, ən yüksək keyfiyyət, 8–10 saniyəlik klip. Səhnə daha uzundursa, 2 klip yaradın.
Hər səhnəni əvvəlcə bir modeldə sınayın. Bəyənmədiyinizi başqa modeldə təkrarlayın (Veo 3.1, Kling, Seedance).

| # | Səhnə | Vaxt | Prompt (EN) |
|---|---|---|---|
| 1 | Loqo girişi (fon) | 0:00–0:08 | Macro shot of glowing orange sparks rising slowly through deep darkness, a thin horizontal line of blue light in the center, shallow depth of field, slow push-in, cinematic, photorealistic, no text, no logos |
| 2 | Bakı, 2019 | 0:08–0:18 | Cinematic dusk over the Caspian Sea, calm dark-blue waves, distant offshore oil platform silhouette on the horizon, slow lateral dolly right, cool steel-blue color grade, volumetric haze, photorealistic, no text, no logos |
| 4 | Məhsul təchizatı | 0:30–0:46 | Clean modern industrial warehouse, rows of industrial compressors, pumps and steel pipes on racks, slow push-in, soft blue rim light, shallow depth of field, photorealistic, no text, no people's faces |
| 5 | Boru inspeksiyası | 0:46–1:00 | Close-up of a large steel pipe on an inspection bench, ultrasonic probe moving along the surface, blue scanning light, slow tracking shot, macro detail of weld seam, photorealistic, no text |
| 6 | Avadanlıq icarəsi | 1:00–1:12 | Organized industrial equipment yard at golden hour, rows of mobile diesel generators and air compressors on trailers, slow aerial dolly forward, clean and orderly, photorealistic, no text, no logos, no people's faces |
| 7 | Washpipe | 1:12–1:24 | Polished steel washpipe with threaded connection rotating slowly on its axis, dark studio background, sparks drifting, dramatic blue key light, slow orbit, photorealistic, no text |
| 8a | Sahələr — neft emalı | 1:24–1:28 | Oil refinery at night, towers and pipelines glowing with warm lights, slow aerial pull-back, photorealistic, no text, no logos |
| 8b | Sahələr — sement | 1:28–1:32 | Cement plant silos at sunrise, light dust in the air, slow crane-up shot, photorealistic, no text, no logos |
| 8c | Sahələr — metal | 1:32–1:36 | Steel mill interior, molten metal pouring with bright sparks, slow dolly, dramatic contrast, photorealistic, no text, no faces |
| 9 | İş prosesi | 1:36–1:46 | Flatbed truck carrying steel pipes on a coastal highway at dawn, aerial tracking shot, calm sea in the background, photorealistic, no text, no logos |

**Neqativ prompt:** blurry, warped metal, melted shapes, text, watermark, logo, distorted hands, extra objects

**İş axını:**
1. Claude Higgsfield ilə yaradır (və ya siz Higgsfield-də yaradırsınız).
2. MP4-ü yükləyin və `video/scenes/<səhnə>.mp4` qovluğuna qoyun (və ya söhbətə göndərin).
3. Claude-a "AI fonlarını əlavə et" yazın.
