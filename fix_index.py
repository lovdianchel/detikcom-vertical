import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Media Styling for videos 3:4, 5:4, 16:9 to be perfectly centered and responsive
# and remove position: absolute for format to make them not squished.
css_media_old = """        .media-item {
            width: 100%;
            height: auto;
            max-height: 80vh;
            object-fit: cover;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.8);
        }
        .format-3-4 { aspect-ratio: 3 / 4; width: 95%; max-width: 400px; }
        .format-5-4 { aspect-ratio: 5 / 4; width: 95%; max-width: 450px; }
        .format-16-9 { aspect-ratio: 16 / 9; width: 100%; border-radius: 0; }"""

css_media_new = """        .media-item {
            width: 100%;
            height: auto;
            max-height: 80dvh;
            object-fit: contain; /* containment to fit box without meslek */
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.8);
            background: #000;
        }
        /* Adjusted specifically to force the exact aspect ratio while containing image/video */
        .format-3-4 { aspect-ratio: 3 / 4; max-width: 90%; }
        .format-5-4 { aspect-ratio: 5 / 4; max-width: 95%; }
        .format-16-9 { aspect-ratio: 16 / 9; max-width: 100%; border-radius: 0; border: none; }"""
html = html.replace(css_media_old, css_media_new)


# 2. Add New Photos (Using UMP and Kucing)
new_cards = """
        <!-- CARD 14: Story Mode 2 -->
        <div class="card" data-id="14">
            <img src="ilustrasi-kucing-tidak-sehat.jpeg" class="bg-image" style="opacity: 0.6;">
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

# Insert new card before Enjoyment (CARD 8 is enjoyment, wait, I think UMP was added to CARD 6 already. We can add to end of feed)
# We need to find the specific enjoyment end tag or just insert before </feed>
# Actually CARD 8 is Enjoyment. Let's find exactly where CARD 8 ends and Add 14 below it
html = html.replace('<!-- BOTTOM NAV -->', new_cards + '\n    <!-- BOTTOM NAV -->')

# Let's write it back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
