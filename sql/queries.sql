-- 1. Top 5 funds by AUM
SELECT fund_house, aum_crore
FROM "03_aum_by_fund_house"
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV by AMFI Code
SELECT amfi_code,
AVG(nav) AS average_nav
FROM nav_history
GROUP BY amfi_code;

-- 3. Monthly SIP Inflow
SELECT month,
sip_inflow_crore
FROM "04_monthly_sip_inflows";

-- 4. Transactions by State
SELECT state,
COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio below 1%
SELECT scheme_name,
expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 6. Average Return (3 Years)
SELECT AVG(return_3yr_pct)
FROM scheme_performance;

-- 7. Count of Funds by Category
SELECT category,
COUNT(*)
FROM scheme_performance
GROUP BY category;

-- 8. Top 10 Highest NAV
SELECT *
FROM nav_history
ORDER BY nav DESC
LIMIT 10;

-- 9. Average Transaction Amount
SELECT AVG(amount_inr)
FROM investor_transactions;

-- 10. Count Verified KYC Investors
SELECT kyc_status,
COUNT(*)
FROM investor_transactions
GROUP BY kyc_status;