# bourse-casablanca-atw-data-platform
# Bourse Casablanca — ATW Data Platform

Data engineering project focused on **Attijariwafa Bank (ATW)**, listed on the **Bourse de Casablanca**.

The objective is to build a reliable data foundation combining market data and company information, with the long-term goal of providing analytics and AI-powered decision-support tools.

> **Current phase:** Data ingestion, transformation, validation, and source management.
>
> AI and prediction are intentionally not implemented yet.

---

## 🎯 Project Objective

The project aims to transform raw Bourse de Casablanca and company-source data into structured, validated datasets that can later support:

- Market analysis
- Historical price analysis
- Trading-volume analysis
- Financial analysis
- Dividend analysis
- Company analysis
- Data-driven decision support
- Future AI/ML applications

The first use case is **Attijariwafa Bank (ATW)**.

---

## 🏦 Current Use Case

### Attijariwafa Bank

| Field | Value |
|---|---|
| Instrument | ATW |
| Company | Attijariwafa Bank |
| Sector | Banks |
| Market | Bourse de Casablanca |

---

## 🏗️ Architecture

The project is being developed progressively as a data pipeline:

```text
Bourse / Company Sources
          │
          ▼
       RAW DATA
          │
          ▼
      INGESTION
          │
          ▼
       BRONZE
          │
          ▼
 CLEAN + VALIDATE
          │
          ▼
       SILVER
          │
          ▼
  BUSINESS METRICS
          │
          ▼
        GOLD
          │
          ▼
   Analytics / AI
```

---

## 🔄 Current Pipeline

```text
Raw Bourse CSV
      ↓
load_market_data.py
      ↓
Clean daily ATW data
      ↓
build_market_history.py
      ↓
ATW historical dataset
      ↓
validate_market_data.py
      ↓
Validated data
      ↓
create_market_features.py
      ↓
ATW market features
      ↓
Future analytics / dashboard / AI
```

The current active transformation stage creates a feature-rich historical market dataset to support technical analysis and later dashboards or AI-based decision support.
