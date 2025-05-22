# Arbitrage Scanner

This project scans for arbitrage opportunities across multiple cryptocurrency exchanges.

## Features
- Fetches prices from centralized and decentralized exchanges
- Compares prices and detects arbitrage opportunities
- Easily configurable threshold for detection

## Project Structure
- `src/` - Main application code
- `src/fetchers/` - Exchange integration modules
- `tests/` - Unit tests

## Setup
1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
```bash
python src/main.py
```

## Running Tests
```bash
PYTHONPATH=src python -m unittest discover tests
``` 