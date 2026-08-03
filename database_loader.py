from sqlalchemy import create_engine
import pandas as pd
import os

print("=" * 60)
print("LOADING CLEANED DATA INTO SQLITE DATABASE")
print("=" * 60)

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

processed_folder = "data/processed"

csv_files = [
    "cleaned_01_fund_master.csv",
    "cleaned_nav_history.csv",
    "cleaned_03_aum_by_fund_house.csv",
    "cleaned_04_monthly_sip_inflows.csv",
    "cleaned_05_category_inflows.csv",
    "cleaned_06_industry_folio_count.csv",
    "cleaned_scheme_performance.csv",
    "cleaned_investor_transactions.csv",
    "cleaned_09_portfolio_holdings.csv",
    "cleaned_10_benchmark_indices.csv"
]

for file in csv_files:

    path = os.path.join(processed_folder, file)

    df = pd.read_csv(path)

    table_name = file.replace(".csv", "").replace("cleaned_", "")

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} loaded ({len(df)} rows)")

print("\nDatabase created successfully!")