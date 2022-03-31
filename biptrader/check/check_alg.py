""" check_alg :
    3/31/2022 8:04 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

class CheckTradeAlgorithm:

    def __init__(self,df=None,INVESTMENT_AMOUNT_DOLLARS=100,price_column="Close",date_column="Date"):
        self.df = df
        self.INVESTMENT_AMOUNT_DOLLARS=INVESTMENT_AMOUNT_DOLLARS
        self.price_column = price_column
        self.date_column = date_column
        self.calculation_mode = "single_hold" # single_hold | waterfall_hold | expo_waterfall_hold
        self.waterfall_hold_pct = 0.1
        self.expo_waterfall_hold_rate = 1.5

    def signal(self,fn_recommendation):
        df = self.df
        counter =0
        for i,row in df.iterrows():
            if counter>0:
                ticker_df_before_date = df[df.Date<=row[self.date_column]]
                signal = fn_recommendation(ticker_df_before_date)
                df._set_value(i,"signal",signal)
            counter+=1

    def calculate_profit(self):
        if self.calculation_mode=="waterfall_hold":
            self._calculate_waterfall_profit()
        elif self.calculation_mode=="expo_waterfall_hold":
            self._calculate_expo_waterfall_profit()
        else:
            self._calculate_single_profit()

    def _calculate_single_profit(self):
        if not "revenue" in self.df.columns or not "profit" in self.df.columns :
            self.df=self.df.assign(revenue=[None]*len(self.df),profit=[None]*len(self.df))

        counter =0
        df = self.df

        HOLDING_QUANTITY=None
        for i,row in df.iterrows():
            if counter>0:
                current_price = float(row[self.price_column])
                if row["signal"]=="BUY" and not HOLDING_QUANTITY:
                    HOLDING_QUANTITY = round(self.INVESTMENT_AMOUNT_DOLLARS/current_price,5)
                    df._set_value(i,"revenue",-self.INVESTMENT_AMOUNT_DOLLARS)
                    df._set_value(i,"profit",0)
                elif row["signal"]=="SELL" and HOLDING_QUANTITY:
                    revenue = HOLDING_QUANTITY*current_price
                    profit=revenue-self.INVESTMENT_AMOUNT_DOLLARS
                    df._set_value(i,"revenue",revenue)
                    df._set_value(i,"profit",profit)
                    self.INVESTMENT_AMOUNT_DOLLARS=revenue
                    HOLDING_QUANTITY=None
            counter+=1

    def _calculate_waterfall_profit(self):
        pass

    def _calculate_expo_waterfall_profit(self):
        pass

    def get_revenue(self):
        return self.df["revenue"].sum()

    def get_profit(self):
        return self.df[self.df.signal=="SELL"]["profit"].sum()

    def get_buy_signal_count(self):
        return len(self.df[self.df.signal=="BUY"])

    def get_sell_signal_count(self):
        return len(self.df[self.df.signal=="SELL"])

    def get_summary(self):
        return "{revenue:%f,profit:%f,remain:%f,buy_signal_count:%i,sell_signal_count:%i}"\
               %(self.get_revenue(),self.get_profit(),self.INVESTMENT_AMOUNT_DOLLARS
                 ,self.get_buy_signal_count(),self.get_sell_signal_count())

