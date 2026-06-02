def add_expense():
    expenses = [100, 200, 150]
    print("Expenses before adding:", expenses)
    new_expense = int(input("Enter new expense amount: "))
    if new_expense <= 0:
        print("Invalid expense amount")
        return
    expenses.append(new_expense)
    print("Updated Expenses List:")
    for expense in expenses:
        print(expense)
add_expense()