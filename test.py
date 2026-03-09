import re

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Make double sure media-items are not stretched on Safari/iOS
new = orig.replace('.media-item {\n            width: 100%;\n            height: auto;\n            max-height: 80dvh;\n            object-fit: contain; /* containment to fit box without meslek */\n            border-radius: 12px;\n            box-shadow: 0 4px 20px rgba(0,0,0,0.8);\n            background: #000;\n        }',
                   '.media-item {\n            max-width: 100%;\n            max-height: 80dvh;\n            object-fit: contain;\n            border-radius: 12px;\n            box-shadow: 0 4px 20px rgba(0,0,0,0.8);\n            background: #000;\n            display: block;\n            margin: 0 auto;\n        }')

# Also fix format classes to explicitly disable forced stretching if that's what's causing the meslek
new = new.replace('.format-3-4 { aspect-ratio: 3 / 4; max-width: 90%; }', '.format-3-4 { aspect-ratio: 3 / 4; max-width: 90%; height: auto; }')
new = new.replace('.format-5-4 { aspect-ratio: 5 / 4; max-width: 95%; }', '.format-5-4 { aspect-ratio: 5 / 4; max-width: 95%; height: auto; }')
new = new.replace('.format-16-9 { aspect-ratio: 16 / 9; width: 100%; height: auto; border-radius: 0; border: none; }', '.format-16-9 { width: 100%; height: auto; object-fit: contain; border-radius: 0; border: none; }')

# Fix background of Live Report to be solid and nice, remove old bg-overlay if it's there
# Actually we updated CARD 5 Live Report, let's make sure it's good

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new)
