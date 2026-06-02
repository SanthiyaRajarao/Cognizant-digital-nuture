def update_employee():
    emp1 = {"id": 101, "name": "John", "salary": 30000}
    emp2 = {"dept": "IT", "location": "Chennai"}

    if not isinstance(emp1, dict) or not isinstance(emp2, dict):
        print("Invalid input")
        return

    emp1.update(emp2)

    print("Updated Employee Data:")
    for key, value in emp1.items():
        print(key, ":", value)

update_employee()