import cv2


image = cv2.imread("input/sajjad.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_gray_inverted = 255 - image_gray
image_gray_inverted_blurred = cv2.GaussianBlur(image_gray_inverted, (21, 21), sigmaX=0, sigmaY=0)
image_gray_blurred = 255 - image_gray_inverted_blurred
image_sketch = (image_gray / image_gray_blurred) * 255

cv2.imwrite("result.jpg", image_sketch)
