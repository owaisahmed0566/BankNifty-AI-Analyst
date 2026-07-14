import yfinance as yf
from datetime import datetime


def get_market_data():

    symbols = {
        "NIFTY50": "^NSEI",
        "BANKNIFTY": "^NSEBANK"
    }

    market_data = {}

    for name, symbol in symbols.items():

        data = yf.download(
            symbol,
            period="5d",
            interval="5m",
            progress=False
        )

        latest = data.iloc[-1]

        market_data[name] = {
            "price": float(latest["Close"]),
            "high": float(latest["High"]),
            "low": float(latest["Low"]),
            "volume": int(latest["Volume"])
        }

    market_data["time"] = str(datetime.now())

    return market_data


if __name__ == "__main__":

    result = get_market_data()

    print(result)
