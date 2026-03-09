import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Revert Live Report CSS and make it better (User didn't like the previous one)
css_live_old = """        /* Redesigned Premium Live Report */
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

css_live_new = """        /* Clean minimal Live Report */
        .live-updates {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-top: 16px;
            max-height: 250px;
            overflow-y: scroll;
            padding-right: 8px;
        }

        .update-card {
            border-left: 2px solid var(--detik-blue);
            padding-left: 12px;
            position: relative;
        }
        
        .update-card::before {
            content: '';
            position: absolute;
            left: -5px;
            top: 0;
            width: 8px;
            height: 8px;
            background: var(--detik-blue);
            border-radius: 50%;
        }

        .update-time {
            font-size: 12px;
            color: #ccc;
            font-weight: bold;
            margin-bottom: 4px;
        }

        .update-text {
            font-size: 14px;
            line-height: 1.4;
            color: #eee;
        }"""

html = html.replace(css_live_old, css_live_new)

# Update the HTML structure for live report
live_report_old = """                <div class="live-updates">
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
                </div>"""

live_report_new = """                <div class="live-updates">
                    <div class="update-card">
                        <div class="update-time">10:45 WIB</div>
                        <div class="update-text">Rapat diskors sementara karena interupsi fraksi terkait anggaran.</div>
                    </div>
                    <div class="update-card">
                        <div class="update-time">10:15 WIB</div>
                        <div class="update-text">Ketua DPR membuka sidang dengan agenda utama pengesahan RUU Perimbangan Keuangan.</div>
                    </div>
                    <div class="update-card">
                        <div class="update-time">09:30 WIB</div>
                        <div class="update-text">Anggota dewan mulai memasuki ruang rapat paripurna. Pengamanan diperketat.</div>
                    </div>
                </div>
                <a href="#" class="cta-link" style="margin-top: 16px;">Ikuti Live Terkini <i class="fa-solid fa-arrow-right"></i></a>"""

html = html.replace(live_report_old, live_report_new)

# Restore CARD 5 right actions position
card5_actions_old = '<div class="right-actions" style="bottom: auto; top: 100px;">'
card5_actions_new = '<div class="right-actions">'
html = html.replace(card5_actions_old, card5_actions_new)

# 2. Add classes for 9:16 and ensure 5:4/4:3 are vertically aligned to TOP
css_format_old = """        /* Forcing strictly correct aspect ratios with contain */
        .format-3-4 { 
            width: 100%; 
            height: auto; 
            aspect-ratio: 3/4; 
            max-width: min(85vw, 60vh); 
            object-fit: cover; /* Since aspect-ratio creates precisely that box */
        }
        .format-5-4 { 
            width: 100%; 
            height: auto; 
            aspect-ratio: 5/4; 
            max-width: min(90vw, 75vh);
            object-fit: cover;
        }
        .format-16-9 { 
            width: 100vw; 
            height: auto; 
            aspect-ratio: 16/9; 
            object-fit: cover; 
            border-radius: 0; 
            border: none;
            box-shadow: none;
            background: transparent;
        }"""
        
css_format_new = """        /* Forcing strictly correct aspect ratios */
        .format-9-16 {
            width: 100%;
            height: 100dvh;
            object-fit: cover;
            border-radius: 0;
            max-width: 100%;
            max-height: 100dvh;
        }
        .format-3-4 { 
            width: 100%; 
            height: auto; 
            aspect-ratio: 3/4; 
            max-width: min(85vw, 60vh); 
            object-fit: cover; 
            margin-top: 15dvh; /* Force alignment towards top */
        }
        .format-5-4 { 
            width: 100%; 
            height: auto; 
            aspect-ratio: 5/4; 
            max-width: 100vw;
            object-fit: cover;
            border-radius: 0;
            margin-top: 10dvh; /* Force alignment towards top */
            align-self: flex-start;
        }
        .format-16-9 { 
            width: 100vw; 
            height: auto; 
            aspect-ratio: 16/9; 
            object-fit: cover; 
            border-radius: 0; 
            border: none;
            box-shadow: none;
            background: transparent;
        }"""
        
html = html.replace(css_format_old, css_format_new)

# Ensure the parent can align them to top if flex is involved
css_media_container_old = """        .media-container {
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 2;
            pointer-events: none;
        }"""
css_media_container_new = """        .media-container {
            position: absolute;
            inset: 0;
            display: flex;
            align-items: flex-start; /* Default push to top for custom aspect ratios */
            justify-content: center;
            z-index: 2;
            pointer-events: none;
        }
        .media-container.center-align {
            align-items: center;
        }"""
html = html.replace(css_media_container_old, css_media_container_new)

# Center align 16:9 explicitly
html = html.replace('<div class="media-container">\n                <video class="media-item format-16-9"',
                    '<div class="media-container center-align">\n                <video class="media-item format-16-9"')

# Wait, the cards have content at the bottom, so placing video at the very top is a requirement.

# Let's change Card 8 Enjoyment Kucing into 9:16 portrait style photo using the format
kucing_old = """        <!-- CARD 8: Enjoyment -->
        <div class="card" data-id="8">
            <img src="https://akcdn.detik.net.id/visual/2023/11/08/kucing_169.jpeg?w=650" class="bg-image"
                style="opacity: 0.7;">
            <div class="bg-overlay"></div>

            <div class="card-info">
                <div class="badges-wrap">
                    <div class="content-badge" style="background: #2a2a2a;">ENJOYMENT</div>
                </div>
                <h2 class="card-title">Kucing Menggemaskan Beraksi Selamatkan Anjing yang Terjebak</h2>
                <p class="story-text">Momen langka tertangkap kamera di mana seekor kucing oren berusaha memandu anjing
                    kecil yang tersesat di saluran air. Kejadian lucu nan mengharukan ini langsung viral di media
                    sosial.</p>
            </div>"""

kucing_new = """        <!-- CARD 8: Enjoyment -->
        <div class="card" data-id="8">
            <div class="media-container center-align">
                <img src="ilustrasi-kucing-tidak-sehat.jpeg" class="media-item format-9-16">
            </div>
            <div class="bg-overlay"></div>

            <div class="card-info">
                <div class="badges-wrap">
                    <div class="content-badge" style="background: #2a2a2a;">ENJOYMENT</div>
                </div>
                <h2 class="card-title">Kucing Menggemaskan Beraksi Selamatkan Anjing yang Terjebak</h2>
                <p class="story-text">Momen langka tertangkap kamera di mana seekor kucing oren berusaha memandu anjing
                    kecil yang tersesat di saluran air. Kejadian lucu nan mengharukan ini langsung viral di media
                    sosial.</p>
            </div>"""
html = html.replace(kucing_old, kucing_new)

# Wait we already added another Kucing at the end. We should remove the duplicate.
# Card 14: Story Mode 2 from earlier
html = re.sub(r'<!-- CARD 14: Story Mode 2 -->.*?</div>\s*</div>', '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
