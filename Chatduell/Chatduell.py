
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def window():
    app = QApplication(sys.argv)
    window = QMainWindow()
    height = 500
    width = 500
    window.setGeometry(200,200,width,height)
    window.setWindowTitle("Chatduell")
    label = QLabel(window)
    label.setText("100")
    label.move(width/2,height-50)
    
    window.show()
    sys.exit(app.exec_())

window()