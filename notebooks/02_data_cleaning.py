"""Clean raw mutual fund datasets and save processed CSV files."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent
RAW_FOLDER = PROJECT_ROOT / "data" / "raw"
PROCESSED_FOLDER = PROJECT_ROOT / "data" / "processed"


def clean_nav_history() -> pd.DataFrame:
    """Clean NAV history data and save the processed dataset."""
    input_path = RAW_FOLDER / "02_nav_history.csv"
    output_path = PROCESSED_FOLDER / "cleaned_nav_history.csv"

    nav = pd.read_csv(input_path)

    nav["date"] = pd.to_datetime(nav["date"])
    nav = nav.sort_values(["amfi_code", "date"])
    nav = nav.drop_duplicates()

    nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()
    nav = nav[nav["nav"] > 0]

    nav.to_csv(output_path, index=False)

    return nav


def clean_investor_transactions() -> pd.DataFrame:
    """Clean investor transaction data and save the processed dataset."""
    input_path = RAW_FOLDER / "08_investor_transactions.csv"
    output_path = PROCESSED_FOLDER / "cleaned_investor_transactions.csv"

    transactions = pd.read_csv(input_path)

    transactions["transaction_date"] = pd.to_datetime(
        transactions["transaction_date"]
    )

    transactions["transaction_type"] = (
        transactions["transaction_type"]
        .str.strip()
        .str.title()
    )

    valid_types = ["Sip", "Lumpsum", "Redemption"]
    transactions = transactions[
        transactions["transaction_type"].isin(valid_types)
    ]

    transactions = transactions[transactions["amount_inr"] > 0]

    transactions["kyc_status"] = (
        transactions["kyc_status"]
        .str.strip()
        .str.title()
    )

    valid_kyc = ["Verified", "Pending"]
    transactions = transactions[
        transactions["kyc_status"].isin(valid_kyc)
    ]

    transactions = transactions.drop_duplicates()

    transactions.to_csv(output_path, index=False)

    return transactions


def clean_scheme_performance() -> pd.DataFrame:
    """Clean scheme performance data and save the processed dataset."""
    input_path = RAW_FOLDER / "07_scheme_performance.csv"
    output_path = PROCESSED_FOLDER / "cleaned_scheme_performance.csv"

    performance = pd.read_csv(input_path)

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
        "expense_ratio_pct",
    ]

    for column in numeric_columns:
        performance[column] = pd.to_numeric(
            performance[column],
            errors="coerce",
        )

    performance = performance.drop_duplicates()

    performance.to_csv(output_path, index=False)

    return performance


def clean_remaining_datasets() -> None:
    """Clean the remaining raw datasets and save processed versions."""
    remaining_files = [
        "01_fund_master.csv",
        "03_aum_by_fund_house.csv",
        "04_monthly_sip_inflows.csv",
        "05_category_inflows.csv",
        "06_industry_folio_count.csv",
        "09_portfolio_holdings.csv",
        "10_benchmark_indices.csv",
    ]

    for file_name in remaining_files:
        input_path = RAW_FOLDER / file_name
        output_path = PROCESSED_FOLDER / f"cleaned_{file_name}"

        df = pd.read_csv(input_path)
        df = df.drop_duplicates()

        for column in df.columns:
            if "date" in column.lower() or column.lower() == "month":
                try:
                    df[column] = pd.to_datetime(df[column])
                except (ValueError, TypeError):
                    pass

        df.to_csv(output_path, index=False)


def main() -> None:
    """Run the complete data cleaning pipeline."""
    PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)

    clean_nav_history()
    clean_investor_transactions()
    clean_scheme_performance()
    clean_remaining_datasets()

    print("Data cleaning completed successfully.")


if __name__ == "__main__":
    main()