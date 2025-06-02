# price_simulator.py

import random

# Simulated base prices for a few tickers (can be expanded)
BASE_PRICES = {
    "AAPL": 175.00,
    "TSLA": 190.00,
    "AMZN": 135.00,
    "MSFT": 280.00,
    "GOOGL": 125.00,
    "NFLX": 400.00
}

def get_simulated_price(ticker):
    base_price = BASE_PRICES.get(ticker.upper(), 100.00)
    # Simulate small random fluctuations: +/- 5%
    fluctuation = base_price * random.uniform(-0.05, 0.05)
    return round(base_price + fluctuation, 2)
