import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix image name
text = text.replace('ilustrasi-kucing-tidak-sehat.jpeg', 'Kucing.jpeg')

# Fix missing #feed closing div
if '</div>\n    <!-- BOTTOM NAV -->' not in text:
    text = text.replace('    <!-- BOTTOM NAV -->', '    </div>\n    <!-- BOTTOM NAV -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
