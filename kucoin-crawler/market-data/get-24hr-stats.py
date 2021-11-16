#Example for get balance of accounts in python
import time
import base64
import hmac
import hashlib
import requests

api_key = "618ce81a3f018700015de3ac"
api_secret = "02d62fe2-2bce-4411-aa4a-d5126c573fb8"
api_passphrase = "ldaram2648"
api = '/api/v1/market/stats?symbol=BTC-USDT'
url = 'https://api.kucoin.com'+api
now = int(time.time() * 1000)
str_to_sign = str(now) + 'GET' + api
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
# {'code': '200000', 'data': {'time': 1636628256628, 'symbol': 'BTC-USDT', 'buy': '65249.6', 'sell': '65249.7', 'changeRate': '-0.023', 'changePrice': '-1539.4', 'high': '69028', 'low': '62540', 'vol': '9629.34881396', 'volValue': '636063010.54094581', 'last': '65249.6', 'averagePrice': '67101.43436476', 'takerFeeRate': '0.001', 'makerFeeRate': '0.001', 'takerCoefficient': '1', 'makerCoefficient': '1'}}
