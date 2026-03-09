import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Restore original Live Report CSS since user hated it
clean_live = """        /* Clean minimal Live Report */
        .live-updates {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-top: 16px;
            max-height: 250px;
            overflow-y: scroll;
            padding-right: 8px;
        }

        .update-card {
            border-left: 2px solid var(--detik-blue);
            padding-left: 12px;
            position: relative;
        }
        
        .update-card::before {
            content: '';
            position: absolute;
            left: -5px;
            top: 0;
            width: 8px;
            height: 8px;
            background: var(--detik-blue);
            border-radius: 50%;
        }

        .update-time {
            font-size: 12px;
            color: #ccc;
            font-weight: bold;
            margin-bottom: 4px;
        }

        .update-text {
            font-size: 14px;
            line-height: 1.4;
            color: #eee;
        }"""

orig_live = """        /* Live Report horizontal slide */
        .live-updates {
            display: flex;
            overflow-x: scroll;
            scroll-snap-type: x mandatory;
            gap: 12px;
            margin-top: 12px;
            padding-bottom: 8px;
            scrollbar-width: none;
        }

        .live-updates::-webkit-scrollbar {
            display: none;
        }

        .update-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 8px;
            padding: 12px;
            flex: 0 0 85%;
            scroll-snap-align: start;
        }

        .update-time {
            font-size: 11px;
            color: var(--detik-blue);
            font-weight: 700;
            margin-bottom: 4px;
        }

        .update-text {
            font-size: 13px;
            line-height: 1.4;
        }"""

text = text.replace(clean_live, orig_live)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

