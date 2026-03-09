import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update bg-image to be cover for fullscreen, and add anim-pan
css_bg_old = """        /* Content Backgrounds */
        .bg-image {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: contain;
            opacity: 0.6;
            z-index: 1;
        }

        .bg-overlay {"""

css_bg_new = """        /* Content Backgrounds */
        .bg-image {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0.6;
            z-index: 1;
        }
        
        @keyframes panImage {
            0% { object-position: 0% 50%; transform: scale(1.1); }
            50% { object-position: 100% 50%; transform: scale(1.1); }
            100% { object-position: 0% 50%; transform: scale(1.1); }
        }
        .anim-pan {
            animation: panImage 20s ease-in-out infinite;
        }

        .bg-overlay {"""
text = text.replace(css_bg_old, css_bg_new)

# 2. Quote and Story text CSS changes
css_text_old = """        .story-text,
        .quote-text {
            font-size: 15px;
            font-weight: 400;
            line-height: 1.5;
            color: #eee;
            margin-top: 4px;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
        }

        .quote-text {
            font-style: italic;
            border-left: 3px solid var(--detik-blue);
            padding-left: 10px;
        }"""

css_text_new = """        .story-text {
            font-size: 15px;
            font-weight: 400;
            line-height: 1.5;
            color: #eee;
            margin-top: 4px;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
        }

        .quote-text {
            font-size: 24px;
            font-weight: 700;
            line-height: 1.3;
            color: #fff;
            margin-top: 12px;
            margin-bottom: 12px;
            font-style: italic;
            border-left: 4px solid var(--detik-blue);
            padding-left: 12px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
        }
        
        .quote-context {
            font-size: 14px;
            color: #ccc;
            margin-top: 16px;
            line-height: 1.5;
        }"""
text = text.replace(css_text_old, css_text_new)

# 3. Breaking News Title top, text bullets
breaking_old = """            <div class="card-info">
                <div class="badges-wrap">
                    <div class="content-badge break-badge">BREAKING</div>
                    <div class="tab-badge"><i class="fa-solid fa-fire"></i> Hangat</div>
                </div>
                <div class="trust-element"><i class="fa-solid fa-user-pen"></i> detikNews · 6 jam lalu</div>
                <h2 class="card-title">Kondisi Terkini Pasca Serangan, Suasana Mencekam</h2>
                <p class="story-text">Situasi darurat ditetapkan. Warga dievakuasi ke tempat paling aman sementara
                    aparat mengamankan lokasi secara ketat.</p>
                <a href="#" class="cta-link">Baca selengkapnya <i class="fa-solid fa-arrow-right"></i></a>
            </div>"""

breaking_new = """            <div class="bg-overlay" style="background: linear-gradient(to bottom, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0) 40%, rgba(0,0,0,0.8) 100%); z-index: 2;"></div>
            
            <div class="card-info" style="top: 80px; bottom: auto;">
                <div class="badges-wrap">
                    <div class="content-badge break-badge">BREAKING</div>
                    <div class="tab-badge"><i class="fa-solid fa-fire"></i> Hangat</div>
                </div>
                <h2 class="card-title" style="font-size: 28px;">Kondisi Terkini Pasca Serangan, Suasana Mencekam</h2>
            </div>
            
            <div class="card-info" style="bottom: 40px; top: auto;">
                <div class="trust-element"><i class="fa-solid fa-user-pen"></i> detikNews · 6 jam lalu</div>
                <ul class="story-text" style="padding-left: 20px;">
                    <li style="margin-bottom: 8px;">Situasi darurat ditetapkan.</li>
                    <li>Warga dievakuasi ke tempat paling aman sementara aparat mengamankan lokasi secara ketat.</li>
                </ul>
                <a href="#" class="cta-link" style="margin-top: 16px;">Baca selengkapnya <i class="fa-solid fa-arrow-right"></i></a>
            </div>"""
text = text.replace(breaking_old, breaking_new)
text = text.replace('alt="Breaking">\n            <div class="bg-overlay"></div>\n\n            <div class="bg-overlay"', 'alt="Breaking">\n\n            <div class="bg-overlay"')

# 4. Quote Highlights swap size
quote_old = """                <h2 class="card-title">Netanyahu Bersumpah Lanjutkan Perang Lawan Iran, Klaim demi Bebas dari Tirani
                </h2>
                <div class="quote-text">
                    "Kita terus maju dengan kekuatan penuh! Perang dimenangkan dengan inisiatif dan strategi, tetapi
                    fondasi pertama kesuksesan adalah tekad."
                </div>"""
                
quote_new = """                <div class="quote-text">
                    "Kita terus maju dengan kekuatan penuh! Perang dimenangkan dengan inisiatif dan strategi, tetapi
                    fondasi pertama kesuksesan adalah tekad."
                </div>
                <div class="quote-context">
                    Konteks: Netanyahu bersumpah lanjutkan perang lawan Iran, ia mengklaim operasi ini perlu untuk membebaskan kawasan dari tirani.
                </div>"""
text = text.replace(quote_old, quote_new)

# 5. Story Mode Pan Animation
story_old = """        <!-- CARD 6: Story Mode -->
        <div class="card" data-id="6">
            <img src="UMP.jpeg" class="bg-image"
                style="opacity: 0.5;">
            <div class="bg-overlay"></div>"""
story_new = """        <!-- CARD 6: Story Mode -->
        <div class="card" data-id="6">
            <img src="UMP.jpeg" class="bg-image anim-pan"
                style="opacity: 0.7;">
            <div class="bg-overlay"></div>"""
text = text.replace(story_old, story_new)

# 6. Banjir Ciledug Relevan -> Dekat
banjir_old = """                    <div class="content-badge">VIDEO <span style="font-size:9px; opacity:0.8; margin-left:4px;">(5:4)</span></div>
                    <div class="tab-badge"><i class="fa-solid fa-thumbtack"></i> Relevan</div>"""
banjir_new = """                    <div class="content-badge">VIDEO <span style="font-size:9px; opacity:0.8; margin-left:4px;">(5:4)</span></div>
                    <div class="tab-badge"><i class="fa-solid fa-location-dot"></i> Dekat</div>"""
text = text.replace(banjir_old, banjir_new)

# 7. Restore Card 8 Enjoyment picture, and Add Card 14 for the Kucing
card8_wrong = """        <!-- CARD 8: Enjoyment -->
        <div class="card" data-id="8">
            <div class="media-container center-align">
                <img src="ilustrasi-kucing-tidak-sehat.jpeg" class="media-item format-9-16">
            </div>
            <div class="bg-overlay"></div>"""
card8_correct = """        <!-- CARD 8: Enjoyment -->
        <div class="card" data-id="8">
            <img src="https://akcdn.detik.net.id/visual/2023/11/08/kucing_169.jpeg?w=650" class="bg-image"
                style="opacity: 0.7;">
            <div class="bg-overlay"></div>"""
text = text.replace(card8_wrong, card8_correct)

# Add card 14
card14 = """
        <!-- CARD 14: Story Mode 2 (Kucing 9:16) -->
        <div class="card" data-id="14">
            <img src="ilustrasi-kucing-tidak-sehat.jpeg" class="bg-image format-9-16" style="opacity: 0.8;">
            <div class="bg-overlay"></div>

            <div class="card-info">
                <div class="badges-wrap">
                    <div class="content-badge">STORY</div>
                </div>
                <div class="trust-element"><i class="fa-solid fa-pen"></i> detikHealth · 1 hari lalu</div>
                <h2 class="card-title">Kenali Tanda Anabul Kesayanganmu Sedang Sakit</h2>
                <p class="story-text">Kucing memang pintar menyembunyikan rasa sakit. Namun sebagai pemilik, kita harus waspada jika mereka mulai kehilangan nafsu makan atau sering bersembunyi.</p>
                <p class="story-text">Deteksi dini sangat penting sebelum kondisinya memburuk. Cek gejala lainnya!</p>
                <a href="#" class="cta-link">Baca panduan lengkapnya <i class="fa-solid fa-arrow-right"></i></a>
            </div>

            <div class="right-actions">
                <button class="action-btn" onclick="toggleAction(this, 'liked')">
                    <div class="action-icon"><i class="fa-solid fa-heart"></i></div><span class="action-text">9.1K</span>
                </button>
                <button class="action-btn">
                    <div class="action-icon"><i class="fa-solid fa-comment-dots"></i></div><span class="action-text">880</span>
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
text = text.replace('    <!-- BOTTOM NAV -->', card14 + '\n    <!-- BOTTOM NAV -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

