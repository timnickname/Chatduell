
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)

        self.setWindowTitle("Chatduell")

        label = QLabel("Testlabel")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec_()