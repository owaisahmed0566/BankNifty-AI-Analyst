import requests
import pandas as pd


def get_option_chain(symbol="BANKNIFTY"):

    url = (
        "https://www.nseindia.com/api/option-chain-indices"
        f"?symbol={symbol}"
    )


    headers = {

        "User-Agent":
        "Mozilla/5.0",

        "Accept":
        "application/json"

    }


    session = requests.Session()


    try:

        response = session.get(
            url,
            headers=headers,
            timeout=10
        )


        data = response.json()


        records = []


        for item in data["records"]["data"]:

            strike = item["strikePrice"]


            if "CE" in item:

                records.append({

                    "Strike": strike,

                    "Type": "CE",

                    "OI":
                    item["CE"]["openInterest"],

                    "Change_OI":
                    item["CE"]["changeinOpenInterest"]

                })


            if "PE" in item:

                records.append({

                    "Strike": strike,

                    "Type": "PE",

                    "OI":
                    item["PE"]["openInterest"],

                    "Change_OI":
                    item["PE"]["changeinOpenInterest"]

                })


        return pd.DataFrame(records)



    except Exception as e:


        print(
            "Option chain error:",
            e
        )


        return None



if __name__ == "__main__":

    chain = get_option_chain()

    print(chain.head())
