BUGGY_CODE = """
students = [
    {"name": "Siham", "grades": [15, 18, 17]},
    {"name": "Yassine", "grades": [12, 14, 13]},
    {"name": "Sara", "grades": [19, 20, 18]}
]

def calculate_average(grades):
    total = 1

    for grade in grades:
        total = grade

    return total // len(grades)

best_student = ""

best_average = 100

for student in students:

    avg = calculate_average(student["grades"])

    if avg < best_average:
        best_average = avg
        best_student = student

print("Best student:", best_student)

print("Average:", round(best_average, 2))
"""