import cv2
import numpy as np


image_sajjad = cv2.imread("input/sajjad.jpg")
image_lion = cv2.imread("input/lion.jpg")

image_sajjad = cv2.cvtColor(image_sajjad, cv2.COLOR_BGR2GRAY)
image_lion = cv2.cvtColor(image_lion, cv2.COLOR_BGR2GRAY)

# result = image_sajjad + image_lion
# result = cv2.add(image_sajjad, image_lion)

image_sajjad = image_sajjad.astype(np.float32)
image_lion = image_lion.astype(np.float32)

result = (image_sajjad*3/4 + image_lion*1/4)
result = result.astype(np.uint8)

cv2.imwrite("output/result2.jpg", result)
