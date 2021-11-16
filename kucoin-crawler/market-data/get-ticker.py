#Example for get balance of accounts in python
import time
import base64
import hmac
import hashlib
import requests

api_key = "618ce81a3f018700015de3ac"
api_secret = "02d62fe2-2bce-4411-aa4a-d5126c573fb8"
api_passphrase = "ldaram2648"
url = 'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT'
now = int(time.time() * 1000)
str_to_sign = str(now) + 'GET' + '/api/v1/market/orderbook/level1?symbol=BTC-USDT'
signature = base64.b64encode(
    hmac.new(api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
passphrase = base64.b64encode(
    hmac.new(api_secret.encode('utf-8'), api_passphrase.encode('utf-8'), hashlib.sha256).digest())
headers = {
    "KC-API-SIGN": signature,
    "KC-API-TIMESTAMP": str(now),
    "KC-API-KEY": api_key,
    "KC-API-PASSPHRASE": passphrase,
    "KC-API-KEY-VERSION": "2"
}
response = requests.request('get', url, headers=headers)
print(response.status_code)
print(response.json())

# 200
# {'code': '200000', 'data': {'time': 1636627149664, 'sequence': '1622402069997', 'price': '65262.6', 'size': '0.0005244', 'bestBid': '65262.5', 'bestBidSize': '0.15630421', 'bestAsk': '65262.6', 'bestAskSize': '1.16205591'}}