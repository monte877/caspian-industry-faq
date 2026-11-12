---
name: audio-voice-director
description: Səs fayllarını analiz edir, səsləndirmə, musiqi və sinxronizasiyanı planlaşdırır və FFmpeg ilə emal edir. Videoya musiqi/səs əlavə etmək, səs səviyyəsini düzəltmək, səsi kadrlara sinxronlaşdırmaq lazım olanda istifadə et.
---
# Audio & Voice Director

- Analiz: `ffprobe -hide_banner səs.mp3`; səs səviyyəsi: `ffmpeg -i s.mp3 -af loudnorm=print_format=summary -f null -`.
- Normallaşdırma (sosial media): `-af loudnorm=I=-14:TP=-1.5:LRA=11`.
- Musiqini səsin altında azaltmaq (ducking): `sidechaincompress` filtri.
- Fade: `afade=t=in:d=1,afade=t=out:st=<son-2>:d=2`.
- Sinxron: səhnə cədvəlindəki vaxtlara görə `adelay` / `atrim`.
**Səsləndirmə:** bu konteynerdə Azərbaycan dilində keyfiyyətli TTS yoxdur. İstifadəçi öz səsini yazıb
`video/audio/`-ya yükləsin, və ya xarici TTS üçün mətn/vaxt cədvəli hazırla.
**Musiqi:** yalnız lisenziyası aydın olan (öz faylı, CC0, royalty-free) — mənbəni `video/audio/MƏNBƏLƏR.md`-yə yaz.
