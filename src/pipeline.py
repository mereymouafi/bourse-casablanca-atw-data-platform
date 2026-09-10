from pathlib import Path
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parent.parent

SCRIPTS = [
    Path("src/ingestion/load_market_data.py"),
    Path("src/ingestion/build_market_history.py"),
    Path("src/transformation/create_market_features.py"),
    Path("src/transformation/prepare_financials.py"),
    Path("src/transformation/prepare_dividends.py"),
    Path("src/transformation/create_fundamental_features.py"),
    Path("src/transformation/create_dividend_features.py"),
    Path("src/validation/validate_market_data.py"),
    Path("src/validation/validate_market_history.py"),
    Path("src/validation/validate_financials.py"),
    Path("src/validation/validate_dividends.py"),
    Path("src/validation/validate_processed_data.py"),
]


def main():
    for script in SCRIPTS:
        print(f"\nRunning: {script}")
        subprocess.run(
            [sys.executable, str(script)],
            cwd=PROJECT_ROOT,
            check=True,
        )

    print("\nATW PIPELINE COMPLETED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())