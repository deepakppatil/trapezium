import yfinance as yf
import mplfinance as mpf

# Set the ticker symbol and timeframe
ticker = "RELIANCE.NS"
start_date = "2021-01-01"
end_date = "2022-02-25"

# Fetch the stock data using yfinance
data = yf.download(ticker, start=start_date, end=end_date)


# Plot a candlestick chart with 10-day SMA and 20-day EMA
mpf.plot(data, type="candle", mav=(10, 20), volume=True)