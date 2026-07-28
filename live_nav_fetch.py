import requests
import pandas as pd
import os

# Create output folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# AMFI Codes
schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

print("=" * 60)
print("FETCHING LIVE NAV FOR 5 SCHEMES")
print("=" * 60)

for scheme_name, amfi_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        print("\n------------------------------------")
        print("Scheme:", data["meta"]["scheme_name"])
        print("Fund House:", data["meta"]["fund_house"])
        print("Latest NAV:", data["data"][0])

        df = pd.DataFrame(data["data"])

        filename = f"data/raw/{scheme_name}.csv"

        df.to_csv(filename, index=False)

        print("Saved:", filename)

    else:
        print("Failed:", amfi_code)

print("\nAll schemes downloaded successfully.")