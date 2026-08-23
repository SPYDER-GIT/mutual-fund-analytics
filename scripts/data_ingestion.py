"""Load and validate raw CSV datasets for the Mutual Fund Analytics project."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_ROOT / "data" / "raw"


def ingest_csv_files(data_folder: Path = DATA_FOLDER) -> dict[str, pd.DataFrame]:
    """Load all CSV files from the raw data directory.

    Args:
        data_folder: Directory containing the raw CSV files.

    Returns:
        Dictionary mapping file names to loaded DataFrames.

    Raises:
        FileNotFoundError: If the raw data directory does not exist.
    """
    if not data_folder.exists():
        raise FileNotFoundError(f"Raw data directory not found: {data_folder}")

    csv_files = sorted(data_folder.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in: {data_folder}")

    datasets = {}

    for file_path in csv_files:
        try:
            datasets[file_path.name] = pd.read_csv(file_path)
        except Exception as exc:
            raise RuntimeError(
                f"Failed to read {file_path.name}: {exc}"
            ) from exc

    return datasets


def main() -> None:
    """Run the data ingestion process."""
    datasets = ingest_csv_files()

    total_rows = sum(len(df) for df in datasets.values())

    print(
        f"Data ingestion completed: "
        f"{len(datasets)} CSV files loaded, "
        f"{total_rows:,} total rows."
    )


if __name__ == "__main__":
    main()