import cv2


def dodge(x,y):
    return cv2.divide(x, 255-y, scale=256)


def burn(image, mask):
    return 255 - cv2.divide(255-image, 255-mask, scale=256)


def image2pencilSketch(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_gray_inv = 255 - image_gray
    image_gray_inv_blur = cv2.GaussianBlur(image_gray_inv, (21, 21), sigmaX=0, sigmaY=0)
    image_dodged = dodge(image_gray, image_gray_inv_blur)
    image_result = burn(image_dodged, image_gray_inv_blur)
    return image_result


if __name__ == "__main__":
    image = cv2.imread("input/sajjad.jpg")
    result = image2pencilSketch(image)
    cv2.imwrite("result.jpg", result)
