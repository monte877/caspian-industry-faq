# AI video promptları (istəyə görə)

Film hazırda tam **pulsuz** qurulub: bütün kadrlar `preview.html`-dan render olunur.
Real görüntülü fon istəsəniz, aşağıdakı səhnələri Runway / Kling / Higgsfield-də yaradıb
`video/scenes/` qovluğuna qoyun, mən onları fon kimi montaja əlavə edərəm.
**Loqo, yazı və məhsul fotolarını AI-a verməyin** — AI onları pozur; onlar sonradan üstə qoyulur.

| Səhnə | Vaxt | Nisbət / müddət | Prompt (EN) |
|---|---|---|---|
| Bakı, 2019 | 0:08–0:18 | 16:9 · 10 san | Cinematic dusk over the Caspian Sea, calm dark-blue waves, distant offshore oil platform silhouette on the horizon, slow lateral dolly right, cool steel-blue color grade, volumetric haze, photorealistic, no text, no logos |
| Məhsul təchizatı | 0:30–0:46 | 16:9 · 10 san | Clean modern industrial warehouse, rows of industrial compressors, pumps and steel pipes on racks, slow push-in, soft blue rim light, shallow depth of field, photorealistic, no text, no people's faces |
| Boru inspeksiyası | 0:46–1:00 | 16:9 · 10 san | Close-up of a large steel pipe on an inspection bench, ultrasonic probe moving along the surface, blue scanning light, slow tracking shot, macro detail of weld seam, photorealistic, no text |
| Washpipe | 1:12–1:24 | 16:9 · 10 san | Polished steel washpipe with threaded connection rotating slowly on its axis, dark studio background, sparks drifting, dramatic blue key light, slow orbit, photorealistic, no text |

**Neqativ prompt:** blurry, warped metal, melted shapes, text, watermark, logo, distorted hands, extra objects

**İş axını:** yarat → 10 san MP4 yüklə → `video/scenes/<səhnə>.mp4` → Claude-a "AI fonlarını əlavə et" yaz.
