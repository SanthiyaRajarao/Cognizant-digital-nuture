def get_salary(dept, emp_name):
    employees = {
        "AI": {
            "Santhiya": 60000,
            "Arun": 55000
        },
        "IT": {
            "Kiran": 70000,
            "Meena": 65000
        }
    }
    if dept not in employees:
        return "Department not found"
    if emp_name not in employees[dept]:
        return "Employee not found"
    return employees[dept][emp_name]
print(get_salary("AI", "Santhiya"))