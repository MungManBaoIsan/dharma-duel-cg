#!/bin/bash

echo "========================================"
echo " DHARMA DUEL - Starting Game"
echo "========================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "ERROR: Python 3 is not installed!"
    echo ""
    echo "Please install Python 3 from:"
    echo "https://www.python.org/downloads/"
    echo ""
    exit 1
fi

# Check if pygame is installed
python3 -c "import pygame" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing pygame..."
    pip3 install pygame
    if [ $? -ne 0 ]; then
        echo ""
        echo "ERROR: Failed to install pygame!"
        echo "Please run: pip3 install pygame"
        echo ""
        exit 1
    fi
fi

# Run the game
echo "Starting Dharma Duel..."
echo ""
python3 main.py

if [ $? -ne 0 ]; then
    echo ""
    echo "Game exited with error!"
    echo ""
    read -p "Press Enter to exit..."
fi
