#read README
# this gets way more info then needed.
# I plan on using more and more data, and I
# wanted the ability to get more easily

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData

Akey = 'ALPHAVANTAGE_API_KEY'

fd = FundamentalData(key=Akey, output_format='pandas')
ts = TimeSeries(key=Akey, output_format='pandas')


#get monthly adjusted
class Gma():
    # "gets entire table"
    def Full(self, symbol):
        d, meta_data = ts.get_monthly_adjusted(symbol)
        return d


    # "gets opening stock price"
    def Open(self, symbol):
        d, meta_data = ts.get_monthly_adjusted(symbol)
        c = d['1. open']
        return c

    # "gets highest priced stock"
    def High(self, symbol):
        d, meta_data = ts.get_monthly_adjusted(symbol)
        c = d['2. high']
        return c

    # "gets lowest priced stock"
    def Low(self, symbol):
        d, meta_data = ts.get_monthly_adjusted(symbol)
        c = d['3. low']
        return c

    # "gets close price"
    def Close(self, symbol):
        d, meta_data = ts.get_monthly_adjusted(symbol)
        c = d['4. close']
        return c

    # "gets adjusted close price"
    def Aclose(self, symbol):
        d, meta_data = ts.get_monthly_adjusted(symbol)
        c = d['5. adjusted close']
        return c

    # "gets volume"
    def Volume(self, symbol):
        d, meta_data = ts.get_monthly_adjusted(symbol)
        c = d['6. volume']
        return c

    # "gets dividend amount"
    def Damount(self, symbol):
        d, meta_data = ts.get_monthly_adjusted(symbol)
        c = d['7. dividend amount']
        return c

#get current quote endpoint

