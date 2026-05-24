from src.db import fetch_all, fetch_one, execute


def set_budget(category_id, month, limit_amount):
    """Insert or update a monthly budget for a category."""
    if limit_amount < 0:
        raise ValueError("Budget limit cannot be negative.")
    existing = fetch_one(
        "SELECT id FROM budgets WHERE category_id = ? AND month = ?",
        (category_id, month),
    )
    if existing:
        execute(
            "UPDATE budgets SET limit_amount = ? WHERE category_id = ? AND month = ?",
            (limit_amount, category_id, month),
        )
    else:
        execute(
            "INSERT INTO budgets (category_id, month, limit_amount) VALUES (?, ?, ?)",
            (category_id, month, limit_amount),
        )


def list_budgets(month):
    return fetch_all(
        """
        SELECT b.id, c.name AS category, b.month, b.limit_amount
        FROM budgets b
        JOIN categories c ON b.category_id = c.id
        WHERE b.month = ?
        ORDER BY c.name
        """,
        (month,),
    )


def get_budget_vs_actual(month):
    """Return each budgeted category with planned vs actual spending."""
    return fetch_all(
        """
        SELECT c.name AS category,
               b.limit_amount AS budget,
               COALESCE(SUM(t.amount), 0) AS actual,
               b.limit_amount - COALESCE(SUM(t.amount), 0) AS remaining
        FROM budgets b
        JOIN categories c ON b.category_id = c.id
        LEFT JOIN transactions t
            ON t.category_id = b.category_id
            AND strftime('%Y-%m', t.date) = b.month
        WHERE b.month = ?
        GROUP BY b.id
        ORDER BY remaining ASC
        """,
        (month,),
    )
