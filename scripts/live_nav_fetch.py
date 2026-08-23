"""Fetch latest NAV data for selected mutual fund schemes."""

from pathlib import Path

import pandas as pd
import requests


PROJECT_ROOT = Path(__file__).resolve().parent
RAW_FOLDER = PROJECT_ROOT / "data" / "raw"

SCHEMES = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841,
}

API_URL = "https://api.mfapi.in/mf/{amfi_code}"


def fetch_scheme_nav(
    scheme_name: str,
    amfi_code: int,
) -> Path:
    """Fetch NAV history for one scheme and save it as CSV.

    Args:
        scheme_name: File-friendly scheme name.
        amfi_code: AMFI scheme code.

    Returns:
        Path to the saved CSV file.

    Raises:
        RuntimeError: If the API request fails or returns invalid data.
    """
    url = API_URL.format(amfi_code=amfi_code)

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as exc:
        raise RuntimeError(
            f"Failed to fetch NAV for {scheme_name} ({amfi_code})."
        ) from exc

    if "data" not in data or not data["data"]:
        raise RuntimeError(
            f"No NAV data returned for {scheme_name} ({amfi_code})."
        )

    nav_data = pd.DataFrame(data["data"])

    output_path = RAW_FOLDER / f"{scheme_name}.csv"
    nav_data.to_csv(output_path, index=False)

    return output_path


def main() -> None:
    """Fetch NAV data for all configured schemes."""
    RAW_FOLDER.mkdir(parents=True, exist_ok=True)

    successful = 0

    for scheme_name, amfi_code in SCHEMES.items():
        fetch_scheme_nav(scheme_name, amfi_code)
        successful += 1

    print(
        f"Live NAV fetch completed successfully: "
        f"{successful}/{len(SCHEMES)} schemes downloaded."
    )


if __name__ == "__main__":
    main()