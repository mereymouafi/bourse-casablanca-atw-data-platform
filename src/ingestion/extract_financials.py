from pathlib import Path


RAW_DIR = Path("data/raw/atw/financials")


def main():
    print(f"Checking financial data directory: {RAW_DIR}")

    if not RAW_DIR.exists():
        print("ERROR: Financial data directory does not exist.")
        return

    files = [file for file in RAW_DIR.iterdir() if file.is_file()]

    if not files:
        print("No financial files found.")
        return

    print(f"\nFound {len(files)} financial file(s):\n")

    for file in sorted(files):
        print(f"- {file.name} [{file.suffix.lower()}]")

    print("\nSupported source formats:")
    print("- PDF")
    print("- CSV")
    print("- XLSX")
    print("- XLS")

    print(
        "\nNext step: extract financial values from the actual "
        "source files. No values were invented."
    )


if __name__ == "__main__":
    main()
