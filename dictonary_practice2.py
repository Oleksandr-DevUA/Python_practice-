students = {
    "Alex": [90, 85, 72, 100],
    "Maria": [95, 98, 91, 88],
    "John": [60, 75, 80, 65],
    "Sasha": [100, 95, 90, 97],
    "Anna": [82, 84, 79, 91]
}

names = list(students.keys())
i = 0

averages = {}
best_average = 0
best_student = None
excellent_students = {}
low_grade_students = {}

while i < len(names):
    name = names[i]
    grades = students[name]

    j = 0
    total = 0
    has_low_grade = False

    # 1. Рахуємо суму оцінок
    while j < len(grades):
        total += grades[j]

        if grades[j] < 70:
            has_low_grade = True

        j += 1

    
    average = total / len(grades)
    averages[name] = average

    
    if average > best_average:
        best_average = average
        best_student = name

    
    if average >= 90:
        excellent_students[name] = average

    
    if has_low_grade:
        low_grade_students[name] = grades

    i += 1


max_grades = students.get("Max")

print("Середні бали:", averages)
print("Найкращий студент:", best_student)
print("Його середній бал:", best_average)
print("Відмінники:", excellent_students)
print("Студенти з оцінками нижче 70:", low_grade_students)
print("Оцінки Max:", max_grades)