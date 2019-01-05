#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
shared object
"""


from logger import get_logger
from error_handler import try_except


# --------------------------------------------------------------------------------------------------
FramelessWindowStyleSheet = """
    /*标题栏*/
    TitleBar {
        background-color: rgb(54, 157, 180);
    }

    /*最小化最大化关闭按钮通用默认背景*/
    #buttonMinimum,#buttonMaximum,#buttonClose {
        border: none;
        background-color: rgb(54, 157, 180);
    }

    QLabel {
        color: #000000;
        font-size:15px;
        font-family: "Arial","Microsoft YaHei","黑体","宋体",sans-serif;
        font-size: 14px;
    }

    #titleLabel {
        color: white;
        font-family: "Arial","Microsoft YaHei","黑体","宋体",sans-serif;
        font-size: 14px;
        background-color: rgb(54, 157, 180);
    }

    /*悬停*/
    #buttonMinimum:hover,#buttonMaximum:hover {
        background-color: rgb(48, 141, 162);
    }
    #buttonClose:hover {
        color: white;
        background-color: rgb(232, 17, 35);
    }

    /*鼠标按下不放*/
    #buttonMinimum:pressed,#buttonMaximum:pressed {
        background-color: rgb(44, 125, 144);
    }
    #buttonClose:pressed {
        color: white;
        background-color: rgb(161, 73, 92);
    }
"""

# --------------------------------------------------------------------------------------------------
@try_except
def TestFunc():
    pass

# --------------------------------------------------------------------------------------------------
if __name__=="__main__":
    TestFunc()