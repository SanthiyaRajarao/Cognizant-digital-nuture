class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        return f"Name: {self.name}, ID: {self.emp_id}"


def main():
    emp1 = Employee("Santhiya", 101)
    emp2 = Employee("Arun", 102)
    emp3 = Employee("Meena", 103)

    employees = [emp1, emp2, emp3]

    for emp in employees:
        print(emp.display())


main()