---
name: vision-ai-director
description: Şəkilləri, loqoları və video kadrlarını analiz edir, dizayn və kompozisiyanı müəyyənləşdirir. İstifadəçi şəkil/loqo/kadr göndərib rəy, dizayn istiqaməti, rəng palitrası və ya kompozisiya istəyəndə istifadə et.
---
# Vision AI Director

1. Şəkli `Read` ilə aç (videodan kadr: `ffmpeg -ss 00:00:03 -i v.mp4 -frames:v 1 kadr.png`).
2. Analiz et: kompozisiya (üçdə bir qaydası, fokus nöqtəsi), rənglər (HEX), şrift, kontrast, brend uyğunluğu.
3. Palitranı çıxar: `ffmpeg -i şəkil.png -vf "palettegen=max_colors=6" palitra.png` və nəticəni bax.
4. Nəticəni bu formada ver: **Güclü tərəflər • Problemlər (vaciblik sırası ilə) • Konkret təklif** (ölçü, rəng, yerləşmə).
5. Brend: tünd göy `#0b2444`, `#12538a`, vurğu `#1266aa` (bax `CLAUDE.md`).
Qısa, Azərbaycan dilində yaz. Görmədiyin şey haqqında fikir uydurma.
