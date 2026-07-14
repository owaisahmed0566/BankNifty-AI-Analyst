def detect_trend(indicators):

    score = 0
    reasons = []


    # EMA analysis

    if indicators["EMA_20"] > indicators["EMA_50"]:

        score += 30

        reasons.append(
            "Short term trend above long term trend"
        )

    else:

        score -= 30

        reasons.append(
            "Short term trend below long term trend"
        )


    # RSI

    rsi = indicators["RSI"]


    if rsi > 50:

        score += 20

        reasons.append(
            "RSI supports bullish momentum"
        )

    else:

        score -= 20

        reasons.append(
            "RSI shows weak momentum"
        )


    # MACD

    if indicators["MACD"] > 0:

        score += 25

        reasons.append(
            "MACD positive"
        )

    else:

        score -= 25

        reasons.append(
            "MACD negative"
        )


    # Final decision

    if score >= 40:

        trend = "Bullish"

    elif score <= -40:

        trend = "Bearish"

    else:

        trend = "Neutral"


    return {

        "Trend": trend,

        "Score": score,

        "Reasons": reasons

    }


if __name__ == "__main__":

    print("Trend Engine Ready")
