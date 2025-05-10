#!/bin/bash

# Exit on error
set -e

# Step 1: Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv .venv
fi

# Step 2: Activate the virtual environment
source .venv/bin/activate

# Step 3: Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
  echo "Installing dependencies..."
  pip install --upgrade pip
  pip install -r requirements.txt
fi

# Step 4: Start the FastAPI app with Uvicorn
echo "Starting FastAPI app..."
uvicorn main:app --reload
