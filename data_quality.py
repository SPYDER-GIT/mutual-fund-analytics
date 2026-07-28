import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 60)
print("FUND MASTER EXPLORATION")
print("=" * 60)

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())

print("\nNumber of unique AMFI Codes:")
print(fund_master["amfi_code"].nunique())

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

missing_codes = set(fund_master["amfi_code"]) - set(nav_history["amfi_code"])

if len(missing_codes) == 0:
    print("All AMFI Codes exist in NAV History.")
else:
    print("Missing Codes:")
    print(missing_codes)

print("=" * 60)
print("DATA QUALITY SUMMARY")
print("=" * 60)

print(f"Fund Master Records : {len(fund_master)}")
print(f"NAV History Records : {len(nav_history)}")
print(f"Missing AMFI Codes : {len(missing_codes)}")