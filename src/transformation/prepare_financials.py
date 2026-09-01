from pathlib import Path
import pandas as pd

INPUT = Path(
    "data/raw/atw/financials/atw_financials.csv"
)

OUTPUT = Path(
    "data/processed/atw/atw_financials.csv"
)

def prepare_financials():
    df = pd.read_csv(INPUT)

    df["year"] = pd.to_numeric(
        df["year"],
        errors="coerce"
    )

    numeric_columns = [
        "share_capital",
        "equity",
        "number_of_shares",
        "revenue",
        "operating_result",
        "net_income",
        "pe_ratio",
        "pb_ratio",
        "yield_pct",
        "roe_pct",
        "payout_pct",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    df = df.sort_values("year")

    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        OUTPUT,
        index=False
    )

    print("Financial data processed.")
    print(f"Saved to: {OUTPUT}")

if __name__ == "__main__":
    prepare_financials()
