import yfinance as yf # yahoo finance to download historical prices, trading volume, and market data for stocks
import pandas as pd # reading datas
import numpy as np
import matplotlib.pyplot as mpt # data visualization and plotting tool

amazon = yf.download("AMZN", start="2015-01-01", end="2020-01-01") 
# choose stocks in the nasdaq and matched it based on the start and end of the stocks 
ticker=["GOOGL", "AMZN", "NKE"]
stocks = yf.download(ticker, start="2015-01-01", end="2020-01-01")
stocks.Close # showing the close row only
stocs.head() # showing the first five columns
stocks.tail() # showing the last five columns
stocks.info() # showing 
stocks.to_csv("quantfinance2027.csv") # move the downloaded stocks to a new csv file



