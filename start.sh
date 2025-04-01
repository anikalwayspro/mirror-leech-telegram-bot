#!/bin/bash

# Activate the virtual environment
source mltbenv/bin/activate

# Start Gunicorn in the background
gunicorn app:app &

# Run update.py
python3 update.py

# Run the bot
python3 -m bot

# Keep the container alive (important for Koye
