def minmax(salary):
    minimum=min(salary)
    maximum=max(salary)
    print("Minimum Salary in the given list is ",minimum)
    print("Maximum Salary in the given list is ",maximum)

salary = list(map(int, input("Enter the salary: ").split()))
minmax(salary)
