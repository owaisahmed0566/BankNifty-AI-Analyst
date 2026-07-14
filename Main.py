from data_collector import download_market_data
from option_data_collector import get_option_chain

from indicators import calculate_indicators
from support_resistance import calculate_support_resistance

from option_analysis import calculate_option_metrics
from trend_engine import detect_trend
from trade_engine import decide_trade

from risk_engine import evaluate_trade

from claude_prompt import create_claude_prompt



def run_analysis():

    print(
        "Starting Bank Nifty AI Analyst..."
    )


    # -------------------------
    # Market Data
    # -------------------------

    market_data = download_market_data()


    bank_nifty = market_data["BANKNIFTY"]


    current_price = float(
        bank_nifty["Close"].iloc[-1]
    )



    # -------------------------
    # Indicators
    # -------------------------

    indicator_df, indicators = calculate_indicators(
        bank_nifty
    )



    # -------------------------
    # Support Resistance
    # -------------------------

    levels = calculate_support_resistance(
        bank_nifty
    )



    # -------------------------
    # Option Chain
    # -------------------------

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



    # -------------------------
    # Trend
    # -------------------------

    trend = detect_trend(
        indicators
    )



    # -------------------------
    # Risk
    # -------------------------

    risk = evaluate_trade(

        trend["Trend"],

        option_result["Option Bias"],

        80,

        False,

        False

    )



    # -------------------------
    # Trade Decision
    # -------------------------

    trade = decide_trade(

        trend["Trend"],

        option_result["Option Bias"],

        risk["Score"],

        False,

        False

    )



    # -------------------------
    # Claude Prompt
    # -------------------------

    prompt = create_claude_prompt(

        market=current_price,

        trend=trend,

        indicators=indicators,

        levels=levels,

        option_data=option_result,

        trade=trade,

        risk_data=risk

    )


    print(
        "\n========== AI ANALYSIS =========="
    )

    print(prompt)



if __name__ == "__main__":

    run_analysis()
