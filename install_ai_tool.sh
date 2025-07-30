#!/bin/bash

echo "🔧 Installing AI Tool - Cyber Recon Scanner..."
echo "---------------------------------------------"

# Ensure internet is up
echo "🌐 Checking internet connectivity..."
if ! ping -c 1 8.8.8.8 &>/dev/null; then
  echo "❌ No internet connection. Aborting installation."
  exit 1
fi

echo "📦 Installing system tools..."
sudo apt update
sudo apt install -y nmap nikto sqlmap gobuster metasploit-framework python3 python3-venv

echo "🐍 Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "📦 Installing Python requirements..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ AI Tool installed successfully. Run it using:"
echo "./.venv/bin/python main.py"

