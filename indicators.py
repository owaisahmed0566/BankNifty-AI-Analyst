import ta


def calculate_indicators(data):

    df = data.copy()


    df["EMA_20"] = ta.trend.ema_indicator(
        df["Close"],
        window=20
    )


    df["EMA_50"] = ta.trend.ema_indicator(
        df["Close"],
        window=50
    )


    df["RSI"] = ta.momentum.rsi(
        df["Close"],
        window=14
    )


    df["MACD"] = ta.trend.macd(
        df["Close"]
    )


    df["VWAP"] = (
        (df["Close"] * df["Volume"]).cumsum()
        /
        df["Volume"].cumsum()
    )


    latest = df.iloc[-1]


    summary = {

        "Price":
        round(float(latest["Close"]),2),

        "EMA20":
        round(float(latest["EMA_20"]),2),

        "EMA50":
        round(float(latest["EMA_50"]),2),

        "RSI":
        round(float(latest["RSI"]),2),

        "MACD":
        round(float(latest["MACD"]),2),

        "VWAP":
        round(float(latest["VWAP"]),2)

    }


    return df, summary



if __name__ == "__main__":

    print(
        "Indicator Engine Ready"
    )
