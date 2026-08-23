"""Recommend mutual funds based on investor risk appetite."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "07_scheme_performance.csv"


RISK_MAPPING = {
    "Low": ["Low"],
    "Moderate": ["Moderate"],
    "High": ["High", "Moderately High", "Very High"],
}


def load_scheme_performance() -> pd.DataFrame:
    """Load scheme performance data from the raw dataset."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Scheme performance file not found: {DATA_PATH}"
        )

    return pd.read_csv(DATA_PATH)


def recommend_funds(
    risk_appetite: str,
    scheme_performance: pd.DataFrame,
) -> pd.DataFrame:
    """Return the top three funds for the selected risk appetite.

    Args:
        risk_appetite: Low, Moderate, or High.
        scheme_performance: Scheme performance DataFrame.

    Returns:
        DataFrame containing the top three recommended funds.

    Raises:
        ValueError: If the risk appetite is invalid.
    """
    risk_appetite = risk_appetite.strip().title()

    if risk_appetite not in RISK_MAPPING:
        raise ValueError(
            "Invalid risk appetite. Choose Low, Moderate, or High."
        )

    matching_grades = RISK_MAPPING[risk_appetite]

    recommendations = scheme_performance[
        scheme_performance["risk_grade"].isin(matching_grades)
    ].copy()

    recommendations = (
        recommendations
        .sort_values("sharpe_ratio", ascending=False)
        .head(3)
    )

    return recommendations[
        [
            "amfi_code",
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
        ]
    ]


def main() -> None:
    """Run the interactive mutual fund recommender."""
    scheme_performance = load_scheme_performance()

    print("Mutual Fund Recommender")
    print("-----------------------")
    print("Risk options: Low / Moderate / High")

    risk = input("Enter your risk appetite: ")

    try:
        recommendations = recommend_funds(
            risk,
            scheme_performance,
        )
    except ValueError as exc:
        print(exc)
        return

    print("\nTop 3 Recommended Funds:")
    print(recommendations.to_string(index=False))


if __name__ == "__main__":
    main()