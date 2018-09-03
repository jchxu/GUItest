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

    def btn_click(self):    # 按钮单击后的操作
        test=self.price_box.toPlainText()       # 读取名为"price_box"的EditText文本框的内容
        self.results_window.setText("fhdsfsj")  # 更改名为"results_window"的EditText文本框的内容
        rate = self.tax_rate.value()            # 读取名为"tax_rate"的范围选择框的内容


######################################



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindows()
    window.show()
    sys.exit(app.exec_())