---
name: video-editor-export
description: FFmpeg ilə video birləşdirmə, səs əlavə etmə, keçidlər, yazı, ölçü dəyişmə və son ixrac (MP4). Səhnələri bir videoya yığmaq, Reels/YouTube üçün ixrac etmək lazım olanda istifadə et.
---
# Professional Video Editor & Export

- PNG → MP4: `ffmpeg -framerate 30 -i dir/%04d.png -c:v libx264 -pix_fmt yuv420p -crf 18 s.mp4`
- Keçidlə birləşdirmə: `-filter_complex "[0][1]xfade=transition=fade:duration=0.5:offset=<1-ci müddət-0.5>"`
- Sadə birləşdirmə: `list.txt` (`file 'a.mp4'`) → `ffmpeg -f concat -safe 0 -i list.txt -c copy out.mp4`
- Səs əlavə: `-i video.mp4 -i səs.m4a -map 0:v -map 1:a -c:v copy -c:a aac -shortest`
- Loqo üstə: `overlay=W-w-40:40`; yazı üçün loqonu/mətni Inkscape ilə PNG et (drawtext-də Azərbaycan hərfləri üçün şrift yoxla).
- İxrac profilləri:
  - Reels/TikTok: 1080×1920, 30fps, `-crf 20 -preset slow -movflags +faststart`
  - YouTube: 1920×1080, `-crf 18`
- Yoxla: `ffprobe` (müddət, ölçü, səs), 3 kadr çıxarıb `Read` ilə bax.
- Nəticəni `video/output/`-a yaz və istifadəçiyə `SendUserFile` ilə göndər. Böyük MP4-ləri commit etmə.
