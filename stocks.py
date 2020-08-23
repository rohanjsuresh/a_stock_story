import json
import urllib.request
from bs4 import BeautifulSoup

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


tickers = get_dow_tickers()
print(tickers)