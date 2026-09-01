from pathlib import Path
import pandas as pd

INPUT = Path("data/raw/atw/dividends/atw_dividends.csv")

def validate_dividends():
    print(f"Reading: {INPUT}")

    if not INPUT.exists():
        print("ERROR: Dividend file not found.")
        return

    df = pd.read_csv(INPUT)

    required = [
        "year",
        "amount_mad",
        "type",
        "ex_date",
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

    # Amount must be positive
    if (df["amount_mad"] <= 0).any():
        errors.append("Dividend amount must be greater than zero.")

    # Convert dates
    df["ex_date"] = pd.to_datetime(
        df["ex_date"],
        errors="coerce"
    )

    if df["ex_date"].isna().any():
        errors.append("Invalid ex_date found.")

    # Duplicate years
    if df["year"].duplicated().any():
        errors.append("Duplicate dividend years found.")

    if errors:
        print("\nVALIDATION FAILED")
        for error in errors:
            print("-", error)
    else:
        print("\nVALIDATION PASSED")
        print(f"Rows: {len(df)}")
        print(
            f"Dividend range: "
            f"{df['year'].min()} - {df['year'].max()}"
        )

if __name__ == "__main__":
    validate_dividends()
