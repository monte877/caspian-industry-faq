# Caspian Industry — Suallar və cavablar

Caspian Industry MMC üçün statik sual-cavab (FAQ) səhifəsi. Server və ya qeydiyyat tələb etmir.

## Fayllar
- `index.html` — səhifənin özü (sual-cavab bazası `const data=[...]` massivindədir)
- `sw.js` — bir dəfə açdıqdan sonra oflayn işləmə üçün keş
- `manifest.webmanifest`, `icon.svg` — telefona "proqram kimi" əlavə etmək üçün

## İmkanlar
- Kateqoriya filtri və axtarış (ə/ı/ö/ü/ş/ç/ğ fərqinə həssas deyil), nəticələrdə vurğulama
- Hər sualın paylaşıla bilən linki (`index.html#s12`)
- Mesaj forması: uyğun cavabı və oxşar sualları göstərir (canlı AI deyil)
- Google üçün FAQPage strukturu (JSON-LD)

## Yeniləmə
Sual əlavə edəndə və ya dəyişəndə həm `data` massivini, həm də `<script type="application/ld+json">` blokunu yeniləyin,
sonra `sw.js` içində `VERSION` dəyərini artırın (məs. `faq-v2`).

## Yayımlama (GitHub Pages)
Repo → **Settings → Pages** → Source: *Deploy from a branch* → branch və `/ (root)` seçin → **Save**.
