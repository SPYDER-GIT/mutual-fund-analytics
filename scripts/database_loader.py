"""Load cleaned mutual fund datasets into the SQLite database."""

from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine


PROJECT_ROOT = Path(__file__).resolve().parent
PROCESSED_FOLDER = PROJECT_ROOT / "data" / "processed"
DATABASE_PATH = PROJECT_ROOT / "bluestock_mf.db"


CSV_FILES = [
    "cleaned_01_fund_master.csv",
    "cleaned_nav_history.csv",
    "cleaned_03_aum_by_fund_house.csv",
    "cleaned_04_monthly_sip_inflows.csv",
    "cleaned_05_category_inflows.csv",
    "cleaned_06_industry_folio_count.csv",
    "cleaned_scheme_performance.csv",
    "cleaned_investor_transactions.csv",
    "cleaned_09_portfolio_holdings.csv",
    "cleaned_10_benchmark_indices.csv",
]


def load_datasets_to_database() -> int:
    """Load all processed CSV files into SQLite.

    Returns:
        Total number of rows loaded across all tables.

    Raises:
        FileNotFoundError: If a processed CSV file is missing.
    """
    engine = create_engine(f"sqlite:///{DATABASE_PATH}")

    total_rows = 0

    for file_name in CSV_FILES:
        file_path = PROCESSED_FOLDER / file_name

        if not file_path.exists():
            raise FileNotFoundError(
                f"Processed file not found: {file_path}"
            )

        df = pd.read_csv(file_path)

        table_name = file_name.replace(".csv", "").replace("cleaned_", "")

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False,
        )

        total_rows += len(df)

    return total_rows


def main() -> None:
    """Run the database loading process."""
    total_rows = load_datasets_to_database()

    print(
        f"Database loading completed successfully: "
        f"{len(CSV_FILES)} tables, {total_rows:,} rows loaded."
    )


if __name__ == "__main__":
    main()