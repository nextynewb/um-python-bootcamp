"""
Exercise: Arbitrage Tracker!

1. Get the latest price of XRP in Kucoin and Luno
2. Normalize the price to MYR (Convert the price to MYR in Kucoin)
3. Calculate the percentage difference between the two prices
4. If the percentage difference is greater than 1%, print the percentage difference
5. If the percentage difference is less than 1%, print "No Arbitrage Opportunity"

Formula for percentage difference:
    percentage_difference = (kucoin_price - luno_price) / luno_price * 100

"""

# Continue here

import requests 

LUNO_API = 'https://api.mybitx.com/api/1/ticker?pair=XRPMYR'
KUCOIN_API = 'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=XRP-USDT'
USD_MYR_RATE = 4.25 # Double check during class




