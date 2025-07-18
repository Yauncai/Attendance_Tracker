#!/bin/bash

# Check if venv exists, if not create it
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run generate_qr.py in the background
python generate_qr.py &

# Run the Flask app
python attendance.py
