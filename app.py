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

def delete_student(name):
    if name in students:
        students.remove(name)
        print(f"{name} deleted successfully.")
    else:
        print("Student not found.")

delete_student("Ali")
view_students()