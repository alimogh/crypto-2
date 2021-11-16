#Example for get balance of accounts in python
import time
import base64
import hmac
import hashlib
import requests

api_key = "618ce81a3f018700015de3ac"
api_secret = "02d62fe2-2bce-4411-aa4a-d5126c573fb8"
api_passphrase = "ldaram2648"
api = '/api/v1/bullet-private'
url = 'https://api.kucoin.com'+api
now = int(time.time() * 1000)
str_to_sign = str(now) + 'POST' + api
signature = base64.b64encode(
    hmac.new(api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
passphrase = base64.b64encode(hmac.new(api_secret.encode('utf-8'), api_passphrase.encode('utf-8'), hashlib.sha256).digest())
headers = {
    "KC-API-SIGN": signature,
    "KC-API-TIMESTAMP": str(now),
    "KC-API-KEY": api_key,
    "KC-API-PASSPHRASE": passphrase,
    "KC-API-KEY-VERSION": "2"
}
response = requests.request('post', url, headers=headers)
print(response.status_code)
print(response.json())

# 200
# {'code': '200000', 'data': {'token': '2neAiuYvAU737TOajb2U3uT8AEZqSWYe0fBD4LoHuXJDSC7gIzJiH4kNTWhCPISWo6nDpAe7aUZt2WFx8ZPtBo8QppwiYgnnrwsoltwU49yj4e1bSpHqoHwZIngtMdMrjqPnP-biofHFLL2mCRRXUtqOaL7dbrslJBvJHl5Vs9Y=.4oyn3BxaFh0aBOaE5COCUA==', 'instanceServers': [{'endpoint': 'wss://ws-api.kucoin.com/endpoint', 'encrypt': True, 'protocol': 'websocket', 'pingInterval': 18000, 'pingTimeout': 10000}]}}
