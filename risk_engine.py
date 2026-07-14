def evaluate_trade(
    trend,
    option_bias,
    indicators,
    levels,
    current_price
):

    score = 0
    reasons = []
    warnings = []


    # Trend confirmation

    if trend == "Bullish":

        score += 25
        reasons.append(
            "Trend supports bullish direction"
        )

    elif trend == "Bearish":

        score += 25
        reasons.append(
            "Trend supports bearish direction"
        )

    else:

        warnings.append(
            "No clear market trend"
        )


    # Option confirmation

    if option_bias == trend:

        score += 25
        reasons.append(
            "Option chain confirms trend"
        )

    else:

        warnings.append(
            "Option chain conflicts with trend"
        )


    # Momentum check

    rsi = indicators.get("RSI",0)


    if 45 <= rsi <= 65:

        score += 15

        reasons.append(
            "Momentum is acceptable"
        )

    else:

        warnings.append(
            "Momentum is weak or extreme"
        )


    # Final decision

    if score >= 70:

        decision = "LOW RISK"

    elif score >= 50:

        decision = "MEDIUM RISK"

    else:

        decision = "HIGH RISK"


    return {

        "Score": score,

        "Risk": decision,

        "Reasons": reasons,

        "Warnings": warnings

    }
