# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'purchase.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_purchase(object):
    def setupUi(self, purchase):
        purchase.setObjectName("purchase")
        purchase.setWindowModality(QtCore.Qt.WindowModal)
        purchase.resize(513, 422)
        self.verticalLayoutWidget = QtWidgets.QWidget(purchase)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 40, 401, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_3.addWidget(self.label_1)
        self.comboBox_1 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox_3 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_3.setProperty("value", 5)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout.addWidget(self.spinBox_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.spinBox_4 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_4.setMaximum(9999999)
        self.spinBox_4.setProperty("value", 1000)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_4.addWidget(self.spinBox_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.textBrowser = QtWidgets.QTextBrowser(purchase)
        self.textBrowser.setGeometry(QtCore.QRect(60, 350, 381, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.label_7 = QtWidgets.QLabel(purchase)
        self.label_7.setGeometry(QtCore.QRect(50, 310, 441, 21))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(purchase)
        self.pushButton.setGeometry(QtCore.QRect(170, 230, 161, 61))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(purchase)
        QtCore.QMetaObject.connectSlotsByName(purchase)
        purchase.setTabOrder(self.comboBox_2, self.spinBox_3)
        purchase.setTabOrder(self.spinBox_3, self.spinBox_4)
        purchase.setTabOrder(self.spinBox_4, self.pushButton)
        purchase.setTabOrder(self.pushButton, self.textBrowser)

    def retranslateUi(self, purchase):
        _translate = QtCore.QCoreApplication.translate
        purchase.setWindowTitle(_translate("purchase", "自动购买"))
        self.label_1.setText(_translate("purchase", "连接方式"))
        self.comboBox_1.setItemText(0, _translate("purchase", "0、USB"))
        self.comboBox_1.setItemText(1, _translate("purchase", "1、腾讯模拟器"))
        self.label_2.setText(_translate("purchase", "购买物品"))
        self.comboBox_2.setItemText(0, _translate("purchase", "0、心魔票"))
        self.comboBox_2.setItemText(1, _translate("purchase", "1、白帝票"))
        self.comboBox_2.setItemText(2, _translate("purchase", "2、蛋"))
        self.label_3.setText(_translate("purchase", "每次购买数量"))
        self.label_4.setText(_translate("purchase", "脚本运行时间(秒)"))
        self.label_7.setText(_translate("purchase", "开始前请手动打开游戏，加载到【交易行-摆摊-道具-购买】界面"))
        self.pushButton.setText(_translate("purchase", "START"))