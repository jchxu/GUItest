# coding=utf-8

from Calc_Tax import Ui_MainWindow
import sys
from PyQt5 import QtGui,QtCore,QtWidgets

class MyWindows(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindows, self).__init__()
        self.setupUi(self)

    def btn_click(self):
        self.results_window.setText("hi,PyQt5~")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindows()
    window.show()
    sys.exit(app.exec_())