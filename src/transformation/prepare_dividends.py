from pathlib import Path


OUTPUT = Path("data/processed/atw/atw_dividends.csv")


COLUMNS = [
    "instrument",
    "dividend_year",
    "dividend_amount",
    "ex_dividend_date",
    "payment_date",
]


def main():
    print("ATW Dividend Data Preparation")
    print("=" * 35)

    print("\nExpected output:")
    print(OUTPUT)

    print("\nExpected columns:")

    for column in COLUMNS:
        print(f"- {column}")

    if OUTPUT.exists():
        print("\nExisting dividend dataset found.")
    else:
        print("\nNo processed dividend dataset exists yet.")

    print(
        "\nNo dividend values were created because the "
        "values must come from real source data."
    )


if __name__ == "__main__":
    main()
