class TemperatureConverter:

    def c_to_f(self, c):
        return (c * 9/5) + 32

    def f_to_c(self, f):
        return (f - 32) * 5/9

    def c_to_k(self, c):
        return c + 273.15

    def k_to_c(self, k):
        return k - 273.15


def main():
    converter = TemperatureConverter()

    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Enter choice (1-4): ")

    try:
        temp = float(input("Enter temperature: "))

        if choice == "1":
            print("Result:", round(converter.c_to_f(temp), 2))

        elif choice == "2":
            print("Result:", round(converter.f_to_c(temp), 2))

        elif choice == "3":
            print("Result:", round(converter.c_to_k(temp), 2))

        elif choice == "4":
            print("Result:", round(converter.k_to_c(temp), 2))

        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid temperature input")


main()