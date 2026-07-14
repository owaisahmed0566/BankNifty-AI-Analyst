def generate_report(
    market,
    indicators,
    levels,
    option_data,
    risk
):

    report = []


    report.append(
        "===== BANK NIFTY AI ANALYSIS ====="
    )


    report.append(
        f"Market: {market}"
    )


    report.append(
        "\n--- Technical Analysis ---"
    )


    report.append(
        f"RSI: {indicators.get('RSI')}"
    )

    report.append(
        f"EMA Trend: {indicators.get('Trend')}"
    )

    report.append(
        f"VWAP Position: {indicators.get('VWAP')}"
    )


    report.append(
        "\n--- Support Resistance ---"
    )


    for key, value in levels.items():

        report.append(
            f"{key}: {value}"
        )


    report.append(
        "\n--- Option Analysis ---"
    )


    for key, value in option_data.items():

        report.append(
            f"{key}: {value}"
        )


    report.append(
        "\n--- Risk Engine ---"
    )


    report.append(
        f"Decision: {risk['Decision']}"
    )


    report.append(
        f"Confidence Score: {risk['Score']}%"
    )


    report.append(
        "\nReasons:"
    )


    for reason in risk["Reasons"]:

        report.append(
            f"✔ {reason}"
        )


    report.append(
        "\nWarnings:"
    )


    for warning in risk["Warnings"]:

        report.append(
            f"⚠ {warning}"
        )


    report.append(
        "\n=============================="
    )


    return "\n".join(report)



if __name__ == "__main__":

    print(
        "Report Generator Ready"
    )
