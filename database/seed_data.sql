-- ============================================================
-- SpendWise — Seed Data
-- ------------------------------------------------------------
-- Sample data for development and demos. Provides:
--   * A realistic set of income and expense categories
--   * ~4 months of transactions (Feb–May 2026)
--   * Monthly budgets for the main expense categories
--
-- Run this AFTER schema.sql. Amounts are illustrative.
-- ============================================================

-- ------------------------------------------------------------
-- Categories
-- ------------------------------------------------------------
INSERT INTO categories (name, type) VALUES
    ('Salary',         'income'),
    ('Freelance',      'income'),
    ('Investments',    'income'),
    ('Groceries',      'expense'),
    ('Rent',           'expense'),
    ('Utilities',      'expense'),
    ('Transport',      'expense'),
    ('Dining Out',     'expense'),
    ('Entertainment',  'expense'),
    ('Healthcare',     'expense'),
    ('Shopping',       'expense');

-- ------------------------------------------------------------
-- Transactions
-- ------------------------------------------------------------
-- category_id values map to the INSERT order above:
--   1 Salary  2 Freelance  3 Investments
--   4 Groceries  5 Rent  6 Utilities  7 Transport
--   8 Dining Out  9 Entertainment  10 Healthcare  11 Shopping
-- ------------------------------------------------------------

-- ---- February 2026 ----
INSERT INTO transactions (date, amount, description, category_id) VALUES
    ('2026-02-01', 4200.00, 'Monthly salary',            1),
    ('2026-02-05',  350.00, 'Logo design gig',           2),
    ('2026-02-01', 1300.00, 'February rent',             5),
    ('2026-02-03',   95.40, 'Weekly groceries',          4),
    ('2026-02-08',  120.00, 'Electricity + water',       6),
    ('2026-02-10',   88.20, 'Weekly groceries',          4),
    ('2026-02-12',   45.00, 'Bus + metro pass',          7),
    ('2026-02-14',   62.50, 'Dinner with friends',       8),
    ('2026-02-17',  102.30, 'Weekly groceries',          4),
    ('2026-02-20',   30.00, 'Movie night',               9),
    ('2026-02-24',   78.90, 'Weekly groceries',          4),
    ('2026-02-26',   55.00, 'Pharmacy',                  10);

-- ---- March 2026 ----
INSERT INTO transactions (date, amount, description, category_id) VALUES
    ('2026-03-01', 4200.00, 'Monthly salary',            1),
    ('2026-03-07',  500.00, 'Website build',             2),
    ('2026-03-15',  180.00, 'Dividend payout',           3),
    ('2026-03-01', 1300.00, 'March rent',                5),
    ('2026-03-04',  110.10, 'Weekly groceries',          4),
    ('2026-03-09',  130.00, 'Electricity + gas',         6),
    ('2026-03-11',   92.75, 'Weekly groceries',          4),
    ('2026-03-13',   48.00, 'Metro pass',                7),
    ('2026-03-16',   75.00, 'Concert tickets',           9),
    ('2026-03-18',   84.60, 'Weekly groceries',          4),
    ('2026-03-21',   95.20, 'Dinner out',                8),
    ('2026-03-25',  140.00, 'New running shoes',         11),
    ('2026-03-28',   88.40, 'Weekly groceries',          4);

-- ---- April 2026 ----
INSERT INTO transactions (date, amount, description, category_id) VALUES
    ('2026-04-01', 4200.00, 'Monthly salary',            1),
    ('2026-04-10',  420.00, 'Consulting hours',          2),
    ('2026-04-01', 1300.00, 'April rent',                5),
    ('2026-04-03',  101.50, 'Weekly groceries',          4),
    ('2026-04-06',  125.00, 'Utilities',                 6),
    ('2026-04-08',   52.00, 'Transport top-up',          7),
    ('2026-04-10',   96.80, 'Weekly groceries',          4),
    ('2026-04-13',  110.00, 'Birthday dinner',           8),
    ('2026-04-15',   60.00, 'Streaming + games',         9),
    ('2026-04-17',   89.30, 'Weekly groceries',          4),
    ('2026-04-20',  220.00, 'Dentist visit',             10),
    ('2026-04-23',   94.10, 'Weekly groceries',          4),
    ('2026-04-27',  175.00, 'Clothing',                  11);

-- ---- May 2026 (partial month) ----
INSERT INTO transactions (date, amount, description, category_id) VALUES
    ('2026-05-01', 4200.00, 'Monthly salary',            1),
    ('2026-05-09',  300.00, 'Freelance article',         2),
    ('2026-05-01', 1300.00, 'May rent',                  5),
    ('2026-05-04',  108.70, 'Weekly groceries',          4),
    ('2026-05-07',  118.00, 'Electricity + water',       6),
    ('2026-05-10',   50.00, 'Metro pass',                7),
    ('2026-05-12',   72.40, 'Weekly groceries',          4),
    ('2026-05-15',   85.00, 'Dinner out',                8),
    ('2026-05-18',   40.00, 'Cinema',                    9),
    ('2026-05-20',   99.90, 'Weekly groceries',          4);

-- ------------------------------------------------------------
-- Budgets
-- ------------------------------------------------------------
-- Monthly limits for the main expense categories. These are
-- intentionally set near actual spending so the budget-vs-actual
-- report shows a mix of under-budget and over-budget results.
-- ------------------------------------------------------------
INSERT INTO budgets (category_id, month, limit_amount) VALUES
    -- April 2026
    (4,  '2026-04', 380.00),   -- Groceries
    (5,  '2026-04', 1300.00),  -- Rent
    (6,  '2026-04', 120.00),   -- Utilities  (will be slightly over)
    (7,  '2026-04', 60.00),    -- Transport
    (8,  '2026-04', 100.00),   -- Dining Out (will be over)
    (9,  '2026-04', 80.00),    -- Entertainment
    (10, '2026-04', 150.00),   -- Healthcare (will be over)
    (11, '2026-04', 200.00),   -- Shopping
    -- May 2026
    (4,  '2026-05', 400.00),   -- Groceries
    (5,  '2026-05', 1300.00),  -- Rent
    (6,  '2026-05', 130.00),   -- Utilities
    (7,  '2026-05', 55.00),    -- Transport
    (8,  '2026-05', 120.00),   -- Dining Out
    (9,  '2026-05', 70.00);    -- Entertainment