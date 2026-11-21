import os
import datetime

files = sorted([f for f in os.listdir("photoes") if f.lower().endswith(".jpg")], key=lambda f: os.path.getmtime(os.path.join("photoes", f)))

for i, f in enumerate(files):
    mtime = os.path.getmtime(os.path.join("photoes", f))
    dt = datetime.datetime.fromtimestamp(mtime).strftime('%H:%M:%S')
    print(f"{i+1:02d}: {f} ({dt})")
