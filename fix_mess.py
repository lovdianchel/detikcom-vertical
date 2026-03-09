import re

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Clean up broken tags at the end
start_marker = '<div class="trust-element"><i class="fa-solid fa-pen"></i> detikHealth'
end_marker = '<div class="action-icon"><i class="fa-solid fa-share"></i></div><span class="action-text">Share</span>\n                </button>\n            </div>'

if start_marker in orig:
    bad_part_start = orig.rfind('    </div>\n\n    \n        \n                <div class="trust-element">')
    if bad_part_start == -1:
        bad_part_start = orig.find(start_marker) - 100
    
    bad_part_end = orig.find(end_marker, bad_part_start) + len(end_marker) + 10
    # Actually let's just use regex to clean up everything between </div>\n    </div>\n\n  and <!-- BOTTOM NAV -->
    
    orig = re.sub(r'    </div>\n\n    \n        \n                <div class="trust-element">.*?<!-- BOTTOM NAV -->', '\n    <!-- BOTTOM NAV -->', orig, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(orig)

