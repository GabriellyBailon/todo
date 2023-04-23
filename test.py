import pandas as pd
import yfinance as yf

msft = yf.Ticker("PETR4.SA")

# Obtém todas as informações da ação
msft.info

# Obtém dados históricos de mercado para a ação
hist = msft.history(period="max")

for data, row in hist.iterrows():
    breakpoint()
    open = row.Open,
    close = row.Close,
    high = row.High,

