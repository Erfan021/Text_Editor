from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


# Class to give click methods/on-click-events access to everything such as labels
class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()  # Calling the parent class init method
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('First Application')
        self.initUI()

    # All the stuff we are going to call in our window
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Hello world!!!')
        self.label.move(100, 100)

        self.btn_1 = QtWidgets.QPushButton(self)
        self.btn_1.setText('Click here')
        self.btn_1.clicked.connect(self.clicked)

    # Update the changes
    def clicked(self):
        self.label.setText("You clicked the button")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)  # Creating the application
    main_win = MyMainWindow()  # Main window for the application

    main_win.show()
    sys.exit(app.exec_())


window()