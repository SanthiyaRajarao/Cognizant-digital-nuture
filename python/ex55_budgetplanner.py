import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        if amount <= 0:
            return "Invalid amount"
        self.spent += amount

    def status(self):
        if self.spent > self.limit:
            return f"{self.name}: Budget exceeded!"
        return f"{self.name}: Within budget"


class BudgetPlanner:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def show_status(self):
        print("\n--- Budget Status ---")
        for c in self.categories:
            print(c.status())

    def show_chart(self):
        names = [c.name for c in self.categories]
        spent = [c.spent for c in self.categories]

        plt.pie(spent, labels=names, autopct="%1.1f%%")
        plt.title("Monthly Budget Distribution")
        plt.show()


def main():
    planner = BudgetPlanner()

    food = Category("Food", 5000)
    travel = Category("Travel", 3000)
    shopping = Category("Shopping", 4000)

    food.add_expense(4500)
    travel.add_expense(3500)
    shopping.add_expense(2000)

    planner.add_category(food)
    planner.add_category(travel)
    planner.add_category(shopping)

    planner.show_status()
    planner.show_chart()


main()