import csv

def process_csv():
    try:
        with open("employees.csv", "r") as file:
            reader = csv.DictReader(file)
            employees = list(reader)

        for emp in employees:
            emp["salary"] = int(emp["salary"])

        high_salary_employees = [
            emp for emp in employees if emp["salary"] > 50000
        ]

        salaries = [emp["salary"] for emp in employees]
        avg_salary = sum(salaries) / len(salaries)

        print("All Employees:")
        for emp in employees:
            print(emp)

        print("\nEmployees with salary > 50000:")
        for emp in high_salary_employees:
            print(emp)

        print("\nAverage Salary:", avg_salary)

    except FileNotFoundError:
        print("employees.csv file not found")
    except Exception as e:
        print("Error:", e)

process_csv()