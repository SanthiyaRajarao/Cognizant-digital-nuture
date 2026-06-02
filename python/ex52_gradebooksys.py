import json

# Student data structure:
# student_name -> list of grades

def calculate_gpa(grades):
    if not grades:
        return 0

    return sum(grades) / len(grades)


def add_student_grade(data, name, grade):
    if name not in data:
        data[name] = []

    if 0 <= grade <= 100:
        data[name].append(grade)
    else:
        print("Invalid grade ignored")


def class_average(data):
    all_grades = []

    for grades in data.values():
        all_grades.extend(grades)

    if not all_grades:
        return 0

    return sum(all_grades) / len(all_grades)


def save_data(data, filename="grades.json"):
    with open(filename, "w") as file:
        json.dump(data, file)


def load_data(filename="grades.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def main():
    students = load_data()

    add_student_grade(students, "Santhiya", 85)
    add_student_grade(students, "Hycinth", 90)
    add_student_grade(students, "Roshini", 78)

    print("GPA Santhiya:", calculate_gpa(students["Santhiya"]))
    print("Class Average:", class_average(students))

    save_data(students)


main()