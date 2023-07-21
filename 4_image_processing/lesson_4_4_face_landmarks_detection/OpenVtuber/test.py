import cv2
import numpy as np

image = np.zeros((300, 400), dtype=np.uint8)

points = np.array([[50, 50],
                   [250, 50],
                   [250, 250],
                   [50, 250]], dtype=int)

cv2.drawContours(image, [points], -1, (255, 255, 255), -1)

cv2.imshow("result", image)
cv2.waitKey()
