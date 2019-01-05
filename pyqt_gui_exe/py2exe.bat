@echo off

cd /d %~dp0

set BinFolder=dist
set PyqtPlatformsFolder="D:/ProgramFiles/Python/Python(x86)/python3.4.3/Lib/site-packages/PyQt5/plugins"

if exist %BinFolder% (
    RD /s /Q %BinFolder%
)

pyinstaller -F -w py2exe.spec

if %errorlevel%==0 (
    xcopy %PyqtPlatformsFolder%\platforms %BinFolder%\platforms\ /c/q/e
    xcopy %PyqtPlatformsFolder%\imageformats %BinFolder%\imageformats\ /c/q/e
)
