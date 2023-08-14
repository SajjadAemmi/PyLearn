import cv2
import time
import argparse
import numpy as np
import tensorflow as tf
from mtcnn_face_detector import face_detect

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input video path', default='input/kim.mp4', type=str)
parser.add_argument('--output', help='output video path', default='output/result.mp4', type=str)
parser.add_argument('--detection-threshold', help='detection confidence threshold', default=0.95, type=float)
parser.add_argument('--recognition-threshold', help='recognition confidence threshold', default=0.9, type=float)
args = parser.parse_args()

model = tf.keras.models.load_model('saved_model')
names = ['Ali-Khamenei', 'Angelina-Jolie', 'Barak-Obama', 'Behnam-Bani',
         'Donald-Trump', 'Emma-Watson', 'Han-Hye-Jin', 'Kim-Jong-Un',
         'Leyla-Hatami', 'Lionel-Messi', 'Michelle-Obama', 'Morgan-Freeman',
         'Queen-Elizabeth', 'Scarlett-Johansson']

video = cv2.VideoCapture(args.input)
width, height = video.get(cv2.CAP_PROP_FRAME_WIDTH), video.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = video.get(cv2.CAP_PROP_FPS)
video_writer = cv2.VideoWriter(args.output, cv2.VideoWriter_fourcc(*'mp4v'),
                               float(fps), (int(width), int(height)))

while True:
    ret, frame = video.read()

    if ret == False:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    start_time = time.time()
    faces = face_detect(frame_rgb, args.detection_threshold)
    print('detection time:', time.time() - start_time)

    for (x, y, a) in faces:
        cv2.rectangle(frame, (x, y), (x + a, y + a), (255, 0, 0), 4)

        img_face = frame_rgb[y:y + a, x:x + a].copy()
        img_face = cv2.resize(img_face, (224, 224))
        img_face = img_face / 255.0
        img_face = img_face.reshape(1, 224, 224, 3)

        result = model.predict(img_face)
        index = np.argmax(result)
        confidence = np.max(result)

        if confidence >= args.recognition_threshold:
            cv2.putText(frame, names[index], (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
            print(names[index], confidence)

    cv2.imshow('result', frame)
    video_writer.write(frame)

    ch = cv2.waitKey(1)
    if ch == 27 or ch == ord('q') or ch == ord('Q'):
        break

video.release()
video_writer.release()
