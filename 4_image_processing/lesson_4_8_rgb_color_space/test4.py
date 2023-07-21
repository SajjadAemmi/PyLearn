# convert jpg image to png image with transparent background in opencv

import cv2
import numpy as np

img = cv2.imread('input/mandrill.jpg')
# convert to png image with transparent background
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
# set alpha to 0
img[10:40, 10:40, 3] = 0
cv2.imwrite('mandrill.png', img)
