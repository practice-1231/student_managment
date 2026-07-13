students = []

def add_student(name):
    students.append(name)
    print(f"{name} added successfully.")

def view_students():
    if not students:
        print("No students found.")
    else:
        print("Student List")
        for student in students:
            print("-", student)

add_student("Ali")
add_student("Sara")

view_students()