# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imu_show_design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_imu_show(object):
    def setupUi(self, imu_show):
        imu_show.setObjectName("imu_show")
        imu_show.resize(900, 600)
        imu_show.setMinimumSize(QtCore.QSize(900, 600))
        imu_show.setMaximumSize(QtCore.QSize(900, 600))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 235, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 235, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 235, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 235, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        imu_show.setPalette(palette)
        imu_show.setAutoFillBackground(False)
        self.openGLWidget_imu = OpenGLWidget(imu_show)
        self.openGLWidget_imu.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.openGLWidget_imu.setMinimumSize(QtCore.QSize(600, 600))
        self.openGLWidget_imu.setMaximumSize(QtCore.QSize(600, 600))
        self.openGLWidget_imu.setObjectName("openGLWidget_imu")
        self.pushButton_connect = QtWidgets.QPushButton(imu_show)
        self.pushButton_connect.setGeometry(QtCore.QRect(785, 40, 100, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_connect.setFont(font)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.comboBox_baud = QtWidgets.QComboBox(imu_show)
        self.comboBox_baud.setGeometry(QtCore.QRect(680, 40, 100, 22))
        self.comboBox_baud.setObjectName("comboBox_baud")
        self.comboBox_com = QtWidgets.QComboBox(imu_show)
        self.comboBox_com.setGeometry(QtCore.QRect(680, 10, 100, 22))
        self.comboBox_com.setObjectName("comboBox_com")
        self.label_com = QtWidgets.QLabel(imu_show)
        self.label_com.setGeometry(QtCore.QRect(610, 10, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_com.setFont(font)
        self.label_com.setTextFormat(QtCore.Qt.AutoText)
        self.label_com.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_com.setWordWrap(False)
        self.label_com.setObjectName("label_com")
        self.textBrowser_receive = QtWidgets.QTextBrowser(imu_show)
        self.textBrowser_receive.setGeometry(QtCore.QRect(610, 70, 280, 451))
        self.textBrowser_receive.setObjectName("textBrowser_receive")
        self.label_baud = QtWidgets.QLabel(imu_show)
        self.label_baud.setGeometry(QtCore.QRect(610, 40, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_baud.setFont(font)
        self.label_baud.setTextFormat(QtCore.Qt.AutoText)
        self.label_baud.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_baud.setWordWrap(False)
        self.label_baud.setObjectName("label_baud")
        self.label_logo = QtWidgets.QLabel(imu_show)
        self.label_logo.setGeometry(QtCore.QRect(640, 525, 219, 68))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_logo.setObjectName("label_logo")
        self.quickWidget = QtQuickWidgets.QQuickWidget(imu_show)
        self.quickWidget.setGeometry(QtCore.QRect(-100, 840, 300, 200))
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        self.pushButton_RefreshCom = QtWidgets.QPushButton(imu_show)
        self.pushButton_RefreshCom.setGeometry(QtCore.QRect(785, 10, 100, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_RefreshCom.setFont(font)
        self.pushButton_RefreshCom.setObjectName("pushButton_RefreshCom")

        self.retranslateUi(imu_show)
        self.pushButton_connect.clicked.connect(imu_show.onConnect)
        self.pushButton_RefreshCom.clicked.connect(imu_show.onRefreshCom)
        self.comboBox_baud.currentTextChanged['QString'].connect(imu_show.onComboBaudChanged)
        QtCore.QMetaObject.connectSlotsByName(imu_show)

    def retranslateUi(self, imu_show):
        _translate = QtCore.QCoreApplication.translate
        imu_show.setWindowTitle(_translate("imu_show", "imu_show V1.5"))
        self.pushButton_connect.setText(_translate("imu_show", "connect"))
        self.label_com.setText(_translate("imu_show", "com"))
        self.label_baud.setText(_translate("imu_show", "baud"))
        self.pushButton_RefreshCom.setText(_translate("imu_show", "refresh com"))

from PyQt5 import QtQuickWidgets
from OpenGLWidget import OpenGLWidget
