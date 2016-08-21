# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_designer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CsvChecker(object):
    def setupUi(self, CsvChecker):
        CsvChecker.setObjectName(_fromUtf8("CsvChecker"))
        CsvChecker.resize(404, 130)
        self.pushButton = QtGui.QPushButton(CsvChecker)
        self.pushButton.setGeometry(QtCore.QRect(210, 30, 111, 61))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(CsvChecker)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 161, 61))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(CsvChecker)
        QtCore.QMetaObject.connectSlotsByName(CsvChecker)

    def retranslateUi(self, CsvChecker):
        CsvChecker.setWindowTitle(_translate("CsvChecker", "Auto test Tool", None))
        self.pushButton.setText(_translate("CsvChecker", "PushButton", None))

