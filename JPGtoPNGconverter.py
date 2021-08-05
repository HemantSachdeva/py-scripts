import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
out_folder = sys.argv[2]

# create out/ if does not exists
if not os.path.exists(out_folder):
    os.makedirs(out_folder)

# loop into the out/ and convert jpg to png
for file in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{file}')
    filename = os.path.splitext(file)[0]
    img.save(f'{out_folder}{filename}.png', 'png')
    print(f'{image_folder}{filename}.jpg saved to {out_folder}{filename}.png')
