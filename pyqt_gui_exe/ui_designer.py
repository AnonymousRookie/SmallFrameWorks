# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_designer.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Sample(object):
    def setupUi(self, Sample):
        Sample.setObjectName("Sample")
        Sample.resize(404, 130)
        self.pushButton = QtWidgets.QPushButton(Sample)
        self.pushButton.setGeometry(QtCore.QRect(210, 30, 111, 61))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Sample)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 161, 61))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Sample)
        QtCore.QMetaObject.connectSlotsByName(Sample)

    def retranslateUi(self, Sample):
        _translate = QtCore.QCoreApplication.translate
        Sample.setWindowTitle(_translate("Sample", "Auto test Tool"))
        self.pushButton.setText(_translate("Sample", "PushButton"))

