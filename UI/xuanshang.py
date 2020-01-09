# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xuanshang.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_xuanshang(object):
    def setupUi(self, xuanshang):
        xuanshang.setObjectName("xuanshang")
        xuanshang.resize(546, 525)
        self.verticalLayoutWidget = QtWidgets.QWidget(xuanshang)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 50, 371, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setProperty("value", 5)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.spinBox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_2.setMaximum(9999999)
        self.spinBox_2.setProperty("value", 3600)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_4.addWidget(self.spinBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.textBrowser = QtWidgets.QTextBrowser(xuanshang)
        self.textBrowser.setGeometry(QtCore.QRect(90, 330, 391, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.label_4 = QtWidgets.QLabel(xuanshang)
        self.label_4.setGeometry(QtCore.QRect(90, 280, 401, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(xuanshang)
        self.pushButton.setGeometry(QtCore.QRect(210, 220, 141, 51))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(xuanshang)
        QtCore.QMetaObject.connectSlotsByName(xuanshang)
        xuanshang.setTabOrder(self.comboBox, self.spinBox)
        xuanshang.setTabOrder(self.spinBox, self.spinBox_2)
        xuanshang.setTabOrder(self.spinBox_2, self.pushButton)
        xuanshang.setTabOrder(self.pushButton, self.textBrowser)

    def retranslateUi(self, xuanshang):
        _translate = QtCore.QCoreApplication.translate
        xuanshang.setWindowTitle(_translate("xuanshang", "自动购买"))
        self.label_2.setText(_translate("xuanshang", "购买物品"))
        self.comboBox.setItemText(0, _translate("xuanshang", "0、心魔票"))
        self.comboBox.setItemText(1, _translate("xuanshang", "1、白帝票"))
        self.comboBox.setItemText(2, _translate("xuanshang", "2、蛋"))
        self.label.setText(_translate("xuanshang", "每次购买数量"))
        self.label_3.setText(_translate("xuanshang", "脚本运行时间(秒)"))
        self.label_4.setText(_translate("xuanshang", "开始前请手动打开游戏，加载到【交易行-摆摊-道具】界面"))
        self.pushButton.setText(_translate("xuanshang", "START"))
