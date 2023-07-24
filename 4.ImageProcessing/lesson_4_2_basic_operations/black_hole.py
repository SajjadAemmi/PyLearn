import cv2 as cv
import numpy as np

images = [[0 for i in range(5)] for j in range(4)]

for i in range(4):
    for j in range(5):
        images[i][j] = cv.imread(str(i + 1) + '/' + str(j + 1) + '.jpg')
        images[i][j] = cv.cvtColor(images[i][j], cv.COLOR_BGR2GRAY)

image_without_noise = [0 for i in range(4)]

for i in range(4):
    for j in range(5):
        image_without_noise[i] = image_without_noise[i] + (images[i][j] / 5)

final_image = np.zeros((2000, 2000), dtype=np.uint8)

final_image[0:1000, 0:1000] = image_without_noise[0]
final_image[0:1000, 1000:2000] = image_without_noise[1]
final_image[1000:2000, 0:1000] = image_without_noise[2]
final_image[1000:2000, 1000:2000] = image_without_noise[3]

cv.imshow('Final Image', final_image)

cv.imwrite('final_image.jpg', final_image)

cv.waitKey()
