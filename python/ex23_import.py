import math

def calc():
    radius=float(input("Enter the radius: "))
    area=math.pi*(radius**2)
    print(f"{area:.2f}")

calc()