from pathlib import Path

import pandas as pd


INPUT = Path("data/processed/atw/atw_dividends.csv")
OUTPUT = Path("data/processed/atw/atw_dividend_features.csv")


def main():
    if not INPUT.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT}")

    df = pd.read_csv(INPUT)
    df = df.sort_values("year").copy()
    previous_dividend = df["amount_mad"].shift(1)

    df["dividend_growth_pct"] = df["amount_mad"].pct_change() * 100
    df["dividend_change_mad"] = df["amount_mad"] - previous_dividend

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)

    print(f"Saved to: {OUTPUT}")


if __name__ == "__main__":
    main()