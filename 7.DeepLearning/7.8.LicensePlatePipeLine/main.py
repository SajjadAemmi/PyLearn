# from ultralytics import YOLO
from deep_text_recognition_benchmark.dtrb import DTRB

# plate_detector = YOLO("weights/yolov8-detector/yolov8-s-license-plate-detector.pt")
# plate_detector.predict("io/input/IMG_5157.JPG", save=True, save_crop=True)

plate_recognizer = DTRB("weights/dtrb-recognizer/dtrb-None-VGG-BiLSTM-CTC-license-plate-recognizer.pth")
plate_recognizer.predict("io/input-plates")
