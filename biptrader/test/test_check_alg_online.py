""" test_check_alg_online :
    3/31/2022 10:34 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

from unittest import TestCase
# from biptrader.check.check_alg_online import CheckTradeAlgorithmOnline
# from biptrader.algorithms import MACD_crossover_points_RSI_of_point
from biptrader import CheckTradeAlgorithmOnline, Plot
from biptrader import MACD_crossover_points_RSI_of_point


class TestCheckTradeAlgorithmOnline(TestCase):


    def test_check_all(self):
        # self.fail()
        checker = CheckTradeAlgorithmOnline()
        alg = MACD_crossover_points_RSI_of_point()
        checker.recommander_title="MACD_crossover_points_RSI_of_point"
        checker.check_all(alg.recommendation,years=5)
        # checker.check_all(getattr(alg,"recommendation"))
        print(checker.df_conclusion.to_string())

    def test_plot_ETHUSD(self):
        checker = CheckTradeAlgorithmOnline()
        alg = MACD_crossover_points_RSI_of_point()
        checker.recommander_title="MACD_crossover_points_RSI_of_point"
        checker.check_lastyears(alg.recommendation, "ETH-USD")
        Plot().show_with_signals(checker.df,checker.get_summary())

    def test_plot_DASHUSD(self):
        checker = CheckTradeAlgorithmOnline()
        alg = MACD_crossover_points_RSI_of_point()
        checker.recommander_title="MACD_crossover_points_RSI_of_point"
        checker.check_lastyears(alg.recommendation, "DASH-USD",years=1)
        Plot().show_with_signals(checker.df,checker.get_summary())

    def test_plot_DASHUSD_lastmonth_1h(self):
        checker = CheckTradeAlgorithmOnline()
        alg = MACD_crossover_points_RSI_of_point()
        checker.recommander_title="MACD_crossover_points_RSI_of_point"
        checker.check_lastmonths(alg.recommendation, "DASH-USD",months=1,interval="1h")
        Plot().show_with_signals(checker.df,checker.get_summary())

    def test_plot_DASHUSD_lastday_1m(self):
        checker = CheckTradeAlgorithmOnline()
        alg = MACD_crossover_points_RSI_of_point()
        checker.recommander_title="MACD_crossover_points_RSI_of_point"
        checker.check_lastdays(alg.recommendation, "DASH-USD",days=1,interval="1m")
        Plot().show_with_signals(checker.df,checker.get_summary())
