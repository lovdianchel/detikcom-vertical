import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure we don't have stray object-fit: cover for the generic video tag if that's what's causing meslek
# Wait, we changed video:not(.media-item) to be cover, which is fine for background videos like CARD 2
html = html.replace('video:not(.media-item) {\n            width: 100%;\n            height: 100%;\n            object-fit: cover;', 
                    'video:not(.media-item) {\n            width: 100%;\n            height: 100%;\n            object-fit: contain;')

# Ensure horizontal 16:9 video is fully responsive and vertically centered without stretching
# For formatting 16:9, we remove max-width 100% since width is already 100% 
html = html.replace('.format-16-9 { aspect-ratio: 16 / 9; max-width: 100%; border-radius: 0; border: none; }',
                    '.format-16-9 { aspect-ratio: 16 / 9; width: 100%; height: auto; border-radius: 0; border: none; }')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
