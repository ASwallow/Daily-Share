@echo off
chcp 65001 >nul
echo ========================================
echo        每日一题项目初始化脚本
echo ========================================
echo.

REM 检查 Node.js 是否安装
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo [错误] 未检测到 Node.js，请先安装 Node.js
    echo 下载地址: https://nodejs.org/
    pause
    exit /b 1
)

echo [1/3] 安装依赖...
call npm install
if %errorlevel% neq 0 (
    echo [错误] 依赖安装失败
    pause
    exit /b 1
)

echo [2/3] 初始化 Git 仓库...
git init
git add .
git commit -m "初始化每日一题项目"

echo [3/3] 完成！
echo.
echo ========================================
echo  下一步操作：
echo  1. 在 GitHub 创建仓库 daily-share
echo  2. 运行以下命令：
echo     git remote add origin https://github.com/你的用户名/daily-share.git
echo     git push -u origin main
echo  3. 进入仓库 Settings - Pages
echo     Source 选择 GitHub Actions
echo ========================================
echo.
pause
