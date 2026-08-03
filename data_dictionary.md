# Data Dictionary

## 1. Fund Master
Source: 01_fund_master.csv

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Unique AMFI Scheme Code |
| fund_house | Text | Mutual Fund Company |
| scheme_name | Text | Name of Scheme |
| category | Text | Equity/Debt |
| sub_category | Text | Large Cap, Mid Cap, etc. |
| plan | Text | Direct/Regular |
| risk_category | Text | Risk Classification |

---

## 2. NAV History

| Column | Description |
|---------|-------------|
| amfi_code | Scheme Code |
| date | NAV Date |
| nav | Net Asset Value |

---

## 3. Investor Transactions

| Column | Description |
|---------|-------------|
| investor_id | Investor Identifier |
| transaction_type | SIP/Lumpsum/Redemption |
| amount_inr | Transaction Amount |
| state | Investor State |
| payment_mode | Payment Method |
| kyc_status | KYC Verification Status |

---

## 4. Scheme Performance

Contains returns, Sharpe Ratio, Beta, Alpha, Expense Ratio and Risk Grade for every scheme.

---

Remaining datasets follow the same structure as provided in the source CSV files.