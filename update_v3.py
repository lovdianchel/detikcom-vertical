import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Bajir Ciledug
text = text.replace('Banjir Ciledug Indah Tangerang.mp4', 'Bajir Ciledug v2.mp4')

# 2. Re-do Live Report
live_report_old = """        <!-- CARD 5: Live Report -->
        <div class="card" data-id="5">
            <img src="rapat-paripurna-dpr-1770694989710_169.jpeg" class="bg-image" style="opacity: 0.4;">
            <div class="bg-overlay"
                style="background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 40%, rgba(0,0,0,0.1) 100%);">
            </div>

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
                        <div class="update-text">Rapat diskors sementara karena interupsi fraksi terkait anggaran.</div>
                    </div>
                    <div class="update-card">
                        <div class="update-time">10:15 WIB</div>
                        <div class="update-text">Ketua DPR membuka sidang dengan agenda utama pengesahan RUU Perimbangan
                            Keuangan.</div>
                    </div>
                    <div class="update-card">
                        <div class="update-time">09:30 WIB</div>
                        <div class="update-text">Anggota dewan mulai memasuki ruang rapat paripurna. Pengamanan
                            diperketat.</div>
                    </div>
                </div>
                <a href="#" class="cta-link" style="margin-top: 16px;">Ikuti Live Terkini <i
                        class="fa-solid fa-arrow-right"></i></a>
            </div>"""

live_report_new = """        <!-- CARD 5: Live Report Carousel -->
        <div class="card" data-id="5">
            <div class="carousel-indicators" id="car-ind-live">
                <div class="c-ind active"></div>
                <div class="c-ind"></div>
                <div class="c-ind"></div>
                <div class="c-ind"></div>
            </div>

            <div class="carousel-container" onscroll="updateCarousel(this, 'car-ind-live')">
                <div class="carousel-slide">
                    <img src="rapat-paripurna-dpr-1770694989710_169.jpeg" class="bg-image" style="opacity: 0.4;">
                    <div class="bg-overlay" style="background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 40%, rgba(0,0,0,0.1) 100%);"></div>
                    <div class="card-info" style="bottom: 40px; right: 16px;">
                        <div class="badges-wrap">
                            <div class="content-badge">LIVE REPORT</div>
                            <div class="tab-badge"><i class="fa-solid fa-fire"></i> Hangat</div>
                        </div>
                        <div class="trust-element"><i class="fa-solid fa-clock"></i> Diperbarui 2 menit lalu</div>
                        <h2 class="card-title" style="font-size: 24px; margin-top: 8px;">Sidang Paripurna DPR RI 2026</h2>
                        <p class="story-text">Rangkuman timeline paripurna hari ini: dari pengamanan ketat, pembukaan sidang, hingga diskors karena interupsi anggaran.</p>
                        <div style="font-size:12px;color:#var(--detik-blue);margin-top:16px">Swipe ke kiri untuk update timeline <i class="fa-solid fa-arrow-right"></i></div>
                    </div>
                </div>

                <div class="carousel-slide">
                    <img src="rapat-paripurna-dpr-1770694989710_169.jpeg" class="bg-image" style="opacity: 0.4;">
                    <div class="bg-overlay" style="background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 40%, rgba(0,0,0,0.1) 100%);"></div>
                    <div class="card-info" style="bottom: 40px; right: 16px;">
                        <div class="badges-wrap">
                            <div class="content-badge" style="background:#e03a3e">LIVE UPDATE</div>
                            <div class="tab-badge"><i class="fa-solid fa-clock"></i> 10:45 WIB</div>
                        </div>
                        <div class="trust-element"><i class="fa-solid fa-pen"></i> Sumber: detikNews (Langsung dari DPR)</div>
                        <h2 class="card-title" style="font-size: 20px; margin-top: 8px;">Rapat Diskors Sementara</h2>
                        <div class="update-card" style="margin-top: 12px; background: rgba(255,255,255,0.05); border:none; border-left: 3px solid var(--detik-blue); border-radius:0;">
                            <div class="update-text">Rapat diskors sementara karena interupsi fraksi terkait anggaran.</div>
                        </div>
                    </div>
                </div>

                <div class="carousel-slide">
                    <img src="rapat-paripurna-dpr-1770694989710_169.jpeg" class="bg-image" style="opacity: 0.4;">
                    <div class="bg-overlay" style="background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 40%, rgba(0,0,0,0.1) 100%);"></div>
                    <div class="card-info" style="bottom: 40px; right: 16px;">
                        <div class="badges-wrap">
                            <div class="content-badge" style="background:#e03a3e">LIVE UPDATE</div>
                            <div class="tab-badge"><i class="fa-solid fa-clock"></i> 10:15 WIB</div>
                        </div>
                        <div class="trust-element"><i class="fa-solid fa-pen"></i> Sumber: Tim detikcom</div>
                        <h2 class="card-title" style="font-size: 20px; margin-top: 8px;">Ketua DPR Membuka Sidang</h2>
                        <div class="update-card" style="margin-top: 12px; background: rgba(255,255,255,0.05); border:none; border-left: 3px solid var(--detik-blue); border-radius:0;">
                            <div class="update-text">Ketua DPR membuka sidang dengan agenda utama pengesahan RUU Perimbangan Keuangan.</div>
                        </div>
                    </div>
                </div>

                <div class="carousel-slide">
                    <img src="rapat-paripurna-dpr-1770694989710_169.jpeg" class="bg-image" style="opacity: 0.4;">
                    <div class="bg-overlay" style="background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 40%, rgba(0,0,0,0.1) 100%);"></div>
                    <div class="card-info" style="bottom: 40px; right: 16px;">
                        <div class="badges-wrap">
                            <div class="content-badge" style="background:#e03a3e">LIVE UPDATE</div>
                            <div class="tab-badge"><i class="fa-solid fa-clock"></i> 09:30 WIB</div>
                        </div>
                        <div class="trust-element"><i class="fa-solid fa-camera"></i> Fotografer: detikFoto (Pintu Masuk DPR)</div>
                        <h2 class="card-title" style="font-size: 20px; margin-top: 8px;">Pengamanan Diperketat</h2>
                        <div class="update-card" style="margin-top: 12px; background: rgba(255,255,255,0.05); border:none; border-left: 3px solid var(--detik-blue); border-radius:0;">
                            <div class="update-text">Anggota dewan mulai memasuki ruang rapat paripurna. Pengamanan diperketat.</div>
                        </div>
                    </div>
                </div>
            </div>"""
text = text.replace(live_report_old, live_report_new)

# 3. Last cat to Kucing.jpeg
# Currently card 8 and card 14 both have gemas-banget-...
# Card 14 is the last cat. So we'll find Card 14 specifically.
card_14_old = """        <!-- CARD 14: Story Mode 2 (Kucing 9:16) -->
        <div class="card" data-id="14">
            <img src="gemas-banget-ekspresi-kucing-yang-bikin-harimu-menyenangkan-1760005451460.webp" class="bg-image format-9-16" style="opacity: 0.8;">"""
card_14_new = """        <!-- CARD 14: Story Mode 2 (Kucing 9:16) -->
        <div class="card" data-id="14">
            <img src="Kucing.jpeg" class="bg-image format-9-16" style="opacity: 0.8;">"""
text = text.replace(card_14_old, card_14_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
