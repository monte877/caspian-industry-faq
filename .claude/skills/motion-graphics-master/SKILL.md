---
name: motion-graphics-master
description: Blender və Inkscape ilə 3D effektlər, hərəkətli yazılar, loqo animasiyaları və vizual keçidlər yaradır. Loqo animasiyası, 3D yazı, intro/outro və ya hərəkətli qrafika lazım olanda istifadə et.
---
# Motion Graphics Master

Alətlər yoxdursa: `bash scripts/setup-tools.sh`.

**Vektor (Inkscape):** SVG-ni əl ilə yaz → `inkscape a.svg -o a.png -w 1920`.
**3D (Blender, ekransız):** Python skripti `scripts/` qovluğunda yaz, işlət:
`blender -b -P scripts/ad.py -- <arqumentlər>`
- Mətn: `bpy.ops.object.text_add()`, `extrude`, `bevel_depth`; SVG loqo: `bpy.ops.import_curve.svg()`.
- Animasiya: `obj.keyframe_insert("rotation_euler", frame=N)`.
- Render: mühərrik `BLENDER_EEVEE` (sürətli) və ya `CYCLES` (keyfiyyət, CPU-da yavaş — samples ≤ 32).
- Çıxış: PNG ardıcıllığı `video/scenes/ad/####.png`, sonra FFmpeg ilə MP4.
- Əvvəl 1 kadr test render et və `Read` ilə bax, sonra hamısını.
**2D hərəkətli yazı (sürətli yol):** HTML/CSS animasiya → Playwright ilə kadr-kadr screenshot → FFmpeg.
Konteynerdə GPU yoxdur: qısa (3–8 san), 30 fps, 1080p-dən böyük olmayan render seç.
