# ATW Project Progress

## Project

Bourse Casablanca ATW Data Engineering Platform

Use case:

ATW — Attijariwafa Bank

---

## Market Data

Status: COMPLETED

Implemented:

- Raw ATW market CSV ingestion
- CSV delimiter handling
- Decimal conversion
- ATW filtering
- Market-data cleaning
- Historical market dataset
- Market feature engineering
- Market validation
- Historical market validation

Main outputs:

- data/processed/atw/atw_market.csv
- data/processed/atw/atw_market_history.csv
- data/processed/atw/atw_market_features.csv

Main code:

- src/ingestion/load_market_data.py
- src/ingestion/build_market_history.py
- src/transformation/create_market_features.py
- src/validation/validate_market_data.py
- src/validation/validate_market_history.py

---

## Financial Data

Status: IN PROGRESS

Raw data location:

data/raw/atw/financials/

Current objective:

Discover and inspect real ATW financial source files before extracting values.

Target output:

data/processed/atw/atw_financials.csv

Important:

Financial values must come from real source documents.

No values should be invented.

---

## Dividend Data

Status: IN PROGRESS

Raw data location:

data/raw/atw/dividends/

Current objective:

Discover and inspect real ATW dividend source files.

Target output:

data/processed/atw/atw_dividends.csv

Expected fields:

- instrument
- dividend_year
- dividend_amount
- ex_dividend_date
- payment_date

No dividend values should be invented.

---

## Company Profile

Status: IN PROGRESS

Raw data location:

data/raw/atw/company_profile/

Current situation:

The ATW company-profile PDF may be scanned/image-based.

Next step:

Inspect the PDF and determine whether OCR is required.

No company information should be invented.

---

## Data Engineering Pipeline

Current architecture:

Raw Data
    ↓
Ingestion
    ↓
Cleaning
    ↓
Historical Dataset
    ↓
Validation
    ↓
Feature Engineering
    ↓
Financial Data
    ↓
Dividend Data
    ↓
Company Profile
    ↓
Integrated Dataset
    ↓
Analytics
    ↓
AI Decision Support

---

## Next Priorities

1. Inspect real financial source files.
2. Extract financial data.
3. Validate financial data.
4. Inspect dividend sources.
5. Extract dividend data.
6. Validate dividend data.
7. Inspect company-profile PDF.
8. Add OCR if required.
9. Build an integrated ATW dataset.
10. Start analytics only after the data foundation is reliable.
