def calculate_support_resistance(data):

    df = data.copy()


    previous = df.iloc[-2]


    high = float(previous["High"])
    low = float(previous["Low"])
    close = float(previous["Close"])


    pivot = (
        high + low + close
    ) / 3


    resistance_1 = (
        2 * pivot
    ) - low


    resistance_2 = (
        pivot + high - low
    )


    support_1 = (
        2 * pivot
    ) - high


    support_2 = (
        pivot - high + low
    )


    levels = {


        "Previous High":
        round(high,2),


        "Previous Low":
        round(low,2),


        "Pivot":
        round(pivot,2),


        "Resistance 1":
        round(resistance_1,2),


        "Resistance 2":
        round(resistance_2,2),


        "Support 1":
        round(support_1,2),


        "Support 2":
        round(support_2,2)

    }


    return levels



if __name__ == "__main__":

    print(
        "Support Resistance Engine Ready"
    )
