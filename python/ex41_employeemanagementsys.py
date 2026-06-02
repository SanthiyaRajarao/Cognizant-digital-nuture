import json
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def to_dict(self):
        return {
            "id": self.emp_id,
            "name": self.name,
            "salary": self.salary
        }
def save_employees(emp_list):
    data = {}

    for emp in emp_list:
        data[emp.emp_id] = emp.to_dict()

    with open("emps.json", "w") as file:
        json.dump(data, file)

    return "Data saved successfully"


def load_employees():
    try:
        with open("emps.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return "No file found"


def main():
    e1 = Employee(101, "Santhiya", 60000)
    e2 = Employee(102, "Hycinth", 55000)

    employees = [e1, e2]

    print(save_employees(employees))
    print(load_employees())


main()