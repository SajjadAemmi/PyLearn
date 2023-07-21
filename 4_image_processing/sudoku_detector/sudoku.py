import argparse
import cv2
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(description="Sajjad Sudoku Detector v1.0")

parser.add_argument("--input", type=str, help="path of your input image")
parser.add_argument("--filter-size", type=int, help="size of GaussianBlur mask", default=7)
parser.add_argument("--output", type=str, help="path of your output image")

args = parser.parse_args()

img = cv2.imread(args.input)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_blurred = cv2.GaussianBlur(img_gray, (args.filter_size, args.filter_size), 3)
thresh = cv2.adaptiveThreshold(img_blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
thresh = cv2.bitwise_not(thresh)

contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0]
contours = sorted(contours, key=cv2.contourArea, reverse=True)

sudoku_contour = None

for contour in contours:
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    if len(approx) == 4:
        sudoku_contour = approx
        break

if sudoku_contour is None:
    print("شرمنده داداش. جدول سودوکو رو نتونستم واست پیدا کنم")

else:
    result = cv2.drawContours(img, [sudoku_contour], -1, (0, 255, 0), 20)
    plt.imshow(result)
    cv2.imwrite(args.output, result)
