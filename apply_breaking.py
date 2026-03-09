import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('https://akcdn.detik.net.id/visual/2023/10/08/serangan-hamas-ke-israel-3_169.jpeg?w=650', 'Kondisi Terkini (breaking news).jpeg')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
