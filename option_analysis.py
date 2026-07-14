def analyze_option_chain(option_data):

    analysis = {}


    # Total Call and Put Open Interest

    total_call_oi = option_data["CE_OI"].sum()

    total_put_oi = option_data["PE_OI"].sum()


    # PCR Calculation

    if total_call_oi != 0:
        pcr = total_put_oi / total_call_oi
    else:
        pcr = 0


    analysis["Total Call OI"] = total_call_oi

    analysis["Total Put OI"] = total_put_oi

    analysis["PCR"] = round(pcr, 2)



    # Highest resistance and support zones

    highest_call = option_data.loc[
        option_data["CE_OI"].idxmax()
    ]


    highest_put = option_data.loc[
        option_data["PE_OI"].idxmax()
    ]



    analysis["Call Resistance Strike"] = (
        highest_call["Strike"]
    )


    analysis["Put Support Strike"] = (
        highest_put["Strike"]
    )



    # Basic interpretation

    if pcr > 1:
        analysis["Market Bias"] = "Bullish"

    elif pcr < 0.7:
        analysis["Market Bias"] = "Bearish"

    else:
        analysis["Market Bias"] = "Neutral"


    return analysis



if __name__ == "__main__":

    print("Option Analysis Engine Ready")
