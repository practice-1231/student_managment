import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="student_db",
    user="postgres",
    password="postgres",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER,
        email VARCHAR(150)
    )
""")

conn.commit()
cursor.close()
conn.close()