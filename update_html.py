import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS styles
css_adds = """
        /* Mute Button */
        .mute-btn {
            position: absolute;
            top: 20px;
            right: 20px;
            z-index: 60;
            background: rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(4px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: white;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: 0.2s;
        }
        .mute-btn:active {
            transform: scale(0.9);
        }

        /* Media Container for custom aspect ratios */
        .media-container {
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 2;
            pointer-events: none;
        }
        .media-container > * {
            pointer-events: auto;
        }
        .media-item {
            width: 100%;
            height: auto;
            max-height: 80vh;
            object-fit: cover;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.8);
        }
        .format-3-4 { aspect-ratio: 3 / 4; width: 95%; max-width: 400px; }
        .format-5-4 { aspect-ratio: 5 / 4; width: 95%; max-width: 450px; }
        .format-16-9 { aspect-ratio: 16 / 9; width: 100%; border-radius: 0; }
        
        .poll-source {
            margin-top: 15px;
            background: rgba(0, 80, 158, 0.2);
            border: 1px solid var(--detik-blue);
            border-radius: 8px;
            padding: 12px;
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: white;
            transition: 0.2s;
        }
        .poll-source:active { background: rgba(0, 80, 158, 0.4); }
"""

html = html.replace('/* Top Bar */', css_adds + '\n        /* Top Bar */')

# 2. Update Polling
poll_html = """
        <!-- CARD 7: Polling -->
        <div class="card" data-id="7">
            <div style="background: #111; position:absolute; inset:0;"></div>

            <div class="card-info" style="bottom: auto; top: 100px;">
                <div class="badges-wrap">
                    <div class="content-badge">POLLING</div>
                </div>
                <div class="trust-element"><i class="fa-solid fa-square-poll-vertical"></i> detikPolling</div>
                <h2 class="card-title" style="margin-bottom: 12px;">Menurut kamu, apakah PSEL Burangkeng akan efektif mengatasi sampah Bekasi?</h2>

                <div class="poll-container" style="border: none; background: rgba(255,255,255,0.05);">
                    <div class="poll-opt" onclick="votePoll(this, 1, 65)">
                        <div class="poll-bar" id="p1-bar"></div>
                        <span class="poll-text">Sangat Efektif</span>
                        <span class="poll-pct" id="p1-pct">65%</span>
                    </div>
                    <div class="poll-opt" onclick="votePoll(this, 2, 25)">
                        <div class="poll-bar" id="p2-bar"></div>
                        <span class="poll-text">Biasa Saja</span>
                        <span class="poll-pct" id="p2-pct">25%</span>
                    </div>
                    <div class="poll-opt" onclick="votePoll(this, 3, 10)">
                        <div class="poll-bar" id="p3-bar"></div>
                        <span class="poll-text">Tidak Efektif</span>
                        <span class="poll-pct" id="p3-pct">10%</span>
                    </div>
                </div>
                
                <a href="https://news.detik.com/foto-news/d-8386051/pembangunan-fasilitas-pengolahan-sampah-jadi-energi-listrik-di-burangkeng-molor" target="_blank" class="poll-source">
                    <img src="https://akcdn.detik.net.id/visual/2023/10/08/serangan-hamas-ke-israel-3_169.jpeg?w=100" style="width: 48px; height: 48px; border-radius: 6px; object-fit: cover;">
                    <div style="flex:1">
                        <div style="font-size: 10px; color: var(--detik-blue); font-weight: 800; margin-bottom: 2px;">SUMBER ARTIKEL</div>
                        <div style="font-size: 12px; font-weight: 600; line-height: 1.3;">Pembangunan PSEL di Burangkeng Molor</div>
                    </div>
                    <i class="fa-solid fa-chevron-right" style="font-size: 14px; opacity: 0.7;"></i>
                </a>
            </div>

            <div class="right-actions">
                <button class="action-btn" onclick="toggleAction(this, 'liked')">
                    <div class="action-icon"><i class="fa-solid fa-heart"></i></div><span class="action-text">980</span>
                </button>
                <button class="action-btn">
                    <div class="action-icon"><i class="fa-solid fa-comment-dots"></i></div><span
                        class="action-text">24</span>
                </button>
                <button class="action-btn" onclick="toggleAction(this, 'bookmarked')">
                    <div class="action-icon"><i class="fa-solid fa-bookmark"></i></div><span
                        class="action-text">Save</span>
                </button>
                <button class="action-btn">
                    <div class="action-icon"><i class="fa-solid fa-share"></i></div><span
                        class="action-text">Share</span>
                </button>
            </div>
        </div>
"""

old_poll = html[html.find('<!-- CARD 7: Polling -->'):html.find('<!-- CARD 8: Enjoyment -->')]
html = html.replace(old_poll, poll_html)

# 3. Add original Card 2 mute button
card2_pattern = r'(<div class="card" data-id="2">.*?<video loop playsinline muted>.*?<source src="Israel Serang Depot BBM IRAN\.mp4" type="video/mp4">.*?</video>\s*<div class="bg-overlay"></div>)'
card2_replace = r'\1\n            <button class="mute-btn" onclick="toggleMute(this, event)"><i class="fa-solid fa-volume-xmark"></i></button>'
html = re.sub(card2_pattern, card2_replace, html, flags=re.DOTALL)


# 4. Add new cards at the end of the feed (before CARD 8 so we have room)
new_cards = """
        <!-- CARD 9: Video Banjir -->
        <div class="card" data-id="9">
            <div style="background: #111; position:absolute; inset:0;"></div>
            <img src="Banjir Ciledug Indah Tangerang.mp4" class="bg-image" style="opacity:0.3; filter:blur(20px);"> <!-- blur bg simulation -->
            <div class="bg-overlay"></div>
            
            <div class="media-container">
                <video class="media-item format-5-4" loop playsinline muted onclick="togglePlay(this, event)">
                    <source src="Banjir Ciledug Indah Tangerang.mp4" type="video/mp4">
                </video>
            </div>
            
            <button class="mute-btn" onclick="toggleMute(this, event)"><i class="fa-solid fa-volume-xmark"></i></button>
            <div class="play-btn" style="z-index: 10;"><i class="fa-solid fa-play"></i></div>

            <div class="card-info" style="z-index: 50;">
                <div class="badges-wrap">
                    <div class="content-badge">VIDEO <span style="font-size:9px; opacity:0.8; margin-left:4px;">(5:4)</span></div>
                    <div class="tab-badge"><i class="fa-solid fa-thumbtack"></i> Relevan</div>
                </div>
                <div class="trust-element"><i class="fa-solid fa-video"></i> 20detik · Baru saja</div>
                <h2 class="card-title">Banjir Ciledug Indah Tangerang</h2>
                <p class="story-text">Kondisi terkini perumahan Ciledug Indah pasca hujan deras. Ketinggian air mencapai lutut orang dewasa.</p>
            </div>

            <div class="right-actions" style="z-index: 50;">
                <button class="action-btn" onclick="toggleAction(this, 'liked')">
                    <div class="action-icon"><i class="fa-solid fa-heart"></i></div><span class="action-text">12K</span>
                </button>
                <button class="action-btn">
                    <div class="action-icon"><i class="fa-solid fa-comment-dots"></i></div><span class="action-text">450</span>
                </button>
                <button class="action-btn" onclick="toggleAction(this, 'bookmarked')">
                    <div class="action-icon"><i class="fa-solid fa-bookmark"></i></div><span class="action-text">Save</span>
                </button>
                <button class="action-btn">
                    <div class="action-icon"><i class="fa-solid fa-share"></i></div><span class="action-text">Share</span>
                </button>
            </div>
        </div>

        <!-- CARD 10: Video Timteng (3:4) -->
        <div class="card" data-id="10">
            <div style="background: #111; position:absolute; inset:0;"></div>
            <div class="bg-overlay"></div>
            
            <div class="media-container">
                <video class="media-item format-3-4" loop playsinline muted onclick="togglePlay(this, event)">
                    <source src="Krisis Timteng Mahal, Filipina Terapkan Kerja 4 Hari (3 banding 4).mp4" type="video/mp4">
                </video>
            </div>
            
            <button class="mute-btn" onclick="toggleMute(this, event)"><i class="fa-solid fa-volume-xmark"></i></button>
            <div class="play-btn" style="z-index: 10;"><i class="fa-solid fa-play"></i></div>

            <div class="card-info" style="z-index: 50;">
                <div class="badges-wrap">
                    <div class="content-badge">VIDEO <span style="font-size:9px; opacity:0.8; margin-left:4px;">(3:4)</span></div>
                </div>
                <div class="trust-element"><i class="fa-solid fa-globe"></i> detikNews · 3 jam lalu</div>
                <h2 class="card-title">Krisis Timteng Makin Mahal, Filipina Terapkan Kerja 4 Hari</h2>
                <p class="story-text">Dampak ekonomi global membuat sejumlah negara merumuskan kebijakan baru, termasuk penyesuaian jam kerja demi ketahanan energi.</p>
            </div>

            <div class="right-actions" style="z-index: 50;">
                <button class="action-btn" onclick="toggleAction(this, 'liked')">
                    <div class="action-icon"><i class="fa-solid fa-heart"></i></div><span class="action-text">5.6K</span>
                </button>
                <button class="action-btn">
                    <div class="action-icon"><i class="fa-solid fa-share"></i></div><span class="action-text">Share</span>
                </button>
            </div>
        </div>

        <!-- CARD 11: Video Horizontal -->
        <div class="card" data-id="11">
            <div style="background: #000; position:absolute; inset:0;"></div>
            
            <div class="media-container">
                <video class="media-item format-16-9" loop playsinline muted onclick="togglePlay(this, event)">
                    <source src="VIDEO-2026-03-09-12-05-24 (horizontal).mp4" type="video/mp4">
                </video>
            </div>
            
            <div class="bg-overlay"></div>
            <button class="mute-btn" onclick="toggleMute(this, event)"><i class="fa-solid fa-volume-xmark"></i></button>
            <div class="play-btn" style="z-index: 10;"><i class="fa-solid fa-play"></i></div>

            <div class="card-info" style="z-index: 50;">
                <div class="badges-wrap">
                    <div class="content-badge">VIDEO <span style="font-size:9px; opacity:0.8; margin-left:4px;">(16:9)</span></div>
                </div>
                <div class="trust-element"><i class="fa-solid fa-video"></i> 20detik · 1 jam lalu</div>
                <h2 class="card-title">Momentum Terkini</h2>
                <p class="story-text">Cuplikan dari kejadian mendadak siang ini yang menyita perhatian publik.</p>
            </div>

            <div class="right-actions" style="z-index: 50;">
                <button class="action-btn" onclick="toggleAction(this, 'liked')">
                    <div class="action-icon"><i class="fa-solid fa-heart"></i></div><span class="action-text">2K</span>
                </button>
            </div>
        </div>

        <!-- CARD 12: Photo Wali Band (3:4) -->
        <div class="card" data-id="12">
            <div style="background: #111; position:absolute; inset:0;"></div>
            <img src="wali-band-deretan lagu bukber.jpeg" class="bg-image" style="opacity:0.2; filter:blur(15px);">
            <div class="bg-overlay"></div>
            
            <div class="media-container">
                <img src="wali-band-deretan lagu bukber.jpeg" class="media-item format-3-4" alt="Wali Band">
            </div>

            <div class="card-info" style="z-index: 50;">
                <div class="badges-wrap">
                    <div class="content-badge" style="background:#555;">ENJOYMENT <span style="font-size:9px; opacity:0.8; margin-left:4px;">(3:4)</span></div>
                </div>
                <div class="trust-element"><i class="fa-solid fa-music"></i> detikHot · 5 jam lalu</div>
                <h2 class="card-title">Deretan Lagu Wali yang Cocok Buat Bukber</h2>
                <p class="story-text">Siapa yang setuju kalau lagu-lagu Wali bikin nostalgia zaman buka bersama bareng teman sekolah?</p>
            </div>

            <div class="right-actions" style="z-index: 50;">
                <button class="action-btn" onclick="toggleAction(this, 'liked')">
                    <div class="action-icon"><i class="fa-solid fa-heart"></i></div><span class="action-text">4.1K</span>
                </button>
                <button class="action-btn">
                    <div class="action-icon"><i class="fa-solid fa-share"></i></div><span class="action-text">Share</span>
                </button>
            </div>
        </div>

"""

html = html.replace('<!-- CARD 8: Enjoyment -->', new_cards + '\n        <!-- CARD 8: Enjoyment -->')


# 5. Fix JS
js_adds = """

        function toggleMute(btn, event) {
            if (event) event.stopPropagation();
            const card = btn.closest('.card');
            const video = card.querySelector('video');
            if (video) {
                video.muted = !video.muted;
                const icon = btn.querySelector('i');
                if (video.muted) {
                    icon.className = 'fa-solid fa-volume-xmark';
                } else {
                    icon.className = 'fa-solid fa-volume-high';
                }
            }
        }
        
        function togglePlay(video, event) {
            if (event) event.stopPropagation();
            const card = video.closest('.card');
            const playBtn = card.querySelector('.play-btn');
            
            if (video.paused) {
                video.play();
                if (playBtn) playBtn.style.display = 'none';
            } else {
                video.pause();
                if (playBtn) playBtn.style.display = 'block';
            }
        }

"""

html = html.replace('// Handle Carousel Indicators', js_adds + '\n        // Handle Carousel Indicators')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

