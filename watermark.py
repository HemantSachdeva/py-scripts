#!/usr/bin/env python3

import sys
try:
    import cv2
    import numpy as np
except ImportError:
    print("Couldn't import modules")
    sys.exit(1)

# read image
img = cv2.imread('img/pic.jpg')
mark = cv2.imread('img/watermark.png')

m, n = img.shape[:2]

# create overlay image with watermark on upper left corner
overlay = np.zeros_like(img, dtype='uint16')
overlay[:mark.shape[0], :mark.shape[1]] = mark

# add images and clip to avoid uint8 wrapping
marked = np.array(np.clip(img+overlay, 0, 255), dtype='uint8')

# add some text of 5 pixels on bottom left
cv2.putText(marked, 'Shot on Laurel Sprout', (5, m-5),
            cv2.FONT_HERSHEY_PLAIN, fontScale=1.0, color=(255, 255, 255))

cv2.imshow('Original Image', img)
cv2.imshow('Watermarked', marked)
cv2.imwrite('img/watermarked.jpg', marked)
cv2.waitKey(0)
cv2.destroyAllWindows()
