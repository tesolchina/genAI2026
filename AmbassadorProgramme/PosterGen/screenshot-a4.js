const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function main() {
  const dir = __dirname;
  const htmlPath = path.join(dir, 'poster_A4.html');
  const outPng = path.join(dir, 'poster_A4.png');

  if (!fs.existsSync(htmlPath)) {
    console.error('poster_A4.html not found');
    process.exit(1);
  }

  console.log('Launching browser...');
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  // A4 at 96 DPI = 794 x 1123 px; scale 3x for high-res = 2382 x 3369
  const scale = 3;
  await page.setViewport({
    width: 794,
    height: 1123,
    deviceScaleFactor: scale,
  });

  console.log('Loading poster_A4.html...');
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0', timeout: 30000 });

  // Wait a moment for fonts/images to load
  await new Promise(r => setTimeout(r, 2000));

  console.log('Taking screenshot...');
  const poster = await page.$('.poster');
  if (poster) {
    await poster.screenshot({ path: outPng, type: 'png' });
  } else {
    await page.screenshot({ path: outPng, type: 'png', fullPage: true });
  }

  await browser.close();

  const stats = fs.statSync(outPng);
  const sizeMB = (stats.size / (1024 * 1024)).toFixed(1);
  console.log(`Saved: ${outPng} (${sizeMB} MB)`);
  console.log(`Resolution: ${794 * scale} x ${1123 * scale} px (${scale}x A4 at 96 DPI)`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
