import os
import pandas as pd

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

print("=" * 60)
print("DAY 2 - DATA CLEANING")
print("=" * 60)

# --------------------------------------------------
# Clean nav_history.csv
# --------------------------------------------------

print("\nCleaning nav_history.csv...")

nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])

duplicates = nav.duplicated().sum()
nav = nav.drop_duplicates()

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

invalid_nav = (nav["nav"] <= 0).sum()
nav = nav[nav["nav"] > 0]

nav.to_csv("data/processed/cleaned_nav_history.csv", index=False)

print("Saved cleaned_nav_history.csv")

# --------------------------------------------------
# Clean investor_transactions.csv
# --------------------------------------------------

print("\nCleaning investor_transactions.csv...")

transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", transactions.shape)

# Convert transaction date
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# Standardize transaction type
transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep only valid transaction types
valid_types = ["Sip", "Lumpsum", "Redemption"]
transactions = transactions[
    transactions["transaction_type"].isin(valid_types)
]

# Remove invalid amount
invalid_amount = (transactions["amount_inr"] <= 0).sum()
transactions = transactions[transactions["amount_inr"] > 0]

# Standardize KYC status
transactions["kyc_status"] = (
    transactions["kyc_status"]
    .str.strip()
    .str.title()
)

valid_kyc = ["Verified", "Pending"]
transactions = transactions[
    transactions["kyc_status"].isin(valid_kyc)
]

# Remove duplicates
duplicates = transactions.duplicated().sum()
transactions = transactions.drop_duplicates()

# Save cleaned data
output_path = "data/processed/cleaned_investor_transactions.csv"
transactions.to_csv(output_path, index=False)

print("Duplicates Removed :", duplicates)
print("Invalid Amount Rows:", invalid_amount)
print("Final Shape        :", transactions.shape)
print("Saved To           :", output_path)

# --------------------------------------------------
# Clean scheme_performance.csv
# --------------------------------------------------

print("\nCleaning scheme_performance.csv...")

performance = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", performance.shape)

# Columns that should be numeric
numeric_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

# Convert to numeric
for column in numeric_columns:
    performance[column] = pd.to_numeric(
        performance[column],
        errors="coerce"
    )

# Count missing numeric values
missing_numeric = performance[numeric_columns].isna().sum().sum()

# Expense ratio validation
invalid_expense = (
    (performance["expense_ratio_pct"] < 0.1) |
    (performance["expense_ratio_pct"] > 2.5)
).sum()

# Remove duplicate rows
duplicates = performance.duplicated().sum()
performance = performance.drop_duplicates()

# Save cleaned file
output_path = "data/processed/cleaned_scheme_performance.csv"
performance.to_csv(output_path, index=False)

print("Missing Numeric Values :", missing_numeric)
print("Invalid Expense Ratio  :", invalid_expense)
print("Duplicates Removed     :", duplicates)
print("Final Shape            :", performance.shape)
print("Saved To               :", output_path)

# --------------------------------------------------
# Clean remaining datasets
# --------------------------------------------------

print("\nCleaning remaining datasets...")

remaining_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in remaining_files:

    print(f"\nCleaning {file}...")

    df = pd.read_csv(f"data/raw/{file}")

    original_rows = len(df)

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert date/month columns if present
    for column in df.columns:
        if "date" in column.lower() or column.lower() == "month":
            try:
                df[column] = pd.to_datetime(df[column])
            except Exception:
                pass

    output_file = f"data/processed/cleaned_{file}"

    df.to_csv(output_file, index=False)

    print(f"Original Rows : {original_rows}")
    print(f"Final Rows    : {len(df)}")
    print(f"Saved To      : {output_file}")