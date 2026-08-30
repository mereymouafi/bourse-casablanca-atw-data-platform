from pathlib import Path
import pandas as pd


INPUT = Path("data/processed/atw/atw_market.csv")


def validate_market_data():
    print(f"Reading: {INPUT}")

    df = pd.read_csv(INPUT)

    errors = []

    # 1. Dataset must not be empty
    if df.empty:
        errors.append("Dataset is empty.")

    # 2. Required columns
    required_columns = [
        "instrument",
        "issuer",
        "market_date",
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

    # 3. Instrument must be ATW
    if not (df["instrument"] == "ATW").all():
        errors.append("Instrument contains values other than ATW.")

    # 4. Date validation
    dates = pd.to_datetime(df["market_date"], errors="coerce")

    if dates.isna().any():
        errors.append("Invalid market_date found.")

    # 5. Prices must be positive
    for column in [
        "last_price",
        "opening_price",
        "high_price",
        "low_price",
    ]:
        if (df[column] <= 0).any():
            errors.append(f"{column} contains values <= 0.")

    # 6. High must be >= Low
    if (df["high_price"] < df["low_price"]).any():
        errors.append("High price is lower than low price.")

    # 7. Volume must not be negative
    if (df["trading_volume"] < 0).any():
        errors.append("Trading volume contains negative values.")

    # 8. Check missing values
    for column in required_columns:
        if df[column].isna().any():
            errors.append(f"{column} contains missing values.")

    # Result
    if errors:
        print("\nVALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
    else:
        print("\nVALIDATION PASSED")
        print(f"Rows: {len(df)}")
        print(f"Instrument: {df['instrument'].unique().tolist()}")
        print(f"Dates: {df['market_date'].min()} → {df['market_date'].max()}")


if __name__ == "__main__":
    validate_market_data()