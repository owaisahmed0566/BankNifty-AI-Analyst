from data_collector import download_market_data
from option_data_collector import get_option_chain
from option_analysis import calculate_option_metrics
from trend_engine import detect_trend
from trade_engine import decide_trade
from claude_prompt import create_claude_prompt


def run_analysis():

    print("Starting Bank Nifty AI Analyst...")


    # 1. Collect market data

    market_data = download_market_data()


    bank_nifty = market_data["BANKNIFTY"]


    latest = bank_nifty.iloc[-1]


    current_price = latest["Close"]



    # 2. Option Chain

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



    # 3. Prepare trend data

    # Temporary placeholder
    # Will connect indicators next

    trend_result = {

        "Trend": "Unknown"

    }



    # 4. Trade decision

    trade = decide_trade(

        trend_result["Trend"],

        option_result["Option Bias"],

        0,

        False,

        False

    )



    # 5. Create Claude prompt

    prompt = create_claude_prompt(

        market=current_price,

        trend=trend_result,

        indicators="Pending",

        levels="Pending",

        option_data=option_result,

        trade=trade,

        risk_data="Pending"

    )


    print("\n========== CLAUDE ANALYSIS ==========")

    print(prompt)



if __name__ == "__main__":

    run_analysis()
