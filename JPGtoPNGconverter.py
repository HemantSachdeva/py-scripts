#!/usr/bin/env python3

import sys
import os
# Project did not have requirements, explicitly check for each import.
try:
    from PIL import Image
except Exception as E:
    print(f"Error while importing Image from PIL\n\n{E}")
    exit(1)

# Check first and second args
try:
    image_folder = sys.argv[1]
    out_folder = sys.argv[2]
except:
    print("Please input argument before proceeding")
    sys.exit(1)

# create out/ if does not exists
if not os.path.exists(out_folder):
    os.makedirs(out_folder)

# loop into the out/ and convert jpg to png
for file in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{file}')
    filename = os.path.splitext(file)[0]
    img.save(f'{out_folder}{filename}.png', 'png')
    print(f'{image_folder}{filename}.jpg saved to {out_folder}{filename}.png')
