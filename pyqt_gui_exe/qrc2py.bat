@echo off

cd /d %~dp0

set inputFile="stylesheet.qrc"
set outputFile="stylesheet.py"

call "D:\ProgramFiles\Python\Python(x86)\python3.4.3\Lib\site-packages\PyQt5\pyrcc5" %inputFile% -o %outputFile%
