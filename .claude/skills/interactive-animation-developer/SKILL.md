---
name: interactive-animation-developer
description: HTML, CSS, JavaScript və SVG ilə işlək animasiyalı, toxunma ilə idarə olunan təqdimatlar (Reveal.js) və interaktiv səhifələr hazırlayır. Təqdimat, slayd, interaktiv kataloq və ya animasiyalı veb səhifə istənəndə istifadə et.
---
# Interactive Animation Developer

- Təqdimat: `design/slides/<ad>/index.html`, Reveal.js `design/slides/node_modules/reveal.js` (və ya CDN `https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/`).
- Animasiya: Reveal `data-auto-animate`, `fragment`; CSS `@keyframes`; SVG `stroke-dashoffset` ilə loqo çəkilişi.
- Telefon üçün: toxunma ilə sürüşdürmə (Reveal-də var), `viewport` meta, 16px kənar boşluq, `prefers-reduced-motion`.
- Brend rəngləri `CLAUDE.md`-də.
- Yoxlama: Playwright ilə 390×844 ekranda screenshot çək, `Read` ilə bax, konsol xətalarını yoxla.
- Videoya çevirmək: Playwright `recordVideo` və ya kadr-kadr screenshot → FFmpeg.
