""" test_MACD_crossover_points_RSI_of_point :
    3/31/2022 9:09 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

from unittest import TestCase

import pandas as pd

from biptrader.algorithms import MACD_crossover_points_RSI_of_point


class TestMACD_crossover_points_RSI_of_point(TestCase):
    def test_recommendation(self):
        alg = MACD_crossover_points_RSI_of_point()
        df = pd.read_csv("../data/dash-daily-20170101-20220330-yahoo.csv", header=0)
        df.sort_values(by=["Date"],ascending=True,inplace=True)
        signal = alg.recommendation(df)
        print("signal=",signal)


