import os
from PIL import Image

photo_dir = "photoes"
files = [
    "Gemini_Generated_Image_8dl4c88dl4c88dl4.jpg",
    "Gemini_Generated_Image_bs0nvgbs0nvgbs0n.jpg",
    "Gemini_Generated_Image_rozjmarozjmarozj.jpg",
    "Gemini_Generated_Image_bx55ccbx55ccbx55.jpg",
    "Gemini_Generated_Image_sh44v4sh44v4sh44.jpg"
]

for f in files:
    path = os.path.join(photo_dir, f)
    with Image.open(path) as im:
        print(f"File: {f}")
        print(f"  Format: {im.format}, Size: {im.size}, Mode: {im.mode}")
        info = im.info
        print(f"  Info keys: {list(info.keys())}")
        if 'exif' in info:
            print("  Has exif")
