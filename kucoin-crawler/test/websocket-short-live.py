import socket
from websocket import create_connection
ws = create_connection("ws://echo.websocket.org/")
# ws = create_connection("ws://echo.websocket.org/",sockopt=((socket.IPPROTO_TCP, socket.TCP_NODELAY),))
print("sending...")
ws.send("hello")
print("sent.")
result = ws.recv()
print("result=",result)
ws.close()
print("socket closed.")
