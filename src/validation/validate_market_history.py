from pathlib import Path
import pandas as pd

INPUT = Path("data/processed/atw/atw_market_history.csv")

def validate_history():
    print(f"Reading: {INPUT}")

    if not INPUT.exists():
        print("ERROR: Historical dataset not found.")
        return

    df = pd.read_csv(INPUT)

    errors = []

    # Required columns
    required_columns = [
        "market_date",
        "instrument",
        "last_price",
        "opening_price",
        "high_price",
        "low_price",
        "trading_volume",
    ]

    for column in required_columns:
        if column not in df.columns:
            errors.append(f"Missing column: {column}")

    if errors:
        print("\nVALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return

    # Validate dates
    df["market_date"] = pd.to_datetime(
        df["market_date"],
        errors="coerce"
    )

    if df["market_date"].isna().any():
        errors.append("Invalid market_date found.")

    # Only ATW should exist
    if not (df["instrument"] == "ATW").all():
        errors.append("Dataset contains instruments other than ATW.")

    # Duplicate trading days
    duplicates = df.duplicated(
        subset=["market_date", "instrument"]
    )

    if duplicates.any():
        errors.append(
            f"Duplicate market dates found: {duplicates.sum()}"
        )

    # Check chronological order
    if not df["market_date"].is_monotonic_increasing:
        errors.append("Market dates are not sorted.")

    # Prices
    for column in [
        "last_price",
        "opening_price",
        "high_price",
        "low_price",
    ]:
        if (df[column] <= 0).any():
            errors.append(
                f"{column} contains values <= 0."
            )

    # High must be >= low
    if (df["high_price"] < df["low_price"]).any():
        errors.append("High price is lower than low price.")

    # Volume
    if (df["trading_volume"] < 0).any():
        errors.append(
            "Trading volume contains negative values."
        )

    # Missing values
    for column in required_columns:
        if df[column].isna().any():
            errors.append(
                f"{column} contains missing values."
            )

    # Result
    if errors:
        print("\nVALIDATION FAILED")

        for error in errors:
            print(f"- {error}")

    else:
        print("\nVALIDATION PASSED")
        print("------------------")
        print(f"Rows: {len(df)}")
        print(f"Instrument: {df['instrument'].unique().tolist()}")
        print(
            f"Date range: "
            f"{df['market_date'].min().date()} → "
            f"{df['market_date'].max().date()}"
        )

if __name__ == "__main__":
    validate_history()
