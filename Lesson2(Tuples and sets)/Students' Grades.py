n = int(input())

students = {}


for _ in range(n):
    name, grade_as_str = tuple(input().split())
    grade = float(grade_as_str)
    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    formated_grades = [str(f"{grade:.2f}") for grade in grades]
    avg_grade = sum(grades)/len(grades)
    print(f"{name} -> {' '.join(formated_grades)} (avg: {avg_grade:.2f})")