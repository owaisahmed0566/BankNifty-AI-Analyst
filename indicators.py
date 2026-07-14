import pandas as pd
import ta


def calculate_indicators(data):

    df = data.copy()

    # EMA
    df["EMA_9"] = ta.trend.ema_indicator(
        df["Close"], window=9
    )

    df["EMA_20"] = ta.trend.ema_indicator(
        df["Close"], window=20
    )

    df["EMA_50"] = ta.trend.ema_indicator(
        df["Close"], window=50
    )

    df["EMA_200"] = ta.trend.ema_indicator(
        df["Close"], window=200
    )

    # RSI
    df["RSI"] = ta.momentum.rsi(
        df["Close"], window=14
    )

    # MACD
    df["MACD"] = ta.trend.macd(
        df["Close"]
    )

    # ATR
    df["ATR"] = ta.volatility.average_true_range(
        df["High"],
        df["Low"],
        df["Close"]
    )

    # VWAP
    df["VWAP"] = (
        (df["Close"] * df["Volume"]).cumsum()
        /
        df["Volume"].cumsum()
    )

    return df
