def decide_trade(
    trend,
    option_bias,
    risk_score
):

    if (
        trend == "Bullish"
        and option_bias == "Bullish"
        and risk_score >= 70
    ):

        return {

            "Decision":
            "BUY CALL",

            "Reason":
            "Trend and options agree"

        }


    elif (
        trend == "Bearish"
        and option_bias == "Bearish"
        and risk_score >=70
    ):

        return {

            "Decision":
            "BUY PUT",

            "Reason":
            "Bearish confirmation"

        }


    else:

        return {

            "Decision":
            "NO TRADE",

            "Reason":
            "Conditions not strong enough"

        }
