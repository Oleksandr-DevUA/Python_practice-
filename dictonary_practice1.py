
students = {
    "Dima": [80, 95, 70, 85],
    "Olga": [100, 92, 96, 98],
    "Max": [55, 68, 75, 80],
    "Ira": [88, 90, 84, 94],
    "Nick": [70, 65, 60, 75]
}

names = list(students.keys())
averages = {}
best_average = 0
best_student = None
excellent_students = {}
low_grade_students = {}

for name in names:
    grades = students[name]
    total = 0
    has_low_grade = False

    for rating in grades:
        total += rating

        if rating < 70:
            has_low_grade = True

    average = total / len(grades)
    averages[name] = average

    if average > best_average:
        best_average = average
        best_student = name

    if average >= 90:
        excellent_students[name] = average

    if has_low_grade:
        low_grade_students[name] = grades

max_grades = students.get("Dima")

print("Середні бали:", averages)
print("Найкращий студент:", best_student)
print("Його середній бал:", best_average)
print("Відмінники:", excellent_students)
print("Студенти з оцінками нижче 70:", low_grade_students)
print("Оцінки Dima:", max_grades)
