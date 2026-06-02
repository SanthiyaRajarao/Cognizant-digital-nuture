def get_coordinates():
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))

    coordinates = (x, y)
    if len(coordinates) != 2:
        return "Invalid coordinates"
    print("Coordinates:", coordinates)

get_coordinates()