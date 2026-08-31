# ATW Data Quality

## Objective

Ensure that ATW market data is reliable, consistent, and suitable
for analytics and future decision-support applications.

## Validation Rules

### 1. Instrument

Only the ATW instrument is accepted.

Expected value:

`ATW`

### 2. Market Date

Every record must contain a valid `market_date`.

The date is extracted from the original market-data filename.

Example:

`actions_en_2026-08-27.csv`

becomes:

`2026-08-27`

### 3. Duplicate Records

There should be only one ATW record per market date.

### 4. Prices

The following prices must be greater than zero:

- last_price
- opening_price
- high_price
- low_price

### 5. High and Low

The high price must be greater than or equal to the low price.

### 6. Trading Volume

Trading volume must not be negative.

### 7. Missing Values

Required fields should not contain unexpected missing values.

### 8. Chronological Order

Historical records should be ordered by `market_date`.

## Data Flow

Raw Bourse data:

`data/raw/atw/market/`

↓

Ingestion

↓

Processed market data:

`data/processed/atw/`

↓

Validation

↓

Historical dataset ready for analytics.

## Important Principle

Raw source data must not be modified.

Cleaning and transformation should happen in the processing layer.
