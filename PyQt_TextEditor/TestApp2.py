# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestApp2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox  # Popup creation and message box


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Picture Changer")
        MainWindow.resize(644, 466)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photos = QtWidgets.QLabel(self.centralwidget)
        self.photos.setGeometry(QtCore.QRect(16, 12, 621, 281))
        self.photos.setText("")

        self.photos.setPixmap(QtGui.QPixmap("Pic1.jpg"))
        # self.photos.setPixmap(QtGui.QPixmap("PyQt_TextEditor/Pic1.jpg"))  # Original

        self.photos.setScaledContents(True)
        self.photos.setObjectName("photos")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(70, 342, 151, 41))
        self.next.setObjectName("next")
        self.previous = QtWidgets.QPushButton(self.centralwidget)
        self.previous.setGeometry(QtCore.QRect(460, 340, 131, 41))
        self.previous.setObjectName("previous")

        # pop-up button
        self.popup = QtWidgets.QPushButton(self.centralwidget)
        self.popup.setGeometry(QtCore.QRect(290, 390, 131, 41))
        self.popup.setObjectName("popup")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Show the pictures
        self.next.clicked.connect(self.show_pic2)
        self.previous.clicked.connect(self.show_pic1)
        # show popup
        self.popup.clicked.connect(self.show_popup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Picture Changer", "Picture Changer"))
        self.next.setText(_translate("Picture Changer", "Next"))
        self.previous.setText(_translate("Picture Changer", "Previous"))
        # popup button
        self.popup.setText(_translate("Picture Changer", "Popup"))

    def show_pic1(self):
        self.photos.setPixmap(QtGui.QPixmap("Pic1.jpg"))

    def show_pic2(self):
        self.photos.setPixmap(QtGui.QPixmap("Pic2.jpg"))

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("First Ever Popup")
        msg.setText('Main Message')
        msg.setInformativeText('Information of message')
        # msg.setIcon(QMessageBox.Critical)
        msg.setIcon(QMessageBox.Warning)
        # msg.setIcon(QMessageBox.Information)
        # msg.setIcon(QMessageBox.Question)

        # .open|.save|.Ok|.Close|.Yes|.No|.Abort|.Retry|.Ignore|.Ok
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Retry | QMessageBox.Abort)
        msg.setDefaultButton(QMessageBox.Abort)

        msg.setDetailedText('Details of the message')

        msg.buttonClicked.connect(self.popup_button)

        x = msg.exec_()

    def popup_button(self, i):
        print(i.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
