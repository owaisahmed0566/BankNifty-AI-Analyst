from data_collector import download_market_data
from option_data_collector import get_option_chain
from option_analysis import calculate_option_metrics
from report_generator import generate_report


def run_analysis():

    print("Starting Bank Nifty AI Analyst...")


    # Market data

    market = download_market_data()


    # Option chain

    option_chain = get_option_chain(
        "BANKNIFTY"
    )


    if option_chain is None:

        print(
            "Option data unavailable"
        )

        return



    option_result = calculate_option_metrics(
        option_chain
    )


    print("\nOPTION ANALYSIS")

    print(option_result)



    print(
        "\nAnalysis completed"
    )



if __name__ == "__main__":

    run_analysis()
