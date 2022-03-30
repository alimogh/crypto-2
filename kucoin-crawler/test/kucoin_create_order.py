symbol = 'DASH-USDT'
kline_type='1min'
api_key = "618ce81a3f018700015de3ac"
api_secret = "02d62fe2-2bce-4411-aa4a-d5126c573fb8"
api_passphrase = "ldaram2648"


#  MarketData
from kucoin.client import Market
client = Market(url='https://api.kucoin.com')
# client = Market()

# or connect to Sandbox
# client = Market(url='https://openapi-sandbox.kucoin.com')
# client = Market(is_sandbox=True)

# get symbol kline
klines = client.get_kline(symbol,kline_type)

# get symbol ticker
server_time = client.get_server_timestamp()

# Trade
from kucoin.client import Trade
# client = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase, is_sandbox=False, url='https://api.kucoin.com')
client = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase)

# or connect to Sandbox
# client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)

# place a limit buy order
# order_id = client.create_limit_order(symbol, 'buy', '1', '8000')

# place a market buy order   Use cautiously
order_id = client.create_market_order(symbol, 'buy', size='0.005')
# order_id = client.create_market_order(symbol, 'sell', size='0.01')
print(order_id)

# cancel limit order
# client.cancel_order('5bd6e9286d99522a52e458de')

# User
from kucoin.client import User
client = User(api_key, api_secret, api_passphrase)

# or connect to Sandbox
# client = User(api_key, api_secret, api_passphrase, is_sandbox=True)

address = client.get_withdrawal_quota('KCS')
print(address)