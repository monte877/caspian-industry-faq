// Caspian Industry filmini kadr-kadr render edir və FFmpeg ilə MP4-ə yığır.
// İstifadə: node scripts/render-promo.js [--from 0] [--to 114] [--out video/output/caspian-promo.mp4] [--no-subs]
// Assetlər (varsa avtomatik qoşulur):
//   video/caspian-promo/assets/logo.(png|svg|webp)            — orijinal loqo
//   video/caspian-promo/assets/product-1..6.(png|jpg|webp)    — məhsul fotoları
//   video/audio/voiceover.(wav|mp3|m4a)                        — səsləndirmə
//   video/audio/music.(wav|mp3|m4a)                            — fon musiqisi (səsin altında azaldılır)
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs'), path = require('path'), os = require('os');
const ROOT = path.resolve(__dirname, '..');
const arg = (n, d) => { const i = process.argv.indexOf('--' + n); return i > -1 ? process.argv[i + 1] : d; };
const SRC = path.join(ROOT, 'video/caspian-promo/preview.html');
const OUT = path.resolve(ROOT, arg('out', 'video/output/caspian-promo.mp4'));
const find = (dir, base, exts) => exts.map(e => path.join(ROOT, dir, base + '.' + e)).find(f => fs.existsSync(f));
const mime = f => ({ png: 'image/png', jpg: 'image/jpeg', jpeg: 'image/jpeg', webp: 'image/webp', svg: 'image/svg+xml' })[path.extname(f).slice(1).toLowerCase()];
const dataUri = f => `data:${mime(f)};base64,${fs.readFileSync(f).toString('base64')}`;

(async () => {
  const html = fs.readFileSync(SRC, 'utf8');
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'promo-'));
  const page = path.join(tmp, 'index.html');
  fs.writeFileSync(page, '<!doctype html><html lang="az"><head><meta charset="utf-8"></head><body>' + html + '</body></html>');
  const tl = JSON.parse(html.match(/<script type="application\/json" id="timeline">([\s\S]*?)<\/script>/)[1]);
  const fps = tl.fps, from = +arg('from', 0), to = Math.min(+arg('to', tl.duration), tl.duration);
  const frames = Math.round((to - from) * fps);

  const browser = await chromium.launch();
  const p = await browser.newPage({ viewport: { width: tl.width, height: tl.height } });
  const errors = []; p.on('pageerror', e => errors.push(e.message));
  await p.goto('file://' + page + '?render');
  await p.evaluate(() => document.fonts.ready);
  if (process.argv.includes('--no-subs')) await p.evaluate(() => { document.getElementById('opt-subs').checked = false; document.getElementById('opt-subs').dispatchEvent(new Event('change')); });
  const logo = find('video/caspian-promo/assets', 'logo', ['svg', 'png', 'webp']);
  if (logo) { await p.evaluate(u => window.setLogo(u), dataUri(logo)); console.log('Loqo:', path.relative(ROOT, logo)); }
  for (let i = 1; i <= 6; i++) { const f = find('video/caspian-promo/assets', 'product-' + i, ['png', 'jpg', 'jpeg', 'webp']); if (f) { await p.evaluate(([n, u]) => window.setProduct(n, u), [i - 1, dataUri(f)]); console.log('Məhsul', i, path.relative(ROOT, f)); } }
  await p.waitForTimeout(300);

  const vo = find('video/audio', 'voiceover', ['wav', 'mp3', 'm4a']);
  const music = find('video/audio', 'music', ['wav', 'mp3', 'm4a']);
  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  const a = ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-'];
  let filter = null, maps = ['-map', '0:v'];
  if (vo) { a.push('-ss', String(from), '-i', vo); }
  if (music) { a.push('-ss', String(from), '-i', music); }
  if (vo && music) { filter = '[2:a]volume=0.35[m];[m][1:a]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=400[duck];[duck][1:a]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5[a]'; maps.push('-map', '[a]'); }
  else if (vo) { filter = '[1:a]loudnorm=I=-14:TP=-1.5[a]'; maps.push('-map', '[a]'); }
  else if (music) { filter = `[1:a]afade=t=out:st=${Math.max(0, to - from - 2)}:d=2,loudnorm=I=-14:TP=-1.5[a]`; maps.push('-map', '[a]'); }
  if (filter) a.push('-filter_complex', filter);
  a.push(...maps, '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', String(fps), '-movflags', '+faststart');
  if (vo || music) a.push('-c:a', 'aac', '-b:a', '192k');
  a.push('-t', String(to - from), OUT);
  const ff = spawn('ffmpeg', a, { stdio: ['pipe', 'inherit', 'inherit'] });
  const done = new Promise((res, rej) => ff.on('close', c => c === 0 ? res() : rej(new Error('ffmpeg ' + c))));

  const t0 = Date.now();
  for (let f = 0; f < frames; f++) {
    await p.evaluate(t => window.seek(t), from + f / fps);
    const buf = await p.screenshot({ type: 'jpeg', quality: 94 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (f % 150 === 0) console.log(`kadr ${f}/${frames} · ${((Date.now() - t0) / 1000).toFixed(0)} san`);
  }
  ff.stdin.end(); await done; await browser.close();
  console.log(`Hazır: ${path.relative(ROOT, OUT)} · ${frames} kadr · səs: ${vo ? 'var' : 'yox'} · musiqi: ${music ? 'var' : 'yox'}`);
  if (errors.length) console.log('Səhifə xətaları:', errors);
})().catch(e => { console.error(e); process.exit(1); });
