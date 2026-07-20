from database import add_student

def test_insert_student():
    add_student("John", 20, "john@example.com")