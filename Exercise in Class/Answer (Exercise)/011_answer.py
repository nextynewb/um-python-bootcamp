import requests

# Fetch BTC price data from GitHub
url = "https://raw.githubusercontent.com/nextynewb/um-python-bootcamp/refs/heads/main/dataset/BTC_1h.json"
data = requests.get(url).json()

# Initialize variables
initial_balance = 10000
balance = initial_balance
btc_holdings = 0
trades = []
position = "CASH"  # Can be either "CASH" or "IN_POSITION"

# Run simulation
for idx, current_data in enumerate(data):
    # Skip first 50 periods
    if idx <= 50:
        continue

    prev_data = data[idx - 1]

    # Buy Signal: When SMA_20 crosses above SMA_50
    if position == "CASH" and prev_data['SMA_20'] <= prev_data['SMA_50'] and current_data['SMA_20'] > current_data['SMA_50']:
        btc_to_buy = balance / current_data['close']
        btc_holdings = btc_to_buy
        balance = 0
        position = "IN_POSITION"
        trades.append({
            'type': 'BUY',
            'datetime': current_data['datetime'],
            'price': current_data['close'],
            'btc_amount': btc_to_buy
        })

    # Sell Signal: When SMA_20 crosses below SMA_50
    elif position == "IN_POSITION" and prev_data['SMA_20'] > prev_data['SMA_50'] and current_data['SMA_20'] <= current_data['SMA_50']:
        balance = btc_holdings * current_data['close']
        btc_holdings = 0
        position = "CASH"
        trades.append({
            'type': 'SELL',
            'datetime': current_data['datetime'],
            'price': current_data['close'],
            'btc_amount': btc_holdings
        })

# Calculate final portfolio value
final_balance = balance + (btc_holdings * data[-1]['close'])
profit_loss = final_balance - initial_balance

# Print results
print(f"Initial Balance: ${initial_balance:,.2f}")
print(f"Final Balance: ${final_balance:,.2f}")
print(f"Profit/Loss: ${profit_loss:,.2f}")
print(f"Number of trades: {len(trades)}")

