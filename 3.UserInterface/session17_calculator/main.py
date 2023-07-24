from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


def sub():
    global a
    a = int(main_window.txtbox.text())
    main_window.txtbox.setText("")


def result():
    b = int(main_window.txtbox.text())
    c = a - b
    main_window.txtbox.setText(str(c))


def num(x):
    old_number = main_window.txtbox.text()
    new_number = old_number + x
    main_window.txtbox.setText(new_number)

app = QApplication([])

loader = QUiLoader()
main_window = loader.load("main.ui")
main_window.show()

main_window.btn_equal.clicked.connect(result)
main_window.btn_sub.clicked.connect(sub)
main_window.btn_num_1.clicked.connect(partial(num, "1"))
main_window.btn_num_2.clicked.connect(partial(num, "2"))


app.exec()
