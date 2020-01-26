# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestApp3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 405)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBoxX = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxX.setGeometry(QtCore.QRect(20, 20, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBoxX.setFont(font)
        self.comboBoxX.setObjectName("comboBoxX")
        self.comboBoxX.addItem("")
        self.comboBoxX.addItem("")
        self.comboBoxY = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxY.setGeometry(QtCore.QRect(180, 20, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBoxY.setFont(font)
        self.comboBoxY.setObjectName("comboBoxY")
        self.comboBoxY.addItem("")
        self.comboBoxY.addItem("")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(110, 100, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 210, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Add item
        self.comboBoxX.addItem('Hello')
        self.comboBoxY.addItem('World')
        # Setting default item
        # index = self.comboBoxX.findText('Hello', QtCore.Qt.MatchFixedString)
        # self.comboBoxX.setCurrentIndex(index)
        # self.comboBoxY.setCurrentIndex(2)  # Value at index 2

        self.comboBoxX.setCurrentIndex(0)
        self.comboBoxY.setCurrentIndex(0)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.submit.clicked.connect(self.pressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBoxX.setItemText(0, _translate("MainWindow", "0"))
        self.comboBoxX.setItemText(1, _translate("MainWindow", "1"))
        self.comboBoxY.setItemText(0, _translate("MainWindow", "0"))
        self.comboBoxY.setItemText(1, _translate("MainWindow", "1"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "X XOR Y = "))

    def pressed(self):
        x = self.comboBoxX.currentText()
        y = self.comboBoxY.currentText()
        xor = x != y
        if xor == True:
            xor = 1
        else:
            xor = 0

        print(xor)
        self.label.setText("X XOR Y = " + str(xor))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
