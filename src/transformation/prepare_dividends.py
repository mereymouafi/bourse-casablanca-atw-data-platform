from pathlib import Path

import pandas as pd


INPUT = Path("data/raw/atw/dividends/atw_dividends.csv")
OUTPUT = Path("data/processed/atw/atw_dividends.csv")


def main():
    if not INPUT.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT}")

    df = pd.read_csv(INPUT)
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["amount_mad"] = pd.to_numeric(df["amount_mad"], errors="coerce")
    df["ex_date"] = pd.to_datetime(df["ex_date"], errors="coerce")
    df = df.sort_values("year")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)

    print(f"Rows: {len(df)}")
    print(f"Saved to: {OUTPUT}")


if __name__ == "__main__":
    main()
