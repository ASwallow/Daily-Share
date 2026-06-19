@echo off
cd /d "%~dp0"

echo [1/3] Creating directories...
if not exist "daily" mkdir "daily"

echo [2/3] Initializing Git...
if not exist ".git" (
    git init
    git remote add origin https://github.com/ASwallow/Daily-Share.git
)

echo [3/3] Done!
echo.
echo Run "启动管理器.bat" to start the GUI tool.
pause
