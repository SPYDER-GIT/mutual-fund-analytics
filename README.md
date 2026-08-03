# Mutual Fund Analytics

## Project Status

🚧 **In Progress (Day 2 Completed)**

This repository contains my Capstone Project developed during the Bluestock Fintech Data Analytics Internship.

---

# Project Objective

The objective of this project is to analyze Mutual Fund datasets using Python and SQL, perform ETL operations, clean and validate data, fetch live Mutual Fund NAV data using APIs, build a SQLite database, generate business insights, and create interactive dashboards.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Requests
- SQLAlchemy
- SQLite
- Jupyter Notebook
- Git
- GitHub

---

# Project Structure

```
Mutual-Fund-Analytics
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
├── sql
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard
├── reports
│
├── data_ingestion.py
├── live_nav_fetch.py
├── data_quality.py
├── data_cleaning.py
├── database_loader.py
│
├── bluestock_mf.db
├── data_dictionary.md
├── requirements.txt
└── README.md
```

---

# Day 1 – Project Setup & Data Ingestion

### Completed Tasks

- Created the project folder structure.
- Initialized the Git repository.
- Connected the project to GitHub.
- Installed all required Python libraries.
- Generated `requirements.txt`.
- Loaded all 10 CSV datasets using Pandas.
- Displayed dataset shape, columns, and data types.
- Performed missing value and duplicate checks.
- Explored Fund Master dataset.
- Validated AMFI scheme codes.
- Retrieved live NAV data using the MF API.
- Saved fetched NAV data into CSV files.
- Created a data quality summary.
- Committed and pushed Day 1 work to GitHub.

---

# Day 2 – Data Cleaning & SQLite Database Design

### Completed Tasks

- Cleaned `nav_history.csv`.
- Parsed date columns into datetime format.
- Removed duplicate records.
- Forward-filled missing NAV values.
- Validated NAV values.

- Cleaned `investor_transactions.csv`.
- Standardized transaction types.
- Standardized KYC status values.
- Validated transaction amounts.
- Removed duplicate records.

- Cleaned `scheme_performance.csv`.
- Validated return columns.
- Checked expense ratio values.
- Removed duplicate records.

- Generated cleaned datasets in `data/processed`.

- Designed SQLite database schema.

- Loaded cleaned datasets into SQLite using SQLAlchemy.

- Created:
  - `schema.sql`
  - `queries.sql`
  - `data_dictionary.md`

- Verified database row counts.

- Committed and pushed Day 2 work to GitHub.

---

# Dataset

The project uses Mutual Fund datasets including:

- Fund Master
- NAV History
- AUM by Fund House
- Monthly SIP Inflows
- Category Inflows
- Industry Folio Count
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices

---

# Current Progress

| Milestone | Status |
|-----------|--------|
| ✅ Day 1 – Project Setup & Data Ingestion | Completed |
| ✅ Day 2 – Data Cleaning & SQLite Database Design | Completed |
| ⏳ Day 3 – Exploratory Data Analysis (EDA) | Pending |
| ⏳ Day 4 – Dashboard Development | Pending |
| ⏳ Day 5 – Advanced Analytics | Pending |
| ⏳ Day 6 – Final Report & Documentation | Pending |

---

# GitHub Repository

https://github.com/SPYDER-GIT/mutual-fund-analytics

---

# Author

**Suraj Singh**

Bluestock Fintech – Data Analytics Internship
