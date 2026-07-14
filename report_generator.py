def generate_report(data):

    print("""
==============================
BANK NIFTY AI ANALYST REPORT
==============================

Market:
""", data["Market"])


    print("""

Trend:
""", data["Trend"])


    print("""

Support / Resistance:
""", data["Levels"])


    print("""

Option Analysis:
""", data["Options"])


    print("""

Decision:
""", data["Trade"])


    print("""

Risk:

""", data["Risk"])


    print("""
==============================
""")
