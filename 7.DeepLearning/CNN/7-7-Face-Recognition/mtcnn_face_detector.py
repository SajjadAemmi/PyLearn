from mtcnn.mtcnn import MTCNN

detector = MTCNN()


def face_detect(image, threshold=0.9):
    faces = detector.detect_faces(image)
    results = []

    for face in faces:
        if face['confidence'] >= threshold:
            bounding_box = face['box']

            x = bounding_box[0]
            y = bounding_box[1]
            w = bounding_box[2]
            h = bounding_box[3]

            a = max(w, h)
            center_x = x + w // 2
            center_y = y + h // 2
            x = center_x - a // 2
            y = center_y - a // 2

            results.append([x, y, a])

    return results
