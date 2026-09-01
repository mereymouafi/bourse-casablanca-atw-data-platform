from pathlib import Path
import pandas as pd

INPUT = Path("data/raw/atw/financials/atw_financials.csv")

def validate_financials():
    print(f"Reading: {INPUT}")

    if not INPUT.exists():
        print("ERROR: Financial file not found.")
        return

    df = pd.read_csv(INPUT)

    required = [
        "year",
        "share_capital",
        "equity",
        "number_of_shares",
        "revenue",
        "operating_result",
        "net_income",
    ]

    errors = []

    for column in required:
        if column not in df.columns:
            errors.append(f"Missing column: {column}")

    if errors:
        print("\nVALIDATION FAILED")
        for error in errors:
            print("-", error)
        return

    # Year validation
    if df["year"].duplicated().any():
        errors.append("Duplicate years found.")

    # Numeric validation
    numeric_columns = [
        "share_capital",
        "equity",
        "number_of_shares",
        "revenue",
        "operating_result",
        "net_income",
    ]

    for column in numeric_columns:
        if (df[column] < 0).any():
            errors.append(f"{column} contains negative values.")

    # Ratio validation
    for column in [
        "yield_pct",
        "roe_pct",
        "payout_pct",
    ]:
        if ((df[column] < 0) | (df[column] > 100)).any():
            errors.append(
                f"{column} contains invalid percentages."
            )

    if errors:
        print("\nVALIDATION FAILED")
        for error in errors:
            print("-", error)
    else:
        print("\nVALIDATION PASSED")
        print(f"Years: {df['year'].min()} - {df['year'].max()}")
        print(f"Rows: {len(df)}")

if __name__ == "__main__":
    validate_financials()
