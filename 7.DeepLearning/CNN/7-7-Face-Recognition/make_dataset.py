import cv2
import os
from mtcnn.mtcnn import MTCNN
from tqdm import tqdm

detector = MTCNN()

origin_directory = '7-7 dataset'
destination_directory = '7-7 dataset - faces'

for dir in tqdm(os.listdir(origin_directory)):
    if not os.path.exists(os.path.join(destination_directory, dir)):
        os.makedirs(os.path.join(destination_directory, dir))

    for file in os.listdir(os.path.join(origin_directory, dir)):
        try:
            image = cv2.imread(os.path.join(origin_directory, dir, file))
            results = detector.detect_faces(image)

            for index, result in enumerate(results):
                bounding_box = result['box']

                x = bounding_box[0]
                y = bounding_box[1]
                w = bounding_box[2]
                h = bounding_box[3]

                a = max(w, h)
                center_x = x + w // 2
                center_y = y + h // 2
                x = center_x - a // 2
                y = center_y - a // 2

                img_face = image[y:y + a, x:x + a]
                if img_face.shape[0] > 0 and img_face.shape[1] > 0:
                    cv2.imwrite(os.path.join(destination_directory, dir, str(index) + file), img_face)
        except Exception as e:
            print(e)
