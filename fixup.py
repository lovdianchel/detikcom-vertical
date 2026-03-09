import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's fix the HTML structure at the end
# The user issue: "Saya malah tidak suka desain live report yang sekarang!" -> Let's change back to horizontal line but make it premium as per the first revision, or just plain and clean. Wait, I already made it vertical minimalist. Let's make it more solid if that's what they mean or change back to horizontal with better padding.

# And "Saya ingin ada beberapa foto yang jadi 9:16. Dan contoh 1 foto yang formatnya 5:4/4:3" -> Card 8 Enjoyment is 9:16 using format-9-16. Card 12 Wali is 5:4 or 3:4. 

# Let's just use regex to clean the end up to bottom nav.
m = re.search(r'(<!-- CARD 8: Enjoyment -->.*?</div>\s*</div>\s*</div>)', text, re.DOTALL)
if m:
    card8 = m.group(1)
    text = text[:m.start()] + card8 + '\n\n    <!-- BOTTOM NAV -->' + text[text.find('<nav id="bottomnav">'):]


# Let's also fix the Media Alignment for 5:4 / 4:3!
text = text.replace('.format-3-4 { \n            width: 100%; \n            height: auto; \n            aspect-ratio: 3/4; \n            max-width: min(85vw, 60vh); \n            object-fit: cover; \n            margin-top: 15dvh; /* Force alignment towards top */\n        }',
                    '.format-3-4 { \n            width: 100%; \n            height: auto; \n            aspect-ratio: 3/4; \n            max-width: min(85vw, 60vh); \n            object-fit: cover; \n            margin-top: 10dvh; \n        }')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
