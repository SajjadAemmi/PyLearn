import cv2
import matplotlib.pyplot as plt

# image = cv2.imread("input/polar_bear.jpeg", cv2.IMREAD_GRAYSCALE)
# image = cv2.imread("input/batman.jpeg", cv2.IMREAD_GRAYSCALE)
image = cv2.imread("input/funny_lion.jpg", cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.plot(hist)
plt.show()
# print(hist.astype(int))