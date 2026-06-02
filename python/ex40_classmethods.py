class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    @classmethod
    def from_string(cls, data):
        name, salary = data.split(",")

        if not salary.isdigit():
            return "Invalid salary"

        return cls(name, int(salary))


def main():
    emp = Employee.from_string("Santhiya,75000")
    print(emp.display())


main()