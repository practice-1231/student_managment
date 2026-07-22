from database import view_students

def test_view_students():
    students = view_students()
    assert students is not None