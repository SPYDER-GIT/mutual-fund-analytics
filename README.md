# Mutual Fund Analytics

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite)
![Status](https://img.shields.io/badge/Status-Day%203%20Completed-success?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)

---

## 📌 Project Status

🚧 **In Progress (Day 3 Completed)**

This repository contains my **Capstone Project** developed during the **Bluestock Fintech Data Analytics Internship**.

---

# 📖 Project Objective

The objective of this project is to analyze Mutual Fund datasets using Python and SQL, perform ETL operations, clean and validate financial data, fetch live Mutual Fund NAV data using APIs, build a SQLite database, generate business insights, and create interactive dashboards for decision-making.

---

# 🔄 Project Workflow

```text
Raw CSV Data
      │
      ▼
Data Ingestion
      │
      ▼
Data Cleaning
      │
      ▼
SQLite Database
      │
      ▼
Exploratory Data Analysis
      │
      ▼
SQL Analysis
      │
      ▼
Dashboard Development
      │
      ▼
Final Business Report
```

---

# 🚀 Features

- ETL Pipeline using Python
- Mutual Fund Data Cleaning
- Live NAV Data Fetching using MF API
- Data Quality Validation
- SQLite Database Design
- SQL Analytical Queries
- Data Dictionary Documentation
- Business Insights Generation
- Interactive Dashboard (Upcoming)

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn, Plotly |
| Database | SQLite |
| ORM | SQLAlchemy |
| API | Requests |
| Notebook | Jupyter Notebook |
| Version Control | Git |
| Repository | GitHub |

---

# 📂 Project Structure

```text
Mutual-Fund-Analytics
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   └── EDA_Analysis.ipynb
│
├── reports
│   ├── nav_trend_2022_2026.png
│   ├── aum_growth_2022_2025.png
│   ├── sip_inflow_trend_2022_2025.png
│   ├── category_inflow_heatmap.png
│   ├── age_group_distribution.png
│   ├── sip_amount_boxplot.png
│   ├── gender_distribution.png
│   ├── sip_amount_by_state.png
│   ├── t30_b30_distribution.png
│   ├── folio_count_growth.png
│   ├── nav_return_correlation.png
│   └── sector_allocation_donut.png
│
├── sql
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard
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

# ✅ Day 1 – Project Setup & Data Ingestion

### Completed Tasks

- Created the project folder structure.
- Initialized the Git repository.
- Connected the project to GitHub.
- Installed all required Python libraries.
- Generated `requirements.txt`.
- Loaded all 10 CSV datasets using Pandas.
- Displayed dataset shape, columns, data types, and sample records.
- Performed missing value and duplicate checks.
- Explored the Fund Master dataset.
- Validated AMFI Scheme Codes.
- Retrieved Live NAV data using the MF API.
- Saved API responses into CSV files.
- Generated a Data Quality Summary.
- Committed and pushed Day 1 deliverables.

---

# ✅ Day 2 – Data Cleaning & SQLite Database Design

### Completed Tasks

### Data Cleaning

- Cleaned `nav_history.csv`.
- Parsed date columns into datetime format.
- Sorted records by AMFI Code and Date.
- Removed duplicate records.
- Forward-filled missing NAV values.
- Validated NAV values greater than zero.

### Investor Transactions

- Standardized Transaction Types.
- Standardized KYC Status values.
- Validated transaction amounts.
- Fixed date formats.
- Removed duplicate records.

### Scheme Performance

- Validated return columns.
- Checked numeric values.
- Verified Expense Ratio range.
- Removed duplicate records.

### Database Design

- Generated cleaned datasets in `data/processed`.
- Designed SQLite database schema.
- Loaded cleaned datasets into SQLite using SQLAlchemy.
- Verified database row counts.
- Created:
  - `schema.sql`
  - `queries.sql`
  - `data_dictionary.md`
- Committed and pushed Day 2 deliverables.

---

# 📊 Dataset

This project uses the following 10 mutual fund datasets:

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

# 📓 Exploratory Data Analysis Notebook

The complete EDA workflow is documented in:

- `notebooks/EDA_Analysis.ipynb`

The notebook includes:

- NAV Trend Analysis
- AUM Growth Analysis
- SIP Inflow Trend
- Category Inflow Heatmap
- Investor Demographics
- Geographic Distribution
- Folio Growth Analysis
- NAV Return Correlation
- Sector Allocation
- Business Insights

---

# ✅ Day 3 – Exploratory Data Analysis (EDA)

### Completed Tasks

- Loaded all cleaned datasets into a Jupyter Notebook.
- Performed exploratory data analysis on mutual fund datasets.
- Created an interactive NAV trend analysis (2022–2026) using Plotly.
- Analyzed Assets Under Management (AUM) growth by fund house.
- Visualized monthly SIP inflow trends and highlighted the all-time high.
- Generated a category-wise net inflow heatmap.
- Analyzed investor demographics by age group and gender.
- Created SIP amount distribution box plots by age group.
- Visualized state-wise SIP investments and T30 vs B30 city distribution.
- Analyzed mutual fund folio growth from 2022 to 2025.
- Computed the correlation matrix of daily NAV returns for selected schemes.
- Created a sector allocation donut chart from portfolio holdings.
- Documented key business insights from each visualization.
- Exported all charts as PNG files for reporting.
- Completed the EDA notebook (`EDA_Analysis.ipynb`).
- Committed and pushed Day 3 work to GitHub.

---
# 📈 Current Progress

| Milestone | Status |
|------------|--------|
| ✅ Day 1 – Project Setup & Data Ingestion | Completed |
| ✅ Day 2 – Data Cleaning & SQLite Database Design | Completed |
| ✅ Day 3 – Exploratory Data Analysis (EDA) | Completed |
| ⏳ Day 4 – Dashboard Development | Pending |
| ⏳ Day 5 – Advanced Analytics & Business Insights | Pending |
| ⏳ Day 6 – Final Report & Project Documentation | Pending |

---

# 🎯 Current Achievement

The project has successfully completed the data ingestion, data cleaning, SQLite database design, and Exploratory Data Analysis (EDA) phases.

---

# 🎯 Future Improvements

- Interactive Power BI Dashboard
- Advanced SQL Business Analysis
- KPI Monitoring Dashboard
- Executive Business Report
- Predictive Analytics (Future Scope)
- Interactive Visualizations
- Final Project Presentation

---

# 🔗 GitHub Repository

https://github.com/SPYDER-GIT/mutual-fund-analytics

---

# 🌟 Current Project Highlights

- 10 Mutual Fund datasets analyzed.
- SQLite database created and populated with cleaned data.
- 12+ professional data visualization charts generated.
- Interactive Plotly and Seaborn visualizations.
- Data cleaning, validation, and transformation completed.
- Business insights documented through Exploratory Data Analysis.
- Project tracked and version-controlled using Git and GitHub.

---

# 📊 Project Statistics

| Metric | Value |
|---------|------:|
| Datasets | 10 |
| Total Records Processed | 87,000+ |
| SQLite Tables | 10 |
| Visualizations | 12+ |
| Notebook | 1 |
| Programming Language | Python |
| Internship | Bluestock Fintech |

# 📄 License

This project was developed for educational and internship purposes as part of the Bluestock Fintech Data Analytics Internship. It is intended to demonstrate data analytics, visualization, and database management skills.

---

# 👨‍💻 Author

**Suraj Singh**

**Bluestock Fintech – Data Analytics Internship**

---

⭐ If you found this project interesting or helpful, consider giving it a star on GitHub. Your support is appreciated!
