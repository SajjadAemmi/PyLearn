import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtUiTools import QUiLoader
from mytime import MyTime


class TimerThread(QThread):
    signal_show = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 15, 30)

    def run(self):
        while True:
            self.time.minus()
            # print(self.second)
            self.signal_show.emit(self.time)
            time.sleep(1)

class StopWatchThread(QThread):
    signal_show = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 0, 0)

    def run(self):
        while True:
            self.time.plus()
            # print(self.second)
            self.signal_show.emit(self.time)
            time.sleep(1)

    def reset(self):
        self.time.hour = 0
        self.time.minute = 0
        self.time.second = 0

def test():
    print("Hello World")

def read_from_file():
    f = open("path/to/file.txt", "r")


def reset_stopwatch():
    thread_stopwatch.reset()

def stop_stopwatch():
    thread_stopwatch.terminate()

def start_stopwatch():
    thread_stopwatch.start()

def start_timer():
    thread_timer.start()

def show_time_timer(time):
    window.tb_hour_timer.setText(str(time.hour))
    window.tb_minute_timer.setText(str(time.minute))
    window.tb_second_timer.setText(str(time.second))

def show_time_stopwatch(time):
    window.lbl_stopwatch.setText(f"{time.hour}:{time.minute}:{time.second}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    loader = QUiLoader()
    window = loader.load("mainwindow.ui")
    window.show()

    thread_stopwatch = StopWatchThread()
    thread_timer = TimerThread()
    window.lbl_stopwatch.setText("0:0:0")
    window.btn_start_stopwatch.clicked.connect(start_stopwatch)
    window.btn_stop_stopwatch.clicked.connect(stop_stopwatch)
    window.btn_reset_stopwatch.clicked.connect(reset_stopwatch)
    thread_stopwatch.signal_show.connect(show_time_stopwatch)
    window.btn_start_timer.clicked.connect(start_timer)
    thread_timer.signal_show.connect(show_time_timer)

    app.exec()
