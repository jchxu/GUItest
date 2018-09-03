# coding=utf-8

from Calc_Tax import Ui_MainWindow
import sys
from PyQt5 import QtGui,QtCore,QtWidgets

#################### Templete ################################
class MyWindows(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindows, self).__init__()
        self.setupUi(self)


######## Slot functions #############

    def btn_click(self):
        price=self.price_box.toPlainText()
        #self.results_window.setText("hi,PyQt5~")
        rate = self.tax_rate.value()
        self.results_window.setText(price*rate)
        #self.label.text(price*rate)
######################################



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindows()
    window.show()
    sys.exit(app.exec_())