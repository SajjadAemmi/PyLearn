import cv2

image1 = cv2.imread("input/e.tif", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("input/f.tif", cv2.IMREAD_GRAYSCALE)

result = image1 / image2

cv2.imshow("result", result)
cv2.waitKey()
