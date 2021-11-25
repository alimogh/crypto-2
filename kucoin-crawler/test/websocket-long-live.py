import kucoin
from kucoin.asyncio import KucoinSocketManager

c = kucoin.client.Client()
ws = KucoinSocketManager()
ws.subscribe("BTC-USDT")

c.create_account()