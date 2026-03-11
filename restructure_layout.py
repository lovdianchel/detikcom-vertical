"""
Layout Restructure: Apply "title at top, caption at bottom" to all non-carousel cards.

Pattern:
  TOP block   → badge(s) + headline (big font)
  BOTTOM block → trust element + 1-2 sentences summary + CTA link
"""
TOP_STYLE    = 'top: 72px; bottom: auto; right: 72px;'
BOTTOM_STYLE = 'bottom: 108px; top: auto; right: 72px;'

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We'll use string operations (not BS4) because the HTML has inline JS and BS4 mangles it.
# Strategy: Replace each card's single .card-info block manually.

# ============================================================
# CARD 2: Video (Israel) — currently one block at bottom
# ============================================================
OLD_C2 = """            <div class="card-info">
                <div class="badges-wrap">
                    <div class="content-badge badge-video">VIDEO</div>
                    <div class="tab-badge"><i class="fa-solid fa-thumbtack"></i> Relevan</div>
                </div>
                <div class="trust-element"><i class="fa-solid fa-video"></i> 20detik · 09 Mar 2026</div>
                <h2 class="card-title">Israel Serang Depot BBM IRAN</h2>
                <p class="story-text">Rekaman udara menunjukkan momen depot BBM dilanda ledakan hebat.</p>
            </div>"""

NEW_C2 = """            <div class="card-info" style="top: 72px; bottom: auto; right: 72px;">
                <div class="badges-wrap">
                    <div class="content-badge badge-video">VIDEO</div>
                    <div class="tab-badge"><i class="fa-solid fa-thumbtack"></i> Relevan</div>
                </div>
                <h2 class="card-title" style="font-size: 26px;">Israel Serang Depot BBM IRAN</h2>
            </div>
            <div class="card-info" style="bottom: 108px; top: auto; right: 72px;">
                <div class="trust-element"><i class="fa-solid fa-video"></i> 20detik · 09 Mar 2026</div>
                <p class="story-text">Rekaman udara menunjukkan momen depot BBM Iran dilanda ledakan hebat. Aksi ini memperparah ketegangan di kawasan.</p>
                <a href="#" class="cta-link">Tonton selengkapnya <i class="fa-solid fa-arrow-right"></i></a>
            </div>"""

html = html.replace(OLD_C2, NEW_C2)

# ============================================================
# CARD 3: Quote Highlights
# ============================================================
OLD_C3 = """            <div class="card-info">
                <div class="badges-wrap">
                    <div class="content-badge badge-quote">QUOTE HIGHLIGHTS</div>
                    <div class="tab-badge"><i class="fa-solid fa-location-dot"></i> Dekat</div>
                </div>
                <div class="trust-element">
                    <i class="fa-solid fa-link"></i>
                    <a href="https://www.detik.com/jogja/berita/d-8391041/netanyahu-bersumpah-lanjutkan-perang-lawan-iran-klaim-demi-bebas-dari-tirani"
                        target="_blank">detikNews · 08 Mar 2026</a>
                </div>
                <div class="quote-text">
                    "Kita terus maju dengan kekuatan penuh! Perang dimenangkan dengan inisiatif dan strategi, tetapi
                    fondasi pertama kesuksesan adalah tekad."
                </div>
                <div class="quote-context">
                    Konteks: Netanyahu bersumpah lanjutkan perang lawan Iran, ia mengklaim operasi ini perlu untuk
                    membebaskan kawasan dari tirani.
                </div>
            </div>"""

NEW_C3 = """            <div class="card-info" style="top: 72px; bottom: auto; right: 72px;">
                <div class="badges-wrap">
                    <div class="content-badge badge-quote">QUOTE HIGHLIGHTS</div>
                    <div class="tab-badge"><i class="fa-solid fa-location-dot"></i> Dekat</div>
                </div>
                <div class="quote-text" style="font-size: 22px; margin-top: 8px;">
                    "Kita terus maju dengan kekuatan penuh! Perang dimenangkan dengan inisiatif dan strategi."
                </div>
            </div>
            <div class="card-info" style="bottom: 108px; top: auto; right: 72px;">
                <div class="trust-element">
                    <i class="fa-solid fa-link"></i>
                    <a href="https://www.detik.com/jogja/berita/d-8391041/netanyahu-bersumpah-lanjutkan-perang-lawan-iran-klaim-demi-bebas-dari-tirani"
                        target="_blank">detikNews · 08 Mar 2026</a>
                </div>
                <div class="quote-context">
                    Netanyahu — Perdana Menteri Israel, bersumpah lanjutkan perang lawan Iran demi membebaskan kawasan dari tirani.
                </div>
            </div>"""

html = html.replace(OLD_C3, NEW_C3)

# ============================================================
# CARD 6: Story Mode (Gaji UMR)
# ============================================================
OLD_C6 = """            <div class="card-info">
                <div class="badges-wrap">
                    <div class="content-badge badge-story">STORY</div>
                    <div class="tab-badge"><i class="fa-solid fa-thumbtack"></i> Relevan</div>
                </div>
                <div class="trust-element"><i class="fa-solid fa-pen"></i> detikFinance · Kemarin</div>
                <h2 class="card-title">Gaji Tetap UMR, Tapi Gaya Hidup Sultan</h2>
                <p class="story-text">Siapa yang sering merasa gajinya cuma numpang lewat tiap bulan? Fenomena ini makin
                    sering dialami Generasi Z. Banyak yang gajinya UMR, tapi rela puasa di akhir bulan demi membeli kopi
                    kekinian atau nonton konser. Bagaimana bisa?</p>
                <p class="story-text">Gaya hidup yang didorong FOMO (Fear of Missing Out) membuat pengeluaran membengkak
                    tanpa terasa. Cek faktanya di artikel selengkapnya.</p>
                <a href="#" class="cta-link">Baca liputan khusus <i class="fa-solid fa-arrow-right"></i></a>
            </div>"""

NEW_C6 = """            <div class="card-info" style="top: 72px; bottom: auto; right: 72px;">
                <div class="badges-wrap">
                    <div class="content-badge badge-story">STORY</div>
                    <div class="tab-badge"><i class="fa-solid fa-thumbtack"></i> Relevan</div>
                </div>
                <h2 class="card-title" style="font-size: 26px;">Gaji Tetap UMR, Tapi Gaya Hidup Sultan</h2>
            </div>
            <div class="card-info" style="bottom: 108px; top: auto; right: 72px;">
                <div class="trust-element"><i class="fa-solid fa-pen"></i> detikFinance · Kemarin</div>
                <p class="story-text">FOMO mendorong Gen Z habiskan gaji UMR untuk konser & kopi kekinian — lalu puasa di akhir bulan.</p>
                <a href="#" class="cta-link">Baca liputan khusus <i class="fa-solid fa-arrow-right"></i></a>
            </div>"""

html = html.replace(OLD_C6, NEW_C6)

# ============================================================
# CARD 8: Enjoyment (Kucing)
# ============================================================
OLD_C8 = """            <div class="card-info">
                <div class="badges-wrap">
                    <div class="content-badge badge-enjoyment">ENJOYMENT</div>
                </div>
                <h2 class="card-title">Kucing Menggemaskan Beraksi Selamatkan Anjing yang Terjebak</h2>
                <p class="story-text">Momen langka tertangkap kamera di mana seekor kucing oren berusaha memandu anjing
                    kecil yang tersesat di saluran air. Kejadian lucu nan mengharukan ini langsung viral di media
                    sosial.</p>
            </div>"""

NEW_C8 = """            <div class="card-info" style="top: 72px; bottom: auto; right: 72px;">
                <div class="badges-wrap">
                    <div class="content-badge badge-enjoyment">ENJOYMENT</div>
                </div>
                <h2 class="card-title" style="font-size: 26px;">Kucing Menggemaskan Selamatkan Anjing yang Terjebak</h2>
            </div>
            <div class="card-info" style="bottom: 108px; top: auto; right: 72px;">
                <p class="story-text">Momen langka: seekor kucing oren memandu anjing kecil yang tersesat di saluran air — langsung viral!</p>
                <a href="#" class="cta-link">Lihat lebih lanjut <i class="fa-solid fa-arrow-right"></i></a>
            </div>"""

html = html.replace(OLD_C8, NEW_C8)

# ============================================================
# CARD 9: Video Banjir Ciledug
# ============================================================
OLD_C9 = """            <div class="card-info" style="z-index: 50;">
                <div class="badges-wrap">
                    <div class="content-badge badge-video">VIDEO <span
                            style="font-size:9px; opacity:0.8; margin-left:4px;">(9:16)</span></div>
                    <div class="tab-badge"><i class="fa-solid fa-location-dot"></i> Dekat</div>
                </div>
                <div class="trust-element"><i class="fa-solid fa-video"></i> 20detik · Baru saja</div>
                <h2 class="card-title">Banjir Ciledug Indah Tangerang</h2>
                <p class="story-text">Kondisi terkini perumahan Ciledug Indah pasca hujan deras. Ketinggian air mencapai
                    lutut orang dewasa.</p>
            </div>"""

NEW_C9 = """            <div class="card-info" style="z-index: 50; top: 72px; bottom: auto; right: 72px;">
                <div class="badges-wrap">
                    <div class="content-badge badge-video">VIDEO <span
                            style="font-size:9px; opacity:0.8; margin-left:4px;">(9:16)</span></div>
                    <div class="tab-badge"><i class="fa-solid fa-location-dot"></i> Dekat</div>
                </div>
                <h2 class="card-title" style="font-size: 26px;">Banjir Ciledug Indah Tangerang</h2>
            </div>
            <div class="card-info" style="z-index: 50; bottom: 108px; top: auto; right: 72px;">
                <div class="trust-element"><i class="fa-solid fa-video"></i> 20detik · Baru saja</div>
                <p class="story-text">Kondisi terkini pasca hujan deras. Ketinggian air mencapai lutut orang dewasa.</p>
                <a href="#" class="cta-link">Lihat video <i class="fa-solid fa-arrow-right"></i></a>
            </div>"""

html = html.replace(OLD_C9, NEW_C9)

# ============================================================
# CARD 10: Video Timteng (3:4)
# ============================================================
OLD_C10 = """            <div class="card-info" style="z-index: 50;">
                <div class="badges-wrap">
                    <div class="content-badge badge-video">VIDEO <span
                            style="font-size:9px; opacity:0.8; margin-left:4px;">(3:4)</span></div>
                </div>
                <div class="trust-element"><i class="fa-solid fa-globe"></i> detikNews · 3 jam lalu</div>
                <h2 class="card-title">Krisis Timteng Makin Mahal, Filipina Terapkan Kerja 4 Hari</h2>
                <p class="story-text">Dampak ekonomi global membuat sejumlah negara merumuskan kebijakan baru, termasuk
                    penyesuaian jam kerja demi ketahanan energi.</p>
            </div>"""

NEW_C10 = """            <div class="card-info" style="z-index: 50; top: 72px; bottom: auto; right: 72px;">
                <div class="badges-wrap">
                    <div class="content-badge badge-video">VIDEO <span
                            style="font-size:9px; opacity:0.8; margin-left:4px;">(3:4)</span></div>
                </div>
                <h2 class="card-title" style="font-size: 24px;">Krisis Timteng Makin Mahal, Filipina Terapkan Kerja 4 Hari</h2>
            </div>
            <div class="card-info" style="z-index: 50; bottom: 108px; top: auto; right: 72px;">
                <div class="trust-element"><i class="fa-solid fa-globe"></i> detikNews · 3 jam lalu</div>
                <p class="story-text">Dampak ekonomi global mendorong kebijakan baru: penyesuaian jam kerja demi ketahanan energi.</p>
                <a href="#" class="cta-link">Tonton selengkapnya <i class="fa-solid fa-arrow-right"></i></a>
            </div>"""

html = html.replace(OLD_C10, NEW_C10)

# ============================================================
# CARD 11: Video Horizontal (16:9)
# ============================================================
OLD_C11 = """            <div class="card-info" style="z-index: 50;">
                <div class="badges-wrap">
                    <div class="content-badge badge-video">VIDEO <span
                            style="font-size:9px; opacity:0.8; margin-left:4px;">(16:9)</span></div>
                </div>
                <div class="trust-element"><i class="fa-solid fa-video"></i> 20detik · 1 jam lalu</div>
                <h2 class="card-title">Momentum Terkini</h2>
                <p class="story-text">Cuplikan dari kejadian mendadak siang ini yang menyita perhatian publik.</p>
            </div>"""

NEW_C11 = """            <div class="card-info" style="z-index: 50; top: 72px; bottom: auto; right: 72px;">
                <div class="badges-wrap">
                    <div class="content-badge badge-video">VIDEO <span
                            style="font-size:9px; opacity:0.8; margin-left:4px;">(16:9)</span></div>
                </div>
                <h2 class="card-title" style="font-size: 26px;">Momentum Terkini</h2>
            </div>
            <div class="card-info" style="z-index: 50; bottom: 108px; top: auto; right: 72px;">
                <div class="trust-element"><i class="fa-solid fa-video"></i> 20detik · 1 jam lalu</div>
                <p class="story-text">Cuplikan dari kejadian mendadak siang ini yang menyita perhatian publik.</p>
                <a href="#" class="cta-link">Tonton sekarang <i class="fa-solid fa-arrow-right"></i></a>
            </div>"""

html = html.replace(OLD_C11, NEW_C11)

# ============================================================
# CARD 12: Photo Wali Band (3:4)
# ============================================================
OLD_C12 = """            <div class="card-info" style="z-index: 50;">
                <div class="badges-wrap">
                    <div class="content-badge badge-enjoyment">ENJOYMENT <span
                            style="font-size:9px; opacity:0.8; margin-left:4px;">(3:4)</span></div>
                </div>
                <div class="trust-element"><i class="fa-solid fa-music"></i> detikHot · 5 jam lalu</div>
                <h2 class="card-title">Deretan Lagu Wali yang Cocok Buat Bukber</h2>
                <p class="story-text">Siapa yang setuju kalau lagu-lagu Wali bikin nostalgia zaman buka bersama bareng
                    teman sekolah?</p>
                <p class="story-text">Artikel ini merekomendasikan beberapa lagu religi yang cocok dijadikan backsound
                    konten bukber selama Ramadan. Beberapa di antaranya adalah Ketika Tangan dan Kaki Berkata versi
                    Cakra Khan, Shalawat Badar dari Hasna, Romantika Badar dan Uhud dari Wali, Pulang PadaMu dari Ungu,
                    dan Syukur Alhamdulillah dari Opick. Lagu-lagu ini menghadirkan nuansa religi yang syahdu dan cocok
                    untuk konten Ramadan.</p>
            </div>"""

NEW_C12 = """            <div class="card-info" style="z-index: 50; top: 72px; bottom: auto; right: 72px;">
                <div class="badges-wrap">
                    <div class="content-badge badge-enjoyment">ENJOYMENT <span
                            style="font-size:9px; opacity:0.8; margin-left:4px;">(3:4)</span></div>
                </div>
                <h2 class="card-title" style="font-size: 24px;">Deretan Lagu Wali yang Cocok Buat Bukber</h2>
            </div>
            <div class="card-info" style="z-index: 50; bottom: 108px; top: auto; right: 72px;">
                <div class="trust-element"><i class="fa-solid fa-music"></i> detikHot · 5 jam lalu</div>
                <p class="story-text">Dari Romantika Badar & Uhud (Wali), Cakra Khan, hingga Opick — ini daftar lagu religi syahdu buat konten bukber Ramadan.</p>
                <a href="#" class="cta-link">Baca daftar lengkap <i class="fa-solid fa-arrow-right"></i></a>
            </div>"""

html = html.replace(OLD_C12, NEW_C12)

# ============================================================
# CARD 14: Story Mode 2 (Kucing 9:16)
# ============================================================
OLD_C14 = """            <div class="card-info">
                <div class="badges-wrap">
                    <div class="content-badge badge-story">STORY</div>
                </div>
                <div class="trust-element"><i class="fa-solid fa-pen"></i> detikHealth · 1 hari lalu</div>
                <h2 class="card-title">Kenali Tanda Anabul Kesayanganmu Sedang Sakit</h2>
                <p class="story-text">Kucing memang pintar menyembunyikan rasa sakit. Namun sebagai pemilik, kita harus
                    waspada jika mereka mulai kehilangan nafsu makan atau sering bersembunyi.</p>
                <p class="story-text">Deteksi dini sangat penting sebelum kondisinya memburuk. Cek gejala lainnya!</p>
                <a href="#" class="cta-link">Baca panduan lengkapnya <i class="fa-solid fa-arrow-right"></i></a>
            </div>"""

NEW_C14 = """            <div class="card-info" style="top: 72px; bottom: auto; right: 72px;">
                <div class="badges-wrap">
                    <div class="content-badge badge-story">STORY</div>
                </div>
                <h2 class="card-title" style="font-size: 26px;">Kenali Tanda Anabul Kesayanganmu Sedang Sakit</h2>
            </div>
            <div class="card-info" style="bottom: 108px; top: auto; right: 72px;">
                <div class="trust-element"><i class="fa-solid fa-pen"></i> detikHealth · 1 hari lalu</div>
                <p class="story-text">Kucing pandai menyembunyikan rasa sakit. Waspadai kehilangan nafsu makan dan perilaku sering bersembunyi.</p>
                <a href="#" class="cta-link">Baca panduan lengkapnya <i class="fa-solid fa-arrow-right"></i></a>
            </div>"""

html = html.replace(OLD_C14, NEW_C14)

# ============================================================
# CARD 7: Polling — keep title at top, poll at mid, source at bottom
# ============================================================
# Polling card already has its own special structure (top: 100px), leave mostly as-is
# but adjust bottom. Currently bottom is handled by card-info top:100px.
# We just need to make sure it still works with the new pill nav.
# The existing style="bottom: auto; top: 100px;" doesn't conflict.

# ============================================================
# Also fix CSS: default .card-info bottom now needs to NOT override the inline styles
# Prepend a note-worthy override removal
# ============================================================
# Remove "!important" on card-info bottom from pill upgrade CSS
html = html.replace(
    '        .card-info { bottom: 108px !important; }',
    '        /* card-info bottom handled per-card inline */'
)
html = html.replace(
    '        .right-actions { bottom: 108px !important; }',
    '        .right-actions { bottom: 108px; }'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Layout restructured! All cards now follow 'title top + caption bottom' pattern.")
