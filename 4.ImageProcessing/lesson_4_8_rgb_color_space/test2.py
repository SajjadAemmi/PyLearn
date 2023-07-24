from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import cv2

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyWidget")
        self.setFixedSize(400, 300)
        self.label = QLabel("Hello World", self)
        self.label.move(100, 100)
        self.label.setFixedSize(200, 50)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 20px; font-weight: bold;")

        # read image with opencv and show in window
        self.image = cv2.imread("input/mandrill.jpg")
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.image = QImage(self.image, self.image.shape[1], self.image.shape[0], QImage.Format_RGB888)
        self.label2 = QLabel(self)
        self.label2.setPixmap(QPixmap.fromImage(self.image))
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
