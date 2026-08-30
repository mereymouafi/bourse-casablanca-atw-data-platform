from pathlib import Path

import pandas as pd


INPUT = Path("data/processed/atw/atw_market_history.csv")
OUTPUT = Path("data/processed/atw/atw_market_features.csv")


def safe_divide(numerator: pd.Series, denominator: pd.Series) -> pd.Series:
    """Divide two series while handling zero and missing values safely."""
    result = pd.Series(float("nan"), index=numerator.index, dtype="float64")
    valid = denominator.notna() & (denominator != 0)
    result[valid] = numerator[valid] / denominator[valid]
    return result


def main():
    print(f"Reading: {INPUT}")

    if not INPUT.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT}. "
            "Generate the historical ATW dataset first."
        )

    df = pd.read_csv(INPUT)

    if df.empty:
        raise ValueError("The historical ATW dataset is empty.")

    # Ensure dates are valid and ordered before any feature calculation.
    df["market_date"] = pd.to_datetime(df["market_date"], errors="coerce")
    df = df.dropna(subset=["market_date"]).sort_values("market_date").reset_index(drop=True)

    if df.empty:
        raise ValueError("No valid market_date values were found in the historical dataset.")

    # Previous-day values are needed for daily changes and rolling comparisons.
    previous_last_price = df["last_price"].shift(1)
    previous_volume = df["trading_volume"].shift(1)

    # Daily return: current close divided by previous close, minus 1.
    df["daily_return"] = safe_divide(df["last_price"], previous_last_price) - 1

    # Intraday range and percentage range using the high/low spread.
    df["intraday_range"] = df["high_price"] - df["low_price"]
    df["intraday_range_pct"] = safe_divide(
        df["high_price"] - df["low_price"],
        df["opening_price"],
    )

    # Price movement relative to the opening price.
    df["price_vs_open_pct"] = safe_divide(
        df["last_price"] - df["opening_price"],
        df["opening_price"],
    )

    # Volume change versus the previous day.
    df["volume_change_pct"] = safe_divide(df["trading_volume"], previous_volume) - 1

    # Rolling price averages for short and medium windows.
    df["moving_average_5"] = df["last_price"].rolling(window=5, min_periods=1).mean()
    df["moving_average_10"] = df["last_price"].rolling(window=10, min_periods=1).mean()

    # Volatility based on 5-day rolling standard deviation of daily returns.
    df["volatility_5"] = df["daily_return"].rolling(window=5, min_periods=2).std(ddof=1)

    # Keep the output columns readable and aligned to the requested business metrics.
    output_columns = [
        "market_date",
        "instrument",
        "last_price",
        "opening_price",
        "high_price",
        "low_price",
        "trading_volume",
        "change_pct",
        "daily_return",
        "intraday_range",
        "intraday_range_pct",
        "price_vs_open_pct",
        "volume_change_pct",
        "moving_average_5",
        "moving_average_10",
        "volatility_5",
    ]

    # Make sure the final dataset contains the required feature columns in order.
    df_output = df.copy()
    for column in output_columns:
        if column not in df_output.columns:
            df_output[column] = pd.NA

    df_output = df_output[output_columns]
    df_output["market_date"] = df_output["market_date"].dt.strftime("%Y-%m-%d")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df_output.to_csv(OUTPUT, index=False)

    print("\nCreated market features:")
    print(df_output.head().to_string(index=False))
    print(f"\nSaved to: {OUTPUT}")


if __name__ == "__main__":
    main()
