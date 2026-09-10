from pathlib import Path

import pandas as pd


INPUT = Path("data/processed/atw/atw_financials.csv")
OUTPUT = Path("data/processed/atw/atw_fundamental_features.csv")


def main():
    if not INPUT.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT}")

    df = pd.read_csv(INPUT)
    df = df.sort_values("year").copy()

    df["revenue_growth_pct"] = df["revenue"].pct_change() * 100
    df["net_income_growth_pct"] = df["net_income"].pct_change() * 100
    df["operating_margin_pct"] = df["operating_result"] / df["revenue"] * 100
    df["net_margin_pct"] = df["net_income"] / df["revenue"] * 100
    df["earnings_per_share"] = df["net_income"] / df["number_of_shares"]

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)

    print(f"Saved to: {OUTPUT}")


if __name__ == "__main__":
    main()