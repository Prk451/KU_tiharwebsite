import shutil
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace Section 4 CSS in <style>
old_css_s4 = '''    /* 7. SECTION 4: WISH LANTERN WALL, MADAL STUDIO & POSTCARD GENERATOR */
    .finale-studio {
      position: relative;
      min-height: 100svh;
      padding: clamp(72px, 10vh, 110px) clamp(20px, 5vw, 72px) 90px;
      background:
        radial-gradient(ellipse at 50% 10%, rgba(255, 168, 38, 0.16) 0%, transparent 55%),
        radial-gradient(ellipse at 85% 85%, rgba(192, 102, 255, 0.12) 0%, transparent 50%),
        #07080d;
      border-top: 1px solid rgba(255, 184, 28, 0.35);
      overflow: hidden;
      isolation: isolate;
    }
    .wish-sky-layer {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 1;
      overflow: hidden;
    }
    .wish-lantern-float {
      position: absolute;
      bottom: -80px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      animation: wish-rise 18s linear forwards;
    }
    .wish-lantern-body {
      width: 34px;
      height: 46px;
      border-radius: 10px 10px 5px 5px;
      background: radial-gradient(circle at 50% 72%, #fff8d6 0%, #ffb84d 48%, #d84315 92%);
      box-shadow: 0 0 28px rgba(255, 184, 28, 0.75);
    }
    .wish-lantern-tag {
      padding: 3px 9px;
      border-radius: 99px;
      background: rgba(8, 9, 14, 0.78);
      border: 1px solid rgba(255, 212, 122, 0.45);
      color: #ffe8ad;
      font-family: "Space Mono", monospace;
      font-size: 9px;
      letter-spacing: 0.1em;
      white-space: nowrap;
    }
    @keyframes wish-rise {
      0% { transform: translate3d(0, 0, 0) scale(0.8); opacity: 0; }
      10% { opacity: 1; }
      90% { opacity: 0.95; }
      100% { transform: translate3d(var(--wdrift, 40px), -115vh, 0) scale(0.65); opacity: 0; }
    }

    .finale-inner {
      position: relative;
      z-index: 5;
      max-width: 1220px;
      margin: 0 auto;
    }
    .finale-header {
      text-align: center;
      margin-bottom: 48px;
    }
    .finale-kicker {
      font-family: "Space Mono", monospace;
      font-size: 10px;
      letter-spacing: 0.26em;
      text-transform: uppercase;
      color: var(--c-gold);
    }
    .finale-title {
      margin: 12px 0 10px;
      font-family: "Instrument Serif", Georgia, serif;
      font-size: clamp(38px, 5.4vw, 72px);
      font-weight: 400;
      line-height: 0.98;
      color: var(--c-cream);
    }
    .finale-title em { color: var(--c-gold); font-style: italic; }
    .finale-sub {
      max-width: 580px;
      margin: 0 auto;
      color: #b8bdd0;
      font-size: 14px;
      line-height: 1.7;
    }

    .finale-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 22px;
    }
    @media (max-width: 980px) {
      .finale-grid { grid-template-columns: 1fr; }
    }
    .studio-card {
      background: rgba(14, 17, 26, 0.82);
      border: 1px solid rgba(255, 184, 28, 0.25);
      border-top: 2px solid var(--c-gold);
      border-radius: 10px;
      padding: 24px;
      backdrop-filter: blur(12px);
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .studio-card-tag {
      font-family: "Space Mono", monospace;
      font-size: 9.5px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--c-gold);
    }
    .studio-card h3 {
      margin: 0;
      font-family: "Instrument Serif", serif;
      font-size: 28px;
      font-weight: 400;
      color: #fff;
    }
    .studio-card p {
      margin: 0;
      font-size: 13px;
      line-height: 1.6;
      color: #c6cbdc;
    }
    .studio-input {
      width: 100%;
      padding: 11px 14px;
      border-radius: 6px;
      border: 1px solid rgba(255, 255, 255, 0.16);
      background: rgba(6, 8, 14, 0.85);
      color: #fff;
      font: inherit;
      font-size: 13px;
    }
    .studio-input:focus {
      outline: none;
      border-color: var(--c-gold);
      box-shadow: 0 0 0 3px rgba(255, 184, 28, 0.16);
    }
    .studio-btn {
      padding: 11px 16px;
      border-radius: 6px;
      border: 1px solid var(--c-gold);
      background: linear-gradient(135deg, rgba(230, 81, 0, 0.35), rgba(255, 184, 28, 0.22));
      color: #ffe9b3;
      font-family: "Space Mono", monospace;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .studio-btn:hover {
      background: var(--c-gold);
      color: #08090c;
      transform: translateY(-1px);
    }
    .madal-pad-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-top: 4px;
    }
    .madal-pad {
      padding: 18px 10px;
      border-radius: 8px;
      border: 1px solid rgba(255, 184, 28, 0.35);
      background: rgba(255, 184, 28, 0.08);
      color: #FAF5EC;
      font-family: "Space Mono", monospace;
      font-size: 10px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      cursor: pointer;
      transition: transform 0.1s ease, background 0.15s ease, box-shadow 0.15s ease;
    }
    .madal-pad:active, .madal-pad.hit {
      transform: scale(0.95);
      background: rgba(255, 184, 28, 0.35);
      box-shadow: 0 0 24px rgba(255, 184, 28, 0.55);
    }
    #postcardPreview {
      width: 100%;
      aspect-ratio: 16 / 10;
      border-radius: 6px;
      border: 1px solid rgba(255, 184, 28, 0.4);
      background: #090b12;
      display: block;
    }'''

new_css_s4 = '''    /* ═══════════════════════════════════════════════════════════════════
       THE ETERNAL COVENANT — CLOSING DEDICATION
    ═══════════════════════════════════════════════════════════════════ */
    .tihar-closing-finale {
      position: relative;
      width: 100%;
      min-height: 52vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(180deg, var(--c-obsidian) 0%, #06070a 100%);
      border-top: 1px solid rgba(255, 184, 28, 0.28);
      padding: clamp(64px, 10vh, 120px) clamp(24px, 6vw, 72px);
      text-align: center;
      overflow: hidden;
      isolation: isolate;
    }
    .closing-glow {
      position: absolute;
      top: 30%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: min(720px, 92vw);
      height: 340px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(255, 184, 28, 0.16) 0%, rgba(230, 81, 0, 0.06) 52%, transparent 72%);
      filter: blur(48px);
      pointer-events: none;
      z-index: 1;
    }
    .closing-inner {
      position: relative;
      z-index: 2;
      max-width: 920px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 18px;
    }
    .closing-emblem {
      margin-bottom: 2px;
      filter: drop-shadow(0 0 20px rgba(255, 184, 28, 0.5));
      animation: flame-flicker 2.4s ease-in-out infinite alternate;
    }
    .closing-kicker {
      font-family: "Space Mono", monospace;
      font-size: 11px;
      letter-spacing: 0.28em;
      text-transform: uppercase;
      color: var(--c-gold);
    }
    .closing-statement {
      margin: 0;
      font-family: "Instrument Serif", "Cormorant Garamond", Georgia, serif;
      font-size: clamp(32px, 4.2vw, 56px);
      font-weight: 400;
      line-height: 1.25;
      letter-spacing: -0.01em;
      color: var(--c-cream);
      text-shadow: 0 4px 30px rgba(0, 0, 0, 0.9), 0 0 50px rgba(255, 184, 28, 0.25);
    }
    .closing-statement em {
      font-style: italic;
      color: var(--c-gold);
    }
    .closing-deva-sub {
      margin: 0;
      font-family: "Noto Serif Devanagari", "Cormorant Garamond", Georgia, serif;
      font-size: clamp(15px, 1.3vw, 19px);
      font-style: italic;
      color: rgba(250, 245, 236, 0.72);
      letter-spacing: 0.04em;
    }
    .closing-saptarangi-rule {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 7px;
      margin: 10px 0 4px;
    }
    .closing-saptarangi-rule span {
      width: 22px;
      height: 2.5px;
      border-radius: 99px;
    }
    .closing-saptarangi-rule span:nth-child(1) { background: #C62828; }
    .closing-saptarangi-rule span:nth-child(2) { background: #E65100; }
    .closing-saptarangi-rule span:nth-child(3) { background: #FFB81C; }
    .closing-saptarangi-rule span:nth-child(4) { background: #FAF5EC; }
    .closing-saptarangi-rule span:nth-child(5) { background: #2E7D32; }
    .closing-saptarangi-rule span:nth-child(6) { background: #1565C0; }
    .closing-saptarangi-rule span:nth-child(7) { background: #9C27B0; }

    .closing-colophon {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 20px;
      flex-wrap: wrap;
      margin-top: 8px;
      font-family: "Space Mono", monospace;
      font-size: 10px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: rgba(250, 245, 236, 0.55);
    }
    .closing-back-to-top {
      background: rgba(255, 184, 28, 0.12);
      border: 1px solid rgba(255, 184, 28, 0.42);
      color: var(--c-gold);
      font-family: "Space Mono", monospace;
      font-size: 9.5px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      padding: 7px 16px;
      border-radius: 99px;
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .closing-back-to-top:hover {
      background: rgba(255, 184, 28, 0.28);
      border-color: var(--c-gold);
      color: #fff;
      transform: translateY(-2px);
      box-shadow: 0 0 20px rgba(255, 184, 28, 0.35);
    }'''

assert old_css_s4 in html, "Could not find old_css_s4 in index.html"
html = html.replace(old_css_s4, new_css_s4, 1)
print("1. Replaced Section 4 CSS with closing dedication CSS.")

# 2. Replace Section 4 HTML
old_html_s4 = re.search(r'<!-- ═════+\s*4\. INTERACTIVE TIHAR STUDIO.*?</section>', html, re.DOTALL)
assert old_html_s4, "Could not find Section 4 HTML block"

new_html_s4 = '''<!-- ══════════════════════════════════════════════════════════════════
       4. THE ETERNAL COVENANT — CLOSING DEDICATION
  ══════════════════════════════════════════════════════════════════ -->
  <footer class="tihar-closing-finale" id="tihar-finale" aria-label="Closing Dedication">
    <div class="closing-glow" aria-hidden="true"></div>
    <div class="closing-inner">
      <div class="closing-emblem" aria-hidden="true">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ffd47a" stroke-width="1.3">
          <path d="M12 2.5c2.8 3.2 4.2 5.7 3 8.2-.7 1.4-2 2.1-3 2.1s-2.3-.7-3-2.1C7.8 8.2 9.2 5.7 12 2.5Z" fill="rgba(255,184,28,0.3)"/>
          <path d="M3.5 14.5c2.2 3.6 5 5.2 8.5 5.2s6.3-1.6 8.5-5.2c-2.8 1.2-5.6 1.8-8.5 1.8s-5.7-.6-8.5-1.8Z"/>
        </svg>
      </div>
      <div class="closing-kicker">✦ THE ETERNAL COVENANT · यमपञ्चक ✦</div>
      <h2 class="closing-statement">
        Every year, we celebrate Tihar for the defeat of death by the bond of brother and sister.
      </h2>
      <p class="closing-deva-sub">
        मृत्युमाथि प्रेमको विजय — दिदी-भाइको पवित्र बन्धन
      </p>
      <div class="closing-saptarangi-rule" aria-hidden="true">
        <span></span><span></span><span></span><span></span><span></span><span></span><span></span>
      </div>
      <div class="closing-colophon">
        <span>शुभ तिहार ✦ KATHMANDU VALLEY</span>
        <button type="button" class="closing-back-to-top" id="closingBackToTopBtn">RETURN TO TOP ↑</button>
      </div>
    </div>
  </footer>'''

html = html[:old_html_s4.start()] + new_html_s4 + html[old_html_s4.end():]
print("2. Replaced Section 4 HTML with closing dedication footer.")

# 3. Add back-to-top script
old_script_snippet = '''      const fiveDaysToTopBtn = document.getElementById('fiveDaysToTopBtn');
      if (fiveDaysToTopBtn) {
        fiveDaysToTopBtn.addEventListener('click', () => {
          window.scrollTo({ top: 0, behavior: 'smooth' });
          window.setTimeout(() => {
            if (typeof celebrating !== 'undefined' && !celebrating && typeof lightUp === 'function') {
              lightUp();
            }
          }, 650);
        });
      }'''

new_script_snippet = '''      const fiveDaysToTopBtn = document.getElementById('fiveDaysToTopBtn');
      if (fiveDaysToTopBtn) {
        fiveDaysToTopBtn.addEventListener('click', () => {
          window.scrollTo({ top: 0, behavior: 'smooth' });
          window.setTimeout(() => {
            if (typeof celebrating !== 'undefined' && !celebrating && typeof lightUp === 'function') {
              lightUp();
            }
          }, 650);
        });
      }

      const closingTopBtn = document.getElementById('closingBackToTopBtn');
      if (closingTopBtn) {
        closingTopBtn.addEventListener('click', () => {
          window.scrollTo({ top: 0, behavior: 'smooth' });
        });
      }'''

assert old_script_snippet in html, "Could not find fiveDaysToTopBtn script snippet"
html = html.replace(old_script_snippet, new_script_snippet, 1)
print("3. Attached back-to-top script for closing section.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

shutil.copyfile('index.html', 'index_3.html')
print("4. Successfully synchronized index.html and index_3.html!")
