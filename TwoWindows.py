# coding=utf-8
import sys
from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog

from TwoWindows1 import Ui_MainWindow
from TwoWindows2 import Ui_Dialog

class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog()
        self.child.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = parentWindow()
    child = childWindow()
    #通过toolButton将两个窗体关联
    btn = window.main_ui.btn
    btn.clicked.connect(child.show)
    # 显示
    window.show()
    sys.exit(app.exec_())
