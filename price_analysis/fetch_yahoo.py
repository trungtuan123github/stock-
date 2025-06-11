import yfinance as yf
import os

def fetch_stock_data(ticker, start='2022-01-01', end=None):
    df = yf.download(ticker, start=start, end=end)
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv(f"data/raw/{ticker}.csv")
    return df