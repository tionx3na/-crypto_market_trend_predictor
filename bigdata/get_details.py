import yfinance as yf
import pandas as pd
import stringcase
import csv

ip = input("Enter the name of the coin: \n")
camel_ip = stringcase.capitalcase(ip)
ticker_list = pd.read_csv("tickers.csv")
ticker_list_name = ticker_list['name']
name = 1
count = 0
item_count = 0

for name in ticker_list_name:
    if name == camel_ip:
        item_count = count
    count = count + 1

if item_count == 0:
    print("Error!")
else:
    ticker = ticker_list['symbol'][item_count]

print(ticker)


coin = yf.Ticker(ticker)
info = coin.info
hist = coin.history(period="max")

with open('info.csv', 'w') as f:
    for key in info.keys():
        f.write("%s,%s\n"%(key,info[key]))

data = pd.DataFrame(data=hist)
print(data)
# data.to_csv("hist.csv")






