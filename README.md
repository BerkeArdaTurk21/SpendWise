# 💸 SpendWise — Personal Finance Tracker & Spending Analysis

A personal finance project built with Python and SQLite — track income and expenses through a command-line interface, set monthly budgets, and analyse spending patterns through an exploratory data analysis notebook.

---

## 📋 Table of Contents

- 🎯 Project Overview
- ✨ Features
- 🧱 Tech Stack
- 📁 Project Structure
- 🗄️ Database Schema
- 🚀 How to Run
- 📊 Visualizations
- 💡 Key Findings
- 👨‍💻 Author

---

## 🎯 Project Overview

SpendWise combines two approaches to personal finance:

1. **SQLite-backed CLI app** — add transactions, set budgets, and check spending in real time via a command-line menu.
2. **EDA notebook** — exploratory analysis of 806 real personal finance transactions (2018–2020) covering income, expenses, category breakdowns, monthly trends and budget performance.

---

## ✨ Features

- **Transactions** — add, list, and delete income/expense records
- **Budgets** — set a monthly spending limit for any category
- **Budget tracking** — compare planned vs. actual spending
- **Summary reports** — total income, total expense, and net balance for any period
- **Visual analysis** — charts covering spending by category, monthly trends, and budget vs. actual

---

## 🧱 Tech Stack

| Layer          | Tool                          |
| -------------- | ----------------------------- |
| Language       | Python 3.8+                   |
| Storage        | SQLite (`sqlite3`, built-in)  |
| Data wrangling | Pandas, NumPy                 |
| Visualization  | Matplotlib, Seaborn           |
| Interface      | Command-line menu (`main.py`) |
| Environment    | Jupyter Notebook              |

---

## 📁 Project Structure

```
SpendWise/
├── README.md
├── main.py                        # CLI menu — main entry point
├── requirements.txt
├── database/
│   ├── schema.sql                 # Table definitions
│   └── seed_data.sql              # Sample data for demos
├── src/
│   ├── db.py                      # Connection handling + schema init
│   ├── transactions.py            # Add / list / delete transactions
│   ├── budgets.py                 # Set budgets + budget-vs-actual
│   └── reports.py                 # Summaries and spending analysis
├── data/
│   ├── personal_transactions.csv  # Raw transactions (not tracked by git)
│   └── Budget.csv                 # Monthly budget by category (not tracked)
├── notebooks/
│   ├── sqlite_analysis.ipynb      # SQLite-powered visualizations
│   └── eda_analysis.ipynb         # EDA notebook (CSV-based)
└── outputs/
    ├── income_vs_expenses.png
    ├── monthly_spending.png
    ├── top_categories.png
    ├── spending_pie.png
    ├── budget_vs_actual.png
    └── spending_by_account.png
```

---

## 🗄️ Database Schema

Three tables linked by foreign keys:

**`categories`** — income sources and expense buckets.

| Column | Type    | Notes                        |
| ------ | ------- | ---------------------------- |
| id     | INTEGER | Primary key                  |
| name   | TEXT    | Unique (e.g. "Groceries")    |
| type   | TEXT    | Either `income` or `expense` |

**`transactions`** — one row per money movement.

| Column      | Type    | Notes                                          |
| ----------- | ------- | ---------------------------------------------- |
| id          | INTEGER | Primary key                                    |
| date        | TEXT    | ISO format `YYYY-MM-DD`                        |
| amount      | REAL    | Always positive; sign comes from category type |
| description | TEXT    | Optional free text                             |
| category_id | INTEGER | Foreign key → `categories.id`                  |

**`budgets`** — a monthly limit for one category.

| Column       | Type    | Notes                             |
| ------------ | ------- | --------------------------------- |
| id           | INTEGER | Primary key                       |
| category_id  | INTEGER | Foreign key → `categories.id`     |
| month        | TEXT    | Format `YYYY-MM` (e.g. `2026-05`) |
| limit_amount | REAL    | Planned spending cap              |

---

## 🚀 How to Run

### CLI App (SQLite)

**1. Install dependencies:**
```bash
pip install pandas matplotlib seaborn jupyter
```

**2. Initialize the database:**
```bash
# Create an empty database
python main.py

# Create and load sample data
python main.py --seed
```

**3. Use the menu:**
```
==============================
        💰  SpendWise
==============================
1. Add transaction
2. List transactions
3. Delete transaction
4. Set monthly budget
5. Check budget vs. actual
6. Summary report
7. List categories
0. Exit
```

---

## 🖥️ Example Output

**List transactions (May 2026):**
```
ID    Date             Amount Category         Description
------------------------------------------------------------
48    2026-05-20        99.90 Groceries        Weekly groceries
47    2026-05-18        40.00 Entertainment    Cinema
46    2026-05-15        85.00 Dining Out       Dinner out
45    2026-05-12        72.40 Groceries        Weekly groceries
44    2026-05-10        50.00 Transport        Metro pass
40    2026-05-09       300.00 Freelance        Freelance article
43    2026-05-07       118.00 Utilities        Electricity + water
42    2026-05-04       108.70 Groceries        Weekly groceries
41    2026-05-01      1300.00 Rent             May rent
39    2026-05-01      4200.00 Salary           Monthly salary
```

**Budget vs. actual (May 2026):**
```
Category             Budget     Actual  Remaining
--------------------------------------------------
Rent                1300.00    1300.00       0.00
Transport             55.00      50.00       5.00
Utilities            130.00     118.00      12.00
Entertainment         70.00      40.00      30.00
Dining Out           120.00      85.00      35.00
Groceries            400.00     281.00     119.00
```

**Summary report (all time):**
```
  Income:    18550.00
  Expense:    8439.05
  Balance:   10110.95
```

---

### EDA Notebook (CSV)

**1. Download the dataset:**

Get both CSV files from [Kaggle](https://www.kaggle.com/datasets/bukolafatunde/personal-finance) and place them inside the `data/` folder.

**2. Run the notebook:**
```bash
jupyter notebook notebooks/eda_analysis.ipynb
```

---

## 📊 Visualizations

### Income vs Expenses vs Savings
![Income vs Expenses](outputs/income_vs_expenses.png)

### Monthly Spending Trend
![Monthly Spending](outputs/monthly_spending.png)

### Top 12 Spending Categories
![Top Categories](outputs/top_categories.png)

### Spending Share by Category
![Spending Pie](outputs/spending_pie.png)

### Budget vs Actual Spending
![Budget vs Actual](outputs/budget_vs_actual.png)

### Spending by Account
![Spending by Account](outputs/spending_by_account.png)

---

## 💡 Key Findings

- The overall savings rate across the period is positive, driven by consistent income
- **Mortgage & Rent** and **Restaurants** are the highest spending categories
- Several categories consistently exceed their monthly budget
- The **Platinum Card** account accounts for the majority of discretionary spending
- Spending spikes are visible in certain months, likely tied to seasonal expenses

---

## 👨‍💻 Author

**Berke Arda Turk**  
Data Science & AI Enthusiast | Computer Science (B.ASc)  
[🌐 Portfolio](https://berkeardaturk.com) · [💼 LinkedIn](https://www.linkedin.com/in/berke-arda-turk/) · [🐙 GitHub](https://github.com/BerkeArdaTurk21)
