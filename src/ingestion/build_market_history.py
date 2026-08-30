import re
from pathlib import Path

import pandas as pd


RAW_DIR = Path("data/raw/atw/market")
OUTPUT = Path("data/processed/atw/atw_market_history.csv")

COLUMNS = [
    "instrument",
    "issuer",
    "sector",
    "best_bid_quantity",
    "best_bid_price",
    "best_ask_quantity",
    "best_ask_price",
    "last_price",
    "opening_price",
    "change_pct",
    "trading_volume",
    "high_price",
    "low_price",
]


def main():
    print(f"Reading market files from: {RAW_DIR}")

    raw_files = sorted(RAW_DIR.glob("*.csv"))
    if not raw_files:
        raise FileNotFoundError(f"No CSV files found in: {RAW_DIR}")

    frames = []

    for file_path in raw_files:
        match = re.search(r"(\d{4}-\d{2}-\d{2})", file_path.name)
        if match is None:
            print(f"Skipping file without date in name: {file_path.name}")
            continue

        market_date = match.group(1)

        df = pd.read_csv(
            file_path,
            sep=";",
            decimal=",",
            skiprows=2,
            header=None,
            names=COLUMNS,
        )

        df = df[df["instrument"].str.strip() == "ATW"].copy()
        df["market_date"] = market_date

        for column in [
            "best_bid_quantity",
            "best_bid_price",
            "best_ask_quantity",
            "best_ask_price",
            "last_price",
            "opening_price",
            "change_pct",
            "trading_volume",
            "high_price",
            "low_price",
        ]:
            df[column] = pd.to_numeric(df[column], errors="coerce")

        frames.append(df)

    if not frames:
        raise ValueError("No valid ATW records were found in the market raw files.")

    history = pd.concat(frames, ignore_index=True)
    history = history[
        [
            "market_date",
            "instrument",
            "issuer",
            "sector",
            "best_bid_quantity",
            "best_bid_price",
            "best_ask_quantity",
            "best_ask_price",
            "last_price",
            "opening_price",
            "change_pct",
            "trading_volume",
            "high_price",
            "low_price",
        ]
    ].copy()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    history.to_csv(OUTPUT, index=False)

    print("\nHistorical ATW dataset:")
    print(history.head().to_string(index=False))
    print(f"\nSaved to: {OUTPUT}")


if __name__ == "__main__":
    main()
