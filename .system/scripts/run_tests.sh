#!/bin/bash
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

source .venv/bin/activate

echo "Ensuring dependencies..."
pip install playwright
playwright install chromium

echo "Running Phase 01 Tests..."
python3 tests/phase_01_test.py

echo "Running Phase 02 Tests (Stubs)..."
python3 tests/phase_02_test.py

