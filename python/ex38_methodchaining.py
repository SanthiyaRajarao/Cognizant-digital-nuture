class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def set_salary(self, salary):
        if salary <= 0:
            self.salary = 0
        else:
            self.salary = salary
        return self

    def apply_raise(self, percent):
        if percent < 0:
            percent = 0
        self.salary += self.salary * (percent / 100)
        return self

    def display(self):
        print("Employee:", self.name)
        print("Final Salary:", self.salary)
        return self


def main():
    emp = Employee("Santhiya")
    emp.set_salary(50000).apply_raise(10).display()


main()