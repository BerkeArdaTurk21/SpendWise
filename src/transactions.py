from datetime import datetime
from src.db import fetch_all, fetch_one, execute


def list_categories():
    return fetch_all("SELECT * FROM categories ORDER BY type, name")


def get_category(category_id):
    return fetch_one("SELECT * FROM categories WHERE id = ?", (category_id,))


def add_category(name, category_type):
    if category_type not in ("income", "expense"):
        raise ValueError("Type must be 'income' or 'expense'.")
    return execute(
        "INSERT INTO categories (name, type) VALUES (?, ?)", (name, category_type)
    )


def add_transaction(date, amount, category_id, description=""):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if not get_category(category_id):
        raise ValueError(f"Category ID {category_id} does not exist.")
    return execute(
        "INSERT INTO transactions (date, amount, description, category_id) VALUES (?, ?, ?, ?)",
        (date, amount, description, category_id),
    )


def list_transactions(limit=None, category_id=None, month=None):
    query = """
        SELECT t.id, t.date, t.amount, t.description,
               c.name AS category, c.type AS category_type
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        WHERE 1=1
    """
    params = []
    if category_id:
        query += " AND t.category_id = ?"
        params.append(category_id)
    if month:
        query += " AND strftime('%Y-%m', t.date) = ?"
        params.append(month)
    query += " ORDER BY t.date DESC"
    if limit:
        query += " LIMIT ?"
        params.append(limit)
    return fetch_all(query, params)


def delete_transaction(transaction_id):
    row = fetch_one("SELECT id FROM transactions WHERE id = ?", (transaction_id,))
    if not row:
        return False
    execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    return True
