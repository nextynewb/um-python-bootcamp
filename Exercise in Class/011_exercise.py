"""
Exercise: Trading Simulation

data = List of dicts for OHLOC + SMA_20 and SMA_50 data

Instructions:

    1. Loop through the data

    2. If the previous_data SMA_20 is less than previous_data SMA_50, and 
       the current_data SMA_20 is greater than current_data SMA_50, and the position is "CASH", then buy BTC (Pivoting Point)
        - Add the trade to the trades list
        - Update the position to "IN_POSITION"
        - Update the balance to the current balance - (btc_holdings * current_data['close'])
        - Update the btc_holdings to btc_holdings + (balance / current_data['close'])

    3. If the previous_data SMA_20 is greater than previous_data SMA_50, and 
       the current_data SMA_20 is less than current_data SMA_50, and the position is "IN_POSITION", then sell BTC (Pivoting Point)
        - Add the trade to the trades list
        - Update the position to "CASH"
        - Update the balance to the current balance + (btc_holdings * current_data['close'])
        - Update the btc_holdings to 0

    4. Print the balance, btc_holdings, and position

    5. Print the trades

"""

import requests

# Fetch BTC price data from GitHub
url = "https://raw.githubusercontent.com/nextynewb/um-python-bootcamp/refs/heads/main/dataset/BTC_1h.json"
data = requests.get(url).json()

# Initialize variables
balance = 10000
btc_holdings = 0
trades = []
position = "CASH"  # Can be either "CASH" or "IN_POSITION"

# Run simulation
for idx, current_data in enumerate(data):
    # Skip first 50 periods
    if idx <= 50:
        continue

    """
    Important Formula:

    btc_holdings = balance / current_data['close]
    balance (when sell) = btc_holdings * current_data['close]
    """
    # Continue here


