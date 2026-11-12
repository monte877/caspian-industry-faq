# Skill kataloqu — haradan gəldi, nə əlavə edildi

Hamısı açıq lisenziyalıdır (MIT və ya Apache-2.0), hər skill qovluğunda `LICENSE` var. Əlavə edilmə tarixi: 2026-11-12.
Fayllar aşağıdakı commit-lərdən götürülüb. Yeniləmək üçün eyni addımları yeni commit-lə təkrarla.

| Repo | Commit | Əlavə edilən skill-lər |
|---|---|---|
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | `2c60614` | karpathy-guidelines |
| [obra/superpowers](https://github.com/obra/superpowers) | `22f0b46` | writing-plans, executing-plans, systematic-debugging, verification-before-completion |
| [mattpocock/skills](https://github.com/mattpocock/skills) | `5863806` | research, grill-me + grilling (`/grill-me` grilling-i çağırır), prototype, writing-for-agents |
| [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | `d2ef268` | frontend-slides, brand-voice, content-engine, marketing-campaign, seo, market-research |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `6ae86f6` | ui-ux-pro-max, banner-design |
| [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) | `v0.4.1` | earshot |
| [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | `03ceb42` | watch (göz) |
| [ThePlasmak/faster-whisper](https://github.com/ThePlasmak/faster-whisper) | `1c8d6a6` | faster-whisper (qulaq) |
| [anthropics/skills](https://github.com/anthropics/skills) (Apache-2.0) | `2c5958e` | webapp-testing, canvas-design (əl) |
| öz skill-imiz | — | seslendirme (ağız; [edge-tts](https://github.com/rany2/edge-tts) alətini işlədir) |

## Niyə hamısı yox
- **Çox skill Claude-u yavaşladır.** everything-claude-code-da 314 skill və 300-dən çox agent var. Hamısının adı və təsviri hər sessiyada yüklənir və diqqəti dağıdır.
- **Hook-lar əlavə edilmədi** (superpowers, everything-claude-code). Onlar avtomatik əmr işlədir və Claude-un davranışını yoxlanmadan dəyişir.
- **superpowers `brainstorming` və `using-superpowers` əlavə edilmədi.** Hər işdən əvvəl uzun sual-cavab tələb edir, istifadəçi isə qısa iş sevir.
- **everything-claude-code yaddaş sistemi** (`unified-memory`, `continuous-learning-v2`) hook və xarici "vault" tələb edir. Bizim yaddaş `yaddas/TAPSIRIQLAR.md`-dir.
- **`social-publisher`, `deep-research`** xarici xidmət və ya API açarı tələb edir.
- **`video-editing`** mövcud `video-editor-export` skill-i ilə üst-üstə düşür.
- **mattpocock `handoff`** faylı müvəqqəti qovluğa (`/tmp`) yazır və sessiya bitəndə o fayl itir. Bizdə bu işi `yaddas/TAPSIRIQLAR.md` görür.
- **calesthio/openmontage** AGPL-3.0 lisenziyalıdır. Bu lisenziya kopyalanan fayllara güclü şərtlər qoyur.
- **claude-video-nun SessionStart hook-u** gətirilmədi, yalnız `watch` skill-i götürüldü.
- **WhisperX** təxminən 3 GB disk və 8 GB RAM istəyir. `faster-whisper` ondan yüngüldür.
- **Azərbaycanca hazır TTS skill-i tapılmadı.** Ona görə `seslendirme` skill-ini özümüz yazdıq.

## Lazım olsa sonra əlavə et
- everything-claude-code: `remotion-video-creation` (React ilə video), `video-editing`, `motion-patterns`,
  `customs-trade-compliance`, `logistics-exception-management`, `strategic-compact`, `security-review`.
- superpowers: `test-driven-development`, `requesting-code-review`, `subagent-driven-development`, `brainstorming`.
- mattpocock: `diagnosing-bugs`, `tdd`, `code-review`, `retro`, `to-questionnaire`.
- ui-ux-pro-max: `slides`, `design-system`, `brand`.
- anthropics/skills: `frontend-design`, `skill-creator`, `slack-gif-creator`, `theme-factory`.

**Necə əlavə etmək olar:**
1. `git clone --depth 1 <repo>` ilə reponu endir.
2. Skill qovluğunu `.claude/skills/`-ə köçür.
3. Repo-nun `LICENSE`-ını həmin qovluğa qoy.
4. Bu cədvəli yenilə.

Hook və ya skript varsa, əvvəlcə oxu.

## Qeyd
superpowers skill-lərində `superpowers:<ad>` eyni adlı yerli skill deməkdir.
Burada olmayanları (məsələn `test-driven-development`) ötür.
