---
name: video-production-studio
description: Video ssenarisi, səhnə siyahısı, keçidlər və montaj planı hazırlayır. Tanıtım videosu, reklam, reels/shorts və ya təqdimat videosu planlaşdırılanda istifadə et.
---
# Video Production Studio

Hər video üçün `video/<ad>/plan.md` yarat:
1. **Brif**: məqsəd, auditoriya, platforma (Reels 1080×1920 / YouTube 1920×1080), müddət.
2. **Ssenari**: səs mətni (1 saniyə ≈ 2–2.5 söz).
3. **Səhnə cədvəli**: `# | müddət | kadrda nə var | mətn/yazı | səs | alət (Blender/Inkscape/HTML/AI)`.
4. **Keçidlər**: fade, slide, zoom — FFmpeg `xfade` adları ilə (fade, slideleft, circleopen...).
5. **Fayl planı**: `video/scenes/NN-ad.mp4`, `video/audio/`, son nəticə `video/output/`.
Sonra icra üçün: motion-graphics-master → audio-voice-director → video-editor-export.
Qiymət/rəqəm/iddia uydurma; şirkət məlumatı yalnız `index.html` və `CLAUDE.md`-dən.
