from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def sum():
    global a
    a = int(main_window.space.text())
    main_window.space.setText("")
    # b = int(main_window.space.text())


def sub():
    ...

def equal():
    b = int(main_window.space.text())
    c = a - b
    main_window.setText(str(c))



app = QApplication([])

loader = QUiLoader()
main_window = loader.load("mainwindow.ui")
main_window.show()

main_window.sum.clicked.connect(sum)
main_window.sub.clicked.connect(sub)
main_window.equal.clicked.connect(equal)


app.exec()