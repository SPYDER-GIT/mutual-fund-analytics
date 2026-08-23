# Mutual Fund Analytics

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge\&logo=sqlite)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge\&logo=powerbi)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge\&logo=github)
![Status](https://img.shields.io/badge/Status-Final%20Capstone-success?style=for-the-badge)

---

## Project Overview

**Mutual Fund Analytics** is an end-to-end data analytics capstone project developed during the **Bluestock Fintech Data Analytics Internship**.

The project analyzes mutual fund market data, scheme performance, investor transactions, SIP activity, AUM, portfolio holdings, and benchmark data using **Python, Pandas, NumPy, SQL, SQLite, Jupyter Notebook, and Power BI**.

The project follows a complete analytics workflow:

```text
Raw Data
   ↓
Data Ingestion
   ↓
Data Cleaning & Validation
   ↓
SQLite Database
   ↓
EDA & Business Analysis
   ↓
Fund Performance Analytics
   ↓
Advanced Risk & Investor Analytics
   ↓
Mutual Fund Recommendation
   ↓
Power BI Dashboard
   ↓
Reports & Presentation
```

---

## Project Objectives

The primary objective is to build a practical mutual fund analytics solution capable of:

* Ingesting and organizing multiple mutual fund datasets.
* Cleaning and validating financial and investor data.
* Storing processed data in a structured SQLite database.
* Performing exploratory data analysis.
* Analyzing fund performance and risk.
* Comparing funds using risk-adjusted performance metrics.
* Analyzing SIP activity and investor behavior.
* Evaluating portfolio concentration.
* Calculating VaR and CVaR risk metrics.
* Analyzing rolling Sharpe ratios.
* Identifying SIP continuity and at-risk investors.
* Building a risk-based mutual fund recommendation system.
* Creating an interactive Power BI dashboard.
* Generating actionable business insights.
* Presenting the final analysis through reports and a presentation.

---

# Data Sources

The project uses the following 10 core datasets:

| Dataset                        | Description                                      |
| ------------------------------ | ------------------------------------------------ |
| `01_fund_master.csv`           | Mutual fund scheme master information            |
| `02_nav_history.csv`           | Historical NAV observations                      |
| `03_aum_by_fund_house.csv`     | Assets Under Management by fund house            |
| `04_monthly_sip_inflows.csv`   | Monthly SIP inflows and SIP account metrics      |
| `05_category_inflows.csv`      | Category-wise mutual fund inflows                |
| `06_industry_folio_count.csv`  | Industry/category folio count information        |
| `07_scheme_performance.csv`    | Fund returns, risk, and performance metrics      |
| `08_investor_transactions.csv` | Investor transaction and demographic information |
| `09_portfolio_holdings.csv`    | Scheme portfolio holdings and sector allocation  |
| `10_benchmark_indices.csv`     | Benchmark index historical data                  |

### Additional API Data

Live NAV data was fetched using the **MF API** for five selected schemes:

* SBI Bluechip
* ICICI Bluechip
* Nippon Large Cap
* Axis Bluechip
* Kotak Bluechip

The downloaded API data is stored in:

```text
data/raw/
```

---

# Tech Stack

| Category        | Technology                  |
| --------------- | --------------------------- |
| Programming     | Python                      |
| Data Analysis   | Pandas, NumPy               |
| Visualization   | Matplotlib, Seaborn, Plotly |
| Database        | SQLite                      |
| Database Access | SQLAlchemy                  |
| API             | Requests                    |
| Notebook        | Jupyter Notebook            |
| Dashboard       | Microsoft Power BI          |
| Version Control | Git                         |
| Repository      | GitHub                      |

---

# Project Structure

```text
Mutual-Fund-Analytics/
│
├── data/
│   ├── raw/
│   │   ├── 01_fund_master.csv
│   │   ├── 02_nav_history.csv
│   │   ├── 03_aum_by_fund_house.csv
│   │   ├── 04_monthly_sip_inflows.csv
│   │   ├── 05_category_inflows.csv
│   │   ├── 06_industry_folio_count.csv
│   │   ├── 07_scheme_performance.csv
│   │   ├── 08_investor_transactions.csv
│   │   ├── 09_portfolio_holdings.csv
│   │   ├── 10_benchmark_indices.csv
│   │   ├── SBI_Bluechip.csv
│   │   ├── ICICI_Bluechip.csv
│   │   ├── Nippon_Large_Cap.csv
│   │   ├── Axis_Bluechip.csv
│   │   └── Kotak_Bluechip.csv
│   │
│   └── processed/
│       └── cleaned datasets
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   └── Performance_Analytics.ipynb
│
├── reports/
│   ├── equity_fund_hhi.csv
│   └── other analytical outputs
│
├── dashboard/
│   └── dashboard-related files
│
├── data_ingestion.py
├── data_cleaning.py
├── data_quality.py
├── database_loader.py
├── live_nav_fetch.py
├── recommender.py
├── run_pipeline.py
│
├── Advanced_Analytics.ipynb
├── bluestock_mf.db
├── bluestock_mf_dashboard.pbix
│
├── Dashboard.pdf
├── Page1_Industry_Overview.png
├── Page2_Fund_Performance.png
├── Page3_Investor_Analytics.png
├── Page4_SIP_Market_Trends.png
│
├── rolling_sharpe_chart.png
├── var_cvar_report.csv
├── sip_continuity_analysis.csv
│
├── schema.sql
├── queries.sql
├── data_dictionary.md
├── requirements.txt
└── README.md
```

---

# ETL Pipeline

The project includes a master pipeline:

```text
run_pipeline.py
```

The pipeline executes the following stages:

```text
data_ingestion.py
        ↓
data_cleaning.py
        ↓
data_quality.py
        ↓
database_loader.py
        ↓
live_nav_fetch.py
```

The complete pipeline was tested successfully and produced:

```text
PIPELINE COMPLETED SUCCESSFULLY
```

### Pipeline Responsibilities

**Data Ingestion**

* Loads the raw CSV datasets.
* Validates file availability and structure.
* Displays dataset shape, data types, and sample records.

**Data Cleaning**

* Standardizes dates and categorical fields.
* Handles duplicates and missing values.
* Validates numerical values.
* Generates cleaned datasets.

**Data Quality**

* Validates relationships between datasets.
* Checks AMFI code consistency.
* Performs structural and data integrity checks.

**Database Loading**

* Loads cleaned datasets into SQLite.
* Creates the analytical database tables.

**Live NAV Fetching**

* Retrieves current NAV information for selected schemes through the MF API.

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/SPYDER-GIT/mutual-fund-analytics.git
cd mutual-fund-analytics
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run the Complete Pipeline

```bash
py run_pipeline.py
```

The master pipeline performs:

```text
Data Ingestion
      ↓
Data Cleaning
      ↓
Data Quality Validation
      ↓
SQLite Database Loading
      ↓
Live NAV Fetching
```

---

# Data Cleaning

The data cleaning process was applied across all datasets.

## NAV History

Processing includes:

* Date conversion.
* Sorting by AMFI code and date.
* Duplicate removal.
* Missing NAV handling.
* Positive NAV validation.

## Investor Transactions

Processing includes:

* Transaction date standardization.
* Transaction type standardization.
* Transaction type validation.
* Transaction amount validation.
* KYC status standardization.
* Duplicate removal.

## Scheme Performance

Processing includes:

* Numeric type conversion.
* Missing-value validation.
* Expense-ratio validation.
* Duplicate removal.

## Other Datasets

The remaining datasets were processed using:

* Duplicate removal.
* Date/month conversion.
* Data type standardization.
* Missing-value validation.
* Processed output generation.

Cleaned datasets are stored in:

```text
data/processed/
```

---

# Data Quality Validation

The project validates the relationship between fund master records and NAV history.

Final validation results:

```text
Fund master records: 40
NAV history records: 46,000
Unique AMFI codes: 40
```

The final quality check confirmed:

```text
Data quality check passed:
all AMFI codes are present in NAV history.
```

---

# SQLite Database

The project uses **SQLite** to store and query the cleaned datasets.

Database:

```text
bluestock_mf.db
```

The database contains **10 analytical tables**.

The database loader uses **SQLAlchemy** to load processed datasets into SQLite.

Final database load:

```text
10 tables
87,533 rows
```

Database-related files:

```text
schema.sql
queries.sql
data_dictionary.md
bluestock_mf.db
```

---

# Exploratory Data Analysis

The EDA phase analyzes multiple dimensions of the mutual fund ecosystem.

### Analysis Areas

* NAV trends.
* AUM growth.
* SIP inflow trends.
* Category-wise inflows.
* Investor demographics.
* Geographic distribution.
* Folio growth.
* Sector allocation.
* Daily NAV returns.
* Fund performance.
* Benchmark relationships.

EDA notebooks:

```text
notebooks/EDA_Analysis.ipynb
notebooks/Performance_Analytics.ipynb
```

---

# Fund Performance Analytics

Mutual fund performance is evaluated using both absolute-return and risk-adjusted metrics.

### Metrics Analyzed

* Daily NAV returns.
* 1-year returns.
* 3-year returns.
* 5-year returns.
* CAGR.
* Sharpe Ratio.
* Sortino Ratio.
* Alpha.
* Beta.
* Standard deviation.
* Maximum Drawdown.
* Benchmark comparison.
* Tracking Error.
* Fund Scorecard.

These metrics allow funds to be compared based on both **return and risk-adjusted performance**.

---

# Advanced Analytics

Advanced analysis is implemented in:

```text
Advanced_Analytics.ipynb
```

## 1. Value at Risk — VaR

Value at Risk estimates the potential portfolio loss at a selected confidence level.

Output:

```text
var_cvar_report.csv
```

## 2. Conditional Value at Risk — CVaR

CVaR estimates the expected loss beyond the VaR threshold and provides an additional measure of downside risk.

## 3. Rolling Sharpe Ratio

Rolling Sharpe analysis evaluates how risk-adjusted performance changes over time.

Output:

```text
rolling_sharpe_chart.png
```

## 4. SIP Continuity Analysis

SIP behavior was analyzed using:

* SIP transaction count.
* Average gap between SIP transactions.
* Investor continuity.
* At-risk investor identification.

Output:

```text
sip_continuity_analysis.csv
```

## 5. Portfolio Concentration

The **Herfindahl-Hirschman Index (HHI)** was calculated to evaluate equity fund portfolio concentration.

Output:

```text
reports/equity_fund_hhi.csv
```

---

# Investor Analytics

The investor transaction dataset contains:

```text
32,778 transactions
```

The SIP analysis identified:

```text
19,716 SIP transactions
4,762 unique SIP investors
1,362 investors with 6+ SIP transactions
```

The SIP continuity analysis classified eligible investors according to transaction frequency and average transaction gaps.

Final analysis results:

```text
SIP continuity rate: 2.20%
At-risk rate: 97.80%
```

These results highlight a potential opportunity for investor-retention and SIP-engagement strategies.

---

# Mutual Fund Recommendation System

The project includes a risk-based recommendation system implemented in:

```text
recommender.py
```

Run the recommendation system using:

```bash
py recommender.py
```

The system accepts three risk categories:

```text
Low
Moderate
High
```

It then recommends the **top three funds based on Sharpe Ratio** within the selected risk category.

Example:

```text
Risk appetite: Low

Top 3 Recommended Funds:

ICICI Pru Liquid Fund
Kotak Liquid Fund
ABSL Liquid Fund
```

The recommendation system was tested successfully for:

* Low risk.
* Moderate risk.
* High risk.

---

# Power BI Dashboard

The project includes an interactive Power BI dashboard:

```text
bluestock_mf_dashboard.pbix
```

The dashboard contains four major pages.

## Page 1 — Industry Overview

Focuses on:

* Industry-level overview.
* Fund and folio information.
* Category distribution.
* Market-level KPIs.

Screenshot:

```text
Page1_Industry_Overview.png
```

## Page 2 — Fund Performance

Focuses on:

* Fund returns.
* Performance comparison.
* Risk metrics.
* Fund-level analysis.

Screenshot:

```text
Page2_Fund_Performance.png
```

## Page 3 — Investor Analytics

Focuses on:

* Investor demographics.
* SIP behavior.
* Investor segmentation.
* Transaction analysis.

Screenshot:

```text
Page3_Investor_Analytics.png
```

## Page 4 — SIP & Market Trends

Focuses on:

* SIP inflows.
* SIP account trends.
* Market/category trends.
* Long-term market movement.

Screenshot:

```text
Page4_SIP_Market_Trends.png
```

A PDF export of the dashboard is also included:

```text
Dashboard.pdf
```

---

# Key Business Insights

The analysis generated insights across fund performance, investor behavior, SIP activity, portfolio concentration, and market trends.

### Major Findings

* Risk-adjusted fund performance varies significantly across schemes.
* Low-risk funds can achieve strong Sharpe Ratios, particularly within liquid-fund categories.
* SIP investors demonstrate different levels of continuity and transaction gaps.
* A significant proportion of eligible long-term SIP investors were classified as at-risk under the defined continuity methodology.
* Portfolio concentration varies substantially across equity funds.
* SIP inflows and active SIP accounts highlight the importance of systematic investing behavior.
* Fund selection should consider risk-adjusted metrics rather than returns alone.

---

# Final Deliverables

| Deliverable                | Status           |
| -------------------------- | ---------------- |
| Final Report PDF           | Completed        |
| 12-Slide Presentation      | Completed        |
| Clean GitHub Repository    | Completed        |
| README.md                  | Completed        |
| ETL Pipeline               | Completed        |
| SQLite Database            | Completed        |
| EDA Analysis               | Completed        |
| Performance Analytics      | Completed        |
| Advanced Analytics         | Completed        |
| Risk-Based Recommender     | Completed        |
| Power BI Dashboard         | Completed        |
| Dashboard PDF Export       | Completed        |
| Dashboard Page Screenshots | Completed        |
| GitHub Version Tag         | Final Submission |

---

# Project Validation

The master pipeline was tested using:

```bash
py run_pipeline.py
```

All pipeline stages completed successfully:

```text
data_ingestion.py completed successfully.
data_cleaning.py completed successfully.
data_quality.py completed successfully.
database_loader.py completed successfully.
live_nav_fetch.py completed successfully.

PIPELINE COMPLETED SUCCESSFULLY
```

The recommendation system was also tested successfully for:

```text
Low
Moderate
High
```

risk categories.

---

# Limitations

The project has several limitations:

* The analysis is based on the datasets provided for the internship project.
* Historical performance does not guarantee future returns.
* The recommendation system primarily uses risk grade and Sharpe Ratio.
* Investor continuity classifications depend on the selected SIP-gap methodology.
* Portfolio concentration analysis depends on the available holdings data.
* Live NAV analysis depends on API availability.
* Power BI dashboard results depend on the underlying dataset and refresh status.
* The project is intended for analytical and educational purposes and should not be considered financial advice.

---

# Recommendations

## For Fund Managers

* Monitor investor SIP continuity.
* Identify potentially at-risk SIP investors early.
* Analyze portfolio concentration regularly.
* Monitor risk-adjusted performance alongside absolute returns.

## For Investors

* Consider risk appetite before selecting funds.
* Evaluate Sharpe and Sortino Ratios alongside returns.
* Review maximum drawdown and volatility.
* Maintain SIP discipline for long-term investing.

## For Analytics Teams

* Automate regular NAV and benchmark data updates.
* Monitor rolling risk metrics.
* Integrate dashboard refresh automation.
* Extend the recommendation system using additional investor and fund characteristics.

---

# Final Project Status

The Mutual Fund Analytics capstone has completed the major development stages:

```text
✓ Project Setup
✓ Data Ingestion
✓ Data Cleaning
✓ Data Quality Validation
✓ SQLite Database
✓ Exploratory Data Analysis
✓ Fund Performance Analytics
✓ Advanced Analytics
✓ Risk Analysis
✓ Investor Analytics
✓ SIP Continuity Analysis
✓ Portfolio Concentration Analysis
✓ Mutual Fund Recommendation System
✓ Power BI Dashboard
✓ Final Documentation
✓ Final Presentation
✓ Master ETL Pipeline
✓ GitHub Repository
```

## Project Status: Final Capstone Completed

---

# GitHub Repository

**Repository:**
https://github.com/SPYDER-GIT/mutual-fund-analytics

---

# Author

**Suraj Singh**

**Bluestock Fintech — Data Analytics Internship**

---

# Disclaimer

This project was developed for educational and internship purposes as part of the **Bluestock Fintech Data Analytics Internship**.

The analysis and recommendation outputs demonstrate data analytics techniques and should not be considered personalized investment or financial advice.
