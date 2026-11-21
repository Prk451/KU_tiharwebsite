import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. 14 Chapters in Story
chapters = re.findall(r'<article class="codex-chapter[^"]*"[^>]*data-index="(\d+)"[^>]*>(.*?)</article>', text, re.DOTALL)
print(f"Total Chapters found: {len(chapters)}")

slots = []

for idx, ch_body in chapters:
    ch_num = int(idx) + 1
    # title
    title_m = re.search(r'<h2 class="ch-giant-title">(.*?)</h2>', ch_body, re.DOTALL)
    title = re.sub(r'<[^>]+>', ' ', title_m.group(1)).strip() if title_m else ""
    # kicker
    kicker_m = re.search(r'<span class="ch-kicker">(.*?)</span>', ch_body, re.DOTALL)
    kicker = re.sub(r'<[^>]+>', ' ', kicker_m.group(1)).strip() if kicker_m else ""
    # narrative / poetry
    narrative_m = re.search(r'<p class="ch-micro-poetry">(.*?)</p>', ch_body, re.DOTALL)
    narrative = re.sub(r'<[^>]+>', ' ', narrative_m.group(1)).strip() if narrative_m else ""
    
    # images in this chapter
    img_matches = re.findall(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]+)"[^>]*>', ch_body)
    for i, (src, alt) in enumerate(img_matches):
        role = "Main Full-Bleed" if i == 0 and len(img_matches) == 1 else f"Image {i+1}"
        slots.append({
            'section': f'Plate {ch_num:02d}: {title}',
            'role': role,
            'kicker': kicker,
            'narrative': narrative,
            'current_src': src,
            'alt': alt
        })

# 2. 5 Days
days = re.findall(r'<article class="tihar-day-page[^"]*"[^>]*data-day-index="(\d+)"[^>]*>(.*?)</article>', text, re.DOTALL)
print(f"Total Days found: {len(days)}")

for idx, day_body in days:
    day_num = int(idx) + 1
    title_m = re.search(r'<h2 class="day-giant-title">(.*?)</h2>', day_body, re.DOTALL)
    title = re.sub(r'<[^>]+>', ' ', title_m.group(1)).strip() if title_m else ""
    img_matches = re.findall(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]+)"[^>]*>', day_body)
    for i, (src, alt) in enumerate(img_matches):
        role = "Main Artwork" if "custom-day-img" in day_body else f"Slot {i+1}"
        slots.append({
            'section': f'Day {day_num:02d}: {title}',
            'role': f'Day {day_num} Image {i+1}',
            'kicker': f'Day {day_num}',
            'narrative': '',
            'current_src': src,
            'alt': alt
        })

print(f"\nTotal Image Slots across site: {len(slots)}")
for s in slots:
    print(f"[{s['section']}] ({s['role']}) -> {s['current_src'].split('/')[-1]}")
