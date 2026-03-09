import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix CSS for video
css_video_old = """        /* Video / Live */
        video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: 1;
            position: absolute;
            inset: 0;
        }"""
css_video_new = """        /* Video / Live */
        video:not(.media-item) {
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: 1;
            position: absolute;
            inset: 0;
        }"""
html = html.replace(css_video_old, css_video_new)

# 2. Remove search icon
search_icon = '<i class="fa-solid fa-magnifying-glass" style="font-size: 18px; color: #fff; cursor: pointer;"></i>'
html = html.replace(search_icon, '')

# 3. Redesign Live Report CSS
# We will replace the old .live-updates CSS with a new premium one
css_live_old = """        /* Live Report horizontal slide */
        .live-updates {
            display: flex;
            overflow-x: scroll;
            scroll-snap-type: x mandatory;
            gap: 12px;
            margin-top: 12px;
            padding-bottom: 8px;
            scrollbar-width: none;
        }

        .live-updates::-webkit-scrollbar {
            display: none;
        }

        .update-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 8px;
            padding: 12px;
            flex: 0 0 85%;
            scroll-snap-align: start;
        }

        .update-time {
            font-size: 11px;
            color: var(--detik-blue);
            font-weight: 700;
            margin-bottom: 4px;
        }

        .update-text {
            font-size: 13px;
            line-height: 1.4;
        }"""

css_live_new = """        /* Redesigned Premium Live Report */
        .live-updates {
            display: flex;
            overflow-x: scroll;
            scroll-snap-type: x mandatory;
            gap: 16px;
            margin-top: 20px;
            padding-bottom: 24px;
            scrollbar-width: none;
        }

        .live-updates::-webkit-scrollbar {
            display: none;
        }

        .update-card {
            background: rgba(0, 40, 80, 0.6);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(0, 150, 255, 0.3);
            border-radius: 16px;
            padding: 24px;
            flex: 0 0 85%;
            scroll-snap-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            display: flex;
            flex-direction: column;
            justify-content: center;
            position: relative;
            overflow: hidden;
        }
        
        .update-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 4px;
            background: linear-gradient(90deg, var(--detik-blue), #66b3ff);
        }

        .update-time {
            font-size: 14px;
            color: #66b3ff;
            font-weight: 800;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
            letter-spacing: 0.5px;
        }
        
        .update-time::before {
            content: '';
            display: inline-block;
            width: 8px;
            height: 8px;
            background: #E8192C;
            border-radius: 50%;
            box-shadow: 0 0 8px #E8192C;
            animation: blinker 1.5s linear infinite;
        }

        .update-text {
            font-size: 16px;
            line-height: 1.5;
            color: #fff;
            font-weight: 500;
        }"""
html = html.replace(css_live_old, css_live_new)

# 4. Redesign CARD 5 (Live Report) HTML and use the new background image
card5_old_start = '        <!-- CARD 5: Live Report -->'
card5_old_end = '        <!-- CARD 6: Story Mode -->'
card5_block = html[html.find(card5_old_start):html.find(card5_old_end)]

card5_new = """        <!-- CARD 5: Live Report -->
        <div class="card" data-id="5">
            <img src="rapat-paripurna-dpr-1770694989710_169.jpeg" class="bg-image" style="opacity: 0.4;">
            <div class="bg-overlay" style="background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 40%, rgba(0,0,0,0.1) 100%);"></div>

            <div class="card-info" style="bottom: 20px; right: 16px;">
                <div class="badges-wrap">
                    <div class="content-badge">LIVE REPORT</div>
                    <div class="tab-badge"><i class="fa-solid fa-fire"></i> Hangat</div>
                </div>
                <div class="trust-element"><i class="fa-solid fa-clock"></i> Diperbarui 2 menit lalu</div>
                <h2 class="card-title" style="font-size: 24px; margin-top: 8px;">Sidang Paripurna DPR RI 2026</h2>

                <div class="live-updates">
                    <div class="update-card">
                        <div class="update-time">10:45 WIB</div>
                        <div class="update-text">Rapat diskors sementara selama 15 menit karena interupsi sejumlah fraksi terkait laporan anggaran prioritas tahun ini.</div>
                    </div>
                    <div class="update-card">
                        <div class="update-time">10:15 WIB</div>
                        <div class="update-text">Ketua DPR membuka sidang dengan agenda utama pengesahan RUU Perimbangan Keuangan Pusat dan Daerah.</div>
                    </div>
                    <div class="update-card">
                        <div class="update-time">09:30 WIB</div>
                        <div class="update-text">Anggota dewan mulai memasuki ruang rapat paripurna. Pengamanan di area gedung DPR diperketat.</div>
                        <a href="#" class="cta-link" style="margin-top: 16px;">Baca Artikel Lengkap <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>

            <div class="right-actions" style="bottom: auto; top: 100px;">
                <button class="action-btn" onclick="toggleAction(this, 'liked')">
                    <div class="action-icon"><i class="fa-solid fa-heart"></i></div><span class="action-text">890</span>
                </button>
                <button class="action-btn">
                    <div class="action-icon"><i class="fa-solid fa-comment-dots"></i></div><span class="action-text">204</span>
                </button>
                <button class="action-btn" onclick="toggleAction(this, 'bookmarked')">
                    <div class="action-icon"><i class="fa-solid fa-bookmark"></i></div><span class="action-text">Save</span>
                </button>
                <button class="action-btn">
                    <div class="action-icon"><i class="fa-solid fa-share"></i></div><span class="action-text">Share</span>
                </button>
            </div>
        </div>
"""
html = html.replace(card5_block, card5_new + '\n')

# 5. Fix Story Mode Image to UMP.jpeg
html = html.replace('https://akcdn.detik.net.id/visual/2023/11/02/ilus-pekerja.jpeg?w=650', 'UMP.jpeg')

# 6. Add new Carousel Context using DPR photos at the end
new_dpr_carousel = """
        <!-- CARD 13: Carousel DPR -->
        <div class="card" data-id="13">
            <div class="carousel-indicators" id="car-ind-2">
                <div class="c-ind active"></div>
                <div class="c-ind"></div>
            </div>

            <div class="carousel-container" onscroll="updateCarousel(this, 'car-ind-2')">
                <!-- Slide 1 -->
                <div class="carousel-slide">
                    <img src="paripurna-pengesahan-ruu-penyesuaian-pidana-1765183774816_169.jpeg" class="bg-image" style="opacity: 0.8;">
                    <div class="bg-overlay"></div>
                    <div class="card-info" style="bottom: 40px;">
                        <div class="badges-wrap">
                            <div class="content-badge">EXPLAINER</div>
                        </div>
                        <div class="trust-element"><i class="fa-solid fa-landmark"></i> detikNews · 2 jam lalu</div>
                        <h2 class="card-title">Paripurna Pengesahan RUU Penyesuaian Pidana</h2>
                        <p class="story-text">DPR resmi mengesahkan RUU Penyesuaian Pidana setelah melalui perdebatan alot antar fraksi di parlemen.</p>
                        <div style="font-size:12px;color:#aaa;margin-top:8px">Swipe untuk konteks Komisi III <i class="fa-solid fa-arrow-right"></i></div>
                    </div>
                </div>

                <!-- Slide 2 -->
                <div class="carousel-slide">
                    <img src="komisi-iii-dpr-rapat-bahas-kasus-nabilah-obrien-1773032015572_169.jpeg" class="bg-image" style="opacity: 0.8;">
                    <div class="bg-overlay"></div>
                    <div class="card-info" style="bottom: 40px;">
                        <h2 class="card-title">Sorotan Kasus Nabilah O'brien</h2>
                        <p class="story-text">Sebelumnya, Komisi III menggelar rapat maraton membahas kasus yang menarik perhatian publik nasional ini sebagai dasar desakan pengesahan RUU tersebut.</p>
                        <a href="#" class="minimalist-btn" target="_blank">Baca Artikel Lengkap</a>
                    </div>
                </div>
            </div>

            <div class="right-actions">
                <button class="action-btn" onclick="toggleAction(this, 'liked')">
                    <div class="action-icon"><i class="fa-solid fa-heart"></i></div><span class="action-text">3.2K</span>
                </button>
                <button class="action-btn">
                    <div class="action-icon"><i class="fa-solid fa-comment-dots"></i></div><span class="action-text">840</span>
                </button>
                <button class="action-btn" onclick="toggleAction(this, 'bookmarked')">
                    <div class="action-icon"><i class="fa-solid fa-bookmark"></i></div><span class="action-text">Save</span>
                </button>
                <button class="action-btn">
                    <div class="action-icon"><i class="fa-solid fa-share"></i></div><span class="action-text">Share</span>
                </button>
            </div>
        </div>
"""
# Insert before CARD 8 Enjoyment
html = html.replace('<!-- CARD 8: Enjoyment -->', new_dpr_carousel + '\n        <!-- CARD 8: Enjoyment -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
