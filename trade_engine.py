def decide_trade(
    trend,
    option_bias,
    risk_score,
    near_support,
    near_resistance
):

    decision = "WAIT"

    reasons = []


    # Bullish setup

    if (
        trend == "Bullish"
        and option_bias == "Bullish"
        and risk_score >= 80
    ):

        if near_support:

            decision = "BUY CALL"

            reasons.append(
                "Bullish confirmation near support"
            )

        else:

            reasons.append(
                "Bullish but not at ideal entry zone"
            )


    # Bearish setup

    elif (
        trend == "Bearish"
        and option_bias == "Bearish"
        and risk_score >= 80
    ):

        if near_resistance:

            decision = "BUY PUT"

            reasons.append(
                "Bearish confirmation near resistance"
            )

        else:

            reasons.append(
                "Bearish but entry zone not confirmed"
            )


    else:

        reasons.append(
            "Conditions not strong enough"
        )


    return {

        "Decision": decision,

        "Reasons": reasons

    }



if __name__ == "__main__":

    print(
        "Trade Engine Ready"
    )
