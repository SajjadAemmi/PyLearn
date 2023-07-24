import cv2 as cv
import numpy as np
import os

img = cv.imread('hw6/ocr3.jpg')

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, img = cv.threshold(img,127, 255, cv.THRESH_BINARY)

img = 255 - img

number_of_files = 0

os.mkdir('hw6/lines/')

i = 0
while i < img.shape[0]:
    if not all(img[i, j] == 0 for j in range(img.shape[1])):
        row1 = i
        for k in range(i + 1, img.shape[0]):
            if all(img[k, j] == 0 for j in range(img.shape[1])):
                row2 = k
                cv.imwrite('hw6/lines/' + str(number_of_files) + '.jpg', img[row1: row2, :])
                number_of_files += 1
                i = row2
                break
    i += 1

for index in range(number_of_files):
    os.mkdir('hw6/lines/character' + str(index))

for index in range(number_of_files):

    img = cv.imread('hw6/lines/character' + str(index) + '.jpg')

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    _, img = cv.threshold(img,127, 255, cv.THRESH_BINARY)

    # img = 255 - img

    i = 0
    while i < img.shape[1]:
        if not all(img[j, i] == 0 for j in range(img.shape[0])):
            col1 = i
            for k in range(i + 1, img.shape[1]):
                if all(img[j, k] == 0 for j in range(img.shape[0])):
                    col2 = k
                    cv.imwrite('hw6/lines/' + str(index) + '/' + str(i) + '.jpg', img[:, col1:col2])
                    i = col2
                    break
        i += 1

# cv.imshow('test', img)
cv.waitKey()