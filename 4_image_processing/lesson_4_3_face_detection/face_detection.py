import random
import cv2

image = cv2.imread("parstech.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_sticker_red = cv2.imread("sticker-red.png")
image_sticker_green = cv2.imread("sticker-green.png")
image_sticker_spongebob = cv2.imread("spongebob.jpg")
stickers = [image_sticker_red, image_sticker_green, image_sticker_spongebob]

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
faces = face_detector.detectMultiScale(image_gray, 1.3)
for face in faces:
    x, y, w, h = face
    # cv2.rectangle(image, [x, y], [x+w, y+h], [0,0,0], 8)
    sticker = cv2.resize(random.choice(stickers), [w, h])
    image[y:y+h , x:x+w] = sticker

cv2.imshow("result", image)
cv2.waitKey()

cv2.imwrite("output.jpg", image)