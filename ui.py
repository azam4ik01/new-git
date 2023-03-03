import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


def window():
    app = QApplication(sys.argv)
    
    win = QWidget()
    win.setGeometry(100,800,500,500)
    win.setWindowTitle('My first app')

    label = QLabel(win)
    label.setText('Type something!')

    edit = QLineEdit(win)

    btn = QPushButton(win)
    btn.setText('Save')

    label.move(200,200)
    edit.move(180,250)
    btn.move(210,300)

    win.show()

    sys.exit(app.exec_())
    




window()