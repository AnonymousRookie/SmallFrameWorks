@echo off

title "auto clean"
echo "clean start..."

color 2
cd /d %~dp0

set BinFolder=dist
set BuildTempFolder=build
set PycacheFolder=__pycache__

if exist %BinFolder% (
    rd /s /Q %BinFolder%
)

if exist %BuildTempFolder% (
    rd /s /Q %BuildTempFolder%
)

if exist %PycacheFolder% (
    rd /s /Q %PycacheFolder%
)


set PyFileGeneratedByUI="ui_designer.py"
set PyFileGeneratedByQrc="stylesheet.py"

if exist %PyFileGeneratedByUI% (
    del /s /Q %PyFileGeneratedByUI%
)


if exist %PyFileGeneratedByQrc% (
    del /s /Q %PyFileGeneratedByQrc%
)

echo "clean end."

pause