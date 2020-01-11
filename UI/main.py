from UI.main_window import Ui_main
from UI.purchase import Ui_purchase
from UI.adb import Ui_adb
from sys import argv, exit
from re import sub
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal


class MainWin(QMainWindow, Ui_main):
    """
    主窗口
    """
    def __init__(self, win1, adb_win):
        super(MainWin, self).__init__()
        self.setupUi(self)
        self.pushButton_1.clicked.connect(win1.show)
        self.pushButton_4.clicked.connect(adb_win.show)


class ADBWin(QWidget, Ui_adb):

    def __init__(self):
        super(ADBWin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openPath)
        self.pushButton_2.clicked.connect(self.adbInstall)
        self.pushButton_3.clicked.connect(self.ADBTest)
        self.pushButton_4.clicked.connect(self.ConnectTest)

    def openPath(self):
        open_path = QFileDialog.getExistingDirectory(self, '选择文件夹', '/')
        self.textEdit.setText(open_path+'/ADB/')

    def adbInstall(self):
        from Scripts.adb_install import MoveFiles
        MoveFiles(path1='../ADB', path2=self.textEdit.toPlainText())
        self.textBrowser.append('安装成功')
        self.textBrowser.append('安装完成后，右键我的电脑-属性-高级系统设置-环境变量，在系统变量中找到Path双击，新建一个变量，变量路径就是上面保存的路径')

    def ADBTest(self):
        from Scripts.adb_install import ADBTest
        self.textBrowser.append(ADBTest())

    def ConnectTest(self):
        from Scripts.adb_install import ConnectTest
        self.textBrowser.append(ConnectTest())


class Win1(QWidget, Ui_purchase):
    """
    自动购买窗口
    """
    def __init__(self):
        super(Win1, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.StartRunning)

    def StartRunning(self):
        self.pushButton.setDisabled(True)
        port = eval(sub('\D', '', self.comboBox_1.currentText()))
        id = eval(sub('\D', '', self.comboBox_2.currentText()))
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
    """
    自动购买线程
    """
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
    app = QApplication(argv)
    purchase = Win1()
    adb_win = ADBWin()
    main_win = MainWin(purchase, adb_win)
    main_win.show()
    exit(app.exec_())
