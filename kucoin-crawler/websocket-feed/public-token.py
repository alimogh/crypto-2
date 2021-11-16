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
# {'code': '200000', 'data': {'token': '2neAiuYvAU61ZDXANAGAsiL4-iAExhsBXZxftpOeh_55i3Ysy2q2LEsEWU64mdzUOPusi34M_wGoSf7iNyEWJ2DUBJg2Qp2YGPtw3zSoNQJ9ZoHCVYOuv9iYB9J6i9GjsxUuhPw3BlrzazF6ghq4L_Rsl7OjYVWmP4lDtXlKRyI=.UM7edBGHyOojadyEtaiK_Q==', 'instanceServers': [{'endpoint': 'wss://ws-api.kucoin.com/endpoint', 'encrypt': True, 'protocol': 'websocket', 'pingInterval': 18000, 'pingTimeout': 10000}]}}
