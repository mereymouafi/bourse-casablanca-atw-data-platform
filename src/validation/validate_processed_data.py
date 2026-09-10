from pathlib import Path

import pandas as pd


DATASET_PATHS = [
    Path("data/processed/atw/atw_market.csv"),
    Path("data/processed/atw/atw_market_history.csv"),
    Path("data/processed/atw/atw_market_features.csv"),
    Path("data/processed/atw/atw_financials.csv"),
    Path("data/processed/atw/atw_dividends.csv"),
    Path("data/processed/atw/atw_fundamental_features.csv"),
    Path("data/processed/atw/atw_dividend_features.csv"),
]


def main():
    all_datasets_valid = True

    for dataset_path in DATASET_PATHS:
        print(f"\nDataset: {dataset_path}")

        if not dataset_path.exists():
            print("Status: missing")
            all_datasets_valid = False
            continue

        try:
            df = pd.read_csv(dataset_path)
        except Exception as error:
            print(f"Status: could not be read ({error})")
            all_datasets_valid = False
            continue

        print(f"Rows: {len(df)}")
        print(f"Columns: {len(df.columns)}")

        if df.empty:
            print("Status: empty")
            all_datasets_valid = False
        else:
            print("Status: available")

    if all_datasets_valid:
        print("\nALL DATASETS ARE AVAILABLE")
        return 0

    print("\nSOME DATASETS NEED ATTENTION")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())