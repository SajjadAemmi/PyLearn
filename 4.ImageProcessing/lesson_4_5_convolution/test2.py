import numpy as np
import cv2
import matplotlib.pyplot as plt 


# image = np.array([[9, 7, 255, 0],
#                   [10, 10, 10, 0],
#                   [254, 0, 1, 1],
#                   [5, 6, 7, 8]], dtype=np.uint8)

image = cv2.imread("")

histogram = []

for ...
    histogram.append()

# histogram
# 0: 3
# 1: 2
# 2: 0
# 3: 0
# 4: 0
# 5: 1
# 6: 1
# 7: 2
...
# 253: 0
# 254: 1
# 255: 1

cv2.imwrite("output/result8.jpg", image)

plt.plot(histogram)
plt.show()
