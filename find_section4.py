with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'SECTION 04' in l or 'Carry the Light Beyond Tonight' in l or 'tihar-studio' in l:
        print(f'{i+1}: {l.strip()[:100]}')
