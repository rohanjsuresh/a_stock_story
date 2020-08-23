import json
import urllib.request
from bs4 import BeautifulSoup
import pandas
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import pandas as pd


# description:
#   get tickers for the DOW 30 from the Yahoo Finance website (https://finance.yahoo.com/quote/%5EDJI/components/)
# args:
#   
# return:
#   tickers - array with all 30 tickers in the DOW 30
def get_dow_tickers():
    url = "https://finance.yahoo.com/quote/%5EDJI/components/"

    # get html
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    html = mybytes.decode("utf8")
    fp.close()

    # from here extract full tage from table in HTML with the tickers
    soup = BeautifulSoup(html, features="lxml")
    tags = soup.findAll("a", {"class": "C($linkColor) Cur(p) Td(n) Fw(500)"})

    # get tickers from tags
    tickers = []
    for tag in tags:
        tickers.append(tag.string)
    return tickers

# description:
#   given an array of tickers and a time period return the average highs and lows over that time period
# args:
#   tickers - array of ticker symbols that we want to get the avg highs and lows for
#   start - start date as a string in the form YYYY-MM-DD
#   end - end date as a string in the form YYYY-MM-DD
# return:
#   avg_high - dictionary of avg high prices over the time period for each ticker with ticker as key
#   avg_low - dictionary of avg low prices over the time period for each ticker with ticker as key
#   data_not_available - arry containing tickers that did not have data for the given time frame 
def get_avg_prices(tickers, start, end):

    avg_high = {}
    avg_low = {}
    data_not_available = []

    # iterate through each ticker and get average high and low for each ticker
    for ticker in tickers:
        # try and get avg high price
        try:
            data = pdr.get_data_yahoo(ticker, start=start, end=end)
            # print(data['High'].mean())
            # print(data['Low'].mean())
            avg_high[ticker] = data['High'].mean()
            avg_low[ticker] = data['Low'].mean()
        # else add ticker to data_not_available 
        except:
            data_not_available.append(ticker)
    return avg_high, avg_low,data_not_available


tickers = get_dow_tickers()
avg_high, avg_low,data_not_available = get_avg_prices(tickers, "2019-01-01", "2019-02-01")