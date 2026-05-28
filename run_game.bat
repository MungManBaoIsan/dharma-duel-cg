@echo off
echo ========================================
echo  DHARMA DUEL - Starting Game
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo.
    echo Please install Python from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

REM Check if pygame is installed
python -c "import pygame" >nul 2>&1
if errorlevel 1 (
    echo Installing pygame...
    pip install pygame
    if errorlevel 1 (
        echo.
        echo ERROR: Failed to install pygame!
        echo Please run: pip install pygame
        echo.
        pause
        exit /b 1
    )
)

REM Run the game
echo Starting Dharma Duel...
echo.
python main.py

if errorlevel 1 (
    echo.
    echo Game exited with error!
    echo.
    pause
)
