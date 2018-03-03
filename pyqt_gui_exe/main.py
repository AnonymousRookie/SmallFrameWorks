#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------
import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication, QCheckBox, QFileDialog, QGridLayout,
        QHBoxLayout, QLabel, QSizePolicy, QSlider, QSpinBox, QStyle,
        QToolButton, QVBoxLayout, QWidget)

from ui_designer import *
import stylesheet
# -------------------------------------------------------


class SampleMainWidget(QWidget, Ui_Sample):
    def __init__(self, parent=None):
        super(SampleMainWidget, self).__init__(parent)
        self.setupUi(self)
        # 类成员变量 -------------------------------------------------------------------------------
        
        # 加载样式表 -------------------------------------------------------------------------------
        self.loadStyleSheet("mystyle")
        # 初始化UI上的显示信息 ---------------------------------------------------------------------
        self.setWindowTitle(u"Hello PyQt")
        # 连接信号与槽 -----------------------------------------------------------------------------
        self.pushButton.clicked.connect(self.btn_clicked)

    # 设置样式表 -----------------------------------------------------------------------------------
    def loadStyleSheet(self, sheetName):
        file = QtCore.QFile(':/qss/%s.qss' % sheetName.lower())
        file.open(QtCore.QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = str(styleSheet, encoding='utf8')
        self.setStyleSheet(styleSheet)


    # 响应函数 -----------------------------------------------------------------------------------
    def btn_clicked(self):
        self.lineEdit.setText("Hello PyQt!!!");


# --------------------------------------------------------------------------------------------------
if __name__=="__main__":
    app = QApplication(sys.argv)
    widget = SampleMainWidget()
    widget.show()
    sys.exit(app.exec_())