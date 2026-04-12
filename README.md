# Data Analysis Portfolio
This repository contains exploratory data analysis projects built during my transition into a Data Analyst role.

## Project 1: Tips Dataset Analysis

**What I analyzed:** Restaurant transaction data (244 records) covering bill amounts, tips, party sizes, gender, day, and meal time.

**Tools used:** Python, Pandas, Matplotlib

**Key findings:**
- Saturday leads in both total revenue ($1,778) and revenue per person ($8.18), with Friday close behind at $8.13 — Sunday and Thursday trail at $7.86 and $7.42 respectively
- Dinner generates nearly 3× more total revenue than lunch ($3,660 vs $1,167), driven by volume rather than higher individual spending
- Smaller parties (2 people) spend more per person ($8.22) than larger ones (6 people at $5.81), suggesting that quality service for small groups pays off in consistent revenue

📄 [Full Report →](analysis/revenue_insights/REPORT.md)

---

## Project 2: Superstore Sales SQL Analysis

**What I analyzed:** 4 years of retail order data (9,994 records) covering sales, profit, product categories, regions, and customer segments from a US-based superstore.

**Tools used:** SQL (SQLite), CSV data from Kaggle

**Key findings:**
- Furniture is the second-highest revenue category ($742K) but has a 2.49% profit margin — nearly 7× lower than Technology (17.4%), meaning high sales volume is masking a near-unprofitable category
- The West region leads in total revenue ($725K), but the East region generates more per order ($238.33 vs $226.49) — volume and efficiency tell different stories depending on which metric you optimize for
- November and December account for the two highest revenue months, consistent with holiday demand — the business has a predictable seasonal window it could plan inventory and promotions around

📄 [Full Insights →](analysis/kaggle_store/Insights.md)