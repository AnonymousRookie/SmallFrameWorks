@echo off

cd /d %~dp0

set inputFile="ui_designer.ui"
set outputFile="ui_designer.py"

call "D:\ProgramFiles\Python\Python(x86)\python3.4.3\Lib\site-packages\PyQt5\pyuic5.bat" %inputFile% -o %outputFile%
