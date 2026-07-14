import pandas as pd


def calculate_support_resistance(data):

    df = data.copy()

    # Previous day levels
    previous_high = df["High"].iloc[-2]
    previous_low = df["Low"].iloc[-2]
    previous_close = df["Close"].iloc[-2]


    # Pivot calculation
    pivot = (
        previous_high +
        previous_low +
        previous_close
    ) / 3


    resistance_1 = (2 * pivot) - previous_low

    resistance_2 = (
        pivot +
        previous_high -
        previous_low
    )


    support_1 = (2 * pivot) - previous_high

    support_2 = (
        pivot -
        previous_high +
        previous_low
    )


    levels = {

        "Previous Day High": round(previous_high, 2),

        "Previous Day Low": round(previous_low, 2),

        "Pivot": round(pivot, 2),

        "Resistance 1": round(resistance_1, 2),

        "Resistance 2": round(resistance_2, 2),

        "Support 1": round(support_1, 2),

        "Support 2": round(support_2, 2)

    }


    return levels



if __name__ == "__main__":

    print("Support Resistance Engine Ready")
