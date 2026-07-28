import pandas as pd
import os

# Folder containing CSV files
DATA_FOLDER = "data/raw"

# Get all CSV files
csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

print("=" * 80)
print("MUTUAL FUND ANALYTICS - DATA INGESTION")
print("=" * 80)

for file in csv_files:
    file_path = os.path.join(DATA_FOLDER, file)

    print("\n" + "=" * 80)
    print(f"FILE : {file}")
    print("=" * 80)

    try:
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}")
        print(e)

print("\n")
print("=" * 80)
print("ALL FILES LOADED SUCCESSFULLY")
print("=" * 80)