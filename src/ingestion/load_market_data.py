import pandas as pd
from pathlib import Path


INPUT = Path(
    "data/raw/atw/market/actions_en_2026-08-27.csv"
)

OUTPUT = Path(
    "data/processed/atw/atw_market.csv"
)


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

    print(f"Reading: {INPUT}")

    # The Bourse file has a split header,
    # so we skip the two header lines and define
    # the correct 13 columns ourselves.
    df = pd.read_csv(
        INPUT,
        sep=";",
        decimal=",",
        skiprows=2,
        header=None,
        names=COLUMNS
    )

    # Keep ATW only
    df = df[
        df["instrument"].str.strip() == "ATW"
    ].copy()

    # Remove spaces from text fields
    df["issuer"] = df["issuer"].str.strip()
    df["sector"] = df["sector"].str.strip()

    # Convert numeric columns
    numeric_columns = [
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

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    print("\nClean ATW data:")
    print(df.to_string(index=False))

    # Create output directory
    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save
    df.to_csv(
        OUTPUT,
        index=False
    )

    print(f"\nSaved to: {OUTPUT}")


if __name__ == "__main__":
    main()