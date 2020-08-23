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
            print(data['High'].mean())
            print(data['Low'].mean())
            avg_high[ticker] = data['High'].mean()
            avg_low[ticker] = data['Low'].mean()
        # else add ticker to data_not_available 
        except:
            data_not_available.append(ticker)
    return avg_high, avg_low,data_not_available

# description:
#   given a start date (YYYY-MM) and and end date (YYYY-MM) and a time interval x, return all the
#   pairs of time intervals from start to end increasing by x.
# args:
#   start - string containing start date in the form YYYY-MM
#   end - string containing end date in the form YYYY-MM
#   interval - length of time interval we want in months
# return:
#   intervals - array with each value being a tuple with its own start date and end date of interval length
def get_time_intervals(start, end, interval):

    # split start/end dates into year and month variables
    start_year, start_month = start.split("-")
    end_year, end_month = end.split("-")

    # convert string to int
    start_year = int(start_year)
    start_month = int(start_month)
    end_year = int(end_year)
    end_month = int(end_month)

    intervals = []
    
    # get dates that are each interval length 
    while (start_year < end_year or start_month < end_month):
        temp_year = start_year
        temp_month = start_month

        start_month += interval
        # if the month is already december, go to new year date
        if start_month > 12:
            start_year += int(start_month / 12)
            start_month = (start_month) % 12

        # final end date should be end date specificed by user
        if start_year >= end_year and start_month >= end_month:
            start_year = end_year
            start_month = end_month

        # add new start - end interval to interval array
        start_str = str(temp_year) + "-" + str(temp_month) + "-" + "1"
        end_str = str(start_year) + "-" + str(start_month) + "-" + "1"
        intervals.append((start_str, end_str))
    return intervals