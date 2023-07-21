import cv2 as cv
import numpy as np

img = cv.imread('game.JPG')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
res = cv.equalizeHist(img)
cv.imwrite('sudoku.JPG', res)

r1 = 0
c1 = 0

# ---------- cropped left and bottom white space ----------
image = cv.imread('sudoku.JPG')
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

flag = False

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i, j] == 0:
            c1 = j
            r1 = i
            flag = True
            break

    if flag == True:
        break

# ---------- cropped right and top white space ----------

flag = False

for i in range(image.shape[0] - 1, 0, -1):
    for j in range(image.shape[1] - 1, 0, -1):
        if image[i, j] == 0:
            c2 = j
            r2 = i
            flag = True
            break

    if flag == True:
        break


image = image[r1:r2, c1:c2]
cv.imwrite('crop2_img.JPG', image)

# ---------- fill white space with black color ----------

print(image.shape)

mini_row = image.shape[0] // 9
mini_col = image.shape[1] // 9

count_i = 0
for i in range(0, image.shape[0], mini_row):
    count_j = 0
    for j in range(0, image.shape[1], mini_col):
        mini_image = image[i: i + mini_row, j:j + mini_col]

        count_white = np.count_nonzero(mini_image)
        count_total = mini_image.shape[0] * mini_image.shape[1]
        count_black = count_total - count_white

        if count_black > 3200:  #  this cell is filled
            cv.imwrite(str(i) + str(j) + '.jpg', mini_image)

        count_j += 1
        if count_j >= 9:
            break

    count_i += 1
    if count_i >= 9:
        break

cv.waitKey()
