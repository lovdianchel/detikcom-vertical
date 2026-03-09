import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure to replace object-fit: contain so horizontal video isn't squished!
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
        }
        /* Adjusted specifically to force the exact aspect ratio while containing image/video */
        .format-3-4 { aspect-ratio: 3 / 4; max-width: 90%; }
        .format-5-4 { aspect-ratio: 5 / 4; max-width: 95%; }
        .format-16-9 { aspect-ratio: 16 / 9; max-width: 100%; border-radius: 0; border: none; }"""

# If the first string didn't match perfectly, let's fix it manually

if 'object-fit: cover;' in html and '.format-3-4' in html:
    new_html = html.replace('object-fit: cover;', 'object-fit: contain;')
    new_html = new_html.replace('aspect-ratio: 3 / 4; width: 95%; max-width: 400px;', 'aspect-ratio: 3 / 4; width: 95%; max-width: 450px;')
    new_html = new_html.replace('aspect-ratio: 16 / 9; width: 100%; border-radius: 0;', 'aspect-ratio: 16 / 9; width: 100%; border-radius: 0; border: none;')
    html = new_html

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
