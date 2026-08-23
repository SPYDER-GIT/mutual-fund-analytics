import subprocess
import sys


def run_script(script_name):
    """Run a project Python script and stop if it fails."""
    print(f"\nRunning {script_name}...")
    
    result = subprocess.run(
        [sys.executable, script_name],
        check=False
    )

    if result.returncode != 0:
        print(f"{script_name} failed.")
        sys.exit(result.returncode)

    print(f"{script_name} completed successfully.")


def main():
    """Run the complete Mutual Fund Analytics pipeline."""
    
    scripts = [
        "data_ingestion.py",
        "data_cleaning.py",
        "data_quality.py",
        "database_loader.py",
        "live_nav_fetch.py"
    ]

    print("=" * 60)
    print("BLUESTOCK MUTUAL FUND ANALYTICS PIPELINE")
    print("=" * 60)

    for script in scripts:
        run_script(script)

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()