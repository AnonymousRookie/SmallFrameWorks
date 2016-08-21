#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------
import os
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ui_designer import *
import stylesheet
# -------------------------------------------------------


class CsvCheckerMainWidget(QtGui.QWidget, Ui_CsvChecker):
    def __init__(self, parent=None):
        super(CsvCheckerMainWidget, self).__init__(parent)
        self.setupUi(self)
        # 类成员变量 -------------------------------------------------------------------------------
        
        # 加载样式表 -------------------------------------------------------------------------------
        self.loadStyleSheet("mystyle")
        # 初始化UI上的显示信息 ---------------------------------------------------------------------
        self.setWindowTitle(u"Hello PyQt")
        # 连接信号与槽 ---------------------------------------------------------------------------------


        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.btn_clicked)


    # 设置样式表 -----------------------------------------------------------------------------------
    def loadStyleSheet(self, sheetName):
        file = QtCore.QFile(':/qss/%s.qss' % sheetName.lower())
        file.open(QtCore.QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = unicode(styleSheet, encoding='utf8')
        #print styleSheet
        self.setStyleSheet(styleSheet)



    # 响应函数 -----------------------------------------------------------------------------------
    def btn_clicked(self):
        self.lineEdit.setText("Hello PyQt!!!");


# --------------------------------------------------------------------------------------------------
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    widget = CsvCheckerMainWidget()
    widget.show()
    sys.exit(app.exec_())