#!/usr/bin/env bash
# Blender, Inkscape, FFmpeg, Reveal.js və earshot quraşdırır (artıq varsa ötür).
set -e
need=()
for t in blender inkscape ffmpeg; do command -v "$t" >/dev/null || need+=("$t"); done
if [ ${#need[@]} -gt 0 ]; then
  apt-get update -qq
  DEBIAN_FRONTEND=noninteractive apt-get install -y -qq --no-install-recommends "${need[@]}"
fi
# earshot: Claude üçün "qulaq" (səs təhlili, yalnız CPU). Modellər (~1,1 GB) ilk istifadədə yüklənir.
# Quraşdırılmasa, digər alətlərə mane olmur.
if ! command -v earshot >/dev/null; then
  { python3 -m pip install -q --break-system-packages torch --index-url https://download.pytorch.org/whl/cpu &&
    python3 -m pip install -q --break-system-packages "earshot @ git+https://github.com/Leonxlnx/earshot@v0.4.1"; } ||
    echo "XƏBƏRDARLIQ: earshot quraşdırılmadı (şəbəkə və ya pip problemi)" >&2
fi
cd "$(dirname "$0")/../design/slides"
[ -d node_modules/reveal.js ] || { [ -f package.json ] || npm init -y >/dev/null; npm i -s reveal.js@5.1.0; }
blender -b --version | head -1; inkscape --version 2>/dev/null; ffmpeg -version | head -1
command -v earshot >/dev/null && echo "earshot $(python3 -m pip show earshot 2>/dev/null | sed -n 's/^Version: //p')" || true
