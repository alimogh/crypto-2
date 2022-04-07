""" algorithms :
    4/4/2022 1:42 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"


############################################
# What are the most successful trading algorithms?
# The most popular strategies are arbitrage, index fund rebalancing, mean reversion, and market timing. Other strategies are scalping, transaction cost reduction, and pairs trading.
# https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/what-are-algorithms-algos/
def arbitrage(df):
    '''
    آربیتراژ روشی است برای استفاده از ناهماهنگی های کوچک قیمت بازار که در قیمت بازار اوراق بهاداری که در دو بورس مختلف معامله می شود به وجود می آید. خرید یک سهام دو بورسیه با تخفیف در بازار A و فروش آن با حق بیمه در بازار B یک فرصت آربیتراژ بدون ریسک برای سود ارائه می دهد.
این روش را می توان در معاملات قراردادهای آتی S&P 500 و سهام S&P 500 به کار برد، زیرا معمولاً تفاوت های جزئی قیمت بین قیمت آتی و کل قیمت سهام اصلی واقعی ایجاد می شود. هنگامی که این اتفاق می افتد، معاملات اوراق بهادار در NASDAQ و NYSE یا از معاملات آتی S&P معامله شده در بازار CME عقب می افتند و فرصت آربیتراژ ایجاد می کنند.
برای اینکه آربیتراژ اتفاق بیفتد، باید سه شرط را داشته باشد. اولاً، دارایی های یکسان نباید در همه بازارها با یک قیمت معامله شود. دوم، دو دارایی با جریان های نقدی یکسان نباید با یک قیمت معامله شوند. در نهایت، دارایی با قیمت مشخص در آینده نباید امروز با قیمت آتی که با نرخ بهره بدون ریسک تنزیل شده است معامله شود.
آربیتراژ فقط با تجارت الکترونیکی اوراق بهادار و محصولات مالی امکان پذیر است. همچنین، معاملات باید به طور همزمان انجام شوند تا ریسک بازار یا احتمال تغییر قیمت یک بازار قبل از تکمیل هر دو معامله به حداقل برسد.

    :param df:
    :return:
    '''
    pass
def index_fund_rebalancing(df):
    """
    پرتفوی صندوق‌های شاخص صندوق‌های سرمایه‌گذاری مشترک مانند حساب‌های بازنشستگی فردی و صندوق‌های بازنشستگی به طور منظم برای منعکس‌کننده قیمت‌های جدید دارایی‌های اساسی صندوق تعدیل می‌شوند. "تعادل مجدد" فرصت هایی را برای معامله گران الگوریتمی ایجاد می کند که بسته به تعداد سهام صندوق شاخص، از معاملات مورد انتظار سرمایه گذاری می کنند. معاملات توسط سیستم های معاملاتی الگوریتمی انجام می شود تا بهترین قیمت ها، هزینه های کم و نتایج به موقع را در اختیار داشته باشند.
    :param df:
    :return:
    """
    pass
def mean_reversion(df):
    pass
def market_timing(df):
    pass

############################################
# What is the best algo trading strategy?
# Weighted Average Price Strategy:
# This is also one of the most efficient algo trading strategies. It can either be based on volume weighted average price or time-weighted average price. In this strategy, the orders are large but they are not released at one go.25 May 2018
# https://www.adigitalblogger.com/algo-trading/algo-trading-strategies/
def weighted_average_price(df):
    pass

############################################
# What algorithms do stock traders use?
# Most algo-trading today is high-frequency trading (HFT), which attempts to capitalize on placing a large number of orders at rapid speeds across multiple markets and multiple decision parameters based on preprogrammed instructions.
# https://www.investopedia.com/articles/active-trading/101014/basics-algorithmic-trading-concepts-and-examples.asp
def high_frequency_trading_HFT(df):
    pass

##############################################
# DataCamp : Python For Finance Tutorial: Algorithmic Trading
# common strategy
# https://www.datacamp.com/community/tutorials/finance-python-trading#common-trading-strategies


##############################################
# 8 Best Python Libraries for Algorithmic Trading
# 1. FinTA
# 2. Zipline
# 3. CCXT
# 4. Freqtrade
# 5. YFinance
# 6. Backtrader
# 7. TensorTrade
# 8. Trump2Cash
# https://dev.to/sewinter/8-best-python-libraries-for-algorithmic-trading-1af8

