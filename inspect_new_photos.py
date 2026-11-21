import os
from PIL import Image

photo_dir = "photoes"
files = [f for f in os.listdir(photo_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

file_info = []
for f in files:
    full_path = os.path.join(photo_dir, f)
    mtime = os.path.getmtime(full_path)
    try:
        with Image.open(full_path) as im:
            w, h = im.size
            ratio = round(w / h, 2)
    except Exception as e:
        w, h, ratio = 0, 0, 0
    file_info.append((mtime, f, w, h, ratio))

# Sort by modification time
file_info.sort(key=lambda x: x[0])

print(f"Total photos: {len(file_info)}")
for i, (mtime, f, w, h, ratio) in enumerate(file_info):
    import datetime
    dt = datetime.datetime.fromtimestamp(mtime).strftime('%H:%M:%S')
    print(f"{i+1:02d} | {dt} | {f} | {w}x{h} (ratio {ratio})")
