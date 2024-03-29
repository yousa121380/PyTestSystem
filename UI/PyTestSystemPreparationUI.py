# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyTestSystemPreparationUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PreMainWindow(object):
    def setupUi(self, PreMainWindow):
        PreMainWindow.setObjectName("PreMainWindow")
        PreMainWindow.resize(800, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PreMainWindow.sizePolicy().hasHeightForWidth())
        PreMainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(PreMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.noteTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.noteTextBrowser.setGeometry(QtCore.QRect(200, 100, 331, 191))
        self.noteTextBrowser.setObjectName("noteTextBrowser")
        self.mockTestPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.mockTestPushButton.setGeometry(QtCore.QRect(190, 370, 75, 23))
        self.mockTestPushButton.setObjectName("mockTestPushButton")
        self.officialTestPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.officialTestPushButton.setGeometry(QtCore.QRect(320, 370, 75, 23))
        self.officialTestPushButton.setObjectName("officialTestPushButton")
        self.gradeInfoPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.gradeInfoPushButton.setGeometry(QtCore.QRect(450, 370, 75, 23))
        self.gradeInfoPushButton.setObjectName("gradeInfoPushButton")
        self.selectTestBox = QtWidgets.QComboBox(self.centralwidget)
        self.selectTestBox.setGeometry(QtCore.QRect(300, 320, 111, 22))
        self.selectTestBox.setObjectName("selectTestBox")
        self.selectTestBox.addItem("")
        self.selectTestBox.addItem("")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 131, 69))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.preStuNameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.preStuNameLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"宋体\";")
        self.preStuNameLabel.setObjectName("preStuNameLabel")
        self.verticalLayout_2.addWidget(self.preStuNameLabel)
        self.preStuGradeLabel = QtWidgets.QLabel(self.layoutWidget)
        self.preStuGradeLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"宋体\";")
        self.preStuGradeLabel.setObjectName("preStuGradeLabel")
        self.verticalLayout_2.addWidget(self.preStuGradeLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.logoutButton = QtWidgets.QPushButton(self.layoutWidget)
        self.logoutButton.setObjectName("logoutButton")
        self.horizontalLayout_2.addWidget(self.logoutButton)
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.timeTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.timeTextBrowser.setGeometry(QtCore.QRect(640, 20, 111, 31))
        self.timeTextBrowser.setStyleSheet("font: 12pt \"黑体\";")
        self.timeTextBrowser.setObjectName("timeTextBrowser")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 30, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 80, 81, 16))
        self.label_6.setObjectName("label_6")
        PreMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PreMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        PreMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PreMainWindow)
        self.statusbar.setObjectName("statusbar")
        PreMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PreMainWindow)
        QtCore.QMetaObject.connectSlotsByName(PreMainWindow)

    def retranslateUi(self, PreMainWindow):
        _translate = QtCore.QCoreApplication.translate
        PreMainWindow.setWindowTitle(_translate("PreMainWindow", "MainWindow"))
        self.mockTestPushButton.setText(_translate("PreMainWindow", "模拟考试"))
        self.officialTestPushButton.setText(_translate("PreMainWindow", "正式考试"))
        self.gradeInfoPushButton.setText(_translate("PreMainWindow", "成绩信息"))
        self.selectTestBox.setItemText(0, _translate("PreMainWindow", "Python考试"))
        self.selectTestBox.setItemText(1, _translate("PreMainWindow", "MATLAB考试"))
        self.label.setText(_translate("PreMainWindow", "学生姓名"))
        self.label_2.setText(_translate("PreMainWindow", "考生年级"))
        self.preStuNameLabel.setText(_translate("PreMainWindow", "NULL"))
        self.preStuGradeLabel.setText(_translate("PreMainWindow", "NULL"))
        self.logoutButton.setText(_translate("PreMainWindow", "注销登录"))
        self.label_5.setText(_translate("PreMainWindow", "当前时间"))
        self.label_6.setText(_translate("PreMainWindow", "考生注意事项："))
