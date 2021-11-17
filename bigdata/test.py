import yfinance as yf
import pandas as pd

ticker_list = pd.read_csv("tickers.csv")
ticker_list_name = ticker_list['name']
name = 1
count = 0
item_count = 0
for name in ticker_list_name:
    if name == "Bitcoin":
        item_count = count
        print(name)
    count = count + 1
print(item_count)
print(ticker_list['symbol'][item_count])



