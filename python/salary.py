def net_salary(salary, tax_rate):
    if salary < 0:
        print("Invalid salary")
        return 
    
    if tax_rate < 0 or tax_rate > 1:
        print("Invalid tax rate (must be between 0 and 1)")
        return

    total_salary = salary - (tax_rate * salary)
    
    print(f"The net salary is {total_salary:.2f} rupees")

salary = float(input("Enter the salary: "))
tax = float(input("Enter the tax rate: ")) 
net_salary(salary, tax)
