#with open("sales.txt", "w") as file:
#   file.write("100 200 150 300 250 400 350")
'''
with open("db.ini", "w") as file:
    file.write("""[database]
host = localhost
port = 3306
username = admin
password = root123
dbname = testdb
""")
    print("Successfull")

with open("employees.csv", "w") as file:
    file.write("name,salary\n")
    file.write("Alice,60000\n")
    file.write("Bob,45000\n")
    file.write("Charlie,70000\n")

'''
import csv

with open("expenses.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["date", "amount", "category"])
    writer.writerow(["2026-06-01", 200, "food"])
    writer.writerow(["2026-06-02", 500, "travel"])
    writer.writerow(["2026-06-05", 150, "food"])
    writer.writerow(["2026-06-10", 1000, "rent"])
    writer.writerow(["2026-06-15", 300, "travel"])
    print("Successfull")
