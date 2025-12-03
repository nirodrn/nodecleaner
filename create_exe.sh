#!/bin/bash

echo "=================================================="
echo "     Node Modules Cleaner - Auto Builder"
echo "=================================================="

# 1. Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "[INFO] Python 3 is NOT installed."
    
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if command -v apt-get &> /dev/null; then
            echo "[INFO] Detected Debian/Ubuntu."
            echo "Attempting to install python3..."
            sudo apt-get update && sudo apt-get install -y python3 python3-pip
        elif command -v yum &> /dev/null; then
            echo "[INFO] Detected RHEL/CentOS."
            sudo yum install -y python3 python3-pip
        else
            echo "[ERROR] Could not detect package manager. Please install Python 3 manually."
            exit 1
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        if command -v brew &> /dev/null; then
            echo "[INFO] Detected macOS (Homebrew)."
            brew install python
        else
            echo "[ERROR] Homebrew not found. Please install Python 3 manually."
            exit 1
        fi
    else
        echo "[ERROR] Unsupported OS. Please install Python 3 manually."
        exit 1
    fi
else
    echo "[INFO] Python 3 is installed."
fi

# 2. Check/Install Dependencies
echo ""
echo "[INFO] Checking dependencies..."
pip3 install -r requirements.txt --break-system-packages 2>/dev/null || pip3 install -r requirements.txt

# 3. Run Build Script
echo ""
echo "[INFO] Starting Build Process..."
python3 build.py
