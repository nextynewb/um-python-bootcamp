"""
Answer: Get latest Price of XRP in Kucoin and Luno

1. Call the API using Kucoin API
2. Call the API using Luno API  
3. Print the latest price of XRP in Kucoin and Luno
"""

import requests

LUNO_API = 'https://api.mybitx.com/api/1/ticker?pair=XRPMYR'
KUCOIN_API = 'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=XRP-USDT'

# Get XRP price from Luno (in MYR)
luno_response = requests.get(LUNO_API)
luno_data = luno_response.json()
luno_price = float(luno_data['last_trade'])

# Get XRP price from Kucoin (in USDT)  
kucoin_response = requests.get(KUCOIN_API)
kucoin_data = kucoin_response.json()
kucoin_price = float(kucoin_data['data']['price'])

print("XRP Prices:")
print(f"Luno (MYR): RM {luno_price:.4f}")
print(f"Kucoin (USDT): ${kucoin_price:.4f}")
