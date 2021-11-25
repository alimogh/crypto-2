#Example for get balance of accounts in python
import time
import base64
import hmac
import hashlib
import requests

api = '/api/v1/bullet-public'
url = 'https://api.kucoin.com'+api
response = requests.request('post', url)
print(response.status_code)
print(response.json())

# 200
# {'code': '200000', 'data': {'token': '2neAiuYvAU61ZDXANAGAsiL4-iAExhsBXZxftpOeh_55i3Ysy2q2LEsEWU64mdzUOPusi34M_wGoSf7iNyEWJwYVXOGC3xJBUdb4jIyh6X2g8Vjoy_QhWtiYB9J6i9GjsxUuhPw3BlrzazF6ghq4LwmVWQJ2K9vOMKqeneRD0WE=.Bt7-iLK8o4ega8W5qqkQIQ==', 'instanceServers': [{'endpoint': 'wss://ws-api.kucoin.com/endpoint', 'encrypt': True, 'protocol': 'websocket', 'pingInterval': 18000, 'pingTimeout': 10000}]}}
