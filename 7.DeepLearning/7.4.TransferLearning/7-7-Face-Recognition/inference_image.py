import cv2
import time
import argparse
import numpy as np
import tensorflow as tf
from mtcnn_face_detector import face_detect


parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input image path', default='input/Khamenei_And_Soleimani.jpg', type=str)
parser.add_argument('--output', help='output image path', default='output/Khamenei_And_Soleimani.jpg', type=str)
parser.add_argument('--detection-threshold', help='detection confidence threshold', default=0.95, type=float)
parser.add_argument('--recognition-threshold', help='recognition confidence threshold', default=0.9, type=float)
args = parser.parse_args()

model = tf.keras.models.load_model('saved_model')
names = ['Ali-Khamenei', 'Angelina-Jolie', 'Barak-Obama', 'Behnam-Bani',
         'Donald-Trump', 'Emma-Watson', 'Han-Hye-Jin', 'Kim-Jong-Un',
         'Leyla-Hatami', 'Lionel-Messi', 'Michelle-Obama', 'Morgan-Freeman',
         'Queen-Elizabeth', 'Scarlett-Johansson']

image = cv2.imread(args.input)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

start_time = time.time()
faces = face_detect(image_rgb, args.detection_threshold)
print('detection time:', time.time() - start_time)

for (x, y, a) in faces:
    cv2.rectangle(image, (x, y), (x + a, y + a), (255, 0, 0), 4)

    img_face = image_rgb[y:y + a, x:x + a].copy()
    img_face = cv2.resize(img_face, (224, 224))
    img_face = img_face / 255.0
    img_face = img_face.reshape(1, 224, 224, 3)

    start_time = time.time()
    result = model.predict(img_face)
    print('recognition time:', time.time() - start_time)

    index = np.argmax(result)
    confidence = np.max(result)

    if confidence >= args.recognition_threshold:
        cv2.putText(image, names[index], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255))
        print(names[index], confidence)

cv2.imwrite(args.output, image)
cv2.imshow('result', image)
cv2.waitKey()
