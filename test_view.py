from database import view_students

students = view_students()

for student in students:
    print(student)