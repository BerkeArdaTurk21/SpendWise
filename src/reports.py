from src.db import fetch_all, fetch_one


def summary_report(start_date=None, end_date=None):
    """Total income, total expense, and net balance for a date range."""
    where = "WHERE 1=1"
    params = []
    if start_date:
        where += " AND t.date >= ?"
        params.append(start_date)
    if end_date:
        where += " AND t.date <= ?"
        params.append(end_date)

    row = fetch_one(
        f"""
        SELECT
            COALESCE(SUM(CASE WHEN c.type = 'income'  THEN t.amount ELSE 0 END), 0) AS total_income,
            COALESCE(SUM(CASE WHEN c.type = 'expense' THEN t.amount ELSE 0 END), 0) AS total_expense
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        {where}
        """,
        params,
    )
    total_income = row["total_income"]
    total_expense = row["total_expense"]
    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense,
    }


def spending_by_category(month=None):
    """Total spending per expense category, optionally filtered by month."""
    where = "WHERE c.type = 'expense'"
    params = []
    if month:
        where += " AND strftime('%Y-%m', t.date) = ?"
        params.append(month)
    return fetch_all(
        f"""
        SELECT c.name AS category, SUM(t.amount) AS total
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        {where}
        GROUP BY c.id
        ORDER BY total DESC
        """,
        params,
    )


def monthly_trend():
    """Total income and expense grouped by month."""
    return fetch_all(
        """
        SELECT strftime('%Y-%m', t.date) AS month,
               COALESCE(SUM(CASE WHEN c.type = 'income'  THEN t.amount ELSE 0 END), 0) AS income,
               COALESCE(SUM(CASE WHEN c.type = 'expense' THEN t.amount ELSE 0 END), 0) AS expense
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        GROUP BY month
        ORDER BY month
        """
    )
