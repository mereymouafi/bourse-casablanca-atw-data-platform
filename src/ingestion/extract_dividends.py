from pathlib import Path


RAW_DIR = Path("data/raw/atw/dividends")


def main():
    print(f"Checking dividend data directory: {RAW_DIR}")

    if not RAW_DIR.exists():
        print("ERROR: Dividend data directory does not exist.")
        return

    files = [file for file in RAW_DIR.iterdir() if file.is_file()]

    if not files:
        print("No dividend files found.")
        return

    print(f"\nFound {len(files)} dividend file(s):\n")

    for file in sorted(files):
        print(f"- {file.name} [{file.suffix.lower()}]")

    print("\nSupported source formats:")
    print("- PDF")
    print("- CSV")
    print("- XLSX")
    print("- XLS")

    print(
        "\nNext step: extract dividend information from the "
        "actual source files. No values were invented."
    )


if __name__ == "__main__":
    main()
