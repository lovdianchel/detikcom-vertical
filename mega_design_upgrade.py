"""
MEGA DESIGN UPGRADE – All 7 improvements:
1. Gradient accent (blue-purple)
2. Frosted glass panel behind card info
3. Video progress bar
4. Breaking News & Quote more dramatic  
5. Floating pill bottom nav
6. Vertical scroll indicator
7. Colored category badges
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================
# 1. Replace CSS block (</style> marker) – inject new CSS rules
# ============================================================

NEW_CSS = """
        /* ========== UPGRADE 1: GRADIENT ACCENT SYSTEM ========== */
        :root {
            --detik-blue: #0066CC;
            --detik-purple: #7B3FF1;
            --detik-red: #E8192C;
            --detik-green: #00C853;
            --detik-orange: #FF6D00;
            --detik-gold: #FFB300;
            --grad-accent: linear-gradient(135deg, #0066CC 0%, #7B3FF1 100%);
            --grad-warm: linear-gradient(135deg, #E8192C 0%, #FF6D00 100%);
            --grad-blue-glow: rgba(0,102,204,0.3);
        }

        /* ========== UPGRADE 2: GLASSMORPHISM CARD INFO PANEL ========== */
        .card-info-panel {
            background: rgba(0,0,0,0.45);
            backdrop-filter: blur(20px) saturate(1.5);
            -webkit-backdrop-filter: blur(20px) saturate(1.5);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 20px;
            padding: 16px 18px;
            position: absolute;
            left: 12px;
            bottom: 88px;
            right: 72px;
            z-index: 50;
            display: flex;
            flex-direction: column;
            gap: 6px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.08);
        }

        /* ========== UPGRADE 3: VIDEO PROGRESS BAR ========== */
        .video-progress {
            position: absolute;
            bottom: 80px;
            left: 0;
            right: 0;
            height: 2px;
            background: rgba(255,255,255,0.2);
            z-index: 60;
            overflow: hidden;
        }
        .video-progress-bar {
            height: 100%;
            background: linear-gradient(90deg, #0066CC, #7B3FF1);
            width: 0%;
            transition: width 0.25s linear;
            box-shadow: 0 0 6px rgba(123,63,241,0.8);
        }

        /* ========== UPGRADE 4: BREAKING NEWS DRAMATIC TREATMENT ========== */
        .breaking-scan {
            position: absolute;
            inset: 0;
            z-index: 3;
            background: repeating-linear-gradient(
                0deg,
                transparent,
                transparent 2px,
                rgba(0,0,0,0.03) 2px,
                rgba(0,0,0,0.03) 4px
            );
            pointer-events: none;
            animation: scanMove 8s linear infinite;
        }
        @keyframes scanMove {
            from { background-position: 0 0; }
            to { background-position: 0 200px; }
        }
        .breaking-glow {
            position: absolute;
            bottom: 0; left: 0; right: 0;
            height: 40%;
            background: linear-gradient(to top, rgba(232,25,44,0.25) 0%, transparent 100%);
            z-index: 3;
            pointer-events: none;
        }

        /* Large decorative quote mark */
        .quote-decor {
            font-family: 'Inter', Georgia, serif;
            font-size: 120px;
            font-weight: 900;
            line-height: 0.7;
            color: var(--detik-blue);
            opacity: 0.18;
            position: absolute;
            top: 30%;
            left: 10px;
            z-index: 3;
            pointer-events: none;
            letter-spacing: -4px;
        }

        /* ========== UPGRADE 5: FLOATING PILL BOTTOM NAV ========== */
        #bottomnav {
            position: fixed;
            bottom: calc(16px + env(safe-area-inset-bottom));
            left: 50%;
            transform: translateX(-50%);
            width: calc(100% - 32px);
            max-width: 400px;
            z-index: 100;
            background: rgba(10,10,15,0.88);
            backdrop-filter: blur(24px) saturate(1.8);
            -webkit-backdrop-filter: blur(24px) saturate(1.8);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 30px;
            display: flex;
            justify-content: space-around;
            padding: 10px 8px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.6), 0 0 0 1px rgba(255,255,255,0.04);
        }

        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 3px;
            color: rgba(255,255,255,0.35);
            text-decoration: none;
            font-size: 9px;
            font-weight: 600;
            cursor: pointer;
            transition: color 0.2s, transform 0.2s;
            padding: 4px 10px;
            border-radius: 20px;
            letter-spacing: 0.2px;
            min-width: 48px;
        }
        .nav-item:active { transform: scale(0.9); }
        .nav-item.active {
            color: #fff;
            background: rgba(255,255,255,0.08);
        }
        .nav-item i { font-size: 18px; }
        .nav-item.active i { color: var(--detik-blue); }

        /* Nudge bottom of cards up a bit so nav pill doesn't cover content */
        .card-info { bottom: 108px !important; }
        .right-actions { bottom: 108px !important; }
        .video-progress { bottom: 96px; }

        /* ========== UPGRADE 6: VERTICAL SCROLL INDICATOR ========== */
        #scroll-indicator {
            position: fixed;
            right: 6px;
            top: 50%;
            transform: translateY(-50%);
            z-index: 90;
            display: flex;
            flex-direction: column;
            gap: 5px;
            align-items: center;
        }
        .scroll-dot {
            width: 4px;
            height: 4px;
            border-radius: 50%;
            background: rgba(255,255,255,0.25);
            transition: all 0.3s;
        }
        .scroll-dot.active {
            background: var(--detik-blue);
            height: 16px;
            border-radius: 3px;
            box-shadow: 0 0 6px var(--detik-blue);
        }

        /* ========== UPGRADE 7: COLORED BADGES per content type ========== */
        .badge-breaking  { background: linear-gradient(135deg, #E8192C, #FF4C30) !important; }
        .badge-video     { background: linear-gradient(135deg, #0066CC, #0099FF) !important; }
        .badge-story     { background: linear-gradient(135deg, #7B3FF1, #A855F7) !important; }
        .badge-quote     { background: linear-gradient(135deg, #FF6D00, #FFB300) !important; }
        .badge-explainer { background: linear-gradient(135deg, #00897B, #00C853) !important; }
        .badge-live      { background: linear-gradient(135deg, #E8192C, #C62828) !important; }
        .badge-polling   { background: linear-gradient(135deg, #0066CC, #7B3FF1) !important; }
        .badge-enjoyment { background: linear-gradient(135deg, #00897B, #00C853) !important; }

        /* Gradient glow behind top badge area */
        .badge-glow::before {
            content: '';
            position: absolute;
            inset: 0;
            background: inherit;
            border-radius: inherit;
            filter: blur(12px);
            opacity: 0.4;
        }

        /* ========== LOGO GRADIENT ========== */
        .logo span {
            background: linear-gradient(135deg, #0066CC, #7B3FF1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        /* Remove old fixed bottom nav positioning override */
        /* (handled above in #bottomnav) */
"""

# Insert new CSS before </style>
html = html.replace('    </style>', NEW_CSS + '\n    </style>', 1)

# ============================================================
# 2. Add scroll indicator + restructure bottom nav to preserve pill shape
# ============================================================

# The bottomnav HTML stays the same – CSS already changes it to pill
# Add scroll indicator + dots right before the bottomnav
SCROLL_DOTS_HTML = """
    <!-- SCROLL INDICATOR -->
    <div id="scroll-indicator">
        <!-- dots injected by JS -->
    </div>

"""
html = html.replace('    <!-- BOTTOM NAV -->', SCROLL_DOTS_HTML + '    <!-- BOTTOM NAV -->', 1)

# ============================================================
# 3. Add breaking news dramatic elements to Card 1
# ============================================================
html = html.replace(
    '        <!-- CARD 1: Breaking News -->\n        <div class="card" data-id="1">\n            <img src="Kondisi Terkini (breaking news).jpeg" class="bg-image" alt="Breaking">',
    '        <!-- CARD 1: Breaking News -->\n        <div class="card" data-id="1">\n            <img src="Kondisi Terkini (breaking news).jpeg" class="bg-image" alt="Breaking">\n            <div class="breaking-scan"></div>\n            <div class="breaking-glow"></div>'
)

# ============================================================
# 4. Add decorative quote to Card 3
# ============================================================
html = html.replace(
    '        <!-- CARD 3: Quote Highlights -->',
    '        <!-- CARD 3: Quote Highlights -->'
)
# Add quote decor after the bg-overlay of card 3
html = html.replace(
    '<img src="netanyahu.jpeg" class="bg-image" alt="Netanyahu">\n            <div class="bg-overlay"',
    '<img src="netanyahu.jpeg" class="bg-image" alt="Netanyahu">\n            <div class="quote-decor">&#8220;</div>\n            <div class="bg-overlay"'
)

# ============================================================
# 5. Add video progress bars to all video card sections
# ============================================================
# Card 2 (Israel) – fullscreen video
html = html.replace(
    '            <div class="play-btn"><i class="fa-solid fa-play"></i></div>\n\n            <div class="card-info">\n                <div class="badges-wrap">\n                    <div class="content-badge">VIDEO</div>',
    '            <div class="play-btn"><i class="fa-solid fa-play"></i></div>\n            <div class="video-progress"><div class="video-progress-bar"></div></div>\n\n            <div class="card-info">\n                <div class="badges-wrap">\n                    <div class="content-badge badge-video">VIDEO</div>'
)

# ============================================================
# 6. Upgrade ALL content-badge colors per type
# ============================================================
# BREAKING badge
html = html.replace(
    '<div class="content-badge break-badge">BREAKING</div>',
    '<div class="content-badge break-badge badge-breaking">BREAKING</div>'
)

# LIVE REPORT badges
html = html.replace(
    '<div class="content-badge">LIVE REPORT</div>',
    '<div class="content-badge badge-live">LIVE REPORT</div>'
)
html = html.replace(
    '<div class="content-badge" style="background:#e03a3e">LIVE UPDATE</div>',
    '<div class="content-badge badge-live">LIVE UPDATE</div>'
)

# STORY badges
html = html.replace(
    '<div class="content-badge">STORY</div>',
    '<div class="content-badge badge-story">STORY</div>'
)

# EXPLAINER badges
html = html.replace(
    '<div class="content-badge">EXPLAINER</div>',
    '<div class="content-badge badge-explainer">EXPLAINER</div>'
)

# POLLING badge
html = html.replace(
    '<div class="content-badge">POLLING</div>',
    '<div class="content-badge badge-polling">POLLING</div>'
)

# QUOTE HIGHLIGHTS badge
html = html.replace(
    '<div class="content-badge">QUOTE HIGHLIGHTS</div>',
    '<div class="content-badge badge-quote">QUOTE HIGHLIGHTS</div>'
)

# ENJOYMENT badges
html = html.replace(
    '<div class="content-badge" style="background:#555;">ENJOYMENT <span',
    '<div class="content-badge badge-enjoyment">ENJOYMENT <span'
)
html = html.replace(
    '<div class="content-badge" style="background: #2a2a2a;">ENJOYMENT</div>',
    '<div class="content-badge badge-enjoyment">ENJOYMENT</div>'
)

# ============================================================
# 7. Add video progress + color badge to Banjir Ciledug (Card 9)
# ============================================================
html = html.replace(
    '<div class="content-badge">VIDEO <span\n                            style="font-size:9px; opacity:0.8; margin-left:4px;">(9:16)</span></div>',
    '<div class="content-badge badge-video">VIDEO <span\n                            style="font-size:9px; opacity:0.8; margin-left:4px;">(9:16)</span></div>'
)
html = html.replace(
    '<div class="content-badge">VIDEO <span\n                            style="font-size:9px; opacity:0.8; margin-left:4px;">(3:4)</span></div>',
    '<div class="content-badge badge-video">VIDEO <span\n                            style="font-size:9px; opacity:0.8; margin-left:4px;">(3:4)</span></div>'
)
html = html.replace(
    '<div class="content-badge">VIDEO <span\n                            style="font-size:9px; opacity:0.8; margin-left:4px;">(16:9)</span></div>',
    '<div class="content-badge badge-video">VIDEO <span\n                            style="font-size:9px; opacity:0.8; margin-left:4px;">(16:9)</span></div>'
)

# ============================================================
# 8. Inject JS for scroll indicator dots + video progress bar
# ============================================================
NEW_JS_ADDITIONS = """
        // ===== SCROLL INDICATOR DOTS =====
        const scrollIndicator = document.getElementById('scroll-indicator');
        function buildDots() {
            scrollIndicator.innerHTML = '';
            cards.forEach((_, i) => {
                const dot = document.createElement('div');
                dot.className = 'scroll-dot' + (i === 0 ? ' active' : '');
                scrollIndicator.appendChild(dot);
            });
        }
        function updateDots(idx) {
            const dots = scrollIndicator.querySelectorAll('.scroll-dot');
            dots.forEach((d, i) => d.classList.toggle('active', i === idx));
        }

        // ===== VIDEO PROGRESS BARS =====
        function startProgressBar(card) {
            const video = card.querySelector('video');
            const bar = card.querySelector('.video-progress-bar');
            if (!video || !bar) return;
            if (card._progInterval) clearInterval(card._progInterval);
            card._progInterval = setInterval(() => {
                if (video.duration) {
                    bar.style.width = (video.currentTime / video.duration * 100) + '%';
                }
            }, 250);
        }
        function stopProgressBar(card) {
            if (card._progInterval) clearInterval(card._progInterval);
            const bar = card.querySelector('.video-progress-bar');
            if (bar) bar.style.width = '0%';
        }

        // Patch videoObserver to also handle progress
        const videoObserver2 = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                const card = entry.target;
                if (entry.isIntersecting && entry.intersectionRatio >= 0.75) {
                    startProgressBar(card);
                } else {
                    stopProgressBar(card);
                }
            });
        }, { threshold: 0.75 });
        cards.forEach(card => videoObserver2.observe(card));

        // ===== INTEGRATE DOTS IN COUNTER UPDATE =====
        const _origUpdateCounter = updateCounter;
        function updateCounter() {
            const scrollTop = feed.scrollTop;
            const cardH = feed.clientHeight;
            const idx = Math.round(scrollTop / cardH);
            if (counter) counter.textContent = `${idx + 1} / ${totalCards}`;
            updateDots(idx);
        }

        // ===== INIT DOTS =====
        buildDots();
"""

# Insert new JS before the final </script>
html = html.replace(
    '        // ===== INIT =====\n        updateCounter();\n    </script>',
    NEW_JS_ADDITIONS + '\n        // ===== INIT =====\n        buildDots();\n        updateCounter();\n    </script>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Mega design upgrade applied!")
print("   1. Gradient accent system")
print("   2. Glassmorphism panels")
print("   3. Video progress bars")
print("   4. Breaking/Quote dramatic treatment")
print("   5. Floating pill bottom nav")
print("   6. Vertical scroll indicator dots")
print("   7. Colored gradient badges per content type")
