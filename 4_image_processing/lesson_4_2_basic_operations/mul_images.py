import cv2
import numpy as np

image_dandoon = cv2.imread("input/c.tif")
image_mask = cv2.imread("input/d.tif")

image_dandoon = cv2.cvtColor(image_dandoon, cv2.COLOR_BGR2GRAY)
image_mask = cv2.cvtColor(image_mask, cv2.COLOR_BGR2GRAY)

image_mask = image_mask / 255.0

# result = image_dandoon * image_mask
result = cv2.multiply(image_dandoon, image_mask)

cv2.imwrite("output/new_dandoon.jpg", result)
