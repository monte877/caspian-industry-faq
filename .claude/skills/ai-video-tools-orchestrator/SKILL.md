---
name: ai-video-tools-orchestrator
description: Runway, Kling, Higgsfield və digər AI video alətləri üçün promptlar və iş axını hazırlayır. İstifadəçi AI ilə video kadr yaratmaq istəyəndə istifadə et.
---
# AI Video Tools Orchestrator

Bu alətlər xarici və (çox vaxt) pulludur; Claude onlara buradan daxil ola bilmir.
Claude-un işi: **hazır promptlar + addım-addım iş axını** hazırlamaq, istifadəçi nəticəni `video/scenes/`-ə yükləyir,
sonra Claude montaj edir (video-editor-export).

Hər səhnə üçün `video/<ad>/ai-promptlar.md`:
- **Prompt (ingiliscə)**: obyekt + hərəkət + kamera (dolly in, orbit, crane) + işıq + üslub + "no text".
- **Neqativ**: blurry, distorted logo, extra limbs, text artifacts.
- **Ayarlar**: nisbət (9:16 / 16:9), müddət (5/10 san), başlanğıc kadr (image-to-video üçün şəkil).
- **Alət seçimi**: real hərəkətli səhnə → Kling/Runway; kamera effektləri → Higgsfield.
Loqo və yazılar AI-da pozulur — onları AI-a vermə, sonradan FFmpeg/Blender ilə üstə qoy.
Pulsuz alternativ əvvəlcə təklif et: Blender ilə eyni səhnə.
