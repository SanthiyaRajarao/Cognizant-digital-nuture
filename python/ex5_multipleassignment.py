def coord(coordinates):
    if len(coordinates) != 2: 
        print("Invalid coord")
        return
    
    x, y = coordinates
    print(f"The coordinates are: X={x:.2f}, Y={y:.2f}")

pt1 = float(input("Enter the first coordinate: "))
pt2 = float(input("Enter the second coordinate: "))

coord([pt1, pt2])
