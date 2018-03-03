@echo off

set BinFolder=dist
set QssFolder=qss
set PyqtPlatformsFolder="D:/ProgramFiles/Python/Python(x86)/python3.4.3/Lib/site-packages/PyQt5/plugins"

if exist %BinFolder% (
	RD /s /Q %BinFolder%
)

python setup.py py2exe

xcopy %QssFolder% %BinFolder%\%QssFolder%\ /c/q/e
XCOPY %PyqtPlatformsFolder%\platforms %BinFolder%\platforms\ /c/q/e

PAUSE
