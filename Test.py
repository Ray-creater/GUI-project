import sys
from PyQt5 import QtWidgets, QtCore,QtGui,Qt
from PyQt5.QtGui import QIcon
import qtawesome


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        widget=QtWidgets.QWidget()
        b1=QtWidgets.QPushButton('btn1')
        b2=QtWidgets.QPushButton('btn2')
        b3=QtWidgets.QPushButton('btn3')
        b4=QtWidgets.QPushButton('btn4')
        b5=QtWidgets.QPushButton('btn5')
        b6=QtWidgets.QPushButton('btn6')

        layout=QtWidgets.QGridLayout()

        layout.addWidget(b1,0,0,2,1,alignment=QtCore.Qt.AlignLeft)
        layout.addWidget(b2,0,1,3,3,alignment=QtCore.Qt.AlignBottom)
        layout.addWidget(b3,1,0)
        layout.addWidget(b4,1,1)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setGeometry(300,600,1000,300)
        self.show()


def main():
    app=QtWidgets.QApplication(sys.argv)
    my=mywindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
