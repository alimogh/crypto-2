import asyncio
from kucoin.client import WsToken
from kucoin.ws_client import KucoinWsClient


api_key = "618ce81a3f018700015de3ac"
api_secret = "02d62fe2-2bce-4411-aa4a-d5126c573fb8"
api_passphrase = "ldaram2648"


async def main():
    async def deal_msg(msg):
        # print('handle_event:',msg['topic'])
        if msg['topic'] == '/spotMarket/level2Depth5:BTC-USDT':
            print(msg["data"])
        elif msg['topic'] == '/spotMarket/level2Depth5:KCS-USDT':
            print(f'Get KCS level3:{msg["data"]}')
        elif msg['topic'] == '/market/ticker:ETH-USDT':
            print(f'Get ETH-USDT:{msg["data"]}')

    # is public
    client = WsToken()
    #is private
    # client = WsToken(key='', secret='', passphrase='', is_sandbox=False, url='')
    # is sandbox
    # client = WsToken(is_sandbox=True)
    ws_client = await KucoinWsClient.create(None, client, deal_msg, private=False)
    # await ws_client.subscribe('/market/ticker:BTC-USDT,ETH-USDT')
    # await ws_client.subscribe('/spotMarket/level2Depth5:BTC-USDT,KCS-USDT')
    await ws_client.subscribe('/market/ticker:BTC-USDT,ETH-USDT')
    while True:
        print("sleeping to keep loop open")
        await asyncio.sleep(10, loop=loop)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())