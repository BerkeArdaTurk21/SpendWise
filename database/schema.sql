-- ============================================================
-- SpendWise — Database Schema
-- ------------------------------------------------------------
-- Defines the three core tables used by the application:
--   1. categories    : income / expense buckets
--   2. transactions  : individual money movements
--   3. budgets       : monthly spending limits per category
--
-- Foreign keys are enabled at the connection level (see src/db.py).
-- Running this script is idempotent: it drops existing tables
-- first so it can be re-run cleanly during development.
-- ============================================================

-- Drop in reverse dependency order to avoid FK conflicts.
DROP TABLE IF EXISTS budgets;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS categories;

-- ------------------------------------------------------------
-- categories
-- ------------------------------------------------------------
-- Each category is either an "income" source or an "expense"
-- bucket. The CHECK constraint guarantees only valid types.
-- Category names are unique so we never end up with duplicates
-- like "Food" and "food".
-- ------------------------------------------------------------
CREATE TABLE categories (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT    NOT NULL UNIQUE,
    type TEXT    NOT NULL CHECK (type IN ('income', 'expense'))
);

-- ------------------------------------------------------------
-- transactions
-- ------------------------------------------------------------
-- One row per money movement. `amount` is always stored as a
-- positive number; whether it adds or subtracts from the
-- balance is determined by the linked category's type.
-- `date` is stored as TEXT in ISO format (YYYY-MM-DD), which
-- sorts correctly and works with SQLite's date functions.
-- Deleting a category is blocked if transactions reference it
-- (ON DELETE RESTRICT) to protect historical data.
-- ------------------------------------------------------------
CREATE TABLE transactions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TEXT    NOT NULL,                       -- ISO format: YYYY-MM-DD
    amount      REAL    NOT NULL CHECK (amount > 0),
    description TEXT,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id)
        REFERENCES categories (id)
        ON DELETE RESTRICT
);

-- ------------------------------------------------------------
-- budgets
-- ------------------------------------------------------------
-- A monthly spending limit for a single category. `month` is
-- stored as "YYYY-MM" (e.g. "2026-05"). The UNIQUE constraint
-- on (category_id, month) ensures there is at most one budget
-- per category per month.
-- ------------------------------------------------------------
CREATE TABLE budgets (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id  INTEGER NOT NULL,
    month        TEXT    NOT NULL,                      -- format: YYYY-MM
    limit_amount REAL    NOT NULL CHECK (limit_amount >= 0),
    FOREIGN KEY (category_id)
        REFERENCES categories (id)
        ON DELETE CASCADE,
    UNIQUE (category_id, month)
);

-- ------------------------------------------------------------
-- Indexes
-- ------------------------------------------------------------
-- Speed up the most common lookups: transactions by date,
-- transactions by category, and budgets by month.
-- ------------------------------------------------------------
CREATE INDEX idx_transactions_date     ON transactions (date);
CREATE INDEX idx_transactions_category ON transactions (category_id);
CREATE INDEX idx_budgets_month         ON budgets (month);