import yfinance as yf
from datetime import datetime


def download_market_data():

    symbols = {
        "NIFTY50": "^NSEI",
        "BANKNIFTY": "^NSEBANK",
        "INDIAVIX": "^INDIAVIX"
    }

    market_data = {}

    for name, symbol in symbols.items():

        try:

            df = yf.download(
                symbol,
                period="1mo",
                interval="5m",
                progress=False
            )

            df.dropna(inplace=True)

            market_data[name] = df


        except Exception as e:

            market_data[name] = {
                "error": str(e)
            }


    return market_data



if __name__ == "__main__":

    data = download_market_data()

    for market, df in data.items():

        print("\n", market)

        print(df.tail())
