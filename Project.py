import yfinance as yf # yahoo finance to download historical prices, trading volume, and market data for stocks
import pandas as pd # reading datas
import numpy as np
import matplotlib as mpt # data visualization and plotting tool

amazon = yf.download("AMZN", start="2015-01-01", end="2020-01-01") 
# choose stocks in the nasdaq and matched it based on the start and end of the stocks 


