import pandas as pd


def calculate_option_metrics(option_chain):

    result = {}


    # Separate Call and Put data

    calls = option_chain[
        option_chain["Type"] == "CE"
    ]

    puts = option_chain[
        option_chain["Type"] == "PE"
    ]


    # Total Open Interest

    total_call_oi = calls["OI"].sum()

    total_put_oi = puts["OI"].sum()


    # PCR

    if total_call_oi > 0:

        pcr = total_put_oi / total_call_oi

    else:

        pcr = 0



    result["Total CE OI"] = total_call_oi

    result["Total PE OI"] = total_put_oi

    result["PCR"] = round(pcr, 2)



    # Resistance

    highest_call = calls.loc[
        calls["OI"].idxmax()
    ]


    # Support

    highest_put = puts.loc[
        puts["OI"].idxmax()
    ]



    result["Resistance"] = (
        highest_call["Strike"]
    )


    result["Support"] = (
        highest_put["Strike"]
    )


    # Bias

    if pcr > 1:

        result["Option Bias"] = "Bullish"

    elif pcr < 0.7:

        result["Option Bias"] = "Bearish"

    else:

        result["Option Bias"] = "Neutral"



    return result



if __name__ == "__main__":

    print("Option Engine Ready")
