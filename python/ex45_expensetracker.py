import csv
from datetime import datetime

def expense_tracker():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)

        current_month = datetime.now().month
        current_year = datetime.now().year

        for exp in expenses:
            exp["amount"] = float(exp["amount"])

        filtered_expenses = [
            exp for exp in expenses
            if datetime.strptime(exp["date"], "%Y-%m-%d").month == current_month
            and datetime.strptime(exp["date"], "%Y-%m-%d").year == current_year
        ]

        category_totals = {}

        for exp in filtered_expenses:
            cat = exp["category"]
            category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

        print("Filtered Expenses (Current Month):")
        for exp in filtered_expenses:
            print(exp)

        print("\nCategory-wise Total:")
        for cat, total in category_totals.items():
            print(cat, ":", total)

    except FileNotFoundError:
        print("expenses.csv file not found")
    except Exception as e:
        print("Error:", e)

expense_tracker()