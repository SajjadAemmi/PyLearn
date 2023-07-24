import sys
import cv2
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.my_btn = QPushButton()
        self.my_btn.setText("Hello World")
        layout.addWidget(self.my_btn)

        self.my_label = QLabel()
        layout.addWidget(self.my_label)

        image = cv2.imread("input/peppers.jpg")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_qt = QImage(image, image.shape[1], image.shape[0], QImage.Format.Format_RGB888)
        image_qpixmap = QPixmap.fromImage(image_qt)
        self.my_label.setPixmap(image_qpixmap)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    app.exec()
