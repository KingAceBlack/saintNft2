import os
from PIL import Image

# Threshold for what counts as "black"
THRESHOLD = 30

# Loop through all image files in the current folder
for filename in os.listdir("."):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        print(f"[PROCESSING] {filename} ...")

        # Open image
        img = Image.open(filename).convert("RGBA")
        datas = img.getdata()

        new_data = []
        for item in datas:
            # If pixel is black (R,G,B all near 0)
            if item[0] < THRESHOLD and item[1] < THRESHOLD and item[2] < THRESHOLD:
                # Make transparent
                new_data.append((0, 0, 0, 0))
            else:
                new_data.append(item)

        img.putdata(new_data)

        # Overwrite original image
        img.save(filename)
        print(f"[OK] Background removed -> {filename}")

print("[DONE] All images processed.")


