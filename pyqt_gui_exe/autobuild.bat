@echo off

title "Build start..."
echo "Build start..."

color 2

cd /d %~dp0


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
call "ui2py.bat"


set errorInfo=Generate %outputFile% failed.
set successInfo=Generate %outputFile% successfully.

if %errorlevel%==1 (
    echo %errorInfo%
    goto FAILED
) else (
    echo %successInfo%
)

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
call "qrc2py.bat"

set errorInfo=Generate %outputFile% failed.
set successInfo=Generate %outputFile% successfully.

if %errorlevel%==1 (
    echo %errorInfo%
    goto FAILED
) else (
    echo %successInfo%
)


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
call "py2exe.bat"

set errorInfo=Generate executable file failed!
set successInfo=Generate executable file successfully.

if %errorlevel%==1 (
    echo %errorInfo%
    goto FAILED
) else (
    echo %successInfo%
)


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
goto SUCCESS


:FAILED

color 4
echo "Build failed!"
title "Build failed!"
pause
exit

:SUCCESS
color 2
echo "Build success."
title "Build success."

pause