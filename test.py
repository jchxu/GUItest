# coding=utf-8

import sys
from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtWidgets import QDialog
from MainWindows import Ui_MainWindow
from TwoWindows2 import Ui_Dialog

#################### Templete ################################
class MyWindows(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindows, self).__init__()
        self.setupUi(self)

class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog()
        self.child.setupUi(self)

    ######## Slot functions #############
    def major_click(self):
        print

    def minor_click(self):
        print

    def base_click(self):
        print

    def classic_click(self):
        print

    def new_click(self):
        print

    def mine_click(self):
        print

    def trend_click(self):
        print

    #def slot_major(self):
    #    print()
    #    price=self.price_box.toPlainText()
    #    self.results_window.setText("hi,PyQt5~")
    #    rate = self.tax_rate.value()
    #    self.results_window.setText(price*rate)
    #    self.label.text(price*rate)
    ######################################


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindows()
    child = childWindow()
    window.major_lib.clicked.connect(child.show)

    window.show()
    sys.exit(app.exec_())