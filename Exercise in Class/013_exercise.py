"""
Exercise: Get latest Price of XRP in Kucoin and Luno

1. Call the API using Kucoin API (https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=XRP-USDT) (use last_trade)
2. Call the API using Luno API (https://api.mybitx.com/api/1/ticker?pair=XRPMYR) (use price)
3. Print the latest price of XRP in Kucoin and Luno

"""

# Continue here
import requests

LUNO_API = 'https://api.mybitx.com/api/1/ticker?pair=XRPMYR'
KUCOIN_API = 'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=XRP-USDT'

