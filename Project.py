import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib as mpt

amazon = yf.download("AMZN", start="2015-01-01", end="2020-01-01") #
