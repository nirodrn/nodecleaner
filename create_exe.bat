@echo off
setlocal EnableDelayedExpansion

echo ==================================================
echo      Node Modules Cleaner - Auto Builder
echo ==================================================

:: 1. Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Python is NOT installed.
    echo [INFO] Downloading Python installer...
    
    :: Download Python 3.11 (stable)
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe' -OutFile 'python_installer.exe'"
    
    if not exist python_installer.exe (
        echo [ERROR] Failed to download Python installer.
        pause
        exit /b 1
    )
    
    echo [INFO] Installing Python (this may take a few minutes)...
    echo [INFO] Please accept the User Account Control (UAC) prompt if it appears.
    
    :: Install silently, add to PATH, install for all users
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    
    :: Clean up
    del python_installer.exe
    
    echo [INFO] Python installation complete.
    echo [INFO] Refreshing environment variables...
    call RefreshEnv.cmd >nul 2>&1
) else (
    echo [INFO] Python is already installed.
)

:: 2. Check/Install Dependencies
echo.
echo [INFO] Checking dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies.
    pause
    exit /b 1
)

:: 3. Run Build Script
echo.
echo [INFO] Starting Build Process...
python build.py

pause
