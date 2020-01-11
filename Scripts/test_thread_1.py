from UI.xuanshang import Ui_xuanshang
import sys, re
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from time import sleep


class Win1(QWidget, Ui_xuanshang):
    def __init__(self):
        super(Win1, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Work)

    def Work(self):
        sleep(10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win1()
    win.show()
    sys.exit(app.exec_())
