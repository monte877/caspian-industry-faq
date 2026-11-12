# Məhsul bazası (Claude-un məhsul yaddaşı)

Hər məhsul üçün ayrıca qovluq: `mehsullar/<mehsul-adi>/`
- `info.md` — aşağıdakı şablon üzrə məlumat (yalnız istifadəçinin verdiyi faktlar)
- `foto-1.png`, `foto-2.jpg` … — orijinal şəkillər (dəyişdirilmədən saxlanır)
- `video/` — bu məhsul üçün hazırlanan təqdimatlar

## info.md şablonu
```
# <Məhsulun adı>
- Kateqoriya:
- Brend / model:
- Əsas texniki göstəricilər: (güc, təzyiq, ölçü, material, standart...)
- Tətbiq sahələri:
- Üstünlükləri (müştəriyə nə verir):
- Hədəf auditoriya:
- Videoda vurğulanmalı 3 əsas fikir:
- Mənbə: (istifadəçi, kataloq, sayt — tarix ilə)
- Təsdiq olunmamış / yoxlanmalı məqamlar:
```
Claude: məlumat uydurma; boş qalan sahəni "verilməyib" yaz və istifadəçidən soruş.
