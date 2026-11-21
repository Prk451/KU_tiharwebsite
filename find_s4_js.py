with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if any(k in l for k in ['releaseLanternBtn', 'deusiLoopBtn', 'postcardPreview', 'finale-studio']):
        print(f'{i+1}: {l.strip()[:100]}')
