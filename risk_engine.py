def evaluate_trade(
    trend,
    option_bias,
    rsi,
    near_resistance,
    near_support
):

    score = 0
    reasons = []
    warnings = []


    # Trend check

    if trend == "Bullish":
        score += 25
        reasons.append("Trend is bullish")

    elif trend == "Bearish":
        score += 25
        reasons.append("Trend is bearish")

    else:
        warnings.append("No clear trend")


    # Option confirmation

    if option_bias == trend:
        score += 25
        reasons.append(
            "Option data confirms trend"
        )

    else:
        warnings.append(
            "Option data conflict"
        )


    # RSI check

    if 40 <= rsi <= 70:
        score += 15
        reasons.append(
            "RSI in healthy zone"
        )

    elif rsi > 70:
        warnings.append(
            "Market may be overbought"
        )


    # Support resistance risk

    if near_resistance:
        warnings.append(
            "Price near resistance"
        )

        score -= 10


    if near_support:
        score += 10
        reasons.append(
            "Price near support"
        )


    # Final decision

    if score >= 80:

        decision = "APPROVED"

    else:

        decision = "REJECTED"



    return {

        "Score": score,

        "Decision": decision,

        "Reasons": reasons,

        "Warnings": warnings

    }



if __name__ == "__main__":

    print("Risk Engine Ready")
