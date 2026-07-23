import psycopg2
#shimi shimi ai

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="student_db",
        user="postgres",
        password="postgres",
        port="5432"
    )

def add_student(name, age, email):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO students (name, age, email)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, age, email))
    conn.commit()

    cursor.close()
    conn.close()

    print("Student added successfully!")

def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return students