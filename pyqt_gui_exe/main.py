#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------------------------------------------------------
import os
import sys
import PyQt5.QtCore
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtWidgets import (QApplication, QCheckBox, QFileDialog, QGridLayout,
        QHBoxLayout, QLabel, QSizePolicy, QSlider, QSpinBox, QStyle,
        QToolButton, QVBoxLayout, QWidget)

from ui_designer import *
import stylesheet
from frameless_window import FramelessWindow

from logger import get_logger
from error_handler import try_except
import shared_obj


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
    # 普通窗口
    # app = QApplication(sys.argv)
    # widget = SampleMainWidget()
    # widget.show()
    # sys.exit(app.exec_())

    # 无边框窗口
    app = QApplication(sys.argv)
    app.setStyleSheet(shared_obj.FramelessWindowStyleSheet)
    w = FramelessWindow()
    w.resize(380, 200)
    w.setWindowTitle('Hello PyQt(V0.0.1)')
    w.setWindowIcon(QIcon(':/logo.ico'))
    w.setWidget(SampleMainWidget(w))
    w.show()
    sys.exit(app.exec_())