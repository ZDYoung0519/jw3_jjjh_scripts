from UI.purchase import Ui_purchase
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
        self.mythread=MyThread()
        self.mythread.start()


class MyThread(QThread):
    trigger = pyqtSignal()

    def __init__(self):
        super(MyThread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        sleep(10)
        self.trigger.emit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win1()
    win.show()
    sys.exit(app.exec_())
