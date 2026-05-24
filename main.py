import sys
from src.db import initialize_database
from src.transactions import (
    list_categories,
    add_transaction,
    list_transactions,
    delete_transaction,
    add_category,
)
from src.budgets import set_budget, list_budgets, get_budget_vs_actual
from src.reports import summary_report, spending_by_category, monthly_trend


def print_menu():
    print("\n" + "=" * 30)
    print("        💰  SpendWise")
    print("=" * 30)
    print("1. Add transaction")
    print("2. List transactions")
    print("3. Delete transaction")
    print("4. Set monthly budget")
    print("5. Check budget vs. actual")
    print("6. Summary report")
    print("7. List categories")
    print("0. Exit")
    print("=" * 30)


def handle_add_transaction():
    categories = list_categories()
    print("\nCategories:")
    for c in categories:
        print(f"  [{c['id']}] {c['name']} ({c['type']})")
    try:
        cat_id = int(input("Category ID: "))
        date = input("Date (YYYY-MM-DD): ").strip()
        amount = float(input("Amount: "))
        desc = input("Description (optional): ").strip()
        add_transaction(date, amount, cat_id, desc)
        print("Transaction added.")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


def handle_list_transactions():
    month = input("Filter by month (YYYY-MM, leave blank for all): ").strip() or None
    rows = list_transactions(month=month)
    if not rows:
        print("No transactions found.")
        return
    print(f"\n{'ID':<5} {'Date':<12} {'Amount':>10} {'Category':<16} Description")
    print("-" * 60)
    for r in rows:
        print(f"{r['id']:<5} {r['date']:<12} {r['amount']:>10.2f} {r['category']:<16} {r['description'] or ''}")


def handle_delete_transaction():
    try:
        tid = int(input("Transaction ID to delete: "))
        if delete_transaction(tid):
            print("Deleted.")
        else:
            print("Transaction not found.")
    except ValueError:
        print("Invalid ID.")


def handle_set_budget():
    categories = list_categories()
    print("\nExpense categories:")
    for c in categories:
        if c["type"] == "expense":
            print(f"  [{c['id']}] {c['name']}")
    try:
        cat_id = int(input("Category ID: "))
        month = input("Month (YYYY-MM): ").strip()
        limit = float(input("Budget limit: "))
        set_budget(cat_id, month, limit)
        print("Budget set.")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


def handle_budget_vs_actual():
    month = input("Month (YYYY-MM): ").strip()
    rows = get_budget_vs_actual(month)
    if not rows:
        print("No budgets found for that month.")
        return
    print(f"\n{'Category':<16} {'Budget':>10} {'Actual':>10} {'Remaining':>10}")
    print("-" * 50)
    for r in rows:
        flag = " ⚠️" if r["remaining"] < 0 else ""
        print(f"{r['category']:<16} {r['budget']:>10.2f} {r['actual']:>10.2f} {r['remaining']:>10.2f}{flag}")


def handle_summary():
    start = input("Start date (YYYY-MM-DD, leave blank for all): ").strip() or None
    end = input("End date (YYYY-MM-DD, leave blank for all): ").strip() or None
    s = summary_report(start, end)
    print(f"\n  Income:  {s['total_income']:>10.2f}")
    print(f"  Expense: {s['total_expense']:>10.2f}")
    print(f"  Balance: {s['balance']:>10.2f}")


def handle_list_categories():
    rows = list_categories()
    print(f"\n{'ID':<5} {'Type':<10} Name")
    print("-" * 30)
    for r in rows:
        print(f"{r['id']:<5} {r['type']:<10} {r['name']}")


def main():
    seed = "--seed" in sys.argv
    initialize_database(seed=seed)

    while True:
        print_menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            handle_add_transaction()
        elif choice == "2":
            handle_list_transactions()
        elif choice == "3":
            handle_delete_transaction()
        elif choice == "4":
            handle_set_budget()
        elif choice == "5":
            handle_budget_vs_actual()
        elif choice == "6":
            handle_summary()
        elif choice == "7":
            handle_list_categories()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
