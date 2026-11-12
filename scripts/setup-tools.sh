#!/usr/bin/env bash
# Blender, Inkscape, FFmpeg və Reveal.js quraşdırır (artıq varsa ötür).
set -e
need=()
for t in blender inkscape ffmpeg; do command -v "$t" >/dev/null || need+=("$t"); done
if [ ${#need[@]} -gt 0 ]; then
  apt-get update -qq
  DEBIAN_FRONTEND=noninteractive apt-get install -y -qq --no-install-recommends "${need[@]}"
fi
cd "$(dirname "$0")/../design/slides"
[ -d node_modules/reveal.js ] || { [ -f package.json ] || npm init -y >/dev/null; npm i -s reveal.js@5.1.0; }
blender -b --version | head -1; inkscape --version 2>/dev/null; ffmpeg -version | head -1
