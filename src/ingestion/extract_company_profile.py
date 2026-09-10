from pathlib import Path


RAW_DIR = Path("data/raw/atw/company_profile")


def main():
    print(f"Checking company profile directory: {RAW_DIR}")

    if not RAW_DIR.exists():
        print("ERROR: Company profile directory does not exist.")
        return

    files = [file for file in RAW_DIR.iterdir() if file.is_file()]

    if not files:
        print("No company profile files found.")
        return

    print(f"\nFound {len(files)} file(s):\n")

    for file in sorted(files):
        print(f"- {file.name} [{file.suffix.lower()}]")

    pdf_files = [
        file for file in files
        if file.suffix.lower() == ".pdf"
    ]

    if pdf_files:
        print("\nPDF files detected. OCR is intentionally not run.")

    print(
        "\nNo company information was extracted or invented."
    )


if __name__ == "__main__":
    main()
