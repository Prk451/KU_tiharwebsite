from PIL import Image
import numpy as np

files = [
    ("29 (Day 03)", "Gemini_Generated_Image_8dl4c88dl4c88dl4.jpg"),
    ("30 (Day 03)", "Gemini_Generated_Image_bs0nvgbs0nvgbs0n.jpg"),
    ("31 (Day 04)", "Gemini_Generated_Image_rozjmarozjmarozj.jpg"),
    ("32 (Day 04)", "Gemini_Generated_Image_bx55ccbx55ccbx55.jpg"),
    ("33 (Day 05)", "Gemini_Generated_Image_sh44v4sh44v4sh44.jpg"),
]

for label, f in files:
    path = f"photoes/{f}"
    im = Image.open(path)
    arr = np.array(im)
    # mean RGB
    r, g, b = arr[:, :, 0].mean(), arr[:, :, 1].mean(), arr[:, :, 2].mean()
    # dominant colors or brightness
    print(f"{label} | {f} | {im.size} | Mean RGB: ({r:.1f}, {g:.1f}, {b:.1f})")
