from kucoin.client import Client

api_key = "618ce81a3f018700015de3ac"
api_secret = "02d62fe2-2bce-4411-aa4a-d5126c573fb8"
api_passphrase = "ldaram2648"

client = Client(api_key,api_secret,api_passphrase)

# or connect to Sandbox
# client = Client(api_key, api_secret, api_passphrase, sandbox=True)

# get currencies
currencies = client.get_currencies()
print(currencies)

# get market depth
depth = client.get_order_book('KCS-BTC')
print(depth)

# get symbol klines
klines = client.get_kline_data('KCS-BTC')
print(klines)

# get list of markets
markets = client.get_markets()
print(markets)

# place a market buy order
# order = client.create_market_order('NEO', Client.SIDE_BUY, size=20)

# get list of active orders
orders = client.get_orders('KCS-BTS',status='active')
print(orders)
