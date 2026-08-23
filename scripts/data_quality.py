"""Validate core data quality and AMFI code consistency."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_FOLDER = PROJECT_ROOT / "data" / "raw"


def load_core_datasets() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load the fund master and NAV history datasets."""
    fund_master = pd.read_csv(RAW_FOLDER / "01_fund_master.csv")
    nav_history = pd.read_csv(RAW_FOLDER / "02_nav_history.csv")

    return fund_master, nav_history


def validate_amfi_codes(
    fund_master: pd.DataFrame,
    nav_history: pd.DataFrame,
) -> set:
    """Return AMFI codes present in fund master but missing from NAV history."""
    return set(fund_master["amfi_code"]) - set(nav_history["amfi_code"])


def generate_quality_summary(
    fund_master: pd.DataFrame,
    nav_history: pd.DataFrame,
    missing_codes: set,
) -> dict:
    """Generate a summary of the core dataset quality checks."""
    return {
        "fund_master_records": len(fund_master),
        "nav_history_records": len(nav_history),
        "unique_amfi_codes": fund_master["amfi_code"].nunique(),
        "missing_amfi_codes": len(missing_codes),
    }


def main() -> None:
    """Run the data quality validation."""
    fund_master, nav_history = load_core_datasets()

    missing_codes = validate_amfi_codes(
        fund_master,
        nav_history,
    )

    summary = generate_quality_summary(
        fund_master,
        nav_history,
        missing_codes,
    )

    if missing_codes:
        print(
            f"Data quality check completed with "
            f"{len(missing_codes)} missing AMFI codes."
        )
    else:
        print("Data quality check passed: all AMFI codes are present in NAV history.")

    print(
        f"Fund master records: {summary['fund_master_records']:,}"
    )
    print(
        f"NAV history records: {summary['nav_history_records']:,}"
    )
    print(
        f"Unique AMFI codes: {summary['unique_amfi_codes']:,}"
    )


if __name__ == "__main__":
    main()