import os
import cv2
import numpy as np


images_path = os.listdir("input/galaxy")
images = []
for image_path in images_path:
    image = cv2.imread("input/galaxy/" + image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image.astype(np.float32)
    images.append(image)

result = np.zeros(image.shape)

for image in images:
    result += image

result = result / len(images)
result = result.astype(np.uint8)
cv2.imwrite("output/good_galaxy.jpg", result)
