import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

css_media_old = """        .media-item {
            max-width: 100%;
            max-height: 80dvh;
            object-fit: contain;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.8);
            background: #000;
            display: block;
            margin: 0 auto;
        }
        /* Adjusted specifically to force the exact aspect ratio while containing image/video */
        .format-3-4 { width: auto; height: 100%; aspect-ratio: 3/4; max-height: 80vh; max-width: 95vw; object-fit: contain; }
        .format-5-4 { width: auto; height: 100%; aspect-ratio: 5/4; max-height: 80vh; max-width: 95vw; object-fit: contain; }
        .format-16-9 { width: 100vw; height: auto; aspect-ratio: 16/9; max-height: 100vh; object-fit: contain; border-radius: 0; border: none; }"""

css_media_new = """        .media-item {
            max-width: 100%;
            max-height: 80dvh;
            object-fit: contain;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.8);
            background: #000;
            display: block;
            margin: 0 auto;
        }
        /* Forcing strictly correct aspect ratios with contain */
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
        
html = html.replace(css_media_old, css_media_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
