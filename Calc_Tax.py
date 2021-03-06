# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calc_Tax.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.price_box = QtWidgets.QTextEdit(self.centralwidget)
        self.price_box.setGeometry(QtCore.QRect(40, 90, 321, 41))
        self.price_box.setObjectName("price_box")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tax_rate = QtWidgets.QSpinBox(self.centralwidget)
        self.tax_rate.setGeometry(QtCore.QRect(70, 230, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.tax_rate.setFont(font)
        self.tax_rate.setProperty("value", 20)
        self.tax_rate.setObjectName("tax_rate")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 200, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setToolTipDuration(2)
        self.label_2.setObjectName("label_2")
        self.calc_tax_button = QtWidgets.QPushButton(self.centralwidget)
        self.calc_tax_button.setGeometry(QtCore.QRect(80, 320, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.calc_tax_button.setFont(font)
        self.calc_tax_button.setObjectName("calc_tax_button")
        self.results_window = QtWidgets.QTextEdit(self.centralwidget)
        self.results_window.setGeometry(QtCore.QRect(90, 400, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.results_window.setFont(font)
        self.results_window.setObjectName("results_window")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.calc_tax_button.clicked.connect(MainWindow.btn_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Price"))
        self.label_2.setText(_translate("MainWindow", "Tax Rate"))
        self.calc_tax_button.setText(_translate("MainWindow", "Calculate Tax"))



class MyWindows(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindows, self).__init__()
        self.setupUi(self)


######## Slot functions #############

    def btn_click(self):
        price = float(self.price_box.toPlainText())
        #self.results_window.setText("hi,PyQt5~")
        rate = (self.tax_rate.value())
        result = "Price * Rate = " + str(price*rate)
        self.results_window.setText(result)
        #self.label.text(price*rate)
######################################



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindows()
    window.show()
    sys.exit(app.exec_())