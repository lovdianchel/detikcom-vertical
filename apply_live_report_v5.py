import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

live_report_old = """        <!-- CARD 5: Live Report Carousel -->
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
                        <h2 class="card-title" style="font-size: 24px; margin-top: 8px;">Sidang Paripurna DPR RI 2026</h2>
                        
                        <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 16px; margin-bottom: 12px;">
                            <div style="display: flex; gap: 12px; align-items: flex-start;">
                                <div style="font-size: 11px; color: var(--detik-blue); font-weight: 700; width: 40px; flex-shrink: 0; padding-top: 3px;">10:45</div>
                                <div style="font-size: 13px; border-left: 2px solid var(--detik-blue); padding-left: 10px; line-height: 1.4;">Rapat diskors sementara karena interupsi fraksi terkait anggaran.</div>
                            </div>
                            <div style="display: flex; gap: 12px; align-items: flex-start;">
                                <div style="font-size: 11px; color: var(--detik-blue); font-weight: 700; width: 40px; flex-shrink: 0; padding-top: 3px;">10:15</div>
                                <div style="font-size: 13px; border-left: 2px solid var(--detik-blue); padding-left: 10px; line-height: 1.4;">Ketua DPR membuka sidang dengan agenda utama...</div>
                            </div>
                            <div style="display: flex; gap: 12px; align-items: flex-start;">
                                <div style="font-size: 11px; color: var(--detik-blue); font-weight: 700; width: 40px; flex-shrink: 0; padding-top: 3px;">09:30</div>
                                <div style="font-size: 13px; border-left: 2px solid var(--detik-blue); padding-left: 10px; line-height: 1.4;">Anggota dewan mulai memasuki ruang rapat paripurna.</div>
                            </div>
                        </div>
                        
                        <div style="font-size:12px;color:#ccc;margin-top:16px"><i class="fa-solid fa-arrow-right" style="margin-right: 4px; color: var(--detik-blue);"></i> Swipe untuk detail timeline terkini</div>
                    </div>
                </div>

                <div class="carousel-slide">
                    <img src="rapat-paripurna-dpr-penutupan-masa-sidang-1771484072745_169.jpeg" class="bg-image" style="opacity: 0.6;">
                    <div class="bg-overlay" style="background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 40%, rgba(0,0,0,0.1) 100%);"></div>
                    <div class="card-info" style="bottom: 40px; right: 16px;">
                        <div class="badges-wrap">
                            <div class="content-badge" style="background:#e03a3e">LIVE UPDATE</div>
                            <div class="tab-badge"><i class="fa-solid fa-clock"></i> 10:45 WIB</div>
                        </div>
                        <div class="trust-element"><i class="fa-solid fa-link"></i> <a href="#" target="_blank" style="color:#ccc; text-decoration:underline;">Sumber: detikNews (Langsung dari DPR)</a></div>
                        <h2 class="card-title" style="font-size: 20px; margin-top: 8px;">Rapat Diskors Sementara</h2>
                        <div class="update-card" style="margin-top: 12px; background: rgba(255,255,255,0.05); border:none; border-left: 3px solid var(--detik-blue); border-radius:0;">
                            <div class="update-text">Rapat diskors sementara karena interupsi fraksi terkait anggaran. Suasana perdebatan yang intens membuat pimpinan terpaksa menjeda sidang.</div>
                        </div>
                    </div>
                </div>

                <div class="carousel-slide">
                    <img src="rapat-paripurna-dpr-penutupan-masa-sidang-1771484091823_169.jpeg" class="bg-image" style="opacity: 0.6;">
                    <div class="bg-overlay" style="background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 40%, rgba(0,0,0,0.1) 100%);"></div>
                    <div class="card-info" style="bottom: 40px; right: 16px;">
                        <div class="badges-wrap">
                            <div class="content-badge" style="background:#e03a3e">LIVE UPDATE</div>
                            <div class="tab-badge"><i class="fa-solid fa-clock"></i> 10:15 WIB</div>
                        </div>
                        <div class="trust-element"><i class="fa-solid fa-link"></i> <a href="#" target="_blank" style="color:#ccc; text-decoration:underline;">Sumber: Tim detikcom</a></div>
                        <h2 class="card-title" style="font-size: 20px; margin-top: 8px;">Ketua DPR Membuka Sidang</h2>
                        <div class="update-card" style="margin-top: 12px; background: rgba(255,255,255,0.05); border:none; border-left: 3px solid var(--detik-blue); border-radius:0;">
                            <div class="update-text">Ketua DPR membuka sidang dengan agenda utama pengesahan RUU Perimbangan Keuangan. Tercatat kuorum telah terpenuhi.</div>
                        </div>
                    </div>
                </div>

                <div class="carousel-slide">
                    <img src="rapat-paripurna-dpr-penutupan-masa-sidang-1771484109817_169.jpeg" class="bg-image" style="opacity: 0.6;">
                    <div class="bg-overlay" style="background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 40%, rgba(0,0,0,0.1) 100%);"></div>
                    <div class="card-info" style="bottom: 40px; right: 16px;">
                        <div class="badges-wrap">
                            <div class="content-badge" style="background:#e03a3e">LIVE UPDATE</div>
                            <div class="tab-badge"><i class="fa-solid fa-clock"></i> 09:30 WIB</div>
                        </div>
                        <div class="trust-element"><i class="fa-solid fa-link"></i> <a href="#" target="_blank" style="color:#ccc; text-decoration:underline;">Fotografer: detikFoto (Pintu Masuk DPR)</a></div>
                        <h2 class="card-title" style="font-size: 20px; margin-top: 8px;">Pengamanan Diperketat</h2>
                        <div class="update-card" style="margin-top: 12px; background: rgba(255,255,255,0.05); border:none; border-left: 3px solid var(--detik-blue); border-radius:0;">
                            <div class="update-text">Anggota dewan mulai memasuki ruang rapat paripurna. Pengamanan diperketat antisipasi demonstrasi massa buruh.</div>
                        </div>
                    </div>
                </div>
            </div>"""

if live_report_old in text:
    text = text.replace(live_report_old, live_report_new)
else:
    print("NOT FOUND!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
