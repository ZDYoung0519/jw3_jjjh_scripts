from UI.main_window import Ui_main
from UI.purchase import Ui_purchase
import sys, re
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal


class MainWin(QMainWindow, Ui_main):

    def __init__(self, win1):
        super(MainWin, self).__init__()
        self.setupUi(self)
        self.pushButton_1.clicked.connect(win1.show)


class Win1(QWidget, Ui_purchase):
    def __init__(self):
        super(Win1, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.StartRunning)

    def StartRunning(self):
        self.pushButton.setDisabled(True)
        port = eval(re.sub('\D', '', self.comboBox_1.currentText()))
        id = eval(re.sub('\D', '', self.comboBox_2.currentText()))
        num = self.spinBox_3.value()
        duration = self.spinBox_4.value()
        self.purchase_thread = PurchaseThread(port, id, num, duration)
        self.purchase_thread.start()
        self.purchase_thread.finish_signal.connect(self.EndRunning)


    def EndRunning(self):
        self.textBrowser.append('程序结束,详情日志可查看log.txt')
        self.pushButton.setDisabled(False)
        self.pushButton.setDisabled(True)

    def end_running(self):
        print(hasattr(self, 'purchase_thread'))
        if hasattr(self, 'purchase_thread'):
            del self.purchase_thread
        print(hasattr(self, 'purchase_thread'))
        self.textBrowser.append('程序已经终止')
        self.pushButton.setDisabled(False)
        self.pushButton.setDisabled(True)


class PurchaseThread(QThread):
    finish_signal = pyqtSignal(list)

    def __init__(self, port, id, num, duration):
        super(PurchaseThread, self).__init__()
        self.port = port
        self.id = id
        self.num = num
        self.duration = duration

    def __del__(self):
        self.wait()

    def run(self):
        from Scripts.purchaseV1 import purchase
        purchase(port=self.port, id=self.id, num=self.num, duration=self.duration)
        self.finish_signal.emit(['程序结束'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    purchase = Win1()
    main_win = MainWin(purchase)
    main_win.show()
    sys.exit(app.exec_())
