#!/bin/bash

# RotMG Web Scraper Runner Script
# This script runs the MongoDB web scraper with Python 3.12.6

echo "🎮 Starting RotMG Web Scraper..."
echo "=================================================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment 'venv' not found!"
    echo "Please create it first with: python3.12 -m venv venv"
    exit 1
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found!"
    echo "Please create a .env file with your MongoDB credentials"
    exit 1
fi

# Display Python version
echo "🐍 Python version: $(venv/bin/python --version)"
echo "📦 Virtual environment: venv"
echo ""

# Check if MongoDB credentials are set (without showing the actual values)
if grep -q "<db_password>" .env; then
    echo "⚠️  WARNING: Please replace <db_password> in .env with your actual MongoDB password"
    echo ""
fi

echo "🚀 Starting scraper..."
echo "=================================================="

# Run the main script
venv/bin/python main.py

# Check exit status
if [ $? -eq 0 ]; then
    echo ""
    echo "=================================================="
    echo "✅ Scraper completed successfully!"
else
    echo ""
    echo "=================================================="
    echo "❌ Scraper failed with exit code $?"
fi