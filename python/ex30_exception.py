def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result:.2f}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

x = float(input("Enter numerator: "))
y = float(input("Enter denominator: "))
safe_divide(x, y)
