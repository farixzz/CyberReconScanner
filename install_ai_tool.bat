@echo off
cls
echo ---------------------------------------------
echo AI Tool - Cyber Recon Scanner Setup for Windows
echo ---------------------------------------------

:: Step 1: Check Python Installation
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python is not installed or not in PATH.
    echo ➤ Please install Python 3.10+ from https://www.python.org/
    pause
    exit /b
)

:: Step 2: Create virtual environment
echo 🔧 Creating Python virtual environment...
python -m venv .venv

:: Step 3: Activate environment and install dependencies
echo 📦 Installing Python packages...
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install customtkinter reportlab

:: Step 4: Create results folder
if not exist results (
    mkdir results
)

echo ---------------------------------------------
echo ✅ Setup complete!
echo ---------------------------------------------
echo 🔍 To run the app:
echo 1. Activate venv: call .venv\Scripts\activate
echo 2. Run: python main.py
echo.
pause
