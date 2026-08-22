import pandas as pd
from pathlib import Path


# Load scheme performance data
DATA_PATH = Path(__file__).parent / "data" / "raw" / "07_scheme_performance.csv"

scheme_perf = pd.read_csv(DATA_PATH)


def recommend_funds(risk_appetite):
    """
    Return the top 3 funds by Sharpe ratio
    for the selected risk appetite.
    """

    risk_appetite = risk_appetite.strip().title()

    risk_mapping = {
        "Low": ["Low"],
        "Moderate": ["Moderate"],
        "High": ["High", "Moderately High", "Very High"]
    }

    if risk_appetite not in risk_mapping:
        print("Invalid risk appetite.")
        print("Please choose: Low, Moderate, or High.")
        return

    matching_grades = risk_mapping[risk_appetite]

    recommendations = scheme_perf[
        scheme_perf["risk_grade"].isin(matching_grades)
    ].copy()

    recommendations = recommendations.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(3)

    recommendations = recommendations[
        [
            "amfi_code",
            "scheme_name",
            "risk_grade",
            "sharpe_ratio"
        ]
    ]

    return recommendations


# User input
print("Mutual Fund Recommender")
print("-----------------------")
print("Risk options: Low / Moderate / High")

risk = input("Enter your risk appetite: ")

result = recommend_funds(risk)

if result is not None:
    print("\nTop 3 Recommended Funds:")
    print(result.to_string(index=False))