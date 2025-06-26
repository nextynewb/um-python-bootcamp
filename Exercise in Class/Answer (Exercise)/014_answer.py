# Answer 014
# Solution will be provided after class # Answer 012
# Solution will be provided after class 

"""
Answer: Arbitrage Tracker!

1. Get the latest price of XRP in Kucoin and Luno
2. Normalize the price to MYR (Convert the price to MYR in Kucoin)
3. Calculate the percentage difference between the two prices
4. If the percentage difference is greater than 1%, print the percentage difference
5. If the percentage difference is less than 1%, print "No Arbitrage Opportunity"
"""

import requests 

LUNO_API = 'https://api.mybitx.com/api/1/ticker?pair=XRPMYR'
KUCOIN_API = 'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=XRP-USDT'
USD_MYR_RATE = 4.25  # Double check during class

# Get XRP price from Luno (in MYR)
luno_response = requests.get(LUNO_API)
luno_data = luno_response.json()
luno_price = float(luno_data['last_trade'])

# Get XRP price from Kucoin (in USDT)
kucoin_response = requests.get(KUCOIN_API)
kucoin_data = kucoin_response.json()
kucoin_price_usd = float(kucoin_data['data']['price'])

# Convert Kucoin price to MYR
kucoin_price_myr = kucoin_price_usd * USD_MYR_RATE

# Calculate percentage difference
percentage_difference = (kucoin_price_myr - luno_price) / luno_price * 100

print("=== ARBITRAGE TRACKER ===")
print(f"Luno XRP Price: RM {luno_price:.4f}")
print(f"Kucoin XRP Price: ${kucoin_price_usd:.4f} (RM {kucoin_price_myr:.4f})")
print(f"Percentage Difference: {percentage_difference:.2f}%")

# Check for arbitrage opportunity
if abs(percentage_difference) > 1:
    print(f"🚨 ARBITRAGE OPPORTUNITY: {percentage_difference:.2f}%")
    if percentage_difference > 0:
        print("💡 Strategy: Buy on Luno, Sell on Kucoin")
    else:
        print("💡 Strategy: Buy on Kucoin, Sell on Luno")
else:
    print("❌ No Arbitrage Opportunity")