import statistics

def process_sales():
    try:
        file = open("sales.txt", "r")
        data = file.read().split()
        file.close()

        sales = []

        for value in data:
            try:
                sales.append(float(value))
            except ValueError:
                print("Skipping invalid data:", value)

        if len(sales) == 0:
            print("No valid sales data found")
            return

        mean_value = statistics.mean(sales)
        median_value = statistics.median(sales)

        print("Sales Data:", sales)
        print("Mean:", mean_value)
        print("Median:", median_value)

    except FileNotFoundError:
        print("File not found: sales.txt")
    except Exception as e:
        print("Error occurred:", e)

process_sales()