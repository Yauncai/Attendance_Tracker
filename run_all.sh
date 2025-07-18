#!/bin/bash

# Create virtual environment if missing
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database (run once)
echo "Initializing database..."
python yaf_database.py

# Generate QR code
echo "Generating QR code..."
python generate_qr.py

# Run Flask app
echo "Starting Flask app..."
python attendance.py
