import cv2
from ultralytics import YOLO
from deep_text_recognition_benchmark.dtrb import DTRB


plate_detector = YOLO("weights/yolov8-detector/yolov8-s-license-plate-detector.pt")
plate_recognizer = DTRB("weights/dtrb-recognizer/dtrb-None-VGG-BiLSTM-CTC-license-plate-recognizer.pth")

image = cv2.imread("io/input/IMG_5178.JPG")
results = plate_detector.predict(image)
for result in results:
    for i in range(len(result.boxes.xyxy)):
        if result.boxes.conf[i] > 0.7:
            bbox_tensor = result.boxes.xyxy[i]
            bbox_ndarray = bbox_tensor.cpu().detach().numpy().astype(int)
            print(bbox_ndarray)
            x1, y1, x2, y2 = bbox_ndarray
            plate_image = image[y1:y2, x1:x2].copy()

            cv2.imwrite(f"io/output/plate_image_result_{i}.jpg", plate_image)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 4)
            
            plate_image = cv2.resize(plate_image, (100, 32))
            plate_image = cv2.cvtColor(plate_image, cv2.COLOR_BGR2GRAY)
            plate_recognizer.predict(plate_image)

cv2.imwrite("io/output/image_result.jpg", image)
