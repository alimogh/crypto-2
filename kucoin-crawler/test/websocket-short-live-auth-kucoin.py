import json
import socket

import yaml
from websocket import create_connection

bullet_public = yaml.full_load( "{'code': '200000'"
    ", 'data': {'token': '2neAiuYvAU61ZDXANAGAsiL4-iAExhsBXZxftpOeh_55i3Ysy2q2LEsEWU64mdzUOPusi34M_wGoSf7iNyEWJwYVXOGC3xJBUdb4jIyh6X2g8Vjoy_QhWtiYB9J6i9GjsxUuhPw3BlrzazF6ghq4LwmVWQJ2K9vOMKqeneRD0WE=.Bt7-iLK8o4ega8W5qqkQIQ=='"
            ", 'instanceServers': [{'endpoint': 'wss://ws-api.kucoin.com/endpoint'"
                            ", 'encrypt': True"
                            ", 'protocol': 'websocket'"
                            ", 'pingInterval': 18000"
                            ", 'pingTimeout': 10000}]}}")

url=bullet_public['data']['instanceServers'][0]['endpoint']
token= bullet_public['data']['token']
ws = create_connection(url+'?token='+token)
result = ws.recv()
print("connection result=",result)
assert result is not None

connectId = json.loads(result)["id"]
print("ping...")
# ws.send("hello") #result= {"id":"TB1SaXKSCu","type":"error","code":400,"data":"data format is invalid"}
ws.send('{"id":"'+connectId+'","type":"ping"}') #result= {"id":"TB1SaXKSCu","type":"error","code":400,"data":"data format is invalid"}
print("sent.")
result = ws.recv()# {"id":"TB2d2lfxGC","type":"pong"}
print("result=",result)
ws.close()
print("socket closed.")
