# Mutual Fund Analytics

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite)
![Status](https://img.shields.io/badge/Status-Day%202%20Completed-success?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)

---

## 📌 Project Status

🚧 **In Progress (Day 2 Completed)**

This repository contains my **Capstone Project** developed during the **Bluestock Fintech Data Analytics Internship**.

---

# 📖 Project Objective

The objective of this project is to analyze Mutual Fund datasets using Python and SQL, perform ETL operations, clean and validate financial data, fetch live Mutual Fund NAV data using APIs, build a SQLite database, generate business insights, and create interactive dashboards for decision-making.

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

- Cleaned `nav_history.csv`
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

This project uses 10 Mutual Fund datasets.

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

# 📈 Current Progress

| Milestone | Status |
|------------|--------|
| ✅ Day 1 – Project Setup & Data Ingestion | Completed |
| ✅ Day 2 – Data Cleaning & SQLite Database Design | Completed |
| ⏳ Day 3 – Exploratory Data Analysis (EDA) | Pending |
| ⏳ Day 4 – Dashboard Development | Pending |
| ⏳ Day 5 – Advanced Analytics & Business Insights | Pending |
| ⏳ Day 6 – Final Report & Project Documentation | Pending |

---

# 🎯 Future Improvements

- Power BI Dashboard
- Advanced SQL Analysis
- KPI Dashboard
- Business Reports
- Predictive Analytics
- Interactive Visualizations
- Final Project Presentation

---

# 🔗 GitHub Repository

**Repository:**  
https://github.com/SPYDER-GIT/mutual-fund-analytics

---

# 👨‍💻 Author

**Suraj Singh**

**Bluestock Fintech – Data Analytics Internship**

---

⭐ If you found this project helpful, feel free to star the repository.
